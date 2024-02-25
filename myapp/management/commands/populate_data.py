from django.core.management.base import BaseCommand
from myapp.models import Category, Product


class Command(BaseCommand):
    help = 'Populate database with initial data'

    def handle(self, *args, **kwargs):
        # Здесь вы можете добавить логику для создания и сохранения объектов Category и Product
        Category.objects.create(name="Category 1", description="Description 1")
        Category.objects.create(name="Category 2", description="Description 2")
        Product.objects.create(name="Product 1", description="Description 1", category_id=1, price=10.99)
        Product.objects.create(name="Product 2", description="Description 2", category_id=2, price=20.99)

        self.stdout.write(self.style.SUCCESS('Successfully populated data'))
