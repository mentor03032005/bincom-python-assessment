
import os
import re
from bs4 import BeautifulSoup
from collections import Counter
import statistics
import psycopg2
import random

def extract_colours_from_html(file_path="python_class_question.html"):

    if not os.path.exists(file_path):
        print("HTML file not found!")
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")

    all_colours = []

    rows = soup.find_all("tr")

    for row in rows:
        cells = row.find_all("td")

        if len(cells) >= 2:
            raw_text = cells[1].get_text(strip=True)

            colours = re.findall(r"[A-Z]+", raw_text.upper())

            all_colours.extend(colours)

    return all_colours

# Extract colours from HTML
colours = extract_colours_from_html()

# Count colour frequencies
freq_counts = Counter(colours)

# Arrange colours alphabetically
unique_colours = sorted(freq_counts.keys())

# Assign a number to each colour
colour_to_num = {
    colour: index
    for index, colour in enumerate(unique_colours)
}

# Convert colours into numbers, preserving frequencies
encoded_values = [
    colour_to_num[colour] for colour in colours
]

# Calculate the mean
mean_value = statistics.mean(encoded_values)

# Find the nearest colour index
mean_colour = unique_colours[round(mean_value)]

print("Total colours:", len(colours))
print("Mean numerical value:", round(mean_value, 2))
print("Mean colour:", mean_colour)
# Calculate population variance
variance_value = statistics.pvariance(encoded_values)

print("Variance:", round(variance_value, 2))
# Calculate probability of choosing RED
red_count = freq_counts["RED"]

red_probability = red_count / len(colours)

print("RED probability:", round(red_probability, 4))
print("RED percentage:", round(red_probability * 100, 2), "%")
# Find the most frequently worn colour
mode_colour = freq_counts.most_common(1)[0]

print("Most worn colour:", mode_colour[0])
print("Times worn:", mode_colour[1])
# Calculate the median colour
sorted_colours = sorted(colours)

median_colour = sorted_colours[len(sorted_colours) // 2]

print("Median colour:", median_colour)
def save_colours_to_database(freq_counts):
    # Save colour frequencies to PostgreSQL
    connection = psycopg2.connect(
        host="localhost",
        database="bincom_assesment",
        user="postgres",
        password="693698afam",
        port="5432"
    )

    cursor = connection.cursor()

    for colour, frequency in freq_counts.items():
        cursor.execute(
            """
            INSERT INTO colour_frequencies (colour, frequency)
            VALUES (%s, %s)
            ON CONFLICT (colour)
            DO UPDATE SET frequency = EXCLUDED.frequency;
            """,
            (colour, frequency)
        )

    connection.commit()
    cursor.close()
    connection.close()

    print("Colours successfully saved to PostgreSQL!")
    # Save colour frequencies to PostgreSQL
save_colours_to_database(freq_counts)
# Recursive search function
def recursive_search(numbers, target, index=0):
    if index >= len(numbers):
        return False

    if numbers[index] == target:
        return True

    return recursive_search(numbers, target, index + 1)
# Ask the user for a number to search
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

target = int(input("Enter a number to search for: "))

result = recursive_search(numbers, target)

if result:
    print("Number found!")
else:
    print("Number not found!")
# Generate a random 4-digit binary number
binary_number = ''.join(random.choice('01') for _ in range(4))

# Convert binary number to base 10
decimal_number = int(binary_number, 2)

print("Random binary number:", binary_number)
print("Base 10 number:", decimal_number)
# Calculate the sum of the first 50 Fibonacci numbers
def fibonacci_sum(n):
    a = 0
    b = 1
    total = 0

    for i in range(n):
        total += a
        a, b = b, a + b

    return total

print("Sum of first 50 Fibonacci numbers:", fibonacci_sum(50))