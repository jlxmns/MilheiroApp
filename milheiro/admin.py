from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin
from .models import CarteiraDePontos, Plataforma
from . import forms

# Register your models here.

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(Plataforma)
class PlataformaAdmin(ModelAdmin):
    fields = ('nome', 'custo_ponto')
    list_display = ('nome', 'custo_ponto', 'created_by')
    list_per_page = 10
    form = forms.PlataformaForm

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()


@admin.register(CarteiraDePontos)
class CarteiraDePontosAdmin(ModelAdmin):
    fields = ('plataforma', 'pessoa', 'pontos', 'valor', 'descricao', 'data_aquisicao', 'data_expiracao')
    list_display = ('plataforma',)
    list_per_page = 10
    form = forms.CarteiraDePontosForm
