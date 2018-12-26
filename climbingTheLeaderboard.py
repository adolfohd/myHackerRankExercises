
import math
import os
import random
import re
import sys

highestScore = 0
highestPosition = 0
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    aliceRankings = [0]*len(alice)
    currentScoreIndex = 0
    aliceRanking = 1
    for j in range(len(alice)-1, -1 , -1):
        # print(j)
        aliceScore = alice[j]        
        # print("current alice's score = ", aliceScore)
        for i in range(currentScoreIndex, len(scores)):
            score = scores[i]
            # print("i =", i, "score =", score)
            # print("current score = ", score)
            if i>0:
                # print("previous score = ", score)
                if scores[i]==scores[i-1]:
                    aliceRanking -=1                                
            if aliceScore < score:
                aliceRanking += 1
                # print("alice ranking = ", aliceRanking)
            else:
                break
            currentScoreIndex = i+1
        aliceRankings[j] = aliceRanking
        # print(aliceRankings)
    return(aliceRankings)

# scores = [100, 100, 50, 40, 40, 20, 10]
# alice  = [5, 25, 50, 120]

scores = [100, 90, 90, 80, 75, 60]
alice = [50, 65, 77, 90, 102]

print(climbingLeaderboard(scores, alice))
