import requests
import webbrowser
#from sklearn.ensemble import RandomForestRegressor
#import numpy as np
class openwindow:
    def __init__(self, score, name, zenith, energy):
        self.opend_url = False
        self.score = score
        self.name = name
        self.energy = str(energy[1:])[1:-1].replace(' ', '')
        self.zenith = str(zenith[1:])[1:-1].replace(' ', '')
        self.max_retries = 100
    def send_score(self):
        url = "https://rsakamoto.pythonanywhere.com/update_score"
        params = {
                "score": str(round(self.score, 1)),
                "name": self.name,
                "zenith": self.zenith, 
                "energy": self.energy
                }
        requests.get(url, params=params, timeout=10)
        webbrowser.open("https://rsakamoto.pythonanywhere.com")



