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

def newListing(request):
    if request.method == 'GET':
        return render(request, 'newListing.html', context=locals(), status=500)
    else:
        category = request.POST.getlist('check[]')
        title = request.POST.get('title')
        description = request.POST.get('description')
        availability = request.POST.get('availability')
        a = availability
        availability = a[6:] + '-' + a[0:2] + '-' + a[3:5]
        rate = request.POST.get('rate')
        db = Listing()
        img = Img(img_url=request.FILES.get('img'))
        db.images = img
        #  images = request.FILES.get('img')
        img.save()

        db.title = title
        db.availability = availability
        db.category = category
        db.description = description
        db.rate = rate
        # db.images = images
        db.save()
        return HttpResponse("Submit Successfully!")

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

def searchResult(request):
    if request.method == 'GET':
        return render(request, 'listings.html', context=locals(), status=500)
    else:
        category = request.POST.get('category')
        search = request.POST.get('search')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        location = request.POST.get('location')
        imgs1=Img.objects.all().filter(img_url__contains=search)
        imgs2=Img.objects.all()[4:]
        inf = Listing.objects.filter(images__contains=search)
        p = len(inf)
        resultNumber = str(p)+" "+"listings found for "+search
        return render(request, 'listings.html', context=locals(), status=500)