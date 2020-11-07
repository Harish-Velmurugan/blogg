from django.urls import path
from . import views 

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', views.BlogDetailView, name='post_detail'),
     path('post/new/',views.BlogCreateView.as_view(), name='post_new'),
]