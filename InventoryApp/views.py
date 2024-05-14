from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from InventoryApp.models import User,Cashier,Products,Category,Loghistory
from django.db import IntegrityError
from .forms import RoleSelectionForm
from collections import Counter
from decimal import Decimal,ROUND_HALF_UP
# Create your views here.

def landing(request):
    # a = User.objects.create(name='admin', password='pass')
    return render(request, 'index.html')

def user_login1(request):
    return render(request, 'loginn.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('cusername')
        name = request.POST.get('cname')
        email = request.POST.get('cemail')
        phone = request.POST.get('cphone')
        aadhar = request.POST.get('caadhar')
        password = request.POST.get('cpassword')
        cdate = request.POST.get('cdate') 

        try:
            print("Date from form:", cdate)
            cashier = Cashier.objects.create(
                cusername=username,
                cname=name,
                cdate=cdate,
                cemail=email,
                cphone=phone,
                caadhar=aadhar,
                cpassword=password
            )
            return redirect('rgr')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('rgr')
    c=Cashier.objects.all()
    return render(request, 'register.html',{"Cashiers": c})
# return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        form = RoleSelectionForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            if role == 'admin':
                g = User.objects.get(name=request.POST['username'])
                if request.POST['password'] == g.password:
                    print("Success")
                    return redirect('/main/')
            elif role == 'cashier':
                g = Cashier.objects.get(cusername=request.POST['username'])
                if request.POST['password'] == g.cpassword:
                    print("Success1")
                    return redirect('/clist/')
    else:
        form = RoleSelectionForm()  # Ensure the form is instantiated here
    return render(request, 'login.html', {'form': form})


def mainpage(request):
    return render(request, 'mainpage.html')

def Cashier_page(request):
    return render(request, 'cashierpage.html')

def about(request):
    return render(request, 'about.html')

def category(request):
    if request.method == "POST":
        name1=request.POST.get('Text')
        a=Category.objects.create(name=name1)
    a=Category.objects.all()[1:]
    print(a)
    
    return render(request, 'category.html',{'Category':a})

def product(request):
    if request.method == "POST":
        name1 = request.POST.get('Text')
        name2 = request.POST.get('Text1')
        name3 = request.POST.get('Text2')
        name4 = request.POST.get('Text3')
        print(name4)
        b=Category.objects.get(name=name4)
        a = Products.objects.create(pname=name1, price=name2,quantity=name3,category_id=b.id,category=b.name)
    z=Products.objects.all()
    y=Category.objects.all()
    return render(request, 'products.html',{'Products':z,'Category':y})

def productedit(request,pid):
    a=Products.objects.get(id=pid)
    if request.method == 'POST':
        a.pname=request.POST.get('namep')
        a.price=request.POST.get('pricep')
        a.quantity=request.POST.get('quantityp')
        a.save()
        return redirect('/pdt/')
    return render(request,'productsedit.html',{'Product':a})

def productdelete(request,pid):
    a=Products.objects.get(id=pid)
    a.delete()
    return redirect('/pdt/')

def categoryedit(request, cid):
    a=Category.objects.get(id=cid)
    if request.method == 'POST':
        a.name=request.POST.get('namec')
        a.save()
        return redirect('/ctg/')
    return render(request,'categoryedit.html',{'Category':a})

def categorydelete(request,cid):
    a=Category.objects.get(id=cid)
    b=Products.objects.filter(category_id=cid)
    a.delete()
    b.delete()
    return redirect('/ctg/')

def viewcashier(request, id):
    a=Cashier.objects.get(id=id)
    return render(request, 'viewcashier.html',{"Cashier":a})

def editcashier(request, id):
    a=Cashier.objects.get(id=id)
    if request.method == 'POST':
        a.cusername = request.POST.get('cusername')
        a.cname = request.POST.get('cname')
        a.cdate = request.POST.get('cdate')
        a.cemail = request.POST.get('cemail')
        a.cphone = request.POST.get('cphone')
        a.caadhar = request.POST.get('caadhar')
        a.cpassword = request.POST.get('cpassword')
        a.save()
        return redirect('rgr')
    return render(request, 'editcashier.html',{"cashier":a})

def deletecashier(request, id):
    a=Cashier.objects.get(id=id)
    a.delete()
    return redirect('/reg/')

def itemslist(request):
    a=Products.objects.all()
    return render(request,'itemslist.html',{'list':a})

l=[]
def adding(request,id):
    l.append(id)
    a=Products.objects.get(id=id)
    a.quantity-=1
    a.save()
    return redirect('list')

def removing(request,id):
    l.remove(id)
    a=Products.objects.get(id=id)
    a.quantity+=1
    a.save()
    return redirect('list')

def cart(request):    
    item_frequencies = Counter(l)
    price=0
    l1=[]
    for item, frequency in item_frequencies.items():
        a=Products.objects.get(id=item)
        a.quantity=frequency
        price+=a.price*frequency
        l1.append(a)
    gst=price* Decimal('0.18')
    total=price+price* Decimal('0.18')
    gst = gst.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    total = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    print(price,gst,total)
    return render(request,'cart.html',{'list':l1,'price':price,'gst':gst,'total':total})

def button(request):
    result_string = ','.join(str(x) for x in l)
    print(result_string)
    a=Loghistory.objects.create(data=result_string)
    l.clear()
    return redirect('/cart/')

def history(request):
    z=Loghistory.objects.all()
    l1=[]
    for i in z:
        b=i.data
        l1.append(f"Bill id: {i.id}")
        list1=b.split(",")
        my_list = [int(x) for x in list1]
        item_frequencies = Counter(my_list)
        price=0
        for item, frequency in item_frequencies.items():
            a=Products.objects.get(id=item)
            a.quantity=frequency
            price+=a.price*frequency
            l1.append(a)
    print(l1)
    return render(request,'history.html',{'list':l1})

def viewcat(request,id):
    a=Products.objects.filter(category_id=id)
    return render(request,'viewcat.html',{'list':a})

def citemslist(request):
    a=Products.objects.all()
    return render(request,'cashierlogin.html',{'list':a})

def ccart(request):    
    item_frequencies = Counter(l)
    price,total=0,0
    l1=[]
    for item, frequency in item_frequencies.items():
        a=Products.objects.get(id=item)
        a.quantity=frequency
        price+=a.price*frequency
        l1.append(a)
    gst=price* Decimal('0.18')
    total=price+price* Decimal('0.18')
    gst = gst.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    total = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return render(request,'cashiercart.html',{'list':l1,'price':price,'gst':gst,'total':total})

# l=[]
def cadding(request,id):
    l.append(id)
    a=Products.objects.get(id=id)
    a.quantity-=1
    a.save()
    return redirect('clist')

def cremoving(request,id):
    l.remove(id)
    a=Products.objects.get(id=id)
    a.quantity+=1
    a.save()
    return redirect('clist')

def cbutton(request):
    result_string = ','.join(str(x) for x in l)
    print(result_string)
    a=Loghistory.objects.create(data=result_string)
    l.clear()
    return redirect('/ccart/')