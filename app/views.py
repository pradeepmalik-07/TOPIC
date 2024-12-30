from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_topic(request):
    tn=input('enter topic name :')
    TOD=Topic.objects.get_or_create(topic_name=tn)
    if TOD[1]:
        # return HttpResponse('new topic is created')
            LTO=Topic.objects.all()
            d={'LTO':LTO}   
            return render(request,'Display_topic.html',d) 

    else:
        return HttpResponse('given topic is already present')

def insert_webpages(request):
    tn=input('enter topic name :')
    name=input('enter name :')
    url=input('enter url :')
    email=input('enter email :')
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        WO=Webpages.objects.get_or_create(topic_name=LTO[0],name=name,url=url,email=email)
        if WO[1]:
            # return HttpResponse('new webpage ic created')
            LWO=Webpages.objects.all()
            d={'LWO':LWO}
            return render(request,'Display_webpage.html',d)

        else:
            return HttpResponse('given webpage already present')
    else:
        return HttpResponse('given parent data is not present')

def insert_Record(request):
    pk=int(input('enter pk :'))
    author=input('enter author name :')  
    date=input('enter date :')   
    LWO=Webpages.objects.filter(pk=pk)
    if LWO:
        AO=AccessRecord.objects.get_or_create(name=LWO[0],author=author,date=date)
        if AO[1]:
            # return HttpResponse('new record created')
            LRO=AccessRecord.objects.all()
            d={'LRO':LRO}
            return render(request,'Display_record.html',d)

        else:
            return HttpResponse('given record is present')
    else:
        return HttpResponse ('given parent data is present')      
    


def Display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}   
    return render(request,'Display_topic.html',d) 

def Display_webpage(request):
    LWO=Webpages.objects.all()
    d={'LWO':LWO}
    return render(request,'Display_webpage.html',d)

def Display_record(request):
    LRO=AccessRecord.objects.all()
    d={'LRO':LRO}
    return render(request,'Display_record.html',d)
