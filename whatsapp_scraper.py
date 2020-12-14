import argparse
import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


def get_contacts():
    # Return list of numbers
    return ["91XXXXXXXXXX", "91XXXXXXXXXX"]


if __name__ == "__main__":
    print("Starting program")

    parser = argparse.ArgumentParser()
    parser.add_argument("--chrome_driver", required=True,
                        help="Specify the chrome driver path")
    parser.add_argument("--message", required=True,
                        help="Specify the message you want to send to your contacts")
    parser.add_argument("--file_type", required=True,
                        help="Specify the file type [image/document]")
    parser.add_argument("--file_path", required=True,
                        help="Specify the file path of the [image/document]")

    args = parser.parse_args()
    chrome_driver = args.chrome_driver
    file_type = args.file_type
    media_file_path = os.path.abspath(args.file_path)
    message = args.message

    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=./newprofile1")
    driver = webdriver.Chrome(chrome_driver, options=options)
    wait = WebDriverWait(driver, 10)
    # driver.get("https://web.whatsapp.com/")

    time.sleep(2)

    contacts = get_contacts()
    for contact in contacts:
        try:
            driver.get('https://web.whatsapp.com/send?phone={phone}'.format(phone=contact))
            driver.implicitly_wait(20)
            driver.find_element_by_xpath(
                '//div[@class="_1awRl copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]').send_keys(
                message + Keys.ENTER)
            driver.implicitly_wait(20)
            # driver.switch_to.alert.accept()

            time.sleep(3)
            attachment = driver.find_element_by_xpath('//div[@title="Attach"]')
            attachment.click()
            if file_type == "image":
                attachment = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                attachment.send_keys(media_file_path)
            elif file_type == "document":
                attachment = driver.find_element_by_xpath(
                    '//input[@accept="*"][@type="file"]')
                attachment.send_keys(media_file_path)

            time.sleep(3)

            send = driver.find_element_by_xpath('//span[@data-icon="send"]')
            send.click()
            # Need to wait until message is sent
            time.sleep(5)

            print("Message sent to", contact)
        except NoSuchElementException:
            print("Failed to send message. Please check if the contact has whatsapp id ")
            continue

    driver.quit()
