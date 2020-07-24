#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)Linear O(n), as the size of the input increases, the runtime or space used will grow at the same rate


b)O(n log n) there is one for loop that will run through the range of n and w while loop that will run through half of n


c)O(n) this functon will run n times to sum the number of bunny ears for n bunnies

## Exercise II

Start by defining a middle variable
        finding the middle of the list of floors
        Drop the egg, if it doesnt break
        remove every floor below that
        continue the test of every floor above

Find the middle, drop, repeat. Until we come to our answer

This is also a binary search O(log n)
    divide in half and then the floors in half
