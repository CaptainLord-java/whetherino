import tkinter as tk
import requests
from tkinter import messagebox


api_key = "610236741ad896925e95e43ff0cbd0c2"

def get_weather():
    city_name = city_entry.get()
    
    
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    try:
        
        response = requests.get(weather_url)
        response.raise_for_status()
        
        weather_data = response.json()
        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]

        
        lat = weather_data["coord"]["lat"]
        lon = weather_data["coord"]["lon"]

        
        air_quality_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
        air_response = requests.get(air_quality_url)
        air_response.raise_for_status()

        air_data = air_response.json()
        aqi = air_data["list"][0]["main"]["aqi"]

        
        if aqi == 1:
            air_quality = "😊 Good"
        elif aqi == 2:
            air_quality = "🙂 Fair"
        elif aqi == 3:
            air_quality = "😐 Moderate"
        elif aqi == 4:
            air_quality = "😷 Poor"
        elif aqi == 5:
            air_quality = "🤢 Very Poor"
        else:
            air_quality = "❓ Unknown"

        
        result_label.config(text=f"🌡️ Temp: {temp}°C\n💧 Humidity: {humidity}%\n🍃 Air Quality: {air_quality}")
    
    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "❌ City not found!")
    except Exception as e:
        messagebox.showerror("Error", f"⚠️ An error occurred: {str(e)}")



root = tk.Tk()
root.title("🌍 Weatherino App!")
root.geometry("450x500")
root.configure(bg="#34495E")  


font_label = ("Arial", 14, "bold")
font_button = ("Arial", 12, "bold")
font_result = ("Arial", 12)


title_label = tk.Label(root, text="🌤️ Weatherino 🌤️", font=("Arial", 20, "bold"), bg="#34495E", fg="#F7DC6F")
title_label.grid(row=0, column=0, padx=10, pady=(20, 10))


city_label = tk.Label(root, text="🏙️ Enter City Name", font=font_label, bg="#34495E", fg="#ECF0F1")
city_label.grid(row=1, column=0, padx=10, pady=10)


city_entry = tk.Entry(root, font=("Arial", 14), width=30, bd=3, relief="solid", bg="#2C3E50", fg="#ECF0F1", insertbackground="#ECF0F1")
city_entry.grid(row=2, column=0, padx=20, pady=10)


get_weather_btn = tk.Button(
    root, text="🌦️ Get Weather Info", font=font_button, bg="#1ABC9C", fg="white", activebackground="#16A085",
    activeforeground="white", borderwidth=5, relief="raised", command=get_weather
)
get_weather_btn.grid(row=3, column=0, padx=10, pady=20)


result_label = tk.Label(root, text="", font=font_result, bg="#34495E", fg="#1ABC9C", justify="left", bd=3, relief="solid", padx=10, pady=10)
result_label.grid(row=4, column=0, padx=20, pady=10)


footer_label = tk.Label(root, text="Created by: 🌟 Captain_Lord-Java 🌟", font=("Arial", 10), bg="#34495E", fg="#ECF0F1")
footer_label.grid(row=5, column=0, padx=10, pady=(20, 10))


for i in range(6):
    root.grid_rowconfigure(i, weight=1)
root.grid_columnconfigure(0, weight=1)


def on_enter(e):
    get_weather_btn.config(bg="#16A085")

def on_leave(e):
    get_weather_btn.config(bg="#1ABC9C")

get_weather_btn.bind("<Enter>", on_enter)
get_weather_btn.bind("<Leave>", on_leave)


root.mainloop()
