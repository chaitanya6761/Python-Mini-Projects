print "Please think of a number between 0 and 100!"
low=0
high=100
ans=(low+high)/2
while True :
    print "Is your secret number " +str(ans)+"?"
    x=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if x=='c':
        break
    elif x=='h' :
        high=ans
    elif x=='l' :
        low=ans
    else :
        print "Sorry, I did not understand your input."
    ans=(high+low)/2
print "Game over. Your secret number was: "+str(ans)