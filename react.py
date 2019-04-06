"""
██████╗ ███████╗ █████╗  ██████╗████████╗
██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝
██████╔╝█████╗  ███████║██║        ██║
██╔══██╗██╔══╝  ██╔══██║██║        ██║
██║  ██║███████╗██║  ██║╚██████╗   ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝
****************************************************************************
|                         python reaction game                             |
|   created by petabite aka philip z(https://github.com/petabite)          |
****************************************************************************
"""

#import modules
import tkinter as tk
import random
import datetime
import pickle

"""
██╗    ██╗██╗██████╗  ██████╗ ███████╗████████╗     ██████╗██╗      █████╗ ███████╗███████╗███████╗███████╗
██║    ██║██║██╔══██╗██╔════╝ ██╔════╝╚══██╔══╝    ██╔════╝██║     ██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝
██║ █╗ ██║██║██║  ██║██║  ███╗█████╗     ██║       ██║     ██║     ███████║███████╗███████╗█████╗  ███████╗
██║███╗██║██║██║  ██║██║   ██║██╔══╝     ██║       ██║     ██║     ██╔══██║╚════██║╚════██║██╔══╝  ╚════██║
╚███╔███╔╝██║██████╔╝╚██████╔╝███████╗   ██║       ╚██████╗███████╗██║  ██║███████║███████║███████╗███████║
 ╚══╝╚══╝ ╚═╝╚═════╝  ╚═════╝ ╚══════╝   ╚═╝        ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝

"""

class TitleText(tk.Label):
    def __init__(self, parent):
        tk.Label.__init__(self, parent)
        self.config(text = 'react', font=("Corbel", 100))
        self.pack()

class BodyText(tk.Label):
    def __init__(self, parent, text):
        tk.Label.__init__(self, parent)
        self.text = text
        self.config(text = self.text, font=("Corbel", 20))
        self.pack()

class GameButton(tk.Button):
    def __init__(self, parent, text, command):
        tk.Button.__init__(self, parent)
        self.text = text
        self.command = command
        self.config(text=self.text, font=("Corbel", 20), height=2, width=15, command = self.command)
        self.pack()

"""
 ██████╗ ██╗   ██╗██╗
██╔════╝ ██║   ██║██║
██║  ███╗██║   ██║██║
██║   ██║██║   ██║██║
╚██████╔╝╚██████╔╝██║
 ╚═════╝  ╚═════╝ ╚═╝

"""

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('react')
        self.geometry('500x700')
        tk.Frame(self).pack()
        StartScreen(self).pack()

class StartScreen(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        TitleText(self)
        btext = BodyText(self, text='welcome')
        btext.config(pady = 150)
        GameButton(self, text='play', command=self.close)
    def close(self):
        self.destroy()
        Game(self.parent).pack()

class Game(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.time = 3
        self.randomtime = random.randint(1,10)
        self.counter = 0
        TitleText(self)
        BodyText(self, text='click when the box turns blue').pack()
        self.countdown = BodyText(self, text = ' ')
        self.countdown.config(font = ("Corbel", 30))
        self.box = tk.Frame(self, width=200, height = 200, background = 'white')
        self.box.pack()
        self.startcountdown()
    def startcountdown(self):
        self.box.config(background='white')
        if self.time > 0:
            self.countdown.config(text=self.time)
            self.time -= 1
            self.after(1000, self.startcountdown)
        else:
            self.countdown.config(text='go')
            self.changecolor()
            self.clickbox = GameButton(self,text='click',command=self.checkmouseclick)
    def changecolor(self):
        if self.counter == self.randomtime:
            self.box.config(background = '#647FE9')
            self.timeboxchange = datetime.datetime.now()
            # self.checkmouseclick()  #uncomment to cheat, will break game at line 117
        else:
            self.counter += 1
            self.after(1000, self.changecolor)
    def checkmouseclick(self):
        if self.counter != self.randomtime:
            BodyText(self, text='you clicked too early')
            GameButton(self, text='try again', command=self.reinit).pack()
        else:
            score = str(float(str(datetime.datetime.now() - self.timeboxchange)[5:-3]))
            self.destroy()
            Highscores(self.parent, score).pack()
        self.clickbox.pack_forget()
    def reinit(self):
        self.destroy()
        Game(self.parent).pack()

class Highscores(tk.Frame):
    def __init__(self, parent, score):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.score = score
        TitleText(self)
        BodyText(self, text='your reaction time: ' + self.score + ' seconds')
        BodyText(self, text='-'*10)
        BodyText(self, text='highscores').pack()
        self.addhighscore()
        self.showhighscores()
        GameButton(self, text='play again', command=self.playagain).pack()
    def addhighscore(self):
        with open('.highscores', 'rb') as highscores_file:
            highscores = pickle.load(highscores_file)
        sorted_highscores = sorted(highscores)
        if len(highscores) == 5 and self.score < sorted_highscores[4]:
            del sorted_highscores[4]
            sorted_highscores.append(self.score)
            with open('.highscores', 'wb') as highscores_file:
                pickle.dump(sorted_highscores, highscores_file)
    def showhighscores(self):
        with open('.highscores', 'rb') as highscores_file:
            highscores = pickle.load(highscores_file)
        sorted_highscores = sorted(highscores)
        if len(highscores) == 0:
            BodyText(self, text='no highscores yet').pack()
        else:
            for i in range(0, len(highscores)):
                BodyText(self, text= str(i+1) + '. ' + str(sorted_highscores[i]) + ' secs')
    def playagain(self):
        self.destroy()
        Game(self.parent).pack()

#init game
app = MainWindow()
app.mainloop()
