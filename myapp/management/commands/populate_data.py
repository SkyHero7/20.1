from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.transaction import TransactionManagementError
from myapp.models import Category, Product


class Command(BaseCommand):
    help = 'Populate database with initial data'

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                """
                Удаление записи в таблицах
                """
                Category.objects.all().delete()
                Product.objects.all().delete()

                """
                Создание новых записей
                """
                Category.objects.create(name="Category 1", description="Description 1")
                Category.objects.create(name="Category 2", description="Description 2")
                Product.objects.create(name="Product 1", description="Description 1", category_id=1, price=10.99)
                Product.objects.create(name="Product 2", description="Description 2", category_id=2, price=20.99)

            self.stdout.write(self.style.SUCCESS('Successfully populated data'))

        except TransactionManagementError:
            self.stdout.write(self.style.ERROR('Failed to populate data. Transaction rolled back.'))

