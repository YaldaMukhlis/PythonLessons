
for num in range(1,6):
    print (num)

note = "(range) is a tabe."

nums = list(range(1,10))
print (nums)

nums = list(range(2,11,2))
print (nums)
note = "we can type even and odd numbers"

nums = []
for num in range(2,11,2):
    square = num**2
    nums.append(square)

print (nums)

minimum = [105,10,40]
print (min(minimum))

note = "we can take minimum number with (min)"

maximum = [140,25,45]
print (max(maximum))

note = "we can take maximum number with (max)"

plus = [165,11,47]
print (sum(plus))

note = "we can take sum number with (sum)"

nums = [num**2 for num in range(2,21,2)]
print (nums)