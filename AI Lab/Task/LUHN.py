def LUHN(card_num):
    sum=0
    for i in range(len(card_num)-1, -1 ,-1):
        a=int(card_num[i])

        if (len(card_num)-1)%2==0:
            a= a*2

        if a> 9 :
            a-= 9

        sum +=a

    if sum % 10 ==0:  
        print("THE CARD IS VALID")
    else:
        print('THE CARD IS INVALID')

card=input("ENTER THE CARD NUMBER")
LUHN(card)