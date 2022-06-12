"""
https://www.airnow.gov/?city=Sugar%20Land&state=TX&country=USA
"""
import tkinter as tk
import requests
import json
from collections import namedtuple

root = tk.Tk()
root.title("Air Now")
root.geometry('400x400')

#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=77479&distance=5&API_KEY=84B7917D-C980-407F-ACBC-B29E3D2E4458


date = tk.StringVar()
area = tk.StringVar()
latitude = tk.StringVar()
longitude = tk.StringVar()
hour = tk.StringVar()
aqi = tk.StringVar()
category = tk.StringVar()

def load():
    global date
    global area
    global latitude
    global longitude
    global hour
    global aqi
    global category
    try:
        apiRequest = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=77479&distance=5&API_KEY=84B7917D-C980-407F-ACBC-B29E3D2E4458")
        airnow = json.loads(apiRequest.content)
    except Exception as e:
        airnow = "Error: " + str(e)
    air1 =airnow[0]
    air2 = airnow[1]
    air3 = json.dumps(air1, indent = 4, sort_keys=True)
    air = json.loads(air3, object_hook=airNowDecoder) 
    date.set(air.DateObserved)
    area.set(air.ReportingArea)
    latitude.set(air.Latitude)
    longitude.set(air.Longitude)
    hour.set(air.HourObserved)
    aqi.set(air.AQI)
    category.set(air.Category.Name)

def airNowDecoder(airNowDict):
    return namedtuple('AirNow', airNowDict.keys())(*airNowDict.values())

tk.Button(root, text="Load Data", command=load).grid(row=0, column=0, sticky='e')
tk.Label(root, text="Date:").grid(row=1, column=0, sticky='e')
tk.Label(root, text="Area:").grid(row=2, column=0, sticky='e')
tk.Label(root, text="Latitude:").grid(row=3, column=0, sticky='e')
tk.Label(root, text="Longitude:").grid(row=4, column=0, sticky='e')
tk.Label(root, text="Hour:").grid(row=5, column=0, sticky='e')
tk.Label(root, text="AQI:").grid(row=6, column=0, sticky='e')
tk.Label(root, text="Category:").grid(row=7, column=0, sticky='e')

tk.Label(root, textvariable=date, padx=10).grid(row=1, column=1, sticky='w')
tk.Label(root, textvariable=area, padx=10).grid(row=2, column=1, sticky='w')
tk.Label(root, textvariable=latitude, padx=10).grid(row=3, column=1, sticky='w')
tk.Label(root, textvariable=longitude, padx=10).grid(row=4, column=1, sticky='w')
tk.Label(root, textvariable=hour, padx=10).grid(row=5, column=1, sticky='w')
tk.Label(root, textvariable=aqi, padx=10).grid(row=6, column=1, sticky='w')
tk.Label(root, textvariable=category, padx=10).grid(row=7, column=1, sticky='w')

root.mainloop()