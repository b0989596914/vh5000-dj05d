# Generated by Django 4.0 on 2022-01-02 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonus', '0003_alter_prize_pid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prize',
            options={'ordering': ['-amount']},
        ),
        migrations.AlterModelOptions(
            name='winner',
            options={'ordering': ['week', 'prize_id']},
        ),
        migrations.AddField(
            model_name='prize',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prize',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='winner',
            name='week',
            field=models.CharField(default='1', max_length=1),
        ),
    ]
