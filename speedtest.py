from selenium import webdriver
import time, xlwt

dl_speed = list()
ul_speed = list()

#Take user input for iteration count
iteration = input("How many times to iterate speedtest page?")
iteration = int(iteration)

#Open Chrome, go to speedtest.net, and click 'begin test'
browser = webdriver.Chrome("C:\Users\mrobert\Documents\chromedriver.exe")
browser.get("http://beta.speedtest.net")
time.sleep(5)

#Complete 'iteration' number of iterations
while iteration > 0:
    iteration -= 1
    link = browser.find_element_by_class_name("start-text")
    link.click()
    time.sleep(60)
    for elem in browser.find_elements_by_xpath('.//span[@class = "result-data-large number result-data-value download-speed"]'):
        dl_speed.append(elem.text)
    for elem in browser.find_elements_by_xpath('.//span[@class = "result-data-large number result-data-value upload-speed"]'):
        ul_speed.append(elem.text)

#Open a spreadsheet
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Speedtest", cell_overwrite_ok=True)

#Put Titles
sheet.write(0,0,"Download")
sheet.write(1,0,"Upload")

#Insert dl and ul speeds
x = 1
for speed in dl_speed:
    sheet.write(0,x,speed)
    x += 1
x = 1
for speed in ul_speed:
    sheet.write(1,x,speed)
    x += 1


workbook.save("Speedest.xls")

#self explainatory
print "End of script."
