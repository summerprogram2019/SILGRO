from django.shortcuts import render
import  csv
# Create your views here.
from django.http import HttpResponse
from .models import *
from .form import *

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
        rate = request.POST.get('rate')
        images = request.POST.get('img')
        db = Listing()
        db.title = title
        db.availability = availability
        db.category = category
        db.description = description
        db.rate = rate
        db.images = images
        db.save()
        return HttpResponse('Submit Successfully!')


