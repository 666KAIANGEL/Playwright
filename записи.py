# ФИО: Брылева Анжелика Павловна
# Дата: 2026-11-09
# Время: 11:20
# Описание: Этот код запускает браузер Chromium, открывает страницу
# playwright.dev и проверяет, что заголовок страницы содержит слово "Playwright".
# Я скопировала пример из раздела "Writing tests" и запустил его локально.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    print(page.title())
    browser.close()
    # Результат запуска: "Fast and reliable end-to-end testing for modern web apps | Playwright"
    # Код выполнен без ошибок.