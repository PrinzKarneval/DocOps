from django.db import models



class Label(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name


class Insurance(Label):
    pass


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    street_no = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    insurance = models.ForeignKey(Insurance, models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
