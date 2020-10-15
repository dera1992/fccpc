from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_list, name='home'),
    path('category_chart/', views.category_chart, name='category_chart'),
    path('ads_list', views.ads_list, name='ads_list'),
    path('allads_list', views.allads_list, name='allads_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('ads_list/', views.ads_list, name='ads_list_by_make'),
    path('delete_post', views.delete_post, name='delete_post'),
    # path('favourite_ad',views.favourite_ad, name='favourite_ad'),
    path('favourite_delete',views.favourite_delete, name='favourite_delete'),
    path('ad_detail', views.ad_detail, name='ad_detail'),
    # path('<int:id>', views.ad_detail_rating, name='ad_detail_rating'),
    path('category_count/',views.category_count,name='category_count'),
    path('views.send_message',views.send_message, name='send_message'),

]