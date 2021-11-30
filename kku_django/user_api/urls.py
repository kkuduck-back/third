from django.urls import path
from . import views

app_name = 'user_api'

urlpatterns = [
    path('users/', views.UserView.as_view()),
    path('users/<int:uid>', views.UserView.as_view()),
    path('subscriptions/', views.SubView.as_view()),
    path('subscriptions/<int:uid>', views.SubView.as_view()),
    path('defaultsubscriptions/', views.DefaultSubView.as_view()),
    path('defaultsubscriptions/<int:uid>', views.DefaultSubView.as_view()),
    # path('plans/', views.PlanView.as_view()),
]