def convert_temp(temp,unit):
    if unit=='c':
        return temp *9/5 + 32
    elif unit=='f':
        return (temp - 32) * 5/9
    else:
        return None