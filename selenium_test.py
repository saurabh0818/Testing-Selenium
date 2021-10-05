from selen import *




#============= INPUT VALUE INTO TEXT BOX ==================
    
def input_value(data):
    _data = data
    bol = page_load("q")
    if bol is True:
        input_data = xpath("name","q")
        input_data.send_keys(_data)
        time.sleep(1)
        click_by_name("btnK")
        time.sleep(1)
        scroll()
        time.sleep(1)
        try:
            click_by_link_text("2")
            time.sleep(2)
            scroll()
            open_new_tab("https://c8.alamy.com/comp/T8ARYH/word-writing-text-tsask-completed-business-photo-showcasing-finished-action-or-assignments-that-has-no-remaining-duration-hand-holding-megaphone-and-o-T8ARYH.jpg")
            
        except():
            print("Error")
        
    else:
        input_value('Testing with Selenium')



#============= LOGIN WITH USER ID & PASSWORD ON SAME PAGE =====================


def login_all(usr_id,usr_pass):
    user_ID = usr_id
    usr_PASS = usr_pass
    input_ID = browser.find_element_by_xpath("//*[@name='']")
    input_ID.send_keys("usr_ID")
    input_PASS = browser.find_element_by_xpath("//*[@name='']")
    input_PASS.send_keys("usr_PASS")
    time.sleep(3)
    btn_click = browser.find_element_by_name('btn')
    btn_click.click()



#============ LOGIN WITH USER ID & PASSWORD ON DIFFERENT PAGES ==================

    
def login_one_by_one(user_id,usr_pass):
    user_ID = user_id
    usr_PASS = usr_pass
    input_ID = browser.find_element_by_xpath("//*[@id='identifierId']")
    input_ID.send_keys(user_ID)
    click_span("RveJvd snByac")
    input_PASS = browser.find_element_by_xpath("//*[@name='password']")
    input_PASS.send_keys(usr_PASS)
    time.sleep(3)
    click_span("RveJvd snByac")



########## ActionChain ##############

def action():
    input_data = browser.find_element_by_xpath("//a[@id='gb_70']")
    if input_data:
        action = ActionChains(browser)
        action.move_to_element(input_data)
        action.context_click(input_data)
        action.perform();
        time.sleep(1)
        action.send_keys(Keys.ARROW_DOWN).perform()
        #action.click(input_data)
        action.perform()
    else:
        print("Calling action Function")
        action()

open_browser("https://google.com")
input_value("Selenium with Python")

