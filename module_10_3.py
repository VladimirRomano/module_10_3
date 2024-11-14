import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            repl = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += repl
            print(f" Пополнение: {repl}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            wdl = random.randint(50, 500)
            print(f" Запрос на {wdl}")
            if wdl <= self.balance:
                self.balance -= wdl
                print(f"Снятие: {wdl}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()
                time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')