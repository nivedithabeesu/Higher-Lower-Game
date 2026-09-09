import random
import subprocess

import game_art
import game_database


print(game_art.game_logo)
score=0

def display_accountinfo(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name}, a {description}, from{country}"
def check_answer(guess,followers_1,followers_2):
    if followers_1<followers_2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return False

account_2=random.choice(game_database.data)
continue_flag=True
while continue_flag:
    account_1 = account_2
    account_2 = random.choice(game_database.data)
    while account_1==account_2:
        account_2=random.choice(game_database.data)

    print(f"compare 1:{display_accountinfo(account_1)}")
    print(game_art.vs)
    print(f"compare 2:{display_accountinfo(account_2)}")
    guess=int(input("who has more followers? type 1 or 2:"))
    followers_count_1=account_1["follower_count"]
    followers_count_2=account_2["follower_count"]
    is_correct=check_answer(guess,followers_count_1,followers_count_2)
    subprocess.run("cls", shell=True)
    print(game_art.game_logo)
    if is_correct==True:
        score +=1
        print(f"you are right your score is:{score}")
    else:
        print(f"you are wrong your score is:{score}")
        continue_flag=False



