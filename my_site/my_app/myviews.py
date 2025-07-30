from django.shortcuts import render
from django.http import HttpResponse
from .models import postpaid
from .models import prepaid
from .models import dth
from .models import wifi
from .models import Contact
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import requests
import time
import uuid  
from django.conf import settings
import json
from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django import forms
from django.db.models import Q
from .models import wifi, prepaid, postpaid, dth
from cashfree_pg.models.create_order_request import CreateOrderRequest
from cashfree_pg.api_client import Cashfree
from cashfree_pg.models.customer_details import CustomerDetails

from math import ceil
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True, label='Search')
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def ShopHome(request):
    return render(request,'index.html')
def wifii(request):
    all_values = list(wifi.objects.values_list('wifi_name', flat=True))
    abcde=all_values[0]
    abcdee=all_values[1]
    abcdeee=all_values[2]
    abcdeeee=all_values[3]
    abcdeeeee=all_values[4]
    all_valuess=list(wifi.objects.values_list('price', flat=True))
    ab=all_valuess[0]
    abb=all_valuess[1]
    abbb=all_valuess[2]
    abbbb=all_valuess[3]
    abbbbb=all_valuess[4]
    all_valuesss=list(wifi.objects.values_list('category', flat=True))
    acd=all_valuesss[0]
    all_valuessss=list(wifi.objects.values_list('desc', flat=True))
    abc=all_valuessss[0]
    abcc=all_valuessss[1]
    abccc=all_valuessss[2]
    abcccc=all_valuessss[3]
    abccccc=all_valuessss[4]
    all_valuesssss=list(wifi.objects.values_list('sub_category', flat=True))
    abd=all_valuesssss[0]

    paraams={'abcde':abcde,'abcdee':abcdee,'abcdeee':abcdeee,'abcdeeee':abcdeeee,'abcdeeeee':abcdeeeee,'acd':acd,'ab':ab,'abb':abb,'abbb':abbb,'abbbb':abbbb,'abbbbb':abbbbb,'abc':abc,'abcc':abcc,'abccc':abccc,'abcccc':abcccc,'abccccc':abccccc,'abd':abd}
    return render(request,'wifi.html',paraams)  

def prepaidd(request):
    h=list(prepaid.objects.values_list('prepaid_name', flat=True))
    hh=h[0]
    hhh=h[1]
    hhhh=h[2]
    hhhhh=h[3]
    i=list(prepaid.objects.values_list('price', flat=True))
    ii=i[0]
    iii=i[1]
    iiii=i[2]
    iiiii=i[3]
    j=list(prepaid.objects.values_list('category', flat=True))
    jj=j[0]
    jjj=j[1]
    jjjj=j[2]
    jjjjj=j[3]
    k=list(prepaid.objects.values_list('desc', flat=True))
    kk=k[0]
    kkk=k[1]
    kkkk=k[2]
    kkkkk=k[3]
    l=list(prepaid.objects.values_list('validity', flat=True))
    ll=l[0]
    lll=l[1]
    llll=l[2]
    lllll=l[3]
    m=list(prepaid.objects.values_list('sub_category', flat=True))
    mm=m[0]
    mmm=m[1]
    mmmm=m[2]
    mmmmm=m[3]
    pparams={'hh':hh,'hhh':hhh,'hhhh':hhhh,'hhhhh':hhhhh,'iiiii':iiiii,'iiii':iiii,'iii':iii,'ii':ii,'jj':jj,'kkkkk':kkkkk,'kkkk':kkkk,'kk':kk,'kkk':kkk,'lllll':lllll,'llll':llll,'lll':lll,'ll':ll,'mmmmm':mmmmm,'mmmm':mmmm,'mmm':mmm,'mm':mm,}
    return render(request,'prepaidd.html',pparams)    

def postpaidd(request):
    a = list(postpaid.objects.values_list('price', flat=True))
    aa=a[0]
    aaa=a[1]
    aaaa=a[2]
    aaaaa=a[3]
    aaaaaa=a[4]
    b= list(postpaid.objects.values_list('data_rollover', flat=True))
    bb=b[0]
    bbb=b[1]
    bbbb=b[2]
    bbbbb=b[3]
    bbbbbb=b[4]
    c = list(postpaid.objects.values_list('sms_per_day', flat=True))
    cc=c[3]
    d = list(postpaid.objects.values_list('calls', flat=True))
    dd=d[3]
    e = list(postpaid.objects.values_list('entertainment_apps', flat=True))  
    ee=e[3]
    f='Monthly Rental Of'
    params={'aa':aa,'aaa':aaa,'aaaa':aaaa,'aaaaa':aaaaa,'aaaaaa':aaaaaa,'cc':cc,'dd':dd,'ee':ee,'bb':bb,'bbb':bbb,'bbbb':bbbb,'bbbbb':bbbbb,'bbbbbb':bbbbbb,'f':f}  
    return render(request,'postpaidd.html',params)
def dthh(request):
    p= list(dth.objects.values_list('dth_name', flat=True))
    pp=p[0]
    ppp=p[1]
    pppp=p[2]
    ppppp=p[3]
    q= list(dth.objects.values_list('price', flat=True))
    qq=q[0]
    qqq=q[1]
    qqqq=q[2]
    qqqqq=q[3]
    r= list(dth.objects.values_list('channels', flat=True))
    rr=r[0]
    rrr=r[1]
    rrrr=r[2]
    rrrrr=r[3]
    s= list(dth.objects.values_list('validity', flat=True))
    ss=s[0]
    paramms={'rrrrr':rrrrr,'rrrr':rrrr,'rrr':rrr,'rr':rr,'qqqqq':qqqqq,'qqqq':qqqq,'qqq':qqq,'qq':qq,'ss':ss,'ppppp':ppppp,'pppp':pppp,'ppp':ppp,'pp':pp}
    return render(request,'dth.html',paramms)
def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "contact.html")


from django.shortcuts import render
from .models import wifi, dth, prepaid, postpaid

def unified_search(request):
    query = request.GET.get('query', '')  # Retrieve the search query from the GET request
    
    # Search in WiFi plans if query is provided
    wifi_results = wifi.objects.filter(wifi_name__icontains=query) if query else wifi.objects.all()
    
    # Search in DTH plans if query is provided
    dth_results = dth.objects.filter(dth_name__icontains=query) if query else dth.objects.all()
    
    # Search in Prepaid plans if query is provided
    prepaid_results = prepaid.objects.filter(prepaid_name__icontains=query) if query else prepaid.objects.all()
    
    # Search in Postpaid plans if query is provided
    postpaid_results = postpaid.objects.filter(price__icontains=query) if query else postpaid.objects.all()

    # Pass the results to the template
    context = {
        'wifi_results': wifi_results,
        'dth_results': dth_results,
        'prepaid_results': prepaid_results,
        'postpaid_results': postpaid_results
    }
    
    return render(request, 'search.html', context)
def signup(request):
    # You can add any logic you need here
    return render(request, 'accounts/signup.html')  # This renders the 'signup.html' template

# Login view
def login(request):
    # Any logic for login goes here
    return render(request, 'accounts/login.html')  # This renders the 'login.html' template

# Show the payment form to the user
def payment_form(request, amount):
    return render(request, 'payment_form.html', {'amount': amount})

@require_POST
def create_order(request, amount):
    order_id = f"ORDER_{int(time.time())}"  # Unique Order ID

    # Fetch customer details from the request
    customer_email = request.POST.get("customer_email", "")
    customer_phone = request.POST.get("customer_phone", "")
    customer_name = request.POST.get("customer_name", "")

    if not customer_email or not customer_phone or not customer_name:
        return JsonResponse({"error": "Missing customer details"}, status=400)

    payment_data = {
        "order_id": order_id,
        "order_amount": amount,  # The amount is taken from the URL
        "order_currency": "INR",
        "customer_details": {
            "customer_id": "12345",  # This could also come from the request if available
            "customer_email": customer_email,
            "customer_phone": customer_phone,
            "customer_name": customer_name,
        },
        "order_meta": {
            "return_url": f"{settings.BASE_URL}/payment-success/?order_id={order_id}"
        },
    }
    
    headers = {
        "x-client-id":f"{settings.CASHFREE_APP_ID}",
        "x-client-secret":f"{settings.CASHFREE_SECRET_KEY}",
        "Content-Type": "application/json",
        "x-api-version": "2022-01-01",
    }

    # Call Cashfree API to Create Order
    response = requests.post(
        f"{settings.CASHFREE_BASE_URL}/orders",
        data=json.dumps(payment_data),
        headers=headers,
    )

    response_data = response.json()

    if response.status_code == 200 and "payment_link" in response_data:
        # Redirect to the Cashfree Payment Page
        return redirect(response_data["payment_link"])
    else:
        return JsonResponse(response_data, safe=False)

def payment_success(request):
    order_id = request.GET.get("order_id")
    # In a real-world scenario, you would query the order status here
    # For example, by calling the Cashfree API to check the payment status
    return render(request, 'payment_success.html', {'order_id': order_id})

def payment_failure(request):
    # You can handle failed payment scenarios here, such as invalid payments or errors
    return render(request, 'payment_failure.html')