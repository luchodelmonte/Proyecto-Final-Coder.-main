# Generated by Django 4.1.2 on 2022-11-26 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Torta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_torta', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='tortas',
        ),
        migrations.RenameField(
            model_name='cafe',
            old_name='sinopsis',
            new_name='descripcion',
        ),
    ]