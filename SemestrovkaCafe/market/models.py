from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib import admin

class Provider(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    rating = models.IntegerField(default=0)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    address = models.TextField(default='')
    geo_location = models.CharField(max_length=250, default='')

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

class Category(models.Model):
    name = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='category', null=True, blank=True)

    def __str__(self):
        return  self.name

    @property
    def image_tag(self):
        try:
            return mark_safe('<img src="%s" />' % self.image.url)
        except:
            return 'None'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='product', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    # Служебный метод (self), возвращает объект в качестве строки
    def __str__(self):
        return '%s (%s)' % (self.name, self.category)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Store(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE,null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

class Delivery(models.Model):

    STATUS = (
        ('new', 'Новый заказ.'),
        ('pending', 'Заказ в работе~'),
        ('finished', 'Заказ выполнен!')
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, default='new', choices=STATUS)

    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Delivers'

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Delivery, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)


    class Meta:
        verbose_name = 'OrderProduct'
        verbose_name_plural = 'OrderProducts'

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()