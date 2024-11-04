from selenium import webdriver
from tqdm import tqdm

from parser import find_data


def create_browser() -> webdriver:
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    # Строчка сверху влияет на запуск/не запуск браузера
    option.add_argument('--blink-settings=imagesEnabled=false')
    browser = webdriver.Chrome(options=option)
    return browser


def open_page(browser: webdriver, url: str) -> None:
    browser.get(url)


def find_data_from_list(urls: list, browser: webdriver) -> list:
    all_data = []

    for url in tqdm(urls, desc="Parsing urls", colour="GREEN"):
        open_page(browser, url)
        data = find_data(browser)
        all_data.append(data)

    return all_data


def main():
    urls = [
        "https://travel.yandex.ru/hotels/moscow/beta-izmailovo/reviews/"
    ]

    browser = create_browser()
    all_data = find_data_from_list(urls, browser)
    print(all_data)


if __name__ == '__main__':
    main()
