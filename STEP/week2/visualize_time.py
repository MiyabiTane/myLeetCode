import numpy
import time
import matplotlib.pyplot as plt

def calc_mat_mal(n):

    a = numpy.zeros((n, n))  # Matrix A
    b = numpy.zeros((n, n))  # Matrix B
    c = numpy.zeros((n, n))  # Matrix C

    #Initialize the matrices to some values.
    for i in range(n):
        for j in range(n):
            a[i, j] = i * n + j
            b[i, j] = j * n + i
            c[i, j] = 0

    begin = time.time()

    # Write code to calculate C = A * B                  #
    # (without using numpy librarlies e.g., numpy.dot()) #
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k]*b[k][j]

    end = time.time()
    print("time: %.6f sec" % (end - begin))

    # Print C for debugging. Comment out the print before measuring the execution time.
    total = 0
    for i in range(n):
        for j in range(n):
            # print c[i, j]
            total += c[i, j]
    # Print out the sum of all values in C.
    # This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
    print("sum: %.6f" % total)
    return end-begin

def visualize():
    x = [i for i in range(1,81)]
    y1 = []
    #y2 = [i*numpy.log(i) for i in range(1, 81)]
    y2 = [(i**3)*(10**(-6)) for i in range(1,81)]
    y3 = [2*(i**3)*(10**(-6)) for i in range(1,81)]
    for n in range(1,81):
        print(n )
        time = calc_mat_mal(n)
        y1.append(time)

    plt.plot(x, y1, label = "calc_time")
    plt.plot(x, y2, label = "n**3 (e-6)")
    plt.plot(x, y3, label = "2n**3 (e-6)")
    plt.xlabel("n")
    plt.ylabel("second")
    plt.legend()
    plt.title("use Chrome at n=50")
    #plt.show()
    plt.savefig(
        "/Users/tanemoto/Desktop/myLeetCode_/STEP/class2/step_homework1.png")

visualize()


