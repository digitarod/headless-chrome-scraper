from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")  # ヘッドレスモード
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# `Service` を使用し、`webdriver-manager` で適切な chromedriver を取得
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")
print(driver.title)

driver.quit()
