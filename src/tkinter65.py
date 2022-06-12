"""
https://www.airnow.gov/?city=Sugar%20Land&state=TX&country=USA
"""
import tkinter as tk
import requests
import json

root = tk.Tk()
root.title("Air Now")
root.geometry('400x400')

try:
    apiRequest = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=77479&distance=5&API_KEY=84B7917D-C980-407F-ACBC-B29E3D2E4458")
    airnow = json.loads(apiRequest.content)
except Exception as e:
    airnow = "Error: " + str(e)

airNowTxt = tk.Text(root)
airNowTxt.pack()
airNowTxt.insert("1.0", airnow)

root.mainloop()