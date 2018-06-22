#answers can be found below the code


from pandas import DataFrame,Series
import pandas.io.data as web
import datetime
import pandas as pd


def getPrice(start, end , company):
    allStock = {}
    startDate = start
    endDate = end
    listOfCompanies = company
    for ticket in listOfCompanies:
        allStock[ticket] = web.get_data_yahoo(ticket,startDate,endDate)
    
    price = web.DataFrame({tic:data['Adj Close'] for tic,data in allStock.iteritems()})
    sumStock = DataFrame(data = price.sum(axis=1),columns = ['individialStockSum'])
    sumStock['dowJones'] = Series(web.get_data_yahoo('DJIA',startDate,endDate)['Adj Close'],index = sumStock.index)
    return sumStock

#the companies dataset keeps changing with the date, I got the below data from wikipedia

cumulativeStock = getPrice('2016-10-15',datetime.datetime.now(),['AAPL','AXP','BA','CAT','CSCO','CVX','KO','DD','XOM','GE','GS','HD','IBM','INTC','JNJ','JPM','MCD',
'MMM','MRK','MSFT','NKE','PFE','PG','TRV','UNH','UTX','V','VZ','WMT','DIS'])

cumulativeStock = cumulativeStock.append(getPrice('2015-03-19',datetime.datetime.now(),['AAPL','AXP','BA','CAT','CSCO','CVX','KO','DD','XOM','GE','GS','HD','IBM','INTC','JNJ','JPM','MCD',
'MMM','MRK','MSFT','NKE','PFE','PG','TRV','UNH','UTX','V','VZ','WMT','DIS']))


cumulativeStock = cumulativeStock.append(getPrice('2013-09-23','2015-03-18',['T','AXP','BA','CAT','CSCO','CVX','KO','DD','XOM','GE','GS','HD','IBM','INTC',
'JNJ','JPM','MCD','MMM','MRK','MSFT','NKE','PFE','PG','TRV','UNH','UTX','V','VZ','WMT','DIS']))

cumulativeStock = cumulativeStock.append(getPrice('2012-09-24','2013-09-22',['AA','BAC','HPQ','T','AXP','BA','CAT','CSCO','CVX','KO','DD',
'XOM','GE','HD','IBM','INTC','JNJ','JPM','MCD','MMM','MRK','MSFT','PFE','PG','TRV','UNH','UTX','VZ','WMT','DIS']))

cumulativeStock = cumulativeStock.append(getPrice('2010-01-04','2012-09-23',['AA','BAC','HPQ','T','AXP','BA','CAT','CSCO','CVX','KO','DD',
'XOM','GE','HD','IBM','INTC','JNJ','JPM','MCD','MMM','MRK','MSFT','PFE','PG','TRV','UTX','VZ','WMT','DIS']))
#Kraft Foods Inc, KFT is not present in Yahoo Finance

cumulativeStock.sort_index(inplace=True)
print (cumulativeStock)
print (cumulativeStock.corr())


"""
==================================================================
Output

                    individialStockSum  dowJones
individialStockSum            1.000000  0.989528
dowJones                      0.989528  1.000000
==================================================================
Answers to the questions in the assignment can be found below:
==================================================================
1. List of Dow companies' stock symbols

The Dow Jones Industrail Average comprises of 30 companies, and some of the companies are occasionally changed, below are the company symbols along with the dates

i) From June 8th 2009 to September 23rd 2012 below are the components of Dow Jones
'AA','BAC','HPQ','T','AXP','BA','CAT','CSCO','CVX','KO','DD',
'XOM','GE','HD','IBM','INTC','JNJ','JPM','MCD','MMM','MRK','MSFT','PFE','PG','TRV','UTX','VZ','WMT','DIS'
Kraft Foods Inc, KFT or KRFT is not present in Yahoo Finance. 


ii) From September 24th 2012 to September 22nd 2013 below are the components of Dow Jones
'AA','BAC','HPQ','T','AXP','BA','CAT','CSCO','CVX','KO','DD',
'XOM','GE','HD','IBM','INTC','JNJ','JPM','MCD','MMM','MRK','MSFT','PFE','PG','TRV','UNH','UTX','VZ','WMT','DIS'

iii) From September 23rd 2013 to March 18th 2015  below are the components of Dow Jones
'T','AXP','BA','CAT','CSCO','CVX','KO','DD','XOM','GE','GS','HD','IBM','INTC',
'JNJ','JPM','MCD','MMM','MRK','MSFT','NKE','PFE','PG','TRV','UNH','UTX','V','VZ','WMT','DIS'

iv) From March 19th 2015 below are the components of Dow Jones
'AAPL','AXP','BA','CAT','CSCO','CVX','KO','DD','XOM','GE','GS','HD','IBM','INTC','JNJ','JPM','MCD',
'MMM','MRK','MSFT','NKE','PFE','PG','TRV','UNH','UTX','V','VZ','WMT','DIS'
==================================================================
2. Correlation value from your index to the actual Dow value

Correlation factor by using inbuilt method "corr" is 0.989528

==================================================================
3. Why is this value not exactly 1? What would be needed to make this value 1?

Before we get into the details of the correlation factor, it is important to understand 
how Dow Jones Industrial Average is calculated. The Dow Jones Industrial Average (DJIA)
is a price-weighted index that is calculated by dividing the sum of the prices of the 
30 component stocks (Dow Jones Industrial Average components) by a number called 
the DJIA Divisor or Dow Divisor. DJIA divisor is updated periodically. [Source : Wikipedia]

For our analysis, we calculated the sum of 30 components in the column individialStockSum.
These 30 components define the value for individualStockSum, whereas actual dow value
has 31 variables ie., 30 components + 1 DJIA divisor. Because of this additional variable
correlation factor is not 1. If dow divisor is kept as constant, the correlation factor
will be 1. 
==================================================================
"""