# question 1 task 1

import random

moods = ["Happy", "Sad", "Energetic", "Angry", "Anxious", "Calm", "Motivated"]

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i in range(len(weekdays)):
    daily_mood = random.choice(moods)
    print("On " + weekdays[i] + ", you were feeling " + daily_mood + ".")
    