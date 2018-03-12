import pandas as pd
import constants
from geopy.geocoders import GoogleV3
import gmplot

#need way to secretly keep API keys in script
geocode_API_key = "[OMITTED]"
javascript_API_key = "[OMITTED]"

geo = GoogleV3(api_key = geocode_API_key)

days_of_week = ['MON','TUE','WED','THU','FRI','SAT','SUN']

color = {"MON": "#FF0000", #Red
        "TUE": "#008000",  #Green
        "WED": "#0000FF",  #Blue
        "THU": "#FF00FF",  #Fuschia
        "FRI": "#FFFF00",  #Yellow
        "SAT": "#00FFFF",  #aqua
        "SUN": "#808080",  #grey            
        }  

def geocode(address):
    code = geo.geocode(address)
    return code.latitude, code.longitude

def scatterPlot_and_writeHTML(day,lat_list,lon_list):
    if lat_list or lon_list == []:
        print("No trash pickup on %s" % day)
        return None

    else:
        try:
            gmap = gmplot.GoogleMapPlotter(lat_list[0],lon_list[0],15,apikey=javascript_API_key)
            gmap.scatter(lat_list,lon_list,color[day], size=6, marker=False)
            file_name = day + "_map.html"
            gmap.draw(file_name)
        except Exception, e:
            print(e)
            print(".html file failed to write")
            print("-"*30)