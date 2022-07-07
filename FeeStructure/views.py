from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def dashboard(request):
    return HttpResponse("Dashboard")


def enter_data(request):
    if request.method == "POST":
        receipt_number = request.POST["receipt-number"]
        received_sum = request.POST["received-sum"]
        date = request.POST['submission-date']
        student_name = request.POST['student-name']
        enrolment_number = request.POST['enrolment-number']
        semester = request.POST['semester-select']

        print(student_name, semester)
        return HttpResponse("SUCCESS")
    else:
        return redirect('Dashboard')