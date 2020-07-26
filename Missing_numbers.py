def missingNumbers(arr, brr):
    
    req_arr = []
    a_dic = {}
    b_dic = {}

    for i in arr:
        if i not in a_dic:
            a_dic[i] = 1
        elif i in a_dic:
            a_dic[i] += 1
    
    for i in brr:
        if i not in b_dic:
            b_dic[i] = 1
        elif i in b_dic:
            b_dic[i] += 1 

    for b_key in b_dic:
        if b_key not in a_dic:
            req_arr.append(b_key)
        else:
            for a_key in a_dic:
                if b_key == a_key and b_dic[b_key] != a_dic[a_key]:
                    req_arr.append(b_key)
    req_arr.sort()
    return req_arr