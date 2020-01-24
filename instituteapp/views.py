from django.shortcuts import render
from instituteapp.models import ContactData,ServicerData
from instituteapp.forms import ContactForm
from django.http.response import HttpResponse


def home_view(request):
    return render(request, 'nareshhome.html')


def contact_view(request):
    if request.method=='POST':
        cform=ContactForm(request.POST)
        if cform.is_valid():
            name=request.POST.get('name')
            location=request.POST.get('location')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            data=ContactData(
                name=name,
                location=location,
                mobile=mobile,
                email=email
            )
            data.save()
            cform=ContactForm()
            return render(request, 'nareshcontact.html', {'cform':cform})
        else:
            return HttpResponse('user missed some values')

    else:
        cform=ContactForm()
        return render(request, 'nareshcontact.html', {'cform':cform})




def gallery_view(request):
    return render(request, 'nareshgallery.html')


def services_view(request):
    service=ServicerData.objects.all()
    return render(request, 'nareshservices.html', {'service':service})
