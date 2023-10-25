from django.urls import path,include
from .import views

urlpatterns = [
   
    path('',views.frontend),
    path('books/', views.book_list, name='book-list'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
    path('members/', views.member_list, name='member-list'),
    path('members/<int:pk>/', views.member_detail, name='member-detail'),
    path('issue-book/', views.issue_book, name='issue-book'),
]