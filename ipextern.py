from browser import browser
from re import compile,findall

class ipextern(browser):

    def getip(self):

        browser=self.browser
        browser.load('http://meuip.datahouse.com.br/')

        soup=browser.soup
        self.ip=soup('span',{'class':'meuip-home'})[0].string

        regexp=compile('(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')
        self.ip=findall(regexp,self.ip)[0].encode('ascii','ignore')

        

        return self.ip