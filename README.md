Log Monitoring and Alert System
📌 Project Description

The Log Monitoring and Alert System is a Python-based project that continuously monitors a log file for error messages.

The system uses Regular Expressions (Regex) to identify ERROR patterns. When the number of detected errors reaches a configurable threshold, the system generates an alert and stores the alert information in a separate log file.

This project is useful for learning file handling, pattern matching, logging, and automation in Python.

🎯 Objectives
Monitor a log file continuously.
Detect error messages automatically.
Use Regex for pattern matching.
Configure an error threshold.
Generate alerts when the threshold is reached.
Store alert information in alerts.log.
Process only newly added log entries instead of repeatedly reading the entire file.
🛠️ Technologies Used
Python 3
Regular Expressions (re)
File Handling
Logging
Time Module
📂 Project Structure
log_monitoring_system/
│
├── monitor.py
├── app.log
├── alerts.log
└── README.md
Files Description
File	Description
monitor.py	Main log monitoring program
app.log	Application log file being monitored
alerts.log	Stores generated alerts
README.md	Project documentation
⚙️ Features
1. Continuous Log Monitoring

The program continuously watches the app.log file for new entries.

2. Error Detection

Regex is used to detect the ERROR keyword.

Example:

2026-09-10 10:02:20 ERROR Database connection failed
3. Configurable Threshold

The error threshold can easily be changed:

ERROR_THRESHOLD = 3

For example:

ERROR_THRESHOLD = 5

will generate an alert after 5 errors.

4. Alert Generation

When the threshold is reached:

ALERT: Error threshold crossed! Total errors detected: 3
5. Alert Logging

Alerts are saved inside:

alerts.log
🚀 Installation
Step 1: Install Python

Make sure Python 3 is installed.

Check the version:

python --version

or:

python3 --version
Step 2: Clone the Repository
git clone https://github.com/yourusername/log-monitoring-system.git

Move into the project folder:

cd log-monitoring-system
▶️ How to Run

Run the Python program:

python monitor.py

Output:

Log monitoring started...
Press CTRL+C to stop.
🧪 Testing the Project

While the program is running, add new errors to app.log:

2026-09-10 15:10:01 ERROR Server connection failed
2026-09-10 15:10:02 ERROR Database unavailable
2026-09-10 15:10:03 ERROR Authentication failed

The program detects the errors:

Error detected:
2026-09-10 15:10:01 ERROR Server connection failed

Error detected:
2026-09-10 15:10:02 ERROR Database unavailable

Error detected:
2026-09-10 15:10:03 ERROR Authentication failed

ALERT: Error threshold crossed! Total errors detected: 3
📊 Sample Alert Evidence

The alerts.log file may contain:

2026-09-10 15:15:20,123 - WARNING - ALERT: Error threshold crossed! Total errors detected: 3
🔄 Project Workflow
        app.log
           │
           ▼
   Read new log entries
           │
           ▼
      Regex Matching
           │
           ▼
     Detect ERROR
           │
           ▼
     Count Errors
           │
           ▼
   Threshold Reached?
       /         \
     No           Yes
     │             │
     ▼             ▼
 Continue       Generate
                 Alert
                   │
                   ▼
              alerts.log
💡 Key Python Concepts Learned

This project helps practice:

open() and file handling
readline()
seek()
while loops
Functions
Exception handling
Regular expressions
logging
Configuration variables
Continuous monitoring
Automation
🔮 Future Improvements

The project can be extended with:

📧 Email alerts
📱 SMS notifications
💬 Telegram alerts
📊 Web dashboard
🗄️ Database storage
🔔 Multiple error levels
📈 Error statistics
⚙️ Configuration file
🐳 Docker deployment
👨‍💻 Author

⭐ Conclusion

The Log Monitoring and Alert System is a beginner-friendly Python automation project that demonstrates how real-world applications can monitor logs, identify errors, and automatically generate alerts when problems occur.

If you found this project useful, consider giving the repository a ⭐ on GitHub.