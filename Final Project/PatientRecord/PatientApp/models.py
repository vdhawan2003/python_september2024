from django.db import models
class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    disease = models.CharField(max_length=200)
    admission_date = models.DateField()

    def __str__(self):
        return f'[id={self.id}, name={self.name}, age={self.age}, disease={self.disease}, admission_date={self.admission_date}]'