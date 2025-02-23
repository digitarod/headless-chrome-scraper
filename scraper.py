from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scrape():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://example.com")  # ここにスクレイピング対象のURLを指定
    
    time.sleep(2)  # ページ読み込み待機
    
    title = driver.find_element(By.TAG_NAME, "h1").text  # h1タグのテキストを取得
    print(f"Page Title: {title}")
    
    driver.quit()

if __name__ == "__main__":
    scrape()
