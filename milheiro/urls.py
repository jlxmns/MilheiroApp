from django.urls import path

from milheiro import views

app_name = 'milheiro'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]
