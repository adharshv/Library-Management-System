from django.shortcuts import render, redirect

# Create your views here.
from fine.models import fine 
from book_loan.models import book_loan
from borrower.models import borrower
from book.models import book
# from django.forms import ModelForm

from django import forms



def index(request):
        return render(request, template_name='fine_index.html') 

# def index(request):
#     allfines = fine.objects.all()
#     print(allfines)
#     return render(request, template_name='fine_index.html', context={
#         "allfines": allfines
#     })

def results(request):
   
    
    
    b = str(request.POST.get("textfield",None)) #only one word 
    
    try:
        borrower_obj = borrower.objects.get(card_id = b) # get the borrower object
    except:
        return render(request, template_name='fine_val_fail.html') 

    # print(borrower_obj)

    book_loan.objs = book_loan.objects.filter(borrower = borrower_obj) # get the loans of the borrower

    # print(book_loan.objs)

    fine_objs = []

    for eachloan in book_loan.objs:
        # print(eachloan)
        fine_objs.append(fine.objects.get(book_loan = eachloan)) # getting list of fine objects

    sum1=0   

    for eachfine in fine_objs: # calculating total unpaid fine_amt

        if eachfine.paid == False:
            sum1 += eachfine.fine_amt

    #print(sum1)

    

    # fine_objs_paid = []

    # fine_objs_unpaid = []

    # for each_fine_obj in fine_objs:
    #     if each_fine_obj.paid ==True and each_fine_obj.fine_amt > 0 :
    #         fine_objs_paid.append(each_fine_obj)
    #     elif each_fine_obj.paid ==False and each_fine_obj.fine_amt > 0 :
    #         fine_objs_unpaid.append(each_fine_obj)
        
        

    return render(request, template_name='fine_results.html', context={
        "fine_objs" : fine_objs,
        # "fine_objs_paid": fine_objs_paid,
        # "fine_objs_unpaid": fine_objs_unpaid,
        "sum1": sum1,
        "borrower_obj" : borrower_obj
    })

def create(request): # to refresh all fines in the system

    all_loans = book_loan.objects.all()
    
    for eachloan in all_loans:
        # print(eachloan.get_days_passed())
        # print(eachloan.date_out)
        # print(eachloan.due_date)
        # print(eachloan.date_in)
        if eachloan.get_days_passed() > 0:

            thisfine = fine.objects.get(book_loan = eachloan)
            if thisfine.paid == False: # doing only for unpaid fines
                days = eachloan.get_days_passed()
                print(days)
                thisfine.fine_amt = 0.25 * days 
                # thisfine.paid = False 
                thisfine.save()
                    
    return redirect('fine_index')

def pay(request, card_id):

    
    # print(card_id)


    borrower_obj = borrower.objects.get(card_id = card_id)

    book_loan.objs = book_loan.objects.filter(borrower = borrower_obj)

    for eachloan in book_loan.objs:
        # print(eachloan)
        #thisbook= book.objects.get(isbn=eachloan.book.isbn) # get each book ever loaned by this borrower
        
        # if thisbook.avail != True and eachloan.borrower = borrower_obj:


        if eachloan.get_days_passed() > 14 :
            if eachloan.date_in is None :
                return render(request, template_name='fine_pay_fail.html')

        thisfine = fine.objects.get(book_loan=eachloan)
        thisfine.paid = True
        thisfine.save()

    return render(request, template_name='fine_pay_success.html')
    