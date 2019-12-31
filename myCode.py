import numpy as np
import matplotlib.pyplot as plt
import xlrd
import array as arr
from multiprocessing import Process
import sys


def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x

    return(b_0, b_1)


def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m",
                marker="o", s=30)

    # predicted response vector
    y_pred = b[0] + b[1]*x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()


def foodcount():

    # Give the location of the file
    loc = ("D:\SourceCodes and POCs\ml-linear\DataSet.xls")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    x_arr = arr.array('i', [])
    y_arr = arr.array('i', [])

    for i in range(sheet.nrows):
        if i > 0:
            xval = int(sheet.cell_value(i, 1))
            x_arr.append(xval)

    for j in range(sheet.nrows):
        if j > 0:
            yval = int(sheet.cell_value(j, 0))
            y_arr.append(yval)
    # observations
    x = np.array(x_arr)
    y = np.array(y_arr)
    # y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

    # estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients: b_0 = {} b_1 = {}").format(b[0], b[1])

    # plotting regression line
    plot_regression_line(x, y, b)


def wastagepercentage():

    # Give the location of the file
    loc = ("D:\SourceCodes and POCs\ml-linear\DataSet.xls")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    x_arr = arr.array('i', [])
    y_arr = arr.array('i', [])

    for i in range(sheet.nrows):
        if i > 0:
            xval = int(sheet.cell_value(i, 2))
            x_arr.append(xval)

    for j in range(sheet.nrows):
        if j > 0:
            yval = int(sheet.cell_value(j, 1))
            y_arr.append(yval)
    # observations
    x = np.array(x_arr)
    y = np.array(y_arr)

    # estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients: b_0 = {} b_1 = {}").format(b[0], b[1])

    # plotting regression line
    plot_regression_line(x, y, b)


if __name__ == "__main__":
    p1 = Process(target=foodcount)
    p1.start()
    p2 = Process(target=wastagepercentage)
    p2.start()
