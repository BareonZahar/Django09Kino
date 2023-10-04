from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
# Create your views here.
def index(req):
    numkino = Kino.objects.all().count()
    numactor = Actor.objects.all().count()
    numfree = Kino.objects.filter(status__kino=1).count()
    # username = req.user.last_name if hasattr(req.user, 'last_name') else 'Гость'
    # username = req.user.first_name
    if req.user.username:
        username = req.user.first_name
    else:
        username = 'Гость'
    data = {'k1':numkino,'k2':numactor,'k3':numfree,'username':username}
    # user = User.objects.create_user('user2','user2@mail.ru','useruser')
    # user.first_name = 'Vlad'
    # user.last_name = 'Petrov'
    # user.save()
    return render(req,'index.html' , context=data)

# def allkino(req):
#     return redirect('home')


from django.views import generic


class Kinolist123(generic.ListView):
    model = Kino
    paginate_by = 2


class KinoDetail(generic.DetailView):
    model = Kino

class Actorlist(generic.ListView):
    model =Actor

class ActorDetail(generic.DetailView):
    model = Actor

class Directorlist(generic.ListView):
    model = Director

from django.http import HttpResponse
# def info(req,id):
#     film = Kino.objects.get(id=id)
#     return HttpResponse(film.title)
# def proactor(req):
#     name = Actor.objects.all()
#     # gim = ''
#     # for i in name:
#     #     gim = i.fname +'  ' +i.lname
#     #     # gam
#     #     print(gim)
#     data = {'k1':name}
#     return render(req,'new.html',context=data)
#



