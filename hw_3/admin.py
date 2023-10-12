import decimal

from django.contrib import admin

# from hw.hw_3 import models


from . import models


@admin.action(description='Увеличить цену товара на 15 процентов')
def change_price(modeladmin, request, queryset):
    """Добавление действий"""
    old_price = queryset.values()[0]['price']
    queryset.update(price=old_price * decimal.Decimal('1.15'))


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'added_date']
    ordering = ['-added_date']
    list_filter = ['added_date', 'price', 'quantity']
    search_fields = ['name']
    search_help_text = 'Поиск по названию продукта'
    actions = [change_price]

    fields = ['name', 'description', 'price', 'quantity', 'added_date', 'product_image']
    readonly_fields = ['product_image', 'added_date']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
    ordering = ['name']
    list_filter = ['registration_date']
    search_fields = ['name']
    search_help_text = 'Поиск по имени клиента'
    readonly_fields = ['registration_date', 'name']

    # Детальная настройка отображения полей
    fieldsets = [
        (
            'Имя клиента',
            {
                'classes': ['wide'],
                'fields': ['name'],
                # Первая группа будет содержать только поле "name", она будет иметь
                # класс "wide", что означает, что она будет занимать все доступное место
                # на странице.
            },
        ),
        (
            'Редактировать данные клиента',
            {
                'classes': ['collapse'],
                'description': 'Будьте внимательны при редактировании данных!',
                'fields': ['email', 'number_phone', 'address'],
                # Вторая группа будет содержать поля 'email', 'number_phone', 'address', они
                # будут скрыты по умолчанию (класс "collapse"), но можно будет
                # развернуть и отредактировать эту группу, нажав на соответствующий заголовок. Под
                # заголовком отобразится описание группы registration_date
            },
        ),
        (
            'Дата регистрации клиента',
            {
                'classes': ['wide'],
                'fields': ['registration_date'],
            },
        )
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'order_date', 'total_amount']
    ordering = ['order_date']
    list_filter = ['order_date']
    search_fields = ['order_date']
    search_help_text = 'Поиск по дате'
    readonly_fields = ['client', 'products', 'order_date', 'total_amount']
    fieldsets = [
        (
            'Клиент',
            {
                'classes': ['wide'],
                'fields': ['client'],
            },
        ),
        (
            'Что купил',
            {
                'classes': ['wide'],
                'fields': ['products'],
            },
        ),
        (
            'Дата оформления заказа',
            {
                'classes': ['wide'],
                'fields': ['order_date'],
            },
        ),
        (
            'Итоговая цена заказа',
            {
                'classes': ['wide'],
                'fields': ['total_amount'],
            },
        )
    ]


admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)
