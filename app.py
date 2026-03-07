import requests
import tkinter
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("api_key")

window = tkinter.Tk()
window.title("Weather App")
photo = tkinter.PhotoImage(file="earth.png")
window.iconphoto(False, photo)

window.config(bg = '#e6e6e4')

def center_window(window):
    window.update_idletasks()
    window.resizable(False, False)
    width = 500
    height = 300
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
center_window(window)

label1 = tkinter.Label(window, text="Enter a city name:",
                    bg = "#49CF7A",
                    fg = 'white',
                    font = ("Arial", 20, "bold"),
                    padx = 10,
                    pady = 0,
                    # width = 20,
                    # height =
                       )
label1.grid(row = 0, column = 4)



user_input = tkinter.Entry(window)
user_input.grid(row = 1, column = 4, padx = 10, pady = 10)

# user_input = input("Enter a city name: ")

# weather_data = requests.get(
#     f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={user_input}&aqi=no"
#     )

# if weather_data.status_code == 200:
#     weather_data = weather_data.json()
#     print(f"At {weather_data['location']['localtime']}")
#     print(f"Current temperature in {user_input} is {weather_data['current']['temp_c']}°C")

window.mainloop()