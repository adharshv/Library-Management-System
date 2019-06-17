from django.shortcuts import render, redirect


from book.models import book
from django.forms import ModelForm

class BookForm(ModelForm):
    class Meta:
        model = book
        fields = ['title','isbn']

# Create your views here.
def index(request):
    allbooks = book.objects.all()
    print(allbooks)
    return render(request, template_name='book_index.html', context={
        "books": allbooks
    })

def new(request):
    bookform = {
        "form" : BookForm()
    }
    return render(request, 'book_new.html', context=bookform)   

def create(request):
    a = BookForm(request.POST)
    if a.is_valid():
        a.save()
    else:
        return render(request, template_name='book_val_fail.html') 

    return redirect('book_index')

def view(request, isbn):
    try:
        a = book.objects.get(isbn=isbn)
    except:
        return render(request, template_name='book_val_fail.html')

    return render(request, 'book_view.html', context = {"book": a})