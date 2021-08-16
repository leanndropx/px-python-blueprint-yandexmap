# This repository contains: 



1. A Blueprint Flask application collect imputed address by any user, with selenium access Yandex map, write the address on search label, click on search button, get the new URL with the address imputed coordinates, after use requests and BeautifulSoup to works on HTML extract the coordinate values in string type, convert to float type, verify if coordinates are out or inside MKAD, and finally works from a conditional to calculate the distance - if addres are out - or not calculate the distance - if address are located inside. The blueprint contains 2 directories: **main**, where app return Homepage, and result, route where are located all the backend and return result of application. 
2. A file **READMEcode.md**, especifically README created to explains the functions and also the code in @result.route
3. 1 directory named **TESTS**, where are located the Unit tests of application, and a file name **READMEtest.md**, which explains all the scenarios of created tests.
4. 1 file named **webserver.py**, where are setted a server of application.

   



# The libraries used in this Blueprint were:



1. **Blueprint from flask**: used to create the modular web application
2. **Request**: used to caption a html forms content, in this case, the imputed address by user 
3. **selenium**: to compose the works backend, driving on map and doing what was necessary to complete the task 
4. **requests**: I decided use requests as a alternative to solve a thecnical question that I did not to get, because I failed to get coordinates from HTML elements using selenium. 
5. **BeautifulSoup**: as a requests, I use to solve the same thecnical question exposed above
6. **Geopy**: used to convert coordinates from decimal degrees and calculate the distance in KM.
7. **Pytest**: used to runs all the Unit tests of application. 



# You can follow the steps bellow to better explore this application:



First, is important to expose here that this program still not complete and not in your better version that I believe it could be, there is a points I'm still workings on and thecnical questions that I'm trying to solve. I decided to comes out this version to show another elements of thinking a program and can show my way to works, write, and think all the process. Anyway, for a right version when it be you can follow the steps bellow:


1. Clone the repository to your devs environment

2. Open the terminal and move yourself to the directory. 

3. In command line, type **pip3 install flask --users** to install the selenium library

4. In command line, type **pip3 install selenium --users** to install the selenium library

5. In command line, type **pip3 install webdriver_manager --users** to install webdriver_manager library.

6. In command line, type **pip3 install requests --users** to install requests library.

7. In command line, type **pip3 install bs4** to install bs4 which will used with a BeautifulSoup module

8. In command line type **pip3 install geopy** to instal geopy library, chosen to be used as a convert coordinates library 

9. In command line, type **pip3 install pytest --users** to install the selenium library

10. You need to certify you have a Google Chrome installed in your computer.

    

Affer concluded necessary libraries installations, we can try to run and works on application:

9. Inside a main directory named **px-python-blueprint-yandexmap** type in command line **python3  webserver.py**
10. The program starts running 
11. Copy the address server, paste in your browser and loads  
12. Type the addres in a address label. 
13. Wait the backend works and if all runs right you will face the output: "the distance from address imputed to MKAD is XXXX" or "We dont need to calculate the distance because the addres computed is located inside MKAD"



For runs the tests, in command line, inside **px-python-blueprint-yandexmap**, type  **python3 -m pytest**



#  How the content is organized:



The executable file are composed by 3 python files: main.py , functions.py, _tests.py  - and 2 html files located inside templates directory 

1. **webserver.py:** start a server of application

2. **READMEcode.md:** readme especifally created to explains all the functions line by line and also code of @result.route

   

3. **app (directory)**: contains ther core of application, other 3 directories with Blueprints started, and 2 executable files:

   

   1. **____init____.py**: executable Python file starts a Flask and register all the blueprints created.

   2. **main (directory)**: contains the Blueprint **@main.route**, which render the index.html template. The blueprint are composed by 2 Python executable files:

      - **init___.py**: set and start a blueprint @main.route after create a main variable with Blueprint class insid
      - **views.py**: where are located the code of application wich will be rendered in a HomeHTML page

      

   3. **result (directory):** contains the blueprint **@result.route**, which render the result.html template. Also contains 2 Python executable files, that set and starts it works

      - **____init___.py**: set and start a blueprint @result.route after create a result variable with Blueprint class inside

      - **views.py**: where are located the code of application wich will be rendered in a Result HTML page. This route contains the core code of application.

   4. **functions.py**: here are located all the functions that were created to organize and runs the code. 



4. **templates (directory)**: directory where are located the 2 html files that compose the web application: index.html, result.html:	

   - **index.html:** simple  home page where the user inout the address

   - **result.html:** results page where the outputs are returned, in the case, the distance or a message informing will be not necessary calculate, because the addres are inside MKAD. 



5. **_tests (directory):** this directory contains:  

   - **test_functions.py**:  test with pytest many diferents input and output scenarios of created functio

   - **READMtest.md**: explains all the test functions created. 





# How was my thinking to drive this task:



First I tried to understand the context of task to chek what knowledge I had and what I would have to learn. So I realized I could use my experience with some libraries to complete most task, but I would have to learn:

1.  Blueprint: I understood that is a module from flask used to scale and modulate application, that all the routes are personalized and stored in folders with the name of route. So, the @app.route that I used to use in my project, would be changed to nameofroute.route. Example: @result.route to result's page of application.
2. Unit Tests: I had never experienced unit tests before. After exploring I understood that is way to check inputs and outputs of function's application, so I decided to explore Pytest to use in this project. The result was the file test_functions.py located inside a tests directory of this repository. I believe there is many points to improve, but I think I got to do something. 
3. Docker: also never experienced this stack before, how it would be considered a plus, I decided to focus in another tasks, but I understood generally that doccker is a way to create images of system's to set and facilitate development environment, since the same project can be accessed from many different machines. 



# Then, I started thinking: 



1. I googled what is Yandex, because I did not know what it was, so I discovered that is the biggest searcher in Russia and thats also contains a map app. 

2. I accessed the URL sent in doc test, found a language that I did not know, realized that was russian because of **.ru**   

3. So I changed **.ru** to **.com** and accessed the english version to start a task, because I have no knowledge in russian.

   - URL sent in russian: https://yandex.ru/dev/maps/geocoder/doc/desc/concepts/about.html

   - URL sent  in task: https://yandex.com/dev/maps/geocoder/doc/desc/concepts/about.html

4. Started to explore the platform.

5. Accessed the **"Maps"** icon  to know the maps app of Yandex.  

6. Entered in maps "MKAD" to localize the Moscow Ring Road and try to understand the thinking I would need to have to build the application. 

7. I understood there are coordinates in map and this could be the starter to build the conditional that would check if address are inside or out MKAD. 

8. Started to click in different points of map to understand latitude and longitude context. 

9. Then, I chose 4 limit points in MKAD circunference 

10. Since I selected 4 limit points inside MKAD circunference, I would have to use them in conditional to check if address imputed are inside or out MKAD. The values were marked in bold bellow:

    

    Latitude_higher = **55.911195**, 37.576244

    latitude_lower = **55.572492**, 37.675021

    longitude_higher = 55.821680, **37.837073**

    longitude_lower = 55.784416, **37.370051**

    

    So, if the address entered contains  values  (lat and long) located inside this values especifed above, they will be computed as a inside MKAD address, else it will be computed as outside address. 

    

    Example in code: 

    if latitude < 55.911195 and latitude > 55.572492 and longitude < 37.837073 and longitude > 37.370051: 

    ​					**Distance not computed because the address are located inside MKAD**

    Else:

    ​					**The code continues to calculate the distance**



11. After this understanding, I started all the work resulted in this respository, with libraries and functions used to achieve the goals.
