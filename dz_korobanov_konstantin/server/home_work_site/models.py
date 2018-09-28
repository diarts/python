from django.db import models


# Create your models here.
class Fabricator(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Shoes_type(models.Model):
    type = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type


class Sex(models.Model):
    sex = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sex


class Sizes(models.Model):
    size = models.DecimalField(max_digits=3, decimal_places=1, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.size)


class Colors(models.Model):
    color = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.color


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    manuf = models.ForeignKey(Fabricator, on_delete=models.CASCADE, default='Производитель отсутствует')
    type = models.ForeignKey(Shoes_type, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, default='Описание отсутствует')
    det_description = models.TextField(default='Детальное описание отсутствует')
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    colors = models.ManyToManyField(Colors)
    size = models.ManyToManyField(Sizes)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def href(self):
        href = self.name
        href = href.replace(' ', '_')
        return href
