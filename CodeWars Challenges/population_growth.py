# In a small town the population is p0 = 1000 at the beginning of a year. The population regularly 
# increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. 
# How many years does the town need to see its population greater or equal to p = 1200 inhabitants?
def nb_year(p0, percent, aug, p):
    yr_count = 0
    while p0 < p:
        p0 = int(p0 * (1 + (percent / 100))) + aug 
        yr_count += 1 
    return yr_count
# Percent sometimes returns a float value which messes up the count (e.g. 0.5 of a human).
