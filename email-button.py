from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_website():
    driver = webdriver.Chrome()

    try:
        # Открываем сайт
        driver.get("https://app.jogging.ai4sport.ru/")

        #Ожидаем загрузку и видимость
        wait = WebDriverWait(driver, 10)

        #Ищем поле ввода
        email_field = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input[type="email"]')
            )
        )

        #Вводим почту
        email_field.clear()
        email_field.send_keys("tkachev.tech@yandex.ru")

        #После того как ввели почту, ищем кнопку
        submit_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.btn-primary")
            )
        )

        #Нажимаем на кнопку
        submit_button.click()

        #Ожидаем результата нажатия кнопки
        wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        print("Сценарий выполнен успешно. Тест пройден.")

    finally:
        driver.quit()


if __name__ == "__main__":
    open_website()