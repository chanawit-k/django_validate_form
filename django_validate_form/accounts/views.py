from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import UserRegistrationForm


class SampleView(TemplateView):
    template_name = "accounts/sample_html.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add your context variables here
        context['test_context'] = 'value from views'
        return context


class SignUpView(CreateView):
    template_name = "accounts/sample_html.html"
    success_url = reverse_lazy('login')
    form_class = UserRegistrationForm

