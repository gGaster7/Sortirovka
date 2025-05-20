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
        self.temp_color = "#FFA500"
        
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
        
        # Инициализация столбцов
        self.bars = []
        self.draw_initial()

        # Настройки анимации
        self.delay = 0.000001
        self.master.after(100, self.start_merge_sort)

    def draw_initial(self):
        for i, height in enumerate(self.data):
            x0 = i * self.bar_width
            y0 = self.screen_height - height
            x1 = x0 + self.bar_width
            self.bars.append(self.canvas.create_rectangle(
                x0, y0, x1, self.screen_height,
                fill=self.bar_color, outline=self.bar_color, width=0
            ))

    def update_bar(self, index, color=None, height=None):
        if height is not None:
            self.data[index] = height
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

    def start_merge_sort(self):
        self.merge_sort(0, len(self.data)-1)
        self.highlight_all_bars(self.highlight_color)

    def merge_sort(self, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            self.merge(left, mid, right)

    def merge(self, left, mid, right):
        temp = []
        i = left
        j = mid + 1
        
        # Визуализация текущего блока
        self.highlight_range(left, right, self.temp_color)
        
        while i <= mid and j <= right:
            self.update_bar(i, self.highlight_color)
            self.update_bar(j, self.highlight_color)
            
            if self.data[i] <= self.data[j]:
                temp.append(self.data[i])
                i += 1
            else:
                temp.append(self.data[j])
                j += 1
                
            self.update_bar(i-1, self.bar_color)
            self.update_bar(j-1, self.bar_color)

        while i <= mid:
            temp.append(self.data[i])
            i += 1

        while j <= right:
            temp.append(self.data[j])
            j += 1

        # Обновление основного массива
        for k in range(len(temp)):
            self.update_bar(left + k, height=temp[k], color=self.highlight_color)
            self.update_bar(left + k, self.bar_color)

    def highlight_range(self, start, end, color):
        for idx in range(start, end+1):
            self.canvas.itemconfig(self.bars[idx], fill=color, outline=color)
        self.master.update()

    def highlight_all_bars(self, color):
        for idx in range(self.size):
            self.canvas.itemconfig(self.bars[idx], fill=color, outline=color)
        self.master.update()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Сортировка слиянием")
    visualizer = SortVisualizer(root, size=1000)
    root.mainloop()
