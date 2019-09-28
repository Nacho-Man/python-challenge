import os
import csv

csvpath = os.path.join('..', 'Resources.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.DictReader(csvfile, delimiter=',')
    
    
    #variables
    max_profit = None
    max_loss = None
    total = 0
    tot_delt = 0
    delta = 0
    avg_delt = 0
    last_profit = None
    profit = 0
    cur_month = None
    max_month = None
    min_month = None

    #the loop
    for line in csvreader:
        
        profit = int(line["Profit/Losses"])
        cur_month = line["Date"]
        if last_profit != None:
            delta = profit - last_profit

        if last_profit != None:
            tot_delt = tot_delt + delta
            last_profit = profit
        if last_profit == None:
                
            total = total + profit
        if max_profit == None or max_profit < delta:
            max_profit = delta
            max_month = cur_month
        if max_loss == None or max_loss > delta:
            max_loss = delta
            min_month = cur_month
        last_profit = profit    



        
                      
    #row count    
    csvfile.seek(0)
    row_count = sum(1 for line in csvreader)
    row_count = row_count - 1

    #simple avg
    avg_delt = tot_delt / (row_count-1)

    #format
    f = lambda a: "{:.2f}".format(a)
    max_profit = int(max_profit)
    
    #display
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {row_count}")
    print(f"Total: ${total}")
    print(f"Average Change: {f(avg_delt)}")
    print(f"Greatest Increase in Profits: {max_month} \
({max_profit})")
    print(f"Greatest Decrease in Profits: {min_month} \
({max_loss})")




#print(data)