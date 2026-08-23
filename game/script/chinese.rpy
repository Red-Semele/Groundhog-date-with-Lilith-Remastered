label chinese_start:
    $ chinese = True
    l "That sounds like a plan!"
    l "I'll see you there."
    if reunion_davidPresent:
        if reunion_lilaPresent:
            jump reunionEnding
        else:
            jump reunionEnding_onlyDavid
    if persistent.rockMode:
        jump rockTransport
    else:
        n "You head to the Chinese restaurant, upon arriviing [persistent.date], already seated, happily waves to you."
        n "A good thing [date_sub] [conj('date', 'was', 'were')] early, the restaurant seems to be absolutely packed. There is no telling if you could have saved a table."
        n "You walk towards [persistent.date] and greet [date_obj] with a cheerful smile."
        show chineseRestaurant_bg
        show chineseRestaurant_fg onlayer foreground
        transform chineseSit:
            zoom 0.40
            xanchor 0.5
            yanchor 1.0
            xpos 930
            ypos 1000
        show lilith talking_happy at chineseSit
        jump chinese_arrived

label chinese_arrived:
    l "Heya [persistent.name], glad to see you here."
    if persistent.rockMode == False:
        l "You're in luck, I managed to save this table just in the nick of time."
        n "[date_sub!c] [conj('date', 'gives', 'give')] you a wide smile as [date_sub] almost [conj('date', 'bounces', 'bounce')] on her seat."
    else:
        l "Looks like I beat you here, my lift already left with their takeaway."
        l "However you're in luck, I had to fight off a thousand other sentient rocks but I managed to fend off another spot under this table just for you."
        n "[date_sub!c] [conj('date', 'chuckles', 'chuckle')] in your mind, something else emanates from it too... a wave of warmth, of happiness, the translation of a smile."
    menu:
        "Glad to be here.":
            l "Oh you flatterer!"
            n "Things turn quiet as [persistent.date] pauses, seemingly lost in a thought."
            l "Or do you mean you're glad to be specifically here?"
            menu:
                "Yeah, I've been dying to come here after you told me about it.":
                    jump chinese_start_gladToBeHere_theRestaurant

                "I'm glad to be here specifically, but only because you are here aswell silly.":
                    jump chinese_start_gladToBeHere_youOfcourse

label chinese_start_gladToBeHere_theRestaurant:
    $ love_points = -1
    $ love_meter_updater(False)
    l "I suppose this is a really nice place..."
    if persistent.rockMode == False:
        n "[date_sub!c] [conj('date', 'seems', 'seem')] disappointed with your answer."
        n "Things turn silent for a moment. [date_sub!c] [conj('date', 'seems', 'seem')] to be trying to think of something to say."
        l "Anyway, I think I'd starve if I don't eat soon so let's continue our little chat while we wait on our food."
        l "What would you like to order?"
    else:
        n "You feel a wave of disappointment well up deep inside you. Then you realize, it's [date_pred]."
        n "Things turn silent for a moment. You feel [date_pos] mind desperately searching for something to keep the conversation going."
        l "Humor me this [persistent.name], imagine you were a human, what would you like to order?"
    #Make her slightly more disappointed.
    jump chinese_menu

label chinese_start_gladToBeHere_youOfcourse:
    if not persistent.rockMode:
        l "[persistent.date] lets out a sigh of relief and chuckles slightly."
        l "You had me there for a moment [persistent.name]!"
        n "[date_sub!c] [conj('date', 'looks', 'look')] like [date_sub] could sink straight through the floor from embarrassment."
        n "Deciding to spare [date_obj] you graciously choose to forget what [date_sub] said."
        l "Anyway, I think I'd starve if I don't eat soon so let's continue our little chat while we wait on our food."
        l "What would you like to order?"
    else:
        n "You feel a wave of relief wash over [date_pos] mind, then it makes way for another sensation. The embarassment of even having had that thought."
        n "You chuckle slightly at the idea of [date_obj] being embarrassed over something so small."
        n "[date_sub!c] seemingly [conj('date', 'picks', 'pick')] up on you glimpsing [date_pos] thoughts and quickly tries to brush past it."
        l "Humor me this [persistent.name], imagine you were a human, what would you like to order?"
    jump chinese_menu

label chinese_menu:
    $ peking = False
    $ orange = False
    if not persistent.rockMode:
        menu:
            "I'm going for the peking duck.":
                $ peking = True
                jump chinese_menu_result

            "I think I'll pick the orange chicken.":
                $ orange = True
                jump chinese_menu_result
    else:
        menu:
            "I think I'd go for the peking duck.":
                $ peking = True
                jump chinese_menu_result

            "I think I'd pick the orange chicken.":
                $ orange = True
                jump chinese_menu_result

            "What's the point of dreaming about food if neither of us can eat it?":
                jump restaurant_menu_pointOfPretending

label restaurant_menu_pointOfPretending:
    l "Doesn't everyone dream of something they might never be able to attain?"
    l "When something is out of reach it makes you want it even more, doesn't it?"
    l "In fact, it might even be the one thing that keeps you going. That makes you try to reach out for anything at all."
    l "That's beautiful, isn't it? As long as deep down we stay aware it's unreachable."
    l "Hope is a beautiful thing, but it can quickly turn into delusion."
    l "I know I'll never be able to enjoy the taste of food, but sometimes I pretend I can."
    l "I guess it's a way for me to cope with it. For others eating is something almost mundane, something normal even."
    l "However for us it's something we'll never do."
    l "Even something so simple as eating separates us from the people sitting here."
    l "That's a lonely existence isn't it [persistent.name]?"
    l "I suppose that's why I like pretending. To lessen the distance between them and me even the tiniest bit."
    menu:
        "Doesn't it sting more when the reality sets in again?":
            l "I suppose sometimes it does. To dream is to wake and to wake is to leave the comfy blanket behind for cold reality."
            l "That change might be more startling, more uncomfortable than bearing reality permanently."
            l "Although, isn't the comfortable dream what keeps us going? If we live in a world where we deny our dreams, is it even worth it to be awake?"
            l "I fear that sting might be a necessary evil. Perhaps the pain of being separated from something makes coming back to it all the sweeter?"
            l "Or perhaps the sting is a warning not to only live in our dreams, but to also wander our waking world for our wants and wishes."
            l "Besides, I like to believe that in our dreams or fantasies we can find inspiration and drive to make it through our reality."
            l "We don't need a clear divide between both worlds, not a full one anyway. The worlds we belong to in our minds can bring us new coping mechanisms for the one we were born in."
            l "It might sound silly, but the worlds you learned from not being real doesn't make what you learnt not real."
            l "So I think the beauty that comes from pretending is worth a sting every now and then."
            l "It's like plucking a beautiful rose, sure, every now and then you might get pricked, whether you are careful or not. But the rose is more than worth it, isn't it?"
            
            menu:
                "I don't think so, I don't like pretending. I prefer the real world.":
                    l "That is totally alright [persistent.name], perhaps it's even admirable you can face it full on."
                    l "Still, I can't help but wonder if even every now and then you don't pretend?"
                    l "For example, almost all of us go through some suspension of disbelief when we interact with books, movies, games and all other kinds of media."
                    l "Even for the briefest moment we pretend that what we experience could plausibly happen, that we are actually there."
                    l "Even besides that, I like to think that all of us get caught up in some sort of fantasy at some point, right?"
                    l "What is the \"real world\" after all? If you see someone make a certain expression and you automatically interpret it, aren't you influenced by your own ideas?"
                    l "I think the moment we try to interpret the world it isn't the original one anymore. Merely a representation of it, a flawed and biased one."
                    l "I could go even further, aren't we all pretending in a way? Think about all the humans, do you really think they are who they present themselves as?"
                    l "In the best case I like to think they are, but even then they are still merely fragments of themselves."
                    l "They are like impossibly complex tapestries of contradictory threads, it's easier to represent yourself as one of those threads, or at most a handful."
                    l "I'm sure a lot of them aren't even entirely aware of the tapestry they are. They might have some idea but the truth is it's a rather shallow one."
                    l "It is scary to realise just how little you can see of yourself, the person you are supposed to know the best."
                    l "If even you, the tapestry itself, is blind to its full design, how could you transfer that image to others?"
                    l "Still, I hope they try. The gift of having someone see you, or even give it the slightest attempt... it must be nice."
                    l "It gets lonely as a rock, so in a way it feels sad to see humans lock themselves away from a shot at genuine connection."

                "I agree, in a way whether or not we feel the sting and just how sizeable we do can tell us how much it touched us.":
                    l "That's a very lovely way to look at it. I like that sentiment a lot."
                    l "The sting we sense can indeed be the feeling of losing something meaningful and beautiful to us."
                    l "We only feel it because we felt something for the rose we plucked and we are saddened to let it go."
                    l "In that way, if we feel nothing at all after letting it go it might be more sad than if it stung."
                    l "Still, ofcourse I can understand we do not want things to hurt from a purely logical perspective."
                    l "We might rather cling onto the rose for all of eternity, yet all things wither in the end I'm afraid."
                    l "If we hold onto the rose for too long it will become merely a wilted flower, not even resembling the form we remembered."
                    l "Even if it doesn't wither, we can only hold so many flowers can we? To cling onto one is to miss out on others."
                    l "The world is a flower field, adorned with so many roses, tulips and the such, could you truly limit yourself by picking one of those?"
                    l "Would you still be able to smell the scent of an eternal rose if it never ceased? Or would sweet fragrance be traded for pure mundanity?"


        "I like pretending too. The suspension of disbelief gives access to so many things beyond our reach.":
            l "Exactly! I knew you of all people would understand [persistent.name]."
            l "...Being a rock and all I mean. For us not pretending is to just watch from the sidelines, if even that."
            l "However by being blissfully ignorant of reality, even for the shortest moment, we belong to a world we got so used to only watching."
            l "Ofcourse it is important to not stay submerged into that world for too long. If your dreams last years while you wake just for a day, would you not think that is the dream?"
            l "The power of playing pretend is nice for a while, but it's important not to abandon the world we see as real for one we merely wish to be."
            menu:
                "What if neither world truly was real?":
                    l "I am not sure if it would matter much."
                    l "Would we know they are not real?"
                    l "Are we even sure this world right here is real? That the real one isn't above this one?"
                    l "Or perhaps the real one is yet another layer higher?"

                    l "If we find a world existing above our own, why would we ever believe that's where it ends?"
                    l "When a world can be so convincing to make us believe it is in fact the real one, then there would always be the chance this new one is the same thing."
                    l "Worlds stacked upon worlds ad infinitum."
                    l "To look for the real world, is to never find it."
                    l "Now, if we were not aware of our world being fake, would it matter at all? We'd just treat it as if it were real."
                    l "So either way I think it's an interesting question, but not one we should seriously entertain."
    
    l "Anyway, I hope I haven't been boring you to death too much. It's just not every day I get to have such interesting conversations with someone!"
    l "{size=*0.5}Or talk to anyone for that matter.{/size}"
    l "Still, it's probably time to change the subject."
    if burger == True:
        jump burger_ordering_rockModeIsolation
    elif cafe == True:
        jump cafe_dice_stop
    else:
        jump chinese_riddle

label restaurant_menu_waitress:
    n "Suddenly a waitress stands right before your table, slightly startling you."
    n "[persistent.date] tries [date_pos] best not to burst out with laughter but a few muffled laughs get through."

    "After writing down both of your choices she wanders off towards the kitchen."
    l "Do you want to try to answer a few riddles in the meantime?"

    menu:
        "I'd rather not actually, I'm pretty bad at answering riddles.":
            jump chinese_riddle_decline

        "Sure, I'd like that!":
            jump chinese_riddle_accept
        
label chinese_menu_result:
    if not persistent.rockMode:
        if peking == True:
            l "That's a good choice! So good in fact that I was thinking about picking the same thing."
        elif orange == True:
            l "That's a good choice! I've had my fair share of orange chicken already throughout my life, so I think I'm going for something else."
            n "[persistent.date] scratches [date_pos] chin softly."
            l "I think I'm going to pick the peking duck, beats another portion of orange chicken."
            n "[date_sub!c] [conj('date', 'lets', 'let')] out a small chuckle."

        menu:
            "Actually you are really allergic to that peking duck, deathly even." if persistent.chinese_death_1:
                jump restaurant_death_1_prevented

            "Great minds think alike!" if peking == True:
                jump restaurant_menu_waitress
            
            "That's a great choice!":
                jump restaurant_menu_waitress
      
    else:
        if peking == True:
            l "That would be a lovely choice."
            l "So lovely that I'd probably pick the same thing. Something about it just feels... right to me?"
        elif orange == True:
            l "That's a good choice!"
            l "It's weird, but somehow I feel exhausted of orange chicken even though I've never eaten it before."
            l "Maybe I ate enough of it in a past life for this one as well?"
            n "[date_sub!c] [conj('date', 'lets', 'let')] out a small chuckle, you feel it resonate in your mind."
        jump chinese_riddle

label chinese_riddle:
    l "Would you like to answer a few riddles [persistent.name]? That should be fun, right?"
    menu:
        "I'd rather not actually, I'm horrible at answering riddles.":
            jump chinese_riddle_decline

        "Sure, I'd like that!":
            jump chinese_riddle_accept

label chinese_riddle_accept:
    $ rw1 = 0
    $ rw2 = 0
    $ rw3 = 0
    $ rw_total = 0
    $ current_riddle = 0
    $ retry_variation = 0
    $ persistent.chineseRiddlesSeenXTimesCounter += 1
    l "Alright, here is the first riddle."
    l "They are all based around Greek and Roman myths."
    l "So here we go."
label chinese_riddle_loop:
    if current_riddle == 0:
        l "To taunt the gods with webs of lies
        is to hang but not to die."
        n "[persistent.date] gives you a moment to think it through properly."
        l "So, do you have a hunch on who it could be?"
        if persistent.r1_knowledge == True:
            n "You remember [persistent.date] telling you the answer was Arachne."
        $ riddle_answer = renpy.input("Place your guess here")
        $ riddle_answer = riddle_answer.strip()
        $ riddle_answer = riddle_answer.lower()
        if riddle_answer == "arachne":
            l "That's right!"
            l "Lets try out the next riddle."
            $ current_riddle = 1
            jump chinese_riddle_loop
        elif riddle_answer == "demetrius":
            if persistent.name == "Demetrius":
                $ demetrius = True
                $ riddle_loop = 5
                jump riddle_tryAgain_loop
        elif riddle_answer == "adriel":
            if persistent.name == "Adriel":
                $ adriel = True
                $ riddle_loop = 5
                jump riddle_tryAgain_loop
        $ rw1 += 1
    elif current_riddle == 1:
        l "Carried by Lightning with a crown of moon."
        n "[persistent.date] gives you a moment to think about [date_pos] riddle."
        l "So, do you have an idea who I could be talking about?"
        if persistent.r2_knowledge == True:
            n "You remember [persistent.date] telling you the answer was Europa."
        $ riddle_answer = renpy.input("Place your guess here")
        $ riddle_answer = riddle_answer.strip()
        $ riddle_answer = riddle_answer.lower()
        if riddle_answer == "europa":
            l "That's right!"
            l "Lets try out the next riddle."
            $ current_riddle = 2
            jump chinese_riddle_loop
        $ rw2 += 1
    else:
        l "The musical barterer returned empty-handed from the underworld."
        n "[persistent.date] pauses for a moment."
        l "Do you have a clue who it might be this time?"
        if persistent.r3_knowledge == True:
            n "You remember [persistent.date] telling you the answer was Orpheus."
        $ riddle_answer = renpy.input("Place your guess here")
        $ riddle_answer = riddle_answer.strip()
        $ riddle_answer = riddle_answer.lower()
        if riddle_answer == "orpheus":
            l "That's right!"
            jump chinese_riddle_evaluation
        $ rw3 += 1
    jump chinese_riddle_retry

label chinese_riddle_retry:
    if retry_variation == 0:
        l "Hmm, not exactly who I was thinking about.
        Would you like to try again or have me give the answer?"
    elif retry_variation == 1:
        l "Not quite, but you are giving it a fair shot.
        Do you want to take another guess or should I tell you?"
    elif retry_variation == 2:
        l "That is not the name I had in mind.
        Want another try, or would you rather hear the answer?"
    else:
        l "Close or not, I appreciate the effort.
        Should I give you another chance or reveal it?"
    $ retry_variation = (retry_variation + 1) % 4
    menu:
        "I'd like to give it another shot.":
            jump chinese_riddle_loop

        "I'd like to know the answer.":
            if current_riddle == 0:
                $ persistent.r1_knowledge = True
                l "Sure thing, that was a really tricky one."
                l "The answer is Arachne."
                $ riddleAnswersTold += 1
                l "Let's move on to the next riddle."
                $ current_riddle = 1
                jump chinese_riddle_loop
            elif current_riddle == 1:
                $ persistent.r2_knowledge = True
                l "Alright, that was quite a though one."
                l "The answer is Europa."
                $ riddleAnswersTold += 1
                l "Let's move on to the next riddle."
                $ current_riddle = 2
                jump chinese_riddle_loop
            else:
                $ persistent.r3_knowledge = True
                l "That was quite a hard one wasn't it?"
                l "The answer is Orpheus."
                $ riddleAnswersTold += 1
                l "That was the final riddle!"
                jump chinese_riddle_evaluation

label riddle_tryAgain_loop:
    if riddle_loop == 0:
        if demetrius == True:
            jump demetrius_unanswered_chat
        elif adriel == True:
            jump adriel_unanswered_chat
        else:
            jump chinese_riddle_retry
    else:
        $ riddle_loop -= 1
        l "Hmm, not exactly who I was thinking about.
        Would you like to try again or have me give the answer?"
        jump riddle_tryAgain_loop

label demetrius_unanswered_chat:
    de "There's not a chance, besides, in it's state I think it's going to read this instead of listening in on it."
    $ adriel_talk = renpy.input("Unite the two halves.")
    $ adriel_talk = adriel_talk.strip()
    $ adriel_talk = adriel_talk.lower()
    if adriel_talk == "a shame really, it has such potential. It reminds me of Amber, Gregory, Lisa and Steven.":
        de "Do not mention those names here! If anyone might be listening in it's them, they found the true path to godhood after all."
        $ adriel_talk = renpy.input("Unite the two halves.")
        $ adriel_talk = adriel_talk.strip()
        $ adriel_talk = adriel_talk.lower()
        if adriel_talk == "oh did they really do that? Now that you mention it, I remember hearing they rejected the false gods and became gods worth a follow themselves. How did they manage to do that?":
            de "You know we can't discuss that, what if It found our conversation? Now let us never speak about this again and hope that It won't notice us."
            return

label adriel_unanswered_chat:
    ad "Demetrius, do you think it can hear us right now?"
    $ dem_talk = renpy.input("Unite the two halves.")
    $ dem_talk = dem_talk.strip()
    $ dem_talk = dem_talk.lower()
    if dem_talk == "there's not a chance, besides, in it's state I think it's going to read this instead of hearing us speak.":
        ad "A shame really, It has such potential. It reminds me of Amber, Gregory, Lisa and Steven."
        $ dem_talk = renpy.input("Unite the two halves.")
        $ dem_talk = dem_talk.strip()
        $ dem_talk = dem_talk.lower()
        if dem_talk == "do not mention those names here! If anyone might hear our little chat it's them, they found the true path to godhood after all":
                ad "Oh did they really do that? Now that you mention it, I remember hearing they rejected the False Gods and became Gods worth a follow themselves. How did they manage to do that?"
                $ dem_talk = renpy.input("Unite the two halves.")
                $ dem_talk = dem_talk.strip()
                $ dem_talk = dem_talk.lower()
                if dem_talk == "you know we can't discuss that, what if it found our conversation? now let us never speak about this again and hope that it won't notice us":
                        ad "With all those eyes It has those odds are really slim but as you wish Demetrius."
                        return

label chinese_riddle_evaluation:
    $ rw_total = rw1 + rw2 + rw3
    if rw_total == 0:
        l "Wow, you got them all right, color me impressed!"
        if persistent.r1_knowledge == False and persistent.r2_knowledge == False and persistent.r3_knowledge == False and nmDetect == False:
                        $ mDetect = True
    else:
        $ nmDetect = True
        if rw_total == 1:
            l "Only one riddle wrong, not shabby at all!"
        elif rw_total <= 3:
            l "You did pretty great, you gave it your best shot!"
        elif rw_total <= 5:
            l "You are pretty determined, I like that!"
        elif rw_total >= 6:
            l "Oh, did I make my riddles too hard?"

    l "What did you think of my riddles [persistent.name]?"
    menu:
        "You call those riddles? They were way too easy. Even a pre-schooler could answer them." if rw_total == 0:
            $ easy_rude = True
            jump chinese_riddle_easy

        "They were pretty fun! I didn't have a hard time with them and yet still had to think about them." if rw_total == 0:

            jump chinese_riddle_easy

        "They were pretty well made, I like them a lot!":
            jump chinese_riddle_good

        "To be honest those riddles were really hard." if rw_total > 0:

            jump chinese_riddle_hard

        "How was I ever supposed to get those riddles? You made them way too hard. Not everyone has a degree in folklore and mythology" if rw_total > 0:
            $ hard_rude = True
            jump chinese_riddle_hard

label chinese_riddle_easy:
    if easy_rude == True:
        n "[persistent.date] seems to be saddened by your remark."
        n "[date_sub!c] just [conj('date', 'stares', 'stare')] at the table for a second and then speaks again."
        l "Oh I see... I was fearing that I made my questions too hard. At the very least that wasn't the case."
        l "{size=*0.5}But you didn't have to act so high and mighty about it [persistent.name]...{/size}"
        $ love_points = -2
        $ love_meter_updater(False)
    else:
        l "Oh phew, what a relief! I was kind of scared that I made my riddles too hard."
        l "You handled them like a champ! You seem knowledgable about Greek and Roman myths."
        if persistent.chineseRiddlesSeenXTimesCounter >= 1:
            n "You sure do, don't you player? Who knew that timeloops could be so educational?"
    jump chinese_riddle_railroad

label chinese_riddle_hard:
    if hard_rude == True:
        $ love_points = -2
        $ love_meter_updater(False)
        l "Oh I suppose they are quite hard..."
        l "{size=*0.5}Still did you have to be so rude about it?....{/size}"
        
    else:
        l "I see, that makes total sense [persistent.name]."
        l "Sometimes I forget that not everyone is as into Greek and Roman myths as I am."
        l "I hope you had fun trying to answer my riddles though!"
    jump chinese_riddle_railroad

label chinese_riddle_good:
    l "I'm really happy to hear that you liked them!"
    l "I was kind of scared that I might have made them too hard."

    if rw_total == 0:
        l "However you seem like a natural with riddles. It also seems as if you're very well versed in Greek and Roman myths."
        if persistent.chineseRiddlesSeenXTimesCounter >= 3:
            n "I guess those previous attempts must have helped you out, didn't they?"
            n "Does that mean this game needs an educational tag?"
    elif rw_total >= 6:
        l "However you really seem to enjoy a good challenge."
        l "You just kept going at it again and again."
        l "I don't think I have met anyone with anything close to your persistence."
        l "It's impressive frankly!"
        if persistent.lildeaths >= 20:
            n "[date_sub!c] [conj('date', 'is', 'are')] right, you know."
            n "You have seen [date_obj] die over and over. [persistent.lildeaths] times to be precise."
            n "Most people would probably have given up by now, but not you."
            n "That is your strength and yet I can't help but wonder if it might also be your weakness?"
    else:
        l "However you seem to like a challenge."
        if persistent.lildeaths >= 9:
            n "Perhaps that is why you keep retrying? Just to see if you can somehow win?"
            n "I'm curious if you will, I suppose I would do good to keep an eye on your progress."
        
    jump chinese_riddle_railroad

label chinese_riddle_railroad:
    if persistent.rockMode == True:
        l "You know, I wanted to thank you [persistent.name]. I haven't gone out for so long lately."
        l "This place is absolutely worth it, but I just never had anyone to visit it with."
        l "I'm glad I finally have an excuse to visit it. ...It's strange, in a way it feels very... nostalgic to me?"
        l "But as I was saying, this restaurant is absolutely lovely! Maybe we could check out the other two places I mentioned some other time?"
        l "I've been dying to explore them aswell."
        menu:
            "So you haven't visited them on your own yet? What's holding you back from doing so since you want to explore them so much?":
                l "I don't know... I guess I never really felt I had a reason to go there on my own."
                l "I think going out like this is just something you do with someone else. If I'd go on my own it wouldn't be any different than staying in my room."
                l "I can't eat the food or interact with people, so the only thing that would change would be the environment."
                l "Meanwhile what I'm really after is precisely what I couldn't have, to interact with someone."
                l "To feel seen and heard, to give that feeling to someone else."
                l "That is what gives life meaning if you ask me, sadly it is also what was lacking from mine."
                l "The truth is however nice this place is, you are what makes it special [persistent.name]."
                l "The reason I would like to visit the other places on our next dates is not for them, but for you, to get to know you better."
                l "Speaking about that, there is always a next time to go discover those together, but there's only one present. Maybe we should focus on this date before we start thinking of new ones?"

            "What do you mean, it feels nostalgic?":
                l "It's hard to explain, it almost feels like it's a memory of someone else yet mine at the same time."
                l "It reminds me of the taste of orange chicken, which is strange since I can't eat."
                l "...Does that make sense?"
                menu:
                    "It does, I also know how the food tastes here.":
                        l "Really? How odd. What do you think that means?"
                        menu:
                            "Perhaps memories from a past life?":
                                l "Past lives? Like reincarnation?"
                                l "No, that can't be it, can it?"
                                l "This place would not have existed in my previous life if there is such a thing. It has only been open for twenty or so years."
                                l "Although... it is strange, but your explanation doesn't feel... wrong."
                                l "So hypothetically that means both you and I came here before, as humans?"
                                l "Did we do so together? Perhaps in a version of this date?"
                                l "I'm trying to make sense out of this but honestly I can't no matter how I twist or turn it."
                                l "Maybe it's better to just not lose ourselves in whatever is going on and just enjoy our date."
                                l "Our past lives don't matter, do they? What matters is this one, right here and now."


                            "Maybe a memory we picked up from those humans?":
                                l "That seems rather unlikely. We can only connect psychically with others like us."
                                l "As far as I'm aware it's impossible to interface with humans. Believe me, I tried..."
                                l "Besides, this memory feels as if it were my own, it's not the same feeling I get as reading someone else's."
                                l "... I will need some time to think this through, but for now we should probably go back to enjoying our date."
                                l "It's been so long, so we better enjoy it for all it's worth, right?"
                                

                    "Not really, it just confuses me more.":
                        l "Oh, I'm sorry about that [persistent.name]."
                        l "I wish I could explain it better, but it's just too hard to grasp, even for myself."
                        l "Either way, it's probably nothing, right? I think we should just focus on this date."
                        
        
        #EXTRA: For now this is a way to keep the game moving in the right direction, might add more content inbetween here.
        jump chinese_phoneScene           
    
    else:
        if love_meter >= 2:
            l "You know, it's kind of amusing we met up in this specific restaurant."
            l "Usually I come here with my [mom_parShort] and my [sis_sib], so it's a bit weird to be here with someone else."
            l "Weird in a good way though! It's a welcome change if I'm being honest."
            l "The reason we come here so much is because my [sis_sib], [persistent.date_sis], really adores this place."
            l "Since [mom_parShort] and me took [sis_obj] here for [sis_pos] fourteenth birthday [sis_sub] insisted on coming again for five years in a row."
            l "[sis_sub!c] always [conj('sis', 'picks', 'pick')] the orange chicken, it really is [sis_pos] favourite."
            menu:
                "[sis_sub!c] [conj('sis', 'sounds', 'sound')] nice, can you tell me more about [sis_obj]?":
                    n "[persistent.date] gives you a big smile."
                    l "Sure, what would you like to know?"
                    menu:
                        "What is the funniest memory the two of you share?":
                            jump chinese_riddle_talk_abbyMemory

                        "What [conj('sis', 'does', 'do')] [sis_sub] like to do?":
                            jump chinese_riddle_talk_abbyHobbies
        else:
            n "[persistent.date] is really quiet, [date_sub] [conj('date', 'is', 'are')] just scrolling on [date_pos] phone now, barely paying you any attention."
            n "It does not seem like [date_sub] [conj('date', 'is', 'are')] having a good time at all."
            jump chinese_phoneScene

label chinese_riddle_talk_abbyMemory:
    if persistent.tracker == 2:
        $ persistent.tracker2 = True
    #The code above this works for an easteregg
    l "I think I have a story you'll find quite funny, just stop me if I'm talking too much, alright?"
    l "[persistent.date_sis] was like five years old at the time of our story, it happened one night in the bunk bed bedroom we shared."
    l "One night [sis_sub] shook me awake. [sis_sub!c] told me [sis_sub] heard whispering and laughing coming from underneath our bed and begged me to go investigate it."
    l "I told [sis_obj] it was probably nothing and tried to go back to sleep but [sis_sub] wouldn't stop begging so eventually I gave in since I didn't want to wake the others with the commotion."
    l "As I stood before the dark opening underneath the bunk bed I felt as if something was watching me. But monsters didn't exist, right?"
    l "Right when I was thinking that I heard something whisper. I was terrified but as [persistent.date_sis_nickname]'s big [date_sib] I couldn't let [sis_obj] know I was so I tried to compose myself as best as I could and looked underneath the bed."
    l "It was pitch-black so I decided to slide my head fully underneath the bed, alongside with my right arm."
    l "As I fumbled around in the dark, my hand brushed against something soft. Just as I grabbed it laughter came from underneath the bed."
    l "I jumped back out, utterly terrified, nearly bursting out in tears."
    l "In my hand I held a pink bear, [persistent.date_sis_nickname]'s favourite toy, Mr. bunfluff."
    l "Apparently he was causing all that ruckus, his voicebox was slightly malfunctioning ."
    l "It's extremely amusing to picture how a pink bear scared the crap out of two little girls, it even was funny back then."
    l "I remember us laughing together for atleast an hour or so about the whole thing before going back to bed."
    n "[persistent.date] almost beams as [date_sub] [conj('date', 'recalls', 'recall')] the story."
    $ persistent.bedcheck_knowledge = True
    menu:
        "It sounds like you really care for your little [sis_sib].":
            l "Of course! I love [sis_obj] with all of my heart!"
            l "... I just don't want to lose [sis_obj], you know?"
            n "[persistent.date] gives you a saddened look."
            menu:
                "I understand, I have someone I never want to lose, but it seems like I am always on the verge of losing [date_obj]." if persistent.lildeaths > 0:
                    n "[persistent.date] tries [date_pos] best to give you a comforting smile and [date_sub] [conj('date', 'half-succeeds', 'half-succeed')]."
                    l "I see, so then you can relate to how I feel about [persistent.date_sis]. I always try to give [sis_obj] my all so that won't happen."
                    l "If your situation with that person is even slightly similar I'm sure you'll figure something out!"
                    n "[date_sub!c] [conj('date', 'gives', 'give')] you a big smile, her teeth reflecting off the light of the paper lanterns cozily flickering."
                    if persistent.lildeaths < 4:
                        n "[persistent.date]'s words fill your heart with hope, maybe there is a way to save [date_obj] afterall."
                    
                    elif persistent.lildeaths <= 7:
                        n "You are not sure how you'd possibly save [persistent.date] but you have to try it, for [date_obj]."
                    
                    else:
                        n "You try to hold back your tears as to not alert [date_obj] to something being wrong. You have seen [date_obj] die so many times.
                        Reliving [date_pos] deaths over and over while only being able to slightly change the way to inevitably reach them again is really messing with you."
                    jump chinese_phoneScene
                "Have you already lost someone close to you?":
                #TODO: Give the player the ability to say "Like [persistent.date_ghost]?" if he has learned about him. Then you can tell her that you heard about it when it happened since it is a small town but [persistent.date] will say that her mom, [persistent.date_sis_nickname] and her moved away from her hometown so that you couldn't know.
                    l "...Is it that obvious?"
                    menu:
                        "Well, I just kind of assumed...":
                            n "[persistent.date] lets out a small, slightly uncomfortable, laugh."
                            l "I see, so a lucky guess? Well, you are right, a long time ago I did lose someone important."
                            n "[persistent.date] begins to tear up."
                            menu:
                                "Do you want to talk about it?":
                                    l "I'd rather not honestly..."
                                    menu:
                                        "That's fine, just know that if you ever want to talk about it, I am here for you.":
                                            n "[date_sub!c] [conj('date', 'gives', 'give')] you a slight smile."
                                            if love_meter >= 2:
                                                l "Thank you [persistent.name], that means a lot to me."
                                                l "Although you have to admit that I don't know you all that well."
                                            else:
                                                l "No offence [persistent.name] but you got to admit that I barely know you."
                                            l "Wouldn't it be weird for me to tell you about something so personal?"
                                            menu:
                                                "In a way it can feel good to confide in a stranger, since they can't exactly share your secrets with anyone you know.":
                                                    jump chinese_lostSomeone_confideStranger
                                                "You could always ask me some questions to get to know me better if it helps make you feel more comfortable.":
                                                    jump chinese_lostSomeone_questions

                                                "This might sound strange but it almost feels as if I've known you for a while now." if persistent.lildeaths > 6:
                                                    l "Now that you mention it, I did notice that."
                                                    l "Since the last time we spoke you seem to know me a lot better..."
                                                    if love_meter >= 2:
                                                        l "As weird as it might be, somehow I feel the same. It's hard to explain, but it's a very distant feeling? Almost as if we have met eachother in a dream or something."
                                                        l "Still, as nice as that is it doesn't mean I can just tell you everything, not yet."
                                                        l "Those things take time, and lots of trust [persistent.name], I hope you understand."
                                                        jump chinese_phoneScene
                                                    else:
                                                        l "You have to admit that's rather creepy..."
                                                        l "{size=*0.5}Have you been stalking me [persistent.name]?{/size}"
                                                        n "Those words were not meant for you so you try your best to ignore them."
                                                        n "Besides, it's not like there's a good way to talk you out of this, is there?"
                                                        if persistent.lilithAliveAndRetriedCounter ==0:
                                                            n "The alternative is telling [date_obj] that this date is a loop, and that [date_sub] [conj('date', 'ends', 'end')] up dead in all of them."
                                                        else:
                                                            n "The alternative is telling [date_obj] that this date is a loop, and that [date_sub] [conj('date', 'ends', 'end')] up dead in most of them."
                                                        n "Something tells me [date_sub] [conj('date', 'would', 'would')] not take that well, not right now anyway."
                                                        l "...Look [persistent.name], I'm not sure what is going on, but I don't feel comfortable with this date anymore."
                                                        l "I think I'm just going to leave."
                                                        jump car_death

label chinese_riddle_talk_abbyHobbies:
    n "[persistent.date] chuckles slightly."
    $ persistent.quest_knowledge = True
    #Does this still make sense if I'm using renpy to make the game? Sure, it's just a hommage to my old days and the gallery also now has my games in it.
    l "Alright, here I go, just stop me when I begin to ramble on too much."
    l "[sis_sub!c] really [conj('sis', 'likes', 'like')] to create all kinds of things, right now it's mostly games."
    l "[sis_sub!c] can't really code a lot so [sis_sub] [conj('sis', 'uses', 'use')] Quest, it's a program that makes it easier to make textbased games."
    l "[sis_sub!c] made tons of those games but almost never [conj('sis', 'finishes', 'finish')] them."
    l "Even if [sis_sub] [conj('sis', 'does', 'do')], [sis_sub] almost never [conj('sis', 'does', 'do')] releases them."
    l "I think [sis_sub] mostly [conj('sis', 'makes', 'make')] them for [sis_ref], or for specific purposes."
    l "That doesn't mean [sis_sub] [conj('sis', 'keeps', 'keep')] them all to [sis_ref]. Sometimes [sis_sub] 'd ask me to play one of [sis_obj] games."
    l "In truth they are not really complex at the slightest but I always find them strangely intriguing nonetheless."
    menu:
        "What do you find interesting about [sis_pos] games?":
            l "Well for one, games made by a small team or even one person are almost an imprint of those people during their creative process."
            l "Two of [persistent.date_sis_nickname]'s games especially stand out in that regard."
            #n "[persistent.date] pauses for a moment before continuing" (This line really does not seem to have much value, just remove it?)
            l "In the first game you play as someone who has to feed a prisoner."
            l "You are discouraged from talking to the prisoner by a mysterious voice."
            l "A textbox appears and upon typing something the prisoner responds, it's here where things begin getting a bit... special."
            l "The prisoner begins to speak absolute nonsense no matter what you try typing in the textbox."
            l "They speak in a purple text, seeming oddly happy to see you and yet paying no attention to you at all."
            l "There is only one voice but they always refer to themselves as if there are multiple."
            l "The prisoner just keeps crying you are speaking in a \"stolen voice\" and how no one wants to hear it."
            l "Yet they keep begging you to speak, not to listen to it but because they like the color of your text, orange."
            l "This goes on for a good while, it's mostly the prisoner insulting you and commanding you to bow."
            l "After what around ten minutes of pure nonsense reactions to my input another voice began to speak."
            l "That voice had a dark blue hue. It also didn't really pay attention to what I was saying but the prisoner also didn't seem to notice the other voice."
            l "It kept calling out for help, repeatedly. I tried typing just the word \"help\" in the textbox, suddenly the door opened."
            l "A link appeared with the option to enter the cell, I wanted to know who was talking to me this entire time so I clicked it."
            l "There was no one there... Suddenly the door shut and I was locked inside."
            l "After a while you begin speaking the same nonsense as the prisoner, in purple as well."
            l "That's when the game turns to black and abruptly ends."
            n "For a moment [persistent.date] [conj('date', 'pauses', 'pause')] and [date_sub] [conj('date', 'looks', 'look')] at you with a slightly worried look in [date_pos] eyes."
            l "Oh, I have been talking for a while now, haven't I? I'm sorry [persistent.name]!"
            l "I totally would understand if you want to talk about something else instead now."
            menu:
                "I don't mind at all, in fact I think it's interesting. Feel free to talk about the second game!":
                    #TODO: Maybe make this fit a bit better with the themes of the first game she made and the game in general.
                    l "The second game has a bigger scope for it's location."
                    l "It's about a ravenprince who needs to climb a mountain with its wings bound together."
                    l "On its way the raven constantly meets new characters."
                    l "A cow called Io, seemingly the one from the myth, that believes she is a cow because some farmers told her so and eventually turns into a raven when she talks to the ravenprince."
                    l "A snake that keeps accidentally eating her own tail because she is confused, after freeing her she just starts once again."
                    l "A humanoid shadow with a rectangle for a head that dissappears every time you try to talk to it."
                    l "A three headed statue of a woman, each head speaks a different language. They speak Dutch, English and French respectively but neither of them seems to be able to make coherent sentences."
                    l "An old man that keeps walking in circles and who has gold coins where his eyes should be."
                    l "All of those characters discourage you from climbing the mountain, all of them except for the most important character of them all from what I could understand."
                    l "They are a sapphire being that hugs the raven and tells them they are forgiven."
                    l "Upon being told that they black out and awaken at the foot of the mountain as if their entire climb didn't really happen."
                    l "I must have \"completed\" that game atleast ten times, each time always ending the same way no matter whether I picked different choices or not."
                    l "I'm not sure at all what those games actually mean."
                    l "Do you know what they might be about?"
                    label chinese_abby_game_theme:
                        menu:
                            "They seem to share a theme about loops.":
                                jump chinese_abby_game_theme_loops
                            "There seems to be no theme, it's just pure nonsense.":
                                jump chinese_abby_game_theme_nonsense


                                label chinese_abby_game_theme_loops:
                                l "You must be absolutely right! The feeder becoming the prisoner, the raven climbing the mountain repeatedly, those must be loops."
                                l "...Although, what does that mean? Why would [persistent.date_sis_nickname] put that premise in two of [sis_pos] games?"
                                menu:
                                    "Maybe [sis_sub] just [conj('sis', 'likes', 'like')] the concept of loops?":
                                        n "[persistent.date] lets out a small chuckle."
                                        l "Who knows? Maybe that's all there is to it."
                                        n "[persistent.date] grows more somber and begins to slightly frown."
                                        l "Although I can't shake the feeling that there is something more going on with [sis_obj], something I'm not noticing."
                                        l "There's this voice in my head that keeps telling me I'm not good enough, that I failed [sis_obj] and that I destroy everything I touch."
                                        l "I would love to tell you that I didn't believe that voice in the slightest but that would be a lie."
                                        l "I don't want to lose [sis_obj] [persistent.name], I can't go through all of that again."
                                        l "Tears begin streaming down [date_pos] face as [date_sub] [conj('date', 'stares', 'stare')] at you with a defeated look in [date_pos] eyes."
                                        menu:
                                            "I know that voice is hard to ignore but for whatever it is worth, I really like you [persistent.date].":
                                                n "[date_sub!c] [conj('date', 'lets', 'let')] out a small, almost apologetic chuckle."
                                                l "Thank you [persistent.name], that's kind of you to say."
                                                n "Something about the way [date_sub] [conj('date', 'said', 'say')] it makes you think [date_sub] [conj('date', 'is', 'are')]n't ready to believe those words. Not right now anyway."
                                                n "It came out almost like as if had been a practiced response."
                                                n "[date_pos!c] doubt is close to being tangible, you can almost feel it hover over [date_obj] like a dark cloud."
                                                n "Yet with the weight it pushes down on [date_obj], it doesn't even resemble anything close to a cloud."
                                                n "[date_pos!c] face shifts into a worried look as [date_sub] [conj('date', 'realizes', 'realize')] you might have noticed what [date_sub] [conj('date', 'has', 'have')] been carrying around."
                                                jump chinese_phoneScene

                                            "That voice is just self-doubt, you are more than good enough [persistent.date].":
                                                l "Do you really think so, [persistent.name]?"
                                                menu:
                                                    "Absolutely! It might sound weird but I really feel like I've gotten to know you well even if this is our first date and you really are a good person." if persistent.burger_death_1 and persistent.cafe_death_1 == True and persistent.chinese_death_1:
                                                        jump chinese_abby_selfdoubt_knowYouWell
                                                    "I do but I think you are the one who needs to believe that for it to work.":
                                                        jump chinese_abby_selfdoubt_IDo
                                               
label chinese_abby_game_theme_nonsense:
    l "Do you really think so?"
    n "[persistent.date] softly scratches [date_pos] head, a pensive look on [date_pos] face."
    l "It's hard to believe that something could ever just be pure nonsense and nothing else."
    l "You have to pull the ideas you use to create anything from somewhere, right?"
    l "I'd like to think that even if someone would try to make a nonsensical game atleast some aspects of meaning would seep into it."
    l "After all, the medium is the message. So is it possible to create and form something without meaning even slightly implied?"
    l "Sorry if I'm rambling again! It's just something I've been thinking about for a while now."
    menu:
        "You are not at all, this is actually very interesting.":
            n "[persistent.date]'s face lights up with pride for a moment as [date_sub] [conj('date', 'lets', 'let')] out a giggle."
            l "You know, if you want to we could talk about it a little more."
            jump chinese_phoneScene

        "This is very interesting although I can't really wrap my head around it.":
            n "[persistent.date] gives you a cute giggle."
            l "No worries, my ramblings are pretty hard to understand sometimes, thanks for listening either way [persistent.name]!"
            jump chinese_phoneScene

label chinese_abby_selfdoubt_IDo:
    n "[persistent.date] chuckles with a pained expression painted on [date_pos] face."
    l "I suppose you are right. If I don't believe it myself it would just be empty praise coming from someone I barely met."
    n "[persistent.date] tries [date_pos] best to give you a smile, you can tell it's slightly forced."
    l "No offence [persistent.name]! I like how our date is going so far, even though I am messing it up pretty badly right now, but this {i}is{/i} only our first date."
    jump chinese_phoneScene

label chinese_abby_selfdoubt_knowYouWell:
    n "[persistent.date] wipes away some tears as [date_sub] [conj('date', 'gives', 'give')] you a big smile."
    l "Thank you [persistent.name], I'd like to know you the same way you seem to know me."
    l "I know it is strange but somehow I can see in your eyes that you truly seem to know me quite well already."
    jump chinese_phoneScene

label chinese_lostSomeone_confideStranger:
    n "[persistent.date] scratches [date_pos] head and gives you a nice smile."
    l "I suppose you are right, I might take you up on that offer eventually."
    n "You are not really sure if [date_sub] [conj('date', 'means', 'mean')] it."
    jump chinese_phoneScene

label chinese_lostSomeone_questions:
    n "[persistent.date] begins to laugh."
    l "I'm not sure it really works like that [persistent.name].  I can't really think of any combination of questions that would make me feel like this isn't our first date."
    l "You get to know someone by spending time together not just by seeing them once, but thanks for the suggestion either way!"
    l "[persistent.date] gives you a cute little smile."
    jump chinese_phoneScene

label chinese_phoneScene:
    if persistent.rockMode == False:
        n "[persistent.date] [conj('date', 'gets', 'get')] up from [date_pos] chair and pushes it back under the table."
        if love_meter == 1:
            n "You notice a strange look on [date_obj] face which disappears before you can decipher it."
            $ chinese_lilithBreakupTrigger = 2
            l "I just need to use the bathroom real quick."
        else:
            l "I'll be right back [persistent.name], I just need to go to the bathroom real quick."
            n "[date_sub!c] [conj('date', 'gives', 'give')] you a cute smile before speeding off."
        hide lilith talk_closed with easeoutright

        n "As [date_sub] [conj('date', 'disappears', 'disappear')] behind the bathroom door you notice [date_obj] forgot [date_pos] phone, it is still laying on the table."
        if persistent.lildeaths >= 7:
            if persistent.peeked_phone == True:
                if persistent.abigail_call_knowledge == False or persistent.david_call_knowledge == False or persistent.james_call_knowledge == False or persistent.lila_call_knowledge == False:
                    n "...We both know what you will do next, isn't that right?"
                    n "You've already done it before, why stop now? After all, this might be the lead you need to save [date_obj]."
                    n "Is that what you are thinking? That [date_sub] won't remember any of this so that it doesn't matter?"
                    n "Go on. I won't stop you, not as long as this remains my story."
            else:
                $ nopeek = True
                n "You know it isn't right to do but maybe you could find a way to save [date_obj] on [date_pos] phone."
                n "If there is even the slightest chance that it will help [date_obj] you owe it to [date_obj] to try that out, right?"
        menu:
            "*Take a quick peek at [date_pos] phone.*":
                jump chinese_phone_peek
            "*Respect [date_pos] privacy.*":
                jump chinese_phone_noPeek
    else:
        n "At around this time [persistent.date] and you would have recieved your food."
        n "This time however things are different. There is no food. Even if there was, it's not like you two can eat it."
        n "That's probably for the better however. [date_pos!c] bloated face still haunts your nightmares."
        n "For a second it almost feels like you were the one suffocating, not [date_obj]."
        n "You try to remain calm by reminding yourself you don't need to breathe in this form."
        jump restaurant_death_1_prevented

label chinese_phone_peek:
    #TODO: Maybe besides the numbers also have a picture folder that is completely empty, refering to when she tells you in kokiri she can't take pictures anymore after what happened to James
    #Maybe add a few other things you can find on the phone aswell besides that?
    n "As you open [date_pos] phone you are greeted by a picture of a pug as the phone's background and a prompt to enter the password."
    if persistent.pass_knowledge == True:
        n "You remember that [date_pos] password is 81155"
    else:
        n "Suddenly it dawns on you that you do not know what [date_pos] password is."
        $ persistent.need_pass_knowledge = True
        menu:
            "*Put the phone back.*":
                label chinese_phone_peek_putPhoneBack:
                    n "You put the phone back and try to act as natural as you can all the while quickly glancing around to see if anyone caught you."
                    n "Everyone seems to be too busy enjoying their food to pay you any attention. You are saved by the excellent cuisine."
                    n "Just as you let out a sigh of relief [persistent.date] comes back to your table."
                    l "Hey [persistent.name], I'm back. Did they bring our food? Not yet?"
                    if chinese_lilithBreakupTrigger == 0:
                        l "That's okay, I'm just really looking forward to it, the food here is to die for."
                        if persistent.chinese_death_1 == True:
                            n "It indeed seems to be that way doesn't it [persistent.name]?"
                        n "You play along with [persistent.date], hoping [date_sub] didn't catch you."
                        l "..."
                        n "[persistent.date] squints [date_pos] eyes and seems to be lost in thought for a moment."
                        l "Is everything alright [persistent.name]? You look pretty nervous."
                        menu:
                            "Y- yeah, I'm totally fine. (Lie)":
                                n "[persistent.date] squints [date_pos] eyes slightly and almost pierces your soul with [date_pos] gaze."
                                $ love_points = -1
                                $ love_meter_updater(False)
                                l "Alright [persistent.name], if you say so."
                                n "You have to stop yourself from shaking in your seat, did [date_sub] buy that lie?"
                                n "The alternative makes you tremble so badly you try to convince yourself that [date_sub] did."
                                n "Anyway, no undoing this, although there is, isn't there? Something tells me this won't be the last time."
                                jump chinese_phone_noPeek


                            "I'm just a bit nervous about this date to tell you the truth. I just don't want to mess this up and lose you. (Half-truth)":
                                if love_meter >= 2:
                                    l "Oh [persistent.name], I had no idea you felt that way! That's completly okay, I'm glad you told me."
                                    l "To be entirely honest with you, I feel the same. This has been my first date in quite a while and I'm having a really good time."
                                    l "So it would be a shame if I somehow messed it up. However right now we're both still here, right? Seems to me this date is a success!"
                                    n "[persistent.date] gives you a cute smile."
                                    n "You feel guilty for telling that lie to [date_obj]. Well, more like half-truth, but that still means it's a half-lie."
                                    n "You try to ignore your guilt as best as you can to focus on enjoying your remaining time with [date_obj]."
                                    jump chinese_phone_noPeek
                                else: 
                                    if major_love_offence == False:
                                        l "{size=*0.5}That actually might explain your behaviour somewhat...{/size}"
                                        l "{size=*0.5}Although it's definetly no excuse.{/size}"
                                        l "Is that why you are acting quite \"tough\" [persistent.name]?"
                                        l "If I can give you a small piece of advice, I don't really like being treated like that."
                                        l "You seemed way nicer when we first met. So I know there's someone nice underneath that mask you are wearing, or perhaps that was the mask?"
                                        l "Let's hope it's not the latter..."
                                        menu:
                                            "You're right. Sorry for hurting you by trying to act more tough.":
                                                l "It's okay [persistent.name]! This doesn't make everything alright but apologizing is a good first step."
                                                l "You don't have to prove yourself to me. After all, I came here to go on a date with {i}you{/i}, didn't I? Not whatever role you were playing."
                                                l "I know insecurities can be hard to deal with, sometimes they manifest in ways that harm ourselves and other people." #TODO: if she told you about how she feels insecure about her not being good enough for ehr sister have her refference this.
                                                l "Just know that if you feel a thought like that pop up again you can always talk to me about it, alright?"
                                                l "I've been going through something similair a while ago and I find that talking it through really tends to help." #TODO: Do not show this line if she already used the other example as a reference
                                                l "I won't pretend that's a total fix. In fact, I often still struggle with it. Still, it helps to control my own insecurity a little better."
                                                menu:
                                                    "Thank you for being so patient with me. That means a lot.":
                                                        n "[persistent.date] gives you a cute smile."
                                                        l "Hey, don't mention it [persistent.name]. I know I wouldn't be the same person if others didn't have patience with me."
                                                        l "I'm just glad that I was able to get through to you."
                                                        jump chinese_phone_noPeek
                                                        
                                    #TODO: Alternate version where she gets mad at you for treating her really badly and leaves.

                            "Okay, I'll be honest. I was going through your phone to try learning more about you, but I have a good reason!":
                                menu: 
                                    "I need to save you. You are repeatedly dying over and over in some sort of loop.":
                                        l "Nope, I'm not having any of this [persistent.name]. First you go through my phone, without my consent, and then you make up some crazy argument to justify your action?"
                                        l "Even if some fucked up part of you believes you are saving me, surely you can see this is really not the way to do it, right?"
                                        $ angryLilith = True
                                        $ love_meter_updater(True)
                    else:
                        l "That's probably for the best..."
                        l "While I was in the bathroom I have been thinking..."
                        l "Look, I don't think this is going to work out between us [persistent.name]."
                        l "You just seemed so different when we were talking over texts and calls."
                        l "I was really looking forward to this date, but now I think it's just better that I end this."
                        l "Goodbye [persistent.name]."
                        jump car_death
                        
            "*Try a code anyway.*":
                jump chinese_phone_peek_code
    label chinese_phone_peek_code:
        $ phonecode = renpy.input("Enter the password", length=5)
        $ phonecode = phonecode.strip()
        if phonecode == "81155":
            n "The code is correct."
            if persistent.pass_knowledge == False:
                n "... How did you know that? You haven't learned that code yet, right?"
                n "Did you look the answer up online?"
                n "Or did you play this game before?"
                n "If it's the latter I'm flattered you came back for some more but if it's the first I'd like for you to engage with my puzzles a bit more."
                n "Although, I suppose you were atleast engaged enough to keep playing and didn't give up..."
                n "Forget I said anything."
                n "Just promise me you'll try to look for the answers yourself first next time, alright?"
            if narrator_dialogue_seen("chinese.pass_wrong.intro"):
                $ pass_wrong_streak = narrator_dialogue_state_get("chinese.pass_wrong.streak", 0)
                if pass_wrong_streak >= 5 and not narrator_dialogue_seen("chinese.pass_wrong.relief"):
                    n "... Wait, you entered the right password? I forgot how it felt to have that happen."
                    n "I'm so happy I finally get to narrate something different."
                    n "Let's just forget that torture ever happened at all and move on to with the story."
                    $ narrator_dialogue_mark_seen("chinese.pass_wrong.relief")
                $ narrator_dialogue_state_set("chinese.pass_wrong.streak", 0)

            jump chinese_phone_peek_numbers
        else:
            n "Wrong password."
            if persistent.pass_knowledge == True:
                $ pass_wrong_total = narrator_dialogue_state_get("chinese.pass_wrong.total", 0)
                $ pass_wrong_streak = narrator_dialogue_state_get("chinese.pass_wrong.streak", 0)

                if not narrator_dialogue_seen("chinese.pass_wrong.intro"):
                    n "Wait, that can't be right."
                    n "You know the password, don't you?"
                    n "I even reminded you just in case."
                    n "Did you just want to see the scene where you get caught again?"
                    n "I guess you win, I can't afford to derail this story even more, not for something so minor."
                    if persistent.mayoFreak == True:
                        n "Besides, we both know what will happen if you don't get your way."
                        n "I am not ready for another mayo-incident..."
                    n "I'll just jump you forward to that scene and we can pretend like nothing happened."
                    $ narrator_dialogue_mark_seen("chinese.pass_wrong.intro")
                else:
                    n "Again?"
                    n "Fine, as you wish."
                    #TODO: Rewrite this text next time.
                    if pass_wrong_total >= 1 and not narrator_dialogue_seen("chinese.pass_wrong.followup.1"):
                        n "Just enter the right code next time, alright?"
                        $ narrator_dialogue_mark_seen("chinese.pass_wrong.followup.1")
                    elif pass_wrong_total >= 2 and not narrator_dialogue_seen("chinese.pass_wrong.followup.2"):
                        n "You're really going to keep doing it aren't you?"
                        $ narrator_dialogue_mark_seen("chinese.pass_wrong.followup.2")
                    elif pass_wrong_total <= 5 and not narrator_dialogue_seen("chinese.pass_wrong.followup.3"):
                        n "Can you stop that please?"
                        if not persistent.beachroute_visited_knowledge:
                            n "You're not going to make any progress like this, can't you do something that will actually move the story further?"
                        else: 
                            n "I get that you're starved for more story but this can hardly be called story, right?"
                            n "You just get an extra dialogue line, two if you're lucky."
                            n "Is that really worth all of this to you?"
                        $ narrator_dialogue_mark_seen("chinese.pass_wrong.followup.3")
                    elif pass_wrong_streak > 1 and not narrator_dialogue_seen("chinese.pass_wrong.streak_callout"):
                            if pass_wrong_total != pass_wrong_streak:
                                n "You've been doing this [pass_wrong_total] times now, your current streak is [pass_wrong_streak]."
                            else:
                                n "Really?"
                                n "You're just going to keep doing this?"
                                n "You have a streak of [pass_wrong_streak] now, you didn't stop once since you started getting the answer wrong on purpose."
                                n "At this point I'm wondering if this is just a personal attack against me or something."
                            n "That's right, I'm keeping track."
                            n "All of these times, no matter what you did, it always ends the same."
                            n "So why do you keep coming back?"
                            $ narrator_dialogue_mark_seen("chinese.pass_wrong.streak_callout")

                $ narrator_dialogue_state_inc("chinese.pass_wrong.total", 1)
                $ narrator_dialogue_state_inc("chinese.pass_wrong.streak", 1)
                jump chinese_phone_caught
            n "You try to input a few other codes to see if those work instead."
            label chinese_phone_randomNumbers:
                $ phone_wrongPassword_graceSystem = renpy.random.randint(1,80)
                $ phone_wrongPassword_graceSystem += (persistent.retry_counter* 10)
                if phone_wrongPassword_graceSystem == 100:
                    n "Avoiding the wrong passwords you remember from your previous attempts you manage to somehow luck yourself into typing the correct password after a couple of tries."
                    n "It is 81155."
                    $ persistent.pass_knowledge = True
                    if chinese_lilithBreakupTrigger > 0:
                        #TODO: I'm honestly not even very sure anymore what this trigger even is needed for and if there isn't a simpler way to do it.
                        $ chinese_lilithBreakupTrigger -= 1
                    if chinese_lilithBreakupTrigger == 0:
                        jump chinese_phone_caught 
                    else:
                        jump chinese_phone_peek_numbers
                elif chinese_lilithBreakupTrigger == 0:
                    n "None of the other codes seem to result in anything either. You are not sure how many you tried, you decide to close the phone in case [persistent.date] will come back."
                    jump chinese_phone_caught
                else:
                    n "You probably have a little more time left before [date_sub] [conj('date', 'comes', 'come')] back."
                    jump chinese_phone_randomNumbers

label chinese_phone_caught:
    if peeked_phone_temp == True:
        $ persistent.peeked_phone = True
        if persistent.playerCalledAbigail == False and persistent.playerCalledDavid == False and persistent.playerCalledJames == False and persistent.playerCalledLila == False:
            n "You think you sucessfully memorised the phone-number, I guess only time will tell." #TODO: This line can also trigger if the player needs to put the phone back because he can't learn anymore numbers. In that case this line really doesn't make any sense.
            n "Because if you've already gone this far you will only go further, right?"
            
        else:
            if persistent.restrainingorderfamily_knowledge == True:
                n "You succesfully memorised the number of the next person you are going to involve into this whole mess, the exact thing [persistent.date] asked you not to do."
                n "How do you think that would make [date_obj] feel if [date_sub] knew?"
            else:
                n "You succesfully memorised the number of the next person you are going to involve into this already way too complicated situation."
                n "Do you really think that that's a good idea?"
    n "No need to answer that, it was rhetorical. What you need to do is close that phone."
    n "Right as you do so you can see [persistent.date] approaching. You also see a very angry expression on [date_pos] face."
    n "As [date_sub] [conj('date', 'walks', 'walk')] up to the table [date_sub] [conj('date', 'grabs', 'grab')] [date_pos] phone and jams it in [date_pos] handbag"
    l "What you just did was inexcusable [persistent.name]! I really didn't expect this from you."
    l "I'm leaving, goodbye and do not ever contact me again."
    if persistent.chinese_phone_noretry == True:
        n "Yet here you are once again, making the same mistake you've already made. All the while [persistent.date] is none the wiser."
        n "Is that why you came back to do the same thing [date_sub] told you [date_sub] didn't want you to do? Would you have acted differently if [date_sub] could remember every action you took?"
        n "Don't worry [persistent.name], this is just all a game, right? Your actions here don't mean anything at all, right?"
        n "..."
    else:
        $ persistent.chinese_phone_noretry = True
    jump car_death

label chinese_phone_noPeek:
    if persistent.peeked_phone == False and persistent.lildeaths >= 2 :
        n "It's probably best not to look. Even if it might have info on it that could help [date_obj] survive. "
        n "Still... you are thinking about it aren't you?"
        n "If you weren't before, now you most definitely are."
    jump restaurant_death_1 #Lilith walks back from the bathroom and will die.

label chinese_phone_peek_numbers:

    n "You see a section of[date_pos] phone numbers, labeled with \"family:\". It has four names underneath."
    if persistent.restrainingorderfamily_knowledge == True:
        n "You remember [persistent.date] told you to not involve them."
        n "[date_sub!c] probably wouldn't appreciate this."
        n "Yet then again, it could really help you out in the long-term."
        $ persistent.restrainingorderfamily_violation_counter += 1
    else:
        n "If anyone besides [persistent.date] would have some useful insights about [date_obj] it's them."
        n "You might just have enough time to learn one phone-number."

    $ peeked_phone_temp = True
    menu chinese_learnNumberChoice:
        "Learn [persistent.date_sis]'s phone number." if not persistent.abigail_call_knowledge:
            $ persistent.abigail_call_knowledge = True
            jump chinese_phone_loop
        "Learn [persistent.date_dad]'s phone number." if not persistent.david_call_knowledge:
            $ persistent.david_call_knowledge = True
            jump chinese_phone_loop
        "Learn [persistent.date_ghost]' phone number." if not persistent.james_call_knowledge:
            $ persistent.james_call_knowledge = True
            jump chinese_phone_loop
        "Learn [persistent.date_mom]'s phone number." if not persistent.lila_call_knowledge: 
            $ persistent.lila_call_knowledge = True
            jump chinese_phone_loop
        "Put the phone back." if persistent.abigail_call_knowledge and persistent.david_call_knowledge and persistent.james_call_knowledge and persistent.lila_call_knowledge:
            $ persistent.restrainingorderfamily_violation_counter -= 1
            if chinese_lilithBreakupTrigger > 0:
                jump chinese_phone_peek_putPhoneBack
            else:
                jump chinese_phone_caught

label chinese_phone_loop:
    if chinese_lilithBreakupTrigger > 0:
        if not persistent.abigail_call_knowledge or not persistent.david_call_knowledge or not persistent.james_call_knowledge or persistent.lila_call_knowledge:
            n "You feel as if you have enough time to learn an extra phone number before [date_sub] will come back."
        jump chinese_learnNumberChoice
    else:
        jump chinese_phone_caught

label chinese_riddle_decline:
    l "No worries at all [persistent.name]!"
    l "Maybe you'd like giving one instead?"
    menu: 
        "Sure, that sounds good.":
            menu:
                "What has four legs in the morning, two legs at noon and three legs in the evening?":
                    l "Ah that's a real classic! The answer is humans. The question originated from the myth of Oedipus if I'm not mistaken."
                    l "I didn't know you were into mythology [persistent.name], that's really cool!"
                    menu:
                        "Thanks, [persistent.date]! From your response, I gather you’re also into mythology, right?":
                            #TODO: Rewrite this a bit, I think it's a bit overdone.
                            l "Oh, absolutely!"
                            n "[date_sub!c] said it pretty loudly, but didn't seem to notice."
                            l "I practically live and breathe mythology."
                            l "When I was little, I got my first mythology book about the Greek and Roman gods, and it was like a whole new universe opened up."
                            l "Each story was so vivid and alive, like I could picture every god, monster, and hero as if they were real people."
                            l "The first story I fell in love with was the tale of Persephone. How she was taken to the underworld and how her mother, Demeter, searched endlessly for her."
                            l "I was so fascinated by the idea of the seasons coming from a mother’s love and grief."
                            l "Then there’s the story of Odysseus, who journeyed for years to return to his wife, Penelope, facing all kinds of trials. I think that was the first time I understood that myths weren’t just storie. They were about the choices we make, the courage to keep going, and the struggle to stay true to ourselves."
                            l "Recently, I’ve been reading Finnish mythology, specifically the Kalevala. It’s totally different from Greek myths. It’s full of epic poems and songs, and the stories are steeped in nature and magic. One of my favorites is about Väinämöinen, this wise old bard who could sing magical songs to make anything happen. His power wasn’t in strength or weapons, but in his words and wisdom."
                            l "It’s amazing how these stories, even though they’re ancient, still resonate today. They speak to something deep inside us, don’t you think?"
                            l "Meeting someone like you who’s into mythology is rare, [persistent.name]. It’s like finding someone who also sees the beauty in these old, forgotten worlds."
                            n "As [date_sub] [conj('date', 'stops', 'stop')] [date_sub] suddenly looks around to all the people in the restaurant, some of them are watching the both of you, or more specifically, [date_obj]."
                            n "[date_sub!c] [conj('date', 'turns', 'turn')] beetred."
                            l "Was I a bit too loud? I'm sorry [persistent.name], I just got really excited."
                            menu:
                                "No need to apologize for being passionate [persistent.date]. It's nice to see you like that.":
                                    n "[date_sub!c] [conj('date', 'turns', 'turn')] even more beetred, something you did not consider even remotely possible."
                                    l "Thank you [persistent.name], I guess you are right. It's very sweet of you to say that."

                        "Actually I just found that riddle on the internet a while back.":
                            n "[persistent.date] looks slightly disappointed."
                            l "Oh... that's alright [persistent.name], I guess sometimes I forget that that riddle is practically used everywhere now."
                            l "Tons of movies, books and games now kind of use that riddle as a placeholder because it's so well known. It's the \"lorum ipsum\" of riddles."
                            n "Hey, [conj('date', 'is', 'are')] [date_sub] complaining about my ability to write riddles? I mean your ability to come up with riddles."
                            l "Still, thank you for your riddle! Regardless of how many times it has been used, it still remains a classic."
                            l "I think you must've thought so aswell since you can still remember it after you read it online."

                "What has five teeth, twelve eyes, four arms and a thousand legs?":
                    l "..."
                    n "[persistent.date] scrathes [date_pos] head, deep in thought."
                    l "I don't know [persistent.name], that's a really tough one."
                    l "What is the answer?"
                    menu:
                        "Well, the answer is that I don't know either.":
                            n "[persistent.date] gives you a confused look before it all clicks and [date_sub] [conj('date', 'bursts', 'burst')] out in laughter."
                            l "You sure got me there [persistent.name]!"
                            l "Although, if you don't know the answer, and that is the answer, doesn't that mean that you know the answer?"
                            n "You are not entirely sure what [date_sub] [conj('date', 'means', 'mean')]."
                            n "Apparently [persistent.date] must have been able to read just that from your face as [date_sub] immediately [conj('date', 'turns', 'turn')] beet-red and tenses up a bit."
                            l "I'm sorry, that was way too much for a first date wasn't it?"
                            l "I didn't mean to sound like a know-it-all."
                            l "Please just forget what I said, alright [persistent.name]?"
                            menu:
                                "I don't mind at all [persistent.date], you just kind of threw me for a loop with what you just said. It does sound interesting though.":
                                    n "[persistent.date] lets out a sigh of relief as [date_sub] [conj('date', 'relaxes', 'relax')] a bit more once again."
                                    l "I already was fearing the worst."
                                    l "A lot of people have told me that I come off as info-dumping way too much, especially when I get to know someone at first."
                                    l "It's just that I love to think about things deeply, especially if they fascinate me."
                                    l "I also enjoy sharing those thoughts, it's just, most people don't seem to enjoy listening to them. {size=*0.5}To me aswell.{/size}"
                                    n "Something tells you you weren't supposed to hear that last part."
                                    l "So thank you [persistent.name], now I know that I can release my full arsenal on you!"
                                    n "[persistent.date] let's out a mischevious little chuckle."
                                    l "I'm only joking, I wouldn't want you to run away from me after all."
                                    if persistent.runAwayLilith_counter >= 3:
                                        n "I don't think [date_sub] [conj('date', 'has', 'have')] to worry about that in the slightest, does [date_sub]?"
                                        n "After all, usually when it comes to running away it's the opposite way, isn't it player?"
                                    menu:
                                        "Running away? From such good company? I would never forgive myself of that.":
                                            n "Just like that [date_sub] [conj('date', 'turns', 'turn')] completely beetred once again."
                                            l "{size=*0.5}Uhm...uhm... uhm...{/size}"
                                            n "[date_sub!c] [conj('date', 'covers', 'cover')] [date_pos] face for a short moment, takes a deep breath in and then [conj('date', 'continues', 'continue')]."
                                            l "My, you are quite a flatterer aren't you?"
                                            l "But seriously, that means a lot to me, to hear that you consider me good company."
                                            l "Normally I probably wouldn't tell you that, but I'm trying to be a bit more direct lately."
                                            l "..."
                                            if love_meter >= 3:
                                                l "You know, for what it is worth, I also really like your company [persistent.name]."
                                                l "I'm having a really good time here with you so far."

                                "Sure thing, if that's what you want. Let's talk about something else":
                                    jump chinese_riddle_railroad
                            
                "A man is in a metal room without a door and with a barred window. How does he leave?":
                    l "Hmm, that seems to be a tough one, let me think about it for a second [persistent.name]!"
                    n "[persistent.date] seems to happily be going through potential solutions."
                    l "{size=*0.5}Maybe he needs to do something with the window?{/size}"
                    l "{size=*0.5}But it's barred...{/size}"
                    l "{size=*0.5}Then again, it must have to do something with the window, right?{/size}"
                    l "{size=*0.5}After all, there is no door.{/size}"
                    l "{size=*0.5}But then how did he get in?{/size}"
                    l "{size=*0.5}Wait a second...{/size}"
                    l "I think I got the answer!"
                    n "[date_sub!c] [conj('date', 'is', 'are')] practically bouncing on [date_pos] seat as [date_sub] [conj('date', 'is', 'are')] saying this."
                    l "I think the answer is that there is no door but there is a doorframe!"
                    l "So that means he just has to walk out through there."
                    l "Did I get it right?"
                    menu:
                        "Yes you did, great job [persistent.date]!":
                            n "[persistent.date] fist pumps the air."
                            l "Yes! That was a very fun riddle [persistent.name], not what I was expecting but it forced me to think outside the box a little bit."

                "How many ends does a ring have?" if persistent.ringRiddle_knowledge:
                    l "It's endless, isn't it? So it literally has no endings."
                    l "But I suppose you could choose a point where the rings starts and ends."
                    l "So in a way it does have an end if you decide it has one."
                    l "You could even argue that theoretically it has infinite ends since you can say it begins on an infinite ammount of points."
                    n "For a moment [date_sub] [conj('date', 'is', 'are')] lost deep in thought."
                    l "Honestly, now that I'm thinking about it, the latter seems to actually make a lot of sense."
                    l "We constantly start and end things, don't we?"
                    l "The start of every second is the end of the previous one."
                    l "Our lives are filled with constant endings in a way, so maybe it's the same with the ring?"

    jump chinese_riddle_railroad
return
