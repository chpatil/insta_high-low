import art
import replit
import random
import game_data
start_flag=True
no_first_attempt=False
wrong_answer=False
score=0
retainer={}
def get_data():
  data=game_data.data
  return data[random.randint(0,len(data))]
def get_sentence(a):
  return "Compare A: "+a["name"]+", a "+a["description"]+", from"+ a["country"]
def check(decision,a,b):
    if(a["followers"]>b["followers"]):
      higher="a"
    else:
      higher="b"
      retainer=b
    if(decision==higher):
      return True
    else:
      return False

while(start_flag):
  print(art.logo)
  if(no_first_attempt):
    print("You're right! Current score: "+score)
  no_first_attempt=True
  a=retainer
  b={}
  if(a is None):
    a=get_data()
  b=get_data()
  print(get_sentence(a))
  print(art.vs)
  print(get_sentence(b))
  if(lower(input("Who has more followers? Type 'A' or 'B': ")),a,b):
    score+=1
    replit.clear()
  else:
    replit.clear()
    print(art.logo)
    print("Sorry, that's wrong. Final score: "+score)
    break
    return
    
    
  
    
    