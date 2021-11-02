import time

print("Pomodoro timer begins!")

for i in range (4):
    t = 25*60       # 25 minute break
    while t:
        mins = t // 60 
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(" " + timer, end="\r") 
        time.sleep(1)
        t -= 1

print("Take a break!")

t = 5*60        # 5 minute break
while t:
    mins = t // 60
    secs = t % 60
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r") 
    time.sleep(1)
    t -= 1
print("Back to Work!")
