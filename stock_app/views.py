from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from stock_app.forms import Login_form, register_form1, StockForm
from stock_app.models import register, stock


# Create your views here.
def index(request):
    return render(request,"index.html")

@login_required(login_url='loginpage')
def dashboard(request):
    return render(request,"dashboard.html")


def logout_view(request):
    logout(request)
    return redirect("loginpage")


def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pass")
        user = authenticate(request,username=username,password=password)
        if user is not None :
            login(request,user)
            if user.is_staff :
                return redirect("base")
            if user.is_customer :
                return redirect("customerbase")
        else :
            messages.info(request,"Invalid credentials")

    return render(request,"login.html")



####################ADMIN######################
@login_required(login_url='loginpage')
def base(request):
    return render(request,"admin/adminbase.html")


@login_required(login_url='loginpage')
def stock_add(request):
    form = StockForm()
    if request.method =='POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("stock_view")
    return render(request,'admin/stock_add.html',{'form':form})

@login_required(login_url='loginpage')
def stock_view(request):
    data = stock.objects.all()
    return render(request,'admin/stock_view.html',{'data':data})


@login_required(login_url='loginpage')
def delete_stock_view(request,id):
    wm = stock.objects.get(id=id)
    wm.delete()
    return redirect("stock_view")

#this is to delete work

@login_required(login_url='loginpage')
def update_stock_view(request,id):
    a = stock.objects.get(id=id)
    form = StockForm(instance=a)
    if request.method == 'POST':
        form = StockForm(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('stock_view')

    return render(request,'admin/update_stock_view.html',{'form':form})




















#######################CUSTOMER#################
@login_required(login_url='loginpage')
def customerbase(request):
    return render(request,"customer/customerbase.html")


@login_required(login_url='loginpage')
def customers(request):
    return render(request,"customer/customers.html")


def customer_registration(request):
    form1=Login_form()
    form2=register_form1()
    if request.method == "POST":
        form1 = Login_form(request.POST)
        form2 = register_form1(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
               a = form1.save(commit=False)
               a.is_customer = True
               a.save()
               user1 = form2.save(commit=False)
               user1.user = a
               user1.save()
               return redirect('loginpage')

    return render(request,"customer/customers.html",{'form1': form1, 'form2': form2})

@login_required(login_url='loginpage')
def customers_data(request):
    data=register.objects.all
    print(data)
    return render(request,"admin/customers_data.html",{"data": data})


@login_required(login_url='loginpage')
def delete(request,id):
 wm=register.objects.get(id=id)
 wm.delete()
 return redirect("customers_data")

#this is to delete workers data


@login_required(login_url='loginpage')
def update(request,id):
    a = register.objects.get(id=id)
    form = register_form1(instance=a)
    if request.method == 'POST':
        form = register_form1(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('customers_data')

    return render(request,'admin/update.html',{'form':form})


@login_required(login_url='loginpage')
def customer_stock_view(request):
    data = stock.objects.all()
    return render(request,'customer/customer_stock_view.html',{'data':data})
