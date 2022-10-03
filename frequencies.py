"""Frequencies function."""

def frequencies(items):
    frequencies = {}
    stringItems = [str(i) for i in items]
    for items in stringItems:
        if items in frequencies:
            frequencies[items] +=1
        else:
            frequencies[items] = 1
    return frequencies
