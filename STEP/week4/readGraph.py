class Node:

    def __init__(self, nickname):
        self.visited = False
        #followしている人（自分->相手）
        self.adjacency = []
        self.value = 100
        self.nickname = nickname


def readGraph(links_path, nicknames_path):
    """
    output
    nick_ind_dic[dict] key: nickname, value: index
    ind_node_dic[dict] key: index, value: Node 
    """
    #.txtファイルからグラフの情報を取得
    #ニックネームとインデックスの関係の取得
    nick_ind_dic = {}
    ind_node_dic = {}
    nicknames_file = open(nicknames_path, "r", encoding="utf_8")
    while True:
        read_word = nicknames_file.readline().split("\t")
        if len(read_word) < 2:
            break
        index = int(read_word[0])
        nickname = read_word[1][:-1]
        nick_ind_dic[nickname] = index
        ind_node_dic[index] = Node(nickname)
    #辺の情報の取得
    links_file = open(links_path, "r", encoding="utf_8")
    while True:
        read_word = links_file.readline().split("\t")
        if len(read_word) < 2:
            break
        index = int(read_word[0])
        link = int(read_word[1][:-1])
        ind_node_dic[index].adjacency.append(link)
    #print(nick_ind_dic)
    #print(ind_node_dic[0].visited)
    return nick_ind_dic, ind_node_dic
