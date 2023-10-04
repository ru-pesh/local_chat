import threading
import os
#four functions are created for better performance and understandings
#below function (wr1) is used to write in a files.
def wr1():
    global a
    global chat
    f= open ('chat.txt','a+')
    chat= input('enter msg\n')
    ful_chat=a+': '+chat+'\n'
    f.write(ful_chat)
    f.close()
#
def chk1():
    while True:
        m=open('chat2.txt','r')
        ch=len(m.read())
        m.close()
        global ch1
        if int(ch)!= ch1:
            os.system('cls')
            print('\t\t\t\twelcome to chat')
            n = open('chat2.txt', 'r')
            print(n.read())
            n.close()
        ch1=ch
        
def write():
    wr1()

def check():
    chk1()

#MAIN CODE
print('\t\t\t\twelcome to chat')
f=open('chat.txt','a+')
g=open('chat2.txt','a+')
f.close()
g.close()
   
a=input('Enter your name to chat\n')
ch1=0
t1 = threading.Thread(target = check)
t1.start()

while True:
    k=open('chat.txt','r')
    j=open('chat2.txt','w')
    wr=k.read()
    j.write(wr)
    k.close()
    j.close()
    t2 = threading.Thread(target = write)
    t2.start()
    t2.join()
