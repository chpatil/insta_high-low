import art
import replit
import random
import game_data
start_flag=True
no_first_attempt=False
wrong_answer=False
score=0
a={}
b={}
retainer={}
def get_data():
  data=game_data.data
  return data[random.randint(0,len(data)-1)]
def get_sentence(a,object):
  return f"Compare {object}: "+a['name']+", a "+a['description']+", from "+ a['country']
def check(decision,a,b):
    if(a["follower_count"]>b["follower_count"]):
      higher="a"
    else:
      higher="b"
    if(decision==higher):
      return True
    else:
      return False

while(start_flag):
  print(art.logo)
  if(no_first_attempt):
    print("You're right! Current score: "+str(score))
  no_first_attempt=True
  #print(str(a))
  if(len(a)==0):
    a=get_data()
  #print(a)
  b=get_data()
  #print(b)
  print(get_sentence(a,"A"))
  print(art.vs)
  print(get_sentence(b,"B"))
  if(check(input("Who has more followers? Type 'A' or 'B': ").lower(),a,b)):
    score+=1
    replit.clear()
    a=b
  else:
    replit.clear()
    print(art.logo)
    print("Sorry, that's wrong. Final score: "+str(score))
    break 