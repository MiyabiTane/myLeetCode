from readGraph import readGraph

def usingKeyword(keyword, nick_ind_dic, ind_node_dic):
    """
    keywordのページからkeywordを含むページだけでいくつ繋がれるか
    どこまで遠くに行けるか
    """
    start_index = nick_ind_dic[keyword]
    qu = [start_index]
    #node.valueを遠さの指標として利用
    ind_node_dic[start_index].value = 0
    
    visited_edge = -1
    max_value = 0
    while qu:
        node = ind_node_dic[qu.pop(0)]
        cur_value = node.value
        if node.visited == False:
            for ad in node.adjacency:
                ad_node = ind_node_dic[ad]
                if keyword in ad_node.nickname:
                    ad_node.value = cur_value + 1
                    if ad_node.value > max_value:
                        max_value = ad_node.value 
                    qu.append(ad)
            node.visited = True
            visited_edge += 1
        
    print("from ", keyword, ", you can access ", visited_edge, "pages")
    print("You can access", max_value, "pages ahead only using", keyword)


links_path = "links2.txt"
pages_path = "pages.txt"
page_ind_dic, ind_node_dic = readGraph(links_path, pages_path)
keyword = "バドミントン"
usingKeyword(keyword, page_ind_dic, ind_node_dic)
