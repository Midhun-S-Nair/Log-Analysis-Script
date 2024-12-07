import re
from collections import Counter, defaultdict
import csv

# Function to parse logs
def parse_logs(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
    return logs

# Function to count requests per IP
def count_requests_per_ip(logs):
    ip_pattern = r'^\d+\.\d+\.\d+\.\d+'
    ip_counts = Counter()

    for log in logs:
        match = re.match(ip_pattern, log)
        if match:
            ip_address = match.group()
            ip_counts[ip_address] += 1

    return ip_counts

# Function to find the most frequently accessed endpoint
def find_most_accessed_endpoint(logs):
    endpoint_pattern = r'\"[A-Z]+\s(/[\w/]+)\sHTTP'
    endpoint_counts = Counter()

    for log in logs:
        match = re.search(endpoint_pattern, log)
        if match:
            endpoint = match.group(1)
            endpoint_counts[endpoint] += 1

    most_accessed = endpoint_counts.most_common(1)
    return most_accessed[0] if most_accessed else None

# Function to detect suspicious activity
def detect_suspicious_activity(logs, threshold=5):
    failed_login_counts = defaultdict(int)

    for log in logs:
        # Check for '401' or 'Invalid credentials'
        if '401' in log or 'Invalid credentials' in log:
            ip_pattern = r'^\d+\.\d+\.\d+\.\d+'
            match = re.match(ip_pattern, log)
            if match:
                ip_address = match.group()
                failed_login_counts[ip_address] += 1

    # Filter IPs exceeding the threshold
    suspicious_ips = [(ip, count) for ip, count in failed_login_counts.items() if count >= threshold]

    return suspicious_ips

# Main function
def main():
    # File path for the log file
    file_path = 'sample.log'

    # Parse the logs
    logs = parse_logs(file_path)

    # 1. Count requests per IP
    ip_counts = count_requests_per_ip(logs)
    print("Requests per IP Address:")
    for ip, count in ip_counts.most_common():
        print(f"{ip:<20}{count}")

    # 2. Find the most frequently accessed endpoint
    most_accessed_endpoint = find_most_accessed_endpoint(logs)
    if most_accessed_endpoint:
        endpoint, count = most_accessed_endpoint
        print(f"\nMost Frequently Accessed Endpoint:\n{endpoint} (Accessed {count} times)")
    else:
        print("\nNo endpoints found in the log.")

    # 3. Detect suspicious activity
    suspicious_ips = detect_suspicious_activity(logs)
    if suspicious_ips:
        print("\nSuspicious Activity Detected:")
        print(f"{'IP Address':<20}{'Failed Login Attempts':<10}")
        for ip, count in suspicious_ips:
            print(f"{ip:<20}{count:<10}")
    else:
        print("\nNo suspicious activity detected.")

    # 4. Save results to CSV
    with open('log_analysis_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Header for Requests per IP
        writer.writerow(['IP Address', 'Request Count'])
        for ip, count in ip_counts.most_common():
            writer.writerow([ip, count])

        # Header for Most Accessed Endpoint
        writer.writerow([])
        writer.writerow(['Endpoint', 'Access Count'])
        if most_accessed_endpoint:
            writer.writerow([endpoint, count])

        # Header for Suspicious Activity
        writer.writerow([])
        writer.writerow(['IP Address', 'Failed Login Count'])
        for ip, count in suspicious_ips:
            writer.writerow([ip, count])

    print("\nResults saved to 'log_analysis_results.csv'")

# Run the script
if __name__ == "__main__":
    main()
