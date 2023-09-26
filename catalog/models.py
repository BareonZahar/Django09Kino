from django.db import models

# Create your models here.


class Doctors(models.Model):
    surname = models.CharField(max_length=20)
    name = models.CharField(max_length=15)
    profesh = models.CharField(max_length=20)

    def __str__(self):
        return self.surname, self.name, self.profesh


class Status(models.Model):
    VIBOR = (('хирург','хирург'),('стоматолог','стоматолог'),
             ('терапевт','терапевт'),('дерматолог','дерматолог'))
    prof = models.CharField(max_length=20, choices=VIBOR)

    def __str__(self):
        return self.prof


class Services(models.Model):
    first_inspection = models.TextField(max_length=500)
    laboratory_tests = models.TextField(max_length=500)
    cupping = models.TextField(max_length=500)
    haircuts = models.TextField(max_length=500)
    nail_trimming = models.TextField(max_length=500)
    delivery_reception = models.TextField(max_length=500)
    stomat_ment = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.first_inspection},{self.laboratory_tests},{self.cupping},' \
               f'{self.haircuts},{self.nail_trimming},{self.delivery_reception},{self.stomat_ment}'


class Prices(models.Model):
    first_inspection = models.IntegerField()
    laboratory_tests = models.IntegerField()
    cupping = models.IntegerField()
    haircuts = models.IntegerField()
    nail_trimming = models.IntegerField()
    delivery_reception = models.IntegerField()
    stomat_ment = models.IntegerField()

    def __str__(self):
        return f'{self.first_inspection},{self.laboratory_tests},{self.cupping},' \
               f'{self.haircuts},{self.nail_trimming},{self.delivery_reception},{self.stomat_ment}'


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


class Breed(models.Model):
    breed = models.CharField(max_length=20)

    def __str__(self):
        return self.breed


class Data(models.Model):
    data = models.DateField()

    def __str__(self):
        return self.data


class Vet_clinic(models.Model):
    doctor = models.ManyToManyField(Doctors)
    services = models.ForeignKey(Services, on_delete=models.SET_NULL,null=True)
    prices = models.ForeignKey(Prices, on_delete=models.SET_NULL,null=True)
    owner_card = models.ForeignKey(Owner_card, on_delete=models.CASCADE)
    animal_card = models.ForeignKey(Animal_card, on_delete=models.CASCADE)
    servis_price = models.DecimalField(decimal_places=3,max_digits=9)
    breeds = models.ForeignKey(Breed, on_delete=models.CASCADE)
    data = models.ForeignKey(Data, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.doctor



