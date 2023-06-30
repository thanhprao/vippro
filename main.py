from selenium import webdriver
from flask import Flask, jsonify, render_template, request
import os
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

app = Flask(__name__, template_folder='Template')


@app.route('/')
def index():
    chrome_option = webdriver.ChromeOptions()
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s,options=chrome_option)
    driver.maximize_window()
    driver.get("https://google.com") 
    #return render_template('index.html')
  
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
