# Generated by Django 3.0.4 on 2020-03-09 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=100, verbose_name='название статьи')),
                ('article_preview', models.CharField(max_length=500, verbose_name='превью статьи')),
                ('article_text', models.TextField(verbose_name='текст статьи')),
                ('pub_date', models.DateTimeField(verbose_name='дата публикации')),
                ('article_main_image', models.ImageField(upload_to='image/article', verbose_name='главное изображение статьи')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=100, verbose_name='ФИО художника')),
                ('artist_biography', models.TextField(verbose_name='биогафия')),
                ('artist_main_image', models.ImageField(upload_to='image/artist', verbose_name='фотография художника')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor_name', models.CharField(max_length=100, verbose_name='')),
                ('comment_text', models.CharField(max_length=500, verbose_name='')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Artist'),
        ),
    ]
