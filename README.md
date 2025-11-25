# Sprint 6 — UI автотесты на Python (Selenium + Pytest)

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![pytest](https://img.shields.io/badge/pytest-tests-green)
![Selenium](https://img.shields.io/badge/selenium-WebDriver-brightgreen)

Учебный проект по автоматизации UI-тестирования сервиса заказа самокатов.  
Тесты написаны на Python с использованием Selenium WebDriver и Pytest, структура приближена к реальному фреймворку: Page Object, фикстуры, конфиг.

---

## Стек

- Python 3.x  
- Selenium WebDriver  
- Pytest  
- Webdriver-manager  

---

## Структура проекта

```text
Sprint_6_Python/
│
├── pages/                     # Page Object-файлы
│   ├── base_page.py
│   ├── main_page.py
│   └── order_page.py
│
├── resources/                 # Тестовые данные и локаторы
│   ├── descriptions.py
│   ├── locators_main_page.py
│   ├── locators_order_page.py
│   └── urls.py
│
├── tests/                     # UI-тесты (pytest)
│   ├── test_main_page.py
│   └── test_order_page.py
│
├── requirements.txt           # Зависимости
├── pytest.ini                 # Конфигурация pytest
├── .gitignore                 # Игнор артефактов и окружения
└── README.md
   ``` 

Как запустить
1. Установить зависимости
    ```bash
    pip install -r requirements.txt
    ```

2. Запустить все тесты
    ```bash
    pytest
    ```