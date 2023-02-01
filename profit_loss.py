# use "def" to create a profit and loss function
def profitloss():
    """
    - Function checks each day to see if the net profit is a surplus or deficit
    - Function will then calculate the deficit amount 
    """
    # import Path from pathlib and csv module
    from pathlib import Path
    import csv

    # locate the csv file by creating a file path
    fp = Path.cwd()/"csv_reports/profit-and-loss.csv"

    # use "open()" to read the file
    # "r" in mode parameter means read
    with fp.open(mode = "r", encoding = "UTF-8", newline = "") as file:
        reader = csv.reader(file)
        next(reader)

        # create an empty list to store data from csv file
        P_and_L = []

        # use a "for" loop to iterate over loop to append data from csv file
        for row in reader:
            # append only the first and fifth column (what's necessary)
            P_and_L.append([row[0], row[4]])

    # create a varible "profit" to store the base net profit (previous day)
    profit = P_and_L[0][1] # use string slicing to obtain data from list

    # create an empty list to store the days that net profit deficit has occured
    deficit_list = []

    # use "for" loop with 2 entities to iterate over nested list
    for day, net_profit in P_and_L:

        # use "if" to check if net profit is lowering than previous day
        if net_profit < profit:

            # append the day number and deficit amount into the list
            deficit_list.append([day, int(profit) - int(net_profit)])

        # update the base net profit with the current day's net profit
        profit = net_profit

    # create a new .txt file to store summary report, "a" in mode parameter means append
    with open("Summary_Report.txt", mode = "a", encoding = "UTF-8") as file:

        # use "if not" to check if the deficit list is empty
        if not deficit_list:
            # write the text in summary report if list is empty
            file.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

        # shows that list is not empty which means there are days where net profit deficit occurs    
        else:
            # use "for" loop again to iterate over nested list
            for day, deficit in deficit_list:
                # write the text in summary report using "f string"
                # two entity variable stores the day number and respective deficit amount
                file.write(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{deficit}")

# ----------------- Base solution ----------------- #
# def profitloss():
#     """
#     - Function checks each day to see if the net profit is a surplus or deficit
#     - Function will then calculate the deficit amount 
#     """
#     from pathlib import Path
#     import csv

#     fp = Path.cwd()/"csv_reports/profit-and-loss.csv"

#     with fp.open(mode = "r", encoding = "UTF-8", newline = "") as file:
#         reader = csv.reader(file)
#         next(reader)

#         P_and_L = []

#         for row in reader:
#             P_and_L.append([row[0], row[4]])

#     profit = P_and_L[0][1]
#     deficit_list = []

#     for day, net_profit in P_and_L:

#         if net_profit < profit:
#             deficit_list.append([day, int(profit) - int(net_profit)])

#         profit = net_profit

#     with open("Summary_Report.txt", mode = "a", encoding = "UTF-8") as file:
#         if not deficit_list:
#             file.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
#         else:
#             for day, deficit in deficit_list:
#                 file.write(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{deficit}")