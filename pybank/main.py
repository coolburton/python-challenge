import os
import csv

bank_csv = os.path.join("budget_data.csv")
output_txt = os.path.join("budget_data_output.txt")

monthly_change_profitlist = []
month = []

total_month = 0
last_month_profit = 0
total_profit = 0
total_change = 0


with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = (','))
    csv_header = next(csvreader)

    for row in csvreader:
        total_month += 1

        month.append(row[0])

        current_month_profit = int(row[1])
        total_profit += current_month_profit

        monthly_change_profit = current_month_profit - last_month_profit
        monthly_change_profitlist.append(monthly_change_profit)
        total_change += monthly_change_profit
        last_month_profit = current_month_profit
    
    average_change = round((total_change - 867884)/(total_month - 1),2)

    greatest_increase_profit = max(monthly_change_profitlist)
    greatest_increase_profit_month = month[monthly_change_profitlist.index(greatest_increase_profit)]

    greatest_decrease_loss = min(monthly_change_profitlist)
    greatest_decrease_loss_month = month[monthly_change_profitlist.index(greatest_decrease_loss)]


    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_month}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increse in Profits: {greatest_increase_profit_month} (${greatest_increase_profit})")
    print(f"Greatest Decrese in Losses: {greatest_decrease_loss_month} (${greatest_decrease_loss})")

with open(output_txt, 'w') as txtfile:
   
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_month}\n")
    txtfile.write(f"Total: ${total_profit}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increse in Profits: {greatest_increase_profit_month} (${greatest_increase_profit})\n")
    txtfile.write(f"Greatest Decrese in Losses: {greatest_decrease_loss_month} (${greatest_decrease_loss})\n")





