from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users,Packages,UserAndinvoice
from django.contrib.auth.models import auth
# Create your views here.

def showAllMembers(request):
    context = {
        'page_name':'All Users',
        'nav_name': 'All Users',
        'packages' : Packages.objects.all(),
    }
    return render(request, 'isp/index.html', context)


def addUsers(request):
    return render(request, 'isp/add_users.html')



def editUsers(request):
    return render(request,'isp/edit_users.html')



def packages(request):
    return render(request, 'isp/packages.html')


def addPackages(request):
    return render(request, 'isp/add_packages.html')


def generateInvoice(request):

    out = UserAndinvoice.objects.filter(user_id=request.session['userid'])
    unpaid = 0
    for x in out:
        unpaid = unpaid + int(x.invoice_id.total_balance)

    context = {
        'invoices' : out,
        'total_unpaid': unpaid
    }
    return render(request, 'isp/invoice.html',context)


def login_check(request):
    request.session['userid'] = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        val = Users.objects.filter(email=email).first()
        if val is not None:
            if(str(val.password) == str(password)):
                request.session['userid'] = val.id
                request.session['username'] = val.name
                request.session['userlocation'] = val.location
                request.session['userno'] = val.phone_no
                return redirect("/")
            else:
                return HttpResponse("Errore")
        else:
            return HttpResponse("Errore")
    else:
        return HttpResponse("Errore")

def logout(request):
    request.session.flush()
    return redirect("/")

def choose_package(request):
    return HttpResponse(choose_package)
