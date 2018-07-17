import random

def simulation(trial):
    success = 0

    for i in range(trial):
        doors = [1, 2, 3]
        prize = random.choice(doors)
        user_choice = random.choice(doors)
        
        npc_choices = [1, 2, 3]
        
        npc_choice = None
        # 나머지 두군데 중에 아무거나 보여줘도 됨.
        if prize == user_choice:
            npc_choices.remove(user_choice)
            npc_choice = random.choice(npc_choices)
        # 유저가 선택한것도 아니고, 정답도 아닌 것을 보여줘야됨.
        else:
            npc_choices.remove(user_choice)
            npc_choices.remove(prize)
            npc_choice = npc_choices[0]

        # 1,2,3 중에 user_choice도 아니고 npc_choice도 아닌 다른 하나를 고른다.
        final_choices = [1, 2, 3]
        final_choices.remove(user_choice)
        final_choices.remove(npc_choice)

        final_choice = final_choices[0]

        if final_choice == prize:
            success += 1
    
    return success/trial

trial = int(input("How many do you want to simulate Monty-Hall Problem?"))
print(simulation(trial))