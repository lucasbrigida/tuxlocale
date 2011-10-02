class proxies():

    def get(self,proxies_list_file=''):

        if proxies_list_file != '':
            arq=open(proxies_list_file,'r')
        elif proxies_list_file == '':
            arq=open('proxies.list','r')
            proxies_list=arq.readlines()

            self.proxies=[]
            for proxy in proxies_list:
                self.proxies.append(proxy.strip('\n'))

            arq.close()
            return self.proxies
