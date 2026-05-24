from django.shortcuts import render,HttpResponse
from django.contrib import messages
import requests
import datetime

def home(request):
    
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='hyderabad'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=232a8859a5743356bda6a9a8013955aa'

    PARAMS = {'units' : 'metric'}
    ACCESS_KEY = 'gafY7WSIfwV6Ue4EmNGzcfrvZ5Xa641hGd1NeGUcl3M'  # Replace with your Unsplash Access

    query = city + " 1920x1080"
    page = 1

    unsplash_url = f"https://api.unsplash.com/search/photos?query={query}&page={page}&per_page=3&orientation=landscape&client_id={ACCESS_KEY}"

    response = requests.get(unsplash_url)
    data = response.json()
    
    # Safely get image URL with fallback
    if data.get("results") and len(data["results"]) > 0:
        image_url = data["results"][0]["urls"]["regular"]
    else:
        image_url = "https://via.placeholder.com/1920x1080?text=Weather"

    try:
        data=requests.get(url,PARAMS).json()

        description=data['weather'][0]['description']
        icon=data['weather'][0]['icon']
        temp=data['main']['temp']
        day=datetime.date.today()
                
        return render(request,'index.html',{'description': description,'icon':icon,'temp':temp,'day':day,'city':city,'exception_occured':False,'image_url':image_url})
    except:
        exception_occured=True
        messages.error(request,'Entered data is not available in API')
        day=datetime.date.today()
        return render(request,'index.html',{'description': 'clear sky','icon':'01d','temp':25,'day':day,'city':city,'exception_occured':True,'image_url':image_url})