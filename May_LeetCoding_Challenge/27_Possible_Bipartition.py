import collections
def possibleBipartition(N, dislikes):
    #人々を-1と1に塗り分ける。未決定のところは0。
    if N == 1 or not dislikes:
        return True

    dict_dislike = collections.defaultdict(list)
    for p1, p2 in dislikes:
        dict_dislike[p1-1].append(p2-1)
        dict_dislike[p2-1].append(p1-1)
    #print(dict_dislike)
    
    color_table = [0 for _ in range(N)]
    def helper(person_id, color):
        color_table[person_id] = color

        for disperson_id in dict_dislike[person_id]:
            if color_table[disperson_id] == color:
                return False
            #dis_pの色がperson_idと違うものになり得ない時
            if color_table[disperson_id] == 0 and (not helper(disperson_id, -color)):
                return False
        return True

    for person_id in range(N):
        #person_idをとある色に塗ることができるか
        if color_table[person_id] == 0 and (not helper(person_id, 1)):
            return False
    return True


ans = possibleBipartition(4, [[1,2],[1,3],[2,4]])
print(ans)




    

 
