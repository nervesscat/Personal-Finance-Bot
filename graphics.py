import matplotlib as mpl
import matplotlib.pyplot as plt

class Graphics:

    def plot(self, balance, income, expense):
        fig, ax = plt.subplots()

        balanceT = balance[0]
        date = balance[1]

        incomeT = income[0]
        dateIncome = income[1]

        expenseT = expense[0]
        dateExpense = expense[1]

        #ax.plot(date, balanceT, color='blue',  linewidth=3, linestyle='--');  # Plot some balance on the axes.

        # A graph with three lines

        ax.plot(date, balanceT, color='blue',  linewidth=3, linestyle='--');  # Plot some balance on the axes.
        ax.plot(dateIncome, incomeT, color='green',  linewidth=3, linestyle='--');  # Plot some income on the axes.
        ax.plot(dateExpense, expenseT, color='red',  linewidth=3, linestyle='--');  # Plot some expense on the axes.

        # Set the x axis label of the current axis.
        ax.set_xlabel('Date', fontsize=14)
        
        # Set the y axis label of the current axis.

        ax.set_ylabel('LPS', fontsize=14)

        # Set a title of the current axes.

        ax.set_title('Balance', fontsize=18)

        # show a legend on the plot

        ax.legend(['Balance', 'Income', 'Expense'], loc='upper left')

        # Save the figure to a file
        fig.savefig('plot.png')

        # Don't show the figure
        plt.close(fig)

        
