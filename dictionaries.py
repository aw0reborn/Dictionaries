### YOUR CODE FOR get_types_counts() FUNCTION GOES HERE ###
def get_types(d):
    docoments = []
    for i in d:
        docoments.append(i)
    return docoments
        


#### End OF MARKER


### YOUR CODE FOR get_types() FUNCTION GOES HERE ###
def get_types_counts(d):
    dic = {}
    for i in d:
        L = len(d[i])
        dic[i] = L
    return dic



#### End OF MARKER


### YOUR CODE FOR get_author_count() FUNCTION GOES HERE ###

def get_author_count(d,username,d_type=0):
    counter = 0
    
    for i in d:
        if d_type == 0:
            w = d[i]
        
            for a in w:
                q = a['author']
                if q['username'] == username:
                    counter += 1
        else: 
            for p in d_type:
                if i == p:
        
                    w = d[i]
        
                    for a in w:
                        q = a['author']
                        if q['username'] == 'jake':
                            counter += 1
    
    return counter    
  



#### End OF MARKER


