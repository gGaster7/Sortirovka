import tkinter as tk
import random
import time

class SortVisualizer:
    def __init__(self, master, size=100):
        self.master = master
        self.master.attributes('-fullscreen', True)
        self.master.bind('<Escape>', lambda e: self.master.attributes('-fullscreen', False))

        # Цветовые настройки
        self.bg_color = '#1a1a1a'
        self.bar_color = "#6D6D6D"
        self.highlight_color = "#00FF6A"
        self.heap_color = "#FFA500"
        
        # Размеры экрана
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        # Настройки визуализации
        self.size = min(size, self.screen_width // 2)
        self.bar_width = self.screen_width / self.size
        self.max_height = self.screen_height * 0.9

        # Создание холста
        self.canvas = tk.Canvas(master, width=self.screen_width, height=self.screen_height, bg=self.bg_color)
        self.canvas.pack()

        # Генерация данных
        self.data = [random.randint(int(self.max_height*0.2), int(self.max_height)) 
                    for _ in range(self.size)]
        
        # Создание столбцов
        self.bars = []
        self.draw_initial()

        # Настройки анимации
        self.delay = 0.001
        self.master.after(100, self.heap_sort)

    def draw_initial(self):
        for i, height in enumerate(self.data):
            x0 = i * self.bar_width
            y0 = self.screen_height - height
            x1 = x0 + self.bar_width
            self.bars.append(self.canvas.create_rectangle(
                x0, y0,
                x1, self.screen_height,
                fill=self.bar_color,
                outline=self.bar_color,
                width=0
            ))

    def update_bar(self, index, color=None):
        new_height = self.screen_height - self.data[index]
        self.canvas.coords(self.bars[index],
                          index * self.bar_width,
                          new_height,
                          (index + 1) * self.bar_width,
                          self.screen_height)
        if color:
            self.canvas.itemconfig(self.bars[index], fill=color, outline=color)
        self.master.update_idletasks()
        time.sleep(self.delay)

    def heap_sort(self):
        n = len(self.data)

        # Построение max-heap
        for i in range(n//2 - 1, -1, -1):
            self.heapify(n, i)

        # Извлечение элементов из кучи
        for i in range(n-1, 0, -1):
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.update_bar(i, self.highlight_color)
            self.update_bar(0)
            self.heapify(i, 0)

        self.highlight_all_bars(self.highlight_color)

    def heapify(self, n, root_idx):
        largest = root_idx
        left = 2 * root_idx + 1
        right = 2 * root_idx + 2

        # Подсветка текущего узла
        self.update_bar(root_idx, self.heap_color)

        # Сравнение с левым потомком
        if left < n:
            self.update_bar(left, self.highlight_color)
            if self.data[left] > self.data[largest]:
                largest = left
            time.sleep(self.delay)
            self.update_bar(left, self.bar_color)

        # Сравнение с правым потомком
        if right < n:
            self.update_bar(right, self.highlight_color)
            if self.data[right] > self.data[largest]:
                largest = right
            time.sleep(self.delay)
            self.update_bar(right, self.bar_color)

        # Если наибольший элемент не в корне
        if largest != root_idx:
            self.data[root_idx], self.data[largest] = self.data[largest], self.data[root_idx]
            self.update_bar(root_idx)
            self.update_bar(largest)
            self.heapify(n, largest)

        # Возврат цвета корневого узла
        self.update_bar(root_idx, self.bar_color)

    def highlight_all_bars(self, color):
        for idx in range(self.size):
            self.canvas.itemconfig(self.bars[idx], fill=color, outline=color)
        self.master.update()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Визуализация Heap Sort")
    visualizer = SortVisualizer(root, size=400)
    root.mainloop()
