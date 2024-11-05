import tkinter as tk
import requests
def get_weather():
    city = city_entry.get()  
    api_key = "9a8fefaf4a82080a2b7e0d3cc38e00c4"  
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric" 
    try:
        response = requests.get(complete_url)
        data = response.json()  
        if data["cod"] != 200:  
            result_label.config(text="City not found. Please try again!", fg="red")
        else:
            main = data["main"]
            weather = data["weather"][0]
            temperature = main["temp"]
            pressure = main["pressure"]
            humidity = main["humidity"]
            weather_desc = weather["description"]
            result_label.config(text=f"Temperature: {temperature}°C\n"
                                    f"Pressure: {pressure} hPa\n"
                                    f"Humidity: {humidity}%\n"
                                    f"Weather: {weather_desc.capitalize()}", 
                                fg="#333", font=("Arial", 14, "bold"))
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error: {e}", fg="red")
root = tk.Tk()
root.title("Weather App")
root.geometry("500x400")
root.config(bg="#87CEEB") 
city_label = tk.Label(root, text="Enter City Name:", font=("times new roman", 16, "bold"), bg="#87CEEB", fg="darkblue")
city_label.pack(pady=20)
city_entry = tk.Entry(root, font=("Helvetica", 14), width=30, bd=2, relief="solid", justify="center")
city_entry.pack(pady=10)
get_weather_button = tk.Button(root, text="Get Weather", font=("Helvetica", 14, "bold"), 
                               command=get_weather, bg="#4CAF50", fg="white", 
                               relief="raised", bd=5)
get_weather_button.pack(pady=20)
result_label = tk.Label(root, text="Weather info will be displayed here.", font=("Arial", 14), 
                        bg="#87CEEB", fg="black", wraplength=400)
result_label.pack(pady=10)
root.mainloop()
