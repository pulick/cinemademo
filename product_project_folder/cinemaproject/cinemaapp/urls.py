
from django.urls import path
from . import views
app_name='cinemaapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('cinema/<int:cinema_id>/',views.detail,name='detail'),
    path('add/',views.add_cinema,name='add_cinema'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),

]
