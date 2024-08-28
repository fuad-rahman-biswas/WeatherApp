# 🌦️ Weather App

## 📖 Description
A simple Python application that provides current weather information for a specified city. This app uses the Tkinter library for the graphical user interface and retrieves weather data from the OpenWeatherMap API.

## 🚀 Features
- 🌍 Get current weather details for any city.
- 🌡️ Displays temperature, humidity, and weather description.
- 🎨 User-friendly interface with a modern design.

## 🛠️ Installation Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/fuad-rahman-biswas/WeatherApp.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd WeatherApp
    ```
3. **Ensure you have Python installed**:
   - Download it from [python.org](https://www.python.org/).
4. **Install the required libraries**:
    ```bash
    pip install requests
    ```
5. **Set up your API key**:
   - Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).
   - Replace the placeholder for the API key in `WeatherApp.py` with your own API key.

## 🖥️ Usage

1. **Run the application**:
    ```bash
    python WeatherApp.py
    ```
2. **Enter a city name in the input field and click "Get Weather" to see the current weather details**.

## 📸 Screenshots

Example of the Weather App interface showing current weather for a city.

<img src="https://github.com/user-attachments/assets/c326c9c2-1587-4783-98b2-7f6d4b56c554" alt="Weather App Screenshot 1" width="600"/><br>
<img src="https://github.com/user-attachments/assets/65aeb05a-69cf-4346-a414-a9364e7a526c" alt="Weather App Screenshot 2" width="600"/>

## ⚙️ Configuration

**API Key**: Replace `"your_api_key_here"` in `WeatherApp.py` with your API key from [OpenWeatherMap](https://openweathermap.org/api).

## 📝 Example Code

Here’s a brief example of how to fetch weather data:

```python
import requests

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    # Handle the response data
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']
    return temperature, humidity, weather_description
```
    
## 🤝 Contributing<br>
Feel free to submit a pull request if you have suggestions or improvements. Please ensure your changes adhere to the project's coding standards.

## 📜 License<br>
This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact<br>
For any questions or feedback, contact me at fuadrahman185@gmail.com.

