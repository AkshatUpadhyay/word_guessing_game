import random
def stringgenerate():
    a1="hello"
    a2="python"
    a3="jaypee"
    a4="mozilla"
    a5="father"
    a6="engineering"
    a7="codechef"
    a8="github"
    a9="programming"
    a10="pubg"
    a11="firefox"
    a=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11]
    x=random.choice(a)
    game(x)
def game(a):
    acopy=a
    b="*"*len(a)
    attempts=len(a)
    c=attempts
    w=" "*len(a)
    print b
    count=0
    success=0
    while 1:
        print "You have ",attempts," attempts left"
        print "Enter letter without cotes\n"
        ch=raw_input()
        x=a.find(ch)
        m=w.find(ch)
        if m!=-1:
            print "You guesses it already! its wrong"
            print "previous wrong guesses : "
            print w
            continue
        if x==-1:
            w=ch+w
            print "previous wrong guesses : "
            print w
            print "Wrong guess! try again"
            attempts=attempts-1
            print b
        else:
            print "Correct Guess!\n"
            b=b[0:x]+a[x]+b[x+1:c]
            a=a[0:x]+'*'+a[x+1:c]
            success=success+1
            print b
        if attempts==0:
            flag=1
            break
        if success==c:
            flag=0
            break
    if flag==0:
        print "Congrats! word is "
        print acopy
    else:
        print "Better luck next time"
    playagain()
def main():
    stringgenerate()
def playagain():
    print "If you want to play again,Press Y else no\n"
    ch=raw_input()
    if ch=='Y' or ch=='y':
        main()
    else:
        print "Thanks for playing the game!\n"
main()    
