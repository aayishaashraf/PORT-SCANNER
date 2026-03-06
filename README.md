Here is the complete, professional content for your README.md file. You can copy this text and save it as a file named README.md in your project folder.

🚀 Python Multi-Threaded Port Scanner
A high-performance TCP Port Scanner built with Python. This tool features a Graphical User Interface (GUI), multi-threading for rapid scanning, and automatic results logging.

📋 Table of Contents
Features

How It Works

Installation

Usage

Technical Details

Security Warning

✨ Features
Speed: Uses Multi-threading to scan 1,024 ports in seconds (approx. 50x faster than sequential scanning).

GUI: User-friendly interface built with Tkinter.

DNS Resolution: Automatically converts hostnames (e.g., google.com) to IP addresses.

Persistent Logging: Automatically generates a scan_results.txt file to store all discovered open ports with timestamps.

Real-time Updates: A scrolled text area provides live feedback as open ports are found.

⚙️ How It Works
The scanner uses Socket Programming to attempt a connection to a specific IP and Port.

It initializes a TCP socket.

It attempts a connect_ex handshake.

If the return code is 0, the port is identified as Open.

To avoid waiting on closed ports, a timeout of 0.5 seconds is applied to each attempt.

🚀 Installation
Clone the Repository:

Bash
git clone https://github.com/your-username/port-scanner.git
cd port-scanner
Prerequisites:
Ensure you have Python 3.x installed. No external pip packages are required as it uses standard libraries.

🛠️ Usage
Run the application from your terminal:

Bash
python scanner.py
Enter a Target IP (e.g., 127.0.0.1) or a Hostname (e.g., scanme.nmap.org).

Click "Launch Port Scan".

Check the scan_results.txt file in the same directory for the saved log.

🔍 Technical Details
Language: Python 3.10+

Concurrency: threading module

Networking: socket module

UI: tkinter (Standard Python GUI Library)

⚠️ Security Warning
Educational Purposes Only.
Port scanning can be interpreted as a malicious act by Internet Service Providers (ISPs) and network administrators. Only scan devices and networks that you own or have explicit, written permission to test. The author is not responsible for any misuse of this software.