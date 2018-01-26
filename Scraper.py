from bs4 import BeautifulSoup
from selenium import webdriver


class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome(r'cd.exe')

    def Login(self, usr, pword):
        self.driver.get("https://mbasic.facebook.com")
        self.driver.find_element_by_name('email').send_keys(usr)
        self.driver.find_element_by_name('pass').send_keys(pword)
        self.driver.find_element_by_name('pass').send_keys('\n')
    
    def getSource(self, url):
        self.driver.get(url)
        return self.driver.page_source

    def close(self):
        self.driver.close()


class Scraper():
    def __init__(self):
        self.host = 'https://mbasic.facebook.com'

    def setHtml(self, html):
        self.bs = BeautifulSoup(html, 'html.parser')

    def getNavLinks(self):
        retVal = []
        links = self.bs.find_all('div', {'class' : 'h'})
        for link in links:
            retVal.append((link.a.text, self.host + link.a['href']))
        return retVal

    def scrape(self):
        div = self.bs.find('div', {'id' : 'structured_composer_async_container'})
        divs = div.find_all('div', {'role' : 'article'})

        retVal = []
        for d in divs:
            tmp = d.find_all('div')
            if len(tmp) >= 3:
                post = tmp[2].text
                retVal.append(post)
        return retVal
