import re

def value_check(color_value): #RGB failsafe
    color_value = int(color_value)
    if color_value < 0:
        color_value = 0
        return color_value

    elif color_value > 255:
        color_value = 255
        return color_value

    elif type(color_value) != int:
        color_value = round(color_value)
        return color_value

    else:
        return color_value

def rgb_arr(arr):
    temp = 0

    for i in range(len(rgb_arr)):
        temp = rgb_arr[i]
        rgb_arr[i] = value_check(temp)

    return rgb_arr


def rgb_to_hex(rgb_arr):
    hex1, hex2 = divmod(int(rgb_arr),16) #get quotient(hex1) and remainder(hex2)
    hex_arr = [hex1, hex2]
    return hex_arr

def hex_output(arr):
    rgb_to_hex_table = {
    '0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5','6':'6', '7':'7', '8':'8', '9':'9',
    '10':'A', '11':'B', '12':'C', '13':'D','14':'E', '15':'F'}

    output = ""
    for i in range(3):
        for i2 in range(2):
            key = str(rgb_to_hex(rgb_arr[i])[i2])
            output += rgb_to_hex_table.get(key)
            key = ''
        i2 = 0
    
    return '#' + output


rgb_str = str(input("Enter RGB values divided either by comma or space: "))
rgb_arr = re.split(r'[, ]+', rgb_str) #" r'[, ]'+ " contains delimiters for splitting the input string,comma and space
print(f"Converted value {hex_output(rgb_arr)}")