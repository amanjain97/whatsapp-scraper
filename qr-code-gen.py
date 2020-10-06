from selenium import webdriver
import time
import shutil
from selenium.webdriver.common.keys import Keys
import os

DOWNLOADS_LOCATION = "/Users/aman.jain/Downloads"
DESTINATION_FOLDER = "qr-images"
CHROME_DRIVER_LOCATION = '/Users/aman.jain/Downloads/chromedriver'


def rename_file(name):
    print(name)
    filename = max([DOWNLOADS_LOCATION + "/" + f for f in os.listdir(DOWNLOADS_LOCATION)], key=os.path.getctime)
    print(filename)
    # print(os.path.getctime(filename))
    new_file_name = f'{name}.png'
    shutil.move(os.path.join(DOWNLOADS_LOCATION, filename), os.path.join(DESTINATION_FOLDER, new_file_name))


if __name__ == "__main__":
    driver = webdriver.Chrome(CHROME_DRIVER_LOCATION)

    # step 1
    driver.get('https://www.qrcode-monkey.com/#text')
    time.sleep(2)

    ids = [
        "1234344233", "1234344234", "1234344235", "1234344236", "1234344237", "1234344238", "1234344239", "1234344240",
        "1234344241", "1234344242", "1234344243", "1234344244", "1234344245", "1234344246", "1234344247", "1234344248",
        "1234344249", "1234344250", "1234344251", "1234344252", "1234344253", "1234344254", "1234344255", "1234344256",
        "1234344257", "1234344258", "1234344259", "1234344260", "1234344261", "1234344262", "1234344263", "1234344264",
        "1234344265", "1234344266", "1234344267", "1234344268", "1234344269", "1234344270", "1234344271", "1234344272",
        "1234344273", "1234344274", "1234344275", "1234344276", "1234344277", "1234344278", "1234344279", "1234344280",
        "1234344281", "1234344282", "1234344283", "1234344284", "1234344285", "2234344254", "2234344255", "2234344256",
        "2234344257", "2234344258", "2234344259", "2234344260", "2234344261", "2234344262", "2234344263", "2234344264",
        "2234344265", "2234344266", "2234344267", "2234344268", "2234344269", "2234344270", "2234344271", "2234344272",
        "2234344273", "2234344274", "2234344275", "2234344276", "2234344277", "2234344278", "2234344279", "2234344280",
        "2234344281", "2234344282", "2234344283", "2234344284", "2234344285", "2234344286", "2234344287", "2234344288",
        "2234344289", "2234344290", "2234344291", "2234344292", "2234344293", "2234344294", "2234344295", "2234344296",
        "2234344297", "2234344298", "2234344299", "2234344300", "2234344301", "2234344302", "2234344303", "2234344304",
        "2234344305", "2234344306", "2234344307", "2234344308", "2234344309", "2234344310"]
    # ids = ["hello"]

    for text in ids:
        content_selector = driver.find_element_by_xpath(
            '//div[@ng-class="{\'active\':editView===\'content\'}"]').click()

        # step 2 type text
        text_box = driver.find_element_by_id("qrcodeText")
        time.sleep(0.5)
        for i in range(11):
            text_box.send_keys(Keys.BACKSPACE)
        text_box.send_keys(text)

        # step 3
        driver.find_element_by_xpath('//div[@ng-class="{\'active\':editView===\'colors\'}"]').click()
        # time.sleep(1)

        # step 4 choose color
        color_box = driver.find_element_by_xpath(
            '//div[@class="color-picker-input-wrapper input-group"]/input[@type="text"]')
        for i in range(10):
            color_box.send_keys(Keys.BACKSPACE)
            time.sleep(0.1)
        time.sleep(0.5)
        color_box.send_keys("#4F4F50")
        time.sleep(1)

        # step 5 choose style
        driver.find_element_by_xpath('//div[@ng-class="{\'active\':editView===\'shape\'}"]').click()
        time.sleep(1)

        # step 6 choose body shape
        driver.find_element_by_xpath('//i[@class="sprite sprite-body sprite-circular"]').click()

        # step 7
        driver.find_element_by_xpath('//i[@class="sprite sprite-frame1"]').click()

        # step 8

        driver.find_element_by_xpath('//i[@class="sprite sprite-ball14"]').click()

        # step 9 generate qr code
        driver.find_element_by_xpath('//button[@ng-click="qrcodeGenerator()"]').click()
        time.sleep(2)

        # step 10 download
        driver.find_element_by_xpath('//button[@ng-click="download(\'png\')"]').click()
        time.sleep(3.5)

        # change the file name and move to desired location
        rename_file(text)
        time.sleep(5)

    driver.quit()
