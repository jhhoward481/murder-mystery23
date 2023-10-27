import os

# Get the current directory
current_directory = os.getcwd()

# Output file name
output_file = "names.txt"

# Iterate over markdown files in the current directory
for filename in os.listdir(current_directory):
    if filename.endswith(".md"):
        with open(filename, "r") as input_file:
            lines = input_file.readlines()
            found_name = False
            with open(output_file, "a") as output_file_obj:
                for line in lines:
                    if found_name:
                        output_file_obj.write(line)
                        break  # Stop after writing the line following "Name:"
                    if "Name:" in line:
                        found_name = True
