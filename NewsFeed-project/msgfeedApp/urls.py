from django.urls import path
from . import views
urlpatterns = [
    path('feed/', views.Feedpage, name="feed"),
    path('likepost/<str:message_id>', views.likepost, name="likepost"),
    path('commentpost/<str:message_id>', views.commentpost, name="commentpost"),
    path('editcomment/<str:pk>', views.editcomment, name="editcomment"),
    path('deletecomment/<str:pk>', views.deletecomment, name="deletecomment"),
]
