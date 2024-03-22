# import tabula 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
from time import sleep
# file = "/Users/benjaminklick/Documents/Python Projects/dob-report-2022.pdf"


# companies = pd.DataFrame(columns=["Name", "Ticker"])

# names = pd.Series([], dtype=object)

# tables = tabula.read_pdf(file, pages="4-18")
# for table in tables:
#     names = pd.concat([names, table.iloc[:, 0]], ignore_index=True)

# file = "/Users/benjaminklick/Documents/Python Projects/HooverExits.pdf"

# tables = tabula.read_pdf(file, pages="33-39")
# for table in tables:
#     names = pd.concat([names, table.iloc[:, 0]], ignore_index=True)

# companies.Name = names

# companies.to_csv("/Users/benjaminklick/Documents/Python Projects/CaliforniaFirms.csv")

file = "/Users/benjaminklick/Documents/Python Projects/CALIFORNIACO.csv"

df = pd.read_csv(file)
ops = Options()
# ops.headless = True
ops.binary_location = "/Applications/Firefox Developer Edition.app/Contents/MacOS/firefox"
serv = Service("/usr/local/bin/geckodriver")
driver = webdriver.Firefox(service=serv, options=ops)
driver.get("https://finance.yahoo.com")

search = driver.find_element(By.CSS_SELECTOR, "#yfin-usr-qry")
for i in range(len(df.Name)):
    search.send_keys(df.Ticker[i])
    input()
    search.clear()

# ops = Options()
# # ops.headless = True
# ops.binary_location = "/Applications/Firefox Developer Edition.app/Contents/MacOS/firefox"
# serv = Service("/usr/local/bin/geckodriver")
# driver = webdriver.Firefox(service=serv, options=ops)

# driver.get("https://finance.yahoo.com")
# search = driver.find_element(By.CSS_SELECTOR, "#yfin-usr-qry")
# for i in range(716, len(df.Name)):
#     search.send_keys(df.Name[i])
#     if i == 716:
#         try:
#             exit = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".close")))
#             exit.click()
#         except:
#             pass
#     search.click()
#     sleep(0.5)
#     try:
#         ticker = driver.find_element(By.CSS_SELECTOR, "li.modules_quoteItem__Ri1wp:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
#         x = re.findall("([A-Z]+).*", ticker.text)[0]
#         if x != "AAPL":
#             print(x)
#             df.Ticker[i] = x
#         else:
#             print("https://www.google.com/search?q=" + df.Name[i] + " ticker barchart")
#             print(df.Name[i])
#             df.Ticker[i] = input()
#     except:
#         print("https://www.google.com/search?q=" + df.Name[i] + " ticker barchart")
#         print(df.Name[i])
#         df.Ticker[i] = input()
#     search.clear()
# driver.quit()

# df.to_csv("/Users/benjaminklick/Documents/Python Projects/CaliforniaFirms2.csv"
# )


