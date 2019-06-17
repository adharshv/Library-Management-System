from django.shortcuts import render, redirect

from django.contrib.postgres.search import SearchVector

from book.models import book
from author.models import author
from book_author.models import book_author
from book_loan.models import book_loan
from django.forms import ModelForm
from book_search.models import book_search
# from time import sleep

class Book_searchForm(ModelForm):
    class Meta:
        model = book_search
        fields=['ISBN_title_or_author']
        

def index(request):
    book_searchform = {
        "form" : Book_searchForm()
    }
    return render(request, template_name='book_search_index.html', context=book_searchform)  

# def view(request, isbn):
#     a = book.objects.get(isbn=isbn)

#     return render(request, 'book_search_view.html', context = {"book": a})

def results(request):
   

    b = str(request.GET["ISBN_title_or_author"])
    
    
    l=[]
    l=b.split(' ')
  
    for x in l:
        res = book.objects.filter(title__icontains=x) 

        res2 = book.objects.filter(isbn__icontains=x)

        res1 = author.objects.filter(name__icontains=x)
        

    allbooks = book.objects.all()

    return render(request, template_name='book_search_results.html', context={
        "res": res,
        "res2":res2,
        "res1":res1,
        "books": allbooks
    })
        
    

# '''
    #     {% for eachbook in res %}
    #         {{eachbook.title}}
    #         {{eachbook.isbn}}
    #         {% for eachauthor in eachbook.authors %}
    #             {{ eachauthor.name }}
    #         {% endfor %}
    #     {% endfor %}
    # '''
    
