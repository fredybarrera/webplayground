from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "core/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Página web asd'
    #     return context
    
    # Permite redefinir el método de retorno
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'Mi página web asd'})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"
