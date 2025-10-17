import numpy as np

companies = ['Google', 'Amazon', 'Apple', 'Meta']
days = ['Mon', 'Tue']
price_types = ['Open', 'Close', 'High', 'Low']

prices = np.round(np.random.uniform(60.1, 70.7, size = (4, 2, 4)), 2) #for generating stock prices

for c_index, company in enumerate(companies):
    print(f'Prices for {company}:')
    for d_index, day in enumerate(days):
        print(f'Day: {day}')
        for p_index, price_type in enumerate(price_types):
            print(f'{price_type} Price: {prices[c_index, d_index, p_index]}')
        print('')
    print('')
