from django.urls import path

from milheiro import views

app_name = 'milheiro'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("plataforma", views.PlataformaView.as_view(), name="plataforma"),
    path("plataforma/add", views.AddPlataformaFormView.as_view(), name="plataforma_add"),
    path("plataforma/<int:pk>", views.UpdatePlataformaFormView.as_view(), name="plataforma_change"),
    path("plataforma/del/<int:pk>", views.DeletePlataformaFormView.as_view(), name="plataforma_del"),
    path("pontos", views.PontosView.as_view(), name="pontos"),
    path("pontos/add", views.AddPontosFormView.as_view(), name="pontos_add"),
    path("pontos/<int:pk>", views.UpdatePontosFormView.as_view(), name="pontos_change"),
    path("pontos/del/<int:pk>", views.DeletePontosFormView.as_view(), name="pontos_del"),
]
