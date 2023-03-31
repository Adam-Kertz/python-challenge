import csv  #get necessary module for reading csv files

#open file with budget data
with open('./Resources/budget_data.csv') as file:
    csvreader = csv.reader(file, delimiter = ",")

    month_count = 0     #initialize count to 0
    running_total = 0   #initialize variable to keep track of running profit total 
    average = 0         #initialize variable to track running average
    max_increase = 0    #initialize variable to track largest increase in profit
    max_decrease = 0    #initialize variable to track largest decrease in profit

    header = next(csvreader)     #store header row
    
    for row in csvreader:
        month_count +=1 #count current month
        monthly_profit = float(row[1])  #store monthly profit
        running_total += monthly_profit #update running profit total
        
        #start calculating profit changes once there are two or more data points
        if month_count >= 2:
            average_count = month_count - 1     #There is exactly one less monthly change than total months
            monthly_change = monthly_profit-monthly_profit_old  #monthly change

            #Calculate average by multiplying the previous average by the previous running total and re-averaging
            average = (average*(average_count-1)+monthly_change)/average_count

            #Update maximum increases and decreases (and store the associated month)
            if monthly_change > max_increase:
                max_increase_month = row[0]     #store associated month and year information
                max_increase = monthly_change   #store amount of increase
            elif monthly_change < max_decrease:
                max_decrease_month = row[0]     #store associated month and year information
                max_decrease = monthly_change   #store amount of decrease

        monthly_profit_old = monthly_profit #on next iteration, this will be used to calculate profit change

# Output results to screen
print("\nFinancial Analysis")
print("\n----------------------------")
print(f"\nTotal Months: {month_count}")
print(f"\nTotal: ${running_total:.0f}")
print(f"\nAverage Change: $ {average:.2f}")
print(f"\nGreatest Increase in Profits: {max_increase_month} (${max_increase:.0f})")
print(f"\nGreatest Decrease in Profits: {max_decrease_month} (${max_decrease:.0f})\n")

# Output same results to file
with open("./analysis/Financial Analysis.txt",'w') as file:
    file.write("Financial Analysis")
    file.write("\n----------------------------")
    file.write(f"\nTotal Months: {month_count}")
    file.write(f"\nTotal: ${running_total:.0f}")
    file.write(f"\nAverage Change: $ {average:.2f}")
    file.write(f"\nGreatest Increase in Profits: {max_increase_month} (${max_increase:.0f})")
    file.write(f"\nGreatest Decrease in Profits: {max_decrease_month} (${max_decrease:.0f})\n")