R={}

R[0]=7
R[1]=7

Add ={0:("J",1,2,4), #somma
      1:("S",0),
      2:("S",2),
      3:("J",1,1,0)}

Sub ={0:("T",0,2), #sottrazione
      1:("Z",0),
      2:("J",1,2,6),
      3:("S",0),
      4:("S",1),
      5:("J",1,1,2)}

Sub_ = {0:("J",0,1,4),
        1:("S",1),
        2:("S",2),
        3:("J",0, 0, 0),
        4:("T",2,0)}

Mul ={0:("Z",2),
      1:("Z",3),
      2:("Z",4),
      3:("J",0,2,8),
      4:("J",1,3,11),
      5:("S",4),
      6:("S",2),
      7:("J",0,0,3),
      8:("S",3),
      9:("Z",2),
      10:("J",0,0,4),
      11:("T",4,0)}
      

def URM(prog,r):
    IR=0
    while IR < len(prog):
        print("IR=",IR)
        istr=prog[IR]
        IR=IR+1
        if istr[0] == "Z":
            r[istr[1]]=0
        if istr[0] == "S":
            if istr[1] in r.keys():
                r[istr[1]]=r[istr[1]]+1
            else:
                r[istr[1]]=1
        if istr[0] =="T":
            if istr[1] in r.keys():
                r[istr[2]]= r[istr[1]]
            else:
                r[istr[2]]=0
        if istr[0] =="J":
           if not istr[1] in r.keys():
               r[istr[1]]=0
           if not istr[2] in r.keys():
               r[istr[2]]=0
           if r[istr[1]]==r[istr[2]]:
               IR = istr[3]
    print(r)
    
URM(Sub_,R)


