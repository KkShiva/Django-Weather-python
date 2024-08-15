from django.shortcuts import render,HttpResponse
import python_weather
import asyncio
import os

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')





async def Indonesiagetweather():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get('Indonesia')
        return weather

def Indonesiaweather_view(request):
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    weather_data = asyncio.run(Indonesiagetweather())

    context = {
        'country': weather_data.country,
        'temperature': weather_data.temperature,
        'coordinates': weather_data.coordinates,
        'feels_like': weather_data.feels_like,
        'humidity': weather_data.humidity,
        'pressure': weather_data.pressure,
        'visibility': weather_data.visibility,
        'wind_direction': weather_data.wind_direction,
        'wind_speed': weather_data.wind_speed,
        'description': weather_data.description,
        'daily_forecasts': weather_data.daily_forecasts,
    }

    return render(request, 'Indonesia.html', context)




async def SriLankagetweather():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get('SriLanka')
        return weather

def SriLankaweather_view(request):
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    weather_data = asyncio.run(SriLankagetweather())

    context = {
        'country': weather_data.country,
        'temperature': weather_data.temperature,
        'coordinates': weather_data.coordinates,
        'feels_like': weather_data.feels_like,
        'humidity': weather_data.humidity,
        'pressure': weather_data.pressure,
        'visibility': weather_data.visibility,
        'wind_direction': weather_data.wind_direction,
        'wind_speed': weather_data.wind_speed,
        'description': weather_data.description,
        'daily_forecasts': weather_data.daily_forecasts,
    }

    return render(request, 'SriLanka.html', context)




async def Russiagetweather():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get('Russia')
        return weather

def Russiaweather_view(request):
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    weather_data = asyncio.run(Russiagetweather())

    context = {
        'country': weather_data.country,
        'temperature': weather_data.temperature,
        'coordinates': weather_data.coordinates,
        'feels_like': weather_data.feels_like,
        'humidity': weather_data.humidity,
        'pressure': weather_data.pressure,
        'visibility': weather_data.visibility,
        'wind_direction': weather_data.wind_direction,
        'wind_speed': weather_data.wind_speed,
        'description': weather_data.description,
        'daily_forecasts': weather_data.daily_forecasts,
    }

    return render(request, 'Russia.html', context)






async def Australiagetweather():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get('Australia')
        return weather

def Australiaweather_view(request):
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    weather_data = asyncio.run(Australiagetweather())

    context = {
        'country': weather_data.country,
        'temperature': weather_data.temperature,
        'coordinates': weather_data.coordinates,
        'feels_like': weather_data.feels_like,
        'humidity': weather_data.humidity,
        'pressure': weather_data.pressure,
        'visibility': weather_data.visibility,
        'wind_direction': weather_data.wind_direction,
        'wind_speed': weather_data.wind_speed,
        'description': weather_data.description,
        'daily_forecasts': weather_data.daily_forecasts,
    }

    return render(request, 'Australia.html', context)







async def Japangetweather():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get('Japan')
        return weather

def Japanweather_view(request):
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    weather_data = asyncio.run(Japangetweather())

    context = {
        'country': weather_data.country,
        'temperature': weather_data.temperature,
        'coordinates': weather_data.coordinates,
        'feels_like': weather_data.feels_like,
        'humidity': weather_data.humidity,
        'pressure': weather_data.pressure,
        'visibility': weather_data.visibility,
        'wind_direction': weather_data.wind_direction,
        'wind_speed': weather_data.wind_speed,
        'description': weather_data.description,
        'daily_forecasts': weather_data.daily_forecasts,
    }

    return render(request, 'Japan.html', context)




async def USAgetweather():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get('USA')
        return weather

def USAweather_view(request):
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    weather_data = asyncio.run(USAgetweather())

    context = {
        'country': weather_data.country,
        'temperature': weather_data.temperature,
        'coordinates': weather_data.coordinates,
        'feels_like': weather_data.feels_like,
        'humidity': weather_data.humidity,
        'pressure': weather_data.pressure,
        'visibility': weather_data.visibility,
        'wind_direction': weather_data.wind_direction,
        'wind_speed': weather_data.wind_speed,
        'description': weather_data.description,
        'daily_forecasts': weather_data.daily_forecasts,
    }

    return render(request, 'USA.html', context)



async def Indiagetweather():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get('India')
        return weather

def Indiaweather_view(request):
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    weather_data = asyncio.run(Indiagetweather())

    context = {
        'country': weather_data.country,
        'temperature': weather_data.temperature,
        'coordinates': weather_data.coordinates,
        'feels_like': weather_data.feels_like,
        'humidity': weather_data.humidity,
        'pressure': weather_data.pressure,
        'visibility': weather_data.visibility,
        'wind_direction': weather_data.wind_direction,
        'wind_speed': weather_data.wind_speed,
        'description': weather_data.description,
        'daily_forecasts': weather_data.daily_forecasts,
    }

    return render(request, 'India.html', context)

async def getweather(city):
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get(city)
        return weather

def weather_view(request):
    city = request.GET.get('city', 'Mumbai')  # Default to 'Mumbai' if no city is provided
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    weather_data = asyncio.run(getweather(city))

    context = {
        'city': city,
        'country': weather_data.country,
        'temperature': weather_data.temperature,
        'coordinates': weather_data.coordinates,
        'feels_like': weather_data.feels_like,
        'humidity': weather_data.humidity,
        'pressure': weather_data.pressure,
        'visibility': weather_data.visibility,
        'wind_direction': weather_data.wind_direction,
        'wind_speed': weather_data.wind_speed,
        'description': weather_data.description,
    }

    return render(request, 'weather.html', context)