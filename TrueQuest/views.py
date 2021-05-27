from django.conf import settings
from django.conf.global_settings import STATIC_ROOT
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import QuestRoom, Image, RoomReservation
from django.core.mail import send_mail



# someone clicks the link to change to English
from .settings import DEFAULT_RECIPIENT


def index(request):
    request = sessions(request)
    quest_rooms = QuestRoom.objects.all()
    images = Image.objects.all().filter(is_main_image=1)
    print(images)
    return render(request, 'index.html', {'quest_rooms': quest_rooms, 'images': images})


def room(request, room_id, message=None):
    request = sessions(request)
    quest_room = QuestRoom.objects.get(pk=room_id)
    image = Image.objects.get(quest_id=room_id, is_main_image=1)
    return render(request, 'room.html', {'quest_room': quest_room, 'image_url': image.image.url})


def book_room(request, room_id):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        date = request.POST['date']
        foo_instance = RoomReservation.objects.create(reservation_date=date,
                                                      quest_room_id=room_id,
                                                      phone_number=phone,
                                                      name=name)
        message = "Дякую за ваше замовлення, очікуйте смс підтвердження"
        send_email("ostapko220@gmail.com")
        send_mail(
            'Бронювання кімнати ' + str(room_id),
            name + '\n' + phone + '\n' + date,
            'trueQuest@quest.com',
            [DEFAULT_RECIPIENT],
            fail_silently=False,
        )
        # truequest.mail@gmail.com
        # SIR1uY8y4Wzd

        return redirect("room", room_id)


def sessions(_request):
    if 'lang' in _request.session.keys():
        print(_request.session['lang'])
    else:
        _request.session['lang'] = "ua"
    return _request


def change_language(request, language):
    # language = request.POST['language']
    request.session['lang'] = language
    return redirect("index")


def send_email(recipient):
    send_mail(
        'Бронювання кімнати',
        'Here is the message.',
        'trueQuest@quest.com',
        [recipient],
        fail_silently=False,
    )


def franchise(request):
    return render(request, 'franchise.html')


def about(request):
    return render(request, 'about.html')
