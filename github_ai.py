from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="./chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1083,590")
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://github.com/")

# Clicking search button
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "/html/body/div[1]/div[1]/header/div/div[2]/div/div/qbsearch-input/div[1]/button",
        )
    )
)
search_button = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div[1]/header/div/div[2]/div/div/qbsearch-input/div[1]/button",
)
search_button.click()

# Searching AI projects
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "query-builder-test"))
)
search_input = driver.find_element(By.ID, "query-builder-test")
search_input.clear()
search_input.send_keys("AI projects" + Keys.ENTER)

# Filtering results by python
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, ":rb:")))
python_filter = driver.find_element(By.ID, ":rb:")
python_filter.click()


# Traversing the pages to get the name, link and stars of resulting projects
num_pages = 5
results = []
for i in range(num_pages):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "Qaxme"))
    )
    projects_elems = driver.find_elements(By.CLASS_NAME, "Qaxme")
    for project_el in projects_elems:
        search_title_el = project_el.find_element(By.CLASS_NAME, "search-title")
        project_name = search_title_el.find_element(By.CLASS_NAME, "search-match").text
        project_link = search_title_el.find_element(By.XPATH, ".//a[1]").get_attribute(
            "href"
        )
        ul_el = project_el.find_element(By.XPATH, ".//ul[1]")
        project_stars = int(
            ul_el.find_element(By.XPATH, ".//li[2]/a[1]")
            .get_attribute("aria-label")
            .split(" ")[0]
        )
        results.append(
            {"name": project_name, "link": project_link, "stars": project_stars}
        )
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@rel='next'][1]"))
    )
    next_page_button = driver.find_element(By.XPATH, "//a[@rel='next'][1]")
    next_page_button.click()

time.sleep(2)
driver.quit()

print(results[0])
print(f"found {len(results)} projects")
