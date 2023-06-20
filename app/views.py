from django.shortcuts import render
from faker import Faker
from app.models import *
from django.http import HttpResponse
# Create your views here.

FO=Faker()
def Insert_Country(request):
    for i in range(0, 3):
        x=FO.country()
        CO=Country.objects.get_or_create(country_name=x)[0]
        CO.save()
    return HttpResponse('Data Is Inserted By Using Faker Module!!')

def Insert_State(request):
    for i in range(0, 3): 
        SO1=FO.state()
        COD1=Country.objects.get(country_name='Tuvalu')
        COD1.save()
        SO1=State.objects.create(country_name=COD1, state_name=SO1)
        SO1.save()
    for j in range(0, 3):
        SO2=FO.state()
        COD2=Country.objects.get(country_name='Northern Mariana Islands')
        COD2.save()
        SO2=State.objects.create(country_name=COD2, state_name=SO2)
        SO2.save()
    for k in range(0, 3):
        FO3=FO.state()
        COD3=Country.objects.get(country_name='Norfolk Island')
        COD3.save()
        SO3=State.objects.create(country_name=COD3, state_name=FO3)
        SO3.save()

    return HttpResponse('States Data I Inserted By Using Faker Module!!')
   



