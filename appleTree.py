def countApplesAndOranges(s, t, a, b, apples, oranges):
    # s is the start point of the house on an x plain, and t is the endpoint.
    # a and b are the points where the apple and the orange trees are located respectivly.
    # apples: integer array, distances at which each apple falls from the tree.
    # orages: integer array, distances at which each apple falls from the tree.
    apple_hit = 0
    orange_hit = 0
    for i in apples:
        if a + i in range(s , t + 1):
            apple_hit += 1
    for i in oranges:
        if b + i in range (s , t + 1):  
            orange_hit +=1
    print(apple_hit)
    print(orange_hit)

#https://www.hackerrank.com/challenges/apple-and-orange/problem