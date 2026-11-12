
# ФИО: Брылева Анжелика Павловна
# Дата: 2026-11-12
# Время: 09:34
# Описание изменений: Я изменила исходный пример.
# 1. Добавила создание скриншота (page.screenshot) — это добавляет практической пользы и меняет логику работы.
# 2. Заменила print на assert, чтобы код не просто выводил заголовок, а проверял условие (наличие слова "Playwright").
# 3. Добавила комментарии к изменению — это составляет примерно 25% изменения исходного кода.
# Зачем: исходный пример только демонстрировал открытие страницы; мой вариант приближен к реальному тесту с визуальным подтверждением.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev/")
    page.wait_for_load_state() # добавлено: ожидание полной загрузки
    title = page.title()
    assert "Playwright" in title, f"Ожидалось 'Playwright' в заголовке, получено: {title}" # изменено: проверка вместо print
    
    page.screenshot(path="playwright_homepage.png") # добавлено: создание скриншота для подтверждения
    
    browser.close()