from django.urls import path
from .views import add_reviews, show_reviews, update_reviews, delete_reviews


urlpatterns = [
    path('', add_reviews, name='add_url'),
    path('show/', show_reviews, name='show_url'),
    path('update/<int:pk>/', update_reviews, name='update_url'),
    path('delete/<int:pk>/', delete_reviews, name='delete_url'),
]
