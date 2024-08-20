import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev

GPIO.setmode(GPIO.BCM)

pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xF0, 0xF0, 0xF0, 0xF0, 0xE1]]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0,17)

radio.setPayloadSize(32)
radio.setChannel(0x76)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openWritingPipe(pipes[0])

radio.openReadingPipe(1, pipes[1])
radio.printDetails()

text = ['0',' ','1',' ','0',' ','1',' ','0',' ','0',' ','0',' ','1']

with open('exampleData.txt', 'w') as f:
	for line in text:
		f.write(line)
		f.write('\n')

with open('exampleData.txt') as f:
    lines = f.read().splitlines()
    print(lines)
    
if len(lines) < 32:
    lines.append(0)
    
while True:
    start = time.time()
    radio.write(lines)
    print("Sent the message: {}".format(lines))
    time.sleep(0.1)
