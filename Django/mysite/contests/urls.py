from django.urls import path

from . import views


urlpatterns = [
    path('', views.contest_list, name='contest_list'),
    path('create/', views.create_contest, name='create_contest'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('<int:contest_id>/signup/', views.contest_signup, name='contest_signup'),
]
