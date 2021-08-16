#  How the file functions.py was planned:



After understanding task, I started thinking steps and actions to achieve the goals system, so I set my mind 4 necessary actions which were resulted in 4 functions located in a file that I named functions.py, inside app directory. Bellow the steps:

1. Access the URL map with selenium library, search the address imputed by user and get the new URL that was generated, this way I used it to do a request, then use SOUP to extract HTML content coordinates.
2. With the new URL collected, I would try to access this current URL by requests and extract content using Beautiful Soup. In the same function, I would convert the string coordinates extracted to a float coordinates and save them in a list, to use in the next step
3. With the coordinates in hands, I would need to verify is this datas would reflect a inside MKAD address or out MKAD address, to do this I create a function **verify_if_inside_mkad (lat_user, long_user)** , that compare the address coordinates with the limit coordinates I chose from 4 edge points of MKAD circunference on map. This function returns True or False
4. Lastly, if the address would located out of MKAD, I would need calculate the distance, so I create a funtion **calculate_distance (lat_user, long_user)** to perform this action. 



So, the steps above were reflect in the 4 functions bellow:

1. 

   ```
   def search_address_on_map(address):
   ```

2. ```
   def get_array_user_coordinates (current_url):
   ```

3. ```
   def verify_if_inside_mkad (lat_user,long_user):
   ```

4. ```
   def calculate_distance(lat_user,lon_user):
   ```



Now, we'll  go in each one of them:



# 1. <small>def</small> 	search_address_on_map (address):



Declare a function with def, in line **driver.get("https://yandex.com/maps/?ll=10.854186%2C49.182076&z=4")**, try to access with driver a Yandex URL, wait 4 seconds and print a message in console in a positive response 

```
def search_address_on_map(address):

    driver.get("https://yandex.com/maps/?ll=10.854186%2C49.182076&z=4")
    sleep(4)
    print("SUCCESSFUL ACCESS")    
```



Wait 15 seconds to continue, I try this way because I had few problems with this part of code, for many times the system didnt get to access the search's label XPATH element to write the address. What was happenig was  that the first time I tried to run the code, the program works perfectly on this piece of code, but second time not. 

```
sleep(15)
    input_search = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div/form/div[2]/div/span/span/input")
```

I tried to solve using this way, explicit wait suggested in selenium to do the driver wait the page loads completely,  but also didnt works and returned a error: 

```
# input_search = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div/div/form/div[2]/div/span/span/input')))
```



same is happening here, to get a search's button XPATH element. I' using it for now:

```
    sleep(15)
    button_search = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div/form/div[3]/button/span/div")
```

I also tried to use:

```
#    button_search = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div/div/form/div[3]/button/span/div')))
```



Then, in the case of succesful collecting XPATH elements, I use the method **.send_keys()**, to write the address on search label, and **.click ()** to click on search button.

```
    input_search.send_keys(address)
    button_search.click()
```



if the writing was successful on the search label, it will be printed on console. Then, was setted a variable current_url that receive a method **.current_url** to collect the URL that was generated after a imputed address. Finally, use **driver.quit** () to finalize the driver. 

```
   print("Successed input")
    current_url = driver.current_url
    driver.quit() 
```



This function will return a variable with address URL content 

```
   return current_url
```



# 2. <small>def</small> 	get_array_user_coordinates (current_url): 



<strong>request_address =</strong> use requests to access the Address URL, then <strong>html_text</strong> receives the text content with method .text, lastly use BeautifulSoup to organize the content in a <strong>soup</strong> variable.

```
def get_array_user_coordinates (current_url):
    
    request_address = requests.get(current_url)
    html_text = request_address.text
    soup = BeautifulSoup(html_texto, 'html.parser')

```



use the method <strong>.find</strong> (. )  to find the HTML element where coordinates are located, save this data in <strong>coordinates_element</strong>. After analyzing HTML structure, I understood that content element was a list and coordinates was located in [ 0 ] index position.  

So, I started a loop in this element and created a conditional that extracted only 0 index position, then save this data in a variable named coordinates_text , it names is because the content extracted was a string.  

```
    coordinates_element=soup.find(class_="toponym-card-title-view__coords-badge")
    for index,coordinates in enumerate(coordinates_element):
        if index==0:
            coordinates_text=coordinates

```

The next step was convert the string values of coordinates to float values of coordinates. To do this, firstly I split the strings using a comma parameter to separate the text of latitude and longitude, then saved them in separed positions inside a list named coordinates_list_float. 

```
    coordinates_list_string = coordinates_text.split(',')
    coordinates_list_float = [float(coordinates_list_string[0]) ,float(coordinates_list_string[1])]

```

Finally, the function returns to this list value with float datas of latitude and longitude. 

```
    return coordinates_list_float
```



# 3. <small>**def**</small> 	verify_if_inside_mkad (lat_user,long_user):



After get a coordinates and convert to float values, I settted a function to compare if this values reflect a address located out or inside MKAD. So, firstly I navigate on map to find 4 limit points around MKAD circunference. I tried to chose the maximum latitude and longitude point, and minimum latitude and longitude points, that were resulted in the datas bellow:

```
def verify_if_inside_mkad (lat_user,long_user):
    
    latitude_higher_mkad = 55.911195
    latitude_minimun_mkad = 55.572492
    longitude_higher_mkad = 37.837073
    longitude_minimum_mkad = 37.370051

```



So, I setted the conditional to compare values and definitely check if addres are located inside or out MKAD circunference. If latitude or longitude values of user was under one of this points defined above,  the addres are inside, else, are out. This function returns the value True - inside - or False - outside. 

```
    if lat_user < latitude_higher_mkad and lat_user > latitude_minimun_mkad     and     long_user < longitude_higher_mkad and long_user > longitude_minimum_mkad:
        return True
    else:
        return False

```



# **4. <small>def</small> 	calculate_distance(lat_user,lon_user):**



When I was searching and trying to understand how I would do to convert the values of coordinates, I found a lot of libraries and function possibilites to do this work, with diferent types of math calculates like a haversine, vincenty and other theories.  I would have to choose one and the chosen was geopy library with geodesic function. 

First, the function was declared, then were setted 2 variables, one to set latitude and longitude of user address imputed, and other to set latitude and longitude of MKAD. For this calculation, I use the MKAD coordinates that are outputted on map when the MKAD addres is typed. 

```
def calculate_distance(lat_user,lon_user):
    user_coordinates = (lat_user, lon_user)  # (latitude, longitude) don't confuse
    mkad_coordinates = (55.898947, 37.632206)
```



Then, I setted a variable named <strong>distance_in_km</strong> to receive geodesic function - with kilometers method - that runs this work of calculation 

```
distance_in_km = geodesic(user_coordinates, mkad_coordinates).kilometers
```



Lastly, the function returns to this variable setted tha contains the result: <strong>distance in Km</strong> 

```
return distance_in_km
```





# How the **Blueprint** was planned: 



It was my first time with Blueprint, I understood that Blueprint is definetly necessary to scale applications, because can modulate them. 

## MAIN (DIRECTORY)

Contains the files init.py and views.py. 

## @main.route



1. Import libraries and Start a @main.route, here will be render the index.html, where the user will input the address to get the coordinates. In Flask, to create a route you always need to use @app.route('name_of_page') folowed by a function.

   ```
   from . import main
   from flask import render_template
   from app import functions
   
   @main.route ("/")
   def home():
       return render_template("index.html")
   
   ```

## RESULT (DIRECTORY)

Contains the files init.py and views.py

## @result.route

1. Start a '/result' route and def a function result ( ), where the core's backend application are located. 

2. Then, set a user_address variable, where request function will be used to get a form html content, in this case, a address imputed. I print in the code just to verify in console if the request was workings right

   ```
   @result.route('/result')
   def result():
       user_address = request.args.get("address")
       print(user_address)
   
   ```

3. Set a variable **user_address_url** to receive the function **funcoes.search_address_on_map**, which will access the URL map, write a address on a search label, click on button and after new URL was loaded the function will get this URL and save in array to use in the next step 

   ```
   user_address_url = funcoes.search_address_on_map("user_address")
   ```

4. Set a variable **user_coordinates_list** to receive the function **funcoes.get_array_user_coordinates** which will use requests to access the new URL and BeautifulSoup to get the coordinates HTML elements in string, after will convert in a float and save in array.  

   ```
   user_coordinates_list = funcoes.get_array_user_coordinates(user_address_url)
       print(user_coordinates_list)
   ```

5. After save a coordinates in array, it will separate in two diferent variables: **lat_user** to save the latitude of address imputed by user, and **long_user** to save the longitude of address imputed by user

   ```
   lat_user = user_coordinates_list [0]
   long_user = user_coordinates_list [1]
   
   ```

6. Set a variable **address_inside_mkad** to receive the **verify_if_inside_mkad ( lat_user , long_user)** function that wil compare the values of coordinates imputde with the limit MKAD coordinates chosen to do this works. This functions returns True if the address was considered inside or False if it out. 

   ```
   address_inside_mkad = funcoes.verify_if_inside_mkad(lat_user,long_user)
   
   ```

7. Set a conditional from a data formed above, which validate if the addres are out or inside. If address was inside, set a variable distance with the string message "Not necessary to calculate the distance...*, if is out, the same will receive a function **calculate_distance (lat_user, long_user)** which convert the decimal degress of coordinates and calculate the distance. 

   ```
   if address_inside_mkad:
      			distance="Not necessary to calculate the distance because the address is inside MKAD"
   else:
           distance = funcoes.calculate_distance(lat_user,long_user)
   
   ```

8. Lastly, wil return the function **render_template** containing the parameters **'result.html**, that will be rendered, the variable address with the address string, and distance with the distance or string  to compose a message output on result page.

   ```
   return render_template('result.html',user_address=user_address,distance=distance)
       
   ```

   

