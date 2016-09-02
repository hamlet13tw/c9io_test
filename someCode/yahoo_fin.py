from yahoo_finance import Share
import datetime
 
def getStock(id):
    stock = Share(str(id)+'.TW')
    today = datetime.date.today() #todays date
    data = stock.get_historical('2016-01-28', str(today))
    return data
 
print getStock(2353)