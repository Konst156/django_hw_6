from django.urls import path

from . import views

# from homework_django.hw_1.hw_1 import views


urlpatterns = [
    path('main/', views.main, name='Главная'),
    path('about/', views.about, name='Обо мне'),
    path('clients/', views.get_all_clients, name='Клиенты'),
    path('products/', views.get_all_products, name='Продукты'),
    path('orders/', views.get_all_orders, name='Заказы'),
    path('list_goods_period_of_time/<int:days>/<int:pk>/',
         views.list_goods_period_of_time, name='list_goods_period_of_time'),
    path('show_client_orders/<int:pk>/', views.show_client_orders, name='show_client_orders'),
    path('show_products/', views.show_products, name='show_products'),
    path('update_product/', views.update_product, name='update_product'),
    path('add_product/', views.add_product, name='add_product'),
    path('', views.index, name='index'),
]