n = int(input("Enter n: "))

mainlist = []
for i in range(1, n+1):
    sublist = [i]
    current = i  # Use a separate variable to track the Collatz sequence
    while current != 1:  # Convention is to stop at 1, not 4
        if current % 2 == 0:
            current = current // 2  # Integer division to avoid floats
        else:
            current = current * 3 + 1
        sublist.append(current)
    mainlist.append(sublist)

mydict = {}

for item in range(len(mainlist)):
    for num in mainlist[item]:
        if num in mydict:
            mydict[num] += 1
        else:
            mydict[num] = 1

sortedlist = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
for i in range(min(10, len(sortedlist))):  # Added safeguard if there are fewer than 10 items
    print(f"{int(sortedlist[i][0])} : {sortedlist[i][1]}")