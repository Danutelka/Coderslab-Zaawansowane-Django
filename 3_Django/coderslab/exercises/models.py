from django.db import models
from django.core.exceptions import ValidationError


SCHOOL_CLASS = (
    (0, "1a"),
    (1, "1b"),
    (2, "2a"),
    (3, "2b"),
    (4, "3a"),
    (5, "3b"),
)

GRADES = (
    (1, "1"),
    (1.5, "1+"),
    (1.75, "2-"),
    (2, "2"),
    (2.5, "2+"),
    (2.75, "3-"),
    (3, "3"),
    (3.5, "3+"),
    (3.75, "4-"),
    (4, "4"),
    (4.5, "4+"),
    (4.75, "5-"),
    (5, "5"),
    (5.5, "5+"),
    (5.75, "6-"),
    (6, "6")
)

PIZZA_SIZES = (
    (1, "small"),
    (2, "medium"),
    (3, "large")
)

EXCHANGE = (
    (1, "PLNtoUSD"),
    (2, "USDtoPLN")
)

BACKGROUND = (
    (1, "black"),
    (2, "white"),
    (3, "red"),
    (4, "yellow"),
    (5, "blue")
)
# Create your models here.

def validate_teacher_name(value):
    if len(value.split()) != 2:
        raise ValidationError("nauczyciel powienien posiadac imie i nazwisko")

class SchoolSubject(models.Model):
    name = models.CharField(max_length=64, verbose_name="nazwa przedmiotu")
    teacher_name = models.CharField(max_length=64, verbose_name="nazwa nauczyciela",
    help_text="Nauczyciel powienien miec imie i nazwisko", validators=[validate_teacher_name])


class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name =  models.CharField(max_length=64)
    # year_of_birth = models.IntegerField(default=0)
    school_class = models.IntegerField(choices=SCHOOL_CLASS)
    grades = models.ManyToManyField(SchoolSubject, through="StudentGrades")

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name


class StudentGrades(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    school_subject = models.ForeignKey(SchoolSubject, on_delete=models.CASCADE)
    grade = models.FloatField(choices=GRADES)


class Toppings(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()

    def __str__(self):
        return "{} ({} zł)" .format(self.name, self.price)
    
class Pizza(models.Model):
    size = models.IntegerField(choices=PIZZA_SIZES)
    toppings = models.ManyToManyField(Toppings)

class PresenceList(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    day = models.DateField()
    present = models.BooleanField(default=False)

