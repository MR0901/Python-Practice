marksheet = []
scoresheet = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet += [[name,score]]
        scoresheet += [score]

lowest = seclowest = 200

for i in scoresheet:
    if lowest > i:
        seclowest = lowest
        lowest = i
    
    elif (i != lowest and seclowest > i):
        seclowest = i
    
for n,s in sorted(marksheet):
    if s == seclowest:
        print (n)