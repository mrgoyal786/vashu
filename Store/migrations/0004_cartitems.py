# Generated by Django 3.2.6 on 2021-08-11 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_alter_ebook_cover_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('price', models.FloatField(null=True)),
                ('cover_url', models.CharField(max_length=5000000, null=True)),
            ],
        ),
    ]
