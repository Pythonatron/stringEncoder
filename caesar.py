def caesar():
    
    def shift_route():
       direction = input("Choose a shift direction (left or right): ").lower()
       if direction not in ("left", "right") or direction == "":
            print("Choose a valid direction.")
            shift_route()
       else:
            return direction
            
    def shift_size():
        adjust = input("Choose a number for shift change: ")
        if not adjust.isnumeric() or adjust == "":
            print("Choose from numbers only.")
            shift_size()
        else:
            return int(adjust)
            
    direction = shift_route()
    n = shift_size()
   
    if direction ==  "right":
        new_letter = chr(((n % 26) + 97))
    else:
         new_letter = chr(((0 - n) % 26) + 97)
    return new_letter
  
x = caesar()
print('output letter',x)