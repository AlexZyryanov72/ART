from django.db import models


class Artist(models.Model):
    artist_name = models.CharField("ФИО художника", max_length=100)
    artist_biography = models.TextField("биогафия")
    artist_main_image = models.ImageField("фотография художника", upload_to="image/artist")

    def __str__(self):
        return self.artist_name


class Article(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    article_title = models.CharField("название статьи", max_length=100)
    article_preview = models.CharField("превью статьи", max_length=500)
    article_text = models.TextField("текст статьи")
    article_data = models.DateTimeField("дата публикации")
    article_main_image = models.ImageField("главное изображение статьи", upload_to="image/article")

    def __str__(self):
        return self.article_title



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    autor_name = models.CharField("", max_length=100)
    comment_text = models.CharField("", max_length=500)

    def __str__(self):
        return self.autor_name
