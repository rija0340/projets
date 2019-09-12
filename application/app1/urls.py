from django.urls import path

from . import views

#espace (namespace) nom de l'application pour identifier cette application, 
app_name = 'app1'

urlpatterns = [
    # ao amin'ny mysite raha ijery vu généric
    path('', views.list, name = 'list'), 
    path('new', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
 
]