from django.urls import path, include
from .views import RegistrationAPIView, SignInView, SignOutView

urlpatterns = [
    path('sign-in/', SignInView.as_view(), name='sign_in'),
    path('sign-out/', SignOutView.as_view(), name='sign_out'),
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
]
