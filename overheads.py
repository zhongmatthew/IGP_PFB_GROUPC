# use "def" to create a overhead function 
def overhead():
    """
    - Function will determine the highest overhead
    """
    # import Path from pathlib and csv module
    from pathlib import Path
    import csv
    
    # locate the csv file by creating a file path
    fp = Path.cwd()/"csv_reports\overheads.csv"

    # use "open()" to read the file
    # "r" in mode parameter means read
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        # create an empty list to store the data from csv file
        overheads = []
        
        # use "for" loop over a list to append data from csv file
        for row in reader:
            overheads.append(row)
    
    # create an empty list to store percentages of overheads
    percentage_list = []

    # use "for" loop with 2 entities to iterate over nested list
    for heading, percentage in overheads:
        # append only percentage data into list
        percentage_list.append(float(percentage))

    # use "for" loop again to iterate over nested list
    for heading, percentage in overheads:

        # use "if" to find the highest overhead percentage
        if float(percentage) == max(percentage_list):

            # create a new .txt file to store summary report, "w" in mode parameter means write
            with open("Summary_Report.txt", mode = "w", encoding = "UTF-8") as file:
                # write the text in summary report using "f string"
                # two entity variable stores the highest overhead and respective percentage
                file.write(f"[HIGHEST OVERHEADS] {heading}: {percentage}%\n")

# ----------------- Base solution ----------------- #
# def overhead():
#     """
#     - Function will determine the highest overhead
#     """
#     from pathlib import Path
#     import csv
    
#     fp = Path.cwd()/"csv_reports\overheads.csv"

#     with fp.open(mode="r", encoding="UTF-8", newline="") as file:
#         reader = csv.reader(file)
#         next(reader)

#         overheads = []
        
#         for row in reader:
#             overheads.append(row)
    
#     percentage_list = []

#     for heading, percentage in overheads:
#         percentage_list.append(float(percentage))

#     for heading, percentage in overheads:
#         if float(percentage) == max(percentage_list):
#             with open("Summary_Report.txt", mode = "w", encoding = "UTF-8") as file:
#                 file.write(f"[HIGHEST OVERHEADS] {heading}: {percentage}%\n")

print("Hello world")
