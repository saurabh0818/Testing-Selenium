from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Note : Your Have to Downlaod and and Place Driver on the Below Location.
browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")



#============== CHECKING PAGE LOAD =================


def page_load(element):
    load_element = element
    while True:
        search_element = browser.find_element_by_name(load_element)
        if search_element:
            return True
            break
        else:
            continue


#============= OPEN BROWSER ==================


        
def open_browser(link):
    site_link = link
    browser.maximize_window()
    try:
        browser.get(site_link)
    except:
        print("No Path given in Open Browser Function")



#============= CLICKING ELEMENT BY ID ==================


    
def click_by_id(element_id):
    id_element = element_id
    try:
        btn_click = browser.find_element_by_id(id_element)
        if btn_click:
            btn_click.click()
        else:
            print("No Element_ID in Click by ID")
    except:
        print("Error in Element By ID Function")




#============= CLICKING BY SPAN CLASS ====================


def click_span(clss):
    cls = clss
    try:
        span_value = browser.find_element_by_xpath("//span[@class='"+cls+"']")
        if span_value:
            span_value.click()
        else:
            print("No Class Found in Span Class")
    except:
        print("Error in Click By Span Function")



#============= CLICKING ELEMENT BY NAME ===================

    
def click_by_name(element_name):
    id_element = element_name
    try:
        btn_click = browser.find_element_by_name(id_element)
        if btn_click:
            btn_click.click()
            return btn_click
        else:
            print("No Such Element Name Found")
    except:
        print("Error in Click by Name Function")




#============ CLICKING ELEMENT LINK TEXT ===================

    
def click_by_link_text(text):
    id_element = text
    try:
        btn_click = browser.find_element_by_link_text(id_element)
        if btn_click:
            btn_click.click()
        else:
            print("No Such Value Found")
    except:
        print("Error in Click Link Text Function")



#=========== CLICKING ELEMENT BY CLASS NAME ================

    
def click_by_class_name(css_clsname):
    id_element = css_clsname
    try:
        btn_click = browser.find_element_by_class_name(id_element)
        if btn_click:
            btn_click.click()
        else:
            print("NO CSS Class Found")
    except:
        print("Error in Click By Class Name")



#============ CLIKING BY XPATH ========================


def xpath(typ,value):
    _value=value
    _type=typ
    try:
        path = browser.find_element_by_xpath("//*[@"+_type+"='"+_value+"']")
        if xpath:
            return path
        else:
            print("No such Element Found with Xpath")
    except:
        print("Error in Xpath Function")




#============ Scrolling Page =====================


def scroll():
    new_height = browser.execute_script("return document.body.scrollHeight")
    for x in range(0,new_height,100):
        browser.execute_script("window.scrollTo(0,'"+str(x)+"');")
        time.sleep(0.1)



def scro():
    new_height = browser.execute_script("return document.body.scrollHeight")
    browser.execute_script("window.scrollTo(0,'"+new_height+"');")
    while True:
        news_height = browser.execute_script("return document.body.scrollHeight")
        browser.execute_script("window.scrollTo('"+new_height+"','"+news_height+"');")
        time.sleep(0.1)



#============ OPEN NEW BROWSER TAB ================


def open_new_tab(url):
    _url = url
    browser.execute_script("window.open('"+_url+"');")



#=========== TAKING SCREEN SHOT ====================


def screenshot(img_name):
    try:
        browser.save_screenshot(img_name+".png")
    except:
        print("Error in Window_Btn Function")





