def minion_game(string):
    s = string
    count1,count2 = 0,0
    for i in range(len(s)):
        if s[i] in "AEIOU":
            count1+=(len(s)-i)
        else:
            count2+=(len(s)-i)
    if (count1 > count2):
        print ("Kevin",count1)
    elif(count2 > count1):
        print ("Stuart",count2)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
