from django.urls import path
from .views import LoginView, CheckAuthenticated, LogoutView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("check/", CheckAuthenticated.as_view(), name="check_authenticated"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
