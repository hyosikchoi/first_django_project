from django.urls import path

from . import views

# app_name 을 추가하여 여러 앱을 Django 에서 path 로 관리 가능
app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.details, name="details"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]