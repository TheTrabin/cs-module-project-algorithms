#pylint: disable=too-many-arguments

'''
Input: an integer
Returns: an integer

Recursion.

Will hang if not optimised.

Can eat 3 cookies 4 ways.

if n = 3

 1. He can eat 1 cookie at a time 3 times
 2. He can eat 1 cookie, then 2 cookies 
 3. He can eat 2 cookies, then 1 cookie
 4. He can eat 3 cookies all at once. 

n = jar of cookies

## Hints from ReadMe
 * Since this question is asking you to generate a bunch of possible permutations, you'll probably want to use recursion for this.
 * Think about base cases that we would want our recursive function to stop recursing on. How many ways are there to eat 0 cookies? What about a negative number of cookies? 
 * Once we've established some base cases, how can we recursively call our function such that we move towards one or more of these base cases?
 * As far as performance optimizations go, 
 caching/memoization might be one avenue we could go down? 
 How should we make a cache available to our recursive function through multiple recursive calls?


Search Cache Cases.

Cache simply is a store, information held for later time.

memoization: Term coined by Donald Michie as in Memorandum, to be remembered. Again, simple case of Storing Information.


Standard form of Memoization via fibonacci formulae:

def fibonacci(input):
    if input == 1:
        return 1
    elif input == 2:
        return 1
    elif input > 2:
        return fibonacci(input -1) + fibonacci (input -2)

for i in range(1, 11):
    print ("fib({}) = ".format(i), fibonacci(i))


Add Cache:

fibonacci_cache = {}

def fibonacci_memo(input):
    if input in fibonacci_cache:
        return fibonacci_cache[input]
    if input == 1:
        value = 1
    elif input == 2:
        value = 1
    elif input > 2:
        value = fibonacci_memo(input -1) + fibonacci_memo(input -2)
    fibonacci_cache[input] = value
    return value

    So, Form it from there.

cookie_jar = {}

def eating_cookies(n):
    # Your code here
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = eating_cookies(n -1) + eating_cookies(n -2)
    cookie_jar[n] = value <~~~ Is the issue.
    return value
    # pass

    Fails 2 tests.
The error states too-many-function-args
    eating cookies can't handle it.

cookie_jar = cache

def eating_cookies(n):
    if n == 0:
        cache = 1
    elif n < 0:
        cache = 1
    elif cache[n] > 0:
        return cache[n]
    else:
        cache[n] = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
        return cache[n]

Takes 1 arg, 2 were given.

def cookie_jar(f):
    jar = {}
    def helper(n):
        if n not in jar:
            jar[n] = f(n)
        return cookie_jar
    return helper

@cookie_jar
def eating_cookies(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    
    else:
        jar[n] = eating_cookies(n - 1, jar) + eating_cookies(n - 2, jar) + eating_cookies(n - 3, jar)
        return jar[n]

    Attempted refactor. On the right track.

def eat(n):
    nom = 0

    if n == 0:
        return 1
    if n < 0:
        return 0
    if n > 2:
        nom += eat(n-3)
    if n > 1:
        nom += eat(n-2)
    if n > 0:
        nom += eat(n-1)
    return nom

def eating_cookies(n, jar=None):
    if jar is None:
        return eat(n)
    for i in range(3):
        jar[i] = eating_cookies(i+1)
    for i in range(3, len(jar) - 1):
        jar[i] = jar[1-3] + jar[i-2] + jar[i-1]

    return jar[-2]

    Passes small, not large.





def eating_cookies(n, cache):
    cache = {}
    if n < 2:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return eating_cookies(n -1, cache) + eating_cookies(n -2, cache) + eating_cookies(n - 3, cache)
'''

def eating_cookies(n):
    if n == 0:
        return 1
    elif n < 1:
        return 0
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)




if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
