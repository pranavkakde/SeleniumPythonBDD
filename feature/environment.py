from selenium import webdriver  
from pages import searchpage

def before_all(context):  
    context.browser = webdriver.Chrome()
    context.SearchPage = searchpage.searchPage(context.browser)
  
def after_all(context):  
    context.browser.quit() 