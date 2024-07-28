from django.shortcuts import render
import datetime
def home(request):
    d={'Welcome':'Welcome to the Navigation Project','Date':datetime.datetime.now(),'About':'Django comes with a lot of in-built template filters that you can readily apply to your project, but in this section, we will be taking a look at the most popular template filters you will find useful in your day-to-day development journey. Please note that this list is in no particular order.'}
    return render(request,'home.html',d)