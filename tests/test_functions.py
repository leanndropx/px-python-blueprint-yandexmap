import pytest
from app import functions

import requests

# command in terminal linux: python3 -m pytest "test_app"

                    # TESTING FUNCTION:   get_array_user_coordinates(current_url)

                            # 1 - FAIL TEST WHEN SELENIUM DOES NOT GET TO COLLECT COORDINATES

def test_search_address_on_map_input_address_return_url ():
        user_address_url = functions.search_address_on_map("MKAD")
        
        assert user_addres_url == "https://yandex.com/maps/213/moscow/geo/mkad/8059375/?ll=10.854186%2C49.182076&mode=search&sll=10.854186%2C49.182076&sspn=82.177734%2C31.812523&text=mkad&z=4"




                    # TESTING FUNCTION:   get_array_user_coordinates(current_url)


                            # 1 - FAIL TEST WHEN SELENIUM DOES NOT GET TO COLLECT COORDINATES
  
            # 1

def test_get_array_user_coordinates_parameter_url_return_coordinates ():
    user_coordinates_list = functions.get_array_user_coordinates("https://yandex.com/maps/?ll=10.854186%2C49.182076&mode=search&sll=10.854186%2C49.182076&sspn=82.177734%2C31.812523&text=MKAD&z=4")

    assert user_coordinates_list == [55.898947,37.632206]





                    #  TESTING FUNCTION:   verify_if_inside_mkad (lat_user,lon_user)

# address outside MKAD
new_york_latitude = 40.714606
new_york_longitude = 74.002800

#addres inside MKAD
basmanniy_district_latitude = 55.766568
basmanniy_district_longitude = 37.671228

latitude_inside_mkad = 55.765234
longitude_outside_mkad = 38.565333

latitude_outside_mkad = 67.567633
longitude_inside_mkad = 37.542198


                            # THE 5 TESTS BELLOW NEED TO PASS

                            # 1 - PASS THE TEST IF ITS TRUE THAT BASMANNIY DISTRICT IS INSIDE MKAD
                            # 2 - PASS THE TEST IF ITS FALSE THAT NEW YORK IS INSIDE MKAD
                            # 3 - PASS THE TEST IF RETURN TYPE ERROR, BECAUSE WAS IMPUTED STRING VALUE AND NOT FLOAT
                            # 4 - PASS THE TEST IF RETURN FALSE WHEN LATITUDE VALUE ITS INSIDE BUT LONGITUDE ITS OUT, SO THE ADDRESS IS NOT INSIDE
                            # 5 - PASS THE TEST IF RETURN FALSE WHEN LATITUDE VALUE ITS OUT BUT LONGITUDE IS INSIDE, SO THE ADDRES IS NOT INSIDE

            # 1

def test_verify_if_inside_mkad_input_latlong_return_true ():
    
    address_inside_mkad = functions.verify_if_inside_mkad(basmanniy_district_latitude,basmanniy_district_longitude)
    
    assert address_inside_mkad == True


            # 2 -

def test_verify_if_inside_mkad_input_latlong_return_false ():
    address_inside_mkad = functions.verify_if_inside_mkad(new_york_latitude,new_york_longitude)
    
    assert address_inside_mkad == False


            # 3

def test_verify_if_inside_mkad_input_string_return_typeError ():
    with pytest.raises(TypeError):
        address_inside_mkad = functions.verify_if_inside_mkad("55.656947","37.545234")

            
            # 4

def test_verify_if_inside_mkad_input_latinside_longoutside_return_false ():
    
    address_inside_mkad = functions.verify_if_inside_mkad(latitude_inside_mkad,longitude_outside_mkad)
    
    assert address_inside_mkad == False


            # 5
            
def test_verify_if_inside_mkad_input_latoutside_longinside_return_false ():
    
    address_inside_mkad = functions.verify_if_inside_mkad(latitude_outside_mkad,longitude_inside_mkad)
    
    assert address_inside_mkad == False




                    # 4 - TESTING FUNCTION:   calculate_distance (lat_user , lon_user)
                            
                            
                            # 1 - PASS THE TEST IF ITS IMPUTED FLOAT VALUE AND RETURNS FLOAT VALUE
                            # 2 - FAIL TEST BECAUSE ITS MISSING LONGITUDE PARAMETER
                            # 3 - PASS THE TEST IF ITS IMPUTED INT VALUE AND RETURNS FLOAT VALUE
                            # 3 - PASS THE TEST IF ITS IMPUTED STRING VALUE AND RETURNS FLOAT VALUE

            # 1
            
def test_calculate_distance_input_latlong_return_distancekm ():
    distance = functions.calculate_distance(new_york_latitude,new_york_longitude)

    assert type(distance) is float


            # 2
            
def test_calculate_distance_not_input_longitude ():
    distance = functions.calculate_distance(new_york_latitude)

    assert type(distance) is float

            
            # 3
            
def test_calculate_distance_input_int_value_return_float ():
    distance = functions.calculate_distance(55,67)

    assert type(distance) is float


            # 4

def test_calculate_distance_input_string_return_float ():
    distance = functions.calculate_distance("55.454367","37.545675")

    assert type(distance) is float
