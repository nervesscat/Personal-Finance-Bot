import matplotlib as mpl
import matplotlib.pyplot as plt

class Graphics:

    def plot(self, balance, income, expense, option):
        if option == '-bal':
            self.plotBalance(balance, income, expense)
        elif option == '-in':
            self.plotIncome(income)
        elif option == '-ex':
            self.plotExpense(expense)
        else:
            self.plotBalance(balance, income, expense)

    def plotBalance(self, balance, income, expense):
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
        ax.set_xticks(date[::4])

        ax.set_ylabel('LPS', fontsize=14)

        ax.set_title('Balance', fontsize=18)

        ax.legend(['Balance', 'Income', 'Expense'], loc='upper left')

        fig.savefig('plot.png')
        plt.close(fig)

    def plotIncome(self, income):

        fig, ax = plt.subplots()

        incomeT = income[0]
        dateIncome = income[1]

        ax.plot(dateIncome, incomeT, color='green',  linewidth=3, linestyle='--');

        ax.set_xlabel('Date', fontsize=14)
        ax.set_xticks(dateIncome[::4])

        ax.set_ylabel('LPS', fontsize=14)

        ax.set_title('Income', fontsize=18)

        fig.savefig('plot.png')
        plt.close(fig)

    def plotExpense(self, expense):

        fig, ax = plt.subplots()

        expenseT = expense[0]
        dateExpense = expense[1]

        ax.plot(dateExpense, expenseT, color='red',  linewidth=3, linestyle='--');

        ax.set_xlabel('Date', fontsize=14)
        ax.set_xticks(dateExpense[::4])

        ax.set_ylabel('LPS', fontsize=14)

        ax.set_title('Expense', fontsize=18)

        fig.savefig('plot.png')
        plt.close(fig)

        
