from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from FeeStructure.models import FeeFormat

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
        stream = request.POST["stream-select"]
        payment_mode = request.POST["payment-mode"]
        transaction_number = request.POST['transaction-number']
        cheque_date = request.POST["cheque-date"]

        
        print(receipt_number, received_sum, date, student_name, enrolment_number, semester, stream, payment_mode, transaction_number, cheque_date)
        
        student_data = FeeFormat(
            receipt_number= receipt_number, received_sum= received_sum, date= date, 
            student_name=student_name, enrolment_number= enrolment_number, semester= semester, 
            stream= stream, payment_mode= payment_mode, transaction_number= transaction_number,
            cheque_date= cheque_date
        )

        student_data.enrolment_number= enrolment_number
        student_data.save()

        return HttpResponse("SUCCESS")

        # redirect('insert-data')
    else:
        return render(request, "FeeStructure/dashboard.html")