import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    
    try:
        response = requests.get(complete_url)
        data = response.json()
        
        if response.status_code == 200 and data.get("cod") != "404":
            main = data["main"]
            weather = data["weather"][0]
            wind = data["wind"]
            
            temperature = main["temp"]
            pressure = main["pressure"]
            humidity = main["humidity"]
            wind_speed = wind["speed"]
            visibility = data["visibility"] / 1000  # Convert visibility from meters to kilometers
            weather_description = weather["description"]
            icon_url = f"http://openweathermap.org/img/wn/{weather['icon']}.png"
            
            # Fetch the weather icon
            icon_response = requests.get(icon_url)
            icon_image = Image.open(BytesIO(icon_response.content))
            icon_photo = ImageTk.PhotoImage(icon_image)
            
            return {
                "text": (f"Temperature: {temperature}°C\n"
                         f"Atmospheric Pressure: {pressure} hPa\n"
                         f"Humidity: {humidity}%\n"
                         f"Wind Speed: {wind_speed} m/s\n"
                         f"Visibility: {visibility} km\n"
                         f"Weather Description: {weather_description}"),
                "icon": icon_photo
            }
        else:
            return {"text": f"City Not Found! (Error: {data.get('message', 'No details available')})", "icon": None}
    except requests.exceptions.RequestException as e:
        return {"text": f"Error: {e}", "icon": None}

def show_weather():
    city_name = city_entry.get().strip()
    if city_name:
        weather_info = get_weather(city_name, api_key)
        result_label.config(text=weather_info["text"])

        # Change background color based on weather
        if "clear" in weather_info["text"].lower():
            main_frame.config(bg="lightblue")
        elif "cloud" in weather_info["text"].lower():
            main_frame.config(bg="lightgrey")
        elif "rain" in weather_info["text"].lower():
            main_frame.config(bg="lightgreen")
        else:
            main_frame.config(bg="lightyellow")

        # Update icon
        if weather_info["icon"]:
            icon_label.config(image=weather_info["icon"])
            icon_label.image = weather_info["icon"]
        else:
            icon_label.config(image='')
    else:
        result_label.config(text="Please enter a valid city.")
        icon_label.config(image='')

if __name__ == "__main__":
    api_key = "abc123def456ghi789"  # Replace with your actual API key
    
    root = tk.Tk()
    root.title("Weather App")
    
    # Maximize the window on startup
    root.state('zoomed')  # Use 'zoomed' to maximize the window

    # Load background image
    try:
        background_image = Image.open(r"C:/Users/background.png") #Replace the path with your image path
        background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.Resampling.LANCZOS)
        background_photo = ImageTk.PhotoImage(background_image)
        
        background_label = tk.Label(root, image=background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_photo
    except Exception as e:
        print(f"Error loading image: {e}")
    
    # Create a frame to hold the other widgets
    main_frame = tk.Frame(root, bg='#f0f0f0', bd=10, relief='raised', padx=20, pady=20)
    main_frame.place(relx=0.5, rely=0.5, anchor='center', width=450, height=400)  # Adjust size as needed
    
    # Title Label
    title_label = tk.Label(main_frame, text="Weather Forecast", font=("Arial", 20, "bold"), bg='#f0f0f0')
    title_label.pack(pady=(0, 10))
    
    # Entry for city name
    city_entry = tk.Entry(main_frame, font=("Arial", 20), justify="center")
    city_entry.pack(pady=(0, 10), fill='x')
    
    # Button to get weather
    get_weather_button = tk.Button(main_frame, text="Get Weather", command=show_weather, font=("Arial", 12, "bold"), bg="#1E90FF", fg="white")
    get_weather_button.pack(pady=(0, 10))
    
    # Label to display the weather icon
    icon_label = tk.Label(main_frame, bg='#D3D3D3')
    icon_label.pack(pady=(0, 10))
    
    # Label to display the results
    result_label = tk.Label(main_frame, text="Enter a city and press 'Get Weather'", font=("Arial", 12), bg='#f0f0f0',anchor="center")
    result_label.pack(pady=(10, 0), fill='x')

    root.mainloop()
