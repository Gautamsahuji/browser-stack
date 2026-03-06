import threading
import time
import requests
import re
from collections import Counter

from selenium import webdriver
from selenium.webdriver.common.by import By
from googletrans import Translator


# BrowserStack credentials
USERNAME = "gautamsahu_g5f8K4"
ACCESS_KEY = "SVpC6RFz795VU43heE6W"


# Browsers for parallel execution
browsers = [
    {"browserName": "Chrome", "browserVersion": "latest", "os": "Windows", "osVersion": "10"},
    {"browserName": "Edge", "browserVersion": "latest", "os": "Windows", "osVersion": "11"},
    {"browserName": "Safari", "browserVersion": "latest", "os": "OS X", "osVersion": "Monterey"},
    {"deviceName": "iPhone 13", "osVersion": "15"},
    {"deviceName": "Samsung Galaxy S22", "osVersion": "12"}
]

translator = Translator()


def run_test(cap):

    browser = cap.get("browserName", cap.get("deviceName"))

    print("\n=====================================")
    print("Running Test On:", browser)
    print("=====================================")

    options = webdriver.ChromeOptions()

    bstack_options = {
        "sessionName": f"Assignment - {browser}"
    }

    # Desktop configuration
    if "browserName" in cap:
        options.set_capability("browserName", cap["browserName"])
        options.set_capability("browserVersion", cap["browserVersion"])
        bstack_options["os"] = cap["os"]
        bstack_options["osVersion"] = cap["osVersion"]

    # Mobile configuration
    if "deviceName" in cap:
        bstack_options["deviceName"] = cap["deviceName"]
        bstack_options["osVersion"] = cap["osVersion"]
        bstack_options["realMobile"] = True

    options.set_capability("bstack:options", bstack_options)

    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    driver.get("https://elpais.com/opinion/")
    time.sleep(5)

    article_elements = driver.find_elements(By.CSS_SELECTOR, "article h2 a")

    links = []
    for article in article_elements[:5]:
        links.append(article.get_attribute("href"))

    translated_titles = []

    for i, link in enumerate(links):

        driver.get(link)
        time.sleep(3)

        try:

            title = driver.find_element(By.TAG_NAME, "h1").text
            print(f"\n[{browser}] Article {i+1} Title (Spanish): {title}")

            paragraphs = driver.find_elements(By.CSS_SELECTOR, "article p")
            content = " ".join([p.text for p in paragraphs if p.text])

            print(f"[{browser}] Content:", content[:200])

            # Download image
            try:
                img = driver.find_element(By.CSS_SELECTOR, "figure img").get_attribute("src")
                img_data = requests.get(img).content

                with open(f"{browser}_image_{i+1}.jpg", "wb") as f:
                    f.write(img_data)

                print(f"[{browser}] Image downloaded")

            except:
                print(f"[{browser}] No image found")

            # Translation
            try:
                translated = translator.translate(title, dest="en")
                translated_text = translated.text
            except:
                translated_text = title

            print(f"[{browser}] Translated Title:", translated_text)

            translated_titles.append(translated_text)

        except Exception as e:
            print(f"[{browser}] Error:", e)

    driver.quit()

    # Word analysis
    all_words = " ".join(translated_titles).lower()

    words = re.findall(r'\b\w+\b', all_words)

    word_count = Counter(words)

    print(f"\n[{browser}] Repeated Words More Than 2 Times:")

    for word, count in word_count.items():
        if count > 2:
            print(word, count)


# Parallel execution
threads = []

for cap in browsers:
    t = threading.Thread(target=run_test, args=(cap,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()