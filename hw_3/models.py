from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Client -> name: {self.name}, email: {self.email},' \
               f'number_phone: {self.phone_number}, address: {self.address}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)
    product_image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return f'Product-> {self.name}, {self.description}, {self.price}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Order-> {self.client}, {self.products}, {self.total_amount}'

