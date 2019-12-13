import random
no_of_quick_picks = int(input("Insert number of quick picks: "))
for x in range(no_of_quick_picks):
    quick_picks = [random.randint(0, 45) for i in range(6)]
    quick_picks.sort()
    print(str(quick_picks).strip("[]"))
