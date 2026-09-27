#Тестовый сценарий: поиск билетов на сайте РЖД, направление Ростов-на-Дону – Санкт-Петербург

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

import time


def rzd_tickets():
    driver = webdriver.Chrome()

    try:
        #Открываем сайт РЖД
        driver.get("https://ticket.rzd.ru/main")

        #Ожидаем загрузку и видимость
        wait = WebDriverWait(driver, 10)
        action = ActionChains(driver)

        #Ищем поле "Откуда"
        from_field = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[data-testid="route-search-from-node-field"] input[role="combobox"]')
            )
        )

        #Вводим город отправления
        action.click(from_field).send_keys("Ростов-на-Дону").perform()
        time.sleep(2)

        #Ищем поле "Куда"
        to_field = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[data-testid="route-search-to-node-field"] input[role="combobox"]')
            )
        )

        #Вводим город прибытия
        action.click(to_field).send_keys("Санкт-Петербург").perform()
        time.sleep(2)

        #Ищем поле "Дата отправления"
        from_date_field = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[data-testid="route-search-from-date-field"]')
            )
        )

        #Нажимаем на поле даты
        action.click(from_date_field).perform()

        #Ищем дату отправления в календаре
        FOUND_FROM_DATE = False
        for i in range(12):
            try:
                from_date_calendar = wait.until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, '[data-testid="ui-kit-day_31.12.2026"]')
                    )
                )
                action.click(from_date_calendar).perform()
                FOUND_FROM_DATE = True
                break

            except TimeoutException:
                #Если дата не найдена – листаем календарь вперёд
                from_datepicker = wait.until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, '[data-testid="datepicker__navigation__go-forward"]')
                    )
                )
                action.click(from_datepicker).perform()

        if not FOUND_FROM_DATE:
            print('Дата отправления не найдена')

        #Ищем поле "Дата обратного рейса"
        back_date_field = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '[data-testid="route-search-back-date-field"]')
            )
        )

        #Нажимаем на поле даты
        action.click(back_date_field).perform()

        #Ищем дату обратного рейса в календаре
        FOUND_BACK_DATE = False
        for i in range(12):
            try:
                back_date_calendar = wait.until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, '[data-testid="ui-kit-day_08.01.2027"]')
                    )
                )
                action.click(back_date_calendar).perform()
                FOUND_BACK_DATE = True
                break

            except TimeoutException:
                #Если дата не найдена – листаем календарь вперёд
                back_datepicker = wait.until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, '[data-testid="datepicker__navigation__go-forward"]')
                    )
                )
                action.click(back_datepicker).perform()

        if not FOUND_BACK_DATE:
            print('Дата обратного рейса не найдена')

        #Пауза для просмотра результата
        time.sleep(4)

    finally:
        driver.quit()


if __name__ == "__main__":
    rzd_tickets()
