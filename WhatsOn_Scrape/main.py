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
        option.add_argument("--no-sandbox")
        option.add_argument("--headless")
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
                        self.data_dict["Date"].append(data)

                    elif column_element == 2:
                        if len(data) == 0:
                            data = "NONE"
                        self.data_dict["Event"].append(data)

                    elif column_element == 3:
                        if len(data) == 0:
                            data = "NONE"
                        self.data_dict["Location"].append(data)

                    elif column_element == 4:
                        if len(data) == 0:
                            data = "NONE"
                        self.data_dict["Venue"].append(data)

                    elif column_element == 5:
                        if len(data) == 0:
                            data = "NONE"
                        data = data.split("/")
                        self.data_dict["Type"].append(data)

                except:
                    break
        return self.data_dict

    def save_data(self):
        try:
            csv_file = "whatsonmalta.csv"
            dict_df = pandas.DataFrame.from_dict(self.data_dict)
            dict_df.to_csv(csv_file, index=False)
        except IOError:
            print("I/O error")

    def quit(self):
        self.driver.quit()



if __name__ == '__main__':
    scrape = Scrape(numbers_per_page=argv[1], from_date="17/01/2020", to_date="24/01/2020")
    scrape.startSelenium()
    scraped_dict = scrape.parseData()
    scrape.save_data()
    scrape.quit()
