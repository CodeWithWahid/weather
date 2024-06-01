from django.shortcuts import render, HttpResponse
import requests
def home(request):
    error_message = {}
    weather_data = {}
    if request.method == "POST":
        city = request.POST['city']
        api_key = "67a5e5882ca593ddbb31dc1c530bc942"
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        try:
            response  = requests.get(url)
            data = response.json()
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'country_code': data['sys']['country'],
                'coordinate': f"{data['coord']['lon']} {data['coord']['lat']}",
                'pressure': data['main']['pressure'],
                'humidity': data['main']['humidity'], 
            }
            # return HttpResponse(weather_data['description'])
        except Exception as e:

            error_message = f"Error: Unable to fetch data for {city}. Please ensure the city name is correct."


    return render(request, 'home/home.html', {'weather_data': weather_data, "error_message": error_message})