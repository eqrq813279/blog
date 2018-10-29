from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    return HttpResponse('Hello world!')