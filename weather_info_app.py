import requests                    # To make HTTP requests to the weather API
from datetime import datetime      # To get the current time

# 1. Set up your API key and base URL for OpenWeatherMap
API_KEY = "079f77e024541d3f9a4d7648892b0e2a"  # 👉 Replace this with your actual API key from https://openweathermap.org
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# 2. Ask the user to enter the name of the city
city = input("Enter city name: ")

# 3. Build the complete request URL
# q = city name, appid = your API key, units = metric for Celsius
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

# 4. Make the request to OpenWeatherMap
response = requests.get(url)


# 5. Check if the request was successful
if response.status_code == 200:
    # 6. Convert JSON response into a Python dictionary
    data = response.json()
    

    # 7. Extract temperature and weather description
    temp = data["main"]["temp"]                      # Current temperature
    description = data["weather"][0]["description"]  # Weather description like "clear sky"

    # 8. Get the current time in a readable format
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")          # Example: 12:05 PM

    # 9. Print the final weather report
    print(f"The temperature in {city} is {temp}°C with {description} as of {current_time}")

else:
    # 10. Handle errors like wrong city name
    print("Sorry, couldn't fetch weather data. Please check the city name and try again.")
