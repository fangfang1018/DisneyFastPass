#!/usr/bin/env python
__author__ = 'ffpku_000'
import schedule
import time
from datetime import datetime, timedelta
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
driver_path = 'C:/Program Files (x86)/Google/Chrome/chromedriver.exe'
n_guest = 1
url = "https://disneyworld.disney.go.com/plan/my-disney-experience/"
account = 'fangf1018@gmail.com'
password = getpass()


def job(n_guest=1):
    driver = webdriver.Chrome(driver_path)
    driver.get(url)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="pageContent"]/div/div[3]/div/a/span').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="loginPageUsername"]').send_keys(account)
    driver.find_element(By.XPATH, '//*[@id="loginPagePassword"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="loginPageSubmitButton"]').click()
    driver.find_element(By.XPATH, '//*[@id="pageContainerInner"]/div[1]/div[2]/div/div[2]/div[6]/a').click()
    time.sleep(10)
    driver.find_element(By.CLASS_NAME, 'pillBase').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="fastPasslandingPage"]/div[3]/div[1]/div/div/div/div').click()
    time.sleep(5)
    for i in range(n_guest):
        driver.find_elements(By.CLASS_NAME, 'checkmarkWrapper')[i+1].click()
    time.sleep(30)
    try:
        driver.find_element(By.CLASS_NAME, 'next').click()
    except:
        driver.find_element(By.CLASS_NAME, 'next').send_keys('\n')
    # select date 11.11
    time.sleep(10)
    driver.find_elements(By.CLASS_NAME, 'day')[20].click()
    time.sleep(10)
    # select Animal Kingdom
    driver.find_elements(By.CLASS_NAME, 'parkImage')[3].click()

    # TO DO: move mouse
    # select ride
    time.sleep(20)
    # TO DO: fix bug "not clickable"
    # Expedition Everest
    driver.find_element(By.XPATH, "//img[contains(@src,'https://secure.parksandresorts.wdpromedia.com/resize/mwImage/1/340/192/75/wdpromedia.disney.go.com/media/wdpro-assets/parks-and-tickets/attractions/animal-kingdom/expedition-everest/expedition-everest-day-00.jpg?17072014122508')]").click()
    # driver.find_element(By.XPATH, '//*[@id="selectExperienceExperiencesList"]/div[2]/div[2]/div[2]/div/div[1]/span[1]/img').click()
    # Avatar Flight of Passage
    # driver.find_element(By.XPATH, "//img[contains(@src,'https://secure.parksandresorts.wdpromedia.com/resize/mwImage/1/340/192/75/wdpromedia.disney.go.com/media/wdpro-assets/parks-and-tickets/attractions/animal-kingdom/flight-of-passage/flight-of-passage-in-ride-16x9.jpg?13102017105857')]").click()
    fp_time = []
    while not fp_time:
        driver.refresh()
        time.sleep(20)
        print 'Check FastPass at: {}'.format(datetime.now())
        fp_time = driver.find_elements(By.CLASS_NAME, 'ampm')
    fp_time[-1].click()
    print 'Found FastPass at: {}'.format(datetime.now())
    time.sleep(10)
    driver.find_element(By.CLASS_NAME, 'confirm').click()
    print 'FastPass booked at: {}'.format(datetime.now())
    driver.close()
    # now = datetime.now()
    # then = now + timedelta(days=7, hours=-7)
    # if then.strftime("%B") != driver.find_element_by_class_name('current-month'):
    #     driver.find_element(By.CLASS_NAME, 'next').click()
    # # driver.find_elements(By.CLASS_NAME, 'day')
    # # driver.find_elements(By.CSS_SELECTOR, ("span[aria-label={}]".format(then.day))).click()
    # driver.find_element(By.XPATH, '//*[@id="selectParkAndDate"]/div[4]/div/div/div[2]/div[2]/span[4]').click()
    # driver.find_element(By.XPATH, '//*[@id="selectParkContainer"]/div[2]/div[4]/div/div[2]').click()

if __name__ == '__main__':
    job()


# schedule.every().day.at("07:00").do(job, 'It is 07:00')
# schedule.every().hour.at("00:00").do(job, 'It is ' + str(datetime.now()))
# while True:
#     schedule.run_pending()
#     time.sleep(60)  # wait one minute
