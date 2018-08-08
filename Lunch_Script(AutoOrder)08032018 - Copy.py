from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Data collection from google spreadsheets

# Variables for menu items
menu = {
    "Burrito": 'Burrito',
    "Burrito Bowl": 'Burrito Bowl',
    "Tacos": 'Tacos',
    "Salad": 'Salad',
    "Chicken": 'Chicken',
    "Steak": 'Steak',
    "Barbacoa": 'Barbacoa',
    "Carnitas": 'Carnitas',
    "Sofritas": 'Sofritas',
    "Veggies": "Veggie",
    "White": 'White Rice',
    "Brown": 'Brown Rice',
    "No Rice": 'No Rice',
    "Black": 'Black Beans',
    "Pinto": 'Pinto Beans',
    "No Beans": 'No Beans',
    "Queso": 'Queso',
    "Guac": 'Guacamole',
    "Mild": 'Fresh Tomato Salsa',
    "Medium": 'Roasted Chili Corn Salsa',
    "Hot": 'Tomatillo-Red Chili Salsa',
    "Sour Cream": 'Sour Cream',
    "Fajita Veggies": "Fajita Veggies",
    "Cheese": 'Cheese',
    "Lettuce": 'Romaine Lettuce',
    "Chips Queso": 'Chips & Queso',
    "Chips_Guac": 'Chips & Guacamole',
    "Chips": "Chips",
    "Drink": "22 fl oz Soda/Iced Tea"
}

item_selected = "Burrito Bowl"

browser = webdriver.Chrome()
browser.get(('https://order.chipotle.com/Meal/Index/1435?showloc=1&_ga=2.208925074.16713686.1533133653-1282624716.1533133653'))

#try:
    #xpath = browser.find_element_by_xpath("//img[@alt='{}']".format(item_selected))
#except Exception:
    #print("Searching for elements")

# Functions

# The time set may need to be modified in the case a web page takes longer than what is set


def first_wait():
    firstWait = WebDriverWait(browser, 20)
    return firstWait


def wait_load():
    global item_selected
    wait = WebDriverWait(browser, 30)
    return wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='{}']".format(item_selected))))

# Parameter order, is of type Dict


def place_order(order_record):
    global item_selected
    global xpath
    global menu
    try:
        xpath = browser.find_element_by_xpath("//img[@alt='{}']".format(item_selected))
    except Exception:
        print("Searching for elements")
    #first_wait()
    wait_load()
    item_selected = order_record["What would you like from Chipotle?"]
    print(item_selected)
    xpath.click()
    item_selected = order_record["What kind of Burrito/Bowl/Salad would you like?"]
    #first_wait()
    wait_load()
    print(item_selected)
    xpath.click()
    item_selected = order_record["What kind of rice would you like?"]
    #wait_load()
    if item_selected == "" or item_selected.lower() == "none":
        item_selected = menu["No Rice"]
        xpath.click()
    else:
        xpath.click()
    item_selected = order_record["What kind of beans would you like?"]
    #wait_load()
    if item_selected == "" or item_selected.lower() == "none":
        item_selected = menu["No Beans"]
        xpath.click()
    else:
        xpath.click()



# The Taco form data is different from that of the Salad, Burrito, and Burrito Bowl

def tacoOrder():
    pass


test_order = {
    "Name:": "Tyler Wong", "What would you like from Chipotle?": "Burrito",
    "What kind of Burrito/Bowl/Salad would you like?": "Chicken",
    "What kind of rice would you like?": "White",
    "What kind of beans would you like?": "Black"
    }

place_order(test_order)
