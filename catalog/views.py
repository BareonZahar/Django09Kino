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


from django.http import HttpResponse

def info(req,id):
    serv = Vet_clinic.objects.get(id=id)
    return HttpResponse(serv.services)