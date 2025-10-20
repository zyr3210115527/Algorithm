def findRelativeRanks(score):
    t=[]
    for i in score:
        t.append(i)
    t.sort()
    t.reverse()
    for i in range(len(score)):
        if score[i]==t[0]:
            score[i]="Gold Medal"
        if len(t)>1 and score[i]==t[1]:
            score[i]="Silver Medal"
        if len(t)>2 and score[i]==t[2]:
            score[i]="Bronze Medal"
        else:
            for s in range(3,len(t)):
                if t[s]==score[i]:
                    score[i]=str(s+1)
    return score
print(findRelativeRanks([3,5,1,7,2,8,6]))
