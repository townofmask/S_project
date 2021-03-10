import time
from selenium import webdriver

driver = webdriver.Chrome()
# time.sleep(5)

driver.get("https://www.kamogo.com/7")
# time.sleep(5)

textarea = driver.find_element_by_css_selector(".row>.form-control")

def test_text():
    content_text = driver.find_element_by_css_selector("div#content-text>p")
    text = content_text.text
    assert text == "The birthday problem states that given a certain amount of people, there will be a certain chance that two people in the room share a birthday. The mind blowing fact is that a room of 23 people has a 50% chance of having two people in the room share a birthday. I would explain to you how this works, but I have no idea. Let's just call it black magic and leave it at that.", \
        f"Wrong text!"

def test_text2():
    i = 0
    textarea.send_keys(i)
    res = driver.find_element_by_id("result")
    output = res.text
    assert output == "0% chance of a shared birthday", \
        f"Wrong text!"

if __name__ == "__main__":
    test_text()
    test_text2()
    print("All tests passed!")

driver.quit()