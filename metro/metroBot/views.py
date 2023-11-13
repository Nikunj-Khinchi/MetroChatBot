from django.shortcuts import render
from .English_Main import get_responsebot
# Create your views here.
def index(request):
    result = None

    if request.method == 'POST':
        user_input = request.POST.get('data', '')
        result = get_responsebot(user_input)
    return render(request, 'index.html' , {'result': result})

def process_input(request):
    result = None

    if request.method == 'POST':
        user_input = request.POST.get('data', '')
        result = get_responsebot(user_input)

    return render(request, 'index.html', {'result': result})