from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', null=True, blank=True, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, related_name='items', null=True, blank=True, on_delete=models.CASCADE)
    birth = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    # def calculate_age(self):
    today = date.today()
    # age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    # from datetime import date

    # def calculate_age(born):
    #     today = date.today()
    #     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    #
    # age = calculate_age(birth)

    def __str__(self):
        return self.name
