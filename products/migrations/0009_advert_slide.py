# Generated by Django 3.1.7 on 2021-02-26 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advert1pics', models.ImageField(blank=True, null=True, upload_to='slides/')),
                ('advert1heading', models.CharField(blank=True, max_length=250, null=True)),
                ('advert1subheading', models.CharField(blank=True, max_length=250, null=True)),
                ('advert1writeup', models.CharField(blank=True, max_length=250, null=True)),
                ('advert2pics', models.ImageField(blank=True, null=True, upload_to='slides/')),
                ('advert2heading', models.CharField(blank=True, max_length=250, null=True)),
                ('advert2subheading', models.CharField(blank=True, max_length=250, null=True)),
                ('advert2writeup', models.CharField(blank=True, max_length=250, null=True)),
                ('advert3pics', models.ImageField(blank=True, null=True, upload_to='slides/')),
                ('advert3heading', models.CharField(blank=True, max_length=250, null=True)),
                ('advert3subheading', models.CharField(blank=True, max_length=250, null=True)),
                ('advert3writeup', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide1pics', models.ImageField(blank=True, null=True, upload_to='slides/')),
                ('slide1heading', models.CharField(blank=True, max_length=250, null=True)),
                ('slide1subheading', models.CharField(blank=True, max_length=250, null=True)),
                ('slide1writeup', models.CharField(blank=True, max_length=250, null=True)),
                ('slide2pics', models.ImageField(blank=True, null=True, upload_to='slides/')),
                ('slide2heading', models.CharField(blank=True, max_length=250, null=True)),
                ('slide2subheading', models.CharField(blank=True, max_length=250, null=True)),
                ('slide2writeup', models.CharField(blank=True, max_length=250, null=True)),
                ('slide3pics', models.ImageField(blank=True, null=True, upload_to='slides/')),
                ('slide3heading', models.CharField(blank=True, max_length=250, null=True)),
                ('slide3subheading', models.CharField(blank=True, max_length=250, null=True)),
                ('slide3writeup', models.CharField(blank=True, max_length=250, null=True)),
                ('slide4pics', models.ImageField(blank=True, null=True, upload_to='slides/')),
                ('slide4heading', models.CharField(blank=True, max_length=250, null=True)),
                ('slide4subheading', models.CharField(blank=True, max_length=250, null=True)),
                ('slide4writeup', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
