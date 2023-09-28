from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Doctors)
admin.site.register(Status)
admin.site.register(Services)
# admin.site.register(Prices)
# admin.site.register(Animal_card)
# admin.site.register(Owner_card)
admin.site.register(Breed)
admin.site.register(Data)
# admin.site.register(Vet_clinic)

class Doctorsadmin(admin.ModelAdmin):
    list_display = ('surname','name','profesh')
    list_display_links = ('surname','profesh')
admin.site.register(Doctors,Doctorsadmin)


class Animal_cardadmin(admin.ModelAdmin):
    list_display = ('nickname','breed','age','height','weight')
admin.site.register(Animal_card,Animal_cardadmin)


class Owner_cardadmin(admin.ModelAdmin):
    list_display = ('surname','name','nickname','breed')
    list_display_links = ('surname','breed')
admin.site.register(Owner_card,Owner_cardadmin)


class Vet_clinicadmin(admin.ModelAdmin):
    list_display = ('services','animal_card','status','display_doctors')
    list_filter = ('status','breeds','services')
    fieldsets = (('Об услугах',{'fields':('doctor','services')}),
                 ('О животных',{'fields':('animal_card','owner_card')}),
                 ('Остальное',{'fields':('status','data','breeds')}))
admin.site.register(Vet_clinic,Vet_clinicadmin)