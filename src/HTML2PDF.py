from selenium import webdriver
import time
import json
import os
import sys
import shutil
from webdriver_manager.chrome import ChromeDriverManager
import base64

n_print=10
cwd = os.getcwd()

"""
while True:
    if not os.path.exists(SAVE_PATH):
        os.makedirs(SAVE_PATH)
        break
    else:
        SAVE_PATH=SAVE_PATH+'_{}'.format(f)
        f+=1
"""

if len(sys.argv)==1:
    print("USAGE: {} (template_file) (output_path) (num_print)".format(sys.argv[0]))
    exit()
elif len(sys.argv)==2:
    #print("chrome-driver is not found.")
    print("output path is not found.")
    exit()
elif len(sys.argv)>3:
    n_print=sys.argv[3]


SAVE_PATH=sys.argv[2]
if os.path.exists(SAVE_PATH):
    os.rmdir(SAVE_PATH)

os.mkdir(SAVE_PATH)
TEMP_FILE=sys.argv[1]

print(n_print)
print(cwd)
print(SAVE_PATH)
print(TEMP_FILE)

def save_to_pdf(driver, file_path):
    parameters = {
                    "printBackground": True, # 背景画像を印刷
                    "paperWidth": 8.27, # A4用紙の横 210mmをインチで指定
                    "paperHeight": 11.69, # A4用紙の縦 297mmをインチで指定
                    # "displayHeaderFooter": True, # 印刷時のヘッダー、フッターを
                }
                    # Chrome Devtools Protocolコマンドを実行し、取得できるBase64形式のPDFデータをデコードしてファイルに保存
    pdf_base64 = driver.execute_cdp_cmd("Page.printToPDF", parameters)
    pdf = base64.b64decode(pdf_base64["data"])
    with open(file_path, 'bw') as f:
        f.write(pdf)




options = webdriver.ChromeOptions() 
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=options)
for i in range(n_print):
    driver.get("file:///{}".format(os.path.join(cwd,TEMP_FILE)))
    time.sleep(1)
    save_to_pdf(driver,os.path.join(SAVE_PATH, "mondai_{}.pdf".format(i+1)))
    time.sleep(1)
driver.quit()
