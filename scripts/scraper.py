import time
from selenium import webdriver
from pyvirtualdisplay import Display

print("Startingggg")


display = Display(visible=0, size=(800, 800))
display.start()
print("Started")

outputdir = '/opt/app'
options = webdriver.ChromeOptions()
options.binary_location = '/opt/google/chrome/google-chrome'
service_log_path = "{}/chromedriver.log".format(outputdir)
service_args = ['--verbose']
driver = webdriver.Chrome('/usr/local/bin/chromedriver',
        chrome_options=options,
        service_args=service_args,
        service_log_path=service_log_path)

# driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
