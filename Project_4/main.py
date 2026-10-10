import argparse
import random


class Order:
    def __init__(self, numder):
        self.number = numder


class User:
    def __init__(self, lastname, firstname, telephone, address):
        self.lastname = lastname
        self.firstname = firstname
        self.telephone = telephone
        self.address = address

    def create(self):
        ...


class Employee(User):
    def __init__(self, lastname, firstname, telephone, address, position, salary):
        super().__init__(lastname, firstname, telephone, address)

        self.position = position
        self.salary = salary

    def create(self):
        with open("users.txt", "a", encoding="utf8") as file:
            file.write(f"lastname |:| {self.lastname} |,| firstname |:| {self.firstname} |,| " + 
                       f"telephone |:| {self.telephone} |,| address |:| {self.address} |,| " + 
                       f"position |:| {self.position} |,| salary |:| {self.salary}\n")


class Client(User):
    def __init__(self, lastname, firstname, telephone, address, order):
        super().__init__(lastname, firstname, telephone, address)

        self.order = order

    def create(self):
        with open("users.txt", "a", encoding="utf8") as file:
            file.write(f"lastname |:| {self.lastname} |,| firstname |:| {self.firstname} |,| " + 
                       f"telephone |:| {self.telephone} |,| address |:| {self.address} |,| " + 
                       f"order |:| {self.order.number}\n")


class CArgparse:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Модуль создания пользователей.")

        self.parser.add_argument("-mode", choices=["auto", "handle", "read"], default="auto", 
                                 help="Сценарий: auto (по умолчанию) или handle (ручной) или read (чтение).")
        self.parser.add_argument("-type", choices=["employee", "client"], default="employee", help="Тип пользователя.")
        self.parser.add_argument("-lastname", help="Фамилия")
        self.parser.add_argument("-firstname", help="Имя")
        self.parser.add_argument("-telephone", help="Телефон")
        self.parser.add_argument("-address", help="Адрес")
        self.parser.add_argument("-position", help="Должность (сотрудник)")
        self.parser.add_argument("-salary", type=int, help="Зарплата (сотрудник)")
        self.parser.add_argument("-order", help="Номер заказа (клиент)")

    def parse(self):
        return self.parser.parse_args()


class CScenario:
    def __init__(self, args):
        self.args = args

    def run(self):
        if self.args.mode == "auto":
            self.auto_scenario()
        elif self.args.mode == "handle":
            self.handle_scenario()
        elif self.args.mode == "read":
            self.read()
        else:
            print("<E> Неверный сценарий")

    def auto_scenario(self):
        print("== Сценарий: АВТОМАТИЧЕСКИЙ ==")

        em_count, cl_count = 5, 5

        lastnames = [
            "Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", 
            "Ковалев", "Соколов", "Федоров", "Михайлов", "Николаев",
            "Морозов", "Васильев", "Павлов", "Волков", "Семенов",
            "Владимиров", "Александров", "Максимов", "Дмитриев",
        ]

        firstnames = [
            "Иван", "Петр", "Сидор", "Смирн", "Кузн", 
            "Ковал", "Сокол", "Федор", "Михаил", "Никола",
            "Мороз", "Василий", "Павл", "Волк", "Семен",
            "Владимир", "Александр", "Максим", "Дмитрий",
        ]

        telephones = [
            "+79456541278", "+79457652389", "+79457763498", "+79457874509", "+79457985610", 
            "+79458096721", "+79458107832", "+79458218943", "+79458329054", "+79458440165",
            "+79458551276", "+79458662387", "+79458773498", "+79458884509", "+79458995610",
            "+79459006721", "+79459117832", "+79459228943", "+79459339054", "+79459450165",
        ]

        addresses = [
            "Красноярск, ул. Ак. Киренского, 26 к1", "Красноярск, пр. Свободный, 79", 
            "Красноярск, ул. Комсомольская, 1", "Красноярск, ул. Комсомольская, 2", "Красноярск, ул. Комсомольская, 3",
            "Москва, ул. Комсомольская, 1", "Москва, ул. Комсомольская, 2", "Москва, ул. Комсомольская, 3",
            "Санкт-Петербург, ул. Ленина, 1", "Санкт-Петербург, ул. Ленина, 2", "Санкт-Петербург, ул. Ленина, 3",
        ]

        positions = [
            "инженер", "руководитель", "программист", "тестировщик", "дизайнер",
            "уборщик", "повар", "администратор", "менеджер", "кладовщик",
            "маркетолог", "продавец", "специалист", "секретарь", "адвокат"
        ]

        for _ in range(em_count):
            employee = Employee(
                lastname=random.choice(lastnames), firstname=random.choice(firstnames),
                telephone=random.choice(telephones), address=random.choice(addresses),
                position=random.choice(positions), salary=random.randint(100, 1000),
            )
            employee.create()
            print(f"<W> Создан сотрудник: {employee.lastname} {employee.firstname}")

        for _ in range(cl_count):
            client = Client(
                lastname=random.choice(lastnames), firstname=random.choice(firstnames),
                telephone=random.choice(telephones), address=random.choice(addresses),
                order=Order(f"Order-{random.randrange(100, 1000)}"),
            )
            client.create()
            print(f"<W> Создан клиент: {client.lastname} {client.firstname}, заказ: {client.order.number}")

        print(f"<W> Данные о {em_count} сотрудниках и {cl_count} клиентах добавлены в файл users.txt")

    def handle_scenario(self):
        print("== Сценарий: РУЧНОЙ (автоматизированный) ==")
        missing = [i for i in ("lastname", "firstname", "telephone", "address") if not getattr(self.args, i)] # x.y
        if missing:
            print(f"<E> Не заданы обязательные параметры: {', '.join('-' + m for m in missing)}")
            return

        if self.args.type == 'employee':
            if self.args.position is None or self.args.salary is None:
                print("<E> Для сотрудника обязательны -position и -salary")
                return
            
            user = Employee(
                lastname=self.args.lastname,
                firstname=self.args.firstname,
                telephone=self.args.telephone,
                address=self.args.address,
                position=self.args.position,
                salary=self.args.salary,
            )
        else:
            if not self.args.order:
                print("<E> Для клиента обязателен -order")
                return
            
            user = Client(
                lastname=self.args.lastname,
                firstname=self.args.firstname,
                telephone=self.args.telephone,
                address=self.args.address,
                order=Order(self.args.order),
            )

        user.create()
        print(f"<W> Пользователь типа '{self.args.type}' создан и записан в users.txt")

    def read(self):
        with open("users.txt", "r", encoding="utf8") as file:
            print("\n========\n\n".join(["\n".join([i.replace(" |:| ", ": ") for i in line.split(" |,| ")]) 
                                         for line in file.readlines()]))
            
                
def main():
    args = CArgparse().parse()
    CScenario(args).run()


if __name__ == "__main__":
    main()