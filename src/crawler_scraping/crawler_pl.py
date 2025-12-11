from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

sys.path.insert(0, "../lib/")

import utils

class Crawler_Portal_Transparencia:
    """
    ### Crawler with driver(Browser) Chrome manipulated for Selenium.

    Class responsible for collecting public data from the municipal government website (PREFEITURA MUNICIPAL DE RESTINGA - Transparência).
    The data collection is performed by a driver that enters the official website,
    locates the "Export XML" button in the HTML (with filters already applied for the selected period), and clicks it.
    The crawler needs to wait 9 seconds for the XML file to be downloaded. 
    Once downloaded, the file is automatically moved to the path (data/scraping/data_raw).

    :param period_from: Start date. (Available years: 2023 - 2024 - 2025 - 2026 - 2027) These options will be available by 2027.
    :type period_from: string

    :param period_to: End date. (Available years: 2023 - 2024 - 2025 - 2026 - 2027) These options will be available by 2027.
    :type period_to: string

    :param search_for: Options: favorecido - empenho - despesa - valor.
    :type search_for: string
    """
    
    def __init__(self, period_from, period_to, search_for):
        self.period_from = period_from
        self.period_to = period_to
        self.search_for = search_for    # Options: favorecido - empenho - despesa - valor
        self.url = f"https://restinga.eddydata.com/gestor-publico/transparencia/pagamento/diaria/restinga/020000/{period_from}/{period_to}/{search_for}="

        self.get_path_to_save()
        self.prefs = {"download.default_directory": f"{self.folder_for_file}", 
                      "safebrowsing.enabled": True}

        self.chrome_options = Options()                  
        self.chrome_options.add_argument('--no-sandbox')                        # Disable Chrome sandbox. 
        self.chrome_options.add_argument('--headless')                          # Run Chrome without opening a visible window.
        self.chrome_options.add_argument('--disable-dev-shm-usage')             # Avoid using /dev/shm (small shared memory). Prevents crashes in Linux/Docker.
        self.chrome_options.add_experimental_option('prefs', self.prefs)        # Apply custom Chrome preferences (dowloads, etc.)

        self.browser =  webdriver.Chrome(options=self.chrome_options)           # Defining settings to the driver.

        
    def execute_crawler(self):                                                  # Function execution.
       self.entering_and_data_collection()
       return self.browser.quit()
       
    def get_path_to_save(self):                                                 # Auxiliary function to get the path to the folder
                                                                                # that will store the raw data.
      self.folder_for_file = utils.get_path_to_file()

    def entering_and_data_collection(self):
      self.browser.get(self.url)                # Entering in the URL with the driver and get method().
      button_install_xml = self.browser.find_element(By.XPATH, '//*[@title="Exportar arquivo xml"]')  # Find the "Export XML" button with the find_element() method.
                                                                                                      # Passing an XPath that points to the Export XML button and find_element() will locate it in the HTML. 
      button_install_xml.click()      # Click on the Export XML button found.
      time.sleep(9)                   # Wait 9 seconds for the XML file to be downloaded.