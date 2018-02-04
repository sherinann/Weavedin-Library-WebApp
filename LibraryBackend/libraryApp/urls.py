from django.urls import path
from . import views

#urls to connect to the views
urlpatterns = [
    path('', views.books, name='books'),
    path('books',views.books,name='books'),
    path('books/<int:isbn_no>', views.book_description, name='bdescription'),
    path('authors',views.authors,name='authors'),
    path('authors/<int:id>',views.author_description,name='adescription'),
    path('addBook', views.addBook, name='addBook'),
    path('addAuthor', views.addAuthor, name='addAuthor'),
]
