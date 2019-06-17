from django.shortcuts import render, redirect

from django.contrib.postgres.search import SearchVector

from book.models import book
# from author.models import author
# from book_author.models import book_author
from book_loan.models import book_loan
from django.forms import ModelForm
from book_return.models import book_return
from borrower.models import borrower


class Book_returnForm(ModelForm):
    class Meta:
        model = book_return
        fields=["Borrower_ID_name_or_ISBN"]
        

def index(request):
    book_returnform = {
        "form" : Book_returnForm()
    }
    return render(request, template_name='book_return_index.html', context=book_returnform)  


def results(request):
   

    b = str(request.GET["Borrower_ID_name_or_ISBN"])
    
    
    l=[]
    l=b.split(' ')
    res = []
    res1=[]
    res2=[]
  
    for x in l: #for each word in search query
        
        try:
            res.append(book.objects.get(isbn=x))
           
        except:
            res = []

        # print(res)

        

        # book_obj = book.objects.get(isbn = x)
        try:
            borrower_obj = borrower.objects.get(card_id=x) 
            
            res1=borrower_obj.books()
        except:
            res1=[]

        
        # print(res3)

        # print(borrower.objects.get(card_id = 1))
        # print(res1)

        res2 = borrower.objects.filter(bname__icontains=x)

         

    # for obj in res1:
    #     if obj.card_id == 1:
    #         print(obj.books())

    # print(res1)

    # allbooks = book.objects.all()
    # print(res)
    # print(res1)
    # print(res2)
    return render(request, template_name='book_return_results.html', context={
        "res": res,
        # "book_obj":book_obj,
        "res1":res1,
        "res2":res2,
        # "books": allbooks,
        
    })
        