from django.urls import path
from autohub import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('accounts/profile/', views.home_page, name='home_page'),
    path('cars/', views.CarList.as_view()),
    path('cars/<int:pk>/', views.CarDetail.as_view()),
    path('manufacturers/', views.ManufacturerList.as_view()),
    path('manufacturers/<int:pk>/', views.ManufacturerDetail.as_view()),
    path('car_types/', views.TypeList.as_view()),
    path('car_types/<int:pk>/', views.TypeDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
