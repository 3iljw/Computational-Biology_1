tmax = 0
chro = 0

def sort(chro,tmax) :
    print ('------ sorting ------')

    TS =[[None]*3 for i in range (1)]
    ##freq          ## recode comparison location
    record=0        ## recode orgin location
    comrec=0        ## recode first different data
    while record < tmax :
        a=0         ## recode string similar or different
        for freq in range (record+1,tmax):
            if str(chro[record][0]) == str(chro[freq][0]) :
                if a == 1 :
                    for ts in range (0,3):
                        TS[0][ts] = chro[comrec][ts]
                        chro[comrec][ts] = chro[freq][ts]
                        chro[freq][ts] = TS[0][ts]
                    a=0
                    record = comrec
                    break
                elif a == 0 and freq == tmax-1 :
                    record = tmax + 1                               ### comparison end
            else :
                if a==1 and freq == tmax-1 :
                    record = comrec
                    break
                elif a==0 :
                    comrec = freq
                    a=1
            if freq == tmax-1 and comrec == freq :                  ####comparison end
                record = tmax + 1
                break

def re_organize(chro,tmax) :
    print ('------ organizing ------')

    for num1 in range(0,tmax):
        if chro[num1][1] > chro[num1][2] :
            change1 = chro[num1][1]
            chro[num1][1] = chro[num1][2]
            chro[num1][2] = change1

#            change2 = chro[num1][4]
#            chro[num1][4] = chro[num1][5]
#            chro[num1][5] = change2

def merge(d,tmax) :
    print ('------ merging ------')
    for num1 in range(0,tmax):
        #print(' => ' + str((num1+1.0)*100 / (tmax + 1)) + '%')
        for num2 in range(0,tmax):
            try:
                if d[num1][0]==d[num2][0] and num1!=num2:
                    if (int(d[num1][1])<=int(d[num2][1])) and (int(d[num1][2])<=int(d[num2][2])) and (int(d[num1][2])>=int(d[num2][1])):
                        d[num1][2]=d[num2][2]
                        del d[num2]
                        num2=num2-1
                        continue
                    elif (int(d[num1][1])<=int(d[num2][1])) and (int(d[num1][2])>=int(d[num2][2])):
                        del d[num2]
                        num2=num2-1
                        continue
                    elif (int(d[num1][1])>=int(d[num2][1])) and (int(d[num1][2])<=int(d[num2][2])):
                        d[num1][1]=d[num2][1]
                        d[num1][2]=d[num2][2]
                        del d[num2]
                        num2=num2-1
                        continue
                    elif (int(d[num1][1])>=int(d[num2][1])) and (int(d[num1][2])>=int(d[num2][2])) and (int(d[num1][1])<=int(d[num2][2])):
                        d[num1][1]=d[num2][1]
                        del d[num2]
                        num2=num2-1
                        continue
            except:
                continue



def main ():

    #   read data from original file

    #f = open ('ar_e5')         ### real data
    f = open ('testtext')       ### test data
    t = f.read()

    #   split and arrange it

    t = t.split("\n")
    t.pop()
    tmax = len(t)               #tmax = data quantity

    chro=[[None]*3 for i in range(tmax)]
    for num1 in range(0,tmax):
        d = t[num1].split(",")
        chro[num1][0]=d[1]   # chr name
        chro[num1][1]=d[8]   # chr start
        chro[num1][2]=d[9]   # chr end

#        chro[num1][3]=d[0]   # gene name
#        chro[num1][4]=d[6]   # gene start
#        chro[num1][5]=d[7]   # gene end

    sort(chro,tmax)

    re_organize(chro,tmax)

    merge(chro,tmax)

    #   write data into new file

    newfile = open('testdata','w')
    for i in range(0,tmax):
        datastring = ",".join(chro[i])
        newfile.write(datastring)
        newfile.write('\n')

if __name__ == '__main__':
    main()
