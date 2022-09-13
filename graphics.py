import matplotlib as mpl
import matplotlib.pyplot as plt

class Graphics:

    def plot(self, data):
        fig, ax = plt.subplots()

        balance = data[0]
        date = data[1]

        ax.plot(date, balance, color='blue',  linewidth=3, linestyle='--');  # Plot some data on the axes.

        # Save the figure to a file
        fig.savefig('plot.png')

        # Don't show the figure
        plt.close(fig)

        
