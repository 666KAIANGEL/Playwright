<<<<<<< HEAD
# ФИО: Брылева Анжелика Павловна
# Дата: 10.11.2026
# Время: 12:00
# Описание изменений: Я изменила исходный пример.
# 1. Добавила ожидание загрузки страницы (wait_for_load_state), чтобы тест был стабильнее.
# 2. Заменила print на assert, чтобы код не просто выводил заголовок, а проверял условие.
# 3. Добавила комментарий к изменению — это составляет примерно 25% изменения исходного кода.
# Зачем: исходный пример только демонстрировал открытие страницы; мой вариант приближен к реальному тесту.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    page.wait_for_load_state()  # добавлено: ожидание полной загрузки
    title = page.title()
    assert "Playwright" in title, f"Ожидалось 'Playwright' в заголовке, получено: {title}"  # изменено: проверка вместо print
    browser.close()
=======
# ФИО: Брылева Анжелика Павловна
# Дата: 10.11.2026
# Время: 12:00
# изменения: я взяла официальный пример из документации Playwright (раздел "Первый тест", функция test_get_started_link).
# 1. Добавлен переход по конкретному URL (https://playwright.dev/python/) вместо главной страницы, чтобы тестировать раздел именно для Python.
# 2. Добавлена проверка того, что мы находимся на странице установки, а не просто на странице с заголовком Installation.
# 3. Добавлена проверка, что кнопка "Get started" была видима перед кликом.

import re
from playwright.sync_api import Page, expect

def test_get_started_link(page: Page):
    # ИЗМЕНЕНО: переходим сразу в раздел документации Python
    page.goto("https://playwright.dev/python/")

    # ДОБАВЛЕНО: проверяем, что кнопка "Get started" видима перед кликом
    get_started_button = page.get_by_role("link", name="Get started")
    expect(get_started_button).to_be_visible()

    # Кликаем по ссылке "Get started"
    get_started_button.click()

    # Ожидаем, что на странице будет заголовок с именем Installation
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    
    # ДОБАВЛЕНО: проверяем URL, чтобы убедиться, что перешли в нужный раздел
    # expect(page) - проверка состояния объекта page
    # to_have_url —  метод проверки, который ожидает, что у страницы будет определенный URL
    # re.compile(".*intro") — это регулярное выражение (Regex), которое задает шаблон для проверки
    expect(page).to_have_url(re.compile(".*intro"))
>>>>>>> 466d40d2e6c5d9f8c0b6f11959c6743a5b97a029
