from django.shortcuts import render

from django.http import HttpResponse


#def contact_view(request):
    #return HttpResponse("Contact app works!")

def contact_view(request):
    return render(request, 'contact/contact.html')
