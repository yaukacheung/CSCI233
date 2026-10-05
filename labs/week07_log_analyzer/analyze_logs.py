# Lab 7: Log File Analyzer

# Counters for each message type
error_count = 0
warning_count = 0
info_count = 0

# List to store timestamps
timestamps = []

# Open and read the log file
with open("server.log", "r") as file:
    for line in file:
        line = line.strip()

        # Extract the timestamp
        timestamp = line[:19]
        timestamps.append(timestamp)

        # Count message types
        if "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "INFO" in line:
            info_count += 1

# Write the summary to a new file
with open("summary.txt", "w") as file:
    file.write("Log File Summary\n")
    file.write("================\n")
    file.write(f"ERROR messages: {error_count}\n")
    file.write(f"WARNING messages: {warning_count}\n")
    file.write(f"INFO messages: {info_count}\n")

    file.write("\nTimestamps:\n")
    for timestamp in timestamps:
        file.write(timestamp + "\n")

print("Log analysis complete!")
print("Summary written to summary.txt")
