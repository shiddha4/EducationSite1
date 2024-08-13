from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
import random
# Create your views here.
from django.http import JsonResponse
from django.contrib.auth.models import User
import random
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import students, classes, daysNumbers
# Create your views here.
from django.http import HttpResponse
from datetime import datetime
import pytz

from django.utils import timezone




def login(request):
    if request.method == 'POST':
        username = request.POST['userName']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/students')
        else:
           messages.error(request, 'Invalid credentials')
           return render(request, 'login.html')
    else:
        return render(request, 'login.html')

@login_required(login_url='/login')
def studen(request):

    return render(request, 'students.html', {"students":students.objects.all()})

@login_required(login_url='/login')
def add(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Belt = request.POST['Belt']
        Days = request.POST['Days']
        Date = request.POST['Date']
        Notes = request.POST['Notes']
        studentNew=students(name=Name , belt=Belt, days=Days,enrollDate=Date,notes=Notes)
        studentNew.save()




        return redirect("/students")

    else:
        return render(request,"add.html")
@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect("/login")
@login_required(login_url='/login')
def details(request,students_id):
    studets_in_db = students.objects.get(id=students_id)
    classes_in_db=classes.objects.filter(ssn=students_id).order_by("-date_today")
    return render(request,"studentsdetails.html",{"student":studets_in_db, "dates":classes_in_db, "number":classes_in_db.count()})
@login_required(login_url='/login')
def update(request, students_id):
    if (request.method=="GET"):
        studets_in_db = students.objects.get(id=students_id)
        return render(request, "update.html", {"student": studets_in_db})
    else:
        newStudent=students.objects.get(id=students_id)
        Name = request.POST['Name']
        Belt = request.POST['Belt']
        Days = request.POST['Days']
        Date = request.POST['Date']
        Notes = request.POST['Notes']
        newStudent.name=Name
        newStudent.belt=Belt
        newStudent.days=Days
        newStudent.enrollDate=Date
        newStudent.notes=Notes
        newStudent.save()
        link="/details/"+str(students_id)
        return redirect(link)

@login_required(login_url='/login')
def delete(request,students_id):
    student=students.objects.get(id=students_id)
    student.delete()
    return redirect("/students")

@login_required(login_url='/login')
def checkin(request):
    messages.get_messages(request).used = True
    return render(request, 'checkin.html', {"students":students.objects.all()})

def blank(request):
    return redirect("/login")

@login_required(login_url='/login')
def checkinStudent(request, students_id):

       # student_2 = classes.objects.get(id=students_id)

        student = classes.objects.filter(ssn=students_id)

        for student1 in student:
            date_today_1 = timezone.now()
            date=student1.date_today
            if(date.year==date_today_1.year  and date.month== date_today_1.month)   and  (date.day==date_today_1.day):
                link="/checkintwice/"+ str(students_id)
                return redirect(link)


        else:
            student_15 = students.objects.get(id=students_id)
            checkin_student = classes(name=student_15.name, date_today=timezone.now(), ssn=student_15)
            checkin_student.save()
            message=student_15.name+" had checked in. You may go to class!"
            messages.success(request, message)
            return redirect("/checkin")



@login_required(login_url='/login')
def checkintwice(request,students_id):
    if(request.method=="POST"):
        student = students.objects.get(id=students_id)
        checkin_student = classes(name=student.name, date_today=timezone.now(), ssn=student)
        checkin_student.save()
        message = student.name + " had checked in. You may go to class!"
        messages.success(request, message)
        return redirect("/checkin")
    else:
        return render(request,"checkintwice.html", {"id": students_id})



