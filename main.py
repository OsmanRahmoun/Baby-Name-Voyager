# Project 5 - Baby Name Voyager
# CS 111, Reckinger
# Osman Rahmoun, 11/3/2022, Fall Semester

import matplotlib.pyplot as plt


# Clean data Function:
#Paramets: List - List of lists containing names and their respective name rank scores
#Max - set value represnting the last number of ranking possible
#Replaces every 0 (name so rare it was not ranked) to the max number
def clean_data(list, max):
  for specific_list in list:
    for i in range(len(specific_list)):
      if specific_list[i] == 0:
        specific_list[i] = max
  pass

#Grab Value Function:
#Opens the name Data Text file, reads the textfile and stores every seperate line into a list, also stripping the "\n" created by every new line
#Returns - a list of nested lists of every name and their respective score
def grabvalues():
  file = open("names-data.txt")
  lines = file.readlines()
  final_list= []
  for i in range(len(lines)):
    lines[i] = lines[i].strip("\n")
  for i in range(len(lines)):
    lines[i] = lines[i].split()
  for lists in lines:
    scores = lists[1:]
    name = lists[0]
    for i in range(0,len(scores)):
      scores[i] = int(scores[i])
    scores.insert(0,name)
    final_list.append(scores)
  return final_list

#Finding Names Function:
#Parameters: Names - Takes User Input of Baby Names
#This function takes the user input of baby names and loops through the list to find the matching name in the list set.
# Returns - The lists of the matching names and their respective scores
def finding_names(names):
  listnames=[]
  lastlist = []
  names= names.split()
  for i in range(len(list1)):
    listnames.append(list1[i][0])
  for i in range(len(names)):
    if names[i] in listnames:
      lastlist.append(list1[(listnames.index(names[i]))])
  return lastlist

#Plotting Function
#Parameter - List of matching Names and their Respective scores
# Takes the list of names and respective scores and plots them
def plotting(thelist):
  list_of_names= []
  plt.ion()
  for i in range(len(thelist)):
    plt.plot(thelist[i][1:],'--o')
  for i in range(len(thelist)):
    list_of_names.append((thelist[i][0]))
  years = [1900,1920,1940,1960,1980,2000]
  ticks = range(0,11,2)
  plt.xticks(ticks,years)
  plt.title("Most Popular Baby Names, by decade")
  plt.xlabel("Years")
  plt.ylabel("Ranking")
  plt.legend(list_of_names)
  plt.ylim(1050, -25)
  final_name = ''.join(list_of_names)
  plt.savefig(final_name + ".png", bbox_inches = 'tight')
  pass

# Main code below
if __name__ == '__main__':
    list1 = grabvalues()
    namestring = input("Enter baby names: ")
    max_num = 1013
    clean_data(list1, max_num)
    desired_list = finding_names(namestring)
    plotting(desired_list)

