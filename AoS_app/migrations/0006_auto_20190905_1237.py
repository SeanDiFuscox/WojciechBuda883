# Generated by Django 2.2.5 on 2019-09-05 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AoS_app', '0005_auto_20190905_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='player_1',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='player_1', to='AoS_app.GamePlayer'),
        ),
        migrations.AlterField(
            model_name='game',
            name='player_2',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='player_2', to='AoS_app.GamePlayer'),
        ),
    ]
