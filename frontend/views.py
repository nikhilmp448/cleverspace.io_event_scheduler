from django.shortcuts import render,redirect
from rest_framework_simplejwt.tokens import UntypedToken
from django.contrib import messages
from django.http import JsonResponse
from .decorator import authorise,emailverification,otpverification
import requests
import json

""" in the below code we are trying to login using the credentials from template and parse those credentials to our Rest API 
    the Rest API validates the credentials and returns a JWT token that we stores in session to pass token in header for other API requests
"""

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # Create a dictionary with the data you want to send as JSON
        data = {
            "email": email,
            "password": password
        }
        # Convert the data dictionary to JSON
        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        # Make a POST request to the external RESTAPI
        api_url = 'https://cleverspace.onrender.com/api/user/login/'
        response = requests.post(api_url, data=json_data, headers=headers)

        if response.status_code == 200 :
            response_data = response.json()
            # Access the 'access_token' field from the response data
            access_token = response_data.get('access_token', None)
            # Save the access token in the session
            request.session['access_token'] = access_token
            # Save the session to make sure the access_token is stored
            request.session.save()


            """ uncomment the below code if you want to check token sored or not"""
            # stored_value = request.session.get('access_token', 'Default Value if not found')
            # print(stored_value)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    return render(request,'login.html')


def register_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        # Create a dictionary with the data you want to send as JSON
        data = {
            "email": email,
            "firstname":firstname,
            "lastname":lastname,
            "password": password
        }
        # Convert the data dictionary to JSON
        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        # Make a POST request to the external RESTAPI
        api_url = 'https://cleverspace.onrender.com/api/user/register/'
        response = requests.post(api_url, data=json_data, headers=headers)
        if response.status_code == 201 :
            return redirect('login')
    return render(request,'register.html')


def login_otp_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        data = {
                "email": email,
            }
        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        # Make a POST request to the external RESTAPI
        api_url = 'https://cleverspace.onrender.com/api/user/otp/'
        response = requests.post(api_url, data=json_data, headers=headers)
        if response.status_code == 200 :
            return redirect('verify_otp')
    return render(request,'login_with_otp.html')


def otp_page(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        
        # Define the parameters as a dictionary
        params = {
            "otp": otp,
        }
        
        # Make a GET request to the external REST API with parameters using the params keyword
        api_url = 'https://cleverspace.onrender.com/api/user/otp/'
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            response_data = response.json()
            # Access the 'access_token' field from the response data
            access_token = response_data.get('access_token', None)
            # Save the access token in the session
            request.session['access_token'] = access_token
            # Save the session to make sure the access_token is stored
            request.session.save()
            return redirect('home')
        else:
            messages.error(request, 'something went wrong or please try after sometime')
    return render(request,'otp.html')
    

def home_page(request):
    is_valid = None
    try:
        token = request.session.get('access_token')
        data = UntypedToken(token)
        if data != None:
            is_valid = True
        else:
            is_valid = False
    except Exception as e: 
        is_valid = False
    context = {"token":token,"is_valid":is_valid}
    return render(request,'home.html',context)


def all_events(request):                                                                                                 
    token = request.session.get('access_token')
    headers = {
    "Authorization": f"Bearer {token}"  # For a bearer token
    }
    api_url = 'https://cleverspace.onrender.com/api/tasks/'
    response = requests.get(api_url, headers=headers)
    out = [] 
    if response.status_code == 200:
        all_events = response.json()                                                                               
                                                                                                                
        for event in all_events:                                                                                             
            out.append({                                                                                                     
                'title': event['title'],                                                                                         
                'id': event['id'],                                                                                              
                'start': event['start'],                                                         
                'end': event['end'],                                                             
            })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False) 
 

