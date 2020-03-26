from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def main_page(request):

    if request.POST:
        print(request.POST)
        if('coordinatesSubmitted' in request.POST):
            messages.success(request, "Your coordinate has been saved!")
            latitude = float(request.POST['latitude'])
            longitude = float(request.POST['longitude'])
            print('LATITUDE: {}, LONGITUDE: {}'.format(latitude, longitude))

            user_location = Point(longitude, latitude, srid=4326)

        return HttpResponseRedirect(reverse('main_page'))
    else:
        storage = messages.get_messages(request)
        storage.used = True
        return render(request, 'main_page.html')
