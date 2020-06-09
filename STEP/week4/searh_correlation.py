import argparse
from readGraph import readGraph
import numpy as np
import matplotlib.pyplot as plt

#ランク付けして上位５人がビンゴの人かどうかを調べる
def PageRank(nick_ind_dic, ind_node_dic):

    def makeValueList(ind_node_dic):
        value_list = []
        for i in range(len(ind_node_dic)):
            value_list.append(ind_node_dic[i].value)
        return value_list


    def finishChecker(pre_value_list, aft_value_list):
        for v1, v2 in zip(pre_value_list, aft_value_list):
            if abs(v1 - v2) >= 1:
                return False
        return True


    for i in range(20):
        print(i)
        pre_value_list = makeValueList(ind_node_dic)
        #print(pre_value_list)
        for i in range(len(ind_node_dic)):
            node = ind_node_dic[i]
            if node.adjacency:
                give_value = node.value/len(node.adjacency)
                node.value = 0
                for ad in node.adjacency:
                    ad_node = ind_node_dic[ad]
                    ad_node.value += give_value
        aft_value_list = makeValueList(ind_node_dic)
        #valueが変化しなかったら計算をやめる
        if finishChecker(pre_value_list, aft_value_list):
            print("value converged!")
            return aft_value_list
    return aft_value_list


def showResult(value_list, ind_node_dic, bingo_path):

    def readBingoTxt(bingo_path):
        #ビンゴの人達の読み込み
        bingo_list = []
        bingo_file = open(bingo_path, "r", encoding="utf_8")
        while True:
            read_word = bingo_file.readline()
            if len(read_word) > 1:
                bingo_list.append(read_word[:-1])
            else:
                break
        return bingo_list


    def searchCorrelation(rank_list, bingo_list):
        plot_x = [i for i in range(5)]
        plot_y = []
        rank_list = np.array(rank_list)
        for i, name in enumerate(bingo_list):
            rank = np.where(rank_list == name)[0][0] + 1
            plot_y.append(rank)
        #plot
        plt.scatter(plot_x, plot_y, label="simularity")
        plt.xlabel("bingo rank")
        plt.ylabel("page rank")
        plt.savefig("images/correlation.png")

        corr = np.corrcoef(plot_x, plot_y)[0][1]
        print("ビンゴランクとページランクの相関係数 ", corr)

    
    bingo_list = readBingoTxt(bingo_path)
    rank_list = []
    #ページランクの結果        
    value_list = np.array(value_list)
    #print(value_list)
    #降順indexの取得
    sort_num = value_list.argsort()[::-1]
    for i, num in enumerate(sort_num):
        nickname = ind_node_dic[num].nickname
        #print(i+1, "位 : ", nickname)
        rank_list.append(nickname)

    searchCorrelation(rank_list, bingo_list)


parser = argparse.ArgumentParser()
parser.add_argument("--links", required="True")
parser.add_argument("--nicknames", required="True")
parser.add_argument("--bingo", required = "True")
args = parser.parse_args()

links_path = args.links
nicknames_path = args.nicknames
nick_ind_dic, ind_node_dic = readGraph(links_path, nicknames_path)
value_list = PageRank(nick_ind_dic, ind_node_dic)

bingo_path = args.bingo
showResult(value_list, ind_node_dic, bingo_path)

