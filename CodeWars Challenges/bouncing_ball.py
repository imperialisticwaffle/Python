# A child is playing with a ball on the nth floor of a tall building. 
# The height of this floor, h, is known.

# He drops the ball out of the window. The ball bounces (for example), to two-thirds 
# of its height (a bounce of 0.66).

# His mother looks out of a window 1.5 meters from the ground.

# How many times will the mother see the ball pass in front of her window (including when 
# it's falling and bouncing?

# Three conditions must be met for a valid experiment:

    # Float parameter "h" in meters must be greater than 0
    # Float parameter "bounce" must be greater than 0 and less than 1
    # Float parameter "window" must be less than h.

# If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

def bouncing_ball(h, bounce, window):
    count = 0
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    else:
        while h > window:
            if (h * bounce) <= window:
                count += 1
                return count
            elif (h * bounce) > window:
                h = h * bounce
                count += 2
        return count
bouncing_ball(3, 0.66, 1.5) # Expected sighting count is 3.

# Most efficient solution:
def bouncingBall(h, bounce, window):
    if not 0 < bounce < 1: return -1
    count = 0
    while h > window:
        count += 1 # Down sighting.
        h *= bounce # Rebound value.
        if h > window: count += 1 # If rebound > window height, up sighting.
    return count or -1
        
