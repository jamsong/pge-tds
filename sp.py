# Program to read PGE CSV file to output daily time of day energy using and calculate savings
# Copyright 2024 James Song
# 2024/01/29

import csv

# Open File
with open('pgn_electric_usage_interval_data_4540771060_1_2023-01-01_to_2023-12-31.csv') as file_obj:
	reader_obj = csv.reader(file_obj)

	for row in reader_obj:
		print(row)
