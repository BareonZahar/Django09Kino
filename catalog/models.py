from django.db import models

# Create your models here.
class Doctors(models.Model):
    surgeon = models.CharField(max_length=30)
    dentist  = models.CharField(max_length=30)
    therapist = models.CharField(max_length=30)
    dermatologist = models.CharField(max_length=30)


    def __str__(self):
        return self.surgeon,self.dentist,self.dermatologist


class Services(models.Model):
    first_inspection = models.TextField(max_length=500)
    laboratory_tests = models.TextField(max_length=500)
    cupping = models.TextField(max_length=500)
    haircuts = models.TextField(max_length=500)
    nail_trimming = models.TextField(max_length=500)
    delivery_reception = models.TextField(max_length=500)
    stomat_ment = models.TextField(max_length=500)



    def __str__(self):
        return self.first_inspection

class Prices(models.Model):
    first_inspection = models.IntegerField()
    laboratory_tests = models.IntegerField()
    cupping = models.IntegerField()
    haircuts = models.IntegerField()
    nail_trimming = models.IntegerField()
    delivery_reception = models.IntegerField()
    stomat_ment = models.IntegerField()



    def __str__(self):
        return self.first_inspection


class Animal_card(models.Model):
    nickname = models.CharField(max_length=20)
    breed = models.CharField(max_length=20)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()



    def __str__(self):
        return self.nickname


class Owner_card(models.Model):
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    telefon = models.IntegerField()
    breed = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)



    def __str__(self):
        return self.surname


class Status(models.Model):
    Vibor = (('бесплатно','бесплатно'),('стандартная','стандартная'),('премиум','премиум'))
    name = models.CharField(max_length=60)



    def __str__(self):
        return self.name


class Vet_clinic(models.Model):
    title = models.CharField(max_length=30)
    doctor = models.ManyToManyField(Doctors)
    services = models.ForeignKey(Services, on_delete=models.SET_NULL,null=True)
    owner_card = models.ForeignKey(Owner_card, on_delete=models.CASCADE)
    animal_card = models.ForeignKey(Animal_card, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2,max_digits=9)
    contacts = models.IntegerField()
    subscription = models.ForeignKey(Status,on_delete=models.SET_NULL,default=1)



    def __str__(self):
        return self.title



