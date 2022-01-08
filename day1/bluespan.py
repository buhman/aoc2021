#file = open("input.txt")
#text = file.read()

def bluespan(text):
    unconvertedsweeps = text.split("\n")
    #split gets rid of the quoted characters and also splits the string into
    #seperate entries

    numbers = [None] * len(unconvertedsweeps)
    #this zero (arbitrary)creates a list that has 2000 (in this case)
    #zeros in it.

    for index in range(0, len(unconvertedsweeps)):
        numbers[index]=int(unconvertedsweeps[index])
        #the zero in range here specifies that the very first item in
        #the list will be used. this is redundant for range however it is
        #useful to specify since the following range specifically does not
        #use the first item.

    count=0
    #count=0 because counting starts at zero and needs to be specified,
    #in this particular problem
    for index in range(1,len(numbers)):
        if numbers[index-1]<numbers[index]:
            count=count+1
    return count
