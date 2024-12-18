from django.db import models
import os
from django.contrib.auth import get_user_model

User = get_user_model()


def custom_upload_to(instance, filename):
    """
    Генерирует путь для сохранения файла с учётом уникального имени.
    """
    extension = os.path.splitext(filename)[-1]
    unique_filename = f"{instance.name}{extension}"
    return os.path.join('ThreeDModel', unique_filename)


class ThreeDModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=255,
        verbose_name="Название файла",
        blank=True
    )
    file = models.FileField(upload_to=custom_upload_to, verbose_name="Файл")
    description = models.TextField('описание', default='Здесь могло быть описание модели')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    def save(self, *args, **kwargs):
        if not self.name:  # Если имя не задано
            self.name = os.path.basename(self.file.name)  # Сохраняем имя файла
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
