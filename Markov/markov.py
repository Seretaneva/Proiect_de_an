import numpy as np
from abc import ABCMeta, abstractmethod


class State:
    def state_name(self): pass

    def transition(self): pass

    def check(self):
        self.state_name()
        self.transition()


class Give_states(State):
    def state_name(self):
        "Music", "Pizza", "Exercises", "Writting"


class Give_transition(State):
    def transition(self):
        ["MM", "ME", "MP", "MW"], ["EM", "EE", "EP", "EW"], ["PM", "PE", "PP", "PW"], ["WM", "WE", "WP", "WW"]

class Matrix(metaclass=ABCMeta):
  @abstractmethod
  def create(self):
    pass

class Set_matrix(Matrix):
  def create(self, transitionMatrix):
    self.transitionMatrix = [["MM","ME","MP","MW"],["EM","EE","EP","EW"],["PM","PE","PP","PW"],["WM","WE","WP","WW"]]

# The statespace
states = ["Music", "Pizza", "Exercises", "Writting"]

# Possible sequences of events
transitionName = [["MM", "ME", "MP", "MW"], ["EM", "EE", "EP", "EW"], ["PM", "PE", "PP", "PW"],
                  ["WM", "WE", "WP", "WW"]]

# Probabilities matrix (transition matrix)
transitionMatrix = [[0.3, 0.2, 0.4, 0.1], [0.1, 0.4, 0.3, 0.2], [0.2, 0.1, 0.5, 0.2], [0.1, 0.2, 0.4, 0.3]]
if sum(transitionMatrix[0]) + sum(transitionMatrix[1]) + sum(transitionMatrix[1]) + sum(transitionMatrix[1]) != 4:
    print("Something went wrong. Transition matrix?")
else:
    print("All is gonna be okay! :D")



def activity_forecast(days):

    activityToday = "Music"
    print("First State: " + activityToday)

    activityList = [activityToday]
    i = 0
    prob = 1
    while i != days:
        if activityToday == "Music":
            change = np.random.choice(transitionName[0], replace=True, p=transitionMatrix[0])
            if change == "MM":
                prob = prob * 0.3
                activityList.append("Music")
                pass
            elif change == "ME":
                prob = prob * 0.2
                activityToday = "Exercises"
                activityList.append("Exercises")
            elif change == "MW":
                prob = prob * 0.1
                activityToday = "Writting"
                activityList.append("Writting")
            else:
                prob = prob * 0.4
                activityToday = "Pizza"
                activityList.append("Pizza")
        elif activityToday == "Exercises":
            change = np.random.choice(transitionName[1], replace=True, p=transitionMatrix[1])
            if change == "EE":
                prob = prob * 0.5
                activityList.append("Exercises")
                pass
            elif change == "EM":
                prob = prob * 0.2
                activityToday = "Music"
                activityList.append("Music")
                pass
            elif change == "EW":
                prob = prob * 0.2
                activityToday = "Writting"
                activityList.append("Writting")
                pass
            else:
                prob = prob * 0.1
                activityToday = "Pizza"
                activityList.append("Pizza")
        elif activityToday == "Pizza":
            change = np.random.choice(transitionName[2], replace=True, p=transitionMatrix[2])
            if change == "PP":
                prob = prob * 0.4
                activityList.append("Pizza")
                pass
            elif change == "PM":
                prob = prob * 0.1
                activityToday = "Music"
                activityList.append("Music")
                pass
            elif change == "PW":
                prob = prob * 0.2
                activityToday = "Writting"
                activityList.append("Writting")
            else:
                prob = prob * 0.3
                activityToday = "Exercises"
                activityList.append("Exercises")
        elif activityToday == "Writting":
            change = np.random.choice(transitionName[3], replace=True, p=transitionMatrix[3])
            if change == "WM":
                prob = prob * 0.10000
                activityList.append("Music")
                pass
            elif change == "WP":
                prob = prob * 0.2
                activityToday = "Pizza"
                activityList.append("Pizza")
                pass
            elif change == "WE":
                prob = prob * 0.4
                activityToday = "Exercises"
                activityList.append("Exercises")
            else:
                prob = prob * 0.3
                activityToday = "Writting"
                activityList.append("Writting")
        i += 1
    print("Possible states: " + str(activityList))
    print("End state after " + str(days) + " days: " + activityToday)
    print("Probability of the possible sequence of states: " + str(prob))

activity_forecast(2)


def activity_forecast(days):
    # Choose the starting state
    activityToday = "Music"
    activityList = [activityToday]
    i = 0
    prob = 1
    while i != days:
        if activityToday == "Music":
            change = np.random.choice(transitionName[0], replace=True, p=transitionMatrix[0])
            if change == "MM":
                prob = prob * 0.3
                activityList.append("Music")
                pass
            elif change == "ME":
                prob = prob * 0.4
                activityToday = "Exercises"
                activityList.append("Exercises")
                pass
            elif change == "MW":
                prob = prob * 0.1
                activityToday = "Writting"
                activityList.append("Writting")
            else:
                prob = prob * 0.2
                activityToday = "Pizza"
                activityList.append("Pizza")
        elif activityToday == "Exercises":
            change = np.random.choice(transitionName[1], replace=True, p=transitionMatrix[1])
            if change == "EE":
                prob = prob * 0.5
                activityList.append("Exercises")
                pass
            elif change == "EM":
                prob = prob * 0.2
                activityToday = "Music"
                activityList.append("Music")
                pass
            elif change == "EW":
                prob = prob * 0.2
                activityToday = "Writting"
                activityList.append("Writting")
            else:
                prob = prob * 0.1
                activityToday = "Pizza"
                activityList.append("Pizza")
        elif activityToday == "Pizza":
            change = np.random.choice(transitionName[2], replace=True, p=transitionMatrix[2])
            if change == "PP":
                prob = prob * 0.4
                activityList.append("Pizza")
                pass
            elif change == "PM":
                prob = prob * 0.1
                activityToday = "Music"
                activityList.append("Music")
                pass
            elif change == "PW":
                prob = prob * 0.2
                activityToday = "Writting"
                activityList.append("Writting")
            else:
                prob = prob * 0.3
                activityToday = "Exercises"
                activityList.append("Exercises")
        elif activityToday == "Writting":
            change = np.random.choice(transitionName[3], replace=True, p=transitionMatrix[3])
            if change == "WP":
                prob = prob * 0.2
                activityList.append("Pizza")
                pass
            elif change == "WM":
                prob = prob * 0.1
                activityToday = "Music"
                activityList.append("Music")
                pass
            elif change == "WW":
                prob = prob * 0.3
                activityToday = "Writting"
                activityList.append("Writting")
            else:
                prob = prob * 0.4
                activityToday = "Exercises"
                activityList.append("Exercises")

        i += 1
    return activityList


list_activity = []
count = 0


for iterations in range(1, 10000):
    list_activity.append(activity_forecast(2))

for smaller_list in list_activity:
    if (smaller_list[2] == "Exercises"):
        count += 1

# Calculate the probability of starting from state:'Music' and ending at state:'Exercises'
percentage = (count / 10000) * 100
print("The probability of starting at state:'Music' and ending at state:'Exercises'= " + str(percentage) + "%")
