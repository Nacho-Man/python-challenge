import os
import csv

csvpath = os.path.join('..', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    #Using DictReader format
    csvreader = csv.DictReader(csvfile, delimiter=',')
    
    #init begin variable
    khan_vote = 0
    cor_vote = 0
    li_vote = 0
    o_vote = 0
    tot = 0

    #Loop
    for line in csvreader:
        
        cand = line["Candidate"]
        tot = tot + 1

        #Vote Tally
        if cand == "Khan":
            khan_vote = khan_vote + 1
        if cand == "Correy":
            cor_vote = cor_vote + 1
        if cand == "Li":
            li_vote = li_vote + 1
        if cand == "O'Tooley":
            o_vote = o_vote + 1

    #winner compairson
    #Bracket Computation - win or tie
    a_win = list
    b_win = list
    champ = None
    #Round 1
    #(name, vote number)
    if li_vote > khan_vote:
        a_win = ["Li", li_vote]
    if li_vote == khan_vote:
        a_win = ["Khan and Li", li_vote] 
    a_win = ["Khan", khan_vote] 
    if cor_vote > o_vote:      
        b_win = ["Correy", cor_vote]
    if cor_vote == o_vote:
        b_win = ["Correy and O'Tooley", cor_vote]
    b_win = ("O'Valley", o_vote)
    #Round 2
    if a_win[1] > b_win[1]:
        champ = a_win
    if a_win[1] < b_win[1]:
        champ = b_win
    if a_win[1] == b_win[1]:
        champ = str(f"{a_win[0]} and {b_win[0]}")




    #Percentage Vote Init
    khan_per = 0    
    cor_per = 0
    li_per = 0 

    ###lambda format
    ft = lambda a: "{0:.3%}".format(a)

    ###Percentage Vote0
    per_khan = khan_vote / tot
    per_cor = cor_vote / tot
    per_li = li_vote /tot
    per_o = o_vote / tot

    print("Election Results")
    print("------------------------------")
    print(f"Total Votes: {tot}")
    print("------------------------------")
    print(f"Khan: {ft(per_khan)} ({khan_vote})")
    print(f"Correy: {ft(per_cor)} ({cor_vote})")
    print(f"Correy: {ft(per_li)} ({li_vote})")
    print(f"Correy: {ft(per_o)} ({o_vote})")
    print("------------------------------")   
    print(f"Winner: {champ[0]}")
    print("------------------------------")