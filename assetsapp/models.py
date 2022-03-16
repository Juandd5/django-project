import datetime

from django.db import models
from django.core.exceptions import ValidationError


class Person(models.Model):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.EmailField(
        verbose_name = 'Email',
        max_length = 60,
        blank = True,
        null = True
    )

    def __str__(self) -> str:
        return self.first_name
    
    class Meta():
        verbose_name_plural = 'Persons'
        db_table = 'persons'


class Area(models.Model):
    name = models.CharField('Area Name', max_length=60)

    def __str__(self) -> str:
        return self.name

    class Meta():
        verbose_name_plural = 'Areas'
        db_table = 'areas'


def validate_negative(value):
    if value < 0:
        raise ValidationError('Cannot be negative')


def validate_future_date(date):
    if date:
        if date > datetime.date.today():
            raise ValidationError('Cannot be future date')


class Asset(models.Model):
    STATUS = [
        ('AV','Available'),
        ('RE','Retired'),
        ('UR','Under Repair'),
        ('AS','Assigned'),
    ]
    person = models.ForeignKey(
        Person,
        blank = True,
        null = True,
        on_delete = models.SET_NULL
    )
    area = models.ForeignKey(
        Area,
        blank = True,
        null = True,
        on_delete = models.SET_NULL
    )
    name = models.CharField(
        verbose_name = 'Asset Name',
        max_length=60
    )
    serial = models.CharField(
        verbose_name = 'Serial',
        max_length=60,
        unique = True
    )
    purchase_price = models.DecimalField(
        verbose_name = 'Purchase Price',
        max_digits = 12,
        decimal_places = 2,
        validators = [validate_negative]
    )
    purchase_date = models.DateField(
        verbose_name = 'Purchase date',
        validators = [validate_future_date]
    )
    leaving_date = models.DateField(
        verbose_name = 'Leaving Date',
        blank = True,
        null = True,
        default = None,
        validators = [validate_future_date]
    )
    current_status = models.CharField(
        verbose_name = 'Current Status',
        max_length = 2,
        choices = STATUS
    )

    def __str__(self) -> str:
        return self.name

    def clean(self):
        if self.leaving_date:
            if self.leaving_date < self.purchase_date:
                raise ValidationError('Leaving date cannot be older than purchase date')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    class Meta():
        verbose_name_plural = 'Assets'
        db_table = 'assets'
