import pyshark
import json
cap = pyshark.FileCapture('C:/Users/dskee/OneDrive/Desktop/test.pcapng')
print (cap[0])