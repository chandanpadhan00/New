import os
import glob
import csv

# Specify the directory where the CSV files are stored
directory_path = r"C:\Path\To\Your\CSVFolder"  # change this to your folder path

# List all CSV files in the specified directory
csv_files = glob.glob(os.path.join(directory_path, "*.csv"))

# Define the path for the combined output file
output_file = os.path.join(directory_path, "combined.csv")

# Open the combined file in write mode
with open(output_file, 'w', newline='', encoding='utf-8') as fout:
    writer = None
    for idx, csv_filename in enumerate(csv_files):
        with open(csv_filename, 'r', newline='', encoding='utf-8') as fin:
            reader = csv.reader(fin)
            # For the first file, write both header and data
            if idx == 0:
                writer = csv.writer(fout)
                for row in reader:
                    writer.writerow(row)
            else:
                # Skip the header in subsequent files, then write the data rows
                next(reader)
                for row in reader:
                    writer.writerow(row)
