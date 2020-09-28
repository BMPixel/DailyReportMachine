import register
import time

if __name__ == "__main__":

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    
    li = []
    with open("./Accounts.txt", "r") as f:
        l = f.readline()
        while l:
            pair = l.split()
            li.append((pair[0], pair[1]))
            l = f.readline()

    for t in li:
        print("### Start " + t[0])
        register.process(t[0], t[1])
        print("### Finish " + t[0])

    register.quit()

    print("# Complete!")