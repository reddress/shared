FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

class SpeechModule:
    def __init__(self):
        self.speech = {}
        for i in range(10):
            self.speech[i] = FIRST_TEN[i]
        for i in range(10, 20):
            self.speech[i] = SECOND_TEN[i-10]
        for i in range(20, 100):
            self.speech[i] = OTHER_TENS[i//10 - 2]
            if i%10 > 0:
                self.speech[i] += " " + self.speech[i%10]
        for i in range(100, 1000):
            self.speech[i] = self.speech[i//100] + " " + HUNDRED
            if i%100 > 0:
                self.speech[i] += " " + self.speech[i%100]
            
s = SpeechModule()

def checkio(number):
    return s.speech[number]

checkio(209)
