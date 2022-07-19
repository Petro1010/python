# Get element with specific attribute: //tagName[@AttributeName="Value"]

# Get text of element: //tagName/text()

# Select only one of the possible elements: //tagName[index]

# Boolean expressions can also be used within the [ ... ]

# Using the contains method: p[contains(@class, 'script')]

# /  select children from node set on left side of it
# // matching node set can be anywhere from document

# Ex. //root/h1 will get the h1 children of the root element

# .  refers to present node
# .. refers to parent node

#Ex. //h1/.. will give the parent node of h1

# * selects all elements
# ./* selects all chidren elements

# Use ctrl-F on inspect to find an element by its Xpath

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd



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

df_headlines.to_csv("headline.csv")

driver.quit()  #close the driver