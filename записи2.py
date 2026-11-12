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

