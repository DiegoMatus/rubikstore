#-*- coding: utf-8 -*-
from django.db import models
from random import randrange
import datetime
from django.utils.text import slugify
from django.conf import settings
#sfrom accounts.models import Profile

CHARSET = '0123456789'
CHARSET_ORDER = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'
LENGTH = 10
LENGTH_ORDER_CODE = 15
MAX_TRIES = 1024


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)
    code = models.BigIntegerField(null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='category/%Y%m%d', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return "/category/%s/" % self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unicode(self.name))
        self.updated_at = datetime.datetime.now()
        loop_num = 0
        unique = False
        while not unique:
            if loop_num < MAX_TRIES:
                new_code = ''
                for i in xrange(LENGTH):
                    new_code += CHARSET[randrange(0, len(CHARSET))]
                if not Category.objects.filter(code=new_code):
                    self.code = new_code
                unique = True
                loop_num += 1
            else:
                raise ValueError("Couldn't generate a unique code.")
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    description_full = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='brand/%Y%m%d', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unicode(self.name))
        super(Brand, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Base(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)
    OFFS = (
        (1,10),(2,20),(3,30),(4,40),(5,50),(6,60),(7,70),(8,80),(9,90),(10,100)
    )
    off = models.IntegerField(choices=OFFS, null=True, blank=True)
    brand = models.ForeignKey(Brand, related_name='products')
    category = models.ForeignKey(Category, related_name='products_c')
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    description_full = models.TextField(blank=True, null=True)
    code = models.BigIntegerField(null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)
    TYPE_CHOICES = (
        (1,'Puzzle'),
        (2,'Timers'),
        (3,'Accessory')
    )
    type = models.IntegerField(choices=TYPE_CHOICES, default=1)
    base = models.ManyToManyField(Base, blank=True)
    thumbnail = models.FileField(upload_to='thumbnails/%Y%m%d', null=True, blank=True)
    featured = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name

    def get_thumbnail_url(self):
        return "{0}{1}".format(settings.MEDIA_ROOT, self.thumbnail.url)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unicode(self.name))
        self.updated_at = datetime.datetime.now()
        loop_num = 0
        unique = False
        while not unique:
            if loop_num < MAX_TRIES:
                new_code = ''
                for i in xrange(LENGTH):
                    new_code += CHARSET[randrange(0, len(CHARSET))]
                if not Product.objects.filter(code=new_code):
                    self.code = new_code
                unique = True
                loop_num += 1
            else:
                raise ValueError("Couldn't generate a unique code.")
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "/product/%s/" % self.slug


class Inventory(models.Model):
    volume = models.IntegerField()
    product = models.ForeignKey(Product, related_name='existence')

    def __unicode__(self):
        return self.product.name + str(self.volume)


class ImageProduct(models.Model):
    product = models.ForeignKey(Product, related_name='images')
    image = models.ImageField(upload_to='product/%Y%m%d')

    def __unicode__(self):
        return self.product.name


class Country(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=300)
    country = models.ForeignKey(Country, related_name='states')

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=300)
    state = models.ForeignKey(State, related_name='cities')

    def __unicode__(self):
        return self.name


#class Address(models.Model):
#    profile = models.ForeignKey(Profile, related_name='address')
#    address = models.CharField(max_length=300)
#    zipcode = models.CharField(max_length=5)
#    city = models.ForeignKey(City)
#
#    def __unicode__(self):
#        return self.profile.name + self.address
#
#
#class Payment(models.Model):
#    credit_card = models.CharField(max_length=16)
#    cvv = models.CharField(max_length=4)
#    expiration_date = models.CharField(max_length=10)
#    name_titular = models.CharField(max_length=300)
#    profile = models.ForeignKey(Profile, related_name='billing_info')
#
#    def __unicode__(self):
#        return self.profile.name
#
#
#class Order(models.Model):
#    date = models.DateTimeField(auto_now_add=True)
#    code = models.CharField(max_length=15)
#    ORDER_STATUS = (
#        (1, 'Pendiente de revisión'),
#        (2, 'Revisado y pendiente de envío'),
#        (3, 'Enviado'),
#        (4, 'Entregado')
#    )
#    status = models.IntegerField(choices=ORDER_STATUS, default=1)
#    total_order = models.DecimalField(max_digits=10, decimal_places=2)
#    profile = models.ForeignKey(Profile, related_name='orders')
#    PAYMENT_OPTIONS = (
#        (1, 'Tarjeta de Crédito'),
#        (2, 'Pago contraentrega'),
#        (3, 'PayPal'),
#    )
#    payment_method = models.IntegerField(max_length=1, choices=PAYMENT_OPTIONS, default=1)
#    payment = models.ForeignKey(Payment, related_name='orders_payed', null=True, blank=True)
#    products = models.ManyToManyField(Product, related_name='selled')

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        loop_num = 0
        unique = False
        while not unique:
            if loop_num < MAX_TRIES:
                new_code = ''
                for i in xrange(LENGTH_ORDER_CODE):
                    new_code += CHARSET_ORDER[randrange(0, len(CHARSET_ORDER))]
                if not Order.objects.filter(code=new_code):
                    self.code = new_code
                unique = True
                loop_num += 1
            else:
                raise ValueError("Couldn't generate a unique code.")
        super(Order, self).save(*args, **kwargs)


#class Comment(models.Model):
#    comment = models.TextField()
#    date = models.DateTimeField(auto_now_add=True)
#    profile = models.ForeignKey(Profile, related_name='comments')
#    product = models.ForeignKey(Product, related_name='comments_by')
#
#    def __unicode__(self):
#        return self.profile.name