import random
import numpy as np
from porter2stemmer import Porter2Stemmer

file = open('sample.csv','r')


train = {}              # original data
signature_dic = {}      # data after min hash
signature_query = []
list_buckets = []       # list if buckets
param_euclidean = []
param_dic = {}
param_dic1 = {}
param_dic2 = {}


b = 3                   # no of bands
r = 2                   # no of elements in each band


def eulcidean():        # LSH for euclidean distance
    j = int(0)
    temp = []
    # print(list_buckets)
    list_buckets.clear()
    # print(list_buckets)
    for i in range(b):
        buckets = {}
        # print(i)
        u = np.random.normal(0, 1, r)
        # print(u)
        bias = random.randint(0,b)
        # param_dic[u]=b
        # print(bias)
        temp.append(u)
        temp.append(b)
        param_dic[i]=temp
        for each in signature_dic:
            sig = np.asarray(signature_dic[each])
            # print(sig)
            sig = sig[j:j+r]
            sig = sig.tolist()
            # print((sig))
            c = [a * b for a, b in zip(u, sig)]
            # print(c)
            c = float(sum(c))
            # print(c)
            h = float(c)/float(b)
            h = h + float(bias)
            # print("hash value",h)
            # if i==0 and len(buckets)==0:
            #     ls = []
            #     ls.append(each)
            #     buckets[h]=ls
            if h in buckets:
                ls = buckets[h]
                ls.append(each)
                buckets[h] = ls
            else:
                ls = []
                ls.append(each)
                buckets[h] = ls

        j += r
        list_buckets.append(buckets)
    param_euclidean.append(param_dic)
    return list_buckets

def query_euclidean(sig_query,list_buckets):
    j = int(0)
    for i in range(b):
        buckets = {}
        # print(i)
        u = param_dic[i][0]
        # print(u)
        bias = param_dic[i][1]
        # print(bias)
        sig = sig_query[j:j + r]
        # print((sig))
        c = [a * b for a, b in zip(u, sig)]
        # print(c)
        c = float(sum(c))
        # print(c)
        h = float(c) / float(b)
        h = h + float(bias)
        # print("hash value",h)
        # if i==0 and len(buckets)==0:
        #     ls = []
        #     ls.append(each)
        #     buckets[h]=ls
        buckets=list_buckets[i]
        if h in buckets:
            ls = buckets[h]
            ls.append('Query')
            buckets[h] = ls
            list_buckets[i]=buckets
        else:
            ls=['Query']
            list_buckets[i][h]=ls
        j += r
    return list_buckets

def hemming():                      # LSH for hemming distance
    j = int(0)
    # print(list_buckets)
    list_buckets.clear()
    # print(list_buckets)
    for i in range(b):
        buckets = {}
        # print(i)
        bit = random.randint(0, r-1)
        param_dic1[i]=bit
        # u = np.random.normal(0, 1, r)
        # print(u)
        # bias = random.randint(0,b)
        # print(bias)
        for each in signature_dic:
            sig = np.asarray(signature_dic[each])
            # print(sig)
            sig = sig[j:j+r]
            sig = sig.tolist()
            h = sig[bit]
            # print("hash value",h)
            # if i==0 and len(buckets)==0:
            #     ls = []
            #     ls.append(each)
            #     buckets[h]=ls
            if h in buckets:
                ls = buckets[h]
                ls.append(each)
                buckets[h] = ls
            else:
                ls = []
                ls.append(each)
                buckets[h] = ls

        j += r
        list_buckets.append(buckets)
    return list_buckets

def query_hemming(sig_query,list_buckets):
    j = int(0)
    for i in range(b):
        buckets = {}
        bit=param_dic1[i]
        sig = sig_query[j:j + r]
        # print((sig))
        h = sig[bit]
        # print("hash value",h)
        # if i==0 and len(buckets)==0:
        #     ls = []
        #     ls.append(each)
        #     buckets[h]=ls
        buckets=list_buckets[i]
        if h in buckets:
            ls = buckets[h]
            ls.append('Query')
            buckets[h] = ls
            list_buckets[i] = buckets
        else:
            ls = ['Query']
            list_buckets[i][h] = ls
        j += r
    return list_buckets

def signum():        # LSH for signum distance
    j = int(0)
    temp = []
    # print(list_buckets)
    list_buckets.clear()
    # print(list_buckets)
    for i in range(b):
        buckets = {}
        # print(i)
        u = np.random.normal(0, 1, r)
        # print(u)
        param_dic2[i]=u
        for each in signature_dic:
            sig = np.asarray(signature_dic[each])
            # print(sig)
            sig = sig[j:j+r]
            sig = sig.tolist()
            # print((sig))
            c = [a * b for a, b in zip(u, sig)]
            # print(c)
            c = float(sum(c))
            # print(c)
            if c>0:
                h=float(1)
            elif c<0:
                h=float(-1)
            else:
                h=float(0)
            # print("hash value",h)
            # if i==0 and len(buckets)==0:
            #     ls = []
            #     ls.append(each)
            #     buckets[h]=ls
            if h in buckets:
                ls = buckets[h]
                ls.append(each)
                buckets[h] = ls
            else:
                ls = []
                ls.append(each)
                buckets[h] = ls

        j += r
        list_buckets.append(buckets)
    return list_buckets

def query_signum(sig_query,list_buckets):
    j = int(0)
    for i in range(b):
        buckets = {}
        # print(i)
        u = param_dic2[i]
        # print(bias)
        sig = sig_query[j:j + r]
        # print((sig))
        c = [a * b for a, b in zip(u, sig)]
        # print(c)
        c = float(sum(c))
        # print(c)
        if c > 0:
            h = float(1)
        elif c < 0:
            h = float(-1)
        else:
            h = float(0)
        # print("hash value",h)
        # if i==0 and len(buckets)==0:
        #     ls = []
        #     ls.append(each)
        #     buckets[h]=ls
        buckets = list_buckets[i]
        if h in buckets:
            ls = buckets[h]
            ls.append('Query')
            buckets[h] = ls
            list_buckets[i] = buckets
        else:
            ls = ['Query']
            list_buckets[i][h] = ls
        j += r
    return list_buckets

def give_doc_number(s, ls):                 # returns the dimension_no of the first occurrence of 1
    for i in range(dimension):
        index = ls.index(i)
        temp = train[s]
        var = int(temp[index])
        if var == int(1):
            return i+1

    return -1

def give_query_hash(q, ls):                 # returns the dimension_no of the first occurrence of 1
    for i in range(dimension):
        index = ls.index(i)
        var = int(q[index])
        if var == int(1):
            return i+1

    return -1

dimension = 0
for each in file:                   # create a train dictionary
    record = each.split(',')
    # print(record)
    s = record[0]
    ls = record[1:]
    # print(ls)
    if dimension == 0:
        dimension = len(ls)
    train[s] = ls
    # print(train)


# print(train)


no_of_doc = len(train)
no_of_permutations = dimension/2

permutations = []

for i in range(int(no_of_permutations)):
    ls = np.random.permutation(dimension)
    ls = ls.tolist()
    permutations.append(ls)

for each in train:              # doing the min_hash for reducing the signature matrix
    signature = []

    for ls in permutations:
        val = give_doc_number(each, ls)
        if val == -1:
            print('Error')
            quit()
        signature.append(val)

    signature_dic[each] = signature

words = open("words.txt","r")   #opening words file
a=words.read().split(',')
dict={}
for k in range(1,dimension+1):
    dict[a[k-1]]=k           #creating dictionary of word-index pairs
query=input().lower()    #getting query from user and converting to lowercase
#normalisation and tokenisation of query
query = query.replace("'m ", " am ")
query = query.replace("'re ", " are ")
query = query.replace("'ve ", " have ")
query = query.replace("'d ", " would ")
query = query.replace("'ll ", " will ")
query = query.replace(" he's ", " he is ")
query = query.replace(" she's ", " she is ")
query = query.replace(" it's ", " it is ")
query = query.replace(" ain't ", " is not ")
query = query.replace("n't ", " not ")
query = query.replace("'s ", " ")
punctuation = (',', "'", '"', ",", ';', ':', '.', '?', '!', '(', ')','{', '}', '/', '\\', '_', '|', '-', '@', '#', '*')
for p in punctuation:
    query = query.replace(p, '')
query=query.split()
#stemming of tokens
stemmer=Porter2Stemmer()
query=[stemmer.stem(q) for q in query]
q_vector=[]
for k in range(dimension):
    q_vector.append(int(0))      #initialising query's tf-idf vector (q_vector)
n=len(query)
for k in range(n):
    if query[k] in dict:
        q_vector[dict[query[k]]-1]=1
q_vector=[0,0,1,1,0,1,1,1,0,0,1,1]
for ls in permutations:
    val = give_query_hash(q_vector,ls)
    if val == -1:
        print('Error')
        quit()
    signature_query.append(val)

list_euclidean = eulcidean()
list_euclidean = query_euclidean(signature_query,list_euclidean)
print("Euclidean Distance")
for each in list_euclidean:
    for name in each:
        print(each[name], end="")
    print("\n")
docs=[]
for each in list_euclidean:
    for name in each:
        if 'Query' in each[name]:
            docs+=each[name]
            break
docs=list(set(docs))
docs.remove('Query')
print(docs)

print("\n")
list_hemmming = hemming()
list_hemmming = query_hemming(signature_query,list_hemmming)
print("Hamming Distance")
for each in list_hemmming:
    for name in each:
        print(each[name], end="")
    print("\n")

for each in list_hemmming:
    for name in each:
        if 'Query' in each[name]:
            docs+=each[name]
            break
docs=list(set(docs))
docs.remove('Query')
print(docs)
print("\n")
list_signum = signum()
list_signum = query_signum(signature_query,list_signum)
print("Signum Distance")
for each in list_signum:
    for name in each:
        print(each[name], end="")
    print("\n")

for each in list_signum:
    for name in each:
        if 'Query' in each[name]:
            docs+=each[name]
            break
docs=list(set(docs))
docs.remove('Query')
print(docs)


