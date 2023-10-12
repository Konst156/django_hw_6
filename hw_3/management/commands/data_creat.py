from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.utils import timezone
from random import randint
import sys
sys.path.append("./Homework_3/hw/hw_3")
from hw_3.models import Product, Client, Order


class Command(BaseCommand):
    help = 'Create N clients, products, and orders'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of objects to be created')

    def create_clients(self, total):
        for i in range(total):
            name = get_random_string(10)
            email = f'{name}@example.com'
            phone_number = get_random_string(10, '1234567890')
            address = get_random_string(20)
            registration_date = timezone.now()
            Client.objects.create(name=name, email=email, phone_number=phone_number, address=address,
                                  registration_date=registration_date)

    def create_products(self, total):
        for i in range(total):
            name = get_random_string(10)
            description = get_random_string(50)
            price = randint(1, 100)
            quantity = randint(1, 10)
            added_date = timezone.now()
            Product.objects.create(name=name, description=description, price=price, quantity=quantity,
                                   added_date=added_date)

    def create_orders(self, total):
        clients = Client.objects.all()
        products = Product.objects.all()

        for i in range(total):
            client = clients[randint(0, len(clients) - 1)]
            product = products[randint(0, len(products) - 1)]
            total_amount = product.price * product.quantity
            order_date = timezone.now()
            order = Order.objects.create(client=client, total_amount=total_amount, order_date=order_date)
            order.products.add(product)

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        self.create_clients(total)
        self.create_products(total)
        self.create_orders(total)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} clients, products, and orders.'))
