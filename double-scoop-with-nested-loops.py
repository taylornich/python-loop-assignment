# question 2 task 1
import random

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["Happy", "Sad", "Energetic", "Mellow", "Angry", "Motivated", "Excited"]
for day in days:
    times = ["Morning", "Afternoon", "Evening"]
    for time in times:
        mood = random.choice(moods)
        print("On " + day + " " + time + " you were " + mood + ".")
