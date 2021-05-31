from django.db import models

BOOLEAN_CHOICES = (
    (1, 1),
    (0, 0)
)
QUEST_DIFFICULTY = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)
RESERVATIONS_STATUS_CHOICES = (
    ('PENDING', 'PENDING'),
    ('CANCELED', 'CANCELED'),
    ('APPROVED', 'APPROVED'),
)


class QuestRoom(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=500)
    title_en = models.CharField(max_length=45)
    description_en = models.CharField(max_length=500)
    title_ru = models.CharField(max_length=45)
    description_ru = models.CharField(max_length=500)
    min_person_amount = models.IntegerField()
    max_person_amount = models.IntegerField()
    time = models.DateTimeField
    location = models.CharField(max_length=60)
    difficulty = models.IntegerField(choices=QUEST_DIFFICULTY)
    quest_duration = models.IntegerField(help_text="час прохдження кімнати в хв")
    age = models.IntegerField
    room_opens_at = models.TimeField()
    room_closes_at = models.TimeField()

    def __str__(self):
        return self.title

    def get_all_objects(self):
        queryset = self._meta.model.objects.all()
        return queryset


class Image(models.Model):
    quest_id = models.ForeignKey(QuestRoom, on_delete=models.CASCADE)
    is_main_image = models.IntegerField(choices=BOOLEAN_CHOICES, help_text="1 - якщо головна картинка, 0 - якщо ні")
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=50)

    def __str__(self):
        return self.image_name


class RoomReservation(models.Model):
    reservation_date = models.DateTimeField()
    quest_room_id = models.ForeignKey(QuestRoom, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    name = models.CharField(max_length=45)
    status = models.CharField(max_length=15, choices=RESERVATIONS_STATUS_CHOICES)

    def str(self):
        return self.name + " " + self.phone_number + " " + str(self.reservation_date)
