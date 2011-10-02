try:
    import spynner
except:
    print 'Is necessary install spynner library in http://pypi.python.org/pypi/spynner'
try:
    from BeautifulSoup import BeautifulSoup
except:
    print 'Is necessary install python-beautifulsoup package'

class browser():
    browser=spynner.Browser(debug_level=spynner.ERROR)
    #browser.create_webview(show=True)
    browser.set_html_parser(BeautifulSoup)

