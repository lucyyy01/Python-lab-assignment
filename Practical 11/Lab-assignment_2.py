# Practical 11, Lab Assignment 2
# Recruitment visualization for multiple companies.

import pandas as pd
import matplotlib.pyplot as plt


DATA = [
    {'Company': 'Microsoft', 'Recruits': 120},
    {'Company': 'Google', 'Recruits': 140},
    {'Company': 'Amazon', 'Recruits': 130},
    {'Company': 'IBM', 'Recruits': 90},
    {'Company': 'Deloitte', 'Recruits': 85},
    {'Company': 'Capgemini', 'Recruits': 110},
    {'Company': 'ATOS Origin', 'Recruits': 75},
    {'Company': 'Amdocs', 'Recruits': 95},
]


def main():
    df = pd.DataFrame(DATA)

    plt.figure()
    plt.bar(df['Company'], df['Recruits'], color='skyblue')
    plt.title('New Recruitment Count by Company')
    plt.xlabel('Company')
    plt.ylabel('Recruits')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure()
    plt.pie(df['Recruits'], labels=df['Company'], autopct='%1.1f%%', startangle=140)
    plt.title('Recruitment Distribution by Company')
    plt.tight_layout()
    plt.show()

    plt.figure()
    colors = plt.cm.tab20.colors[:len(df)]
    plt.pie(df['Recruits'], labels=df['Company'], autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops={'edgecolor': 'black'})
    plt.title('Customized Recruitment Pie Chart')
    plt.tight_layout()
    plt.show()

    plt.figure()
    wedges, texts = plt.pie(df['Recruits'], labels=df['Company'], startangle=140, wedgeprops=dict(width=0.4))
    plt.title('Recruitment Doughnut Chart')
    plt.tight_layout()
    plt.show()

    comparison = df[df['Company'].isin(['IBM', 'Amdocs'])]
    plt.figure()
    plt.bar(comparison['Company'], comparison['Recruits'], color=['blue', 'orange'])
    plt.title('IBM vs Amdocs Recruitment Comparison')
    plt.xlabel('Company')
    plt.ylabel('Recruits')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
