from django.shortcuts import render,redirect

# Create your views here.
from book_loan.models import book_loan 
from book.models import book
from borrower.models import borrower
from fine.models import fine
from django.forms import ModelForm
from django.core.exceptions import ValidationError
import datetime

class BookForm(ModelForm):
    class Meta:
        model = book_loan
        fields = ['book','borrower']


def index(request):
    allbook_loans = book_loan.objects.all()
    print(allbook_loans)
    return render(request, template_name='book_loan_index.html', context={
        "book_loans": allbook_loans
    })

def new(request, isbn):
    # borrowers_list = borrower.objects.all().order_by("card_id")

    try:
        loan_book=book.objects.get(isbn=isbn) #getting the book object
    except:
        return render(request, template_name='fine_val_fail.html') 


 

    # book_form = BookForm(initial={'book':loan_book}) #setting one field of the bookform
    # book_form.fields["book"].widget.attrs["readonly"]="readonly" #disabling the book field
    # book_form.fields["book"].widget.attrs["style"]="visibility: hidden;" #disabling the book field
    # bookform = { 
    #     "loan_book":loan_book,
    #     "form":book_form
    # }

    return render(request, template_name='book_loan_new.html', context={
        "isbn" : isbn
    }
    )

def create(request):

    b = str(request.POST.get("textfield",None)) #only one word

    try:
        borrower_obj = borrower.objects.get(card_id = b) # get the borrower object
    except:
        return render(request, template_name='book_loan_val_fail.html') 
    # print(borrower_obj)

    a = str(request.POST.get("isbn",None))

    # print(a)

    try:
        book_obj = book.objects.get(isbn = a) # get the borrower object
    except:
        return render(request, template_name='book_loan_val_fail.html') 

    

    # Happens only for available books. So no need for another validation.
    
    
    if borrower_obj.loans == 3 : # borrower has already reached his loans limit
        return render(request, template_name='book_loan_fail.html', context={
        "borrower_obj": borrower_obj
    })

    print(book_obj)

    c = book_loan(book = book_obj, borrower = borrower_obj)
    c.save() # creating a book loan object
    created_book_loan = c
    # print(created_book_loan)
    
    # borrower_obj = created_book_loan.borrower

    # book_obj = created_book_loan.book

    borrower_obj.loans = borrower_obj.loans + 1 # incrementing pending book loans 
    
    borrower_obj.save()

    # setting availability = False
    book_obj.avail = False
    book_obj.save()

    f=fine(book_loan=created_book_loan) # creating a fine entry for the book loan
    f.paid = False
    f.save()

    
    return render(request, template_name='loan_success.html', context={
        "book_obj": book_obj,
        "borrower_obj" : borrower_obj
    })


 
def return1(request, isbn):
    try:
        book_obj =book.objects.get(isbn=isbn) #getting the book object
    except:
        return render(request, template_name='book_loan_val_fail1.html')

    
    loans_for_book = book_loan.objects.filter(book = book_obj)

    for eachloan in loans_for_book:
        if eachloan.date_in is None:
            borrower_obj = eachloan.borrower
            book_loan_obj = eachloan

    # book_form = BookForm(initial={'book':loan_book}) #setting one field of the bookform
    # book_form.fields["book"].widget.attrs["readonly"]="readonly" #disabling the book field
    # book_form.fields["book"].widget.attrs["style"]="visibility: hidden;" #disabling the book field
    # bookform = { 
    #     "loan_book":loan_book,
    #     "form":book_form
    # }

    flag=0

    #print(borrower_obj.books)

    for eachbook in borrower_obj.books(): #checking whether the entered fields are valid: active borrower - book pair
        
        if eachbook.isbn == book_obj.isbn and book_loan_obj.date_in is None:
            flag = 1

    if flag != 1:
        return render(request, template_name='book_loan_absent.html', context={
        "borrower_obj": borrower_obj,
        "book_obj" : book_obj
    })

    


    borrower_obj.loans = borrower_obj.loans - 1 #decrementing number of active book loans
    borrower_obj.save()

    book_loan_obj.date_in = datetime.date.today() #setting current date as the date_in
    book_loan_obj.save()

    book_obj.avail = True
    book_obj.save()

    return render(request, template_name='closure_success.html', context={
        "borrower_obj": borrower_obj,
        "book_obj" : book_obj
    })

   


    