def caesar():
    def shift_route():
       direction = input("Choose a shift direction (left or right): ").lower()
       if direction not in ("left", "right") or direction == "":
            print("Choose a valid direction.")
            shift_route()
       else:
            return direction
            
    def shift_size():
        print("Choose a number for shift change (preferably a number between 1 of 26. But it doesn't have to be)")
        adjust = input("Number for change: ")
        if not adjust.isnumeric() or adjust == "":
            print("Choose from numbers only.")
            shift_size()
        else:
            return int(adjust)
            
    direction = shift_route()
    n = shift_size()
   
    if direction ==  "right":
        nl = chr(((n % 26) + 97))
    else:
         nl = chr(((0 - n) % 26) + 97)
    return nl
    #x = caesar()