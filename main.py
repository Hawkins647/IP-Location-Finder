import tkinter as tk
import geocoder

root = tk.Tk()
root.title("IP Tracker")
root.geometry("400x400")
root.resizable(0, 0)
root.config(bg="black")


def process_ip(passed_ip: str):
    """Take in an ip and display information on a tkinter label widget"""
    global final_label

    ip_info = geocoder.ip(passed_ip)
    final_label.config(text="City: " + ip_info.city + "\nLatitude: " + str(ip_info.latlng[0]) + "\nLongitude: " + str(ip_info.latlng[1]))


title_frame = tk.Frame(root, bg="black")
title_frame.pack()
main_frame = tk.Frame(root, bg="black")
main_frame.pack(pady=10)

tk.Label(title_frame, text="IP Tracker", font=("Terminal", 28), bg="black", fg="green").pack(padx=2, pady=2)

tk.Label(main_frame, text="Enter IP:", font=("Terminal", 22), bg="black", fg="green").grid(row=0, column=0, pady=5)

ip_entry = tk.Entry(main_frame, font=("Terminal", 20), bg="black", fg="green", width=25)
ip_entry.grid(row=1, column=0, pady=5)

confirm_button = tk.Button(main_frame, text="Search", font=("Terminal", 23), bg="black", fg="green", activebackground="green", command=lambda: process_ip(ip_entry.get()))
confirm_button.grid(row=2, column=0, pady=10)

final_label = tk.Label(main_frame, text="", font=("Terminal", 20), bg="black", fg="green")
final_label.grid(row=3, column=0, pady=10)

tk.Label(root, text="DO NOT USE FOR MALICIOUS PURPOSES", font=("Terminal", 20), bg="black", fg="green").pack(side=tk.BOTTOM)

root.mainloop()

