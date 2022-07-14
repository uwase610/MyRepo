from django.urls import path
from .views import *

urlpatterns = [
    path('', Test_end_point.as_view()),
    path('add/', Test_end_point.as_view()),
    path('getdata/<id>/', Test_end_point.as_view() ),
    path('updatedata/<id>/', Test_end_point.as_view() ),
    path('deletedata/<id>/', Test_end_point.as_view() ),

]