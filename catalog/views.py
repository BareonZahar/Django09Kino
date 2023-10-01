from django.shortcuts import render
from .models import *
# Create your views here.


def index(req):
    numbreed = Breed.objects.all().count()
    numdoctor = Doctors.objects.all().count()
    numservis = Services.objects.filter().count()
    data = {'k1':numbreed,'k2':numdoctor,'k3':numservis}
    return render(req,'index.html',context=data)


from django.views import generic


class Vetclinlist(generic.ListView):
    model = Vet_clinic


# class VetcDetail(generic.DetailView):
#     model = Vet_clinic

from django.http import HttpResponse

def info(req,id):
    vetc = Vet_clinic.objects.get(id=id)
    # serv = Vet_clinic.objects.get(id=id)
    # vet = Vet_clinic.objects.filter(serv)
    # k5 = ''
    # for i in vet:
    #     k5 = i.animal_card
    # data = {'k5':k5}
    return HttpResponse(vetc.services)