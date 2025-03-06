import json  # Импортируем модуль для работы с JSON
# Импортируем ABC и abstractmethod для создания абстрактных классов
from abc import ABC, abstractmethod

# Базовый класс для оргтехники
class OfficeEquipment(ABC):
    def __init__(self, name, price, last_modified):
        self.name = name
        self.price = price
        self.last_modified = last_modified

    @abstractmethod
    def get_info(self):
        """Абстрактный метод для получения информации об оргтехнике"""
        pass  # Метод должен быть реализован в подклассах

# Класс для мышек
class Mouse(OfficeEquipment):
    # Конструктор класса инициализирующий атрибуты объекта
    def __init__(self, name, price, last_modified, mouse_type, button_count):
        # Вызов конструктора базового класса
        super().__init__(name, price, last_modified)
        self.mouse_type = mouse_type
        self.button_count = button_count

    def get_info(self):
        """Возвращает информацию о мыши в виде строки"""
        return (f"Мышь: {self.name}, Тип: {self.mouse_type}, "
                f"Кнопки: {self.button_count}, Цена: {self.price}, "
                f"Дата последнего редактирования: {self.last_modified}")

# Класс для клавиатур
class Keyboard(OfficeEquipment):
    def __init__(self, name, price, last_modified, keyboard_type, connector):
        # Вызов конструктора базового класса
        super().__init__(name, price, last_modified)
        self.keyboard_type = keyboard_type  # Тип клавиатуры
        self.connector = connector  # Разъем клавиатуры

    def get_info(self):
        """Возвращает информацию о клавиатуре в виде строки"""
        return (f"Клавиатура: {self.name}, Тип: {self.keyboard_type}, "
                f"Разъем: {self.connector}, Цена: {self.price}, "
                f"Дата последнего редактирования: {self.last_modified}")

# Класс для мониторов
class Monitor(OfficeEquipment):
    def __init__(self, name, price, last_modified, width, height):
        # Вызов конструктора базового класса
        super().__init__(name, price, last_modified)
        self.width = width  # Ширина монитора
        self.height = height  # Высота монитора

    def get_info(self):
        """Возвращает информацию о мониторе в виде строки"""
        return (f"Монитор: {self.name}, Ширина: {self.width}, "
                f"Высота: {self.height}, Цена: {self.price}, "
                f"Дата последнего редактирования: {self.last_modified}")

# Контейнер для хранения оргтехники
class EquipmentContainer:
    def __init__(self):
        self.equipments = []  # Инициализация списка для хранения оргтехники

    def add_equipment(self, equipment):
        """Добавляет оргтехнику в контейнер"""
        self.equipments.append(equipment)  # Добавляем объект оргтехники в конец списка

    def remove_equipment(self, condition):
        """Удаляет оргтехнику по заданному условию"""
        # Преобразуем условие в функцию
        def check_condition(eq):
            # Разделяем условие на части
            parts = condition.split()  # Разделяем строку условия на части
            attribute = parts[0]  # Атрибут, по которому будет производиться сравнение
            operator = parts[1]  # Оператор сравнения
            value = int(parts[2])  # Значение для сравнения (предполагаем, что это целое число)

            attr_value = getattr(eq, attribute)  # Получаем значение атрибута у объекта оргтехники

            # Проверяем условие
            if operator == '<':
                return attr_value < value  # Проверка на меньше
            elif operator == '>':
                return attr_value > value  # Проверка на больше
            elif operator == '==':
                return attr_value == value  # Проверка на равенство
            elif operator == '<=':
                return attr_value <= value  # Проверка на меньше или равно
            elif operator == '>=':
                return attr_value >= value  # Проверка на больше или равно
            elif operator == '!=':
                return attr_value != value  # Проверка на неравенство
            else:
                raise ValueError(f"Неизвестный оператор: {operator}")  # Обработка неизвестного оператора

        # Удаляем объекты, соответствующие условию
        self.equipments = [eq for eq in self.equipments if not check_condition(eq)]

    def print_equipments(self):
        """Выводит информацию о всех объектах в контейнере"""
        for eq in self.equipments:
            print(eq.get_info())  # Вывод информации о каждом объекте оргтехники

# Функция для обработки команд из файла
def process_commands(file_path):
    container = EquipmentContainer()  # Создаем новый контейнер для оргтехники

    with open(file_path, 'r', encoding='utf-8') as file:  # Открываем файл для чтения с указанием кодировки
        for line in file:  # Читаем файл построчно
            command = line.strip().split()  # Убираем пробелы и разбиваем строку на команды
            if command[0] == "ADD":  # Если команда "ADD"
                data = json.loads(" ".join(command[1:]))  # Загружаем данные из JSON(все части команды кроме первой)
                if data['type'] == 'mouse':  # Если тип мышь
                    equipment = Mouse(data['name'], data['price'], data['last_modified'], data['mouse_type'],
                                      data['button_count'])  # Создаем объект мыши
                elif data['type'] == 'keyboard':  # Если тип клавиатура
                    equipment = Keyboard(data['name'], data['price'], data['last_modified'], data['keyboard_type'],
                                         data['connector'])  # Создаем объект клавиатуры
                elif data['type'] == 'monitor':  # Если тип монитор
                    equipment = Monitor(data['name'], data['price'], data['last_modified'], data['width'],
                                        data['height'])  # Создаем объект монитора
                container.add_equipment(equipment)  # Добавляем оргтехнику в контейнер
            elif command[0] == "REM":  # Если команда "REM"
                condition = " ".join(command[1:])  # Получаем условие для удаления
                container.remove_equipment(condition)  # Удаляем оргтехнику по условию
            elif command[0] == "PRINT":  # Если команда "PRINT"
                container.print_equipments()  # Выводим информацию о текущих объектах

# Пример использования
if __name__ == "__main__":
    process_commands('commands.txt')  # Запускаем обработку команд из файла 'commands.txt'