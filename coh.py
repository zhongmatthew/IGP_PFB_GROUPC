def coh(forex):
    """
    - Function will check each day whether there is a cash surplus or deficit
    - Function will calculate the deficit amount if there is any
    """

from pathlib import Path
import csv
fp = Path.cwd()/"csv_reports\cash-on-hand.csv"

with fp.open(mode = "r", encoding = "UTF-8", newline = "") as file:
    reader = csv.reader(file)
    next(reader)

    cash_on_hand = []

    for row in reader:
        cash_on_hand.append(row)

    current_cash = cash_on_hand[0][1]
    deficit_list = []

    for day, cash in cash_on_hand:

        if current_cash > cash:
            deficit_list.append([day,int(current_cash) - int(cash)])

            current_cash = cash

    with open("Summary_Report.txt", mode = "w", encoding = "UTF-8") as file:
        if not deficit_list:
            file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        else:
            for day, deficit in deficit_list:
                file.write(F"[CASH DEFICIT] DAY: {day}, AMOUNT: SGD{round(deficit * forex, 2)}\n")