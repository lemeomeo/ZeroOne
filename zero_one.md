zero_one
===================

#### 1. Convert text file to binary
zero_one is the file that contains mutiples lines of ZERO and ONE texts, and zero and one are binary.
This is my code to convert zero_one to binary.

```python
#!/usr/bin/env python
with open("zero_one") as f:
	for line in f:
		aline = line.split(" ") 
		for ch in aline:
			if ch == "ZERO":
				print "1",
			else:
				print "0",			
```

#### 2. Convert binary to ASCII
I continue to convert the binary into ASCII.

```python
#!/usr/bin/env python
import binascii
with open("zero_one.txt") as f:
	data=f.read().replace(" ", "")
	n = int(data, 2)
	print binascii.unhexlify('%x' % n)
```

#### 3. Continue to convert
This is the output of the program above:

> Li0gLi0uLiAuIC0uLi0gLS4tLiAtIC4uLS4gLSAuLi4uIC4tLS0tIC4uLi4uIC0tLSAuLS0tLSAuLi4gLS0tIC4uLi4uIC4uLSAuLS0uIC4uLi0tIC4tLiAtLS0gLi4uLi4gLiAtLi0uIC4tLiAuLi4tLSAtIC0tLSAtIC0uLi0gLQ==

It is a base64, which means I can continue to convert it to ASCII

#### 4. Convert to ASCII
I decoded that base64 into ASCII:

```bash
./zero_one_two.py | base64 -d 
```

The result ASCII looks like a morse code, I continue to decode the morse.

### 4. Morse code
This is the code that I use to decode the morse.

```python
#!/usr/bin/env python
morsedict = {'..-.': 'F',
			'-..-': 'X',
			'.--.': 'P', 
			'-': 'T', 
			'..---': '2',
			'....-': '4', 
			'-----': '0', 
			'--...': '7', 
			'...-': 'V', 
			'-.-.': 'C', 
			'.': 'E', 
			'.---': 'J',
            '---': 'O', 
            '-.-': 'K', 
            '----.': '9', 
            '..': 'I',
            '.-..': 'L', 
            '.....': '5', 
            '...--': '3', 
            '-.--': 'Y',
            '-....': '6', 
            '.--': 'W', 
            '....': 'H', 
            '-.': 'N', 
            '.-.': 'R',
            '-...': 'B', 
            '---..': '8', 
            '--..': 'Z', 
            '-..': 'D', 
            '--.-': 'Q',
            '--.': 'G', 
            '--': 'M', 
            '..-': 'U', 
            '.-': 'A', 
            '...': 'S', 
            '.----': '1'}
value = ""
with open("morse") as f:
	for word in f:
		words = word.split(" ")
		for i in words:
			value = value + morsedict.get(i)
	print value
```

The result is ALEXCTFTH15O1SO5UP3RO5ECR3TOTXT, formatting the flag for a bit into **ALEXCTF{TH15_1S_5UP3R_5ECR3T_TXT}**
