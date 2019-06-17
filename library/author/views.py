from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.http import request, response
from django.forms import ModelForm
# Create your views here.

from author.models import author

class AuthorForm(ModelForm):
    class Meta:
        model = author
        fields = ['name']

def index(request):
    allauthors = author.objects.all()
    return render(request, 'author_index.html', context={
        "authors":allauthors
    })
    
def new(request):
    authorform = {
        "form" : AuthorForm()
    }
    return render(request, 'author_new.html', context=authorform)

def create(request):
    a = AuthorForm(request.POST)
    if a.is_valid():
        a.save()
    else:
        return render(request, template_name='validation_fail.html') 


    return redirect('author_index')

def view(request, author_id):
    try:
        a = author.objects.get(author_id=author_id)
    except:
        return render(request, template_name='validation_fail.html')

    return render(request, 'author_view.html', context = {"author": a})
