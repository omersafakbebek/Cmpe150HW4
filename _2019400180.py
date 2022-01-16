
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
if x==0:
    print("YOU WON!")
t=0
mesafe=0
if y%2==0:
    spaceship=(y//2)-1
else:
    spaceship=y//2
frame=[]
for i in range(x+g+1):
    row=[]
    for m in range(y):
        if i<mesafe:
            row.append(" ")
        if i>=mesafe and i<x+mesafe:
            row.append("*")
        if i>=x+mesafe and i<x+g:
            row.append(" ")
        if i==x+g:
            if m==spaceship:
                row.append("@")
            else:
                row.append(" ")
    frame.append(row)
for k in frame:
    for m in k:
        print(m,end="")
    print()
print(72*"-")
score=0
while(x>0):
    command=input("Choose your action!\n")
    command=command.lower()
    if command=="right":
        if spaceship==y-1:
            pass
        else:
            frame[-1][spaceship]=" "
            frame[-1][spaceship+1]="@"
            spaceship=spaceship+1
    if command=="left":
        if spaceship==0:
            pass
        else:
            frame[-1][spaceship]=" "
            frame[-1][spaceship-1]="@"
            spaceship = spaceship - 1
    if command=="fire":
        for i in range(g+x):
            if frame[-i-2][spaceship]=="*":
                frame[-i-2][spaceship]=" "
                if i>0:
                    frame[-i-1][spaceship]=" "
                score=score+1
                break
            else:
                if i>0:
                    frame[-i-1][spaceship]=" "
                frame[-i-2][spaceship]="|"
            for k in frame:
                for m in k:
                    print(m, end="")
                print()
            print(72 * "-")
    if frame[0][spaceship]=="|":
        frame[0][spaceship]=" "
    if command=="exit":
        for k in frame:
            for m in k:
                print(m, end="")
            print()
        print(72 * "-")
        break
    t=t+1
    if t%5==0 and t>0:
        if "*" in frame[-2]:
            print("GAME OVER")
            for k in frame:
                for m in k:
                    print(m, end="")
                print()
            print(72 * "-")
            break
        else:
            l=y*[" "]
            frame.insert(0,l)
            frame.pop(-2)
    a=0
    for i in frame:
        for k in i:
            if k=="*":
                a=1
    if a==0:
        print("YOU WON!")
        for k in frame:
            for m in k:
                print(m, end="")
            print()
        print(72 * "-")
        break
    for k in frame:
        for m in k:
            print(m, end="")
        print()
    print(72 * "-")
print("YOUR SCORE:",score)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
