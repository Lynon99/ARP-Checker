import subprocess
import tkinter as tk
from tkinter import messagebox

def check_arp_table():
    try:
        arp_output = subprocess.check_output(['arp', '-a'])
        arp_lines = arp_output.decode().splitlines()

        arp_entries = []
        for line in arp_lines[3:-1]:
            fields = line.split()
            if len(fields) == 3:
                # Handles ARP table entry with three fields (Windows format)
                ip_address, mac_address, _ = fields
                arp_entries.append({'IP Address': ip_address, 'MAC Address': mac_address})
            elif len(fields) == 4:
                # Handles ARP table entry with four fields (Linux format)
                _, ip_address, _, mac_address = fields
                arp_entries.append({'IP Address': ip_address, 'MAC Address': mac_address})
            else:
                print(f"Warning: Unexpected ARP table line format: {line}")

        return arp_entries

    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve ARP table.")
        return []

def show_arp_table():
    arp_table = check_arp_table()
    arp_info = '\n'.join(f"{entry['IP Address']} : {entry['MAC Address']})" for entry in arp_table)
    messagebox.showinfo("ARP Table", arp_info)



if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(True,True)
    root.geometry('300x150')
    root.title("ARP Table Viewer")
    root.configure(bg="red")
    

    button = tk.Button(root, text="Show ARP Table", command=show_arp_table, width=15, height=3)
    button.pack(anchor='center', side='top', pady='50')
    

    root.mainloop()

