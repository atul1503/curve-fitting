# fit a second degree polynomial to the economic data
from numpy import arange,sin,log,tan
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot

# define the true objective function
def objective(x):
	return 0.01006304431397636*sin(0.009997006528342673*x+0.010000006129223197)+0.3065914809778943*x+0.01033913912969194 

    
# load the dataset
url = 'output.csv'
dataframe = read_csv(url, header=None)
data = dataframe.values
# choose the input and output variables
x, y = data[1:, 0], data[1:, -1]
# plot input vs output
pyplot.scatter(x, y)
#convert string to float
x=[float(i) for i in x]
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x),max(x),1)
# calculate the output for the range
y_line = objective(x_line)
# create a line plot for the mapping function
pyplot.plot(x_line, y_line, color='red')
pyplot.show()