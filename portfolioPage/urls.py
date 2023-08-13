from django.urls import path
from portfolioPage import views
app_name = 'portfolio' 
urlpatterns = [
    path('',views.home, name='home'),
    path('browse/',views.browse, name='browse'),
    path('details/',views.details, name='details'),
    path('streams/',views.streams, name='streams'),
    path('profile/',views.profile, name='profile'),
    path('go_to_projects/', views.go_to_projects, name='go_to_projects'),
    path('go_to_portfolio/', views.home, name='go_to_portfolio'),
]
