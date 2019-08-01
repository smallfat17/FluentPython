import bisect

a = [0, 1, 3, 5, 7, 8, 10, 15, 21]
b = [2, 9, 11, 13, 15, 20, 21, 25]

s = " ".join(str(a) for a in a)
print(" ",s)
for i in range(len(b)):
    index = bisect.bisect(a, b[i])
    print('| '*index , str(b[i]))

#查找成绩对应评级   如果使用bisect_left，刚好等于70分则被识别为D
def grade(score, breakpoints=[60, 70, 80, 90], grades="FDCBA"):
    index = bisect.bisect_right(breakpoints, score)
    return grades[index]

for score in [22, 77, 59, 80, 100, 99]:
    print(grade(score))

bisect.insort()


