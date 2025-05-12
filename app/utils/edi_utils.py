def pad(value, length, align='right', padchar='0'):
    value = str(value) if value is not None else ''
    if align == 'right':
        return value.rjust(length, padchar)
    else:
        return value.ljust(length, padchar)
    

