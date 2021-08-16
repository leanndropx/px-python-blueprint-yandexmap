# Thechnical errors I'm facing and trying to solve: 



1. I'm facing a technical error (image attached in this directory) when the function **<big>search_address_on_map (URL)</big>** (ocated inside the file functions.py, that is located inside a directory app) uses selenium to try to get **XPATH** from search label to write the address. My coding, sometimes, runs perfectly until in the point of "write a address with selenium in a Yandex Map'. The script with selenium opens chrome, access the Yandex URL, input the address and click on search button. Another times, with the same script, the system does not work and the terminal returns this error above: 
2. I've tried to input the sleep() functions on script, because I was thinking the error was running because the page was not completely loaded while the script was trying collect the X Path elements. I also found on stackoverflow some simiraly cases thats were solved using wait functions on selenium, but also does not work in my case.



To solve, I tried to change this way:

```
sleep(15)
input_search = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div/form/div[2]/div/span/span/input")
```

for this way:

```
# input_search = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div/div/form/div[2]/div/span/span/input')))
```



but also did not work and returns the error bellow (image attached):

```
Traceback (most recent call last):
  File "/Users/leandropeixoto/Library/Python/3.8/lib/python/site-packages/flask/app.py", line 2088, in __call__
    return self.wsgi_app(environ, start_response)
  File "/Users/leandropeixoto/Library/Python/3.8/lib/python/site-packages/flask/app.py", line 2073, in wsgi_app
    response = self.handle_exception(e)
  File "/Users/leandropeixoto/Library/Python/3.8/lib/python/site-packages/flask/app.py", line 2070, in wsgi_app
    response = self.full_dispatch_request()
  File "/Users/leandropeixoto/Library/Python/3.8/lib/python/site-packages/flask/app.py", line 1515, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/Users/leandropeixoto/Library/Python/3.8/lib/python/site-packages/flask/app.py", line 1513, in full_dispatch_request
    rv = self.dispatch_request()
  File "/Users/leandropeixoto/Library/Python/3.8/lib/python/site-packages/flask/app.py", line 1499, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)
  File "/Users/leandropeixoto/Desktop/px-python-blueprint-unittest-yandexmap/app/result/views.py", line 10, in result
    user_address_url = functions.search_address_on_map(user_address)
  File "/Users/leandropeixoto/Desktop/px-python-blueprint-unittest-yandexmap/app/functions.py", line 25, in search_address_on_map
    input_search = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/div/div/form/div[2]/div/span/span/input")
  File "/Users/leandropeixoto/Library/Python/3.8/lib/python/site-packages/selenium/webdriver/remote/webdriver.py", line 394, in find_element_by_xpath
    return self.find_element(by=By.XPATH, value=xpath)
  File "/Users/leandropeixoto/Library/Python/3.8/lib/python/site-packages/selenium/webdriver/remote/webdriver.py", line 976, in find_element
    return self.execute(Command.FIND_ELEMENT, {
  File "/Users/leandropeixoto/Library/Python/3.8/lib/python/site-packages/selenium/webdriver/remote/webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "/Users/leandropeixoto/Library/Python/3.8/lib/python/site-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"/html/body/div[1]/div[2]/div[3]/div/div/div/form/div[2]/div/span/span/input"}
  (Session info: chrome=92.0.4515.131)
127.0.0.1 - - [16/Aug/2021 12:38:33] "GET /result?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 200 -
127.0.0.1 - - [16/Aug/2021 12:38:33] "GET /result?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 200 -
127.0.0.1 - - [16/Aug/2021 12:38:33] "GET /result?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 200 -
127.0.0.1 - - [16/Aug/2021 12:38:33] "GET /result?__debugger__=yes&cmd=resource&f=ubuntu.ttf HTTP/1.1" 200 -
```

