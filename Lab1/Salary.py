from abc import ABC, abstractmethod
import numpy as np


class Worker(ABC):

    def __init__(self, name):
        self.name = name
        self.money = 0
        self.work_done_list = []

    @abstractmethod
    def do_work(self, list_1: list, list_2: list):
        pass

    def take_salary(self, salary: int):
        self.money += salary


class Pupa(Worker):

    def do_work(self, list_1: list, list_2: list):
        sum_array = np.array(list_1) + np.array(list_2)
        sum_list = sum_array.tolist()
        print(sum_list)
        self.work_done_list.append(sum_list)


class Lupa(Worker):

    def do_work(self, list_1: list, list_2: list):
        diff_array = np.array(list_1) - np.array(list_2)
        diff_list = diff_array.tolist()
        print(diff_list)
        self.work_done_list.append(diff_list)


class Accountant:

    def __init__(self, salary_per_number):
        self.salary_per_number = salary_per_number

    def give_salary(self, worker: Worker):
        for work_done in worker.work_done_list:
            salary_to_give = len(work_done) * self.salary_per_number
            worker.take_salary(salary_to_give)
            print(f'{worker.name} took {salary_to_give} money')
        worker.work_done_list = []


if __name__ == '__main__':
    accountant = Accountant(5)
    pupa = Pupa('Oleg')
    lupa = Lupa('Igor')

    pupa.do_work([1, 2, 3, 4], [1, 2, 3, 4])
    pupa.do_work([1, 2], [1, 2])

    lupa.do_work([1, 3, 5], [1, 2, 3])

    accountant.give_salary(pupa)
    accountant.give_salary(lupa)

    print()
    print(f"{pupa.name} have {pupa.money} money")
    print(f"{lupa.name} have {lupa.money} money")
