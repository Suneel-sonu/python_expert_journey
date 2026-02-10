# Raw data: Temperatures in Celsius
celsius_temps = [0, 10, 20, 25, 30, 38]

# List Comprehension logic
fahrenheit_temps = [(t * 9/5) + 32 for t in celsius_temps]

print("--- Weather Data Analysis ---")
# Correct f-string: No quotes around the variable name inside the braces
print(f"Celsius:    {celsius_temps}")
print(f"Fahrenheit: {fahrenheit_temps}")