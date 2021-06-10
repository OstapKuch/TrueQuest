from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import QuestRoom, Image, RoomReservation, MainImage, RoomClose, RoomPrice


@admin.register(QuestRoom)
class QuestRoomAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'min_person_amount', 'max_person_amount',
              'title_en', 'description_en', 'title_ru', 'description_ru', 'quest_duration',
              'difficulty', 'location', 'location_google_url', 'room_opens_at', 'room_closes_at')
    list_display = ('title', 'difficulty', 'quest_duration', 'room_opens_at', 'room_closes_at')


@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    fields = ('quest_id', 'is_main_image', 'image', 'image_name')
    list_display = ('quest_id', 'is_main_image')
    list_filter = (
        'quest_id',
        'is_main_image'
    )


@admin.register(RoomReservation)
class RoomReservationAdmin(admin.ModelAdmin):
    fields = ('quest_room_id', 'reservation_date', 'phone_number', 'name', 'person_number', 'price', 'status')
    list_display = ('quest_room_id', 'reservation_date', 'name', 'phone_number', 'status')
    list_editable = ('status',)
    list_filter = (
        ('reservation_date', DateFieldListFilter),
        'status',
        'quest_room_id'
    )


@admin.register(MainImage)
class MainImage(admin.ModelAdmin):
    fields = ('image', 'name')


@admin.register(RoomClose)
class RoomClose(admin.ModelAdmin):
    fields = ('quest_room_id', 'closes_at', 'opens_at')
    list_display = ('quest_room_id', 'closes_at', 'opens_at')
    list_filter = (
        'quest_room_id',
        ('closes_at', DateFieldListFilter),
        ('opens_at', DateFieldListFilter)
    )


@admin.register(RoomPrice)
class RoomPrice(admin.ModelAdmin):
    fields = ('quest_room_id', 'number_of_person', 'price')
    list_display = ('quest_room_id', 'number_of_person', 'price')
    list_filter = (
        'quest_room_id',
    )