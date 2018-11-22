import sys

#Gets the order of G(X) and pass it to the append function
def getOrder(G):
    pos = G.find('1')
    y = G[pos:]
    order = len(y)-1
    #print(order)
    return order

#Recieve the order of G(X) and add zeros to F(X)
def append(G,F):
    order = getOrder(G)
    for i in range(order):
        F+="0"
    return F

#Perform XOR operation
def XOR(b1,b2):
    if len(b1)>len(b2):
        b1 = b1[:len(b2)]
    x = len(b2)
    answer = ""
    for i in range(x):
        if(b1[i] == b2[i]):
            answer+="0"
        else:
            answer+="1"
    return answer

#Perform the long division operation
def longDiv(F,G):
    # F = "10011101"
    # G = "1001"
    op = append(G,F)
    #print(op)
    res1 = XOR(op,G)
    op1 = res1
    x = (len(op)-len(G))
    if op1[0] == "0":
        dev = "0" * len(G)
    else:
        dev = G
    #print(x)
    for i in range(x):
        # print(i)
        op2 = op1[1:]+op[i+len(G)]
        if op2[0] == "0":
            dev = "0" * len(G)
        else:
            dev = G
        #print(str(op2) + " XOR " + str(dev))
        op1 = XOR(op2,dev)
        #print(op1)
    rem = op1[1:]
        #print(str(len(op1)) + " " + str(len(dev)))
    message = F+str(rem)
    return message

def generator(infile):
    infile = open(infile, "r")
    args=[]
    for line in infile:
        args.append(line.split()[0])
    F = args[0]
    G = args[1]
    res = longDiv(F,G)
    outfile = open("transmitted_message.txt","w")
    outfile.write(res)
    print("Message is correct")

def alter(infile):
    infile = open(infile, "r")
    args=[]
    for line in infile:
        args.append(line.split()[0])
    F = args[0]
    G = args[1]
    res = longDiv(F,G)
    outfile = open("transmitted_message.txt","w")
    outfile.write(res)
    print("Message is not correct")



def main():
    # x = append("10011","1101011111")
    # print(x)
    # answer = XOR("1101011111","10011")
    # print(answer)
    # devAns = longDiv("10011101","1001")
    # print(devAns)
    if sys.argv[3] == "verifier":
        generator(sys.argv[2])
    else:
        alter(sys.argv[2])

if __name__ == "__main__":
    main()
