limit = input("Enter the Fibonacci limit:");
if limit != '':
    limitValue=int(limit);
    fibNumbers=[0,1];
    if limitValue==1:
        print("0");
    elif limitValue==2:
        print("0,1");
    elif limitValue>2:
        fibString="";
        for number in range(limitValue-2):
            index=len(fibNumbers);
            lastNum=fibNumbers[index-1];
            preNum=fibNumbers[index-2];
            fibNumbers.append(lastNum+preNum);
        for number in fibNumbers:
            fibString+=(str(number)+",")
        print(fibString[:-1])
