from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from milheiro.models import Plataforma, CarteiraDePontos


# Create your views here.

class IndexView(TemplateView):
    template_name = 'milheiro/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        return context


class PlataformaView(TemplateView):
    template_name = 'milheiro/plataforma_changelist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['plataformas'] = Plataforma.objects.filter(created_by=self.request.user)

        return context


class AddPlataformaFormView(CreateView):
    model = Plataforma
    fields = ["nome", "custo_ponto"]
    success_url = reverse_lazy("milheiro:plataforma")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class UpdatePlataformaFormView(UpdateView):
    model = Plataforma
    fields = ["nome", "custo_ponto"]
    success_url = reverse_lazy("milheiro:plataforma")


class DeletePlataformaFormView(DeleteView):
    model = Plataforma
    fields = ["nome", "custo_ponto"]
    success_url = reverse_lazy("milheiro:plataforma")


class PontosView(TemplateView):
    template_name = 'milheiro/pontos_changelist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['plataformas'] = Plataforma.objects.filter(created_by=self.request.user)

        return context


class AddPontosFormView(CreateView):
    model = CarteiraDePontos
    fields = ['plataforma', 'pontos', 'valor', 'descricao', 'data_aquisicao', 'data_expiracao']
    success_url = reverse_lazy("milheiro:pontos")

    def form_valid(self, form):
        form.instance.pessoa = self.request.user
        return super().form_valid(form)


class UpdatePontosFormView(UpdateView):
    model = CarteiraDePontos
    fields = ['plataforma', 'pessoa', 'pontos', 'valor', 'descricao', 'data_aquisicao', 'data_expiracao']
    success_url = reverse_lazy("milheiro:pontos")


class DeletePontosFormView(DeleteView):
    model = CarteiraDePontos
    fields = ['plataforma', 'pessoa', 'pontos', 'valor', 'descricao', 'data_aquisicao', 'data_expiracao']
    success_url = reverse_lazy("milheiro:pontos")
