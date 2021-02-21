def collation(s,t):
    collection = []
    count = coll_r(s[1:],t,s[0],collection) + coll_r(s,t[1:],t[0],collection)
    print(f'number of results: {count}')
    return collection
    
def coll_r(s,t,r,col):
    if len(s) == 0 and len(t) == 0:
        col.append(r)
        return 1
    else:
        left_ct, right_ct = 0, 0
        if len(s) != 0: left_ct = coll_r(s[1:],t,r+s[0],col)
        if len(t) != 0: right_ct = coll_r(s,t[1:],r+t[0],col)
    return left_ct + right_ct
