from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect

from .forms import SignUpForm, SignInForm, UrlForm
from .models import Urls


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'shortener/signup.html', context={'form': form, })

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'shortener/signup.html', context={'form': form, })


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'shortener/signin.html', context={'form': form, })

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'shortener/signin.html', context={'form': form, })


class ShortUrlView(View):
    def get(self, request, *args, **kwargs):
        form = UrlForm()
        return render(request, 'shortener/shortener.html', context={'form': form, })

    def post(self, request, *args, **kwargs):
        form = UrlForm(request.POST)
        if form.is_valid():
            user = self.request.user
            full_url = form.cleaned_data['full_url']
            Urls.objects.create(user=user, full_url=full_url)
            return render(request, 'shortener/shortener.html',
                          context={'form': form, 'url': Urls.objects.filter(user=user, full_url=full_url).last()})
        return render(request, 'shortener/shortener.html', context={'form': form, })

    def redirect_url(request, short_url):
        url = get_object_or_404(Urls, short_url=short_url)
        return redirect(url.full_url)


class UrlsView(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        urls = Urls.objects.filter(user=user)

        paginator = Paginator(urls, 8)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'shortener/myurls.html', context={'urls': page_obj})
