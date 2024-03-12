from django.urls import path
from . import views

urlpatterns = [
  path("",views.home, name="home"),
  path("about/",views.about, name="about"),
  path('function/', views.function_view, name='function_view'),
  path('class/', views.ClassView.as_view(), name='class_view'),
  path('theme/', views.ThemeView.as_view(), name='theme'),
  path('profile/', views.profile_view, name='profile'),
  path('product/', views.product_view, name='product'),
  path('specialmenu/', views.specialmenu_view, name='specialmenu'),
  path('ourplum/', views.ourplum_view, name='ourplum'),
]
