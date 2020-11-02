from django.shortcuts import render

# Create your views here
def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=7CEAEF41-A2C2-410A-8D31-4892D1D90F69")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
			cat_descr = "(0 - 50) Air quality is satisfactory, and air pollution poses little or no risk."
			cat_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
			cat_descr = "(51 - 100)Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
			cat_color = "Moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
	  	    cat_descr = "(101 - 150)Members of sensitive groups may experience health effects. The general public is less likely to be affected."
	  	    cat_color = "usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
	  		cat_descr = "(151 - 200)Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
	  		cat_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
	  		cat_descr = "(201 - 300)Health alert: The risk of health effects is increased for everyone."
	  		cat_color = "very_unhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
	  		cat_descr = "(301 - 500)Health warning of emergency conditions: everyone is more likely to be affected."
	  		cat_color = "hazardous"


		return render(request, 'home.html', {"api": api,
											'cat_descr': cat_descr,
											'cat_color': cat_color
											})
		
	else:
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=75211&distance=5&API_KEY=7CEAEF41-A2C2-410A-8D31-4892D1D90F69")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
			cat_descr = "(0 - 50) Air quality is satisfactory, and air pollution poses little or no risk."
			cat_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
			cat_descr = "(51 - 100)Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
			cat_color = "Moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
	  	    cat_descr = "(101 - 150)Members of sensitive groups may experience health effects. The general public is less likely to be affected."
	  	    cat_color = "usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
	  		cat_descr = "(151 - 200)Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
	  		cat_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
	  		cat_descr = "(201 - 300)Health alert: The risk of health effects is increased for everyone."
	  		cat_color = "very_unhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
	  		cat_descr = "(301 - 500)Health warning of emergency conditions: everyone is more likely to be affected."
	  		cat_color = "hazardous"


		return render(request, 'home.html', {"api": api,
											'cat_descr': cat_descr,
											'cat_color': cat_color
											})


def about(request):
	return render(request, "about.html", {})


	