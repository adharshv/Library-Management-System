from django.shortcuts import render, redirect


from borrower.models import borrower
from django.forms import ModelForm

class BorrowerForm(ModelForm):
    class Meta:
        model = borrower
        fields = ['card_id','ssn','bname','address','phone']
        ordering = ['card_id']

# Create your views here.
def index(request):
    allborrowers = borrower.objects.all()
    print(allborrowers)
    return render(request, template_name='borrower_index.html', context={
        "borrowers": allborrowers
    })

def new(request):
    borrowerform = {
        "form" : BorrowerForm()
    }
    return render(request, 'borrower_new.html', context=borrowerform)   

def create(request):
    a = BorrowerForm(request.POST)
    if a.is_valid():
        saved_borrower = a.save()
        borrower_id = saved_borrower.card_id

        # return redirect('borrower_index')
        return render(request, template_name='borrower_added.html', context={
            "borrower_id": borrower_id
        })

    else:
        return render(request, template_name='borrower_val_fail.html') 

def view(request, card_id):

    try:
        a = borrower.objects.get(card_id=card_id)
    except:
        return render(request, template_name='borrower_val_fail.html') 

    return render(request, 'borrower_view.html', context = {"borrower": a})