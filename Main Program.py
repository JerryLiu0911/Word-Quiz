import random  #imports random library
x=list(range(0,20))   #sets for range of values
wa=[]     #list for the correct answers that the player got wrong
wq=[]     #list for the question number the player got wrong
s=0       #score counter
w1=["hot", "summer", "hard", "dry", "simple",                 #word bank #1
"light", "weak", "male", "sad", "win", "small",
"ignore", "buy", "succeed", "reject",
"prevent", "exclude","stay", "ordinary","love"]
w2=["cold", "winter", "soft", "wet", "complex",               #word bank #2
"darkness", "strong", "female", "happy",
"lose", "big", "pay attention", "sell", "fail",
"accept", "allow", "include","leave","unusual","hate"]
for question in range(1,11):                               #shows 10 questions
  a=random.choice(x)                                       #chooses a random set of words and removes them from the list so they don't appear again in another question
  x.remove(a)
  b=random.choice(x)
  x.remove(b)
  print("Q"+str(question),":", w1[a],"is to",w2[a], ", as", w1[b], "is to?") #structure of the questions
  if ans:=input()==w2[b] :
    print ("correct answer!")                              #marking the answers
    s+=1                                                   #adds marks
  else:
    print("incorrect.Let's move on.")
    wa.append(b)                                           #appends the index of the correct answer for the wrong question to list, and question number
    wq.append(question)
  print()
print ("You scored",s,"out of 10 correct.")                #player score
for w in range(0,len(wa)):                                 #a for loop to show the correct answers to the questions the player answered incorrectly
  print("The answer to question", wq[w],"is ",w2[wa[w]])
