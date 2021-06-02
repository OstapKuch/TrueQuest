import json
from datetime import datetime, date, timedelta

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import QuestRoom, Image, RoomReservation
from django.core.mail import send_mail
from .settings import DEFAULT_RECIPIENT, DEFAULT_SENDER


def index(request):
    request = sessions(request)
    quest_rooms = QuestRoom.objects.all()
    images = Image.objects.all().filter(is_main_image=1)
    return render(request, 'index.html', {'quest_rooms': quest_rooms, 'images': images})


def room(request, room_id):
    current_date = date.today()
    request = sessions(request)
    quest_room = QuestRoom.objects.get(pk=room_id)
    image = Image.objects.get(quest_id=room_id, is_main_image=1)
    current_date, room_hours = fill_reservations_list(quest_room, current_date)
    return render(request, 'room.html', {'quest_room': quest_room,
                                         'image_url': image.image.url,
                                         'reservations': room_hours,
                                         'current_date': current_date.strftime('%Y-%m-%d'),
                                         'max_date': current_date + timedelta(days=14)})


def franchise(request):
    return render(request, 'franchise.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contact.html')


def leave_feedback(request):
    feedback = request.POST['feedback']
    send_email(DEFAULT_RECIPIENT, "Відгук", feedback)
    return redirect("index")


def get_reservations(request):
    room_id = int(request.GET['room_id'])
    chosen_date = request.GET['chosen_date']
    quest_room = QuestRoom.objects.get(pk=room_id)
    date_list = chosen_date.split('-')
    date_object = date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    current_date, room_hours = fill_reservations_list(quest_room, date_object)
    return HttpResponse(json.dumps(room_hours), content_type='application/json')


def fill_reservations_list(quest_room, chosen_date):
    current_datetime = datetime.now()
    print(current_datetime)
    reservations = RoomReservation.objects.filter(
        reservation_date__range=[str(chosen_date) + " 00:00:00", str(chosen_date + timedelta(days=1)) + " 00:00:00"],
        quest_room_id=quest_room.pk).exclude(status="CANCELED")
    duration_min = (quest_room.room_closes_at.hour * 60 + quest_room.room_closes_at.minute) - (
            quest_room.room_opens_at.hour * 60 + quest_room.room_closes_at.minute)
    count_quests_per_day = int(duration_min / quest_room.quest_duration)
    room_hours = []
    quest_time_finish = quest_room.room_opens_at
    for i in range(0, count_quests_per_day):
        room_available = "1"
        if current_datetime.time() > quest_time_finish and date.today() == chosen_date:
            room_available = "0"
        for i in range(0, len(reservations)):
            if reservations[i].reservation_date.hour == quest_time_finish.hour:
                room_available = "0"
        quest_start_time = quest_time_finish
        quest_time_finish = add_minutes(quest_time_finish, quest_room.quest_duration)
        room_hours.append(["{:d}:{:02d}".format(quest_start_time.hour, quest_start_time.minute),
                           "{:d}:{:02d}".format(quest_time_finish.hour, quest_time_finish.minute), room_available])
    return chosen_date, room_hours


def book_room(request, room_id):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        reservation_date = request.POST['date']
        time = request.POST['chosen_time']
        reservation_datetime = reservation_date + " " + time + ":00"
        print(reservation_datetime)
        foo_instance = RoomReservation.objects.create(reservation_date=reservation_datetime,
                                                      quest_room_id=QuestRoom.objects.get(pk=room_id),
                                                      phone_number=phone,
                                                      name=name,
                                                      status="PENDING")
        message = "Дякую за ваше замовлення, адміністратор зв'яжеться з вами"
        send_confirmation_email(reservation_datetime, name, phone, QuestRoom.objects.get(pk=room_id).title,
                                foo_instance.pk)
        return redirect("room", room_id)


def send_confirmation_email(reservation_datetime, name, phone, room_id, reservation_id):
    title = "Бронювання №" + str(reservation_id)
    message = "Кімната " + str(room_id) \
              + "\nЗамовив: " + name \
              + "\nТел: " + phone \
              + "\nДата: " + reservation_datetime
    send_email(DEFAULT_RECIPIENT, title, message)


def sessions(_request):
    if 'lang' in _request.session.keys():
        print(_request.session['lang'])
    else:
        _request.session['lang'] = "ua"
    return _request


def change_language(request, language):
    request.session['lang'] = language
    return redirect("index")


def send_email(recipient, title, message):
    send_mail(
        title,
        message,
        DEFAULT_SENDER,
        [recipient],
        fail_silently=False,
    )


def add_minutes(start_time, minutes):
    hours = start_time.hour
    minutes = start_time.minute + minutes
    if minutes >= 60:
        minutes = minutes - 60
        hours += 1
    start_time = start_time.replace(hour=hours)
    start_time = start_time.replace(minute=minutes)
    return start_time
