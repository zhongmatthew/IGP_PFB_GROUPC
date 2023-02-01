def profitloss():
    """
    - Function checks each day to see if the net profit is a surplus or deficit
    - Function will then calculate the deficit amount 
    """
    from pathlib import Path
    import csv

    fp = Path.cwd()/"csv_reports/profit-and-loss.csv"

    with fp.open(mode = "r", encoding = "UTF-8", newline = "") as file:
        reader = csv.reader(file)
        next(reader)

        P_and_L = []

        for row in reader:
            P_and_L.append([row[0], row[4]])

    profit = P_and_L[0][1]
    deficit_list = []

    for day, net_profit in P_and_L:

        if net_profit < profit:
            deficit_list.append([day, int(profit) - int(net_profit)])

        profit = net_profit

    with open("Summary_Report.txt", mode = "a", encoding = "UTF-8") as file:
        if not deficit_list:
            file.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        else:
            for day, deficit in deficit_list:
                file.write(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{deficit}")