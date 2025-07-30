from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from Pages.search_page import SearchPage

def test_search_erke_fleece_jacket():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    chrome_options.page_load_strategy = 'eager'

    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # You can optionally navigate here or have search_page.open() handle it
        # driver.get("https://www.daraz.com.np/")

        search_page = SearchPage(driver)
        search_page.open()  # This method should navigate to base URL internally if needed
        search_page.search_for_item("Erke fleece jacket")

        product_titles = search_page.get_product_titles()
        print("Found products:", product_titles)

    finally:
        driver.quit()

if __name__ == '__main__':
    test_search_erke_fleece_jacket()
