#main

#Objectives for Data Analysis  
    #Total number of Months
    #The net total amount of "PandL" over the period
    #The average of the changes in "PandL" over the entire period
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period

#import the resource
import os
import csv

#file to load
budget_data='C:/Users/Shawn/Desktop/python-challenge/PyBank/Resources/budget_data.csv'

#file to export
budget_export='C:/Users/Shawn/Desktop/python-challenge/PyBank/Analysis/budget_analysis.txt'

#Variables
total_months=0
period_revenue=0
month_change=[]
revenue_change_list=[]
av_change_pl=0
greatest_increase=["",0]
greatest_loss=["",0]
total_revenue=0
#Column names in resource [Date and PandL]

with open(budget_data) as budget_data:
    reader=csv.DictReader(budget_data)
    #creates a dictionary of the data allowing for easier reference
#count the months(rows)
    for row in reader:
       
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["PandL"])
        #print(total_months, period_revenue)

        #changes in revenue
        revenue_change=int(row["PandL"])-period_revenue
        period_revenue=int(row["PandL"])
        revenue_change_list=revenue_change_list+[revenue_change]
        month_change=month_change+[row["Date"]]

        #increase
        if (revenue_change > revenue_change_list[0]):
            greatest_increase[0]=row["Date"]
            greatest_increase[1]=revenue_change

        #decrease
        if (revenue_change < revenue_change_list[0]):
            greatest_loss[0]=row["Date"]
            greatest_loss[1]=revenue_change
            
#Average change in revenue
av_change_pl=sum(revenue_change_list)/len(revenue_change_list)

#Summary
output=(
    f'\nFinancial Analysis\n'
    f'---------------------------\n'
    f'\nTotal Months: {total_months}\n'
    f'\nTotal: ${total_revenue}\n'
    f'\nAverage Change: ${av_change_pl:.2f}\n'
    f'\nGreatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n'
    f'\nGreatest Decrease in Revenue: {greatest_loss[0]} (${greatest_loss[1]})\n'
)

print(output)

with open(budget_export,"w") as txt_file:
    txt_file.write(output)