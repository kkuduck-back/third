from django.urls import path
from . import views

app_name = 'user_api'

urlpatterns = [
    path('users/', views.UserView.as_view()),
    path('users/<int:uid>', views.UserView.as_view()),
    path('subsciptions/', views.SubView.as_view()),
    path('subsciptions/<int:uid>', views.SubView.as_view()),
    path('defaultsubsciptions/', views.DefaultSubView.as_view()),
    path('defaultsubsciptions/<int:uid>', views.DefaultSubView.as_view()),
    # path('plans/', views.PlanView.as_view()),
]