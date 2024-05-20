label cafe_start:
    $ cafe = True

    if persistent.cafe_taste_knowledge == True:
        l "Oh my, you surely know how to get me excited! I'll meet you there!"
    else:
        l "That sounds good to me! I'll meet you there!"

    n "You arrive a tad too early and find no space to park so you decide to park a few streets later and walk to the cafe."
    n "The inner walls are made out of glass and function as aquariums that seem to stretch on even beyond the ceiling."
    n "It's probably them though, atleast they seem to be enjoying themselves."
    n "When you get there Lilith is already sitting at a nice looking mahogany table."
    n "When she notices you she waves at you enthusiastically with a wide grin on her face."
    l "Heya, glad you could make it! "
    l "This place has a really nice atmosphere, those mahogany tables and the aquariums are real eye catchers don't you think?"
    l "Anyway, let's go order our food and then we can talk some more."
    n "You and Lilith walk towards the barista, as he glances up from his phone he greets you with a shy smile."
    n "He looks quite young, if you'd have to guess you would say he is somewhere around 17 years old."
    n "You get lost in the thoughts of how life was when you still were 17 until Lilith gives you a playful nudge."
    b "What could I get the both of you?"
    l " Hmm, I think I'm going for the ham and cheese sandwich and a cafe cubano.
    What are you choosing [name]? "
    menu:
        "I'll have the same as you.":
            jump cafe_food_choiceSame

        "I'll have the sandwich of the day and an espresso.":
            jump cafe_food_choice1

        "I'll have the beef sandwich and a frappuchino.":
            jump cafe_food_choice2

label cafe_food_choice1:
    jump cafe_food_result

label cafe_food_choice2:
    jump cafe_food_result

label cafe_food_choiceSame:
    l "You know what they say [name], great minds think alike. I guess that also counts for hungry stomachs."
    n "Lilith lets out a small chuckle."
label cafe_food_result:
    n "The barista smiles and says: \"Coming right up!\""
    n "Lilith and you walk back to your table and take a seat."

    n "Lilith gives you a mischievous smile."
    l "I just got a fun idea."
    n "She eagerly digs into her handbag and takes out two red six-sided dice."
    l "It's a little game I came up with a while ago, I want to test it with you."
    l "So, the rules are simple. "
    l "{size=*0.5}Actually they might be a little complex...{/size}"
    l "I will first roll two dice and tell you the sum of them. If I roll a double so for example if I roll two four's an extra four is added. So every double I roll is effectively a tripple."
    l "After that I can take one action each turn."
    l "I can change one of the dice numbers into any number that isn't the number it was the last turn, so a three could become any number except for a three."
    l "But I also can subtract a value from one dice and add it to another, so a five and a one could become two three's."
    l "After every action I take I'll tell you the new sum of the dice."
    l "So, do you still want to do this?"
    menu:
        "Sure, I'm excited to try it out!":
            jump cafe_dice_continue

        "Actually, I'm not sure about this anymore.":
            jump cafe_dice_stop

label cafe_dice_continue:
    $ persistent.dice_counter += 1
    n "Lilith throws two six-sided dice and puts her hands in front of them so you can't see the result."
    l "The sum of the dice is nine."
    if persistent.dice_knowledge == True:
        n "You remember that the first dice is 6 and the second dice is 3."
    menu:
        "*Use the reflection of the aquarium to peek at the dice.*":
            $ cafedicecheat = True
            jump cafe_dice_result
        "*Play normally.*":
            jump cafe_dice_result



label cafe_dice_result:
    if cafedicecheat == True:
        n "You peek at the dice using the aquarium as a mirror, the first dice appears to be a 6 and the second is a 3."
        $ cafedicecheat = False
    n "Lilith waits for you to look away and she then takes an action."
    l "The sum of the dice is nine."
    n "She takes her next action."
    l "The sum of the dice is eight."
    n "Lilith hums an unfamiliar song as she takes her next action, it's quite catchy."
    $ persistent.song_knowledge = True
    l "The sum of the dice is five."
    l "So, that was the puzzle. You'll need one hint to solve it."
    l "The last action I took was changing the second dice.
    I hope that hint is helpful!"
    l "So, what was the number of the first dice on the first turn?"
    label cafe_dice_choice:
        $ dicenumber = renpy.input("Place your guess here", length=5)
        $ dicenumber = dicenumber.strip()

        if not dicenumber:
            $ dicenumber = "4"

        $ dicelength = len(dicenumber)

        if dicelength == 1:
            python:
                try:
                    dicenumber = int(dicenumber)
                except ValueError:
                    renpy.say(n, "That was a kind of weird response. Let's just pretend that never happened. Please enter a number this time.")
                    renpy.jump("cafe_dice_choice")
            if dicenumber > 6:
                n "Let's try that again, she is using six-sided dice, remember? So you can only choose a number from 1-6."
                jump cafe_dice_choice
        else:
            $ dicenumber = dicenumber.lower()
            #This sets the text to lowercase.
            if dicenumber == "one":
                $ dicenumber = 1
            elif dicenumber == "two":
                $ dicenumber = 2
            elif dicenumber == "three":
                $ dicenumber = 3
            elif dicenumber == "four":
                $ dicenumber = 4
            elif dicenumber == "five":
                $ dicenumber = 5
            elif dicenumber == "six":
                $ dicenumber = 6
            else: 
                n "That doesn't really feel like the right answer, you should give a number from 1-6, let me just put you back a little so you can retry."
                jump cafe_dice_choice
        $ dicenumber2 = 9 - dicenumber
        if dicenumber2 > 6:
            n "You do realise that that means the second dice would be a [dicenumber2], right?"
            n "Remember that the sum of both dice has to be 9."
            n "Let's just try again."
            jump cafe_dice_choice 
        else:
            l "So do you think the number of the second dice is [dicenumber2]?"
        menu:
            "Yes, that's right.":
                if dicenumber2 == 3:
                    label cafe_dice_right:
                    l "Wow, you managed to figure it out. Nicely done [name]!"
                    $ persistent.dice_knowledge = True
                    #TODO: Make a better segway for this.
                    jump cafe_rateCafe
                else:
                    label cafe_dice_wrong:
                    l "Nope, that's not the answer."
                    l "You gave it your best shot [name]!
                    I might have made this a bit too hard.

                    Would you like to know the answer?"
                    menu:
                        "Yeah, please tell me what the answer was.":
                            $ persistent.dice_knowledge = True
                            l "The first dice was 6 and the second dice was 3."
                            #TODO: Make a better segway.
                            jump cafe_rateCafe
                        "No, if I ever learn the answer I want it to be because I solved it.":
                            l "That's respectable but I'm not sure when you'll get your next chance, this is not something I do all of the time."
                            if persistent.dice_counter >= 2:
                                n "Oh I think she doesn't have to worry about that at all..."
                                n "Afterall, isn't this the [persistent.dice_counter] time you try this puzzle?"
                                if persistent.dice_knowledge == True:
                                    n "But what is peculiar to me is that you already know the correct answer, right?"
                                    n "I even gave you a reminder about it."
                                    n "And yet you got it wrong, why is that?"
                                    n "Is it because you want to see these lines of new dialogue?"
                                    #TODO: Check if the player never saw these lines and otherwise have the narrator say "no, that can't be the case, there mmust be a different reason..."
                            #TODO: Make this new segway a bit better because now it doesn't make much sense.
                            jump cafe_rateCafe

            "No, that's not right.":
                l "Oh,so what number do you think the second dice is [name]?"
                $ dicenumber2 = renpy.input("Place your guess here", length=5)
                $ dicenumber2 = dicenumber2.strip()

                if not dicenumber2:
                    $ dicenumber2 = "2"

                $ dicelength = len(dicenumber2)

                if dicelength == 1:
                    $ dicenumber2 = int(dicenumber2)
                else:
                    $ dicenumber2 = dicenumber2.lower()

                    if dicenumber2 == "one":
                        $ dicenumber2 = 1
                    elif dicenumber2 == "two":
                        $ dicenumber2 = 2
                    elif dicenumber2 == "three":
                        $ dicenumber2 = 3
                    elif dicenumber2 == "four":
                        $ dicenumber2 = 4
                    elif dicenumber2 == "five":
                        $ dicenumber2 = 5
                    elif dicenumber2 == "six":
                        $ dicenumber2 = 6
                if dicenumber == 6:
                    if dicenumber2 == 3:
                        jump cafe_dice_right
                    else:
                        jump cafe_dice_wrong
                else:
                    jump cafe_dice_wrong


label cafe_dice_stop:
    l "Oh no worries [name]!
    I might have made this a bit too daunting so I completely understand."
    #TODO: Make a slightly better segway for this.
    jump cafe_rateCafe



#TODO: In the code, at exactly this place there is a "jump cafe_rateCafe" extra. Find out if it ever belonged to something.

label cafe_rateCafe:
    n "Lilith looks around in pure awe, a bright smile forms on her face."
    l "So, what do you think of this place now that you've seen it for the first time?"

    menu:
        "Actually it's not the first time I've seen this place." if persistent.cafe_death_1:
            jump cafe_notTheFirstTimeISaw
        "It's fantastic! Look at all those fish!":
            jump cafe_rateCafe_great

        "This cafe really sucks.":
            jump cafe_rateCafe_bad

        "I can see why you like it but it's not really my thing.":
            jump cafe_rateCafe_okayish


label cafe_notTheFirstTimeISaw:
    l "Oh... I thought you said that you had only heard about this place."
    n "Lilith pauses, seemingly not knowing what to say."
    menu:
        "Oh, you probably just misheard me.":
            jump cafe_backOnTrack

label cafe_backOnTrack:
    n "Lilith lets out a polite chuckle."
    l "Oh, my bad then!"
    #TODO: ADD a better segway
    jump cafe_abigailJoke


label cafe_rateCafe_great:
    n "Lilith let's out a small giggle."
    l " I knew you would love it as much as me when I saw your smile.
    I've never seen so many colors at the same time, thank you for taking me here [name]!
    Just the fish on their own made this one of the best dates I ever had, it can only get better from here."
    $ persistent.cafe_taste_knowledge = True
    jump cafe_rateCafe_result

label cafe_rateCafe_okayish:
    n "Lilith flashes you an understanding smile."
    l "Ah, sorry to hear that, but I am really loving this place if that's worth something.
    Maybe we can go to a place you like next time?"
    l "I've never seen so many colors at the same time, thank you for taking me here [name].
    So far this is one of the best dates I ever had!"
    $ persistent.cafe_taste_knowledge = True
    jump cafe_rateCafe_result

label cafe_rateCafe_bad:
    $ love_points = -1
    $ love_meter_updater()
    n "Lilith frowns at your reaction."
    l "..."
    l "There's no need to drag this place down just because you don't like it."
    l "Lilith takes her phone and begins aimlessly scrolling on it, you can see her screen through the reflection on the aquarium.
    She's growing less and less responsive after every word you say until the two of you sit in pure silence for what feels like an hour."
    if persistent.need_pass_knowledge == True:
        n "Atleast you also managed to catch her password thanks to the reflection, it's 81155."
        $ persistent.pass_knowledge = True

    jump restaurant_death_1



label cafe_rateCafe_result:
    menu:
        "Sorry to ask you this, but did you have bad experiences in love?":
            l "That's quite an unusual question to ask [name], why do you think I did?"
            #Maybe rephrase it slightly, comes of as a bit defensive.
            menu:
                "Well, you said this was one of the best dates you've ever had. It seems as if your bar is set pretty low.":
                    $ cafe_badLove_lowbar = True
                    jump cafe_badLove
                "I just kind of had a feeling.":
                    $ cafe_badLove_justafeeling = True
                    jump cafe_badLove
                    #Make her mention something about this during the pshycic route?
        "You are very welcome, thank you for making me come here in the first place.":
            l "Did you just counter my thank you with another thank you?"
            l "Well, in that case I'll retaliate with a \"You are very welcome.\" aswell!"
            l "Lilith let's out a cute giggle. She has a gleeful look in her eyes."
            l "You know, you made laugh quite good there [name], now it's my turn! Would you like to hear a joke?"
            menu:
                "Sure, I'd love to!":
                    jump cafe_abigailJoke

label cafe_abigailJoke:
    l "So a priest, a monk and a rabbit enter a bar.
    Says the rabbit :\"Whoops, did you slip your tongue there Lilith?\""
    $ persistent.joke_knowledge = True
    menu:
        "Wow, that was a really good one!":
            jump cafe_joke_good
        "That was not funny at all.":
            jump cafe_joke_bad
        "Hmm, I'm not sure I'm getting the joke.":
            jump cafe_joke_dontGet
label cafe_joke_bad:
    $ love_points = -1
    $ love_meter_updater()
    n "Lilith looks saddened by your remark."

    l "Really? ..."
    l "I thought it was funny when Abigail told me..."
    menu:
        "Quick, come stand next to me!" if persistent.cafe_death_1:
            jump restaurant_death_1_prevented
        "Well...":
            jump restaurant_death_1


label cafe_joke_good:
    n "Lilith explodes in laughter."
    l "Exactly! The first time Abigail, my sister, told me that joke I spent an entire hour laughing.
    But then again, she always makes me laugh so much that I just might pass out one time."
    l "I'm kidding, I'm kidding! About the passing out part that is, she really is funny though."
    menu:
        "Quick, come stand next to me!" if persistent.cafe_death_1:
            jump restaurant_death_1_prevented
        "She sounds nice!":
            jump restaurant_death_1

label cafe_joke_dontGet:
    l "Oh, the point of the joke is that the other two who entered the bar where religious fiures, the monk and the priest.
    So the rabbit doesn't quite fit in, it's because he was actually a rabbi instead. So I mispronounced that hence the \"did you slip your tongue?\" ."
    l "Is the joke now funnier or did it now become less funny? It tends to be that way when you explain a joke so I'm sorry if I ruined it for you."
    menu:
        "Quick, come stand next to me!" if persistent.cafe_death_1:
            jump restaurant_death_1_prevented
        "No need to apoligize, I made you explain it. Besides, it's still pretty funny now that I understand the joke.":
            jump restaurant_death_1



label cafe_badLove:


    if cafe_badLove_lowbar == True:
        l "Hey, don't sell yourself or this date short!"
        l "So far I'm having a really good time [name]."
        l "Anyway, to answer your question..."

    elif cafe_badLove_justafeeling == True:
        l "Ah I see, are you sure you are not a psychic?"
        n "Lilith lets out a cute chuckle before becoming a bit more serious again."
        l "You came pretty close to the truth with that intuition, not entirely though."

    l "I wouldn't say I had really bad experiences with love. It's just that I tend to grow connected with people before they even had the chance to grow fond of me."
    l "I also do not need to be with someone every single moment, both as a friend or lover, once I'm connected I start to sort of withdraw a little bit."
    if cafe_badLove_lowbar == True:
        if persistent.lildeaths > 0:
            l "But it's strange, I feel as if you already know me pretty well even though this is our first date. Not that I'm complaining though, I really like it if I'm being honest with you."
    l "In the beginning I thought that I was weird for acting that way, I started trying to make sure that I didn't distance myself from anyone so I wouldn't hurt them."
    l "Of course this only made things worse, soon I began having almost no confidence in myself and messed up quite a few relationships and friendships."
    l "It took me a while before I managed to find the courage in myself to try and fix my problems."
    l "It didn't happen instantly, even now I sometimes come of as too distant, but little by little I managed to tell myself that there is nothing wrong with not needing an overdose of affection every second."
    l "So, did I have bad experiences in love?"
    l "Maybe, but they were all quite necessary as without them I wouldn't be here with you today, I wouldn't even be myself if that makes sense."
    l "Sorry for blabbering on by the way, I'm quite talkative when you get me going."
    menu:
        "No need to apologise for talking, I like listening to you.":
            l "Oh you flatterer! "
            n "Lilith looks at you and gives you a big grin, you can clearly see she's blushing."
            n "Suddenly the grin begins to make place for a slight frown."
            l "Is it normal for me to be that happy because someone told me they don't mind me speaking?"
            l "..."
            l "I... kind of struggle with self-confidence."
            l "Sometimes I think other people find it a burden to talk to me or be around me at all."
            menu:
                "Quick, come stand next to me!" if persistent.cafe_death_1:
                    jump restaurant_death_1_prevented

                "Well, I really enjoy our time together!":
                    l "Thank you [name], it really helps to hear someone say that from time to time."
                    n "Lilith gives give a thankfull smile."
                    jump restaurant_death_1
