def areaoftriangle():
    input1 = int(input("what is the base of the triangle?"))
    input2 = int(input("what is the height of the triangle?"))
    area = input1*input2/2
    print(area)
areaoftriangle()

def powercalc():
    input1 = int(input("what is the volts?"))
    input2 = int(input("what is the current?"))
    answer = input1*input2
    print(answer)
powercalc()

def sumcalc():
    input1 = int(input("what is the first number?"))
    input2 = int(input("what is the second number?"))
    print(input1 + input2)
sumcalc()

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}


