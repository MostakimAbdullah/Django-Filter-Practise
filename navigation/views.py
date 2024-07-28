from django.shortcuts import render
import datetime

# Create your views here.
def about(request):
    d={'Profession':'Django Developer','Project':['Ecomerrece site','Blog site','Bank management site','Hospital Management site'],'Time':'10 minutes','Publised':datetime.datetime.now(),'About':'Better days ahead!'}
    return render(request, 'navigation/about.html',d)

def contact(request):
    d={'CEO':'01871392168','Location':['Anderkilla','Rajapukur lane', 'Chattrogram'],'Employees':[
        {
            'id':1,
            'name':'Abdul Mukit',
            'age':22
        },
        {
            'id':2,
            'name':'Kawser Jamal',
            'age':28
        },
        {
            'id':3,
            'name':'Tasnimul Hasan',
            'age':29
        },
        {
            'id':4,
            'name':'Tawhidul Hasan',
            'age':28
        }
    ]}
    return render(request, 'navigation/contact.html',d)