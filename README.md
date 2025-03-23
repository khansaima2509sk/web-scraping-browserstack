🌐 Web Scraping & BrowserStack Testing Project

📌 Project Overview

This project automates web scraping, text translation, and analysis using Selenium, BeautifulSoup, and OpenAI translators. It runs locally and on BrowserStack to test across multiple browsers and mobile devices.

⚙️ Setup & Installation

1️⃣ Clone the Repository

git clone <repository-url>
cd your_project_directory

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Set Up BrowserStack Credentials

Create a .env file in the root directory and add:

BROWSERSTACK_USERNAME=saimakhan_OKu0xR
BROWSERSTACK_ACCESS_KEY=ojnKZTzpnTSWPTxpuXwn

Alternatively, update browserstack_config.py:

BROWSERSTACK_USERNAME = "your-username"
BROWSERSTACK_ACCESS_KEY = "your-access-key"
BROWSERSTACK_URL = f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

🚀 Running the Project

🔹 Run Locally

python main.py

Scrapes 5 articles from El País.
Translates titles to English.
Analyzes repeated words.
Saves images and outputs in output/ folder.

🔹 Run on BrowserStack (Single Browser Test)

python browserstack_tests/test_script.py
Runs scraping, translation, and analysis on BrowserStack.
Saves outputs in browserstack_tests/output/.

🔹 Run on BrowserStack (Parallel Browsers & Devices)

python browserstack_tests/parallel_test.py
Runs tests across Chrome, Firefox, Safari, iPhone 13, and Samsung Galaxy S22.


🔍 Viewing BrowserStack Results

1️⃣ Log into BrowserStack: https://automate.browserstack.com
2️⃣ Check the test dashboard for your recent runs.
3️⃣ Refer to browserstack_dashboard.png for a visual representation.