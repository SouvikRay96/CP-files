# Enter number of students
n = int(input())
students = [i for i in range(1,n+1)] # Creating the lists of students
lyrics = input() # taking input of the lyrics as a string of "a" and "b"
# initialising 2 variables to 0 which will be used as the pointers to traverse through students list and the lyrics
i,j = 0,0
# Here i tells which student has the parcel and j tells what lyrics is played
# Running the loop which will run until only 1 student is left in the students list who is the winner
while len(students) != 1:
    # Checking j is less than or equal to lenght of the lyrics - 1 
    # This is done to just keep j within the lenght of the lyrics so that it does not go out of bounce
    if j <= len(lyrics)-1:
        if lyrics[j] == 'a':
            # if the lyric is "a" then the parcel will be passed to the adjacent student execute the following
            if i <= len(students)-1:
                # if i is within the range then pass the parcel i.e. increment i by 1
                i = i + 1
            else:
                # if not then i should again point to the first student and then pass the parcel
                # this is done because the passing takes place in a clockwise direction
                # i.e. increment i by 1
                i = 0
                i = i +1
        elif lyrics[j] == 'b':
            # if the lyric is "b" then the student who has the parcel will be out of the game
            if i >= len(students):
                # if i is out of the range of the students list then initialise i to 0
                # And then remove the student
                i = 0
                students.remove(students[i])
            else:
                # if i is within the range then remove the student which i points to
                students.remove(students[i])
        j += 1 # Increment j by one to traverse thorugh the lyrics
    else:
        # If j is out of the lenght of the lysrics then initialize j to 0 to again play the lyrics
        j = 0
print(students[0]) # Printing the student who won the game