import random

'''  z clonnig process and fun. that xst togzr  '''

# no bug


def ranomzzr(lst):
    llst2 = []
    while len(lst) != 0:
        x = random.randint(0, (len(lst) - 1))
        y = lst[x]
        lst.remove(y)
        llst2.append(y)
    return llst2

# no bug


def clone(org, clonee):
    g = clonee
    clonee = org[:]
    y = ranomzzr(clonee)
    return y


# no bug
def clone1(org):
    org = ranomzzr(org)
    return org[:]


# no bug
def lsttname(no):
    name_lst = []
    '''making up names'''
    for u in range(no):
        var = 'made_up_' + str(u)
        name_lst.append(var)
    return name_lst


# no bug
def list_of_clons(org, llen):
    lstlst = []
    lstclonernamelst = lsttname(llen)  # the list of clone names
    for i in range(llen):
        t = clone(org, lstclonernamelst[i])
        lstlst.append(t)
    return lstlst


''' permutation process fun. dfnshn '''


def permutation(alphabet, lngz):
    prmutd_lst = []
    combolst = list_of_clons(alphabet, lngz)
    for v in range(len(combolst)):
        vv = 'combo' + str(v)
        vv = combolst[v]
        prmutd_lst.append(vv)
    return prmutd_lst


ol = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
