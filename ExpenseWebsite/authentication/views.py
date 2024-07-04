from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email

# Create your views here.
class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body) #contains everything entered by user
        username = data['username']

        # if it doesn't contains alphanumeric characters
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username should only contain alphanumeric characters'}, status=400)
        
        # if username is already taken
        # check database
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Sorry, this username is already taken. Please try another one'}, status=409)
        
        return JsonResponse({'username_valid': True})

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body) #contains everything entered by user
        email = data['email']

        # if its in a valid email format
        # pipenv install validate-email
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        
        # if username is already taken
        # check database
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry, this email is already taken. Please try another one'}, status=409)
        
        return JsonResponse({'email_valid': True})
