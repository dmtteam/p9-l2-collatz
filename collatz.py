#import sys

# x=0
while True:
    print('Lets check the length of the Collatz sequence before it reaches one! \nEnter a starting number: 1-100')
    x = int(input())
    first = x
    if x == 0 or x > 100:
        print('The number should be in the range 1-100. Try Again!')
        continue
    step = 0
    counter = 0
    while True:
        step += 1

# b=int(sys.argv[1])
# for y in range(b):

        if x == 1:

# counter = counter-1

            counter += 1
            print("The length of the string until it reaches one is:", counter, ", when it starts with a number:", first)
            break

        if x % 2 == False:
            x = (x/2)
            print(x)
            counter += 1
        else:
            x = (3 * x+1)
            print(x)
            counter += 1
            print('The current string length is:', counter+1, '(I keep counting)...')
            continue
    print("End")
    break

# print('End of declared mileage sys.argv[1]')
