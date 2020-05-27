import matplotlib.pyplot as plt

def read_txt():
    time_list = []
    time_file = open(
        "/Users/tanemoto/Desktop/myLeetCode_/STEP/week2/matmal_time.txt", "r", encoding="utf_8")
    count = 0
    while True:
        count += 1
        word = time_file.readline()
        if word:
            if count % 2 == 1:
                start = float(word[-15:-5])
            else:
                end = float(word[-15:-5])
                time_list.append(end-start)
        else:
            #print(time_list[:10])
            return time_list


def visualize(time_list):
    leng = len(time_list)
    x = [i for i in range(leng)]
    y1 = [t for t in time_list]
    #y2 = [i*numpy.log(i) for i in range(1, 81)]
    y2 = [(i**3)*(10**(-6)) for i in range(leng)]
    y3 = [2*(i**3)*(10**(-6)) for i in range(leng)]

    plt.plot(x, y1, label = "calc_time")
    plt.plot(x, y2, label = "n**3 (e-6)")
    plt.plot(x, y3, label = "2n**3 (e-6)")
    plt.xlabel("n")
    plt.ylabel("second")
    plt.legend()
    plt.title("EusLisp")
    #plt.show()
    plt.savefig(
        "/Users/tanemoto/Desktop/myLeetCode_/STEP/week2/img/Lisp_1.png")

time_list = read_txt()
visualize(time_list)


