from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse


def home(request):
    return render(request, 'index.html')

def browse(request):
    return render(request, 'browse.html')

def details(request):
    return render(request, 'details.html')

def streams(request):
    return render(request, 'streams.html')

def profile(request):
    return render(request, 'profile.html')

# def go_to_portfolio(request):
#     return redirect(reverse('portfolioPage:home')) 

# def go_to_meta(request):
#     return redirect(reverse('metaAPP:home'))

# def go_to_landing(request):
#     return redirect(reverse('landing:home'))

def go_to_projects(request):
    app_env_home_url = reverse('app_env:home')
    return redirect('base.html')