from django.urls import path
from tellme import views
from django.contrib.auth import views as auth_views

app_name = 'tellme'

urlpatterns = [
    path('',views.home,name="index"),
    path('login/',auth_views.login,{'template_name': 'form.html'},name='login'),
    path('logout/',auth_views.logout,{'template_name': 'home.html'}),
    path('signup/', views.signup,name="signup"),
    path("form/",views.test),
    path('profile/', views.profile,name="profileupdate"),
    path('viewshout/',views.viewshout,name='viewshout'),

    path("<username>/",views.propage,name="profile"),

]