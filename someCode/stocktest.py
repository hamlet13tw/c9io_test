from grs import Stock

stock = Stock('2618')
print stock.moving_average(0)
print stock.moving_average_value(1)
print stock.moving_average_bias_ratio(1, 3)