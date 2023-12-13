import time
import os
s='''Sam loved to draw, but he wished he had a magic pencil that could make his 
    drawings come to life.One day, he found a shiny pencil in his backyard. 
    He decided to try it out and drew a big, friendly dog. 
    To his surprise, the dog jumped out of the paper and licked his face.   
    Sam was overjoyed and named him Spot. He drew more things with the magic pencil,
    like a bike, a cake, and a kite. He had so much fun with his new friends. 
    He decided to keep the magic pencil as his secret treasure. The End.'''
count=0
print("Your test will start in : please hit enter when done typing 😉")
for x in range(5,0,-1):
    m=int(x/60)%60
    so=x%60
    f=f"{m:02}:{so:02}"
    print(f"\r{f}",end='') 
    time.sleep(1)
os.system('cls')
print(s)
start=time.time()
t=input("Enter the text : ")
end=time.time()
c0=len(str(s).split())
c1=len(t.split())
s=list(str(s))
t=list(t)
for i in range(c1):
    if t[i]==s[i]:
        count+=1
acc=(count/c0)*100
wpm=(60*count)/(end-start)
print(f"Accuracy : {acc}%")
print(f"speed : {int(wpm)} wpm")