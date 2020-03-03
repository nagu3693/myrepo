#!/usr/local/bin/python3.6
count=0
while count < 40:
    if count % 2 != 0:
        count += 1
        continue
    print(f"We're printing the even number: {count}")
    count += 2


