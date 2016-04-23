from django.shortcuts import render
from django.http import HttpResponse

from volatum.models import Airport
from airportdb import addToDB

# Create your views here.

def index(request):
    #addToDB()

    return HttpResponse("Hello, world.")


def zipsearch(request):
    return HttpResponse(request.get_full_path())

def addAirPortsToDB(request):
    addToDB()


def drone(request):
    # Example POST request from Drone data
    # volatum.mybluemix.net/drone?lat=VALUE&log=VALUE&speed=VALUE&alt=VALUE

    if request.method == 'POST':
        #lat = request.get('lat')
        #log = request.get('log')
        #speed = request.get('speed')
        #alt = request.get('alt')

        coordinates = (request.get('lat'), request.get('log'))
        # If drone input has no lat or log
        if not coordinates:
            HttpResponse('Drone check input invalid, no latitude and longitude')

        drone_input = {'location':coordinates,
                       'speed':request.get('speed'),
                       'alt':request.get('alt'),
                       'drone_id':request.get('drone_id')}





            

        pass



    return HttpResponse("Drone Check - Hello, George :) ")


def airport(request):
    #airports = Airports.objects.all()
    #for x in airports:
    #    print(x)


    x = Airport(airport_id=4, name='dullas', city='amazon',

                 country='united states of swag', iata_faa='PWN', icao='LEET',

                 latitude=58.39405, longitude=47.12830, altitude=68,

                 timezone_offset=5, dst=1, timezone_tz='New York/Americas')

    y = Airport(airport_id=4, name='dullas', city='amazon',

                country='united states of swag', iata_faa='PWN', icao='LEET',

                latitude=58.39405, longitude=47.12830, altitude=68,

                timezone_offset=5, dst=1, timezone_tz='New York/Americas')

    input = [x, y]


    #render(request, template, {key:value of data})
    return render(request, 'volatum/index.html', {'input':input})


def airportdb(request):
    airports = Airport.objects.all()


    #render(request, template, {key:value of data})
    return render(request, 'volatum/index.html', {'input':airports})