from django.urls import path
from .views import *

urlpatterns =[
    path('', MainPageView.as_view(), name = 'home'),
    path('category/<str:slug>/', category_page , name = 'category' ),
    path('book_review/<int:pk>/', book_detail, name = 'bk_review'),
    path('add-review/', add_review, name= 'add-review'),
]
