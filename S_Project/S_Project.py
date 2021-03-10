import time
import openpyxl
from selenium import webdriver

driver = webdriver.Chrome()
output = []
# time.sleep(5)

driver.get("https://www.kamogo.com/7")
# time.sleep(5)

textarea = driver.find_element_by_css_selector(".row>.form-control")
content_text = driver.find_element_by_css_selector("div#content-text>p")
text = content_text.text

book = openpyxl.Workbook()
sheet = book.active
sheet["A1"] = text 

i = 0
textarea.send_keys(i)
res = driver.find_element_by_id("result")
output = res.text
sheet["A2"] = str(i)
sheet["B2"] = ">>>"
sheet["C2"] = output
driver.find_element_by_css_selector(".row>.form-control").clear()

for i in range(101):
    textarea.send_keys(i)
    res = driver.find_element_by_id("result")
    output = res.text
    # print(str(i) + ">>>"+ output + "\n")
    # time.sleep(1)
    driver.find_element_by_css_selector(".row>.form-control").clear()

book.save("parse.xlsx")
book.close()

driver.quit()
