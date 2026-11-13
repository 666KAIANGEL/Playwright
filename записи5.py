# ДЕНЬ 5. Работа с событиями (Events) в Playwright
# ФИО: Брылева Анжелика Павловна
# Дата: 2026-11-13
# Время: 15:05
# Описание изменений:
# 1. Добавила сбор URL в список requests_list для сбора статистики.
# 2. Добавила подсчет общего числа запросов.
# 3. Добавила проверки (assert) заголовков для обоих сайтов, превратив скрипт в тест.
# 4. Оставила механизм добавления/удаления слушателя (как в документации).
# Зачем: исходный пример только печатал текст; мой вариант собирает метрики и проверяет сайты.

from playwright.sync_api import sync_playwright

# Список для сбора всех запросов
requests_list = []

def print_request_sent(request):
    requests_list.append(request.url)
    print("Request sent: " + request.url)

def print_request_finished(request):
    print("Request finished: " + request.url)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # 1. Подписываемся на события
    page.on("request", print_request_sent)
    page.on("requestfinished", print_request_finished)

    print("--- Переход на Wikipedia ---")
    page.goto("https://wikipedia.org")
    
    # Проверка заголовка
    assert "Wikipedia" in page.title(), f"Ошибка: не Википедия! Текущий заголовок: {page.title()}"
    
    page.wait_for_timeout(2000) # Ждем завершения запросов
    print(f"\n=== Статистика: Всего отправлено {len(requests_list)} запросов ===")

    # 2. Отписываемся от события requestfinished
    page.remove_listener("requestfinished", print_request_finished)
    print("\n--- Слушатель requestfinished удален ---")

    print("--- Переход на OpenStreetMap ---")
    page.goto("https://www.openstreetmap.org/")
    page.wait_for_timeout(2000)
    
    # Проверка второго заголовка
    assert "OpenStreetMap" in page.title(), f"Ошибка: не OpenStreetMap! Текущий заголовок: {page.title()}"
    print("\n✅ Оба сайта успешно проверены!")

    browser.close()