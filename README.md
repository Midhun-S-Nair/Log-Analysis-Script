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
