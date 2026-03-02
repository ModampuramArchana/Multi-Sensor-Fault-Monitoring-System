import random
import csv
import matplotlib.pyplot as plt

# User input
threshold = int(input("Enter Fault Threshold Value: "))

# Number of sensors & readings
num_sensors = 3
num_readings = 10

# Initialize sensor data dictionary
sensor_data = {}
for i in range(1, num_sensors + 1):
    sensor_data[f"Sensor_{i}"] = [random.randint(10, 100) for _ in range(num_readings)]

# Print readings
for sensor, readings in sensor_data.items():
    print(f"{sensor} Readings: {readings}")

# Fault detection & stats
for sensor, readings in sensor_data.items():
    fault_count = sum(1 for r in readings if r > threshold)
    fault_percentage = (fault_count / num_readings) * 100
    avg = sum(readings) / num_readings
    print(f"{sensor} -> Faults: {fault_count}, Fault%: {fault_percentage}%, Average: {avg}")

# Save CSV
with open("multi_sensor_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Reading No"] + [f"Sensor_{i}" for i in range(1, num_sensors+1)])
    for i in range(num_readings):
        row = [i+1] + [sensor_data[f"Sensor_{j}"][i] for j in range(1, num_sensors+1)]
        writer.writerow(row)

print("Data saved to multi_sensor_data.csv")

# Graph plot
for sensor, readings in sensor_data.items():
    plt.plot(readings, marker='o', label=sensor)

# Threshold line
plt.axhline(y=threshold, color='red', linestyle='--', label=f"Threshold = {threshold}")
plt.title("Multi-Sensor Readings")
plt.xlabel("Reading Number")
plt.ylabel("Sensor Value")
plt.grid(True)
plt.legend()
plt.show()