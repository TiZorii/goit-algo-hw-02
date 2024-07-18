import queue
import random
import time

# Створити чергу заявок
request_queue = queue.Queue()

def generate_request():
    # Створити нову заявку з унікальним номером
    request_id = random.randint(1000, 9999)
    request = f"Request-{request_id}"
    # Додати заявку до черги
    request_queue.put(request)
    print(f"Generated: {request}")

def process_request():
    # Якщо черга не пуста
    if not request_queue.empty():
        # Видалити заявку з черги
        request = request_queue.get()
        # Обробити заявку
        print(f"Processed: {request}")
    else:
        print("Queue is empty")

# Головний цикл програми
try:
    while True:
        generate_request()
        time.sleep(1)  # Імітувати затримку між генераціями заявок
        process_request()
        time.sleep(1)  # Імітувати затримку між обробками заявок
except KeyboardInterrupt:
    print("Програма завершена")
