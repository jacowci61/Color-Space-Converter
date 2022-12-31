def value_check(color_value): #RGB failsafe
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

def return_rgb(r, g, b):
    rgb_arr = [None] * 3
    rgb_arr[0] = r
    rgb_arr[1] = g
    rgb_arr[2] = b
    temp = 0

    for i in range(len(rgb_arr)):
        temp = rgb_arr[i]
        rgb_arr[i] = value_check(temp)

    return rgb_arr


def rgb_to_hex(return_rgb):
    hex1, hex2 = divmod(return_rgb,16) #get quotient(hex1) and remainder(hex2)
    hex_arr = [hex1, hex2]
    return hex_arr    

rgb_to_hex_table = {
'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5','6':'6', '7':'7', '8':'8', '9':'9',
'10':'A', '11':'B', '12':'C', '13':'D','14':'E', '15':'F'}

print(f"#{rgb_to_hex_table[str(rgb_to_hex(return_rgb(35, 177, 95)[0])[0])]}\
{rgb_to_hex_table[str(rgb_to_hex(return_rgb(35, 177, 95)[0])[1])]}\
{rgb_to_hex_table[str(rgb_to_hex(return_rgb(35, 177, 95)[1])[0])]}\
{rgb_to_hex_table[str(rgb_to_hex(return_rgb(35, 177, 95)[1])[1])]}\
{rgb_to_hex_table[str(rgb_to_hex(return_rgb(35, 177, 95)[2])[0])]}\
{rgb_to_hex_table[str(rgb_to_hex(return_rgb(35, 177, 95)[2])[1])]}")