import sys  # Импортируем модуль sys для работы с системными параметрами
import os   # Импортируем модуль os для работы с файловой системой

# Добавляем родительскую директорию в sys.path
# Это позволяет импортировать модули из родительской директории
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Импортируем классы из основного файла main.py
from main import Mouse, Keyboard, Monitor, EquipmentContainer
import unittest  # Импортируем модуль unittest для написания тестов

# Класс для тестирования функциональности мыши
class TestMouse(unittest.TestCase):

    def setUp(self):
        """Создаем экземпляр мыши для тестирования"""
        # Инициализируем объект Mouse с заданными параметрами
        self.mouse = Mouse("Logitech", 1500, "2023-01-01", "Wireless", 3)

    def test_get_info(self):
        """Тестируем метод get_info для мыши"""
        # Ожидаемая строка, которую должен вернуть метод get_info
        expected_info = ("Мышь: Logitech, Тип: Wireless, "
                         "Кнопки: 3, Цена: 1500, "
                         "Дата последнего редактирования: 2023-01-01")
        # Проверяем, что метод get_info возвращает ожидаемую строку
        self.assertEqual(self.mouse.get_info(), expected_info)

# Класс для тестирования функциональности клавиатуры
class TestKeyboard(unittest.TestCase):

    def setUp(self):
        """Создаем экземпляр клавиатуры для тестирования"""
        # Инициализируем объект Keyboard с заданными параметрами
        self.keyboard = Keyboard("Razer", 3000, "2023-01-01", "Mechanical", "USB")

    def test_get_info(self):
        """Тестируем метод get_info для клавиатуры"""
        # Ожидаемая строка, которую должен вернуть метод get_info
        expected_info = ("Клавиатура: Razer, Тип: Mechanical, "
                         "Разъем: USB, Цена: 3000, "
                         "Дата последнего редактирования: 2023-01-01")
        # Проверяем, что метод get_info возвращает ожидаемую строку
        self.assertEqual(self.keyboard.get_info(), expected_info)

# Класс для тестирования функциональности монитора
class TestMonitor(unittest.TestCase):

    def setUp(self):
        """Создаем экземпляр монитора для тестирования"""
        # Инициализируем объект Monitor с заданными параметрами
        self.monitor = Monitor("Dell", 10000, "2023-01-01", 1920, 1080)

    def test_get_info(self):
        """Тестируем метод get_info для монитора"""
        # Ожидаемая строка, которую должен вернуть метод get_info
        expected_info = ("Монитор: Dell, Ширина: 1920, "
                         "Высота: 1080, Цена: 10000, "
                         "Дата последнего редактирования: 2023-01-01")
        # Проверяем, что метод get_info возвращает ожидаемую строку
        self.assertEqual(self.monitor.get_info(), expected_info)

# Класс для тестирования функциональности контейнера оргтехники
class TestEquipmentContainer(unittest.TestCase):

    def setUp(self):
        """Создаем экземпляр контейнера для тестирования и добавляем оргтехнику"""
        # Инициализируем объект EquipmentContainer
        self.container = EquipmentContainer()
        # Создаем экземпляры оргтехники
        self.mouse = Mouse("Logitech", 1500, "2023-01-01", "Wireless", 3)
        self.keyboard = Keyboard("Razer", 3000, "2023-01-01", "Mechanical", "USB")
        # Добавляем оргтехнику в контейнер
        self.container.add_equipment(self.mouse)
        self.container.add_equipment(self.keyboard)

    def test_add_equipment(self):
        """Тестируем добавление оргтехники в контейнер"""
        # Проверяем, что в контейнере теперь два элемента
        self.assertEqual(len(self.container.equipments), 2)

    def test_remove_equipment(self):
        """Тестируем удаление оргтехники по условию"""
        # Удаляем оргтехнику с ценой менее 2000
        self.container.remove_equipment("price < 2000")
        # Проверяем, что в контейнере осталась одна единица оргтехники
        self.assertEqual(len(self.container.equipments), 1)
        # Ожидаем, что одна единица оргтехники будет удалена

# Запускаем тесты, если файл выполняется как основная программа
if __name__ == '__main__':
    unittest.main()
