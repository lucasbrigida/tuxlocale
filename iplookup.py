from browser import browser
from proxies import proxies

class iplookup(browser):

    info={}
    proxies=[]

    def get_locale(self,ip='0.0.0.0',use_proxy=False,proxy_list_file='',*proxy):

        browser=self.browser

        if use_proxy == True:
            try:
                if proxy:
                    browser.set_proxy(proxy)
                else:
                    proxy_list=proxies()
                    self.proxies=proxy_list.get(proxy_list_file)
                    print self.proxies
                    browser.set_proxy(self.proxies.pop())
            except:
                print "Cannot find 'proxies.list' file."
        

        while(True):
            try:
                # Code block to obtain data of other maxmind source
                #browser.load('http://www.maxmind.com/')
                #browser.fill("input[name=ips]",str(ip))
                #browser.submit("input.searchButton2")

                #soup=browser.soup

                #self.info['ip']=soup('td')[83].text
                #self.info['country_code']=soup('td')[84].text
                #self.info['country']=soup('td')[85].text
                #self.info['state']=soup('td')[87].text
                #self.info['city']=soup('td')[88].text
                #self.info['lat']=soup('td')[90].text
                #self.info['lng']=soup('td')[91].text
                #self.info['isp']=soup('td')[92].text
                #self.info['organization']=soup('td')[93].text

                browser.load("http://www.maxmind.com/app/mylocation")

                soup=browser.soup

                self.info['ip']=soup('td')[126].text
                self.info['country']=soup('td')[128].text
                self.info['state']=soup('td')[130].text
                self.info['city']=soup('td')[136].text
                self.info['lat']=soup('td')[140].text[0:8]
                self.info['lng']=soup('td')[140].text[9:]


                return self.info

            except:
                if len(self.proxies) >= 1:
                    browser.set_proxy(self.proxies.pop())
                    print 'Change proxy'
                    continue
                else:
                    break
        return None