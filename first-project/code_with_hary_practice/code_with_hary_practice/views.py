from django.http import HttpResponse;
import os
from django.shortcuts import render

def index(request):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '1.txt')
    with open(file_path, 'r') as file:
        content = file.read()

    return HttpResponse(content,content_type='text/html')

def about(request):
    # get the text from form thar are sent by contact form
    formData = request.GET.get('text','default')
    uppercase = request.GET.get('uppercase','off')
    removePuntuations=request.GET.get('removePuntuations','off')

    print(formData)
    print(removePuntuations)
    analyzedText=''
    puntuations  = '''!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''

    for char in formData:
        if removePuntuations == 'on':
            if char not in puntuations:
                analyzedText+=char
    for char in analyzedText:
        if uppercase =='on':
             analyzedText = analyzedText.upper()
    params ={'data' : analyzedText}
    print(params)
    return render(request,'analyzedText.html',params)
    
def contact(request):
    return render(request,'index.html')