import requests
import tkinter
import threading
from tkinter import PhotoImage
from tkinter import ttk
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("api_key")

window = tkinter.Tk()
window.title("Weather App")
icon = tkinter.PhotoImage(file="earth.png")
image = tkinter.PhotoImage(file="image1.png")
window.iconphoto(False, icon)


window.config(bg = '#e6e6e4')
# frame = tkinter.Frame(window, bg = '#e6e6e4')


def center_window(window):
    window.update_idletasks()
    window.resizable(False, False)
    width = 260
    height = 300
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
center_window(window)

def get_weather():
    user_input_handling = user_input.get()

    if not user_input_handling:
        city_name_label.config(text="Please enter a city name.", fg = "red")
        return
  
    response = requests.get(
        f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={user_input_handling}&aqi=no"
        )

    if response.status_code == 200:
        weather_window = tkinter.Toplevel(window)
        weather_window.title("Weather Details")
        # weather_window.config(bg = '#e6e6e4')
        # weather_window.geometry("1150x500") # widthxheight
        weather_window.resizable(True, True)

        weather_data = response.json()

        if weather_data['current']['is_day'] == 1:
            weather_window.config(bg = "#5c97c2")
        else:
            weather_window.config(bg = "#143b62")

        image_label = ttk.Label(weather_window, image=image)
        image_label.grid(row = 0, column = 1, pady = (20, 20))
        
        ttk.Label(weather_window,
                   text = f"Weather in {user_input_handling}",
                     font = ("Arial", 20, "bold"),
                       background = '#e6e6e4').grid(row = 1, column = 1, pady = 10)
        ttk.Label(weather_window,
                   text = f"Temperature: {weather_data['current']['temp_c']}°C",
                     font = ("Arial", 16),
                       background = '#e6e6e4').grid(row = 2, column = 0, pady = 10, padx=20)
        ttk.Label(weather_window,
                   text = f"Condition: {weather_data['current']['condition']['text']}",
                     font = ("Arial", 16),
                       background = '#e6e6e4').grid(row = 3, column = 0, pady = 10)
        ttk.Label(weather_window,
                  text = f"Wind Speed: {weather_data['current']['wind_kph']} km/h",
                  font = ("Arial", 16),
                  background = '#e6e6e4').grid(row = 2, column = 2, pady = 10)
        ttk.Label(weather_window,
                  text = f"Feels Like: {weather_data['current']['feelslike_c']}°C",
                  font = ("Arial", 16),
                  background = '#e6e6e4').grid(row = 3, column = 2, pady = 10)
        tkinter.Button(weather_window, text="Close", width=15, height=2, command=weather_window.destroy).grid(row = 4, column = 1, pady = 20)

city_name_label = tkinter.Label(window, text="Enter a city name:",
                    bg = "#49CF7A",
                    fg = 'white',
                    font = ("Arial", 20, "bold"),
                    padx = 10,
                    pady = 5,
                    # width = 20,
                    # height =
                       )


user_input = tkinter.Entry(window, width = 20,
                            font = ("Arial", 14),
                            borderwidth = 2,
                            relief = "groove",
                            justify = "center",
                            )

weather_button = tkinter.Button(window, text="Get Weather", 
                                width=15,
                                height=2, 
                                padx=10, 
                                pady=5,
                                command=lambda: threading.Thread(target=get_weather).start() 
                                )

author_label = tkinter.Label(window, text="2026 © Created by marlonhtml")


user_input.grid(row = 2, column = 0, pady = 10)
city_name_label.grid(row = 0, column = 0, pady = (20, 10))
weather_button.grid(row=3, column=0, pady = 10)
author_label.grid(row = 4, column = 0, pady = (10, 20))

## Configure grid to center the content
window.grid_columnconfigure(0, weight=1)



window.mainloop()