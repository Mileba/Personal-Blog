from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="starting-page"),
    path('posts/', views.posts, name="post"),
    path('posts/<slug:slug>', views.post_detail, name="post_details")
]
