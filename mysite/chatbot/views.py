from django.shortcuts import render , redirect
from .English_Main import get_responsebot as english_response 
from .Hinglish_Main import get_response  as hinglish_response
from .Neural_Main import chatbot_response as Neural_response

# Create your views here.
def process_input(request):
    result = None

    if request.method == 'POST':
        user_input = request.POST.get('data', '')
        language = request.POST.get('language', '')
        model = request.POST.get('model', '')   
        
        print(language)
        
        if language == 'english':
            result = english_response(user_input)
        else:
            result = hinglish_response(user_input)
            
        if model == 'neural':
            result = Neural_response(user_input)
        
    return render(request, 'index.html', {'result': result})