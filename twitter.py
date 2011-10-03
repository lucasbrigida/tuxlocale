from browser import browser
from time import sleep

class twitter(browser):

    def login(self,username,password):
        while True:
            try:
                browser=self.browser
                browser.load("https://mobile.twitter.com/session/new")
                browser.fill('input[id=username]',username)
                browser.fill('input[id=password]',password)
                browser.wait(5)
                sts_opt=browser.submit('button#signupbutton.signup')

                if sts_opt == True: break
            except:
                print 'Try sign in  twitter again'
		sleep(10)
                continue
    def update_locale(self,msg=''):

        while True:
            try:
                browser=self.browser
                browser.fill('textarea#tweet_text.tweet_input',msg)
                sts_opt=browser.submit('button#tweet_submit.tweet-btns')

                if sts_opt == True: break
            except:
                print 'Try post in twitter again'
		sleep(5)
                continue
        #browser.browse()
