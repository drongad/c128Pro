from bs4 import BeautifulSoup
import requests
import time, csv
from selenium.webdriver.common.by import By
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(start_url)

soup = BeautifulSoup(page.text, "html.parser")
star_table = soup.find_all("table")
temporary_list = []
tablerows = star_table[7].find_all("tr")
for tr in tablerows:
    td_tags = tr.find_all("td")
    row = [i.text.rstrip() for i in td_tags]
    temporary_list.append(row)

star_names = []
mass=[]
distance = []
radius = []
for i in range(1,len(temporary_list)):
    star_names.append(temporary_list[i][0])
    mass.append(temporary_list[i][7])
    distance.append(temporary_list[i][5])
    radius.append(temporary_list[i][8])

df = pd.DataFrame(list(zip(star_names, distance, mass, radius, )), columns= ["Star_Name", "Distance","Mass", "Radius" ] )
print(df)

df.to_csv("Brown_Dwarfs.csv")




    





