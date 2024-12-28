from datetime import datetime

# Example datetime string
datetime_str = "2024-12-27 01:59:26.335530+00:00"

# Parse the datetime string
dt = datetime.fromisoformat(datetime_str)

# Convert to the desired format
formatted_date = dt.strftime("%dth %b %Y, %I:%M %p")

print(formatted_date)  # Output: 27th Dec 2024, 01:59 AM
