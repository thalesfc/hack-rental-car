from datetime import date, time
from common import istype_or_error, Data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Companies(object):
    @staticmethod
    def check_parameters(start_date, end_date, pickup_time):
        istype_or_error(start_date, date,
                        "Start date not of the %r" % date)
        istype_or_error(end_date, date,
                        "End date not of %r" % date)
        istype_or_error(pickup_time, time,
                        "Pickup time not of %r" % time)

        # check if pickup_time is multiple of 30 mins
        if pickup_time.minute % 30 != 0:
            raise ValueError("Pickup time minutes must be 00 or 30, " +
                             "got %s instead." % pickup_time.minute)

    @staticmethod
    def set_city(browser, city, city_name):
        # type city_name in input_css
        browser.find_element_by_css_selector(city.INPUT_CSS)\
            .send_keys(city_name)

        # wait for conformation windows
        WebDriverWait(browser, 3).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, city.CONFIRMATION_CSS)))

        # click on confirmation windows
        browser.find_element_by_css_selector(
            city.CONFIRMATION_CSS).click()

    @classmethod
    def get_data(cls, browser):
        WebDriverWait(browser, 7).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, cls.CARS.CONTAINER_XPATH)
            )
        )
        cars = browser.find_element_by_xpath(cls.CARS.CONTAINER_XPATH)
        carList = cars.find_elements_by_xpath(cls.CARS.LIST)

        returned = []

        for car in carList:
            data = Data()
            data.brand = cls.__name__
            data.category = car.find_element_by_xpath(
                cls.CAR.CATEGORY_XPATH).text
            price = car.find_element_by_xpath(
                cls.CAR.PRICE_XPATH).text
            price = price.replace("$", "")
            data.price = int(float(price))

            returned.append(data)
        return returned

    @classmethod
    def get_prices(cls, start_date, end_date, pickup_time,
                   pickup_city, return_city):
        Companies.check_parameters(start_date, end_date, pickup_time)

        # opening URL
        chromedriver = "/Users/thalesfc/Downloads/_tmp/chromedriver"
        browser = webdriver.Chrome(executable_path=chromedriver)
        browser.get(cls.URL)

        # wait for page to load
        WebDriverWait(browser, 5).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, cls.PICKUP_CITY.INPUT_CSS)))

        # setting pickup city
        Companies.set_city(
            browser,
            cls.PICKUP_CITY,
            pickup_city
        )

        # setting up return city
        if pickup_city != return_city:
            browser.find_element_by_css_selector(
                cls.SAME_LOCATION_CHECKBOX_CSS).click()
            Companies.set_city(
                browser,
                cls.RETURN_CITY,
                return_city
            )

        # setting up date / time
        browser.find_element_by_css_selector(cls.PICKUP_DATE_CSS)\
            .send_keys(start_date.strftime("%m/%d/%Y"))

        browser.find_element_by_css_selector(cls.DROPOFF_DATE_CSS)\
            .send_keys(end_date.strftime("%m/%d/%Y"))

        ttime = pickup_time.strftime("%H%M")
        browser.find_element_by_xpath(
            (cls.TIME.PICKUP_XPATH % ttime)).click()

        browser.find_element_by_xpath(
            (cls.TIME.DROPOFF_XPATH % ttime)).click()

        # submit
        browser.find_elements_by_css_selector(cls.SUBMIT)[-1].click()

        # get data
        return cls.get_data(browser)
