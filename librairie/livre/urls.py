from django.urls import path
from  . import views
urlpatterns = [
    path('books/', views.allBooks),
    path('book/<int:id>/', views.getBook),
    path('addbooks/', views.addBooks),
    path('update/<int:id>/', views.updateBook),
    path('deletebook/<int:id>/', views.delBook),

]