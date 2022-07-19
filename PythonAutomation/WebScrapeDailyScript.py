from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime # manipulate date and time
import os
import sys

# this will allow us to automatically run a script
applicationPath = os.path.dirname(sys.executable) # get path of executable being created

date = datetime.now()

#MMDDYYYY
dateStr = date.strftime("%m%d%Y") # get time in string format, https://strftime.org/

website = "https://www.thesun.co.uk/sport/football/"
path = "C:/Users/petro/Downloads/chromedriver_win32/chromedriver.exe"

# headless mode, without the actual opening of the page
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)

driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')  #get all the elements with the specific Xpath

titles = []
subtitles = []
links = []

#get the titles from the containers we found
for container in containers:
    title = container.find_element(by="xpath", value='./a/h2').text # titles, just a single title per container
    subtitle = container.find_element(by="xpath", value='./a/p').text  # subtitles
    link = container.find_element(by="xpath", value="./a").get_attribute('href') # get the specific href value
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# now export this to a CSV file

# Create a dataframe using pandas
data = {"titles": titles, "subtitles": subtitles, "links": links}

df_headlines = pd.DataFrame(data)

file_name = f"headline--{dateStr}.csv"
finalPath = os.path.join(applicationPath, file_name) # this will create the correct path based on the os used

df_headlines.to_csv(finalPath)

driver.quit()  #close the driver

#To make this file automated/executable:
 # use command pyinstaller --onefile filename  (must be in folder with the py file)

 #To schedule the executable:
   # 1. Go to task scheduler
   # 2. Create Basic Task
   # 3. Select the trigger
   # 4. Choose the executable file under action
   # 5. Click Finish and all is done