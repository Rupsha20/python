# Define initial states
left_bank = ['farmer', 'wolf', 'goat', 'cabbage']
right_bank = []
boat_position = 'left'

def display_state():
    print(f"Left Bank: {left_bank}",end=';')
    print(f"Right Bank: {right_bank}")
    print(f"Boat is on the {boat_position} bank")
    print('-' * 10)

def move(item=None):        # none can handle both cases where the farmer moves with an item or moves alone.
    global boat_position
    
    if boat_position == 'left':
        if item:
            left_bank.remove(item)
            right_bank.append(item)
        boat_position = 'right'
    else:
        if item:
            right_bank.remove(item)
            left_bank.append(item)
        boat_position = 'left'
    
    display_state()

def solve():
    # Step by step moves to ensure safety
    steps = [
        ('goat',),     # 1. Farmer takes the goat across
        (None,),       # 2. Farmer returns alone
        ('wolf',),     # 3. Farmer takes the wolf across
        ('goat',),     # 4. Farmer brings the goat back
        ('cabbage',),  # 5. Farmer takes the cabbage across
        (None,),       # 6. Farmer returns alone
        ('goat',)      # 7. Farmer takes the goat across again
    ]
    
    for step in steps:
        if step[0]:
            move(step[0])      # when the farmer tranport with an item
        else:
            move()         # when the farmer tranport without an item or moves alone

    print("All items successfully transported across the river!")

# Run the solution
display_state()
solve()