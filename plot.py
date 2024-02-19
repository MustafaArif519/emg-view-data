from datetime import datetime, timedelta
import matplotlib.pyplot as plt

timestamps = []
signal_value = []

# Open the file and read line by line
previous_timestamp = None
starting_timestamp = None
with open('data/emg.out', 'r') as file:
    for line in file:
        # Split the line into timestamp and integer
        parts = line.split(' -> ')
        timestamp = datetime.strptime(parts[0], "%H:%M:%S.%f")
        if starting_timestamp is None:
            starting_timestamp = timestamp

        if len(parts) == 2:
            # Append the timestamp and integer to their respective lists
            if timestamp == previous_timestamp:
                incremented_timestamp = previous_timestamp + timedelta(milliseconds=1)
                elapsed_time = incremented_timestamp - starting_timestamp
                timestamps.append(elapsed_time.total_seconds())  # Convert timedelta to seconds
                previous_timestamp = incremented_timestamp
            else:
                elapsed_time = timestamp - starting_timestamp
                timestamps.append(elapsed_time.total_seconds())  # Convert timedelta to seconds
                previous_timestamp = timestamp
            signal_value.append(int(parts[1]))

# Plot the data
plt.plot(timestamps, signal_value)
plt.xlabel('Elapsed Time (seconds)')
plt.ylabel('Signal Value')
plt.xticks(rotation=45)
plt.savefig('output.png')