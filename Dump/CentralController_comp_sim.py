from Policy_UCB1 import Policy_UCB1 as PUCB1
from SecondaryUserDAL import SecondaryUserDAL as SU_DAL
from CentralControllerDAL import CentralControllerDAL as CC_DAL
from Policy_LUCB import Policy_LUCB as PLUCB
from SecondaryUser import SecondaryUser as SU
from CentralController import CentralController as CC
from beta import beta
import numpy as np
import math
import matplotlib.pyplot as plt
from sys import argv

#script, foutput, foutput_data, regret_figure, selection_data = argv
script, num, up, low, arms, give = argv

foutput = "CCA\Sim" + str(num) + "_output.txt"
foutput_data = "CCA\Sim" + str(num) + "_data.csv"
regret_figure = "CCA\Sim" + str(num) + "_regret_figure.png"
selection_data = "CCA\Sim" + str(num) + "_selection_data.txt"

selection_data = open(selection_data, 'w')


p = [0.54, 0.56, 0.58, 0.60, 0.68, 0.70, 0.72, 0.72, 0.74, 0.76, 
		0.77, 0.78, 0.79, 0.80, 0.85, 0.81, 0.82, 0.83, 0.83, 0.84]
#p = [0.32, 0.78, 0.54, 0.80, 0.25, 0.67, 0.86, 0.59, 0.54, 0.55,
#		0.49, 0.29, 0.53, 0.71, 0.48, 0.85, 0.66, 0.37, 0.43, 0.79]
#p = [ 0.60916442,  0.79078749,  0.58481901,  0.4453407,   0.65724737,  0.74819669,
#  0.55999234,  0.50357646,  0.57017747,  0.61546778,  0.73533915,  0.32226127,
#  0.46059955,  0.30982127,  0.59668442,  0.60143155,  0.69334041,  0.35996052,
#  0.45795674,  0.72516579]



narms = int(arms)
m = int(give)
T = 30
Ts = 10000
Tsu = Ts
N = 3000
Nsig = 1

epsilon = 0.5
delta = 0.0005

b = 3
p_con = 0.5

s = .01
lamb = 4

upper = up
lower = low

CC2 = CC_DAL(narms, T, Ts, PUCB1, SU_DAL, b, s, lamb)
CC1 = CC(narms, m, T, Tsu, N, Nsig, PLUCB, SU, beta, epsilon, delta, b, p_con, lamb)



print "We're going to overwrite files %r and %r." % (foutput, foutput_data)
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")



output = open(foutput, 'w')
output_data = open(foutput_data, 'w')

print "Probabilities are going to have upper bound %s and lower bound %s." % (upper, lower)
output.write("Probabilities are %s." % (p))
output.write("\n")

print "There are %s arms with simulation running for %s time slots with %s subslots per slot." % (narms, T, Ts)
output.write("There are %s arms with simulation running for %s time slots with %s subslots per slot." % (narms, T, Ts))
output.write("\n")

print "The average number of secondary users per slot is assumed to be %s." % (lamb)
output.write("The average number of secondary users per slot is assumed to be %s." % (lamb))
output.write("\n")


regret = 0
i = 0
slots = 0
slotlist = []
nuserslist = []

successlist1 = []
regretlist1 = []
conflictlist1 = []

successlist2 = []
regretlist2 = []
conflictlist2 = []

output_data.write("Time Slot" + "," + "Number of Users" + "," + "Reward Gained by CC1" + "," + "Reward Gained by CC2" + "," +  
	 "Best Reward" + "," +  "Total Regret for CC1" + "," +  "Total Regret for CC2" + "," +  "Average Regret for CC1" + "," +  
	 "Average Regret for CC2" + "," +  "Conflicts for CC1" + "," +  "Conflicts for CC2")

output_data.write("\n")

l = 1

for q in range(0,T):
	
	p = np.random.uniform(upper,lower,narms)
	CC1.CCfun(p,m)
	
	print "==================================================================================="
	output.write("===================================================================================")
	output.write("\n")
		
	print "Probabilities are p = %s." % (p)
	output.write("Probabilities are p = %s." % (p))
	output.write("\n")

	
	print "==================================================================================="
	output.write("===================================================================================")
	output.write("\n")
	
	print "\n"
	output.write("\n")

	print "For the time slot %s." %(CC1.t)
	output.write("For the time slot %s." %(CC1.t))
	output.write("\n")

	print "Number of sub-slots already used by central controller are %s." % (CC1.ts)
	output.write("Number of sub-slots already used by central controller are %s." % (CC1.ts))
	output.write("\n")
	
	print "\n"
	output.write("\n")
	
	nsus = np.random.poisson(lamb-1,1)[0] + 1
	
	CCt = CC1.CCuse
	
	CC1.SUs_gen_sync(p, nsus)
	CC2.SUs_gen_sync(p, nsus)
	
	print "In this slot there are %s secondary users." %(nsus)
	output.write("In this slot there are %s secondary users." %(nsus))
	output.write("\n")
	
	choosen_actions1 = {}
	choosen_actions2 = {}
	
	for i in range(0, nsus):
		choosen_actions1[i] = []
		choosen_actions2[i] = []
	
	conflicts1 = 0
	conflicts2 = 0
	
	rewards1 = [0 for j in range(0,CC1.nsus)]
	rewards2 = [0 for j in range(0,CC2.nsus)]

	
	while CC1.ts < CC1.Tsu or CC2.ts < CC2.Ts:
		su_actions1 = CC1.get_su_action()
		CC1.genRewards(p)
		
		su_actions2 = CC2.get_su_action()
		CC2.genRewards(p)
		
		selection_data.write("--------------------------------------------------------------------------------")
		selection_data.write("\n")
		selection_data.write("t = %s and ts = %s" %(CC1.t, CC1.ts))
		selection_data.write("\n")
		selection_data.write("--------------------------------------------------------------------------------")
		selection_data.write("\n")		
		selection_data.write("The chosen actions for CC1 are %s, and for CC2 are %s,"%(su_actions1, su_actions2))
		selection_data.write("\n")
		selection_data.write("the conflicts are: %s and %s respectively,"%(CC1.conflicts, CC2.conflicts))
		selection_data.write("\n")
		selection_data.write("and the rewards are %s and %s respectively." % (CC1.rewards, CC2.rewards))
		selection_data.write("\n")
		
		conflicts1 += len(CC1.permits) - sum(CC1.permits)
		conflicts2 += len(CC2.permits) - sum(CC2.permits)
		
		for i in range(0, nsus):
			choosen_actions1[i].append(su_actions1[i])
			choosen_actions2[i].append(su_actions2[i])
			
			
		rewards1 = [rewards1[j] + CC1.rewards[j] for j in range(0,CC1.nsus)]
		rewards2 = [rewards2[j] + CC2.rewards[j] for j in range(0,CC2.nsus)]
		
	
	dict = {}
			
	for i in range(0,CC1.narms):
		dict[i] = p[i]			
	
	p_sorted = np.array(sorted(dict, key = lambda x: dict[x], reverse = True))
	
	
	best_reward = int(sum([p[q] for q in p_sorted[range(0,CC1.nsus)]]) * Ts)
	
	slots += Ts * CC1.nsus
	
	regretlist1.append((best_reward - sum(rewards1)) / float(CC1.nsus))
	regretlist2.append((best_reward - sum(rewards2)) / float(CC2.nsus))
	
	nuserslist.append(CC1.nsus)
	
	successlist1.append(sum(rewards1))
	conflictlist1.append(conflicts1)
	
	successlist2.append(sum(rewards2))
	conflictlist2.append(conflicts2)
	
	output_data.write(str(CC1.t) + "," + str(CC1.nsus) + "," + str(sum(rewards1)) + "," +
		str(sum(rewards2)) + "," + str(best_reward) + "," + str(best_reward - sum(rewards1)) +
		"," + str(best_reward - sum(rewards2)) + "," + str((best_reward - sum(rewards1)) / float(CC1.nsus)) 
		+ "," + str((best_reward - sum(rewards2)) / float(CC2.nsus)) 
		+ "," + str(conflicts1)+ "," + str(conflicts2))
	output_data.write("\n")
	
	print "\n"
	output.write("\n")
	
	print "While the best case cummulative reward for this slot is %s, \n actual reward for CC1 is %s, \n and for CC2 is %s." % (best_reward, sum(rewards1), sum(rewards2))
	output.write("While the best case cummulative reward for this slot is %s, \n actual reward for CC1 is %s, \n and for CC2 is %s." % (best_reward, sum(rewards1), sum(rewards2)))
	output.write("\n")
	
	print "\n"
	output.write("\n")
	
	print "Actual rewards for CC1 are %s, \n and that for %s." %(rewards1, rewards2)
	output.write("Actual rewards for CC1 are %s, \n and that for %s." %(rewards1, rewards2))
	output.write("\n")
	
	print "\n"
	output.write("\n")
	
	print "For CC1 regret for this time slots is %s, which averages to %s," %(best_reward - sum(rewards1), (best_reward - sum(rewards1))/float(CC1.nsus))
	output.write("For CC1 regret for this time slots is %s, which averages to %s," %(best_reward - sum(rewards1), (best_reward - sum(rewards1))/float(CC1.nsus)))
	output.write("\n")
	
	print "and for CC2 regret for this time slots is %s, which averages to %s." %(best_reward - sum(rewards2), (best_reward - sum(rewards2))/float(CC2.nsus))
	output.write("and for CC2 regret for this time slots is %s, which averages to %s." %(best_reward - sum(rewards2), (best_reward - sum(rewards2))/float(CC2.nsus)))
	output.write("\n")
	
	print "\n"
	output.write("\n")
	
	print "There were %s conflicts in this slot for CC1," %(conflicts1)
	output.write("There were %s conflicts in this slot for CC1," %(conflicts1))
	output.write("\n")
	
	
	print "and %s conflicts in this slot for CC2." %(conflicts2)
	output.write("and %s conflicts in this slot for CC2." %(conflicts2))
	output.write("\n")
	
	print "\n"
	output.write("\n")
	
	print "==================================================================================="
	output.write("===================================================================================")
	output.write("\n")
	
	print "\n"
	output.write("\n")
	
	CC2.ts =1
	CC2.t += 1
	
	plt.figure(l)
	plt.subplot(211)
	
	for i in range(0, nsus):
		plt.plot(range(1, len(choosen_actions1[i]) + 1), choosen_actions1[i])
	
	plt.subplot(212)
	
	for i in range(0, nsus):
		plt.plot(range(1, len(choosen_actions2[i]) + 1), choosen_actions2[i])
	
	fig1 = plt.gcf()
	plt.draw()
	
	fig1.savefig("CCA\\" + str(num) + "\\Sim_"+str(l)+"_"+str(nsus)+".png", dpi=100)	
	l += 1

print "==================================================================================="
output.write("===================================================================================")
output.write("\n")	


plt.figure(l*10)
plt.subplot(211)
plt.plot(range(1,T+1), regretlist1, 'bo', range(1,T+1), regretlist2, 'ro')
plt.xlabel('Time Slots')
plt.ylabel('Average regret per user in the slot')
plt.title('Histogram of IQ')
plt.subplot(212)
plt.plot(range(1,T+1), conflictlist1, 'bx', range(1,T+1), conflictlist2, 'rx')
plt.xlabel('Time Slots')
plt.ylabel('Conflicts in the slot')
plt.title('Histogram of IQ')

fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig(regret_figure, dpi=100)	

output.close()
output_data.close()
selection_data.close()
