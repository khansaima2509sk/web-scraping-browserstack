import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from browserstack_config import BROWSERSTACK_URL

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scraping import fetch_articles  
from translation import translate_titles  
from word_analysis import analyze_repeated_words  

os.makedirs("output", exist_ok=True)
os.makedirs("output/screenshots", exist_ok=True)
os.makedirs("output/logs", exist_ok=True)

def run_browserstack_test(browser, os, os_version, device=None, real_mobile=False):
    """Runs a BrowserStack test for scraping, translation, and word analysis."""

    options = Options()

    if device:
        options.set_capability("browserName", "Chrome")
        options.set_capability("bstack:options", {
            "deviceName": device,
            "realMobile": real_mobile,
            "userName": "saimakhan_OKu0xR",
            "accessKey": "ojnKZTzpnTSWPTxpuXwn"
        })
    else:
        options.set_capability("browserName", browser)
        options.set_capability("bstack:options", {
            "os": os,
            "osVersion": os_version,
            "userName": "saimakhan_OKu0xR",
            "accessKey": "ojnKZTzpnTSWPTxpuXwn"
        })

    print(f"Starting BrowserStack test on {browser if browser else device}...")

    driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, options=options)

    try:
        articles = fetch_articles()
        if not articles:
            print("No articles found.")
            return

        titles = [article[0] for article in articles]
        contents = [article[1] for article in articles]

        translated_titles = translate_titles(titles)

        repeated_words = analyze_repeated_words(translated_titles)

        with open("output/spanish_titles_and_content.txt", "w", encoding="utf-8") as f:
            for title, content in zip(titles, contents):
                f.write(f"Title: {title}\nContent: {content}\n\n")

        with open("output/translated_titles.txt", "w", encoding="utf-8") as f:
            for title in translated_titles:
                f.write(title + "\n")

        with open("output/word_analysis.txt", "w", encoding="utf-8") as f:
            for word, count in repeated_words.items():
                f.write(f"{word}: {count}\n")

        driver.get("https://www.google.com")
        time.sleep(3) 
        screenshot_path = f"output/screenshots/{browser if browser else device}.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at {screenshot_path}")

        log_path = f"output/logs/{browser if browser else device}.txt"
        with open(log_path, "w", encoding="utf-8") as log_file:
            log_file.write(f"Test on {browser if browser else device} - {os if os else 'Mobile'}\n\n")
            log_file.write("Spanish Titles:\n" + "\n".join(titles) + "\n\n")
            log_file.write("Translated Titles:\n" + "\n".join(translated_titles) + "\n\n")
            log_file.write("Repeated Words:\n" + "\n".join(f"{word}: {count}" for word, count in repeated_words.items()))
        print(f"Logs saved at {log_path}")

    except Exception as e:
        print(f"Test failed on {browser if browser else device}: {e}")

    finally:
        driver.quit()
        print(f"Test finished on {browser if browser else device}")

    print("Process completed. Check the 'browserstack_tests/output' folder for results.")

if __name__ == "__main__":
    run_browserstack_test("chrome", "Windows", "10")
