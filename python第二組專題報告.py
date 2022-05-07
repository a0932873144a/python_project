# -*- coding: utf-8 -*-
"""「python第二組專題報告.ipynb」的副本

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fzxYlX7VPSQAodgKSCuq3Invx4NdfXii

簡易版：
"""

N1=0
N2=0
Z=0
while True:
  N=int(input("請輸入欲投候選人號碼"))
  if N == 1 :
     N1 += 1
  if N == 2 :
     N2 += 1
  if N == 0 :
     break
  elif N != 1 and N != 2:
     Z+=1
    
if N1 > N2 :
  print("N1 won the election.")
elif N1 < N2 : 
  print("N2 won the election.")
else:
  print("No one won the election.")

print("Total votes of N1 : ", N1)
print("Total votes of N2 : ", N2)
print("Total null votes : ", Z)

"""進階版："""

import pandas as pd

df = pd.read_csv('president_county_candidate.csv') 
print(df)

vote = df[df["won"] == True]
print(vote)

"""依候選人統計："""

#Biden的票
vote_Biden = vote['candidate'] == "Joe Biden"
print("Joe Biden get", vote_Biden.sum(), "votes\n")

#Trump的票
vote_Trump = vote['candidate'] == "Donald Trump"
print("Donald Trump get", vote_Trump.sum(), "votes\n")

#Jorgensen的票
vote_Jorgensen = vote['candidate'] == "Jo Jorgensen"
print("Jo Jorgensen get", vote_Jorgensen.sum(), "votes\n")

#Hawkins的票
vote_Hawkins = vote['candidate'] == "Howie Hawkins"
print("Howie Hawkins get", vote_Hawkins.sum(), "votes\n")

#Gloria的票
vote_Gloria = vote['candidate'] == "Gloria La Riva"
print("Gloria La Riva get", vote_Gloria.sum(), "votes\n")

#Pierce的票
vote_Pierce = vote['candidate'] == "Brock Pierce"
print("Brock Pierce get", vote_Pierce.sum(), "votes\n")

#Fuente的票
vote_Fuente = vote['candidate'] == "Rocky De La Fuente"
print("Rocky De La Fuente get", vote_Fuente.sum(), "votes\n")

#Blankenship的票
vote_Blankenship = vote['candidate'] == "Don Blankenship"
print("Don Blankenship get", vote_Blankenship.sum(), "votes\n")

#Carroll的票
vote_Carroll = vote['candidate'] == "Brian Carroll"
print("Brian Carroll get", vote_Carroll.sum(), "votes\n")

#West的票
vote_West = vote['candidate'] == "Kanye West"
print("Kanye West get", vote_West.sum(), "votes\n")

#Simmons的票
vote_Simmons = vote['candidate'] == "Jade Simmons"
print("Jade Simmons get", vote_Simmons.sum(), "votes\n")

#Hoefling的票
vote_Hoefling = vote['candidate'] == "Tom Hoefling"
print("Tom Hoefling get", vote_Hoefling.sum(), "votes\n")

#Hammons的票
vote_Hammons = vote['candidate'] == "Bill Hammons"
print("Bill Hammons get", vote_Hammons.sum(), "votes\n")

#Boddie的票
vote_Boddie = vote['candidate'] == "President Boddie"
print("President Boddie get", vote_Boddie.sum(), "votes\n")

#Kennedy的票
vote_Kennedy = vote['candidate'] == "Alyson Kennedy"
print("Alyson Kennedy get", vote_Kennedy.sum(), "votes\n")

#Collins的票
vote_Collins = vote['candidate'] == "Phil Collins"
print("Phil Collins get", vote_Collins.sum(), "votes\n")

#Huber的票
vote_Huber = vote['candidate'] == "Blake Huber"
print("Blake Huber get", vote_Huber.sum(), "votes\n")

#Segal的票
vote_Segal = vote['candidate'] == "Jerome Segal"
print("Jerome Segal get", vote_Segal.sum(), "votes\n")

#Scalf的票
vote_Scalf = vote['candidate'] == "Zachary Scalf"
print("Zachary Scalf get", vote_Scalf.sum(), "votes\n")

#Swing的票
vote_Swing = vote['candidate'] == "Gary Swing"
print("Gary Swing get", vote_Swing.sum(), "votes\n")

#Kopitke的票
vote_Kopitke = vote['candidate'] == "Kyle Kopitke"
print("Kyle Kopitke get", vote_Kopitke.sum(), "votes\n")

#McCormic的票
vote_McCormic = vote['candidate'] == "Keith McCormic"
print("Keith McCormic get", vote_McCormic.sum(), "votes\n")

#LaFontaine的票
vote_LaFontaine = vote['candidate'] == "Christopher LaFontaine"
print("Christopher LaFontaine get", vote_LaFontaine.sum(), "votes\n")

#Duncan的票
vote_Duncan = vote['candidate'] == "Richard Duncan"
print("Richard Duncan get", vote_Duncan.sum(), "votes\n")

#Paige的票
vote_Paige = vote['candidate'] == "Brooke Paige"
print("Brooke Paige get", vote_Paige.sum(), "votes\n")

#Myers的票
vote_Myers = vote['candidate'] == "John Richard Myers"
print("John Richard Myers get", vote_Myers.sum(), "votes\n")

#Gammon的票
vote_Gammon = vote['candidate'] == "Connie Gammon"
print("Connie Gammon get", vote_Gammon.sum(), "votes\n")

#Charles的票
vote_Charles = vote['candidate'] == "Mark Charles"
print("Mark Charles get", vote_Charles.sum(), "votes\n")

#Kopitke的票
vote_Kopitke = vote['candidate'] == "Kyle Kopitke"
print("Kyle Kopitke get", vote_Kopitke.sum(), "votes\n")

#McHugh的票
vote_McHugh = vote['candidate'] == "Joe McHugh"
print("Joe McHugh get", vote_McHugh.sum(), "votes\n")

#Kishore的票
vote_Kishore = vote['candidate'] == "Joseph Kishore"
print("Joseph Kishore get", vote_Kishore.sum(), "votes\n")

#Hunter的票
vote_Hunter = vote['candidate'] == "Dario Hunter"
print("Dario Hunter get", vote_Hunter.sum(), "votes\n")

#Princess的票
vote_Princess = vote['candidate'] == "Princess Jacob-Fambro"
print("Princess Jacob-Fambro get", vote_Princess.sum(), "votes\n")

#Scott的票
vote_Scott = vote['candidate'] == "Jordan Scott"
print("Jordan Scott get", vote_Scott.sum(), "votes\n")

#廢票
Write_ins = vote['candidate'] == " Write-ins"
print("Write-ins gets", Write_ins.sum(), "votes\n")

candidates = {'Biden' : vote_Biden.sum(), 'Trump' : vote_Trump.sum(), 'Jorgensen' : vote_Jorgensen.sum(), 'Hawkins' : vote_Hawkins.sum(), 'Gloria' : vote_Gloria.sum(), 'Pierce' : vote_Pierce.sum(), 'Fuente' : vote_Fuente.sum(), 'Blankenship' : vote_Blankenship.sum(), 'Carroll' : vote_Carroll.sum(), 'West' : vote_West.sum(), 'Simmons' : vote_Simmons.sum(), 'Hoefling' :  vote_Hoefling.sum(), 'Hammons' : vote_Hammons.sum(), 'Boddie' : vote_Boddie.sum(), 'Kennedy' : vote_Kennedy.sum(), 'Collins' : vote_Collins.sum(), 'Huber' : vote_Huber.sum(), 'Segal' : vote_Segal.sum(), 'Scalf' : vote_Scalf.sum(), 
              'Swing' : vote_Swing.sum(), 'Kopitke' : vote_Kopitke.sum(), 'McCormic' : vote_McCormic.sum(), 'LaFontaine' : vote_LaFontaine.sum(), 'Duncan' : vote_Duncan.sum(), 'Paige' : vote_Paige.sum(), 'Myers' : vote_Myers.sum(), 'Gammon' : vote_Gammon.sum(), 'Charles' : vote_Charles.sum(), 'Kopitke' : vote_Kopitke.sum(), 'McHugh' : vote_McHugh.sum(), 'Kishore' : vote_Kishore.sum(), 'Hunter' : vote_Hunter.sum(), 'Princess' : vote_Princess.sum(), 'Scott' : vote_Scott.sum()}

winner_votes = max(candidates.values())

def get_key(val):
    for key, value in candidates.items():
         if val == value:
             return key
 
    return "There is no such Key"

print("The winner is ", get_key(winner_votes), ",who gets ", winner_votes, "votes")

"""工具欄："""

print(select_df.describe()) # 回傳描述性統計  
print("---")

president.drop(['party','won'], axis=1, inplace=True)   #drop是把不需要的數據(欄)丟掉

result_votes = df[['total_votes']]\.groupby(['state','county']).mean().reset_index()
result_votes.head()

#dict = {  
    "factory": "Taipei",
    "sensor1": "1",
    "sensor2": "2",
    "sensor3": "3",
    "sensor4": "4",
    "sensor5": "5"}