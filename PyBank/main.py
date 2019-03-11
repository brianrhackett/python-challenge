import csv
import os

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

budget_output = os.path.join(".", "budget_report.txt")

print("Financial Analysis \n------------------")

with open(budget_csv,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_headers = next(csvreader)

    numMonths = 0
    lastMonthProfit = 0
    total = 0
    maxProfit = 0
    minProfit = 0 
    profitChanges = []
    for row in csvreader:
        profit = int(row[1])
        total += profit

        if numMonths > 0:
            profitChange = profit - lastMonthProfit
            profitChanges.append(profitChange)
       
            if profitChange > maxProfit:
                maxProfit =  profitChange
                bestMonth = row[0]
            elif profitChange < minProfit:
                minProfit = profitChange
                worstMonth = row[0]

        numMonths += 1
        lastMonthProfit = profit

averageChange = round(sum(profitChanges) / len(profitChanges), 2)

print(f"Total Months:\t {numMonths}")
print(f"Total:\t ${total}")
print(f"Average Change:\t ${averageChange}")
print(f"Greatest Increase in Profits:\t {bestMonth} (${max(profitChanges)})")
print(f"Greatest Decrease in Profits:\t {worstMonth} (${min(profitChanges)})")

with open(budget_output, 'w', newline='') as txtfile:
    print("Financial Analysis \n------------------", file=txtfile)
    print(f"Total Months:\t {numMonths}", file=txtfile)
    print(f"Total:\t ${total}", file=txtfile)
    print(f"Average Change:\t ${averageChange}", file=txtfile)
    print(f"Greatest Increase in Profits:\t {bestMonth} (${max(profitChanges)})", file=txtfile)
    print(f"Greatest Decrease in Profits:\t {worstMonth} (${min(profitChanges)})", file=txtfile)