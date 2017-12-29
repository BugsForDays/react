import tkinter as tk
# from pygame import mixer # Load the required library
import time
#BUG not working
# mixer.init()
# mixer.music.load('beep.mp3')
# mixer.music.set_volume(1.0)
# mixer.music.play()

# class StartScreen:
#     def __init__(self, parent):
#         self.parent = parent
#         self.frame = tk.Frame(self.parent)
#         self.title = tk.Label(self.frame, text='react')
#         self.playbutton = tk.Button(self.frame, text= 'play', command = self.close)
#         self.title.pack()
#         self.playbutton.pack()
#         self.frame.pack()
#     def close(self):
#         self.frame.destroy()
# class Game:
#     pass
# window = tk.Tk()
# window.title('react')
# window.geometry('500x500')
#
# firstscreen = StartScreen(window)
#
# window.mainloop()



class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('react')
        self.geometry('500x500')
        tk.Frame(self).pack()
        StartScreen(self).pack()
class StartScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.title = tk.Label(self, text='react')
        self.title.pack()
        self.playbutton = tk.Button(self, text= 'play', command = self.close)
        self.playbutton.pack()
    def close(self):
        self.destroy()
        Game(self.parent).pack()
class Game(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.title = tk.Label(self, text='react')
        tk.Label(self, text='Click anywhere when the box turns blue').pack()
        self.title.pack()
        self.countdown = tk.Label(self)
        self.countdown.pack()
        box = tk.Frame(self, width=200, height = 200, background = 'white')
        box.pack()
        box.config(background = '#647FE9')
        # self.countdown.config(text='1')
        # time.sleep(1)
        # self.countdown.config(text='2')
        self.startcountdown()
    def startcountdown(self):
        time = 3
        while time > 0:
            time -= 1
            self.after(1000, self.countdown.config(text=str(time)))

        # for i in range(3, 0, -1):
        #     self.countdown.config(text=i)
        #     self.after(1000)
        # self.countdown.config(text='GO!')

        # canvas = tk.Canvas(self, width=200, height=200)
        # canvas.pack()
        # canvas.create_rectangle(2, 190, 190, 0, fill='white')

app = MainWindow()
app.mainloop()
