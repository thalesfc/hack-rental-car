from companies import Companies
from datetime import date, time


class Alamo(Companies):
    URL = "https://www.alamo.com/en_US/car-rental/home.html"

    class CAR:
        CATEGORY_XPATH = './/*[@class="car-description"]//h2'
        PRICE_XPATH = ('.//*[contains(@class, "ayment")]//' +
                       '*[contains(text(), "$")]')

    class CARS:
        CONTAINER_XPATH = '//ul[@class="carList"]'
        LIST = '//li[@class="cars" or @class="suvs"]'

    class PICKUP_CITY:
        INPUT_CSS = ("#_content_alamo_en_US_car_rental_home_jcr" +
                     "_content_reservationStart_pickUpLocation" +
                     "_searchCriteria")
        CONFIRMATION_CSS = "#ui-id-1"

    class RETURN_CITY:
        INPUT_CSS = ("#_content_alamo_en_US_car_rental_home_jcr" +
                     "_content_reservationStart_dropOffLocation" +
                     "_searchCriteria")
        CONFIRMATION_CSS = "#ui-id-2"

    SAME_LOCATION_CHECKBOX_CSS = (
        "#_content_alamo_en_US_car_rental_home_jcr" +
        "_content_reservationStart_returnToSameLocation")

    PICKUP_DATE_CSS = ("#_content_alamo_en_US_car_rental_home_jcr" +
                       "_content_reservationStart_pickUpDateTime_date")

    DROPOFF_DATE_CSS = ("#_content_alamo_en_US_car_rental_home_jcr" +
                        "_content_reservationStart_dropOffDateTime_date")

    class TIME:
        PICKUP_XPATH = (
            '//*[@id="_content_alamo_en_US_car_rental_home' +
            '_jcr_content_reservationStart_pickUpDateTime_time"]' +
            '/option[@value="%s"]')

        DROPOFF_XPATH = (
            '//*[@id="_content_alamo_en_US_car_rental_home' +
            '_jcr_content_reservationStart_dropOffDateTime_time"]' +
            '/option[@value="%s"]')

    SUBMIT = ("#_content_alamo_en_US_car_rental_home" +
              "_jcr_content_reservationStart_submit")

data = Alamo.get_prices(
    date(2015, 12, 9),
    date(2016, 1, 7),
    time(10, 00),
    'SJC', 'SFO')


# Alamo.get_prices(
#     date(2015, 12, 9),
#     date(2016, 1, 7),
#     time(11, 00),
#     'SJC', 'SJC')
