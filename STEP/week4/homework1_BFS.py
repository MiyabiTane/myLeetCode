import argparse

class Node:

    def __init__(self):
        self.visited = False
        self.adjacency = []


def readGraph(links_path, nicknames_path):
    """
    output
    nick_ind_dic[dict] key: nickname, value: index
    ind_node_dic[dict] key: index, value: Node 
    """
    #.txtファイルからグラフの情報を取得
    #ニックネームとインデックスの関係の取得
    nick_ind_dic = {}
    nicknames_file = open("nicknames.txt", "r", encoding="utf_8")
    while True:
        read_word = nicknames_file.readline().split("\t")
        if len(read_word) < 2:
            break
        index = int(read_word[0])
        nickname = read_word[1][:-1]
        nick_ind_dic[nickname] = index
    #辺の情報の取得
    ind_node_dic = {}
    links_file = open("links.txt", "r", encoding="utf_8")
    while True:
        read_word = links_file.readline().split("\t")
        if len(read_word) < 2:
            break
        index = int(read_word[0])
        link = int(read_word[1][:-1])
        if not index in ind_node_dic:
            ind_node_dic[index] = Node()
        ind_node_dic[index].adjacency.append(link)
    #print(nick_ind_dic)
    #print(ind_node_dic[0].visited)
    return nick_ind_dic, ind_node_dic

def canReach(start_name, target_name, nick_ind_dic, ind_node_dic):
    """
    start_name[str]
    target_name[str]
    check if start can reach target 
    """
    start_index = nick_ind_dic[start_name]
    target_index = nick_ind_dic[target_name]
    qu = [start_index]

    while qu:
        node = ind_node_dic[qu.pop(0)]
        for ad in node.adjacency:
            if ad == target_index:
                return True
            else:
                qu.append(ad)
    return False


parser = argparse.ArgumentParser()
parser.add_argument("--links", required = "True")
parser.add_argument("--nicknames", required = "True")
parser.add_argument("--start", required = "True")
parser.add_argument("--target", required = "True")
args = parser.parse_args()

links_path = args.links
nicknames_path = args.nicknames
nick_ind_dic, ind_node_dic = readGraph(links_path, nicknames_path)
start_name = args.start
target_name = args.target
ans = canReach(start_name, target_name, nick_ind_dic, ind_node_dic)
print(ans)
