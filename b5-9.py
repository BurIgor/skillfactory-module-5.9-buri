import time

# Число прогонов функции задаем константой
NUM_RUNS = 10


# На вход декоратор принимает количество проходов
def time_this(num_runs):
    # Создаем собственно обертку-декоратор
    def time_run(func):
        # Фиксируем действия, которые должны выполняться
        def stopwatch(*args):
            avg_time = 0
            for i in range(num_runs):
                time_start = time.time()
                func()
                avg_time += time.time() - time_start
                print(i, 'проход, общее время: %.5f секунд' % avg_time)
            avg_time /= num_runs
            print("\nСреднее время выполнения = %.5f секунд" % avg_time)
        return stopwatch
    return time_run


# Декорируем исследуемую функцию
@time_this(NUM_RUNS)
def f():
    for j in range(1000000):
        pass


# Вызов функции для получения результата
f()
