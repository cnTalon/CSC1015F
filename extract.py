# extraction of data
# 2 April 2022

def location(block):
    # finds the location
    loca_end = block.index(" ")             # finds the beginning of the location
    loca_end = block.index(" ", loca_end+1) # finds the end of the location section
    location = block[-5:loca_end:-1]        # gets location section
    location = location.title()             # formats the location
    return location


def temperature(block):
    # determines the temperature
    temp = block.find(" ")                  # finds beginning of temp
    temp_end = block.find("_")              # finds end of temp
    temp = float(block[temp+1:temp_end])    # gets temperature
    return temp


def x_coordinate(block):
    # finds x coord
    x_coord = block.find(":")                   # finds the beginning of x coord
    xcoord_end = block.find(",")                # finds end of x coord 
    x_coord = str(block[x_coord+1:xcoord_end])  # gets x coord block
    return x_coord

def y_coordinate(block):
    # finds y coord
    ycoord_end = block.index(" ")               # finds start of y coord
    ycoord_end = block.index(" ", ycoord_end+1) 
    y_coord = block.find(",")                   # finds end of y coord
    y_coord = str(block[y_coord+1:ycoord_end])  # gets y coord block
    return y_coord

def pressure(block):
    # determine the pressure
    press = block.find("_")                 # finds beginning of pressure block
    press_end = block.find(":")             # finds end of pressure block
    press = float(block[press+1:press_end]) # gets pressure
    return press

def get_block(data):
    # finds the whole code
    start = data.find("BEGIN")              # finds start of block
    end = data.find("END")+3                # finds end of block
    data = data[start:end]                  # gets info block
    return data

def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)                 # stores the extracted data
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
    main()