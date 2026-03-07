import requests
import tkinter
from tkinter import PhotoImage
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("api_key")

window = tkinter.Tk()
window.title("Weather App")
photo = tkinter.PhotoImage(file="earth.png")
window.iconphoto(False, photo)


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
        weather_data = weather_data.json()
        city_name_label.config(text=f"At {weather_data['location']['localtime']}\nCurrent temperature in {user_input_handling} is {weather_data['current']['temp_c']}°C")
    else:
        city_name_label.config(text="Error fetching weather data. Please try again.")

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