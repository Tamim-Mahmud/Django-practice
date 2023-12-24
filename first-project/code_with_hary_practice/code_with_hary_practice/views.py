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
    print(formData)
    return HttpResponse("This is tamim mahmud")
def contact(request):
    
    return render(request,'index.html')