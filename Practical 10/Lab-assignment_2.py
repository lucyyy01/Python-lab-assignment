# Practical 10, Lab Assignment 2
# Manage state information and calculate population statistics.

import pandas as pd


STATES = [
    {'State': 'California', 'Area': 423967, 'Population': 39538223},
    {'State': 'Texas', 'Area': 695662, 'Population': 29145505},
    {'State': 'Florida', 'Area': 170312, 'Population': 21538187},
    {'State': 'New York', 'Area': 141297, 'Population': 20201249},
    {'State': 'Illinois', 'Area': 149995, 'Population': 12812508},
]


def main():
    df = pd.DataFrame(STATES)
    df['Density'] = df['Population'] / df['Area']

    print('Complete information of states:')
    print(df.to_string(index=False))

    largest_area = df.loc[df['Area'].idxmax()]
    print(f"\nState with largest area: {largest_area['State']}")

    largest_population = df.loc[df['Population'].idxmax()]
    print(f"State with largest population: {largest_population['State']}")

    print('\nPopulation density for each state:')
    for _, row in df.iterrows():
        print(f"{row['State']}: {row['Density']:.2f} people per square km")

    highest_density = df.loc[df['Density'].idxmax()]
    print(f"\nState with highest population density: {highest_density['State']}")


if __name__ == '__main__':
    main()
