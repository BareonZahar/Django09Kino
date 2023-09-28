from django.db import models

# Create your models here.


class Doctors(models.Model):
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    name = models.CharField(max_length=15, verbose_name='Имя')
    profesh = models.CharField(max_length=20, verbose_name='Профессия')

    def __str__(self):
        return f'{self.surname},{self.name},{self.profesh}'


class Status(models.Model):
    VIBOR = (('хирург','хирург'),('стоматолог','стоматолог'),
             ('терапевт','терапевт'),('дерматолог','дерматолог'))
    prof = models.CharField(max_length=20, choices=VIBOR, verbose_name='Профессия')

    def __str__(self):
        return f'{self.prof}'


class Services(models.Model):
    # first_inspection = models.TextField(max_length=500, verbose_name='Первичный осмотр')
    # laboratory_tests = models.TextField(max_length=500, verbose_name='Лабораторные исследования')
    # cupping = models.TextField(max_length=500, verbose_name='Купирование')
    # haircuts = models.TextField(max_length=500, verbose_name='Стрижка')
    # nail_trimming = models.TextField(max_length=500, verbose_name='Обрезка ногтей')
    # delivery_reception = models.TextField(max_length=500, verbose_name='Прием родов')
    # stomat_ment = models.TextField(max_length=500, verbose_name='Стомотологическое лечение')
    VIB = (('Первичный осмотр','Первичный осмотр'),('Лабораторные исследования','Лабораторные исследования'),
           ('Купирование','Купирование'),('Стрижка','Стрижка'),('Обрезка ногтей','Обрезка ногтей'),
           ('Прием родов','Прием родов'),('Стомотологическое лечение','Стомотологическое лечение'))
    servis = models.CharField(null=True,blank=True,max_length=30, choices=VIB, verbose_name='Услуги')

    def __str__(self):
        return f'{self.servis}'


# class Prices(models.Model):
    # first_inspection = models.IntegerField(verbose_name='Первичный осмотр')
    # laboratory_tests = models.IntegerField(verbose_name='Лабораторные исследования')
    # cupping = models.IntegerField(verbose_name='Купирование')
    # haircuts = models.IntegerField(verbose_name='Стрижка')
    # nail_trimming = models.IntegerField(verbose_name='Обрезка ногтей')
    # delivery_reception = models.IntegerField(verbose_name='Прием родов')
    # stomat_ment = models.IntegerField(verbose_name='Стомотологическое лечение')
    #
    # def __str__(self):
    #     return f'{self.first_inspection},{self.laboratory_tests},{self.cupping},' \
    #            f'{self.haircuts},{self.nail_trimming},{self.delivery_reception},{self.stomat_ment}'
    # Viborprice = (('350$','Первичный осмотр'),('750$','Лабораторные исследования'),
    #               ('1200$','Купирование'),('450$','Стрижка'),('600$','Обрезка ногтей'),
    #               ('1500$','Прием родов'),('550$','Стомотологическое лечение'))
    # price = models.CharField(null=True,blank=True,max_length=30, choices=Viborprice, verbose_name='Стоимость')
    # pric = models.IntegerField(null=True,verbose_name='Стоимость услуги')
    #
    # def __str__(self):
    #     return self.pric


class Animal_card(models.Model):
    nickname = models.CharField(max_length=20, verbose_name='Кличка питомца')
    breed = models.CharField(max_length=20, verbose_name='Порода')
    age = models.IntegerField(verbose_name='Возраст')
    height = models.IntegerField(verbose_name='Рост')
    weight = models.IntegerField(verbose_name='Вес')

    def __str__(self):
        return f'{self.breed},{self.nickname}'


class Owner_card(models.Model):
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    name = models.CharField(max_length=20, verbose_name='Имя')
    address = models.CharField(max_length=50, verbose_name='Адрес')
    email = models.EmailField(max_length=30, verbose_name='Почта')
    telefon = models.CharField(max_length=12, verbose_name='Телефон')
    breed = models.CharField(max_length=20, verbose_name='Порода питомца')
    nickname = models.CharField(max_length=20, verbose_name='Кличка')

    def __str__(self):
        return f'{self.surname},{self.breed},{self.nickname}'


class Breed(models.Model):
    breed = models.CharField(max_length=20, verbose_name='Порода питомца')

    def __str__(self):
        return f'{self.breed}'


class Data(models.Model):
    data = models.DateField()

    def __str__(self):
        return f'{self.data}'


class Vet_clinic(models.Model):
    doctor = models.ManyToManyField(Doctors, verbose_name='Врач')
    services = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Услуги')
    # prices = models.ForeignKey(Prices, on_delete=models.SET_NULL,null=True, verbose_name='Цена услуг')
    owner_card = models.ForeignKey(Owner_card, on_delete=models.CASCADE, verbose_name='Владелец питомца')
    animal_card = models.ForeignKey(Animal_card, on_delete=models.CASCADE, verbose_name='Питомец')
    # servis_price = models.DecimalField(decimal_places=3,max_digits=9, verbose_name='Стоимость услуг')
    breeds = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='Породы животных')
    data = models.ForeignKey(Data, on_delete=models.CASCADE, verbose_name='Дата')
    status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=1, verbose_name='Профессия')

    def __str__(self):
        return f'{self.doctor}'

    def display_doctors(self):
        res = ''
        for a in self.doctor.all():
            res += a.surname+' '
        return res
    display_doctors.short_description = 'Врач'



