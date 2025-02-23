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

driver.get(url='https://grp03.id.rakuten.co.jp/rms/nid/login') # URLにアクセス

# 指定したname属性のテキストボックスに文字を入力する
# 要素をIDで取得
user_box = driver.find_element(By.ID, "loginInner_u")

# テキストを入力
input_text = "affilinno@gmail.com"
user_box.send_keys(input_text)

pass_box = driver.find_element(By.ID, "loginInner_p")

# テキストを入力
input_text = "@FF1l1nn0"
pass_box.send_keys(input_text)

submit_button = driver.find_element(By.NAME, "submit")
submit_button.click()
print(driver.title)

driver.quit()
