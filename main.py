import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium
#trouver le numero
num = "+237654424923"
monNum = phonenumbers.parse(num)
localisation = geocoder.description_for_number(monNum, "fr")
print(localisation)
#trouver l'operteur mobile
operateur  = phonenumbers.parse(num)
print(carrier.name_for_number(operateur, "fr"))
#trouver la latitude et la longitude
clef = "d77acaf9384a49e29283eb06dbe71ab2"
coord = OpenCageGeocode(clef)
requete = str(localisation)
reponse = coord.geocode(requete)
lat = reponse[0]["geometry"]["lat"]
lng = reponse[0]["geometry"]["lng"]
print(lat,lng)
#creation du map

monMap = folium.Map(localisation=[lat,lng], zoom_start=12)
folium.Marker([lat, lng], popup=localisation).add_to(monMap)
monMap.save("map.html")
