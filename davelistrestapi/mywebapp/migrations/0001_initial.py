# Generated by Django 4.1 on 2022-08-20 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_id', models.IntegerField(default=1)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=50)),
                ('categories', models.CharField(choices=[('PRIVATE', 'Private'), ('PUBLIC', 'Public')], default='PUBLIC', max_length=10)),
            ],
        ),
    ]