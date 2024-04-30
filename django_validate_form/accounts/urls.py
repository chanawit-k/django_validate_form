from django.contrib.auth.views import logout_then_login
from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('',views.SampleView.as_view(),name='test_template'),
    path('signup',views.SignUpView.as_view(),name='signup')
]
