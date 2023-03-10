import matplotlib as mpl
import matplotlib.pyplot as plt

import datetime

class Graphics:

    def plot(self, balance, income, expense, option, currency):
        if option == '-bal':
            self.plotBalance(balance, income, expense, currency)
        elif option == '-in':
            self.plotIncome(income, currency)
        elif option == '-ex':
            self.plotExpense(expense, currency)
        elif option == '-lm':
            self.plotLastMonthBalance(balance, income, expense, currency)
        else:
            self.plotBalance(balance, income, expense, currency)

    def plotBalance(self, balance, income, expense, currency):
        fig, ax = plt.subplots()

        balanceT = balance[0]
        date = balance[1]

        incomeT = income[0]
        dateIncome = income[1]

        expenseT = expense[0]
        dateExpense = expense[1]

        ax.plot(date, balanceT, color='blue',  linewidth=3, linestyle='--');  # Plot some balance on the axes.
        ax.plot(dateIncome, incomeT, color='green',  linewidth=3, linestyle='--');  # Plot some income on the axes.
        ax.plot(dateExpense, expenseT, color='red',  linewidth=3, linestyle='--');  # Plot some expense on the axes.

        ax.set_xlabel('Date', fontsize=14)
        #Depending on the amount of data, it might be better to use a different interval, to avoid cluttering the graph
        ax.set_xticks(date[::14])


        ax.set_ylabel(currency, fontsize=14)

        ax.set_title('Balance', fontsize=18)

        ax.legend(['Balance', 'Income', 'Expense'], loc='upper left')

        fig.savefig('plot.png')
        plt.close(fig)

    def plotLastMonthBalance(self, balance, income, expense, currency):
        fig, ax = plt.subplots()
        today = datetime.date.today()
        one_month_ago = today - datetime.timedelta(days=30)

        # Lamda function to found the index of the first date that is greater than one_month_ago
        maskBal = next((i for i, date in enumerate(balance[1]) if date > one_month_ago.isoformat()), None)
        maskBal = slice(maskBal, None)

        balanceT = balance[0][maskBal]
        date = balance[1][maskBal]

        # Lamda function to found the index of the first date that is greater than one_month_ago
        maskIn = next((i for i, date in enumerate(income[1]) if date > one_month_ago.isoformat()), None)
        maskIn = slice(maskIn, None)

        incomeT = income[0][maskIn]
        dateIncome = income[1][maskIn]

        # Lamda function to found the index of the first date that is greater than one_month_ago
        maskEx = next((i for i, date in enumerate(expense[1]) if date > one_month_ago.isoformat()), None)
        maskEx = slice(maskEx, None)

        expenseT = expense[0][maskEx]
        dateExpense = expense[1][maskEx]

        ax.plot(date, balanceT, color='blue',  linewidth=3, linestyle='--');  # Plot some balance on the axes.
        ax.plot(dateIncome, incomeT, color='green',  linewidth=3, linestyle='--');  # Plot some income on the axes.
        ax.plot(dateExpense, expenseT, color='red',  linewidth=3, linestyle='--');  # Plot some expense on the axes.

        ax.set_xlabel('Date', fontsize=14)
        ax.set_xticks(date[::4])

        ax.set_ylabel(currency, fontsize=14)

        ax.set_title('Last Month Balance', fontsize=18)

        ax.legend(['Balance', 'Income', 'Expense'], loc='upper left')

        fig.savefig('plot.png')
        plt.close(fig)


    def plotIncome(self, income, currency):

        fig, ax = plt.subplots()

        incomeT = income[0]
        dateIncome = income[1]

        ax.plot(dateIncome, incomeT, color='green',  linewidth=3, linestyle='--');

        ax.set_xlabel('Date', fontsize=14)
        ax.set_xticks(dateIncome[::7])

        ax.set_ylabel(currency, fontsize=14)

        ax.set_title('Income', fontsize=18)

        fig.savefig('plot.png')
        plt.close(fig)

    def plotExpense(self, expense, currency):

        fig, ax = plt.subplots()

        expenseT = expense[0]
        dateExpense = expense[1]

        ax.plot(dateExpense, expenseT, color='red',  linewidth=3, linestyle='--');

        ax.set_xlabel('Date', fontsize=14)
        ax.set_xticks(dateExpense[::7])

        ax.set_ylabel(currency, fontsize=14)

        ax.set_title('Expense', fontsize=18)

        fig.savefig('plot.png')
        plt.close(fig)

        
