def birthdayCakeCandles(x):
    blow_candle=max(x)
    num=0
    for i in x:
        if i==blow_candle:
            num+=1
    return num


#https://www.hackerrank.com/challenges/birthday-cake-candles/problem