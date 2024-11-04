from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from tqdm import tqdm


def press_button(browser: webdriver) -> None:
    xpath_button = "/html/body/div[1]/div/div[5]/div/div/div/div[2]/div[3]/div[1]/div/div[2]/div[7]/button"
    browser.find_element(By.XPATH, xpath_button).click()


def find_data(browser: webdriver) -> list:
    xpath_block_reviews = "/html/body/div[1]/div/div[5]/div/div/div/div[2]/div[3]/div[1]/div/div[2]/div[6]"
    css_selector_reviews = "section.root.esfDh.xa7LR"

    class_block_text = "RYSdb"
    class_text = "lpglK._1m7jk.TQ2-5.b9-76"

    css_selector_block_user = "section.l3aLW.ouyGq.root_desktop"
    class_user_data = "Qmk1o"
    class_rate = "Ia-4D.qiRU-.OtYYq.tzdr8"
    class_successful_star = "LFBXk.KN22d"

    for _ in tqdm(range(39), desc="Pressing buttons", colour="GREEN"):
        press_button(browser)
        sleep(1)

    block_reviews = browser.find_element(By.XPATH, xpath_block_reviews)
    reviews = block_reviews.find_elements(By.CSS_SELECTOR, css_selector_reviews)

    reviews_data = []
    
    for review in tqdm(reviews, desc="Parsing reviews", colour="GREEN"):
        block_text = review.find_element(By.CLASS_NAME, class_block_text)
        text = block_text.find_element(By.CLASS_NAME, class_text)
        formatted_text = text.text.split("\n")

        block_user = review.find_element(By.CSS_SELECTOR, css_selector_block_user)
        user_data = block_user.find_element(By.CLASS_NAME, class_user_data)
        rate = user_data.find_element(By.CLASS_NAME, class_rate)
        successful_star = rate.find_elements(By.CLASS_NAME, class_successful_star)
        count_start = len(successful_star)

        reviews_data.append((formatted_text[0], count_start))

    return reviews_data
