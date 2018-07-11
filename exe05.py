#-*-coding:utf-8-*-

type = 10
x = f"There are {type}types of people"

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not} know"

print(x)
print(y)

print(f"If I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke = "Isnot that joke so funny? {}"
print(joke.format(hilarious))

w = "my cat"
e = "is cute"
print(w+e)

