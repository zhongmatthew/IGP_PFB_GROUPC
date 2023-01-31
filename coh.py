from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports\cash-on-hand.csv"
with fp.open(mode"r",enncoding = "UTF-8", newline = "") as file:
    reader = csv.reader(file)
    next(reader)
    cash_on_hand = []
    for row in reader:
        cash_on_hand.append(row)