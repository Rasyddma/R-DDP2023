import tkinter as tk
import tkinter.messagebox
import time


class Application(tk.Frame): 
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.running = False
        self.time = 0
        self.hour = 0
        self.min = 0
        self.sec = 0
        self.hours = 0
        self.mins = 0
        self.secs = 0
        self.build_interface()

    def build_interface(self):

        self.hour = tk.Label(self, text="Hour : ", font=("Courier", 10), width=8)
        self.hour.grid(row=0, column=0, stick="S")

        self.h_entry = tk.Entry(self)
        self.h_entry.grid(row=0, column=1)

        self.min = tk.Label(self, text="Min : ", font=("Courier", 10), width=8)
        self.min.grid(row=1, column=0, stick="S")

        self.m_entry = tk.Entry(self)
        self.m_entry.grid(row=1, column=1)

        self.sec = tk.Label(self, text="Sec : ", font=("Courier", 10), width=8)
        self.sec.grid(row=2, column=0, stick="S")

        self.s_entry = tk.Entry(self)
        self.s_entry.grid(row=2, column=1)

        self.clock = tk.Label(self, text="00:00:00", font=("Courier", 20), width=10)
        self.clock.grid(row=3, column=1, stick="S")

        self.time_label = tk.Label(self, text="hour   min   sec", font=("Courier", 10), width=20)
        self.time_label.grid(row=4, column=1, sticky="N")

        self.power_button = tk.Button(self, text="Start", command=lambda: self.start())
        self.power_button.grid(row=5, column=0,padx=20,pady=10)

        self.reset_button = tk.Button(self, text="Reset", command=lambda: self.reset())
        self.reset_button.grid(row=5, column=1,padx=20,pady=10)

        self.quit_button = tk.Button(self, text="Quit", command=lambda: self.quit())
        self.quit_button.grid(row=5, column=2,padx=20,pady=10)

        self.pause_button = tk.Button(self, text="Pause", command=lambda: self.pause())
        self.pause_button.grid(row=5, column=3,padx=30,pady=10,sticky="E")

        self.master.bind("<Return>", lambda x: self.start())

    def calculate(self):
        #used to calculate time and return in formatted style
        self.hours = self.time // 3600
        self.mins = (self.time // 60) % 60
        self.secs = self.time % 60
        s = "{:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs)
        return s

    def update(self):
        #used to update the clock text
        self.hours = int(self.h_entry.get())
        self.mins = int(self.m_entry.get())
        self.secs = int(self.s_entry.get())
        try:
            self.clock.configure(text=self.calculate())
        except:
            self.clock.configure(text="00:00:00")

    def timer(self):
        #used to check whether time is left and calls calculate to update time left value
        if self.running:
            if self.time <= 0:
                self.clock.configure(text="Time's up!")
            else:
                self.clock.configure(text=self.calculate())
                self.time = self.time - 1
            self.after(1000,self.timer)        

    def start(self):
        #used to initiate timer by calling timer function
        try:
            if self.h_entry.get():
                self.hours = int(self.h_entry.get())
            else:
                self.hours = 0

            if self.m_entry.get():
                self.mins = int(self.m_entry.get())
            else:
                self.mins = 0

            if self.s_entry.get():
                self.secs = int(self.s_entry.get())
            else:
                self.secs = 0

            self.time = (self.hours*3600) + (self.mins*60) + self.secs
            self.hour.delete(0, 'end')
            self.min.delete(0, 'end')
            self.sec.delete(0, 'end')
        except:
            self.hours = self.hours
            self.mins = self.mins
            self.secs = self.secs
        self.power_button.configure(text="Stop", command=lambda: self.stop())
        self.master.bind("<Return>", lambda x: self.stop())
        self.running = True
        self.timer()

    def stop(self):
        #used to stop timer
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False

    def reset(self):
        #used to reset all fields and clock value to 0
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False
        self.h_entry.delete(0,'end')
        self.m_entry.delete(0,'end')
        self.s_entry.delete(0,'end')
        self.clock["text"] = "00:00:00"

    def quit(self):
        #used to quit the timer
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    def pause(self):
        #used to pause the timer
        self.pause_button.configure(text="Resume", command=lambda: self.resume())
        self.master.bind("<Return>", lambda x: self.resume())
        if self.running == True:
            self.running = False
        self.timer()


    def resume(self):
        #used to resume the timer
        self.pause_button.configure(text="Pause", command=lambda: self.pause())
        self.master.bind("<Return>", lambda x: self.pause())
        if self.running == False:
            self.running = True
        self.timer()


if __name__ == "__main__":
    """Main loop of timer"""
    root = tk.Tk()
    root.title("TIMER")
    Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()