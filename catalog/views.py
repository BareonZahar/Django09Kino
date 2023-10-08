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
        # print(req.user.first_name,'#',req.user.id)  #   Для проверки что выводит
    else:
        username = 'Гость'
        # print(req.user.id)   #  Для проверки что выводит
    data = {'k1':numkino,'k2':numactor,'k3':numfree,'username':username}
    # user = User.objects.create_user('user2','user2@mail.ru','useruser')
    # user.first_name = 'Vlad'  #  ------------Програмно регистрировали пользователя -------------
    # user.last_name = 'Petrov'
    # user.save()
    return render(req,'index.html' , context=data)


def ganry(req):
    k2 = Genre.objects.all()
    print(k2, 'нет ничего')
    data = {'ganry':k2}
    return render(req,'index.html',data)

def pro_ganry(req):
    k1 = Genre.objects.all()
    for i in k1:
        k2 = ''
        data = {}
        for kino in i.kino_set.all():
            k2 = kino
        data = {'k2':k2}
        return render(req, 'new.html', data)



def status(req):
    k1 = Status.objects.all()
    print(k1)
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
    paginate_by = 2

class ActorDetail(generic.DetailView):
    model = Actor

class Directorlist(generic.ListView):
    model = Director
    paginate_by = 7

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



