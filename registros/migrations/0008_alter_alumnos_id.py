# Generated by Django 4.0.5 on 2022-07-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0007_comentariocontacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
