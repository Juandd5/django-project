from datetime import date, timedelta

from django.test import TestCase
from assetsapp.models import Person, Area, Asset
from django.core.exceptions import ValidationError


class PersonTests(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Person.objects.create(
            first_name = 'Pedro',
            last_name = 'Perez',
            email = 'pedro@perez.com'
        )

    def test_max_length_of_first_and_last_name(self):
        person = Person.objects.get(pk=1)
        first_name_length = person._meta.get_field('first_name').max_length
        last_name_length = person._meta.get_field('last_name').max_length
        self.assertEqual(first_name_length, 50)
        self.assertEqual(last_name_length, 50)

    def test_email_max_length(self):
        person = Person.objects.get(pk=1)
        email_length = person._meta.get_field('email').max_length
        self.assertEqual(email_length, 60)


class AreaTests(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Area.objects.create(name='Web Development')

    def test_name_max_length(self):
        area = Area.objects.get(pk=1)
        name_length = area._meta.get_field('name').max_legth
        self.assertEqual(name_length, 60)


class AssetTests(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Asset.objects.create(
            name = 'Computer',
            serial = '123abc',
            purchase_price = 2500000.00,
            purchase_date = date.today(),
            current_status = 'AV'
        )

    def test_purchase_price_cannot_be_negative(self):
        asset = Asset.objects.get(pk=1)
        asset.purchase_price *= -1
        with self.assertRaises(ValidationError):
            asset.save()
    
    def test_future_purchase_date(self):
        asset = Asset.objects.get(pk=1)
        asset.purchase_date = date.today() + timedelta(days=1)
        with self.assertRaises(ValidationError):
            asset.save()
    
    def test_field_leaving_date_is_empty(self):
        asset = Asset.objects.get(pk=1)
        self.assertIsNone(asset.leaving_date)

    def test_future_leaving_date(self):
        asset = Asset.objects.get(pk=1)
        asset.leaving_date = date.today() + timedelta(days=1)
        with self.assertRaises(ValidationError):
            asset.save()

    def test_leaving_date_cannot_be_older_than_purchase_date(self):
        asset = Asset.objects.get(pk=1)
        asset.leaving_date = date.today() - timedelta(days=1)
        with self.assertRaises(ValidationError):
            asset.clean()

    #def test_serial_is_unique(self):
    #    with self.assertRaises(ValidationError):
    #        asset = Asset.objects.create(serial='123abc')
