
score = int(0)

# INTRODUCTION
# ZELF VERZONNEN!!!
print ('Welcome stranger. Welcome to The Game ')
print ("You're here to find out, if you can reclaim ")
print ("The secrets I keep, not one is the same ")
name = input ("So without further ado, will you tell me your name?: ")

# QUESTION 1 (CHESS)
# RIDDLE VAN INTERNET
print ('')
print ('Thirty men and ladies two')
print ('Gathered for a festive do')
print ('Dressed quite formal, black and white')
print ('Soon movement turned to nasty fight.')
question1 = input ('What am I?: ')
if question1 == 'chess':
    score = score + 10
    print ('')
    print ('You got it right.')
else:
    print ('')
    print (name + ' ....you gave me a fright')
 
# QUESTION 2 (SPACE)
# RIDDLE VAN INTERNET
print ('')
print ('I have no beginning, no middle or end')
print ("And all the greatest thinkers see me, but can't comprehend.")
question2 = input ('What am I?: ')
if question2 == 'space':
    score = score + 10
    print ('')
    print ('Your answer was well-spent.')
else:
    print ('')
    print ('There is still time to amend.')

# QUESTION 3 (SHADOW)
# RIDDLE VAN INTERNET
print ('')
print ('By Moon or by Sun, I shall be found')
print ("Yet I am undone, if there's no light around.")
question3 = input ('What am I?: ')
if question3 == 'shadow' or question3 == 'a shadow' or question3 =='shadows':
    score = score + 10
    if score == 30:
        print ('')
        print (name + ' you continue to astound.')
    else:
        print ('')
        print ('You can stick around.')
else:
    print ('')
    print ("Perhaps you'll come around.")

# QUESTION 4 (STORM)
# RIDDLE VAN INTERNET
print ('')
print ('I have an eye but cannot see')
print ("You'll head inside, when you see me.")
question4 = input ('What am I?: ')
if question4 == 'storm' or question4 =='a storm' or question4 == 'hurricane' or question4 =='a hurricane':
    score = score + 10
    if score == 40:
        print ('')
        print ('I am filled with glee.')
    else:
        print ('')
        print ('I agree.')
else:
    print ('')
    print ("You can still flee.")

# QUESTION 5 (ORANGE)
# RIDDLE VAN INTERNET
print ('')
print ("Strip my skin twice, and my flesh you'll reveal")
print ("I taste sweet and tart, now throw out the peel.")
question5 = input ('What am I?: ')
if question5 == 'orange' or  question5 == 'an orange' or  question5 =='a orange' or question5 == 'oranges':
    score = score + 10
print (score)

# RHYMES 1 (RHYME)
# ZELF VERZONNEN!!!

if score == 0:
    print ('')
    print (("Frankly ") + name + (", I don't think you've tried at all"))
    print ("Maybe next time, I will have to drawl...")
    print ("Goodbye for now, I hope that you've learned")
    print ("That my treasure is not easily earned.")
    SystemExit

elif score >=10 and score <=30:
    print ('')
    print (("I'll have to say ") + name + (", that at least you have tried"))
    print ("But it wasn't enough, my secrets will continue to hide.")
    print ("Maybe, perhaps, you can try once more")
    print ("And next time I might even open the door.")
    SystemExit

elif score >30:
    print ('')
    print (name + " you've surprised me, I cannot deny")
    print ("My expectations for you, are now very high.")
    print ("Perhaps my secrets, will be yours to keep")
    print ("But that's an offer, that doesn't come cheap.")
    print ("These next few questions, I don't think you're aware")
    print ("The wrong words can bring an end, to this whole affair.")
    print ("So please " + name + ", do take your time")
    rhyme1 = input ('And finish my ')
    if rhyme1 == 'rhyme':
        score = score + 10
        print ('')
        print ('The first one was easy, it was handed to you')
        print ('This next one might be, hard to get through.')
    else:
        print ('')
        print ("Since you couldn't even, get past this first one")
        print ("Perhaps it seems like our time here is done.")
        print ("I've warned you that one word, is all that it takes")
        print ("To end our time together, and pull on the brakes.")
        SystemExit

# RHYMES 2 (TEA)
# ZELF VERZONNEN!!!

if score == 60:
    print ('')
    print ("It's late and it's cozy, I'm in the mood for some thing ")
    print ("No gold nor silver nearby, but it does have a ring.")
    print ("Tonight I'm thinking, it will be sweetened by bee")
    rhyme2 = input ("I'm making myself a cup of ")        
    if rhyme2 == 'tea':
        score = score + 10
        print ('')
        print ("One step closer, to finding my end")
        print ("By then I'm sure, I'll consider you a friend.")
    else:
        print ('')
        print ("It only took two, to get you to fail")
        print ("No more chances for you, this ship has set sail.")
        SystemExit

# RHYMES 3 (FIRE)
# ZELF VERZONNEN!!!

if score == 70:
    print ('')
    print ("The bells are still ringing, I can't do this alone")
    print ("We're waiting too long, can't you see it has grown.")
    print ("I'm telling you now, the situation is dire")
    rhyme3 = input ("So please help me put out this ")
    if rhyme3 == 'fire':
        score = score + 10
        print ('')
        print ("Well done " + name + ", you're almost there")
        print ("All that there's left, is a single pair.")
    else:
        print ('')
        print ("So closeby, and yet so far")
        print ("You must know all my riddles, I have set the bar.")
        SystemExit

# RHYMES 4 (LOVE)
# ZELF VERZONNEN!!!

if score == 80:
    print ('')
    print ("Two people together, all eyes fixed on them")
    print ("On their fingers you will see, a big shiny gem.")
    print ("Purity and innocence, symbolized by a dove ")
    rhyme4 = input ("I am a celebration of ")
    if rhyme4 == 'love':
        score = score + 10
    else:
        print ('')
        print ("This is where, we say goodbye")
        print ("You're welcome to try again, do not be shy.")
        SystemExit


# RHYMES 5 (USER NAME)
# ZELF VERZONNEN!!!

if score == 90:
    print ('')
    print ("We've reached the end " + name +  ", we have one more to go")
    print ("My hint to you is, that this one you know. ")
    print ("You might have to think though, there's no doubt about that")
    print ("But this answer is one, that some take from a hat.")
    print ("I've been with you ever since, you started this game")
    print ("This answer might even be, the one very same.")
    rhyme4 = input ("Who am I? ")
    if rhyme4 == name:
        score = score + 10
        print ('')
        print ("You've done it, you're done, you've found all that I'm hiding")
        print ("The time that we spent, will be a memory abiding.")
        print ("My secrets are yours, do with them as you please")
        print (("It was a pleasure to meet you ") + name + (", Keeper of the Keys."))
    else:
        print ('')
        print ("I've warned you that one word, is all that it takes")
        print ("To end our time together, and pull on the brakes.")
        print ("My secrets are mine, how lonely it may be")
        print ("But please do try again " + name + ", that is my final plea.")
        SystemExit

#if score > 50:
#   print ("Well then "  I cannot deny")
#   print ("Perhaps it is time for us to say goodbye")
#   laatste riddle is over de gebruiker. dus het input antwoord moet = name zijn!!!!!