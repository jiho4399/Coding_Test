# 방법1
import sys

print(sys.stdin.read())


# 방법2
while True:
    try:
        print(input())
    except EOFError:
        break