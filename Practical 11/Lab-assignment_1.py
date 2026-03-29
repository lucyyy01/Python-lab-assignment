# Practical 11, Lab Assignment 1
# Sales analysis for a cosmetic company using matplotlib.

import pandas as pd
import matplotlib.pyplot as plt


DATA = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Total Profit': [12000, 15000, 13000, 17000, 16000, 15500, 18000, 17500, 16800, 19000, 20000, 21000],
    'Face Cream': [4000, 4200, 4300, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300],
    'Face Wash': [3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100],
    'Lipstick': [2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600],
}


def main():
    df = pd.DataFrame(DATA)

    plt.figure()
    plt.plot(df['Month'], df['Total Profit'], marker='o')
    plt.title('Total Profit by Month')
    plt.xlabel('Month')
    plt.ylabel('Profit')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure()
    for column in ['Face Cream', 'Face Wash', 'Lipstick']:
        plt.plot(df['Month'], df[column], marker='o', label=column)
    plt.title('Product Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure()
    plt.bar(df['Month'], df['Face Cream'], alpha=0.7, label='Face Cream')
    plt.bar(df['Month'], df['Face Wash'], alpha=0.7, label='Face Wash', bottom=df['Face Cream'])
    plt.title('Face Cream and Face Wash Sales')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.legend()
    plt.tight_layout()
    plt.show()

    totals = {product: df[product].sum() for product in ['Face Cream', 'Face Wash', 'Lipstick']}
    plt.figure()
    plt.pie(totals.values(), labels=totals.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Total Sales Share by Product')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
