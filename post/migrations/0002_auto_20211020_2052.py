# Generated by Django 3.2.8 on 2021-10-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='blog_pics/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]