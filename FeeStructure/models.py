from django.db import models
# Create your models here.

class FeeFormat(models.Model):
    SEMESTERS = (
        ("SEM1", 'Semester 1'),
        ("SEM2", 'Semester 2'),
        ("SEM3", 'Semester 3'),
        ("SEM4", 'Semester 4'),
        ("SEM5", 'Semester 5'),
        ("SEM6", 'Semester 6'),
        ("SEM7", 'Semester 7'),
        ("SEM8", 'Semester 8'),
    )

  

    receipt_number = models.IntegerField(default= 0)
    received_sum = models.IntegerField(default= 0)
    date = models.DateField()
    student_name = models.CharField(max_length= 80, default= "Student Name")
    enrolment_number = models.IntegerField(default= 0)
    semester = models.CharField(max_length= 11, choices= SEMESTERS, default= SEMESTERS[6])
    Stream = models.CharField(max_length= 10, default="Stream")
    payment_mode = models.CharField(max_length= 10, default= "Payment Mode")
    transaction_number = models.BigIntegerField(default= 0)
    cheque_date = models.DateField()
    