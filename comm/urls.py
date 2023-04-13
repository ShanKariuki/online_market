from django.urls  import path
from.views import *

app_name='comm'

urlpatterns=[
    path('new/<int:item_pk>/',new_conversation, name='new'),
    path('',inbox, name='inbox'),
    path('messages/<int:pk>/', detail, name='detail'),
]