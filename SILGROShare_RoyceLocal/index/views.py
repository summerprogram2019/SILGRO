from django.shortcuts import render
import  csv
# Create your views here.
from django.http import HttpResponse
from .models import *
from .form import *
#from imgTest.views import uploadImg, showImg
from django.conf.urls.static import static
from django.conf import settings

def index(request):
    if request.method == 'GET':
        product = ProductForm()
        title = '123'
        names = Type.objects.values('id', 'type_name')
        return render(request, 'First.html', context=locals(), status=500)
    else:
        product = ProductForm(request.POST)
        if product.is_valid():
            name = product['name']
            return HttpResponse('Submit Successfully!')
        else:
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'First.html', context=locals(), status=500)

def mydate(request,year,month,day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day))

def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['First row','A','B','C'])
    return response


def format_date(date):
    day, month, year = date.split('/')
    return year + '-' + month + '-' + day


def newListing(request):
    if request.method == 'GET':
        return render(request, 'newListing.html', context=locals(), status=500)
    else:
        # Save listing information to the database
        db = Listing()
        db.title = request.POST.get('title')
        db.category = request.POST.getlist('check[]')
        db.description = request.POST.get('description')
        db.availability = format_date(request.POST.get('availability'))
        db.rate = request.POST.get('rate')
        db.images = request.POST.get('img')
        db.save()
        return HttpResponse('Submit Successfully!')

def productPage(request):
    if request.method == 'GET':
        return render(request, 'productPage.html', context=locals(), status=500)

def mountain_bike(request):
    if request.method == 'GET':
        listing = Listing()
        details = Listing.objects.get(id=28)
        return render(request, 'mountain-bike.html', context=locals(), status=500)

def navbar(request):
    if request.method == 'GET':
        imgs = Img.objects.all()
        return render(request, 'navbar.html', context=locals(), status=500)
    else:
        category = request.POST.get('category')
        search = request.POST.get('search')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        location = request.POST.get('location')
        result = Listing.objects.filter(title=category)
        return HttpResponse('Submit Successfully!')
def homePage(request):
    if request.method == 'GET':
        return render(request, 'homePage.html', context=locals(), status=500)
    else:
        category = request.POST.get('category')
        search = request.POST.get('search')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        location = request.POST.get('location')
        result = Listing.objects.filter(title=category)
        return HttpResponse('Submit Successfully!')

def createAccount(request):
    if request.method == 'GET':
        return render(request, 'create-account.html', context=locals(), status=500)
    else:
        firstName = request.POST.get('firstName')
        secondName = request.POST.get('secondName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        account = UserAccount()
        account.first_name = firstName
        account.last_name = secondName
        account.email = email
        account.password = password
        account.save()
        return HttpResponse("Submit Successfully!")