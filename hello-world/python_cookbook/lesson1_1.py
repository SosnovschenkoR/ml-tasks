import numpy as np


def drop_first_last(grades):
    first, *middle, last = grades
    return np.average(middle)

X = drop_first_last((11, 20, 40, 33))
print('drop_first_last=', X)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers)

sales_record = (10, 8, 7, 1, 9, 5, 10, 3)
*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
print(trailing_avg)
# avg_comparison(trailing_avg, current_qtr)

