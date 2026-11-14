# =========================================================
# ДЕНЬ 6. Работа с диалоговыми окнами (Dialogs) в Playwright
# ФИО: Брылева Анжелика Павловна
# Дата: 2026-11-14
# Время: 20:00
# =========================================================
# Описание изменений (модификация ~25%):
# 1. Взяла базовый пример из документации Playwright (раздел Dialogs).
# 2. Добавила сохранение текста диалога в переменную и проверку (assert).
# 3. Вместо простого закрытия (dismiss) добавила подтверждение (accept).
# 4. Добавила второй тип диалога (prompt) с вводом текста.
# Зачем: исходный пример просто печатал сообщение; мой вариант проверяет его содержимое.

from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # --- Модификация: обработчик диалогов (alert) ---
    dialog_messages = []
    
    def handle_dialog(dialog):
        print(f"Тип диалога: {dialog.type}")
        print(f"Сообщение: {dialog.message}")
        dialog_messages.append(dialog.message)
        dialog.accept() # Нажимаем "ОК" (accept)

    # Регистрируем обработчик
    page.on("dialog", handle_dialog)

    # Открываем пустую страницу
    page.goto("about:blank")
    
    # Вызываем alert через JavaScript (самый надежный способ)
    page.evaluate("alert('Привет, Playwright!')")
    
    # --- Модификация: проверка (assert) ---
    assert len(dialog_messages) == 1, "Диалог не был перехвачен!"
    assert "Playwright" in dialog_messages[0], "В сообщении нет слова Playwright!"
    print("✅ Проверка alert пройдена!")

    # --- Модификация: второй тип диалога (prompt) ---
    def handle_prompt(dialog):
        print(f"Тип диалога: {dialog.type}")
        dialog.accept("Анжелика") # Вводим текст и нажимаем ОК
        print("✅ В prompt введено имя 'Анжелика'")

    # Убираем старый обработчик и ставим новый для prompt
    page.remove_listener("dialog", handle_dialog)
    page.on("dialog", handle_prompt)
    
    # Вызываем prompt через JavaScript
    page.evaluate("prompt('Введите имя:')")
    
    print("✅ Все проверки диалогов пройдены успешно!")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)