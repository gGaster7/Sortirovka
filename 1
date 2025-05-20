import tkinter as tk
import random
import time

class SortVisualizer:
    def __init__(self, master, size=100):
        self.master = master
        self.master.attributes('-fullscreen', True)
        self.master.bind('<Escape>', lambda e: self.master.attributes('-fullscreen', False))

        # Цвет
        self.bg_color = '#1a1a1a'
        self.bar_color = "#6D6D6D"
        self.highlight_color = "#00FF6A"
        self.pivot_color = "#269E3A"
        
        # Получаем размеры экрана
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        self.size = min(size, self.screen_width // 2)  
        self.bar_width = self.screen_width / self.size
        self.max_height = self.screen_height * 0.9  # столбики делает выше

        # Создаем холст
        self.canvas = tk.Canvas(master, width=self.screen_width, height=self.screen_height, bg=self.bg_color)
        self.canvas.pack()



        self.data = [random.randint(int(self.max_height*0.2), int(self.max_height)) 
                    for _ in range(self.size)]
        



        self.bars = []
        self.draw_initial()


        self.delay = 0.001  # Задержка для плавности
        self.master.after(100, self.quick_sort_wrapper)

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
                width=0  # гладкость через убирание контура
            ))

    def update_bar(self, index, color=None):
        # обновление кадва
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

    def quick_sort_wrapper(self):
        self.quick_sort(0, len(self.data)-1)
        self.highlight_all_bars(self.highlight_color)

    def quick_sort(self, low, high):
        if low < high:
            # визуал диапозона/
            self.highlight_range(low, high, self.pivot_color)
            pi = self.partition(low, high)
            self.quick_sort(low, pi-1)
            self.quick_sort(pi+1, high)

    def partition(self, low, high):
        pivot = self.data[high]
        i = low - 1
    

        self.update_bar(high, self.pivot_color)
        
        for j in range(low, high):
            # Подсветка сравниваемых элементов
            self.update_bar(j, self.highlight_color)
            if self.data[j] <= pivot:
                i += 1
                if i != j:
                    # перемещаемые элементы 
                    self.update_bar(i, self.highlight_color)
                    self.data[i], self.data[j] = self.data[j], self.data[i]
                    self.update_bar(i)
                    self.update_bar(j)
                self.update_bar(i, self.bar_color)
            self.update_bar(j, self.bar_color)
        
        # Перемещение 
        self.data[i+1], self.data[high] = self.data[high], self.data[i+1]
        self.update_bar(i+1)
        self.update_bar(high)
        self.update_bar(high, self.bar_color)  # Сброс 
        
        return i + 1

    def highlight_range(self, low, high, color):
        for idx in range(low, high+1):
            self.canvas.itemconfig(self.bars[idx], fill=color, outline=color)
        self.master.update()

    def highlight_all_bars(self, color):
        for idx in range(self.size):
            self.canvas.itemconfig(self.bars[idx], fill=color, outline=color)
        self.master.update()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Сортировка массива")
    visualizer = SortVisualizer(root, size=1000)
    root.mainloop()
