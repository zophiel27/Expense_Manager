from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email # type: ignore
from django.contrib import messages
# Create your views here.
class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    def post(self, request):
        #messages.warning(request, 'This is a warning message')
        #messages.error(request, 'This is an error message')
        #messages.success(request, 'This is a success message')
        #messages.info(request, 'This is an info message')
        
        # get user data
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }        
        # validate user data
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 8:
                    messages.error(request, 'Password too short')
                    return render(request, 'authentication/register.html', context)
                User.objects.create_user(username=username, email=email, password=password) # user module to create user
                messages.success(request, 'Account created successfully')
                return render(request, 'authentication/register.html')
            else:
                messages.error(request, 'Email is already taken')
                return render(request, 'authentication/register.html')




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
