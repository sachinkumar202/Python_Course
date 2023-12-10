import tkinter as tk
from datetime import datetime

def update_clock():
    current_time = datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")

# Create a label to display the clock
clock_label = tk.Label(window, font=("Arial", 80), fg="black")
clock_label.pack(padx=20, pady=20)

# Start the clock
update_clock()

# Run the application
window.mainloop()
