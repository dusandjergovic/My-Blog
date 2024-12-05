from . import views
from django.urls import path

urlpatterns = [
    path("", views.StartingPageVieW.as_view(), name="index"),
    path("posts/", views.AllPostsView.as_view(), name="posts"),
    path("post/<slug:slug>", views.SinglePostView.as_view(), name="hobi"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]