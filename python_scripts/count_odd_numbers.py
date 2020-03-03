#!/usr/local/bin/python3.6
count=0
while count < 10:
    if count % 2 == 0:
        count +=1
        continue
    print(f"We're counting the odd numbers: {count}")
    count +=1
