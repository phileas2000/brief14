from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

import pickle



from django import forms
 
# creating a form
class UploadFileForm(forms.Form):
 
    file = forms.FileField()
    



def post(request):
    
    #messages.add_message(request, messages.INFO, 'Hello world.')
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():    
            file =request.FILES['file']
            file = file.read()
            output = open('static/immo_CSV.csv', 'wb')
            output.write(file)
            output.close()
    return render(request, 'uploadImage.html')


def main(request):
    if request.method == 'POST':
        return post(request)
    else:

        return render(request, 'uploadImage.html')

