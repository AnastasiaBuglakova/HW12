# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре
# недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов
# вместе взятых.
class FIO_check:
    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if self.param(value):
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f"You have to enter FIO in title style")


class Student:
    students = {}
    fio = FIO_check(str.istitle)

    def __init__(self, fio):
        self.fio = fio
        with open("предметы.csv", "r", encoding="utf-8") as f:
            subjects = f.readlines()
        self.tests_results = {i.strip(): [] for i in subjects}
        self.valuations = {i.strip(): [] for i in subjects}

    def __repr__(self):
        return (f'Student FIO{self.fio}')

    def __call__(self, val_or_test, **kwargs):
        if val_or_test == 'valuations':
            for k, v in kwargs.items():
                if k in self.valuations:
                    if 2 <= v <= 5:
                        self.valuations[k] += [v]
                    else:
                        raise ValueError('Valuation have to be more than 2 and less than 5')
                else:
                    raise KeyError('Such subject doesn`t exists')
        elif val_or_test == 'tests':
            for k, v in kwargs.items():
                if k in self.tests_results:
                    if 0 <= v <= 100:
                        self.tests_results[k] += [v]
                    else:
                        raise ValueError('Valuation have to be more than 0 and less than 100')
                else:
                    raise KeyError('Such subject doesn`t exists')

    def average_tests(self, subject):
        if subject in self.tests_results:
            return sum(self.tests_results[subject]) / (len(self.tests_results[subject]))
        else:
            raise KeyError('Such subject doesn`t exists')

    def average_valuations(self):
        count = 0
        sum_ = 0
        for k in self.valuations:
            if self.valuations[k] != []:
                count += len(self.valuations[k])
                sum_ += sum(self.valuations[k])
        return sum_ / count


nasta = Student('Dafgadf Tdf Gii')
val = nasta('valuations', Биология=3)
val = nasta('tests', Биология=87)
val = nasta('valuations', Конфликтология=5)

print(nasta.__dict__)
print(nasta.average_tests('Биология'))
print(nasta.average_valuations())
