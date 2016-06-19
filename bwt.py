# -*- coding:UTF-8 -*-

# 巡回シフト
def cyclic_shift(name):
    arr = []
    for i in range(len(name)):
        arr.append(name[i:] + name[:i])
    return arr

# 辞書順にソート
def lexical_order_sort(arr):
    return sorted(arr)

# Lを取得
def get_L(arr_sort):
    n = len(arr_sort[0])
    result = ""
    for string in arr_sort:
        result = result + string[n-1]
    return result

# Fを取得
def get_F(arr_sort):
    n = len(arr_sort[0])
    result = ""
    for string in arr_sort:
        result = result + string[0]
    return result

# 元の文字列と等しい行(row)の番号を取得
def get_same_str_row_num(arr_sort, target):
    for i in range(len(arr_sort)):
        if arr_sort[i] == target:
            return i

# targetという文字よりも小さい文字の出現回数を返す
def C(target, string):
    return string.find(target)

# targetという文字がbeginとendの中で何回出現するか取得
def occ(target, begin, end, string):
    count = 0
    for i in range(begin, end):
        if string[i] == target:
            count = count + 1
    return count

# LF_mapping
def LF_mapping(L, F, i):
    return C(L[i], F) + occ(L[i], 0, i, L)

# bwt変換した文字列を逆変換して返す
def reverse(L, F):
    result = ""
    for i in range(len(L)):
        if i == 0:
            result = L[0]
            index = LF_mapping(L, F, i)
        else:
            result = result + L[index]
            index = LF_mapping(L, F, index)
    result = result[::-1]
    return result[1:]

if __name__ == "__main__":
    #print "please input string"
    #string = raw_input() + "$"
    #print "please input target string for search"
    #search_str = raw_input()

    string = "~~$"

    # 巡回シフト
    arr = cyclic_shift(string)
    print "巡回シフト"
    for i in arr:
        print i

    # 辞書順にソート
    arr_sort = lexical_order_sort(arr)
    print "辞書順にソート"
    for i in arr_sort:
        print i

    # n番目の列を取得
    L = get_L(arr_sort)
    print "L : " + L

    # Fを取得
    F = get_F(arr_sort)
    print "F : " + F

    # 元の文字列と等しい行(row)の番号を取得
    same_str_row_num = get_same_str_row_num(arr_sort, string)
    print same_str_row_num

    print reverse(L, F)
