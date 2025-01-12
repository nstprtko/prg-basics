import matplotlib.pyplot as plt

# Data: Temperatures recorded at different stations
temperatures = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# Extract city names and temperatures using map()
cities = list(map(lambda x: x, temperatures.keys()))
temp_values = list(map(lambda x: x, temperatures.values()))

# Create the bar chart
plt.bar(cities, temp_values, color='skyblue')

# Add title and labels
plt.title("Temperatures Recorded in Cities")
plt.xlabel("Cities")
plt.ylabel("Temperature (°C)")

# Show the chart
plt.show()