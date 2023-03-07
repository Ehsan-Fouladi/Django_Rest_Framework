from . import views
from django.urls import path
from rest_framework.authtoken import views as auth_token
from rest_framework import routers

app_name = 'account'
urlpatterns = [
    path('register/', views.RegisterAPI.as_view()),
    path('auth_token/', auth_token.obtain_auth_token),
]

router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls