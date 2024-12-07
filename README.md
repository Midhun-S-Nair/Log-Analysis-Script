# Log Analysis Script

![Log Analysis Diagram](https://vrvsecurity.in/favicon.ico)

## Overview

This project contains a Python-based log analysis script designed to process web server log files and extract meaningful insights. The script performs the following analyses:

- Count Requests per IP Address: Identifies the total number of requests made by each IP address.
- Most Frequently Accessed Endpoint: Detects the endpoint (e.g., /home, /login) accessed most frequently.
- Suspicious Activity Detection: Flags IPs exceeding a threshold of failed login attempts, indicating potential brute force attacks.

The results are displayed in the terminal and saved in a CSV file for easy access and documentation.

## Features

- **Requests per IP Address**: Outputs the total number of requests sorted in descending order of frequency.
- **Endpoint Analysis**: Identifies the most accessed endpoint along with its access count.
- **Suspicious Activity Detection**: Detects suspicious IP addresses based on failed login attempts.
- **CSV Output**: Saves the results to a structured CSV file named log_analysis_results.csv.

## Sample Output

The script outputs the following in the terminal:

- Requests per IP address.
- Most frequently accessed endpoint.
- Detected suspicious activities based on failed login attempts.

Additionally, a CSV file (log_analysis_results.csv) is generated with the results.

## Usage

1. Clone the repository and navigate to the project directory.
2. Place your log file in the project directory.
3. Run the script to analyze the log file.
4. View the results in the terminal and in the log_analysis_results.csv file.

## Author

**Midhun S. Nair**  
[GitHub Profile](https://github.com/Midhun-S-Nair)

