from django.shortcuts import render, get_object_or_404, redirect
from .models import Items, Orders

# Create your views here.
def home(request):
    items = Items.objects.all()

    return render(request, 'home.html', {'items' : items})

def desc(request,uname, id):

    if request.method == 'POST':
        print("if part desc")
        address = request.POST['address']
        phone = request.POST['phone']
        quantity = request.POST['quantity']

        order = Orders(address=address, phone=phone, quantity=quantity, cus_uname=uname, item_id=id)
        order.save()
        print("order_placed")
        return redirect('end')

    else:
        item = get_object_or_404(Items,item_id=id)
        return render(request,'desc.html',{'item':item})

def end(request):
    return render(request, 'end.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
    
def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')
