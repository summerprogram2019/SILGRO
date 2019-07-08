from django.shortcuts import render
import  csv
# Create your views here.
from django.http import HttpResponse
from .models import Type

def index(request):
    title = '123'
    names = Type.objects.values('id','type_name')
    #or names = Type.objects.all()
    return render(request,'First.html',context=locals(),status=500)

def mydate(request,year,month,day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day))

def download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['First row','A','B','C'])
    return response

