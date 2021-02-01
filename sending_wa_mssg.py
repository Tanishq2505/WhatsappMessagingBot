from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep



#Important Functions 
def total_users():
    users = int(input("Enter Total number of users "))
    c = 0
    d = 1
    u_list = []
    total_messages = int(input("Enter Number of messages: "))
    while (c<users):
        u_list.append(input(f"Enter full name of user: {d} that you saved in device: "))
        c+=1
        d+=1
    return u_list, total_messages

def sending_message(contact, total_messages):
    i=0
    names_chat = driver.find_element_by_xpath("//span[@title='"+contact+"']")
    names_chat.click()
    sleep(1)
    user_input = input("Please Enter Your Message: ")
    sleep(0.5)
    while (i<total_messages):
        text_box = '//div[@class="_1awRl copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]'
        driver.find_element_by_xpath(text_box).send_keys(f"{user_input}"+Keys.ENTER)
        sleep(1)
        i+=1

def searching_user(contact,total_messages):
    a=0
    print(len(contact))
    while (a<len(contact)):
        search_box_id = '//div[@class="_1awRl copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"]'
        driver.find_element_by_xpath(search_box_id).send_keys(contact[a])
        sleep(3)
        sending_message(contact[a],total_messages)
        j = 0
        while j < len(contact[a]):
            driver.find_element_by_xpath(search_box_id).send_keys(Keys.BACK_SPACE)
            sleep(0.1)
            j+=1
        sleep(2)
        a+=1



#Main Code
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
input("Press Enter After You Have Scanned the QR code:")
sleep(1)
contact, messages = total_users()
searching_user(contact,messages)


#Exiting command
driver.quit()