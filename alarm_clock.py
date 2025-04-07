from collections import namedtuple

# Define a namedtuple to store time input and result
AlarmTime = namedtuple('AlarmTime', ['current_hour', 'wait_hours', 'alarm_hour'])

# Get input from the user
current_hour = int(input("Enter the current time (0-23): "))
wait_hours = int(input("Enter how many hours to wait for the alarm: "))

# Calculate alarm time using modulo 24
alarm_hour = (current_hour + wait_hours) % 24

# Store values in namedtuple
alarm = AlarmTime(current_hour, wait_hours, alarm_hour)

# Prepare lines of content
lines = [
    f"⏰ Alarm Set!",
    f"Current: {alarm.current_hour:02d}:00",
    f"Wait:    {alarm.wait_hours} hrs",
    f"Alarm:   {alarm.alarm_hour:02d}:00"]

# Calculate the width of the box
max_len = max(len(line) for line in lines)
box_width = max_len + 4  # Padding for borders and spacing

# Print the dynamic box
print("\n " + "_" * (box_width - 2))
print("| " + lines[0].center(box_width - 4) + " |")
print("|" + "-" * (box_width - 2) + "|")

for line in lines[1:]:
    print("| " + line.ljust(box_width - 4) + " |")

print("|" + "_" * (box_width - 2) + "|")
