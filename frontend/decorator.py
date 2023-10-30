from django.shortcuts import redirect
from rest_framework_simplejwt.tokens import UntypedToken

def authorise(view_func):
    def wrapper(request, *args, **kwargs):
        token = request.session.get('access_token')
        try:
            data = UntypedToken(token)
            if data:
                return redirect('home')
        except Exception as e:
            # Handle the error, in this case, you can redirect to the login page
            return redirect('login')  # Replace 'login_url' with the actual URL of your login page
        return view_func(request, *args, **kwargs)

    return wrapper

def emailverification(view_func):
    def wrapper(request, *args, **kwargs):
        token = request.session.get('access_token')
        try:
            data = UntypedToken(token)
            if data:
                return redirect('home')
        except Exception as e:
            # Handle the error, in this case, you can redirect to the login page
            return redirect('login_otp')  # Replace 'login_url' with the actual URL of your login page
        return view_func(request, *args, **kwargs)

    return wrapper

def otpverification(view_func):
    def wrapper(request, *args, **kwargs):
        token = request.session.get('access_token')
        try:
            data = UntypedToken(token)
            if data:
                return redirect('home')
        except Exception as e:
            # Handle the error, in this case, you can redirect to the login page
            return redirect('verify_otp')  # Replace 'login_url' with the actual URL of your login page
        return view_func(request, *args, **kwargs)

    return wrapper

