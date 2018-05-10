from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200,verbose_name="Başlık")
    text = models.TextField(verbose_name="Açıklama")
    created_date = models.DateTimeField(
            default=timezone.now,verbose_name="Oluşturulma Tarihi")
    published_date = models.DateTimeField(
            blank=True, null=True,verbose_name="Yayınlanma Tarihi")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
