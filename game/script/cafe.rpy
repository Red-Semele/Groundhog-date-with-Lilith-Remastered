#The cafe is one of the shortest paths you can take, perhaps it would be a nice idea to, once all my todo's are taken care of, extend it a bit? Give it some extra options etc.
label cafe_start:
    $ cafe = True
    $ love_meter += 1
    if persistent.cafe_taste_knowledge == True:
        l "Oh my, you sure know how to get me excited! I'll see you there!"
    else:
        l "That sounds good to me. I'll see you there!"
    if persistent.rockMode == False:
        if persistent.cafe_death_1 == False:
            n "You arrive pretty early and are greeted at the entrance by not a single parking spot in view." 
            n "Since you don't exactly have to rush you decide to park a few streets further away and walk to the cafe."
            n "As you finally make it and enter you immediately pick up the lovely atmosphere of the cafe."
            n "The inner wall is lined with aquariums that seem to stretch on even beyond the ceiling, almost resembling an oceanium."
            n "There are some holes in the specially shaped aquarium to allow for easy fish feeding."
            n "It also makes things feel more alive. Colorful fish sometimes poke their head out of the aquarium as if they want to watch the customers."
            n "It's almost as if you are the one in the glass cage and you just don't know it."
            n "It's probably the other way around though. Atleast they are enjoying themselves in their captivity, or they seem to."
        else:
            n "You once again make it to the cafe, the fish poking their heads out of the aquariums almost as if to greet you."
        n "Your eyes fall on [persistent.date], who is already sitting at a nice looking mahogany table."
        n "When [date_sub] [conj('date', 'notices', 'notice')] you [date_sub] [conj('date', 'waves', 'wave')] enthusiastically with a wide grin on [date_pos] face."
        l "Heya, glad you could make it!"
        l "This place has a really nice atmosphere, those aquariums are real eye catchers don't you think?"
        l "Anyway, let's go order our food and then we can talk some more, I'm starving!" #TODO: Should I make you talk to her for a bit before she suggests this?
        n "[persistent.date] and you walk towards the barista, as he glances up from his phone he greets you with a shy smile."
        b "What could I get the both of you?"
        n "He seems quite young, if you'd have to guess you would say he is about 17."
        n "You get lost in the thoughts of your life when you were that young until [persistent.date] gives you a playful nudge."
        l " Hmm, I think I'm going for the ham and cheese sandwich and a cafe cubano."
        l "What are you choosing [persistent.name]?"
        menu:
            "I'll have the same as you.":
                jump cafe_food_choiceSame

            "I'll have the sandwich of the day and an espresso.":
                jump cafe_food_choice1

            "I'll have the beef sandwich and a frappuchino.":
                jump cafe_food_choice2
    else:
        label rockTransport:
            if burger == True:
                $ changeableWord = "burger restaurant"
            elif cafe == True:
                $ changeableWord = "cafe"
            else:
                $ changeableWord = "chinese restaurant"
            #TODO: Polish (like a rock) this text a bit more.
            n "Through excruciating effort you manage to roll off your bed. Now what though? It's not like you can open any doors or windows."
            n "And then suddenly you see it, a very small gap in the corner of the wall. No wonder your room always feels chilly."
            n "Right now though, that hole is a welcome sight, you still take a mental note to plug it up later though."
            n "You roll right through, landing on the sidewalk outside. There you wait until the moment is right."
            n "You aren't sure exactly what you are waiting for, just that it shouldn't take too long."
            n "And then suddenly, you hear someone right in front of you talking to someone on the phone about a date in the [changeableWord]."
            n "You decide to exert all your psychic energy to move a full 5 centimeters to the right."
            n "You perfectly align yourself with the shoe stomping down right on you, using this opportunity to nudge yourself inbetween it."
            n "You can't see anything, but you do feel the sensation of every step."
            n "Suddenly you feel something soft brush against you, and then something plastic that gets pushed in and out."
            n "These sensations feel quite familiar, even if a bit different than how you might experience them normally."
            n "And then it dawns on you, the person you are lifting with is driving their car."
            n "After that it doesn't take long at all for you to feel the pavement brush against you with each step once more."
            if burger == True:
                n "Eventually you make contact with a familiar looking floor. You wriggle yourself free from the shoe."
                n "The familiar walls of the restaurant greet you as you can't help but feel the same sense of comfiness you usually feel, just perhaps a tad more distant."
                n "Suddenly you feel a presence in your mind."
                jump burger_arrived
                
            elif cafe == True:
               
                n "Eventually you make contact with a wooden floor, and a little bit later the walking stops. You use this opportunity to dislodge yourself from between the shoe."
                n "Suddenly you feel a presence in your mind."
                l "Heya [persistent.name]. Glad you could make it!"
                l "And look, it seems we got really lucky, the person I lifted with is here to see your person."
                l "That saves us a lot of rolling around."
                l "This place has a really nice atmosphere, those mahogany tables and the aquariums are real eye catchers don't you think?"
                l "It's a shame it's pretty hard to notice from down here, but atleast the food will be free."
                l "My person already went to grab the food. It should be two beef sandwiches."
                n "Right as [date_sub] [conj('date', 'says', 'say')] that a tiny piece of beef falls right next to you."
                l "Does it smell good?"
            
                jump cafe_foodReplyChoice
            else:
                n "You hear your ride open and close a door, before sitting down. You wriggle your way out of the shoe."
                n "You are surrounded by the busy sounds of the Chineserestaurant, the clattering of dishes, the chattering of people all contrasted by the lovely calming music playing."
                n "Suddenly you feel a presence in your mind."
                jump chinese_arrived
                
        menu cafe_foodReplyChoice:
            "I don't have a nose, I can't smell it.":
                n "That's very correct. However, how are you able to look around with no eyes? To think with no mind?"
                n "All of this is just pure nonsense. This script is giving me a headache."
                n "Perhaps His vision is elevated far above what either of us could comprehend."
                n "{size=*0.5}Or maybe He is just a hack. You are very lucky I'm paid per word I read, otherwise I would not be doing this.{/size}"
                n "Either way, I think it is best to not think too much about it. Ignorance is bliss afterall, isn't it?"
                l "I know silly, but what do you {i}think{/i} it smells like?"
                l "Our imagination is one hell of a tool, isn't it? Then we better put it to good use."
                menu:
                    "What's the point of dreaming about food if neither of us can eat it?":
                        jump restaurant_menu_pointOfPretending
                    "I imagine it smells...":
                        #TODO: Fill this in better.
                        menu:
                            "...sweet.":
                                "filler"
                            "...savory.":
                                "filler"
                            "...spicy.":
                                "filler"
                            "...sour.":
                                "filler"
                            
            "It does, it's just a shame I can't eat it.":
                l "Eat it? Why would we do that? We are rocks, we don't need to eat."
                l "Just watching it is it's own experience, isn't it?"
                l "Sure, it might be a little... different, but it's an experience nontheless, right?"
                #TODO: If the player is streaming or recording the game then add a line kind of referring to the viewers, they too just watch the game while not playing it.
                menu:
                    "What's the point of dreaming about food if neither of us can eat it?":
                            jump restaurant_menu_pointOfPretending

                    "I suppose it's better than not watching it at all.":
                        l "See? Now you are getting it! We are as close to the human experience as we can be right now."
                        l "We are lucky to catch a glimpse of their world, even such a small one."
                        l "Surely you know how isolating our world is, but seeing theirs, even for a moment, makes you almost feel part of it."
                        l "However, a different part of me is even more aware of it not being truly ours."
                        l "That's why I'm so glad we found eachother, you truly exist in my world as I in yours."
                        n "Things turn quiet for a short moment. It's gentle, just the two of you existing together, watching the people around you."
        
        jump cafe_dice_stop

label cafe_food_choice1:
    jump cafe_food_result

label cafe_food_choice2:
    jump cafe_food_result

label cafe_food_choiceSame:
    l "Great minds think alike, I guess that also counts for hungry stomachs."
    n"[persistent.date] lets out a small chuckle."
    jump cafe_food_result

label cafe_food_result:
    b "Alright, coming right up."
    n "Together you walk back to your table and take a seat."
    n "[persistent.date] gives you a somewhat mischievous smile."
    l "I have a fun little game we could try while we wait."
    n "[date_sub!c] eagerly [conj('date', 'digs', 'dig')] into [date_pos] handbag and takes out two red six-sided dice."
    l "It's something I came up with a while ago. I'd like to test it out with you."
    l "So, the rules are simple. {size=*0.5}Actually they might be a little complex...{/size}"
    l "I will first roll two dice and tell you the sum of them. If I roll a double, for example if I roll two four's, an extra one of that number is added. So every double I roll is effectively a tripple."
    l "After that each turn I can take one action. I can change one of the dice's numbers into any number that isn't the number it was the last turn, so a three could become any number except for a three."
    l "But I also can subtract a value from one dice and add it to another, so a five and a one could become two three's by removing two from the five and adding it to the one."
    l "After every action I take I'll tell you the new sum of the dice. I hope that atleast made some sense..."
    l "So, would you like to try the game?"
    menu:
        "Sure, I'm excited to try it out!":
            jump cafe_dice_continue

        "Actually, I'm not sure about this anymore.":
            jump cafe_dice_stop

label cafe_dice_continue:
    l "Great! {size=*0.5}Usually I don't make it this far...{/size}"
    l "Let's see what you are made of [persistent.name]!"
    $ persistent.dice_counter += 1
    n "[persistent.date] rolls the two red dice, obscuring them with [date_pos] hands."
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
    #TODO: Is this actually doable to get to? Try it out for yourself to see if you could deduce it.
    if cafedicecheat == True:
        n "You peek at the dice using the reflection of the aquarium, the first dice is a 6 and the other one a 3."
        $ cafedicecheat = False
    n "[persistent.date] waits for you to look away, then [conj('date', 'takes', 'take')] an action."
    l "The sum of the dice is still nine."
    n "[date_sub!c] [conj('date', 'performs', 'perform')] [date_pos] next action."
    l "The sum just changed to eight."
    n "[persistent.date] hums an unfamiliar song as [date_sub] [conj('date', 'takes', 'take')] [date_pos] next action, it's quite catchy."
    $ persistent.song_knowledge = True
    l "The final sum is five."
    l "That was the puzzle. You'll need one hint to solve it."
    l "The last thing I did was changing the second dice."
    l "I hope that hint is helpful!"
    l "So, what was the number of the first dice on the first turn?"
    label cafe_dice_choice:
        $ dicenumber = player_input("Place your guess here", length=5)
        $ dicenumber = dicenumber.strip()

        if not dicenumber:
            $ dicenumber = "4"

        $ dicelength = len(dicenumber)

        if dicelength == 1:
            python:
                try:
                    dicenumber = int(dicenumber)
                except ValueError:
                    renpy.say(n, "...Not sure what you're trying to achieve with that. Please enter a number this time and let us just pretend it never happened.")
                    renpy.jump("cafe_dice_choice")
            if dicenumber > 6:
                n "Let's try that again, [date_sub] [conj('date', 'is', 'are')] using six-sided dice, remember? So you can only choose a number from 1-6."
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
                        l "Nope that's- wait you figured it out?... Nicely done [persistent.name]!"
                        l "Here I was thinking this puzzle would be too hard but you handled it like a champ!"
                        l "I'm actually very impressed."
                        if persistent.lildeaths >= 1: 
                            if persistent.dice_knowledge == False:
                                n "I'm quite impressed aswell player, you haven't done this before, have you? You are quite the natural."
                        l "I love puzzles that really put your brain to good use so it's always fun to see someone else who feels the same."
                        l "Anyway, enough about me, let's move on to another question for you, what do you think about this place?"
                        $ persistent.dice_knowledge = True
                        jump cafe_rateCafe
                else:
                    label cafe_dice_wrong:
                        l "Nope, that's not the answer."
                        l "You gave it your best shot [persistent.name]! {size=*0.5}I might have made this a bit too hard.{/size}"
                        l "Would you like to know the answer?"
                        menu:
                            "Yeah, please tell me what the answer was.":
                                $ persistent.dice_knowledge = True
                                l "Sure thing [persistent.name], I won't keep up the suspense any longer."
                                l "The first dice was 6 and the second dice was 3."
                                l "That was quite tricky wasn't it? I hope it was fun for you though!"
                                n "[persistent.date] gives you a cute smile."
                                l "Oh, I almost forgot to ask you! What do you think about this place?"
                                jump cafe_rateCafe

                            "No, if I ever learn the answer it will be because I solved it.":
                                l "That's nothing if not commendable [persistent.name]! I'm just not sure when you'll get your next chance..."
                                if persistent.dice_counter >= 2:
                                    n "Oh I think [date_sub] [conj('date', 'does', 'do')]n't have to worry about that at all..."
                                    n "After all, isn't this the [persistent.dice_counter] time you try this puzzle?"
                                    if persistent.dice_knowledge == True:
                                        n "However, peculiarly enough you already know the correct answer, right?"
                                        n "I even gave you a reminder about it and yet you got it wrong, why is that?"
                                        n "Is it because you want to see these lines of new dialogue?"
                                        $ intentional_fail_count = narrator_dialogue_state_inc("cafe.dice.intentional_fail.count", 1)
                                        if narrator_dialogue_seen("cafe.dice.intentional_fail.rant"):
                                            n "No that can't be the case, after all there is no new dialogue now that you returned once again to do the same thing."
                                            n "So there must be a different reason, right?"
                                            n "Although I suppose, what I am saying now could be considered extra dialogue."
                                            n "Alright that's it, I'm not giving you anymore extra dialogue here, and I'm not changing my dialogue either, it will always be just this."
                                            n "By the way, you intentionally failed this puzzle [intentional_fail_count] times now."
                                        else:
                                            $ narrator_dialogue_mark_seen("cafe.dice.intentional_fail.rant")
                                
                                l "Anyway, I've been meaning to ask you something."
                                l "What do you think about this place?"
                                jump cafe_rateCafe

            "No, that's not right.":
                l "Oh,so what number do you think it is then [persistent.name]?"
                $ dicenumber2 = player_input("Place your guess here", length=5)
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
    if not persistent.rockMode:
        #TODO: EXTRA: This could be a good place to add something else, instead of just segwaying she offers another game of sorts.
        l "Oh no worries [persistent.name]! It might come off as a little daunting so I completely understand."
    else: 
        l "I was going to ask you to try out a little dice game I came up with."
        l "But as you are well aware I have no pockets to store them in, nor hands to roll them with."
    l "We can just continue talking if you'd like to."
    l "After all, we are hopefully not running out of topics already."
    n "[persistent.date] lets out a cute chuckle."
    l "Don't stress it [persistent.name], it's alright if you can't think of anything for a moment."
    l "I completely get it, to be honest I'm quite stressed about this date too."
    l "Well... maybe stressed is not the right word. Moreso excited?"
    l "Let's just see where things go and enjoy ourselves."
    l "I've been meaning to ask you, what do you think of the cafe now that you've seen it for the first time?"
    jump cafe_rateCafe
    
label cafe_rateCafe:
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
    n "[persistent.date] pauses, seemingly not knowing what to say."
    menu:
        "Maybe you just misheard me.":
            jump cafe_backOnTrack

label cafe_backOnTrack:
    n "[persistent.date] lets out a polite and also confused chuckle."
    l "That's probably right, my bad then."
    n "For a moment there's a slightly awkward silence."
    l "So uhm- anyway, would you like to hear a joke?"
    n "You nod, thankfull for the icebreaker to get this conversation back on track."
    l "Perfect, here it comes!"
    jump cafe_abigailJoke

label cafe_rateCafe_great:
    n "[persistent.date] let's out a small giggle."
    if not persistent.rockMode:
        l "I knew you would love it as much as me when I saw your smile."
        #TODO: For the other ones have lilith be slightly confused, as your player character still was smiling while you said somethin else.
    else:
        l "I feel the same way, this place just simply {b}rocks{/b}."
    l "I've never seen so many colors at the same time, thank you for taking me here [persistent.name]!"
    if love_meter >= 3:
        l "Just the fish on their own made this one of the best dates I ever had and the company isn't half bad either."
        n "[persistent.date] blushes slightly, [date_sub] [conj('date', 'looks', 'look')] down at [date_pos] hands for a moment before looking back up at you."
    else:
        l "Just the fish on their own made this one of the best dates I ever had, it can only get better from here."
    $ persistent.cafe_taste_knowledge = True
    jump cafe_rateCafe_result

label cafe_rateCafe_okayish:
    if persistent.rockMode == False:
        n "[persistent.date] flashes you an understanding smile."
    else:
        n "You feel a gentle wave of understanding wash over you, it feels strange for only a second, then it feels almost comfortable."
    l "Sorry to hear that [persistent.name]. For what it's worth I am really enjoying it here."
    l "Maybe we can go to a place you like next time? I've never seen so many colors at the same time, thank you for taking me here [persistent.name]."
    l "So far this is one of the best dates I ever had!"
    $ persistent.cafe_taste_knowledge = True
    jump cafe_rateCafe_result

label cafe_rateCafe_bad:
    $ love_points = -1
    $ love_meter_updater(False)
    n "[persistent.date] frowns at your reaction."
    l "...There's no need to drag this place down just because you don't like it."
    n "Things fall silent for a moment. It feels as if entire minutes are going by with neither of you saying a thing."
    l "[persistent.date] takes [date_pos] phone and begins aimlessly scrolling on it, you can see [date_pos] screen through the reflection on the aquarium.
    [date_sub!c] [conj('date', 'is', 'are')] growing less and less responsive after every word you say until the two of you sit in pure silence for what feels like an hour."
    if persistent.need_pass_knowledge == True and not persistent.rockMode:
        n "Atleast you also managed to glimpse [date_pos] password thanks to the reflection, it's 81155."
        $ persistent.pass_knowledge = True
    jump restaurant_death_1

label cafe_rateCafe_result:
    menu:
        
        "Sorry to ask you this, but did you have bad experiences in love?":
            l "That's quite an unusual question [persistent.name], what makes you think I did?"
            #Maybe rephrase it slightly, comes of as a bit defensive.
            menu:
                "You said this was one of your best dates. It seems as if the bar wasn't exactly high.":
                    $ cafe_badLove_lowbar = True
                    jump cafe_badLove
                "I'm not sure, honestly it was just a gut feeling.":
                    $ cafe_badLove_justafeeling = True
                    jump cafe_badLove
                    #TODO:Make her mention something about this during the pshycic route?

        #TODO: I'm fairly certain this reply doesn't always make sense depending on what you say about the cafe. Check that and if not write some alternate lines.
        "You are very welcome, thank you for making me come here in the first place.":
            l "Did you just counter my thank you with another thank you?"
            l "Well, in that case I'll retaliate with a \"You are very welcome.\" aswell!"
            l "[persistent.date] let's out a cute giggle. [date_sub!c] [conj('date', 'has', 'have')] a gleeful look in [date_pos] eyes."
            l "You know, you gave me quite a laugh there [persistent.name], now it's my turn! Would you like to hear a joke?"
            menu:
                "Sure, I'd love to.":
                    jump cafe_abigailJoke

label cafe_abigailJoke:
    l "So a priest, a monk and a rabbit enter a bar."
    l "Says the rabbit: \"Whoops, did you slip your tongue there [persistent.date]?\""
    $ persistent.joke_knowledge = True
    menu:
        "Wow, that was a really good one!":
            jump cafe_joke_good

        "That was not funny at all.":
            jump cafe_joke_bad

        "I'm not sure I get the joke...":
            jump cafe_joke_dontGet

label cafe_joke_bad:
    $ love_points = -1
    $ love_meter_updater(False)
    n "[persistent.date] looks saddened by your remark."

    l "Really? ..."
    if persistent.rockMode == False:
        l "I thought it was funny when [persistent.date_sis] told me..."
    else:
        l "I found it pretty funny. Although... I'm not sure where I heard it from."
        l "It's almost as if I always knew, like I was born with it... that probably doesn't make much sense though, does it?"
    menu:
        "Quick, come stand next to me!" if persistent.cafe_death_1 and not persistent.rockMode:
            jump restaurant_death_1_prevented
        "Well...":
            jump restaurant_death_1

label cafe_joke_good:
    n "[persistent.date] explodes in laughter."
    if persistent.rockMode == False:
        l "Exactly! The first time [persistent.date_sis], my [sis_sib], told me that joke I must've laughed for at least an hour."
        l "Then again, [sis_sub] always [conj('sis', 'makes', 'make')] me laugh so much. I swear that I just might pass out one time."
        l "I'm kidding, I'm kidding! About the passing out part that is, [sis_sub] really [conj('sis', 'is', 'are')] funny though."
    else:
        l "Exactly! The first time I heard that joke I must have laughed for at least an hour."
        l "Although... it's strange, I do not remember where I heard that joke, just that I did."
        l "..."
    menu:
        "Quick, come stand next to me!" if persistent.cafe_death_1 and not persistent.rockMode:
            jump restaurant_death_1_prevented

        "[sis_sub!c] [conj('sis', 'sounds', 'sound')] nice." if not persistent.rockMode:
            jump restaurant_death_1

        "That indeed is strange." if persistent.rockMode:
            jump restaurant_death_1

label cafe_joke_dontGet:
    l "Oh, the point of the joke is that the other two who entered the bar where religious fiures, the monk and the priest.
    So the rabbit doesn't quite fit in, it's because he was actually a rabbi instead."
    l "So I mispronounced that hence the \"did you slip your tongue?\"."
    l "Is the joke now funnier or did it now become less funny? It tends to be that way when you explain a joke so I'm sorry if I ruined it for you."
    menu:
        "Quick, come stand next to me!" if persistent.cafe_death_1 and not persistent.rockMode:
            jump restaurant_death_1_prevented

        "No need to apoligize, I made you explain it. Besides, it's still pretty funny now that I understand the joke.":
            jump restaurant_death_1

label cafe_badLove:
    if cafe_badLove_lowbar == True:
        l "Hey, don't sell yourself or this date short!"
        l "So far I'm having a really good time [persistent.name]."
        l "Anyway, to answer your question..."

    elif cafe_badLove_justafeeling == True:
        if persistent.rockMode == False:
            l "Ah I see, are you sure you are not a psychic?"
        else:
            l "Are you sure you are not taking a peek at my thoughts?"
        n "[persistent.date] lets out a cute chuckle before becoming a bit more serious again."
        l "You came pretty close to the truth with that intuition, not entirely though."
    if persistent.rockMode == False: 
        l "I wouldn't say I necessarily had bad experiences with love. It's just that I tend to grow connected with people before they even had the chance to grow fond of me."
        l "I also do not need to be with someone every single moment, both as a friend or lover, once I'm connected I start to sort of withdraw a little bit."
        if cafe_badLove_lowbar == True:
            if persistent.lildeaths > 0:
                l "Maybe you are the same? It strangely enough feels like you are pretty familiar with me even though this is our first date."
                l "I'm not complaining though, if I am being honest this is actually really nice."
        l "I used to think I was weird for acting that way. I tried to be closer to others so I wouldn't make them feel as if I didn't care about them."
        l "Of course this only made things worse, I began second-guessing every situation and messed up quite a few relationships and friendships."
        l "It took me a while before I managed to find the trust in myself to feel like I didn't owe people my proximity while also being able to compromise with them."
        l "It didn't happen instantly, even now I sometimes struggle with the balance between too clingy and too distant, but I get better at it every day."
        l "So, did I have bad experiences in love?"
        l "Maybe, but without them I wouldn't be here with you today. In a way I wouldn't even be the person you know if that makes sense."
       
    else:
        l "I didn't exactly have much experience with love, let alone a bad one."
        l "I am trapped between two worlds, one of rocks and one of humans. Neither of them is like me."
        l "The first can't hear me psychically and the other one can't hear anything at all."
        l "There are some who can, but psychic rocks like you and me are very few and far between."
        l "However, I guess I did have one experience with love, if I even could call it that."
        l "There was this one rock who called himself \"Flint\"."
        l "I didn't really have any friends or anything that came close."
        l "I suppose I really was living under a {i}rock{/i}."
        n "She lets out a small chuckle in your mind, but it feels anything but humorous."
        l "One day I felt this voice in my mind. It was confident, charismatic. It was Flint."
        l "It turns out he was a travelling rock, trying to find others like them wherever he went."
        l "His travel-stories about the things he saw were just so...- I liked imagining myself in his place, living that life, meeting all those others."
        l "Eventually we started talking more and more, and for the first time in years I began leaving my house again."
        l "We went on adventures all over the country, just exploring to our hearts content."
        l "I felt seen by Flint. For the first time in my life there was someone with who I could do things together."
        l "Eventually... I felt something else. I had been so starved of contact, of attention that I thought I felt love."
        l "In a way it definitely was possible, but with a lot of reflection on my end I now know that I was more in love with the idea of it all than with him. With the idea of being in love."
        l "That need for love, it blinded me to what I already had, a great friendship."
        l "...Eventually I couldn't take it anymore. I tried to fight it for some time, but I ended up confessing my feelings to him."
        l "He... did not reciprocate. At first we agreed to remain friends but things got more and more awkward between the both of us."
        l "It didn't take long for us to grow apart. It's been forever since I last heard from him."
        l "So for my very small exposure to experiences with love I guess my first one indeed wasn't a good. Yet I did learn a lot from it, however cliché that might sound."
        l "I learned to try to see and take things for what they are. There is no use trying to force something that is already good into perfection."
        l "Because the truth is, there is no such thing as perfection, anything resembling it is an illusion."
        l "Even if there was such a thing, we would quickly grow rather bored of it, wouldn't we?"
        l "Once we have forced our perfection upon something, then what do we have to look forward to?"
        l "I'm convinced we need obstacles, everyone does. Without obstacles reaching our goal becomes something that is already done before we started."
        l "We need good enough, so we can grow along with it, watch it get better over time. We do not need the stagnant, forever unchanging perfection."
        l "It's a saying I made for myself. \"Do not confuse the silver moon for the sun just because she reflects it's light.\""
        l "To choose the sun is a pretty sight for a while. But you will find yourself blind to everything else if you stare into it too long."
        l "That's why I am choosing the moon, she reflects the light of perfection, into something more manageable for our minds."
        l "Afterall, we can also find perfection in good enough, just a version that is a lot more manageable. perhaps more fleeting, but that's what makes it beautiful, isn't it?"
        l "For example, right now, I want to take things slow with you, to see where this date will bring us. To get to know you better, the real you."
        l "So did I have a bad experience before? Maybe. But it did help me to hopefully make this a good one."
    l "Sorry for blabbering on by the way, I'm quite talkative when you get me going."
    menu:
        "No need to apologise for talking, I like listening to you.":
            l "Oh you flatterer!"
            if not persistent.rockMode:
                n "[persistent.date] looks at you and gives you a big grin, you can clearly see [date_sub] [conj('date', 'is', 'are')] blushing."
                n "Suddenly the grin begins to make place for a slight frown."
            else:
                n "You feel a gentle wave of warmth wash over you, it feels strange for only a second, then it feels almost comfortable."
                n "Suddenly the warmth begins to make place for a slight chill."

            l "Is it normal for me to be that happy because someone told me they don't mind me speaking?"
            l "..."
            l "I... kind of struggle with self-confidence."
            l "Sometimes I think other people find it a burden to talk to me or be around me at all."
            menu:
                "Quick, come stand next to me!" if persistent.cafe_death_1 and not persistent.rockMode:
                    jump restaurant_death_1_prevented

                "Well, I really enjoy our time together!":
                    l "Thank you [persistent.name], it really helps to hear someone say that from time to time."
                    if not persistent.rockMode:
                        n "[persistent.date] gives you a thankful smile."
                    else:
                        n "You feel just how thankful [persistent.date] is beamed right into your mind."
                    jump restaurant_death_1