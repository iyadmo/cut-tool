import sys

if len(sys.argv)==3:
 with open(sys.argv[2],"r") as f:

    if len(sys.argv[1])==3:
     arg=int(sys.argv[1][2])
     for line in f:
        field=line.strip().split("\t")
        print(field[arg-1])
        
    if len(sys.argv[1])>3:    
     for line in f:
      field=line.strip().split("\t")
      i=2
      while i+1<=len(sys.argv[1]):
          arg=int(sys.argv[1][i])
          print(field[arg-1],end="\t")
          i=i+2
      print()

    
elif len(sys.argv)==4:
    with open(sys.argv[3],"r") as f:
     
     arg=int(sys.argv[1][2])
     delimiter= sys.argv[2][2]
     for line in f:
        field=line.strip().split(delimiter)
        print(field[arg-1])
     



   

    
    

                                 