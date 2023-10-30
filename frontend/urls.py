from django.urls import path
from .import views
urlpatterns = [
    path('login/',views.login_page,name='login'),
    path('register',views.register_page,name='register'),

    path('emailverification',views.login_otp_page,name='login_otp'),
    path('emailverification/otp',views.otp_page,name='verify_otp'),
    path('',views.home_page,name='home'),


    path('all_events/', views.all_events, name='all_events'), 
    
]
