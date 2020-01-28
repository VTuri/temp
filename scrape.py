from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep


# TODO: find a normal name to the screenshot like: month, type of consumption
# TODO: use while loop to prompt for new value

def prompt_status():
    """
    Prompts the user for the current status of the given cost type
    :return: integer of the current level
    """

    level_input = input('Please provide the current level: ')
    try:
        level_val = float(level_input)
        print(level_val)
    except ValueError:
        print('The value you provided is not a number!')


numbers_per_page = str(100)
page_index = str(1)
from_date = "17/01/2020"
to_date = "24/01/2020"
# TODO page index check
url = "https://www.whatson.com.mt/en/events/events/bycategory//publish_date/asc" \
      "/{}/{}/events.htm?from={}&to={}&view=list".format(numbers_per_page, page_index, from_date, to_date)


class Scrape(object):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    rows = []
    for i in range(1, int(numbers_per_page)):
        try:
            text = driver.find_element_by_xpath("/html/body/div[3]/div[11]/div[{}]".format(i))
            data = text.text
            data = data.split("\n")
            rows.append(data)
        except:
            break

    columns = rows[0]
    columns = [i.strip(":") for i in columns]
    data_dict = dict.fromkeys(columns, [])

    column1 = []
    column2 = []
    column3 = []
    column4 = []
    column5 = []

    for row_index in range(1, len(rows)):
        try:
            column1.append(rows[row_index][0])
            column2.append(rows[row_index][1])
            column3.append(rows[row_index][2])
            column4.append(rows[row_index][3])
            column5.append(rows[row_index][4])
            # data_dict["Event"].append(rows[row_index][1])
            # data_dict["Location"].extend(rows[row_index][2])
            # data_dict["Venue"].extend(rows[row_index][3])
            # data_dict["Type"].extend(rows[row_index][4])
        except IndexError:
            continue



    print("lol")

    def __init__(self, url, ):
        self.url = url


""

# def open_browser(self):
#     browser_open = self.browser
#     browser_open.get(self.GAS_URL)
#
# def post_consumption(self):
#     browser = self.browser
#     current_value = browser.find_element_by_name('havifogyasztas')
#     current_value.clear()
#     current_value.send_keys(self.consumption)
#

# def post_value(self):
#     current_value = self.browser.find_element_by_name('futoertek')
#     current_value.clear()
#     current_value.send_keys(str(self.consumption))
#
# def calculate(self):
#     calculate_button = self.browser.find_element_by_xpath("//input[@type='button' and @value='Számol']")
#     calculate_button.click()
#
# def screenshot(self):
#     sleep(1)
#     self.browser.save_screenshot(self.GAS_PIC_NAME)
#
# def save_price(self):
#     price = self.browser.find_element_by_xpath("//input[@class='mezo' and @name='havi1afasl']")
#     price = price.get_attribute('value')
#     price = price.replace(' ', '')
#     price = int(price)
#     return price

# def run_scrape(self):
#     self.open_browser()
#     self.post_consumption()
#     self.select_company()
#     self.post_value()
#     self.calculate()
#     self.screenshot()
#     self.final_price = self.save_price()
#     return self.final_price

Scrape(url)
print("Lol")
