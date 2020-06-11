import argparse
from readGraph import readGraph
# ALEXNOTE: nice that you imported the common code!

def canReach(start_name, target_name, nick_ind_dic, ind_node_dic):
    """
    check if start can reach target 

    start_name[str]
    target_name[str]
    nick_ind_dic[dict] key: nickname, value: index
    ind_node_dic[dict] key: index, value: Node 
    """
    start_index = nick_ind_dic[start_name]
    target_index = nick_ind_dic[target_name]
    qu = [start_index]

    visited_edge = 0
    while qu:
        node = ind_node_dic[qu.pop(0)]
        if node.visited == False:
            for ad in node.adjacency:
                if ad == target_index:
                    print(visited_edge)
                    return True
                else:
                    qu.append(ad)
            node.visited = True 
            visited_edge += 1   
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
