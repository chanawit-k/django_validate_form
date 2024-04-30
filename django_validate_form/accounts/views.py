from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class SampleView(TemplateView):
    template_name = "accounts/sample_html.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add your context variables here
        context['test_context'] = 'value from views'
        return context

