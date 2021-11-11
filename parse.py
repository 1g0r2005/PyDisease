from bs4 import BeautifulSoup
from selenium import webdriver

urlTable = "https://www.malacards.org/categories/respiratory_disease_list"

def getWeb(url):
    wd = webdriver.Chrome(executable_path="C:/Users/student/Downloads/Parse/chromedriver")
    wd.get(url)
    html = BeautifulSoup(wd.page_source,"html.parser")
    wd.quit()
    return html

print(getWeb(urlTable))