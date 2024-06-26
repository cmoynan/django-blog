from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_me, name='about'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
]