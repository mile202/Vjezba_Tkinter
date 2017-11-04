"""
mainloop() - Loop koji pokrece Tkinter. Ovaj loop radi u nedogled.

Frame - Nevidljivi okvir u koji stavljamo stvari.

Label - Dio u koji stavljamo tekst.

Button - Za stvaranje gumba

StringVar - Varijabla koja sadrzi string.

IntVar - Varijabla koja sadrzi integer.

trace() - Nacin da se prate promjene i pristupi varijablama.

columnconfigure() i rowconfigure() - Metode za konfiguraciju broja redova i stupaca

pack() - Metoda za ubacivanje widgeta u prostor.

grid() - Jos jedna metoda za ubacivanje stvari u frame, samo sto nam ova metoda dozvoljava ubacivanje na odredeno mjesto ( stupac ili red)

fill - opcija omogucuje da orjenitramo predmet NPR: fill='news'.
sticky - opcija omogucuje da predmet ostane na mjestu prilikom resize prozora



"""



import Tkinter

import tkMessageBox

DEFAULT_GAP = 60 * 25
#==== DEFAULT_GAP = 5 ==== Test sto ce se desiti kada timer dode do kraja!!====

class vjezba_2:  # ==== Definira Class ====
    def __init__(self, master): #==== Glavna definicija programa ====
        self.master = master
        self.mainframe = Tkinter.Frame(self.master, bg="white")
        self.mainframe.pack(fill=Tkinter.BOTH, expand=True)

        self.timer_text = Tkinter.StringVar()
        self.timer_text.trace('w', self.build_timer)
        self.time_left = Tkinter.IntVar()
        self.time_left.set(DEFAULT_GAP)
        self.time_left.trace('w', self.alert)
        self.running = False

        self.bulid_grid()
        self.build_banner()
        self.build_buttons()
        self.build_timer()

        self.update()

    def bulid_grid(self):  #=======Definira grid ====
        self.mainframe.columnconfigure(0, weight=1) #==== Definira kolonu u gridu ====
        self.mainframe.rowconfigure(0, weight=0)    #==== Definira redove u gridu ====
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)

    def build_banner(self):  #==== Definicija bannera ===
        banner = Tkinter.Label(
            self.mainframe,
            background='black',
            text='TIMER - VJEZBA',
            foreground='white',
            font=('Helvetica', 24)
        )

        banner.grid(   #==== Postavljanje na mjesto u gridu ======
            row=0, column=0,
            sticky='ew',
            padx=10, pady=10
        )

    def build_buttons(self):
        buttons_frame = Tkinter.Frame(self.mainframe) # ==== izrada novog grida koji kaze da je Tkinter.Frame unutar ili glavnog okvira(self.mainframe)
        buttons_frame.grid(row=2, column=0, sticky='nsew',padx=10,pady=10)
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        self.start_button = Tkinter.Button(
            buttons_frame,
            text='Start',
            command=self.start_timer
        )

        self.stop_button = Tkinter.Button(
            buttons_frame,
            text='Stop',
            command=self.stop_timer
        )

        self.start_button.grid(row=0, column=0, sticky='ew')
        self.stop_button.grid(row=0, column=1, sticky='ew')
        self.stop_button.config(state=Tkinter.DISABLED)

    def build_timer(self, *args):
        timer = Tkinter.Label(
            self.mainframe,
            text=self.timer_text.get(),
            font=('Helvetica', 36)
        )

        timer.grid(row=1, column=0, sticky='nsew')

    def start_timer(self):
        self.time_left.set(DEFAULT_GAP)
        self.running = True
        self.stop_button.config(state=Tkinter.NORMAL)
        self.start_button.config(state=Tkinter.DISABLED)


    def stop_timer(self):
        self.running = False
        self.stop_button.config(state=Tkinter.DISABLED)
        self.start_button.config(state=Tkinter.NORMAL)

    def alert(self, *args): #==== Definira ALERT poruku nakon sto vrijeme istekne ====
        if not self.time_left.get():
            tkMessageBox.showinfo('Timer Gotov!', 'Vase vrijeme je isteklo!')


    def minutes_seconds(self, seconds):
        return int(seconds/60), int(seconds%60)

    def update(self):
        time_left = self.time_left.get()

        if self.running and time_left:
            minutes, seconds = self.minutes_seconds(time_left)
            self.timer_text.set(
                '{:0>2}:{:0>2}'.format(minutes, seconds)
            )
            self.time_left.set(time_left-1)
        else:
            minutes, seconds = self.minutes_seconds(DEFAULT_GAP)
            self.timer_text.set(
                '{:0>2}:{:0>2}'.format(minutes, seconds)
            )
            self.stop_timer()
        self.master.after(1000, self.update)

if __name__ == '__main__':
    root = Tkinter.Tk()
    vjezba_2(root)
    root.mainloop()