def return_rgb(r, g, b):
#region r,g,b failsafe
    rgb_arr = [None] * 3

    if r < 0:
        r = 0
        rgb_arr[0] = r
    elif r > 255:
        r = 255
        rgb_arr[0] = r
    elif type(r) != int:
        r = round(r)
        rgb_arr[0] = r
    else:
        rgb_arr[0] = r

        
    if g < 0:
        g = 0
        rgb_arr[1] = g
    elif g > 255:
        g = 255
        rgb_arr[1] = g
    elif type(g) != int:
        g = round(g)
        rgb_arr[1] = g
    else:
        rgb_arr[1] = g

        
    if b < 0:
        b = 0
        rgb_arr[2] = b
    elif b > 255:
        b = 255
        rgb_arr[2] = b
    elif type(g) != int:
        b = round(b)
        rgb_arr[2] = b
    else:
        rgb_arr[2] = b
    return rgb_arr
    #endregion

    #region Convertion
rgb_to_hex_table = {
'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5','6':'6', '7':'7', '8':'8', '9':'9',
'10':'A', '11':'A', '12':'C', '13':'D','14':'E', '15':'F'}
def rgb_to_hex(return_rgb):
    hex1, hex2 = divmod(return_rgb,16) #get quotient(hex1) and remainder(hex2)
    hex_arr = [hex1, hex2]
    return hex_arr    

print(f"#{rgb_to_hex_table[str(rgb_to_hex(return_rgb(35, 177, 95)[0])[0])]}\
{rgb_to_hex_table[str(rgb_to_hex(return_rgb(35, 177, 95)[0])[1])]}\
{rgb_to_hex_table[str(rgb_to_hex(return_rgb(35, 177, 95)[1])[0])]}\
{rgb_to_hex_table[str(rgb_to_hex(return_rgb(35, 177, 95)[1])[1])]}\
{rgb_to_hex_table[str(rgb_to_hex(return_rgb(35, 177, 95)[2])[0])]}\
{rgb_to_hex_table[str(rgb_to_hex(return_rgb(35, 177, 95)[2])[1])]}")
'''
print(f"#{rgb_to_hex_table[str(rgb_to_hex(return_rgb(-10, 254, 254)[0])[0])]}\
{rgb_to_hex_table[str(rgb_to_hex(return_rgb(-10, 254, 254)[0])[1])]}\
{rgb_to_hex_table[str(rgb_to_hex(return_rgb(-10, 254, 254)[1])[0])]}\
{rgb_to_hex_table[str(rgb_to_hex(return_rgb(-10, 254, 254)[1])[1])]}\
{rgb_to_hex_table[str(rgb_to_hex(return_rgb(-10, 254, 254)[2])[0])]}\
{rgb_to_hex_table[str(rgb_to_hex(return_rgb(-10, 254, 254)[2])[1])]}")
'''
#endregion