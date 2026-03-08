import requests
import tkinter
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
frame = tkinter.Frame(window, bg = '#e6e6e4')


def center_window(window):
    window.update_idletasks()
    window.resizable(True, True)
    width = 500
    height = 300
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
center_window(window)

def get_weather():
    user_input_handling = user_input.get()
    weather_data = requests.get(
        f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={user_input_handling}&aqi=no"
        )

    if weather_data.status_code == 200:
        weather_window = tkinter.Toplevel(window)
        weather_window.title("Weather Details")
        weather_window.config(bg = '#e6e6e4')
        weather_window.geometry("1150x500") # widthxheight
        weather_window.resizable(True, True)
        weather_data = weather_data.json()
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
    else:
        city_name_label.config(text="City not found. Please try again.", fg = "red")

city_name_label = tkinter.Label(frame, text="Enter a city name:",
                    bg = "#49CF7A",
                    fg = 'white',
                    font = ("Arial", 20, "bold"),
                    padx = 10,
                    pady = 5,
                    # width = 20,
                    # height =
                       )


user_input = tkinter.Entry(frame, width = 20,
                            font = ("Arial", 14),
                            borderwidth = 2,
                            relief = "groove",
                            justify = "center",
                            )

weather_button = tkinter.Button(frame, text="Get Weather", 
                                width=15,
                                height=2, 
                                padx=10, 
                                pady=5,
                                command=get_weather 
                                )


user_input.grid(row = 2, column = 0, pady = 10)
city_name_label.grid(row = 0, column = 0, pady = (20, 10))
weather_button.grid(row=3, column=0, pady = 10)
frame.pack()

window.grid_columnconfigure(0, weight=1)

window.mainloop()