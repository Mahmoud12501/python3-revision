def next_edge(side1,side2):

    return (side1+side2)-1

#Return the Remainder from Two Numbers
def remainder(x, y):
    return x%y


# Find the Perimeter of a Rectangle
def find_perimeter(length, width):
	return (length*2)+(width*2)

# Power Calculator

def circuit_power(voltage, current):
	return voltage*current

# Convert Hours into Seconds
def how_many_seconds(hours):

    return hours*60*60


#  function that takes a decimal number representation of a signal 
# and returns the analog voltage level that would be created by a DAC if it were given the same number in binary.
def V_DAC(value):
    analog_voltage = (5*value)/1023

    return round(analog_voltage,2)
