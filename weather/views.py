import requests
from django.shortcuts import render
from django.http import HttpResponse
from .forms import WeatherForm


# Create your views here.
def home(request):
	if request.method == "GET":
		form = WeatherForm()
		return render(request, 'index.html', {'form': form})


def get_weather_data(request): 
	if request.method == "POST":
		longitude = request.POST.get('longitude')
		latitude = request.POST.get('latitude')
		api_call = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={int(longitude)}&lon={int(latitude)}"
		headers = requests.utils.default_headers()
		headers.update({'User-Agent': 'Custom Agent',})
		print(headers, " headers")
		response = requests.get(api_call, headers)
		print(response.content, "response")
		print(type(response.content), "response type")	
		return HttpResponse("Done")
