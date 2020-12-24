import datetime
import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from tkinter import messagebox
from datetime import date, timedelta

# chromedriver configuration
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])
option.add_argument("disable-gpu")
driver = webdriver.Chrome(options=option)

# opening and intializating the database  
data = open('data.txt', 'r').readlines()

link = [data[2], data[6], data[10], data[14], data[18], data[22], data[26], data[30]]
materiKuliah = [data[3], data[7], data[11], data[15], data[19], data[23], data[27], data[31]]

lecturer = [
    # i deleted the lecturer list for privacy
]
prodi = [
    # deleted for privacy 
]

pelaksanaan = [1, 1, 1, 1, 1, 1, 1, 1]
mediaA = [3, 6, 4, 6, 6, 5, 3, 3]
mediaB = [5]
hoursE = [3, 3, 3, 3, 3, 3, 3, 3]
minutesE = [4, 4, 4, 4, 4, 4, 4, 4]
hoursV = ['13', '09', '08', '09', '13', '08', '13', '13']
minutesV = ['00', '30', '00', '30', '00', '00', '00', '10']
materiE = [5, 5, 5, 5, 5, 5, 5, 5]


# simplifying path
inputan = "(//input[@class='quantumWizTextinputPaperinputInput exportInput'])"
listan = "(//*[@class='quantumWizMenuPaperselectOptionList'])"
listanChoose = "(//*[@class='quantumWizMenuPaperselectContent exportContent'])"
# listanChoose = "(//*[@class='quantumWizMenuPaperselectOption appsMaterialWizMenuPaperselectOption freebirdThemedSelectOptionDarkerDisabled exportOption'])"
circle = "(//*[@class='appsMaterialWizToggleRadiogroupOffRadio exportOuterCircle'])"
mark = "(//*[@class='quantumWizTogglePapercheckboxInnerBox exportInnerBox'])"
yesterday = date.today() - timedelta(days=1)
# loop?

def element_fill(indeks, inputs):
    element = driver.find_element_by_xpath("%s[%s]" % (inputan, indeks))
    element.send_keys(inputs)

def element_click(element_ID, indeks):
    element = driver.find_element_by_xpath("%s[%s]" % (element_ID, indeks))
    element.click()

# Uses loop to fill multiple similar form in one go.
for i in range(0, 8):
    driver.get(link[i])
    html = driver.find_element_by_tag_name('html')
    time.sleep(1)
    driver.implicitly_wait(10)

    # nama
    element_fill(1, "Ahmad Fauzan Mansur")

    # Nomor Induk Mahasiswa
    element_fill(2, "H071201001")

    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)

    # Kelas (PART OF LOOP)
    element_click(listan, 1)
    time.sleep(1)
    cat = driver.find_element_by_xpath("(//div[@data-value='%s'])[2]" % (prodi[i]))
    cat.click()
    time.sleep(1)

   #dosen (PART OF LOOP )
    element_click(listan, 2)
    time.sleep(1)
    who = driver.find_element_by_xpath("(//div[@data-value='%s'])[2]" % (lecturer[i]))
    who.click()

    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

    # Pelaksanaan (PART OF LOOP)
    element_click(mark, 1)

    # Media Mark
    element_click(mark, mediaA[i])
    if i == 0:
        element_click(mark, mediaB[i])

    #tanggal (PART OF LOOP?)
    if i == 6:
        dateNow = str(yesterday).split('-')
        date = driver.find_element_by_xpath("%s[%s]" % (inputan, 3))
        date.send_keys(dateNow[1], dateNow[2][0:1], dateNow[0])
    else:
    # jam (PART OF LOOP)
        element_fill(hoursE[i], hoursV[i])
        element_fill(minutesE[i], minutesV[i])

    # materi, import from txt files. (PART OF LOOP OFC)
    if i == 6:
        element_fill(4, materiKuliah[i])
    else:
        element_fill(materiE[i], materiKuliah[i])

    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(10)

    # confirmation box
    messagebox.showinfo('Submit before clicking ok!')
    # driver.find_element_by_xpath("(//*[@class='appsMaterialWizButtonPaperbuttonContent exportButtonContent'])[2]").click()
