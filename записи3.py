<<<<<<< HEAD
# ФИО: Брылева Анжелика Павловна
# Дата: 10.11.2026
# Время: 17:35
# Описание: На основе официальной документации Playwright (раздел "Использование фикстур") 
# Что изменено
# 1. Я добавила в фикстуру вывод текущего URL в консоль (print) чтобы лучше понимать процесс.
# 2. Я добавила переход на рускоязычную версию сайта.
# Зачем: Это делает тест более информативным при отладке и более устойчивым к небольшим изменениям на сайте.

import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("Начало выполнения теста")
    
    # ИЗМЕНЕНО: переходим на русскоязычную версию сайта для удобност
    page.goto("https://playwright.dev/python/")
    
    # ДОБАВЛЕНО: выводим в консоль, на какую страницу мы попали
    print(f"Открыт URL: {page.url}")
    
    yield
    
    # ДОБАВЛЕНО: проверяем, что после теста мы всё ещё на сайте
    print(f"Тест завершен. Текущий URL: {page.url}")
    print("Конец выполнения теста")


def test_main_navigation(page: Page):
    # Утверждения используют API expect.
    expect(page).to_have_url("https://playwright.dev/")
    
    # ДОБАВЛЕНО: проверяем, что в заголовке страницы есть слово "Playwright"
    expect(page).to_have_title(re.compile("Playwright"))
=======
# ФИО: Брылева Анжелика Павловна
# Дата: 10.11.2026
# Время: 17:35
# Описание: На основе официальной документации Playwright (раздел "Использование фикстур") 
# Что изменено
# 1. Я добавила в фикстуру вывод текущего URL в консоль (print) чтобы лучше понимать процесс.
# 2. Я добавила переход на рускоязычную версию сайта.
# Зачем: Это делает тест более информативным при отладке и более устойчивым к небольшим изменениям на сайте.

import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("Начало выполнения теста")
    
    # ИЗМЕНЕНО: переходим на русскоязычную версию сайта для удобност
    page.goto("https://playwright.dev/python/")
    
    # ДОБАВЛЕНО: выводим в консоль, на какую страницу мы попали
    print(f"Открыт URL: {page.url}")
    
    yield
    
    # ДОБАВЛЕНО: проверяем, что после теста мы всё ещё на сайте
    print(f"Тест завершен. Текущий URL: {page.url}")
    print("Конец выполнения теста")


def test_main_navigation(page: Page):
    # Утверждения используют API expect.
    expect(page).to_have_url("https://playwright.dev/")
    
    # ДОБАВЛЕНО: проверяем, что в заголовке страницы есть слово "Playwright"
    expect(page).to_have_title(re.compile("Playwright"))
>>>>>>> 466d40d2e6c5d9f8c0b6f11959c6743a5b97a029
