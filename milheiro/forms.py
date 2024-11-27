from django import forms
from .models import Plataforma, CarteiraDePontos


class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = ['nome', 'custo_ponto']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.created_by = self.user
        if commit:
            instance.save()
        return instance


class CarteiraDePontosForm(forms.ModelForm):
    class Meta:
        model = CarteiraDePontos
        fields = ['plataforma', 'pontos']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.created_by = self.user
        if commit:
            instance.save()
        return instance
