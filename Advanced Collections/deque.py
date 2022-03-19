# deque objects are like double-ended queues
import collections
import string

def main():
    # initialise a new deque
    d = collections.deque(string.ascii_letters)
    print(d)

    print("item count", str(len(d)))

    #iterating over a deque
    # for elem in d:
    #     print(elem.upper(), end=",")

    d.pop() # removes last item
    d.popleft() #removes first item
    d.append(2) #adds 2 to the end
    d.appendleft(3) #adds 3 to the left/start
    #print(d)

    #rotate the deque
    d.rotate(10) #rotates by 10 spaces clockwise (right)
    print(d)


if __name__ == '__main__':
    main()