import re

def ErrorHandling():
    print(" Incorrect input data. Please try again.")
    InputString = ''
    InputString = str(input("\n Enter correct color value: "))
    return print(f"\n Converted value: {DefineInputColorType(InputString)}")
    
    
def  RGB_ValuesCheck(RGBValue):
    if RGBValue < 0:
       ErrorHandling()
        
    elif RGBValue > 255:
        ErrorHandling()
        

def RGBArray(Array):
    temp = 0

    for i in range(len(RGBArray)):
        temp = RGBArray[i]
        RGBArray[i] = ValueVerification(temp)

    return RGBArray
    
def RGBValue_to_HEXValue(RGBArray):
    hex1, hex2 = divmod(int(RGBArray),16) #get quotient(hex1) and remainder(hex2)
    Array = [hex1, hex2]
    return Array

def HEXOutput(InputString):
    RGBtoHEX_table = {
    '0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5','6':'6', '7':'7', '8':'8', '9':'9',
    '10':'A', '11':'B', '12':'C', '13':'D','14':'E', '15':'F'}

    RGBArray = re.split(r'[, ]+', InputString) #"r'[, ]'+" contains delimiters for splitting the input string,comma and space
    if len(RGBArray) < 3:
        ErrorHandling()
    ConvertedColor = ""
    for i in range(3):
        RGB_ValuesCheck(int(RGBArray[i]))
        for i2 in range(2):
            key = str(RGBValue_to_HEXValue(RGBArray[i])[i2])
            ConvertedColor += RGBtoHEX_table.get(key)
            key = ''
        i2 = 0
    
    return '#' + ConvertedColor

def RGBOutput(InputString):
    ConvertedColor = ""
    
    if InputString[0] == '#':
        InputString = InputString.replace(InputString[0],'')
        
    RedInHexidecimal = InputString[0] + InputString[1]
    GreenInHexidecimal = InputString[2] + InputString[3]
    BlueInHexidecimal = InputString[4] + InputString[5]
    
    RedInDecimal = int(RedInHexidecimal,16)
    GreenInDecimal = int(GreenInHexidecimal,16)
    BlueInDecimal = int(BlueInHexidecimal,16)    
    ConvertedColor = str(RedInDecimal) + " " + str(GreenInDecimal) + " " + str(BlueInDecimal)
    
    return ConvertedColor

def DefineInputColorType(InputString): #could be optimised to avoid too many if's?
    try:
        CharCounter = 0
        for i in range(len(InputString)):
            if InputString[i].isalpha():
                CharCounter += 1
                break
            elif InputString[i] == ' ':
                return HEXOutput(InputString)
                break
            else:
                continue
        if CharCounter == 0:
            return HEXOutput(InputString)
        elif CharCounter != 0:
            return RGBOutput(InputString)
    except:
        ErrorHandling()

print(" Note: if you're entering RGB value, please separate each color channel by either comma or space.")
InputString = str(input("\n Enter color value: ")) #auto define color type by 'if str has char than hex to rgb'
print(f"\n Converted value: {DefineInputColorType(InputString)}")