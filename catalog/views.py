from django.shortcuts import render
from .models import *
# Create your views here.
def index(req):
    numbreed = Breed.objects.all().count()
    numdoctor = Doctors.objects.all().count()
    numservis = Vet_clinic.objects.filter(services__vet_clinic=1).count()
    data = {'k1':numbreed,'k2':numdoctor,'k3':numservis}
    return render(req,'index.html',context=data)