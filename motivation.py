""".Imagine you need to repeat a cheerful message. Write a program that uses a for
loop to print "ALL IS WELL" exactly twenty times. How will you set up your loop to 
ensure this message appears the right number of times?"""

#using rangefunction
def motivation():
    for i in range(0,20):
        print("ALL IS WELL")
str = input("if you are not feeling well or de motivated just enter not well: ").lower()
if str == 'not well':
  motivation()
else :
  print("its ok, just breath and enjoy bye ...")
