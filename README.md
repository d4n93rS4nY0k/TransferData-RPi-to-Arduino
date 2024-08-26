# Transfer data from Raspberry Pi 4 to Arduino Uno

The project is based on Raspberry Pi 4, Arduino Uno and transcievers nRF24L01+ PA LNA

Used programming languages: Python, C++


## Used Libraries

Necessary library for transciever nRF24L01:

Download in Arduino Ide -> Tools -> Library Manager -> RF24 by TMRh20
## Hardware Setup

- **Raspberry Pi and nRF24L01+ connection**
| nRF24L01+             | Raspberry Pi 4                                                                |
| ----------------- | ------------------------------------------------------------------ |
| GND | 6 ~ GND |
| VCC | 1 ~ 3.3V |
| CE | 11 ~ GPIO17 |
| CSN | 24 ~ GPIO8 ~ SPI_CE0_n |
| SCK | 23 ~ GPIO11 ~ SPI_CLK |
| MOSI | 19 ~ GPIO10 ~ SPI_MOSI |
|MISO|21 ~ GPIO9 ~ SPI_MISO|

![nRFtoRPi]([![full.png](https://i.postimg.cc/FzTtFZn3/full.png)](https://postimg.cc/9wwgJG2Q))


## Run main code files on RPi4 and Arduino Uno

Run the example **mainRPi.py** on Raspberry Pi 

Run the example **mainArduino.ino** on Arduino

- If everything is connected correctly, the output on Raspberry Pi should look like this:

```python
STATUS	 = 0x0f RX_DR=0 TX_DS=0 MAX_RT=0 RX_P_NO=7 TX_FULL=1
RX_ADDR_P0-1	 =
 0xe8e8f0f0e1 0xf0f0f0f0e1
RX_ADDR_P2-5	 =
0xc3
0xc4
0xc5
0xc6

TX_ADDR		 =
 0xe8e8f0f0e1
RX_PW_P0-6	 =
0x20
0x20
0x00
0x00
0x00
0x00

EN_AA		 =
0x3f

EN_RXADDR	 =
0x03

RF_CH		 =
0x76

RF_SETUP	 =
0x01

CONFIG		 =
0x0e

DYNPD/FEATURE	 =
0x3f
0x06

Data Rate	 = 1MBPS
Model		 = nRF24l01+
CRC Length	 = 16 bits
PA Power	 = PA_MIN
['0', ' ', '1', ' ', '0', ' ', '1', ' ', '0', ' ', '0', ' ', '0', ' ', '1']
Sent the message: ['0', ' ', '1', ' ', '0', ' ', '1', ' ', '0', ' ', '0', ' ', '0', ' ', '1', 0]

```

- And the output on Arduino Uno should look like this:

```python
SPI Speedz	= 10 Mhz
STATUS		= 0x0e RX_DR=0 TX_DS=0 MAX_RT=0 RX_P_NO=7 TX_FULL=0
RX_ADDR_P0-1	= 0xf0f0f0f0e1 0xe8e8f0f0e1
RX_ADDR_P2-5	= 0xc3 0xc4 0xc5 0xc6
TX_ADDR		= 0xf0f0f0f0e1
RX_PW_P0-6	= 0x20 0x20 0x20 0x20 0x20 0x20
EN_AA		= 0x3f
EN_RXADDR	= 0x03
RF_CH		= 0x76
RF_SETUP	= 0x07
CONFIG		= 0x0e
DYNPD/FEATURE	= 0x3f 0x04
Data Rate	= 1 MBPS
Model		= nRF24L01+
CRC Length	= 16 bits
PA Power	= PA_MAX
ARC		= 0
0 1 0 1 0 0 0 1

```
## Data

This example uses the transfer of data written in .txt file **exampleData.txt**

**You can use any other data format.**

The function of writing data and formatting through the variable:


```python
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
```
## Viewers count

![Visitor Count](https://profile-counter.glitch.me/d4n93rS4nY0k/count.svg)



## Authors

- [@d4n93rS4nY0k](https://github.com/d4n93rS4nY0k)

