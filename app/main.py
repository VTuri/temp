from selenium import webdriver
import pandas
from sys import argv

page_index = str(1)


# docker pull centos:centos8.1.1911
# TODO https://developpaper.com/centos7-install-selenium/

class Scrape(object):
    data_dict = {
        "Date": [],
        "Event": [],
        "Location": [],
        "Venue": [],
        "Type": [],
    }

    data_list = []
    rows = []

    def __init__(self, numbers_per_page, from_date, to_date, ):
        self.numbers_per_page = str(numbers_per_page)
        self.from_date = from_date
        self.to_date = to_date
        self.url = "https://www.whatson.com.mt/en/events/events/bycategory//publish_date/asc" \
                   "/{}/{}/events.htm?from={}&to={}&view=list".format(numbers_per_page, page_index,
                                                                      from_date, to_date)

    def startSelenium(self):
        option = webdriver.ChromeOptions()
        option.add_argument("no-sandbox")
        option.add_argument("headless")
        option.add_argument("privileged")
        option.add_argument("window-size=1200x800")

        self.driver = webdriver.Chrome(executable_path="./chromedriver", options=option)
        self.driver.get(self.url)

    def parseData(self):
        for row_element in range(1, int(self.numbers_per_page)):
            for column_element in range(1, 6):
                try:
                    text = self.driver.find_element_by_xpath(
                        "/html/body/div[3]/div[11]/div[{}]/div[{}]".format(row_element, column_element))
                    data = text.text

                    if column_element == 1:
                        if len(data) == 0:
                            data = "NONE"
                        self.data_dict["Date"] = data

                    elif column_element == 2:
                        if len(data) == 0:
                            data = "NONE"
                        self.data_dict["Event"] = data

                    elif column_element == 3:
                        if len(data) == 0:
                            data = "NONE"
                        self.data_dict["Location"] = data

                    elif column_element == 4:
                        if len(data) == 0:
                            data = "NONE"
                        self.data_dict["Venue"] = data

                    elif column_element == 5:
                        if len(data) == 0:
                            data = "NONE"
                        data = data.split("/")
                        self.data_dict["Type"] = data



                except:
                    break

            if len(self.data_dict) > 0:
                self.data_list.append(self.data_dict.copy())

            self.data_dict.clear()

        self.data_list = self.data_list[1:]

    def quit(self):
        self.driver.quit()

    def clear(self):
        self.data_list.clear()

    def clean_data(self):
        for event in self.data_list:
            if len(event["Type"]) > 1:
                event["Type"] = ', '.join(event["Type"])
            else:
                event["Type"] = event["Type"][0]

    def get_data(self):
        return self.data_list


if __name__ == '__main__':
    scrape = Scrape(numbers_per_page=100, from_date="01/02/2020", to_date="10/02/2020")
    scrape.startSelenium()
    scrape.parseData()
    scraped_list = scrape.get_data()
    scrape.quit()
