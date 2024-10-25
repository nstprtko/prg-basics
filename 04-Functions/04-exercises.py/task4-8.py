def time_string(hours, minutes, time_format):
    if time_format == '24':
        # Format in 24-hour time as HH:MM
        return f"{hours:02}:{minutes:02}"
    elif time_format == '12':
        # Convert to 12-hour time
        period = "AM" if hours < 12 else "PM"
        hour_12 = hours % 12
        hour_12 = 12 if hour_12 == 0 else hour_12  # Adjust hour to be 12 instead of 0
        return f"{hour_12:02}:{minutes:02} {period}"
    else:
        return "Invalid format. Please use '24' or '12'."

# Test examples
print(time_string(14, 30, '24'))  # Output: 14:30
print(time_string(14, 30, '12'))  # Output: 02:30 PM