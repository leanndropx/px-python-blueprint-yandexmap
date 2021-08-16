from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from geopy.distance import geodesic
from time import sleep
import requests
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())

                
                # 1 - SELENINUM - OPEN MAP, WRITE ADDRES ON SEARCH LABEL, CLICK ON SEARCH BUTTON, GET NEW ADDRESS URL AND SAVE


def search_address_on_map(address):

    driver.get("https://yandex.com/maps/?ll=10.854186%2C49.182076&z=4")
    sleep(4)
    print("SUCCESSFUL ACCESS")
    
    sleep(15)
    input_search = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div/form/div[2]/div/span/span/input")

#    input_search = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div/div/form/div[2]/div/span/span/input')))

    sleep(15)
    button_search = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div/form/div[3]/button/span/div")

#    button_search = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div/div/form/div[3]/button/span/div')))
    
    input_search.send_keys(address)
    button_search.click()

    
    print("Successed input")
    current_url = driver.current_url
    driver.quit()
    
    return current_url

    
  

                        # 2 - OPEN ADDRESS URL, GET ELEMENT COORDINATES, CONVERT IN A FLOAT NUMBER, SAVE IN ARRAY

def get_array_user_coordinates (current_url):
    request_address = requests.get(current_url)

    #salved html text in a variable
    html_texto = request_address.text
    soup=BeautifulSoup(html_texto, 'html.parser')


    #found and collect the html element by class, where coordinates are located
    coordinates_element=soup.find(class_="toponym-card-title-view__coords-badge")
    for index,coordinates in enumerate(coordinates_element):
        if index==0:
            coordinates_text=coordinates

    coordinates_list_string = coordinates_text.split(',')
    
    coordinates_list_float = [float(coordinates_list_string[0]) ,float(coordinates_list_string[1])]
    
    return coordinates_list_float





                                # 3 - SER A LIMIT COORDINATES OF MKAD CIRCUNFERENCES, VERIFY IF USER COORDINATES ARE INSIDE OR OUT


def verify_if_inside_mkad (lat_user,long_user):
    
    latitude_higher_mkad = 55.911195
    latitude_minimun_mkad = 55.572492
    longitude_higher_mkad = 37.837073
    longitude_minimum_mkad = 37.370051

    ## VERIFy IF IS OUT OR INSIDE MKAD

    if lat_user < latitude_higher_mkad and lat_user > latitude_minimun_mkad     and     long_user < longitude_higher_mkad and long_user > longitude_minimum_mkad:
        return True
    else:
        return False


                                # 4 - CONVERT DECIMAL DEGREES AND CALCULATE DISTANCE
                                

def calculate_distance(lat_user,lon_user):
    user_coordinates = (lat_user, lon_user)  # (latitude, longitude) don't confuse
    mkad_coordinates = (55.898947, 37.632206)

    distance_in_km = geodesic(user_coordinates, mkad_coordinates).kilometers
    return distance_in_km




