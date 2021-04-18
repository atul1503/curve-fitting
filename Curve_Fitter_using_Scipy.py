# fit a second degree polynomial to the economic data
from numpy import arange,sin,log,tan
from pandas import read_csv
from scipy.optimize import curve_fit
from matplotlib import pyplot

# define the true objective function
def objective(x, a, b,c,d,e):
	return a*sin(b*x+c)+d*x+e
    
# load the dataset
url = 'output.csv'
dataframe = read_csv(url, header=None)
data = dataframe.values
# choose the input and output variables
x, y = data[1:, 0], data[1:, -1]
# curve fit
print(x,y)
popt, _ = curve_fit(objective, x, y)
# summarize the parameter values
a,b,c,d,e= popt
print(a,b,c,d,e)
# plot input vs output
pyplot.scatter(x, y)
#convert string to float
x=[float(i) for i in x]
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x),max(x),1)
# calculate the output for the range
y_line = objective(x_line,a, b,c,d,e)
# create a line plot for the mapping function
pyplot.plot(x_line, y_line, color='red')
pyplot.show()