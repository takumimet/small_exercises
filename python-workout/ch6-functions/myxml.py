
# The intent is to use multiple types of parameters in functions
def myxml(tag, text='', **kwargs):
    attrs = ''.join({f'{key} = "{value}"' for key, value in kwargs.items()})
    return f"<{tag} {attrs}>{text}</{tag}>"

print(myxml('pupu', 'caca', mierda='shit'))
