import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# --- Logic Functions ---

def scan_port(ip, port, display_area):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            output = f"[+] Port {port}: OPEN\n"
            display_area.insert(tk.END, output)
            # Log to file
            with open("scan_results.txt", "a") as f:
                f.write(f"{datetime.now()} - {ip} - Port {port} is OPEN\n")
        
        sock.close()
    except:
        pass

def start_scan():
    target = entry_target.get()
    try:
        target_ip = socket.gethostbyname(target)
        txt_display.insert(tk.END, f"Starting scan on {target_ip}...\n")
        
        # Scan standard ports 1-1024
        for port in range(1, 1025):
            t = threading.Thread(target=scan_port, args=(target_ip, port, txt_display))
            t.start()
    except Exception as e:
        txt_display.insert(tk.END, f"Error: {e}\n")

# --- GUI Setup ---

root = tk.Tk()
root.title("Python Ultra Port Scanner")
root.geometry("500x400")

# Input for Hostname/IP
tk.Label(root, text="Enter Target (IP or Hostname):").pack(pady=5)
entry_target = tk.Entry(root, width=40)
entry_target.pack(pady=5)

# Scan Button
btn_scan = tk.Button(root, text="Start Scan", command=start_scan, bg="green", fg="white")
btn_scan.pack(pady=10)

# Display Area
txt_display = scrolledtext.ScrolledText(root, width=60, height=15)
txt_display.pack(pady=10)

root.mainloop()