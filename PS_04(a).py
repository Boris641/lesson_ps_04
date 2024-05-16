
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Настройка драйвера (замените путь на путь к вашему chromedriver)
driver = webdriver.Chrome()


def search_wikipedia(query):
    driver.get("https://www.wikipedia.org/")

    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)


def list_paragraphs():
    paragraphs = driver.find_elements(By.TAG_NAME,"p")
    for i, p in enumerate(paragraphs):
        print(f"Параграф {i + 1}: {p.text[:100]}...")  # Вывод первых 100 символов параграфа
        if i % 5 == 4:  # Выводить по 5 параграфов за раз
            action = input("Введите 'c' для продолжения или 'q' для выхода: ")
            if action == 'q':
                break


def list_internal_links():
    links = driver.find_elements(By.CSS_SELECTOR, "#bodyContent a[href^='/wiki/']")
    for i, link in enumerate(links):
        print(f"{i + 1}. {link.text} - {link.get_attribute('href')}")
        if i % 5 == 4:  # Выводить по 5 ссылок за раз
            action = input("Введите 'c' для продолжения или 'q' для выхода: ")
            if action == 'q':
                break
    return links


def main():
    initial_query = input("Введите ваш запрос: ")
    search_wikipedia(initial_query)

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")

        choice = input("Введите номер действия: ")

        if choice == '1':
            list_paragraphs()
        elif choice == '2':
            links = list_internal_links()
            link_choice = int(input("Введите номер ссылки для перехода: ")) - 1
            if 0 <= link_choice < len(links):
                driver.get(links[link_choice].get_attribute('href'))
            else:
                print("Некорректный выбор.")
        elif choice == '3':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

    driver.quit()


if __name__ == "__main__":
    main()