from django.urls import path
from book import views

urlpatterns = [
    path('api/book', views.store, name="book-store"),
    path('api/books', views.getAll, name="books"),
    path('api/book/<int:id>', views.detail, name="book-detail"),
    path('api/book/update/<int:id>', views.update, name="book-update"),
    path('api/book/delete/<int:id>', views.delete, name="book-delete")
]
