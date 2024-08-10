import random


class Help:
    @staticmethod
    def generate_valid_email():
        return f"Natali_Dmitrievskaya_12_{random.randint(100, 999)}@yandex.ru"

    @staticmethod
    def generate_valid_password():
        return f"F{random.randint(10, 99)}_{random.randint(10, 99)}"

    @staticmethod
    def generate_not_valid_password():
        return f"{random.randint(10, 99)}_{random.randint(10, 99)}"