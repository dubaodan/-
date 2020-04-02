import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox


udpList=[
    0b0110011001100000,
    0b0101010101010101,
    0b1000111100001100]

def checkSum(udplist):
    add1 = udplist[0]+udplist[1]
    if  add1 >= 2**16:
        addt= add1>>16
        add1 = add1 & 0xffff
        add1+=addt
    add2 = add1 + udplist[2]
    if add2 >= 2**16:
        addt= add2>>16
        add2 = add2 & 0xffff
        add2+=addt
    return 0xffff - add2

def sumAll(udplist,result):
    add = 0xffff- checkSum(udplist)+result
    add = add&0xffff
    return add

checksum = checkSum(udpList)
allsum = sumAll(udpList,checksum)

textbox1 = TextBox(plt.axes([0.3, 0.7, 0.5, 0.1]), '16-bit data1', initial=format(udpList[0],'016b'))
textbox2 = TextBox(plt.axes([0.3, 0.6, 0.5, 0.1]), '16-bit data2', initial=format(udpList[1],'016b'))
textbox3 = TextBox(plt.axes([0.3, 0.5, 0.5, 0.1]), '16-bit data3', initial=format(udpList[2],'016b'))
textbox4 = TextBox(plt.axes([0.3, 0.4, 0.5, 0.1]), 'checksum', initial=format(checksum,'016b'))
textbox5 = TextBox(plt.axes([0.3, 0.3, 0.5, 0.1]), 'allsum', initial=format(allsum,'016b'))


plt.show()
