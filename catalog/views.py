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


def status(req):
    k1 = Status.objects.all()
    data = {'podpiska':k1}
    return render(req,'podpiska.html',data)

def prosmotr(req,id1,id2,id3):
    print(id1,id2,id3)
    mas = ['бесплатно','базовая','супер']  #  kino id2
    mas2 = ['free','based','super']   #  user  id3  status
    if id3 != 0:
        status = User.objects.get(id=id3)  #  нашли юзера
        print(status)
        status = status.groups.all()  # нашли его подписки
        print(status)
        status = status[0].id  #  нашли айди его подписки(она одна)
        print(status)
    else:
        if id3 == 0:
            status = 1
    if status >= id2:
        print('ok')
    else:
        print('nelzy')

    return render(req,'index.html')

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

class DirectorDetail(generic.DetailView):
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



