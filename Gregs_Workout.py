"""
Greg is a beginner bodybuilder. Today the gym coach gave him the training plan. All it had was n integers a 1, a 2, ..., a n. These numbers mean that Greg needs to do exactly n exercises today. Besides, Greg should repeat the i-th in order exercise a i times.

Greg now only does three types of exercises: "chest" exercises, "biceps" exercises and "back" exercises. Besides, his training is cyclic, that is, the first exercise he does is a "chest" one, the second one is "biceps", the third one is "back", the fourth one is "chest", the fifth one is "biceps", and so on to the n-th exercise.

Now Greg wonders, which muscle will get the most exercise during his training. We know that the exercise Greg repeats the maximum number of times, trains the corresponding muscle the most. Help Greg, determine which muscle will get the most training.

"""

no_of_exercises = int(input())

repeat_exer = list(map(int, input().split())) + ([0] * (3 - (no_of_exercises % 3)))
chest = sum([repeat_exer[i] for i in range(0, no_of_exercises + 1, 3 )])
biceps = sum([repeat_exer[i] for i in range(1, no_of_exercises + 1, 3 )])
back = sum([repeat_exer[i] for i in range(2, no_of_exercises + 1, 3 )])

if chest > biceps and chest > back :
    print("chest")
elif biceps > chest and biceps > back :
    print("biceps")
else :
    print("back")
