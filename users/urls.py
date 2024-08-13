from django.urls import path
from .views import UserSignUpView, CustomLoginView, dashboard

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
]

