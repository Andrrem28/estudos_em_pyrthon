from time import sleep
from threading import Thread, Lock

# class MyThread(Thread):
#     def __init__(self, text: str, time: float) -> None:
#         self.text = text
#         self.time = time

#         super().__init__()

#     def run(self) -> None:
#         sleep(self.time)
#         print(self.text)


# thread_1 = MyThread('Thread 1', 3)
# thread_1.start()

# thread_2 = MyThread('Thread 2', 7)
# thread_2.start()

# thread_3 = MyThread('Thread 3', 4)
# thread_3.start()

# for i in range(10):
#     print(i)
#     sleep(1)

# def awaiting(text: str, time: float) -> None:
#     sleep(time)
#     print(text)

# thread_1 = Thread(target=awaiting, args=('Olá mundo!', 4))
# thread_2 = Thread(target=awaiting, args=('Olá mundo!', 6))
# thread_3 = Thread(target=awaiting, args=('Olá mundo!', 8))

# thread_1.start()
# thread_1.join()

# for i in range(12):
#     print(i)
#     sleep(3)

# while thread_1.is_alive():
#     print('Aguardando a Thread')
#     sleep(2)

class Ticket():
    def __init__(self, stock: int) -> None:
        self.stock = stock
        self.lock = Lock()

    def buy_ticket(self, quantity: int) -> None:
        self.lock.acquire()

        if self.stock < quantity:
            print('Não temos ingressos suficientes')
            self.lock.release()
            return
        
        sleep(1)

        self.stock -= quantity

        print(f'Você comprou {quantity} de ingressos. '
              f'Ainda temos {self.stock}')
        
        self.lock.release()

if __name__ == '__main__':
    ticket = Ticket(10)

    for i in range(1, 20):
        t = Thread(target = ticket.buy_ticket, args = (i,))
        t.start()

    print(ticket.stock)
