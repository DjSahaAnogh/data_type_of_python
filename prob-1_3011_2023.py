def num_into(integer):
	num1 = integer + 1
	num2 = integer - 1
	print(num1, " is the next of ", integer)
	print(num2, " is the before of ", integer)


num_into(5)

# 1. Print the numbers from 1 to 100
for x in range(1, 101):
	print(x)

# 2. Calculate the sum of the numbers from 1 to 10
total = 0
for num in range(1, 11):
	total += num
print(total)


def is_prime(number):
	if number <= 1:
		return False
	for i in range(2, int(number ** 0.5) + 1):
		if number % i == 0:
			return False
	return True


num = 2
if is_prime(num):
	print(num, "is a prime number")
else:
	print(num, "is not a prime number")
