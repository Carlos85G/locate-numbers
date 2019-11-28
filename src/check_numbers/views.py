from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Function exempt from CSRF verification for CURL access
def index(request):
    # Default GET response
    return HttpResponse('This is the API\'s main URL. It will not process any data. What you\'re looking for is at "/locate_numbers"')
