# use "def" to create a cash on hand function
def coh():
    """
    - Function will check each day whether there is a cash surplus or deficit
    - Function will calculate the deficit amount if there is any
    """
    # import Path from pathlib and csv module
    from pathlib import Path
    import csv

    # locate the csv file by creating a file path
    fp = Path.cwd()/"csv_reports\cash-on-hand.csv"

    # use "open()" to read the file
    # "r" in mode parameter means read
    with fp.open(mode = "r", encoding = "UTF-8", newline = "") as file:
        reader = csv.reader(file)
        next(reader)

        # create an empty list to store data from csv file
        cash_on_hand = []

        # use a "for" loop to iterate over loop to append data from csv file
        for row in reader:
            cash_on_hand.append(row)

        # create a variable "cash" to store base cash on hand (previous day)
        cash = cash_on_hand[0][1] # use string slicing to retrieve data

        # create an empty list to store the days that a cash deficit occurs
        deficit_list = []

        # use "for" loop with 2 entities to iterate over nested list
        for day, current_cash in cash_on_hand:
            
            # use "if" to check if cash on hand is lower than the previous day
            if current_cash < cash :

                # append the day number and deficit amount into the list
                deficit_list.append([day,int(cash) - int(current_cash)])

            # update the base cash with the current day's cash on hand
            cash = current_cash

        # create a new .txt file to store summary report, "a" in mode parameter means append
        with open("Summary_Report.txt", mode = "a", encoding = "UTF-8") as file:

            # use "if not" to check if the deficit list is empty
            if not deficit_list:
                # write the text in summary report if list is empty
                file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
            
            # shows that list is not empty which means there are days where cash on hand deficit occurs
            else:
                # use "for" loop again to iterate over nested list
                for day, deficit in deficit_list:
                    # write the text in summary report using "f string"
                    # two entity variable stores the day number and respective deficit amount
                    file.write(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{deficit}\n")

# ----------------- Base solution ----------------- #
# def coh():
#     """
#     - Function will check each day whether there is a cash surplus or deficit
#     - Function will calculate the deficit amount if there is any
#     """
#     from pathlib import Path
#     import csv

#     fp = Path.cwd()/"csv_reports\cash-on-hand.csv"

#     with fp.open(mode = "r", encoding = "UTF-8", newline = "") as file:
#         reader = csv.reader(file)
#         next(reader)

#         cash_on_hand = []

#         for row in reader:
#             cash_on_hand.append(row)

#         current_cash = cash_on_hand[0][1]
#         deficit_list = []

#         for day, cash in cash_on_hand:

#             if current_cash > cash:
#                 deficit_list.append([day,int(current_cash) - int(cash)])

#             current_cash = cash

#         with open("Summary_Report.txt", mode = "a", encoding = "UTF-8") as file:
#             if not deficit_list:
#                 file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
#             else:
#                 for day, deficit in deficit_list:
#                     file.write(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{deficit}\n")