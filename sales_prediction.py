"""
A company has determined that its annual profit is typically 23 percent of the total sales. 
Write a program called sales_prediction.py that asks the user to enter the projected amount of
 total sales and then displays the profit that will be made from that amount. The program should 
 then display the projected total profits for each of the next following 10 years, assuming that 
 the amount of total sales grows by 5 percent every year.

*Make sure that all the printed profits are rounded to 2 decimal places, 
the underscore character is used to separate the hundreds from the thousands (and the thousands from the millions)
groups of digits, and the amounts are 16 characters long with zeros to fill the empty spaces.
"""




from operator import index

## asking the user for first year sales

total_sales =float(input("Enter the total sales :"))
profit_percentage = 0.23


# function for  generating yearly sales
def growthTotalSales(total_sales):
    projected_sales =[]
    projected_sales.append(total_sales)
    for i in range(1,10):
        total_sales =total_sales * 1.05
        projected_sales.append(total_sales)
    
    return projected_sales

sales = growthTotalSales(total_sales)


## looping to calculate profit for each year
for i in sales:
    projected_profit =[]
    profit= i * profit_percentage
    rounded_profit = round(profit,2)
    year = sales.index(i)
    print(f'Projected total Profit for year {year +1 } is {rounded_profit}' ) 




        

