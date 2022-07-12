from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from .views import SignInView, SignUpView, ShortUrlView, UrlsView

urlpatterns = [
    path('', TemplateView.as_view(template_name="shortener/index.html"), name='index'),
    path('signin', SignInView.as_view(), name='signin'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('shortener', ShortUrlView.as_view(), name='shortener'),
    path('urls', UrlsView.as_view(), name='my_urls'),
    path('<str:short_url>', ShortUrlView.redirect_url, name='redirect'),
]
