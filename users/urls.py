
from .views import UserRegisterViewset
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import*

router = DefaultRouter()

router.register(r'register',UserRegisterViewset,basename='register')

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('otp/', UserLoginWithOtpView.as_view(), name='otp'),

]

urlpatterns+= router.urls