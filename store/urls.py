from django.urls import path
from.views import *
app_name='store'
urlpatterns=[
    path('',index, name='index'),
    path('about/',about,name='about'),
    path('detail/<int:id>/',detail, name='detail'),
    path('create/',newitem, name='create'),
    path('update/<int:id>/', edititem, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('items/', items, name='search'),
]