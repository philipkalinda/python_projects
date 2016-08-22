##############################imports######################################

import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

##############################AutoBot Game#################################

choice_1_scores = {
	'rock': {'wins':0, 'losses':0, 'draws':0},
	'paper' : {'wins':0, 'losses':0, 'draws':0},
	'scissors' : {'wins':0, 'losses':0, 'draws':0}
}

choice_2_scores = {
	'rock': {'wins':0, 'losses':0, 'draws':0},
	'paper': {'wins':0, 'losses':0, 'draws':0},
	'scissors': {'wins':0, 'losses':0, 'draws':0}
}

choices = ['rock', 'paper', 'scissors']


number_of_games = 100000
n = number_of_games
while number_of_games >0:
	choice_1 = random.choice(choices)
	choice_2 = random.choice(choices)
	number_of_games -=1

	if choice_1 == 'rock':
		if choice_2 == 'rock':
			choice_1_scores['rock']['draws']+=1
			choice_2_scores['rock']['draws']+=1
		elif choice_2 == 'paper':
			choice_1_scores['rock']['losses']+=1
			choice_2_scores['paper']['wins']+=1
		elif choice_2 == 'scissors':
			choice_1_scores['rock']['wins']+=1
			choice_2_scores['scissors']['losses']+=1
			
	elif choice_1 == 'paper':
		if choice_2 == 'paper':
			choice_1_scores['paper']['draws']+=1
			choice_2_scores['paper']['draws']+=1
		elif choice_2 == 'rock':
			choice_1_scores['paper']['wins']+=1
			choice_2_scores['rock']['losses']+=1
		elif choice_2 == 'scissors':
			choice_1_scores['paper']['losses']+=1
			choice_2_scores['scissors']['wins']+=1
	
	elif choice_1 == 'scissors':
		if choice_2 == 'scissors':
			choice_1_scores['scissors']['draws']+=1
			choice_2_scores['scissors']['draws']+=1
		elif choice_2 == 'paper':
			choice_1_scores['scissors']['wins']+=1
			choice_2_scores['paper']['losses']+=1
		elif choice_2 == 'rock':
			choice_1_scores['scissors']['losses']+=1
			choice_2_scores['rock']['wins']+=1
	
	# number_of_games -=1

for _ in range(1):
	print('\nThe results of the choice 1 the runs are as follows:\n')
	for i in choice_1_scores:
		print('{} -> {}'.format(i, choice_1_scores[i]))
	print('\n\n***************************************************\n\n')
	print('\nThe results of the choice 2 the runs are as follows:\n')
	for i in choice_2_scores:
		print('{} -> {}'.format(i, choice_2_scores[i]))


# categorizing data

rock_data = {
	'rock_wins': choice_1_scores['rock']['wins'],
	'rock_losses': choice_1_scores['rock']['losses'],
	'rock_draws': choice_1_scores['rock']['draws']
}
rock_list = [choice_1_scores['rock']['wins'],choice_1_scores['rock']['losses'],choice_1_scores['rock']['draws']]


paper_data = {
	'paper_wins': choice_1_scores['paper']['wins'],
	'paper_losses': choice_1_scores['paper']['losses'],
	'paper_draws': choice_1_scores['paper']['draws']
}
paper_list = [choice_1_scores['paper']['wins'],choice_1_scores['paper']['losses'],choice_1_scores['paper']['draws']]


scissors_data = {
	'scissors_wins': choice_1_scores['scissors']['wins'],
	'scissors_losses': choice_1_scores['scissors']['losses'],
	'scissors_draws': choice_1_scores['scissors']['draws']
}
scissors_list = [choice_1_scores['rock']['wins'],choice_1_scores['rock']['losses'],choice_1_scores['rock']['draws']]

total = np.sum(rock_list) + np.sum(paper_list) + np.sum(scissors_list)
print(total)

# Plotting of the data


fig = plt.figure(figsize=(20,8.5))
rock_ax = fig.add_subplot(3,1,1)
paper_ax = fig.add_subplot(3,1,2)
scissors_ax = fig.add_subplot(3,1,3)

rock_ax.bar(np.arange(3),rock_list, width=0.6)
rock_ax.set(ylabel='Number Of Outcomes', xticklabels=['wins','losses','draws'], xticks=np.arange(3)+0.3, title='Rock Outcomes',ylim=(0,(n/5)))

paper_ax.bar(np.arange(3),paper_list, width=0.6)
paper_ax.set(ylabel='Number Of Outcomes', xticklabels=['wins','losses','draws'], xticks=np.arange(3)+0.3, title='Paper Outcomes', ylim=(0,(n/5)))

scissors_ax.bar(np.arange(3),scissors_list, width=0.6)
scissors_ax.set(ylabel='Number Of Outcomes', xticklabels=['wins','losses','draws'], xticks=np.arange(3)+0.3, title='Scissors Outcomes',ylim=(0,(n/5)))

plt.show()
















