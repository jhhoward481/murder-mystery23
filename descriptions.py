import os
import csv

# Get the current directory
current_directory = os.getcwd()

# Output CSV file name
output_csv = "output.csv"

# Initialize a list to store extracted text
extracted_texts = []

# Iterate over markdown files in the current directory
for filename in os.listdir(current_directory):
    if filename.endswith(".md"):
        with open(filename, "r") as input_file:
            lines = input_file.readlines()
            description_text = None
            found_description = False
            for line in lines:
                if found_description:
                    # Extract text after "Description"
                    description_text = line.strip()
                    extracted_texts.append(description_text)
                if "Description" in line:
                    found_description = True

# Write extracted texts to CSV file
with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Description"])  # Header row
    for text in extracted_texts:
        csv_writer.writerow([text])

print(f"Extracted text from {len(extracted_texts)} files and saved to {output_csv}.")
