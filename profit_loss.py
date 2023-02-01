def profitloss(forex):
    """
    Function checks each day to see if the net profit is a surplus or deficit
    Function will then calculate the deficit amount 
    """
    from pathlib import Path
    import csv

    fp = Path.cwd()/"csv_reports/profits-and-loss.csv"

    with fp.open(mode ="r", encoding ="UTF-8", newline = "") as file:
        reader = csv.reader(file)
        next(reader)

        P_and_L = []

        for row in reader:
            P_and_L.append([row[0], row[4]])
