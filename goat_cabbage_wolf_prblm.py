
left_bank = ['farmer', 'wolf', 'goat', 'cabbage']
right_bank = []
boat_position = 'left'

def display_state():
    print(f"Left Bank: {left_bank}",end=';')
    print(f"Right Bank: {right_bank}")
    print(f"Boat is on the {boat_position} bank")
    print('-' * 10)

def move(item=None):        
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
    steps = [
        ('goat',),     
        (None,),      
        ('wolf',),     
        ('goat',),   
        ('cabbage',), 
        (None,),    
        ('goat',)     
    ]
    
    for step in steps:
        if step[0]:
            move(step[0])      
        else:
            move()       

    print("All items successfully transported across the river!")

# Run the solution
display_state()
solve()
