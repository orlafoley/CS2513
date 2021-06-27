# Sources outside lecture notes:
# https://redhuli.io/tkinter-radiobutton-and-checkbutton/
# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

from tkinter import *
from random import *
from time import *


class Counter:
    def __init__(self):
        self._counter = 0

    def increment(self):
        self._counter += 1

    def getCounter(self):
        return self._counter

    def __str__(self):
        return '%s' % (str(self._counter))

    counter = property(getCounter, increment)


myCounter = Counter()


def updateScore():
    score['text'] = 'Score: ' + myCounter.__str__()


def totalTime(begin, end):
    return end - begin


start = int(round(time() * 1000))


def addToCounter1(event):
    global start
    gameCanvas.delete(peanut1)
    finish = int(round(time() * 1000))
    if totalTime(start, finish) < 2000:
        myCounter.increment()
        start = int(round(time() * 1000))
    myCounter.increment()
    updateScore()
def addToCounter2(event):
    global start
    gameCanvas.delete(peanut2)
    finish = int(round(time() * 1000))
    if totalTime(start, finish) < 2000:
        myCounter.increment()
        start = int(round(time() * 1000))
    myCounter.increment()
    updateScore()
def addToCounter3(event):
    global start
    gameCanvas.delete(peanut3)
    finish = int(round(time() * 1000))
    if totalTime(start, finish) < 2000:
        myCounter.increment()
        start = int(round(time() * 1000))
    myCounter.increment()
    updateScore()
def addToCounter4(event):
    global start
    gameCanvas.delete(peanut4)
    finish = int(round(time() * 1000))
    if totalTime(start, finish) < 2000:
        myCounter.increment()
        start = int(round(time() * 1000))
    myCounter.increment()
    updateScore()
def addToCounter5(event):
    global start
    gameCanvas.delete(peanut5)
    finish = int(round(time() * 1000))
    if totalTime(start, finish) < 2000:
        myCounter.increment()
        start = int(round(time() * 1000))
    myCounter.increment()
    updateScore()
def addToCounter6(event):
    global start
    gameCanvas.delete(peanut6)
    finish = int(round(time() * 1000))
    if totalTime(start, finish) < 2000:
        myCounter.increment()
        start = int(round(time() * 1000))
    myCounter.increment()
    updateScore()
def addToCounter7(event):
    global start
    gameCanvas.delete(peanut7)
    finish = int(round(time() * 1000))
    if totalTime(start, finish) < 2000:
        myCounter.increment()
        start = int(round(time() * 1000))
    myCounter.increment()
    updateScore()
def addToCounter8(event):
    global start
    gameCanvas.delete(peanut8)
    finish = int(round(time() * 1000))
    if totalTime(start, finish) < 2000:
        myCounter.increment()
        start = int(round(time() * 1000))
    myCounter.increment()
    updateScore()
def addToCounter9(event):
    global start
    gameCanvas.delete(peanut9)
    finish = int(round(time() * 1000))
    if totalTime(start, finish) < 2000:
        myCounter.increment()
        start = int(round(time() * 1000))
    myCounter.increment()
    updateScore()
def addToCounter10(event):
    global start
    gameCanvas.delete(peanut10)
    finish = int(round(time() * 1000))
    if totalTime(start, finish) < 2000:
        myCounter.increment()
        start = int(round(time() * 1000))
    myCounter.increment()
    updateScore()


def playQuiz():
    class SampleApp(Tk):
        def __init__(self, *args, **kwargs):
            Tk.__init__(self, *args, **kwargs)
            self.title('Jimmy Carter Peanut Game')
            self.geometry('600x600')

            container = Frame(self)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}
            for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven,
                      PageEight, PageNine, PageTen):
                page_name = F.__name__
                frameC = F(parent=container, controller=self)
                self.frames[page_name] = frameC
                frameC.grid(row=0, column=0, sticky="nsew")

            self.show_frame("StartPage")

        def show_frame(self, page_name):
            frameC = self.frames[page_name]
            frameC.tkraise()

    class StartPage(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.controller = controller
            label = Label(self,
                          text="This is a quiz relating to Jimmy Carter. \n Click each of the answers to learn more. "
                               "\n There is no scoring in this quiz, it is \n a simple learning exercise. \n"
                               "\n Information has been gathered from his autobiography.")
            label.pack(side="top", fill="x", pady=10)
            begin = Button(self, text="Start Quiz", command=lambda: controller.show_frame("PageOne"))
            begin.pack()

    class PageOne(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.controller = controller
            var1 = StringVar(self)

            def qu1out():
                if var1.get() == '1924':
                    ans1['text'] = ''
                    ans1['text'] = 'Correct - he was born on the 1st of October 1924.'
                elif var1.get() == '1925':
                    ans1['text'] = ''
                    ans1['text'] = 'Not in 1925 but you\'re close.'
                elif var1.get() == '1926':
                    ans1['text'] = ''
                    ans1['text'] = 'Maybe a bit earlier...'

            Label(self, text='What year was Jimmy Carter born?').pack(anchor='w')
            Radiobutton(self, text="1924", variable=var1, value='1924', command=qu1out).pack(anchor='w')
            Radiobutton(self, text="1925", variable=var1, value='1925', command=qu1out).pack(anchor='w')
            Radiobutton(self, text="1926", variable=var1, value='1926', command=qu1out).pack(anchor='w')
            ans1 = Label(self, text='')
            ans1.pack()

            buttonForward = Button(self, text="Continue", command=lambda: controller.show_frame("PageTwo"))
            buttonForward.pack(side=RIGHT)

    class PageTwo(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.controller = controller
            var2 = StringVar(self)

            def qu2out():
                if var2.get() == 'Alabama':
                    ans2['text'] = ''
                    ans2['text'] = 'Unlike Lynyrd Skynyrd, Carter does not refer to Alabama as his "Sweet Home".'
                elif var2.get() == 'Georgia':
                    ans2['text'] = ''
                    ans2[
                        'text'] = 'Correct - he was born in the State of Georgia as opposed to the country like Stalin.'
                elif var2.get() == 'South Carolina':
                    ans2['text'] = ''
                    ans2['text'] = 'He lives a little bit further south than South Carolina.'

            Label(self, text='What state was he born in?').pack(anchor='w')
            Radiobutton(self, text="Alabama", variable=var2, value='Alabama', command=qu2out).pack(anchor='w')
            Radiobutton(self, text="Georgia", variable=var2, value='Georgia', command=qu2out).pack(anchor='w')
            Radiobutton(self, text="South Carolina", variable=var2, value='South Carolina', command=qu2out).pack(
                anchor='w')
            ans2 = Label(self, text='')
            ans2.pack()

            buttonBack = Button(self, text="Back", command=lambda: controller.show_frame("PageOne"))
            buttonBack.pack(side=LEFT)
            buttonForward = Button(self, text="Continue", command=lambda: controller.show_frame("PageThree"))
            buttonForward.pack(side=RIGHT)

    class PageThree(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.controller = controller
            var3 = StringVar(self)

            def qu3out():
                if var3.get() == 'Air Force':
                    ans3['text'] = ''
                    ans3['text'] = 'Incorrect'
                elif var3.get() == 'Army':
                    ans3['text'] = ''
                    ans3['text'] = 'Incorrect'
                elif var3.get() == 'Navy':
                    ans3['text'] = ''
                    ans3['text'] = 'Correct'

            Label(self, text='What branch of the military did he serve in?').pack(anchor='w')
            Radiobutton(self, text="Air Force", variable=var3, value='Air Force', command=qu3out).pack(anchor='w')
            Radiobutton(self, text="Army", variable=var3, value='Army', command=qu3out).pack(anchor='w')
            Radiobutton(self, text="Navy", variable=var3, value='Navy', command=qu3out).pack(anchor='w')
            ans3 = Label(self, text='')
            ans3.pack()

            buttonBack = Button(self, text="Back", command=lambda: controller.show_frame("PageTwo"))
            buttonBack.pack(side=LEFT)
            buttonForward = Button(self, text="Continue", command=lambda: controller.show_frame("PageFour"))
            buttonForward.pack(side=RIGHT)

    class PageFour(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.controller = controller
            var4 = StringVar(self)

            def qu4out():
                if var4.get() == 'Georgia State Senate':
                    ans4['text'] = ''
                    ans4['text'] = 'Correct - he was elected in 1962 to the State Senate.'
                elif var4.get() == 'Governor of Georgia':
                    ans4['text'] = ''
                    ans4['text'] = 'Incorrect - he was elected Governor in 1970.'
                elif var4.get() == 'US Presidency':
                    ans4['text'] = ''
                    ans4['text'] = 'Incorrect - this was the last office he held.'

            Label(self, text='What office was he first elected to?').pack(anchor='w')
            Radiobutton(self, text="Georgia State Senate", variable=var4, value='Georgia State Senate',
                        command=qu4out).pack(anchor='w')
            Radiobutton(self, text="Governor of Georgia", variable=var4, value='Governor of Georgia',
                        command=qu4out).pack(anchor='w')
            Radiobutton(self, text="US Presidency", variable=var4, value='US Presidency', command=qu4out).pack(
                anchor='w')
            ans4 = Label(self, text='')
            ans4.pack()

            buttonBack = Button(self, text="Back", command=lambda: controller.show_frame("PageThree"))
            buttonBack.pack(side=LEFT)
            buttonForward = Button(self, text="Continue", command=lambda: controller.show_frame("PageFive"))
            buttonForward.pack(side=RIGHT)

    class PageFive(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.controller = controller
            var5 = StringVar(self)

            def qu5out():
                if var5.get() == 'Amy':
                    ans5['text'] = ''
                    ans5['text'] = 'Incorrect - that\'s his daughter\'s name.'
                elif var5.get() == 'Lillian':
                    ans5['text'] = ''
                    ans5['text'] = 'Incorrect - that was his mother\'s name.'
                elif var5.get() == 'Rosalynn':
                    ans5['text'] = ''
                    ans5['text'] = 'Correct - they have been married since 1946.'

            Label(self, text='What is his wife\'s name?').pack(anchor='w')
            Radiobutton(self, text="Amy", variable=var5, value='Amy', command=qu5out).pack(anchor='w')
            Radiobutton(self, text="Lillian", variable=var5, value='Lillian', command=qu5out).pack(anchor='w')
            Radiobutton(self, text="Rosalynn", variable=var5, value='Rosalynn', command=qu5out).pack(anchor='w')
            ans5 = Label(self, text='')
            ans5.pack()

            buttonBack = Button(self, text="Back", command=lambda: controller.show_frame("PageFour"))
            buttonBack.pack(side=LEFT)
            buttonForward = Button(self, text="Continue", command=lambda: controller.show_frame("PageSix"))
            buttonForward.pack(side=RIGHT)

    class PageSix(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.controller = controller
            var6 = StringVar(self)

            def qu6out():
                if var6.get() == '1974-1977':
                    ans6['text'] = ''
                    ans6['text'] = 'Incorrect - this was Gerald Ford\'s term.'
                elif var6.get() == '1977-1981':
                    ans6['text'] = ''
                    ans6['text'] = 'Correct'
                elif var6.get() == '1981-1989':
                    ans6['text'] = ''
                    ans6['text'] = 'Incorrect - this was Ronald Reagan\'s term.'

            Label(self, text='Between which dates was he the President?').pack(anchor='w')
            Radiobutton(self, text="1974-1977", variable=var6, value='1974-1977', command=qu6out).pack(anchor='w')
            Radiobutton(self, text="1977-1981", variable=var6, value='1977-1981', command=qu6out).pack(anchor='w')
            Radiobutton(self, text="1981-1989", variable=var6, value='1981-1989', command=qu6out).pack(anchor='w')
            ans6 = Label(self, text='')
            ans6.pack()

            buttonBack = Button(self, text="Back", command=lambda: controller.show_frame("PageFive"))
            buttonBack.pack(side=LEFT)
            buttonForward = Button(self, text="Continue", command=lambda: controller.show_frame("PageSeven"))
            buttonForward.pack(side=RIGHT)

    class PageSeven(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.controller = controller
            var7 = StringVar(self)

            def qu7out():
                if var7.get() == 'Hubert Humphrey':
                    ans7['text'] = ''
                    ans7['text'] = 'Incorrect - he was VP in the 1960\'s.'
                elif var7.get() == 'Millard Fillmore':
                    ans7['text'] = ''
                    ans7['text'] = 'Incorrect - he was the President in the 1850\'s'
                elif var7.get() == 'Walter Mondale':
                    ans7['text'] = ''
                    ans7['text'] = 'Correct - Mondale was a Senator from Minnesota before becoming Carter\'s VP.'

            Label(self, text='Who was his Vice President?').pack(anchor='w')
            Radiobutton(self, text="Hubert Humphrey", variable=var7, value='Hubert Humphrey', command=qu7out).pack(
                anchor='w')
            Radiobutton(self, text="Millard Fillmore", variable=var7, value='Millard Fillmore', command=qu7out).pack(
                anchor='w')
            Radiobutton(self, text="Walter Mondale", variable=var7, value='Walter Mondale', command=qu7out).pack(
                anchor='w')
            ans7 = Label(self, text='')
            ans7.pack()

            buttonBack = Button(self, text="Back", command=lambda: controller.show_frame("PageSix"))
            buttonBack.pack(side=LEFT)
            buttonForward = Button(self, text="Continue", command=lambda: controller.show_frame("PageEight"))
            buttonForward.pack(side=RIGHT)

    class PageEight(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.controller = controller
            var8 = StringVar(self)

            def qu8out():
                if var8.get() == 'Israel and Egypt':
                    ans8['text'] = ''
                    ans8[
                        'text'] = 'Correct - he invited Anwar Sadat and Menachem Begin to Camp David to work out a deal.'
                elif var8.get() == 'Sudan and South Sudan':
                    ans8['text'] = ''
                    ans8['text'] = 'Incorrect - South Sudan did not become a country until 2011.'
                elif var8.get() == 'North Korea and South Korea':
                    ans8['text'] = ''
                    ans8['text'] = 'Incorrect - the armistice was signed in 1953.'

            Label(self, text='One of Carter\'s greatest achievements was a peace deal brokered between...?').pack(
                anchor='w')
            Radiobutton(self, text="Israel and Egypt", variable=var8, value='Israel and Egypt', command=qu8out).pack(
                anchor='w')
            Radiobutton(self, text="Sudan and South Sudan", variable=var8, value='Sudan and South Sudan',
                        command=qu8out).pack(anchor='w')
            Radiobutton(self, text="North Korea and South Korea", variable=var8, value='North Korea and South Korea',
                        command=qu8out).pack(anchor='w')
            ans8 = Label(self, text='')
            ans8.pack()

            buttonBack = Button(self, text="Back", command=lambda: controller.show_frame("PageSeven"))
            buttonBack.pack(side=LEFT)
            buttonForward = Button(self, text="Continue", command=lambda: controller.show_frame("PageNine"))
            buttonForward.pack(side=RIGHT)

    class PageNine(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.controller = controller
            var9 = StringVar(self)

            def qu9out():
                if var9.get() == 'Transfer of the Panama Canal.':
                    ans9['text'] = ''
                    ans9['text'] = 'Incorrect - though a politically unpopular move, \n Carter gave Panama more sovereignty over the Canal.'
                elif var9.get() == 'American citizens were held hostage in Iran.':
                    ans9['text'] = ''
                    ans9['text'] = 'Correct - 52 Americans were kept as hostages. They were held for 444 days.'
                elif var9.get() == 'Stagflation':
                    ans9['text'] = ''
                    ans9['text'] = 'Incorrect - although the economy was poor at this time, \n it was not the worst issue Carter faced.'

            Label(self, text='Carter describes his final year in office as \n "the most stressful and unpleasant year of my life". '
                       '\n Why does he describe it like this?').pack(anchor='w')
            Radiobutton(self, text="Transfer of the Panama Canal.", variable=var9,
                        value='Transfer of the Panama Canal.', command=qu9out).pack(anchor='w')
            Radiobutton(self, text="American citizens were held hostage in Iran.", variable=var9,
                        value='American citizens were held hostage in Iran.', command=qu9out).pack(anchor='w')
            Radiobutton(self, text="Stagflation", variable=var9,
                        value='Stagflation', command=qu9out).pack(anchor='w')
            ans9 = Label(self, text='')
            ans9.pack()

            buttonBack = Button(self, text="Back", command=lambda: controller.show_frame("PageEight"))
            buttonBack.pack(side=LEFT)
            buttonForward = Button(self, text="Continue", command=lambda: controller.show_frame("PageTen"))
            buttonForward.pack(side=RIGHT)

    class PageTen(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.controller = controller
            var10 = StringVar(self)

            def qu10out():
                if var10.get() == 'Peanuts':
                    ans10['text'] = ''
                    ans10['text'] = 'Correct - one of his campaign slogans was "Not Just Peanuts".'
                elif var10.get() == 'Cotton':
                    ans10['text'] = ''
                    ans10['text'] = 'Incorrect - cotton is more commonly produced in Texas.'
                elif var10.get() == 'Tobacco':
                    ans10['text'] = ''
                    ans10['text'] = 'Incorrect - in fact he never smoked.'

            Label(self, text='What did he grow on his farm? Hint: Think of what you\'ve collected earlier.').pack(anchor='w')
            Radiobutton(self, text="Peanuts", variable=var10, value='Peanuts', command=qu10out).pack(anchor='w')
            Radiobutton(self, text="Cotton", variable=var10, value='Cotton', command=qu10out).pack(anchor='w')
            Radiobutton(self, text="Tobacco", variable=var10, value='Tobacco', command=qu10out).pack(anchor='w')
            ans10 = Label(self, text='')
            ans10.pack()

            buttonBack = Button(self, text="Back", command=lambda: controller.show_frame("PageNine"))
            buttonBack.pack(side=LEFT)
            buttonEnd = Button(self, text="Finish", command=self.quit)
            buttonEnd.pack(side=RIGHT)

    if __name__ == '__main__':
        quiz = SampleApp()
        quiz.mainloop()


game = Tk()
game.title('Jimmy Carter Peanut Game')
Instructions = Label(game, text='Jimmy Carter has dropped 10 peanuts. Help him pick them up. Keep the gap between \n'
                                'collecting peanuts under two seconds to keep up a streak of earning 2 points per \n'
                                'peanut from the moment the game launches. If you break your \n'
                                'streak then you will earn 1 point per peanut from then on.')
Instructions.pack()
Instructions.config(bg='navajo white', padx=34)
score = Label(game, text="Score: " + str(myCounter.__str__()), padx=270)
score.pack()
score.config(bg='CadetBlue2')
gameCanvas = Canvas(game, width=600, height=600, bg='PaleGreen3')
gameCanvas.pack()
frame = Frame(game)
frame.pack(side=BOTTOM)
but1 = Button(frame, text="Play Quiz", command=playQuiz)
but1.grid(row=1, column=1)
but2 = Button(frame, text="Quit Game", command=game.quit)
but2.grid(row=1, column=2)

x, y = randint(50, 550), randint(50, 550)
a, b = randint(50, 550), randint(50, 550)
c, d = randint(50, 550), randint(50, 550)
e, f = randint(50, 550), randint(50, 550)
g, h = randint(50, 550), randint(50, 550)

peanut1 = gameCanvas.create_oval(x - 10, y + 30, x + 30, y + 80, fill='DarkGoldenrod3', outline='DarkGoldenrod4')
peanut2 = gameCanvas.create_oval(a - 10, b + 30, a + 30, b + 80, fill='DarkGoldenrod3', outline='DarkGoldenrod4')
peanut3 = gameCanvas.create_oval(c - 10, d + 30, c + 30, d + 80, fill='DarkGoldenrod3', outline='DarkGoldenrod4')
peanut4 = gameCanvas.create_oval(e - 10, f + 30, e + 30, f + 80, fill='DarkGoldenrod3', outline='DarkGoldenrod4')
peanut5 = gameCanvas.create_oval(g - 10, h + 30, g + 30, h + 80, fill='DarkGoldenrod3', outline='DarkGoldenrod4')
peanut6 = gameCanvas.create_oval(y - 10, x + 30, y + 30, x + 80, fill='DarkGoldenrod3', outline='DarkGoldenrod4')
peanut7 = gameCanvas.create_oval(b - 10, a + 30, b + 30, a + 80, fill='DarkGoldenrod3', outline='DarkGoldenrod4')
peanut8 = gameCanvas.create_oval(d - 10, c + 30, d + 30, c + 80, fill='DarkGoldenrod3', outline='DarkGoldenrod4')
peanut9 = gameCanvas.create_oval(f - 10, e + 30, f + 30, e + 80, fill='DarkGoldenrod3', outline='DarkGoldenrod4')
peanut10 = gameCanvas.create_oval(h - 10, g + 30, h + 30, g + 80, fill='DarkGoldenrod3', outline='DarkGoldenrod4')

gameCanvas.tag_bind(peanut1, '<ButtonPress-1>', addToCounter1)
gameCanvas.tag_bind(peanut2, '<ButtonPress-1>', addToCounter2)
gameCanvas.tag_bind(peanut3, '<ButtonPress-1>', addToCounter3)
gameCanvas.tag_bind(peanut4, '<ButtonPress-1>', addToCounter4)
gameCanvas.tag_bind(peanut5, '<ButtonPress-1>', addToCounter5)
gameCanvas.tag_bind(peanut6, '<ButtonPress-1>', addToCounter6)
gameCanvas.tag_bind(peanut7, '<ButtonPress-1>', addToCounter7)
gameCanvas.tag_bind(peanut8, '<ButtonPress-1>', addToCounter8)
gameCanvas.tag_bind(peanut9, '<ButtonPress-1>', addToCounter9)
gameCanvas.tag_bind(peanut10, '<ButtonPress-1>', addToCounter10)

game.mainloop()
