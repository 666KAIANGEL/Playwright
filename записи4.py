import pytest
import unittest
from playwright.sync_api import Page

# ==============================================================================
# ДЕНЬ 3. Тестирование с использованием unittest.TestCase
# ФИО: Брылева Анжелика Павловна
# Дата: 11.11
# Время: 12:52
# ==============================================================================

class MyTest(unittest.TestCase):
    
    # ИСПРАВЛЕНО: Используем метод setup_method (или setUp) для unittest.
    # Он автоматически принимает фикстуру page от Playwright перед каждым тестом.
    @pytest.fixture(autouse=True)
    def setup_method(self, page: Page):
        self.page = page

    def test_microsoft_title(self):
        """
        Тест проверяет открытие сайта Microsoft.
        
        # Изменено (по сравнению с исходным примером из документации):
        # 1. В метод goto добавлен параметр wait_until="domcontentloaded", чтобы тест не падал из-за долгой загрузки картинок, а ждал только основную структуру страницы.
        # 2. Удален клик по несуществующему элементу #foobar (self.page.locator("#foobar").click()), так как на реальном сайте Microsoft его нет, и тест бы упал с ошибкой TimeoutError.
        # 3. Вместо клика по кнопке добавлено получение заголовка страницы (page.title()) и проверка через assertIn, что в нем есть слово "Microsoft". Это приближает тест к реальной проверке работоспособности сайта.
        """
        
        # Переход на сайт с ожиданием загрузки DOM (Модификация 1)
        self.page.goto("https://microsoft.com", wait_until="domcontentloaded")
        
        # Получаем заголовок страницы (Модификация 2 и 3)
        page_title = self.page.title()
        
        # Проверяем, что мы действительно на сайте Microsoft
        self.assertIn("Microsoft", page_title, "Заголовок страницы не содержит слово Microsoft")
        
        # Оставляем проверку математики из исходного примера для демонстрации работы evaluate()
        assert self.page.evaluate("1 + 1") == 2

if __name__ == '__main__':
    unittest.main()