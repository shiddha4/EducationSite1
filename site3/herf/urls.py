from django.urls import path

from . import views

urlpatterns = [
    path("login", views.login, name="login"),
    path("", views.blank, name="blank"),
    path("students/", views.studen, name="studen"),
    path("addstudents/", views.add, name="add"),
    path("logout/",views.logout, name="logout"),
    path("details/<int:students_id>", views.details, name="details"),
    path("update/<int:students_id>", views.update, name="update"),
    path("delete/<int:students_id>", views.delete, name="delete"),
    path("checkin/", views.checkin, name="checkin"),
    path("checkin/<int:students_id>", views.checkinStudent, name="checkinStudent"),
    path("checkintwice/<int:students_id>",  views.checkintwice, name="checkintwice"),

]
