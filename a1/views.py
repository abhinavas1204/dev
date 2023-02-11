from django.shortcuts import render
from django.http import HttpResponse
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)




def home(request):
    return render(request,'switch.html')


def lamp1_on(request):
    GPIO.output(2,0)
    return HttpResponse('''<html><script> window.location.replace('/a1/home');</script></html> ''')
    
def lamp1_off(request):
    GPIO.output(2,1)
    return HttpResponse('''<html><script> window.location.replace('/a1/home');</script></html> ''')
    
def lamp2_on(request):
    GPIO.output(4,0)
    return HttpResponse('''<html><script> window.location.replace('/a1/home');</script></html> ''')
    
def lamp2_off(request):
    GPIO.output(3,1)
    return HttpResponse('''<html><script> window.location.replace('/a1/home');</script></html> ''')
    
def lamp3_on(request):
    GPIO.output(4,0)
    return HttpResponse('''<html><script> window.location.replace('/a1/home');</script></html> ''')
    
def lamp3_off(request):
    GPIO.output(4,1)
    return HttpResponse('''<html><script> window.location.replace('/a1/home');</script></html> ''')
    
def lamp4_on(request):
    GPIO.output(17,0)
    return HttpResponse('''<html><script> window.location.replace('/a1/home');</script></html> ''')
    
def lamp4_off(request):
    GPIO.output(17,1)
    return HttpResponse('''<html><script> window.location.replace('/a1/home');</script></html> ''')

def all_off(request):
    GPIO.output(2,1)
    GPIO.output(3,1)
    GPIO.output(4,1)
    GPIO.output(17,1)
    print("all lamps are offed")
    return HttpResponse('''<html><script> window.location.replace('/a1/home');</script></html> ''')