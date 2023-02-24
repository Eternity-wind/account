
from django.urls import path
from django.contrib import admin
from acc_records import views

urlpatterns = [
    path('', views.list_account_view, name='accounts'),
    path('<int:account_id>/', views.detail_account_view)
]