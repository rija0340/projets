from django.urls import path
from .views import ArticleCreate, RenderPdf


from . import views

#espace (namespace) nom de l'application pour identifier cette application, 
app_name = 'blog'

urlpatterns = [
    # ao amin'ny mysite raha ijery vu généric
    path('', views.IndexView.as_view(), name='index'),

    path('create/', ArticleCreate.as_view(), name='create_article'),

    path('<int:pk>/', views.DetailView.as_view(), name='detail_article'),
    
    path('update/<int:pk>/', views.ArticleUpdate.as_view(), name='update_article'),
    path('delete/<int:pk>/', views.ArticleDelete.as_view(), name='delete_article'),
    path('log_in/', views.log_in, name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
    path('register/', views.register, name='register'),
    path('renderpdf/', RenderPdf.as_view(), name='renderpdf'),
    path('forms/', views.forms, name='create_article'),
    
]