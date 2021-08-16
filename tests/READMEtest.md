



# 1. <small>def</small> 	search_address_on_map (address):



**input:** any string address

**output:** url with coordinates of this address

**pass:** when the system get to collect the url with the address coordinates

**fail:** when the system doesnt get to collect the coordinates or other selenium's fail 

```
def test_search_address_on_map_input_address_return_url ():
        user_address_url = functions.search_address_on_map("MKAD")
        
        assert user_addres_url == "https://yandex.com/maps/213/moscow/geo/mkad/8059375/?ll=10.854186%2C49.182076&mode=search&sll=10.854186%2C49.182076&sspn=82.177734%2C31.812523&text=mkad&z=4"
```





# 2. <small>def</small> 	get_array_user_coordinates (current_url): 

**input:** address URL on yandex map

**output:** float list with address coordinates [latitude, longitude]

**pass:** when the value its float

**fail**: any selenium's fail 

```
def test_get_array_user_coordinates_parameter_url_return_coordinates ():
    user_coordinates_list = functions.get_array_user_coordinates("https://yandex.com/maps/?ll=10.854186%2C49.182076&mode=search&sll=10.854186%2C49.182076&sspn=82.177734%2C31.812523&text=MKAD&z=4")

    assert user_coordinates_list == [55.898947,37.632206]
```



# 3. <small>**def**</small> 	verify_if_inside_mkad (lat_user,long_user):



set 4 diferent address examples to verify if function is working correctly: 

**New York:** located outside MKAD to verify if function returns FALSE

**Basmanniy District:** address inside MKAD to verify if function returns TRUE

**latitude inside, longitude outside:** verify if function returns FALSE

**Latitude outside, longitude inside:** verify if function returns FALSE

```
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
```



input **Basmanniy District coordinates** and pass the test when the returned its **True**, because if you check on map, this address is located inside MKAD.

```
def test_verify_if_inside_mkad_input_latlong_return_true ():
    
    address_inside_mkad = functions.verify_if_inside_mkad(basmanniy_district_latitude,basmanniy_district_longitude)
    
    assert address_inside_mkad == True
```

input **New York coordinates** and pass the test when value returned is False 

```
def test_verify_if_inside_mkad_input_latlong_return_false ():
    address_inside_mkad = functions.verify_if_inside_mkad(new_york_latitude,new_york_longitude)
    
    assert address_inside_mkad == False
```

Pass the test when the **TypeError** raises because string values were imputed

```
def test_verify_if_inside_mkad_input_string_return_typeError ():
    with pytest.raises(TypeError):
        address_inside_mkad = functions.verify_if_inside_mkad("55.656947","37.545234")
```



input latitude value located inside MKAD, but longitude located out. Pass the test when the value returned is False

```
def test_verify_if_inside_mkad_input_latinside_longoutside_return_false ():
    
    address_inside_mkad = functions.verify_if_inside_mkad(latitude_inside_mkad,longitude_outside_mkad)
    
    assert address_inside_mkad == False
```



Input latitude value located outside MKAD, but longitude located inside. Pass the test when the value returned is False

```
def test_verify_if_inside_mkad_input_latoutside_longinside_return_false ():
    
    address_inside_mkad = functions.verify_if_inside_mkad(latitude_outside_mkad,longitude_inside_mkad)
    
    assert address_inside_mkad == False
```



# **4. <small>def</small> 	calculate_distance(lat_user,lon_user):**

Input float latitude and longitude values and pass the test when the type value of variable distance is float

```
def test_calculate_distance_input_latlong_return_distancekm ():
    distance = functions.calculate_distance(new_york_latitude,new_york_longitude)

    assert type(distance) is float
```

Does not pass the test because is missing longitude positional argument, 

```
def test_calculate_distance_not_input_longitude ():
    distance = functions.calculate_distance(new_york_latitude)

    assert type(distance) is float
```

Pass the test when are imputed int values and returned float values

```
def test_calculate_distance_input_int_value_return_float ():
    distance = functions.calculate_distance(55,67)

    assert type(distance) is float
```

Pass the test when are imputed string values and returned float values

```
def test_calculate_distance_input_string_return_float ():
    distance = functions.calculate_distance("55.454367","37.545675")

    assert type(distance) is float
```



