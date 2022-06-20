import serial
import matplotlib.pyplot as plt
import numpy as np
import time


#comPort=input("Com Port :- ")
#comPort="com"+comPort
arduinoData=serial.Serial('/dev/tty.wchusbserial1410',115200)
date_string = time.strftime("%d-%m-%y-%H:%M")
def is_Int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

flag=True
plt.ion()
plt.interactive(True)
plt.show()
def capture():
    a=[]
    count1=0
    myData1=0
    val1=0
    while True:
        while(arduinoData.inWaiting==0):
            pass
        myData1=arduinoData.readline()
        #print (myData1)
        #print 'a'
        #if(myData1[-1]=='\n'):
        myData1=myData1[:-2:]
        if(is_Int(myData1)):
            
            if(int(myData1)==3000):
                break
            else:
                myData1=float(myData1)
                myData1=(myData1*5)/1023
                myData1=myData1-2.5
                #myData1=(myData1*1068)/68
                if(count1==0) :
                    val1=myData1
                    myData1=myData1-val1
                else:
                    myData1=myData1-val1
                a.append(myData1)
                #print(count1, end = '')
                count1=count1+1
    n=0
    val1=[]
    while(n<2):
        while(arduinoData.inWaiting==0):
            pass
        myData1=arduinoData.readline()
        myData1=myData1[:-2:]
        if(is_Int(myData1)) :
            val1.append(int(myData1))
            n=n+1
    #print (val1[0])
    #print (val1[1])
    print('End')
    time1=np.linspace(0,val1[1]-val1[0],count1)
    #Try add into CSV 
    saveX = np.asarray(time1)
    saveY = np.asarray(a)
    print(len(saveX))
    np.savetxt('/Users/harshari/Desktop/SOSPictures/23DecSOSData/June2SingleMagnet/ComputeB_single/Xdata/singlemagnet' + date_string + '.csv', saveX, delimiter = ",")
    np.savetxt('/Users/harshari/Desktop/SOSPictures/23DecSOSData/June2SingleMagnet/ComputeB_single/Ydata/singlemagnet' + date_string + '.csv', saveY, delimiter = ",")
    plt.plot(time1,a,)
    #plt.plot(h,q,'b-')
    plt.grid(True)
    plt.ylabel('Voltage (in V)')
    plt.xlabel('Time (in ms) ')
    plt.title("Lenz Law demonstration")
    #plt.show()
    plt.show()
    plt.pause(.001)
#raw_input("<Hit Enter To Close>")
#matplotlib.pyplot.close()

print('Enter the number of plots you need')
counter = int(input())
for i in range(counter):
    print('plot number', i+1, )
    date_string = time.strftime("%d-%m-%y-%H:%M:%S")
    capture()
    plt.savefig('/Users/harshari/Desktop/SOSPictures/23DecSOSData/June2SingleMagnet/ComputeB_single/singleplot' + date_string + '.png',
                 timestamp=3, boldfont=1, textpos='bc')
    
    #Below is concerned with saving the csv
    #np.savetxt('/Users/harshari/Desktop/SOSPictures/23DecSOSData/CASE3_EndFixed/10.9cm/SOS_CSV ' + date_string + '.csv', saveX, delimiter = ",")
    
    #print(counter) 
#print('Type t if you need new plot')

    
#again = input()
#if(again=='t'):
#capture()


    
#if
''' 

    fig, ax1 = plt.subplots() # fig : figure object, ax : Axes object
    ax1.plot(time, a, 'r-')
    ax1.set_xlabel('x label')
    ax1.set_ylabel('y label')
    ax1.set_title("I am compatible with multithreading")
    plt.show()

check = input()
while check != 'a':
    pass
    cd Desktop
    python "Lenz's_Law_Python.py"
    '''
