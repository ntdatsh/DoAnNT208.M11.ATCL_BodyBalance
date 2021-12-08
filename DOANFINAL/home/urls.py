from django.urls import path
from .import views

app_name = 'UserMember'

urlpatterns = [
    path('', views.get_index, name = 'home'),
    path('login/', views.loginUser.as_view(), name='loginUser'),
    path('login/register/', views.registerUser.as_view(), name='registerUser'),
    path('indexafterlogin', views.get_indexafterlogin, name='indexafterlogin'),
    path('login/monitor/', views.pro.as_view(), name=''),
    path('',views.logoutUser, name='logout'),
    path('login/WheyProtein/', views.wheys),
    path('login/Nutrition/', views.get_nutri, name = 'Nutrition'),
    path('login/PTRental/', views.get_PT),
    path('login/Schedule/', views.get_schedule),
    path('login/TrainingPlan/', views.get_train),
    path('Nutrition/', views.get_nutri, name = 'Nutrition'),
    path('PTRental/', views.get_PT),
    path('Schedule/', views.get_schedule),
    path('TrainingPlan/', views.get_train),
    path('WheyProtein/', views.wheys),
    path('monitor/', views.pro.as_view(), name=''),
    path('monitor/cart/', views.get_cart),
    path('login/monitor/cart/', views.get_cart),
    path('monitor/cart/checkout', views.get_checkout, name="checkout"),
    path('login/monitor/cart/checkout', views.get_checkout, name="checkout"),
    path('WheyProtein/cart/', views.get_cart),
    path('login/WheyProtein/cart/', views.get_cart),
    path('login/WheyProtein/cart/checkout', views.get_checkout, name="checkout"),
    path('WheyProtein/cart/checkout', views.get_checkout, name="checkout"),
    path('cartadd/', views.cartadd, name= "cartadd"),
    path('cartadd1/', views.cartadd1, name= "cartadd1")
]