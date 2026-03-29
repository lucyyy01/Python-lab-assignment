# Practical 12, Lab Assignment 1
# Diamonds DataFrame operations.

import pandas as pd


DATA = [
    {'carat': 0.23, 'cut': 'Ideal', 'color': 'E', 'clarity': 'SI2', 'depth': 61.5, 'table': 55.0, 'price': 326, 'x': 3.95, 'y': 3.98, 'z': 2.43},
    {'carat': 0.21, 'cut': 'Premium', 'color': 'E', 'clarity': 'SI1', 'depth': 59.8, 'table': 61.0, 'price': 326, 'x': 3.89, 'y': 3.84, 'z': 2.31},
    {'carat': 0.23, 'cut': 'Good', 'color': 'E', 'clarity': 'VS1', 'depth': 56.9, 'table': 65.0, 'price': 327, 'x': 4.05, 'y': 4.07, 'z': 2.31},
    {'carat': 0.29, 'cut': 'Premium', 'color': 'I', 'clarity': 'VS2', 'depth': 62.4, 'table': 58.0, 'price': 334, 'x': 4.2, 'y': 4.23, 'z': 2.63},
    {'carat': 0.31, 'cut': 'Good', 'color': 'J', 'clarity': 'SI2', 'depth': 63.3, 'table': 58.0, 'price': 335, 'x': 4.34, 'y': 4.35, 'z': 2.75},
]


def main():
    df = pd.DataFrame(DATA)
    print('Diamonds DataFrame:')
    print(df.to_string(index=False))

    grouped = df.groupby('cut')['price']
    mean_price = grouped.mean()
    stats = grouped.agg(['count', 'min', 'max'])

    print('\nMean price for each cut:')
    print(mean_price)

    print('\nCount, minimum and maximum price for each cut:')
    print(stats)

    print('\nAverage value for x, y, z:')
    print(f"x: {df['x'].mean():.2f}")
    print(f"y: {df['y'].mean():.2f}")
    print(f"z: {df['z'].mean():.2f}")


if __name__ == '__main__':
    main()
