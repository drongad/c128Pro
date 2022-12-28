from selenium import webdriver
from bs4 import BeautifulSoup

import time, csv

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/dronagaddam/Downloads/chromedriver")
browser.get(start_url)

time.sleep(10)

def scrape():
    headers = ["name","distance", "mass", "radius"]
    star_ = []
    for i in range(0,522):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul",attrs = {"class","star"}):
            li_tags = ul_tag.find_all("li")
            temporary_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temporary_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try: 
                        temporary_list.append(li_tag.contents[0])
                    except:
                        temporary_list.append("")

            star_data.append(temporary_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a')
    with open ("scraper2.csv","w") as f:
        csvwriter = csv.writer(f) 
        csvwriter.writerow(headers) 
        csvwriter.writerows(star_data)




        scrape()