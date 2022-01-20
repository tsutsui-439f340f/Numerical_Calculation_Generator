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

print(len(sys.argv))
if len(sys.argv)==1:
    print("USAGE: {} (template_file) (output_path) (num_print)".format(sys.argv[0]))
    exit()
elif len(sys.argv)==2:
    print("output path is not found.")
    exit()
elif len(sys.argv)>3:
    n_print=int(sys.argv[3])


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
                    "printBackground": True,
                    "paperWidth": 8.27,
                    "paperHeight": 11.69, 
                }
                    
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
