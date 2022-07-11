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

    STREAMS = (
        ("ICT", "Information and Communication Technology"), 
        ("CIVIL", "Civil"),
        ("ELE", "Electrical"), 
        ("CS", "CS"),
    )
  
    PAYMENT_METHODS = (
        ("CHEQUE", "Cheque"),
        ("DRAFT", "Draft"),
        ("PAYTM", "Paytm"),
    )
    receipt_number = models.BigIntegerField(default= 0)
    received_sum = models.IntegerField(default= 0)
    date = models.DateField()
    student_name = models.CharField(max_length= 80, default= "Student Name")
    enrolment_number = models.CharField(max_length=12)
    semester = models.CharField(max_length= 11, choices= SEMESTERS, default= SEMESTERS[6])
    stream = models.CharField(max_length= 10, choices=STREAMS, default=STREAMS[0])
    payment_mode = models.CharField(max_length= 10, choices=PAYMENT_METHODS, default= PAYMENT_METHODS[2])
    transaction_number = models.BigIntegerField(default= 0)
    cheque_date = models.DateField()
    
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now= True)