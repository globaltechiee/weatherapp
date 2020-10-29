from django.shortcuts import render

# Create your views here
def home(request):
	import json
	import requests

	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=75211&distance=5&API_KEY=7CEAEF41-A2C2-410A-8D31-4892D1D90F69")

	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error..."

	return render(request, 'home.html', {"api": api})


def about(request):
	return render(request, "about.html", {})


	