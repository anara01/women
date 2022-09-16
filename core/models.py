from django.urls import reverse

from django.db import models

class Women(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    content = models.TextField("Текст статьи", blank=True)
    photo = models.ImageField("Фото", upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField("Время создания", auto_now_add=True)
    time_update = models.DateTimeField("Время изменения", auto_now=True)
    is_published = models.BooleanField("Публикация", default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = "Известные женщины"
        verbose_name_plural = "Известные женщины"
        ordering = ['-time_create', 'title']

class Category(models.Model):
    name = models.CharField("Категория", max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']