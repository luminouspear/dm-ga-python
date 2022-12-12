# selenium webdriver reference: https://chromedriver.chromium.org/getting-started
# note to self: must download the appropriate version of chromedriver https://chromedriver.chromium.org/downloads
# + add it to "the path".
import csv
import time
from selenium import webdriver
driver = webdriver.Chrome()

# python csv reader reference: https://docs.python.org/3/library/csv.html
with open('C:\\Users\\Alex\\ga\\demos\\csv_to_download\\TOR_DSI_09_August_2020 Recording Tracker - Sheet1.csv') as csvfile:
    recording_tracker = csv.reader(csvfile)
    count = 1
    for row in recording_tracker:
        # skip october 23 which has no password
        if row[2].startswith('https://') and len(row[3]) > 0:
            print("accessing", row[2], row[3], "...")
            driver.get(row[2])  # go to url link
            time.sleep(1)  # Let the user actually see something!
            pw_input = driver.find_element_by_xpath(
                "//input[@type='password']")
            pw_input.send_keys(row[3])
            pw_input.send_keys(webdriver.common.keys.Keys.ENTER)
            time.sleep(1)
            download_button = driver.find_element_by_xpath(
                "//a[@class='download-btn']")
            download_button.click()
            # wait 180 seconds (3 minutes) before moving on to the next one
            time.sleep(300)
            count += 1
            print("Download count is", count)
