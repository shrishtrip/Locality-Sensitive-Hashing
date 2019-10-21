import csv

file = open('mxm_dataset_test.txt','r')


train = {}


def check(ls,j):
    for tup in ls:
        tup = str(tup)
        # print(type(tup),"\n")
        temp_ls = tup.split(':')
        if int(temp_ls[0]) == int(j):           ###  check for \n in the last entry
            return int(temp_ls[1])
    return int(-1)


for each in file:       ##create a train ditionary
    record = each.split(',')
    # print(record)
    s = record[0]
    ls = record[2:]
    # print(ls)
    train[s] = ls
    # print(train)


N=int(len(train))
print("train made with size:",N)


cnt = int(0)
w = csv.writer(open("binary_doc_vector.csv", "w",newline=''))


for each in train:      #calculate tf-idf score
    cnt = cnt + 1
    print(cnt)
    # if cnt > int(10):
    #     break
    print("************************\n")
    print("\n","vector making start ", each,":")
    ls_final = []
    # ls = []
    ls_final.append(each)
    for j in range(5000):
        # print("iteration no:",j," ")
        # temp = float(tf_idf(each,j))
        # print(" ",temp," ")
        temp = check(train[each],j+1)
        if temp != -1:
            ls_final.append(int(1))
        else:
            ls_final.append(int(0))
    w.writerow(ls_final)





