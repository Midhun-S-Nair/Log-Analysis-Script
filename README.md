# **Log Analysis Script**

## **Overview**

This project contains a Python-based log analysis script designed to process web server log files and extract meaningful insights. The script performs the following analyses:  

1. **Count Requests per IP Address**: Identifies the total number of requests made by each IP address.
2. **Most Frequently Accessed Endpoint**: Detects the endpoint (e.g., `/home`, `/login`) accessed most frequently.
3. **Suspicious Activity Detection**: Flags IPs exceeding a threshold of failed login attempts, indicating potential brute force attacks.

The results are displayed in the terminal and saved in a CSV file for easy access and documentation.

---

## **Features**

- **Requests per IP Address**: Outputs the total number of requests sorted in descending order of frequency.  
- **Endpoint Analysis**: Identifies the most accessed endpoint along with its access count.  
- **Suspicious Activity Detection**: Detects suspicious IP addresses based on failed login attempts.  
- **CSV Output**: Saves the results to a structured CSV file named `log_analysis_results.csv`.  

---

## **Sample Output**

**Terminal Output**:

Requests per IP Address: 203.0.113.5 8 198.51.100.23 8 192.168.1.1 7 10.0.0.2 6 192.168.1.100 5

Most Frequently Accessed Endpoint: /login (Accessed 13 times)

Suspicious Activity Detected: IP Address Failed Login Attempts 203.0.113.5 8 192.168.1.100 5

Results saved to 'log_analysis_results.csv'


**CSV File Content**:  
- **Requests per IP**: Contains columns for `IP Address` and `Request Count`.  
- **Most Accessed Endpoint**: Contains columns for `Endpoint` and `Access Count`.  
- **Suspicious Activity**: Contains columns for `IP Address` and `Failed Login Count`.

---

## **Prerequisites**

1. **Python**: Ensure Python 3.7 or higher is installed.  
2. **Required Libraries**: Install the necessary Python libraries using the following command:
   ```bash
   pip install -r requirements.txt

   Usage
Clone the Repository:

bash
Copy code
git clone https://github.com/Midhun-S-Nair/Log-Analysis-Script.git
cd Log-Analysis-Script
Place the Log File:
Add your log file in the project directory (e.g., sample.log).

Run the Script:
Execute the script with the log file:

bash
Copy code
python log_analysis.py sample.log
View the Results:

Terminal: Displays the analysis results.
CSV: Results are saved in log_analysis_results.csv.

