from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

sys.path.insert(0, "../lib/")

import utils

class Crawler_Portal_Transparencia:
    
    def __init__(self, period_from, period_to, search_for):
        self.period_from = period_from
        self.period_to = period_to
        self.search_for = search_for    # Options: favorecido - empenho - despesa - valor
        self.url = f"https://restinga.eddydata.com/gestor-publico/transparencia/pagamento/diaria/restinga/020000/{period_from}/{period_to}/{search_for}="

        self.get_path_to_save()
        self.prefs = {"download.default_directory": f"{self.folder_for_file}", 
                      "safebrowsing.enabled": True}

        self.chrome_options = Options()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.chrome_options.add_experimental_option('prefs', self.prefs)

        self.browser =  webdriver.Chrome(options=self.chrome_options)

        
    def execute_crawler(self):
       self.entering_and_data_collection()
       return self.browser.quit()
       
    def get_path_to_save(self):
      self.folder_for_file = utils.get_path_to_file()

    def entering_and_data_collection(self):
      self.browser.get(self.url)
      button_install_xml = self.browser.find_element(By.XPATH, '//*[@title="Exportar arquivo xml"]')
      button_install_xml.click()
      time.sleep(8)

# Missing add Logging + Documentation.