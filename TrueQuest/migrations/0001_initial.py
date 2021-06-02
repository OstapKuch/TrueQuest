# Generated by Django 3.2.3 on 2021-06-02 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='QuestRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=500)),
                ('title_en', models.CharField(max_length=45)),
                ('description_en', models.CharField(max_length=500)),
                ('title_ru', models.CharField(max_length=45)),
                ('description_ru', models.CharField(max_length=500)),
                ('min_person_amount', models.IntegerField()),
                ('max_person_amount', models.IntegerField()),
                ('location', models.CharField(max_length=60)),
                ('difficulty', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('quest_duration', models.IntegerField(help_text='час прохдження кімнати в хв')),
                ('room_opens_at', models.TimeField()),
                ('room_closes_at', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateTimeField()),
                ('phone_number', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=45)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('CANCELED', 'CANCELED'), ('APPROVED', 'APPROVED')], max_length=15)),
                ('quest_room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TrueQuest.questroom')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main_image', models.IntegerField(choices=[(1, 1), (0, 0)], help_text='1 - якщо головна картинка, 0 - якщо ні')),
                ('image', models.ImageField(upload_to='images/')),
                ('image_name', models.CharField(max_length=50)),
                ('quest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TrueQuest.questroom')),
            ],
        ),
    ]
