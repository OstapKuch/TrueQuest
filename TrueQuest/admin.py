from django.contrib import admin
from .models import QuestRoom, Image, RoomReservation

@admin.register(QuestRoom)
class QuestRoomAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'min_person_amount', 'max_person_amount',
              'title_en', 'description_en', 'title_ru', 'description_ru', 'quest_duration',
              'difficulty', 'location')


@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    fields = ('quest_id', 'is_main_image', 'image', 'image_name')


@admin.register(RoomReservation)
class RoomReservationAdmin(admin.ModelAdmin):
    fields = ('quest_room_id', 'reservation_date', 'phone_number', 'name', 'status')
