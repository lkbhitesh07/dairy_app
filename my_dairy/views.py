from django.shortcuts import render, redirect
from .forms import ProfileForm, SignUpForm
from django.contrib.auth.decorators import login_required
from allauth.account.views import SignupView
from .models import *
from my_dairy import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def home(request):
    return render(request, 'my_dairy/home.html')

def accountSignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # If you want to login user after signup, than use this code
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)

            return redirect('add_customer')
    else:
        form = SignUpForm()
    return render(request, 'my_dairy/signup2.html', {'form': form})

@login_required
def add_customer(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
        context = {
            'form': form,
        }
    return render(request, 'my_dairy/add_customer.html', context)

@login_required
def morning_all_customer(request):
    customer_info = models.Profile.objects.filter(time="Morning")
    context = {
        'customer_info': customer_info
    }
    return render(request, 'my_dairy/customer_detail_morning.html', context)

@login_required
def evening_all_customer(request):
    customer_info = models.Profile.objects.filter(time="Evening")
    context = {
        'customer_info': customer_info
    }
    return render(request, 'my_dairy/customer_detail_evening.html', context)

def customer_ledger(request, pk):
    customer_obj = get_object_or_404(User, pk=pk)
    cus_user_info = models.Profile.objects.get(user=customer_obj)
    cus_ledger_info = models.CustomerLedger.objects.filter(related_customer=customer_obj)
    customer_full_name = f"{cus_user_info.first_name} {cus_user_info.last_name}"

    all_total = 0.0
    for i in cus_ledger_info:
        all_total = all_total + float(i.total)

    context = {
        'customer_full_name': customer_full_name,
        'customer_obj': customer_obj,
        'cus_ledger_info': cus_ledger_info,
        'cus_user_info': cus_user_info,
        'all_total': all_total,
    }
    return render(request, 'my_dairy/customer_ledger.html', context)

def customer_ledger_save(request):
    if request.method == 'POST':
        print(request.POST)
        customer_pk = request.POST.get("customer", None)
        date = request.POST.get("date", None)
        quantity = request.POST.get("quantity", None)
        related_customer = models.User.objects.get(pk=customer_pk)
        price = request.POST.get("price", None)
        total = float(price)*float(quantity)

        data = models.CustomerLedger(
            related_customer=related_customer,
            date=date,
            quantity=quantity,
            total=total,
            price=price,
        )
        data.save()

        current_url = "/customer_ledger/" + str(customer_pk)

        return redirect(current_url)

def customer_ledger_delete(request):
    if request.method == 'POST':
        pk = request.POST.get('customer_pk')
        customer_ledger_entry = models.CustomerLedger.objects.get(pk=pk)
        customer_ledger_entry.delete()
        customer_pk = customer_ledger_entry.related_customer.pk
        current_url = "/customer_ledger/" + str(customer_pk)

        return redirect(current_url)

def customer_page(request):
    customer = request.user
    customer_info = models.CustomerLedger.objects.filter(related_customer=customer)
    print(customer_info)
    cus_user_info = models.Profile.objects.get(user=customer)

    all_total = 0.0

    for i in customer_info:
        all_total = all_total + float(i.total)

    context = {
        'customer_info': customer_info,
        'all_total': all_total,
        'cus_user_info': cus_user_info,
    }

    return render(request, 'my_dairy/customer_page.html', context)
