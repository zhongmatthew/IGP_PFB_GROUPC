def overheads():
    from pathlib import Path
    import csv
    
    fp = Path.cwd()/"csv_reports\overheads.csv"
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        overheads = []
        
        for row in reader:
            overheads.append(row)
    
    percentage_list = []

    for headings, percentage in overheads:
        percentage_list.append(float(percentage))

    for heading, percentage in overheads:
        if float(percentage) == max(percentage_list):
            with open("Summary_Report.txt", mode = "a", encoding="UTF-8") as file:
                file.write(f"[HIGHEST OVERHEADS] {headings}: {percentage}%\n")

overheads()
