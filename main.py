from flask import Flask, jsonify , render_template
import os
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

app = Flask(__name__, template_folder='Template')


@app.route('/')
def index():
    return render_template('index.html')
    
@app.get("/homepage")
async def demo_get():
    driver=createDriver()
    getGoogleHomepage(driver)

def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.headless = True
    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return myDriver
    
def getGoogleHomepage(driver: webdriver.Chrome):
    driver.get("https://www.24h.com.vn")

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
