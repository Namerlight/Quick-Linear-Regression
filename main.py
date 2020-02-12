import numpy
import matplotlib.pyplot as plt
from scipy import stats


print("Hello")

demand = (305, 307, 312, 316, 317, 319, 321, 322, 325, 327, 355, 365, 371, 380, 385, 391, 395, 406, 412, 439,
                  441, 449, 451, 454, 465, 471, 472, 476, 479, 490, 491, 499, 502, 507, 520, 523, 529, 530, 537, 542,
                  549, 560, 562, 563, 569, 570, 575, 577, 586, 603, 604, 607, 620, 622, 624, 633, 645, 646, 648, 654,
                  666, 670, 687, 691, 692, 698, 703, 706)
price = (344, 251, 107, 246, 389, 372, 307, 348, 259, 423, 298, 684, 646, 543, 442, 591, 348, 415, 268, 427,
                     599, 499, 500, 454, 464, 370, 414, 691, 469, 985, 650, 917, 703, 384, 1047, 465, 940, 1066, 552, 680,
                     971, 599, 1063, 937, 539, 426, 427, 983, 864, 973, 969, 791, 811, 758, 423, 408, 509, 546, 730, 722,
                     747, 550, 806, 259, 269, 374, 629, 444)


def linear_regression(xinp, yinp):

    x = numpy.asarray(xinp)
    y = numpy.asarray(yinp)

    # Plotting the Graph
    plt.xlabel('Demand')
    plt.ylabel('Price')

    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

    plt.plot(x, y, 'o', label='original data')
    plt.plot(x, intercept + slope * x, 'r', label='fitted line')
    plt.legend()
    plt.show()


linear_regression(demand, price)
