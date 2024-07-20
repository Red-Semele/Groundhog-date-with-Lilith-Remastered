label chinese_start:
    $ chinese = True
    l "That sounds like a plan!"
    l "I'll see you there."
    n "You head to the Chinese restaurant, when you arive there Lilith is already seated. She happily waves at you."
    n "It's appears to be quite busy, there are people at every table."
    n "You walk towards the table where Lilith is sitting and greet her with a cheerful smile."
    l "Heya [name]!
    Glad to see you here.
    You're in luck, I managed to save this table just in the nick of time."
    n "She gives you an honest smile."
    menu:
        "Glad to be here.":
            l "Oh you flatterer!"
            n "Lilith pauses for a moment, seemingly lost in a thought."
            l "Or are you glad to be here for the restaurant itself?"
            menu:
                "Mostly the restaurant actually, otherwise I wouldn't have come her with you in the first place.":
                    jump chinese_start_gladToBeHere_theRestaurant

                "I'm glad to see you of course, otherwise I would've just come to this place on my own.":
                    jump chinese_start_gladToBeHere_youOfcourse

label chinese_start_gladToBeHere_theRestaurant:
$ love_points = -1
$ love_meter_updater()
l "Oh, I mean I like this place aswell I suppose..."
n "She seems slightly dissapointed with your answer."
l "Anyway, I think I'd starve if I don't eat soon so let's continue our little chat while we wait on our food.
What would you like to order?"
#Make her slightly more dissapointed.
jump chinese_menu
label chinese_start_gladToBeHere_youOfcourse:
    l "Lilith lets out a sigh of relief and chuckles slightly."
    l "Sorry, that was just a thought that popped up in my head."
    n "She looks like she could sink through the floor out of embarrassment so you decide it's best to forget what she has said."
    l "Anyway, I think I'd starve if I don't eat soon so let's continue our little chat while we wait on our food.
    What would you like to order?"
    jump chinese_menu
label chinese_menu:
    $ peking = False
    $ orange = False
    menu:
        "I'm going for the peking duck.":
            $ peking = True
            jump chinese_menu_result

        "I think I'll pick the orange chicken.":
            $ orange = True
            jump chinese_menu_result

label chinese_menu_result:
    if peking == True:
        l "That's a good choice!
        So good in fact that I was thinking about picking the same thing."
    elif orange == True:
        l "That's a good choice!
        I've had my fair share of orange chicken already throughout my life, so I think I'm going for something else."
        n "Lilith scratches her chin softly."
        l "I think I'm going to pick the peking duck, beats another portion of orange chicken."
        n "She lets out a small chuckle."

    menu:
        "Actually there is something in that peking duck that you are really allergic to, deathly even." if persistent.chinese_death_1:
            jump restaurant_death_1_prevented

        "Sounds good to me!":
            n "Suddenly a waitress stands right before your table, slightly startling you.
            Lilith tries her best not to burst out with laughter but a few muffled laughs get through.

            After writing down both of your choices she wanders of towards the kitchen."

            l "Do you want to try to answer a few riddles in the meantime?"

            menu:
                "I'd rather not actually, I'm pretty bad at answering riddles.":
                    jump chinese_riddle_decline

                "Sure, I'd like that!":
                    jump chinese_riddle_accept


label chinese_riddle_accept:
    $ rw1 = 0
    $ rw2 = 0
    $ rw3 = 0
    $ rw_total = 0
    $ persistent.chineseRiddlesSeenXTimesCounter += 1
    l "Alright, here is the first riddle.
    They are all based around Greek and Roman myths.
    So here we go."
    label chinese_riddle_first:
        l "To taunt the gods with webs of lies
        is to hang but not to die."
        #The second part should probably be based on the wrong answer counter so she doesn't constantly say the same thing.

        n "Lilith pauses for a moment."
        l "So, do you have an idea who I could be talking about?"
        if persistent.r1_knowledge == True:
            n "You remember Lilith telling you the answer was Arachne."
        $ r1 = renpy.input("Place your guess here")
        $ r1 = r1.strip()
        $ r1 = r1.lower()
        if r1 == "arachne":
            l "That's right!"
            l "Lets try out the next riddle."
            jump chinese_riddle_second
        #For some reason it triggers the demetrius text every time you give yourself a wrong name.
        elif r1 == "demetrius":
            if name == "Demetrius":
                $ demetrius = True
                $ riddle_loop = 5
                jump riddle_tryAgain_loop


        elif r1 == "adriel":
            if name == "Adriel":
                $ adriel = True
                $ riddle_loop = 5
                jump riddle_tryAgain_loop
                #It seems to never be five and just instantly become less than zero.
                #My current theory is that it is due to the fact that the r2 and r3 text also moves you back to the loop for some reason.

        else:
            label cafe_riddleOne_retry:
            l "Hmm, not exactly who I was thinking about.
            Would you like to try again or have me give the answer?"
            $ rw1 += 1
            label cafe_riddle_menu:
                menu:
                    "I'd like to give it another shot.":
                        if rw3 == 0:
                            if rw2 == 0:
                                if rw1 == 0:
                                    "Error, you are not supposed to be here or something went wrong."
                                else:
                                    jump chinese_riddle_first
                            else:
                                jump chinese_riddle_second

                        else:
                            jump chinese_riddle_third

                    "I'd like to know the answer.":
                            if rw3 == 0:
                                if rw2 == 0:
                                    if rw1 == 0:
                                        "Error, you are not supposed to be here or something went wrong."
                                    else:
                                        $ persistent.r1_knowledge = True
                                        l "Sure thing, that was a really tricky one."
                                        l "The answer is Arachne."
                                        $ riddleAnswersTold += 1
                                        l "Let's move on to the next riddle."
                                        jump chinese_riddle_second
                                else:
                                    $ persistent.r2_knowledge = True
                                    l "Alright, that was quite a though one."
                                    l "The answer is Europa."
                                    $ riddleAnswersTold += 1
                                    l "Let's move on to the next riddle."
                                    jump chinese_riddle_third

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
                            jump cafe_riddleOne_retry
                    else:
                        $ riddle_loop -= 1
                        l "Hmm, not exactly who I was thinking about.
                        Would you like to try again or have me give the answer?"
                        jump riddle_tryAgain_loop

label demetrius_unanswered_chat:
    de "There's not a chance, besides, in it's state I think it's going to read this instead of hearing us speak."
    $ adriel_talk = renpy.input("Unite the two halves.")
    $ adriel_talk = adriel_talk.strip()
    $ adriel_talk = adriel_talk.lower()
    if adriel_talk == "a shame really, it has such potential. It reminds me of amber, gregory, lisa and steven.":
        de "Do not mention those names here! If anyone might hear our little chat it's them, they found the true path to godhood afterall."
        $ adriel_talk = renpy.input("Unite the two halves.")
        $ adriel_talk = adriel_talk.strip()
        $ adriel_talk = adriel_talk.lower()
        if adriel_talk == "oh did they really do that? Now that you mention it, i remember hearing they rejected the false gods and became gods worth a follow themselves. How did they manage to do that?":
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
        if dem_talk == "do not mention those names here! If anyone might hear our little chat it's them, they found the true path to godhood afterall":
                ad "Oh did they really do that? Now that you mention it, I remember hearing they rejected the False Gods and became Gods worth a follow themselves. How did they manage to do that?"
                $ dem_talk = renpy.input("Unite the two halves.")
                $ dem_talk = dem_talk.strip()
                $ dem_talk = dem_talk.lower()
                if dem_talk == "you know we can't discuss that, what if it found our conversation? now let us never speak about this again and hope that it won't notice us":
                        ad "With all those eyes It has those odds are really slim but as you wish Demetrius."
                        return




    label chinese_riddle_second:
        l "Carried by Lightning with a crown of moon."
        n "Lilith pauses for a moment."
        l "So, do you have an idea who I could be talking about?"
        if persistent.r2_knowledge == True:
            n "You remember Lilith telling you the answer was Europa."
        $ r2 = renpy.input("Place your guess here")
        $ r2 = r2.strip()
        $ r2 = r2.lower()
        if r2 == "europa":
            l "That's right!"
            l "Lets try out the next riddle."
            jump chinese_riddle_third
        else:
            $ riddle_loop -= 1
            l "Hmm, not exactly who I was thinking about.
            Would you like to try again or have me give the answer?"
            $ rw2 += 1
            jump cafe_riddle_menu

    label chinese_riddle_third:
        l "The musical barterer returned empty-handed from the underworld."
        n "Lilith pauses for a moment."
        l "So, do you have an idea who I could be talking about?"
        if persistent.r3_knowledge == True:
            n "You remember Lilith telling you the answer was Orpheus."
        $ r3 = renpy.input("Place your guess here")
        $ r3 = r3.strip()
        $ r3 = r3.lower()
        if r3 == "orpheus":
            l "That's right!"
            jump chinese_riddle_evaluation
        else:
            $ riddle_loop -= 1
            l "Hmm, not exactly who I was thinking about.
            Would you like to try again or have me give the answer?"
            $ rw3 += 1
            jump cafe_riddle_menu

    label chinese_riddle_evaluation:
        $ rw_total = rw1 + rw2 + rw3
        if rw_total == 0:
            l "Wow, you got them all right, color me impressed!"
            if persistent.r1_knowledge == False and persistent.r2_knowledge == False and persistent.r3_knowledge == False and NMdetect == False:
                            $ Mdetect = True
        else:
            $ NMdetect = True
            if rw_total == 1:
                l "Only one riddle wrong, not shabby at all!"
            elif rw_total <= 3:
                l "You did pretty great, you gave it your best shot!"
            elif rw_total <= 5:
                l "You are pretty determined, I like that!"
            elif rw_total >= 6:
                l "Oh, did I make my riddles too hard?"

        l "What did you think of my riddles [name]?"
        menu:
            "You call those riddles? They were way too easy. Even a pre-schooler could answer them." if rw_total == 0:
                $ easy_rude = True
                jump chinese_riddle_easy

            "They were pretty fun! I didn't have a hard time with them and yet still had to think about them." if rw_total == 0:

                jump chinese_riddle_easy

            "They were pretty well made, I like them a lot!":
                jump chinese_riddle_good

            "The riddles were really hard to be honest with you." if rw_total > 0:

                jump chinese_riddle_hard

            "How was I ever supposed to get those riddles? You made them way too hard. Not everyone has a degree in Folklore & Mythology" if rw_total > 0:
                $ hard_rude = True
                jump chinese_riddle_hard
    label chinese_riddle_easy:
        if easy_rude == True:
            n "Lilith seems to be very saddened by your remark."
            n "She just looks at the table for a second and then speaks again."
            l "Oh I see..."
            l "I was fearing that I might had asked you some impossible questions."
            l "So atleast that wasn't the case."
            l "{size=*0.5}But you didn't have to act so high and mighty about it [name]...{/size}"
            $ love_points = -2
            $ love_meter_updater()
        else:
            l "Oh phew, what a relief!"
            l "I was kind of scared that I made my riddles too hard."
            l "But you handled them like a champ!"
            l "Have you ever learned about Greek and Roman myths before?"
            if persistent.chineseRiddlesSeenXTimesCounter >= 1:
                n "I suppose you did, didn't you player?"
                n "Who knew that timeloops could be so educational?"
            #TODO: Also make this a jump to a choice because this choice is asked twice in this part I think.
            
        jump chinese_riddle_railroad
    label chinese_riddle_hard:
        if hard_rude == True:
            $ love_points = -2
            $ love_meter_updater()
            l "Oh I suppose they are quite hard..."
            l "{size=*0.5}But did you have to say it so rudely?....{/size}"
            
        else:
            l "I see, that makes total sense [name].
            Sometimes I forget that not everyone is as into Greek and Roman myths as I am.

            I hope you had fun trying to find the answers though!"
        jump chinese_riddle_railroad
    label chinese_riddle_good:
        l "I'm really happy to hear that you liked them!"
        l "I was kind of scared that I might have made them too hard."
        #TODO: Add some varying text from here based on how many times you had to try.
        if rw_total == 0:
            l "But you seem like a natural with riddles. Have you ever learned about Greek and Roman myths before?"
            if persistent.chineseRiddlesSeenXTimesCounter >= 3:
                n "I guess you did in your previous attempts here, didn't you?"
                n "Does that mean this game needs an educational tag?"
        else:
            l "But you seem to like a challenge." 
            if persistent.lildeaths >= 9:
                n "Perhaps that is why you keep retrying?"
                n "Just to see if you can somehow win?"
                n "I'm curious if you will, I suppose I would do good to keep an eye on your progress."
        jump chinese_riddle_railroad

label chinese_riddle_railroad:
    #TODO: Make this dialogue vary based on the amount of love points she has in her meter. (That way if you insult her she will be a lot less sweet, and the situation will be very awkward.)
    l "You know, I thought it was kind of funny that you brought me here."
    l "Don't get me wrong, I really enjoy like it here but my sister, Abigail, adores this places."
    l "Since mom and me took her here for her twelfth birthday she insisted on coming again for five years in a row."
    l "She would always pick the orange chicken, it really was her favourite."
    #In the rude route she tells you this but a bit more rude, you get the option to shit on the restaurant (verbally, not literally)
    menu:
        "She sounds nice, can you tell me more about her?":
            n "Lilith gives you a big smile."
            l "Sure, what would you like to know?"
            menu:
                "What is the funniest memory the two of you share?":
                    jump chinese_riddle_talk_abbyMemory

                "What does she like to do?":
                    jump chinese_riddle_talk_abbyHobbies


label chinese_riddle_talk_abbyMemory:
    if persistent.tracker == 2:
        $ persistent.tracker2 = True
    #The code above this works for an easteregg
    l "I think I have a story you'll find quite funny, just stop me when I'm talking too much alright?"
    l "Abigail was like five years old at the time of our story.
    One night she shook me until I was awake, we used to share a bedroom with a bunk bed."
    l "She told me she heard whispering and laughing coming from underneath our bed and begged me to go investigate it."
    l "I told her it was probably nothing and tried to go back to sleep but she wouldn't stop begging so I eventually gave in since I didn't want to wake the others."
    l "As I stood before the dark opening underneath the bunk bed I felt as if something was watching me. But monsters didn't exist, right?"
    l "Right when I was thinking that I heard something whisper.
    I was terrified but as Abby's big sister I couldn't let her know I was so I tried to compose myself as best as I could and looked underneath the bed."
    l "It was pitch-black so I decided to put my head fully underneath the bed, alongside with my right arm.
    My hand brushed against something soft and just as I grabbed it laughter came from underneath the bed."
    l "I jumped back out, utterly terrified, nearly bursting out in tears.
    In my hand I held a pink bear, Abby's favourite toy, Mr. bunfluff."
    l "Apparently he was causing all that ruckus, his voicebox was slightly malfunctioning ."
    l "It's extremely amusing to picture how a pink bear scared the crap out of two little girls, it even was funny back then.
    I remember laughing with her about the whole ordeal for what must've been another hour or so before going to sleep."
    $ persistent.bedcheck_knowledge = True
    menu:
        "It sounds like you really care for your little sister.":
            l "Of course! I love her with all of my heart!
            ... I just don't want to lose her, you know?"
            n "Lilith gives you a saddened look."
            menu:
                "I understand, I also know someone I wouldn't want to lose but it seems like I am always on the verge of losing her." if persistent.lildeaths > 0:
                    n "Lilith tries her best to give you a comforting smile and she half-succeeds."
                    l "I also sometimes feel like I will lose Abigail. When that happens I always try to give it my all so that that won't happen."
                    l "If your situation with the person you mentioned is even slightly similair I'm sure you'll figure something out."
                    if persistent.lildeaths < 4:
                        "Lilith's words fill your heart with hope, maybe there is a way to save her. "
                    
                    elif persistent.lildeaths <= 7:
                        "You are not sure if you can figure something out to save Lilith but you have to try it, for her."
                    
                    else:
                        "You try to hold back your tears as to not alert her to something being wrong. You have seen her die so many times.
                        Reliving her deaths over and over while only being able to slightly change the way to inevitably reach  them again is really messing with you."
                    jump chinese_phoneScene
                "Have you already lost someone close to you?":
                #Give the player the ability to say "Like James?" if he has learned about him. Then you can tell her that you heard about it when it happened since it is a small town but Lilith will say that her mom, abby and her moved away from her hometown so that you couldn't know.
                    l "...
                    Is it that obvious?"
                    menu:
                        "Well, everybody has lost someone before. I just kind of asumed...":
                            n "Lilith lets out a small, slightly uncomfortable, laugh."
                            l "I suppose you are right."
                            n "Lilith begins to tear up."
                            menu:
                                "Do you want to talk about it? ":
                                    l "I'd rather not honestly..."
                                    menu:
                                        "That's fine, if you ever want to talk about it you can always give me a call.":
                                            n "She gives you a slight smile."
                                            l "No offence [name] but you got to admit that I barely know you.
                                            Isn't it pretty weird to tell you about it?"
                                            menu:
                                                "It can feel good to confide in strangers, it's not like they are going to know who to tell your secrets to.":
                                                    jump chinese_lostSomeone_confideStranger
                                                "Then ask me a few questions to not make me a stranger anymore.":
                                                    jump chinese_lostSomeone_questions

                                                "This might sound strange but I feel as if I've already known you for a lot longer than I actually do.":
                                                    "Filler"
                                                    #TODO: Fill this in and make this only appear if you have around 6 times reset.
                                                    #Make her more likely to admit feeling that way aswell if you have high lovepoints.
   
label chinese_riddle_talk_abbyHobbies:
    n "Lilith chuckles slightly."
    $ persistent.quest_knowledge = True
    #Does this still make sense if I'm using renpy to make the game?
    l "Alright, here I go, just stop me when I begin to ramble on too much."
    l "She really likes to make all kinds of stuff, right now it's mostly games.
    She can't really code much so she uses Quest, it's a program that makes it easier to make textbased games."
    l "She makes tons of those games but barely manages to finish them.
    Even is she finishes them eventually, she almost never does anything with them."
    l "She asks me to play a select few of those that get finished every now and then, they are not really complex at the slightest but I always find them strangely intriguing nontheless."
    menu:
        "What do you find interesting about her games?":
            l "Well for one, games made by a small team or even one person are almost an imprint of what those people were thinking right when they made their project."
            l "Two of Abby's games especially seem like they have something to say about her as a person."
            n "Lilith pauses for a moment before continuing"
            l "In the first game you play as someone who has to feed a prisoner.
            You are discouraged from talking to the prisoner by someone who speaks in red text.

            A textbox appears and upon typing something the prisoner responds..."
            l "It's here where things begin getting a bit... special."
            l "The prisoner begins to speak absolute nonsense no matter what you decide on typing into the textbox.
            The text coming from them is dark blue."
            l "They seem oddly happy to see you and yet they pay no attention to you at all."
            l "It's only one voice in there but they always refer to them as if there are multiples.
            They keep going on and on about how you are speaking in a \"stolen voice\" and how no one wants to listen to you.
            And yet they keep begging you to speak, not because they listen to you or understand your words but because they like the color of your text, light green."
            l "The prisoner keeps talking, mostly insulting you and commanding you to bow before them.
            After what felt like probably ten minutes of pure nonsense reactions to my input another voice began to speak."
            l "That voice was dark green,
            It also didn't really pay attention to what I was saying but the prisoner also didn't seem to notice the other voice.
            It kept calling out for help, repeatedly."
            l "I tried typing just the word \"help\" in the textbox, suddenly the door opened.
            A link appeared, if you clicked it you would enter the room so I did, I wanted to know who was talking to me this entire time."
            l "There was no one there...
            Suddenly the door shut and I was locked inside.

            After a while you begin speaking the same nonsense as the prisoner, in dark blue aswell.
            That's when the game ends abruptly and turns to black."
            l "Oh, I've been talking longer than I thought I would, maybe it's better to not talk about the other game then.
            What do you think [name]?"
            menu:
                "I don't mind at all, tell me about the second game if you want.":
                    l "The second game is a lot bigger in the scope of the location.
                    It's about a ravenprince who needs to climb a mountain with his wings bound together."
                    l "On his way the raven constantly meets new characters."
                    l "A cow called Io that believes she is a cow because some farmers told her so and eventually turns into a raven when she talks to the ravenprince."
                    l "A snake that keeps accidentally eating her own tail because she is confused, after freeing her she just starts once again."
                    l "A humanoid shadow with a rectangle for a head that dissappears every time you try to talk to it."
                    l "A three headed statue of a woman, each head speaks a different language. They speak Dutch, English and French respectively but neither of them seems to be able to make coherent sentences"
                    l "An old man that keeps walking in circles and who has gold coins where his eyes should be."
                    l "All of those characters discourage you from climbing the mountain, all of them except for the most important character of them all from what I could understand.
                    They are a saphire being that hugs the raven and tells them they are forgiven."
                    l "Upon being told that they black out and awaken at the foot of the mountain as if their entire climb didn't really happen."
                    l "I must have \"completed\" that game atleast ten times, every time was exactly the same no matter wheter I picked different choices or not."
                    l "You know, I'm not sure what those games actually mean.
                    What do you think?"
                    label chinese_abby_game_theme:
                        menu:
                            "The theme seems to be about loops.":
                                jump chinese_abby_game_theme_loops
                            "There seems to be no theme, it's just pure nonsense.":
                                jump chinese_abby_game_theme_nonsense


                                label chinese_abby_game_theme_loops:
                                "You might be onto something!
                                The feeder becoming the prisoner and the raven climbing the mountain again and again, those things are cleary loops.
                                But what does that mean?
                                Why would Abby put that premise in two of her games?"
                                menu:
                                    "Maybe she just likes the concept of loops?":
                                        n "Lilith lets out a small chuckle."
                                        l "Who knows? Maybe that's all there is to it."
                                        n "Lilith grows more somber and begins to slightly frown."
                                        l "And yet I can't shake the feeling that there is something going on with her, something I'm not noticing."
                                        l "There's this voice in my head that keeps telling me I'm not good enough, that I failed her and that I destroy everything I touch."
                                        l "I would love to tell you that I didn't believe that voice in the slightest but that would be a lie."
                                        l "I don't want to lose her [name], I can't go through all of that again."
                                        l "Tears begin streaming down her face as she looks at you with a defeated look in her eyes."
                                        menu:
                                            "I know that voice is hard to ignore but for whatever it is worth, I really like you Lilith.":
                                                "Filler"
                                                #TODO: This dialogue does not yet exist, make it.
                                                jump chinese_phoneScene

                                            "That voice is just self-doubt, you are more than good enough Lilith.":
                                                l "Do you really believe that, [name]?"
                                                menu:
                                                    "Absolutely! It might sound weird but I really feel like I've gotten to know you well even if this is our first date and you really are a good person." if persistent.burger_death_1 and persistent.cafe_death_1 == True and persistent.chinese_death_1:
                                                        jump chinese_abby_selfdoubt_knowYouWell
                                                    "I do but I think you are the one who needs to believe that for it to work.":
                                                        jump chinese_abby_selfdoubt_IDo
                                               




label chinese_abby_game_theme_nonsense:
    l "Hmm, do you really think so?"
    n "Lilith softly scratches her head."
    l "It's hard to believe that something could ever be just pure nonsense and nothing else.
    You have to pull the ideas you use to make a game or something else from somewhere, right?"
    l "I'd like to think that even if someone would try to make a game that is just pure nonsense that atleast some aspects of meaning would seep into it."
    l "Afterall, the medium is the message."
    l "So is it possible to create and form something without meaning even slightly implied?"
    l "Sorry if I'm boring you, it's just something I've been thinking about for a while now."
    menu:
        "You are not at all, this is actually very interesting.":
            n "Lilith's face lights up with pride for a moment as she lets out a giggle."
            l "You know, if you want to we could talk about it a little more."
            jump chinese_phoneScene

        "This is very interesting although I can't really wrap my head around it.":
            n "Lilith gives you a cute giggle."
            l "No worries, my ramblings are pretty hard to understand sometimes, thanks for listening either way [name]!"
            jump chinese_phoneScene

label chinese_abby_selfdoubt_IDo:
    n "Lilith chuckles with a pained expression painted on her face."
    l "I suppose you are right.
    I need to believe that I'm a good person, otherwise it would just be empty praise coming from someone I barely met."
    n "Lilith tries her best to give you a smile, you can tell it's slightly forced."
    l "No offence [name]! I like how our date is going so far, even though I am messing it up pretty badly right now, but this is our first date afterall."
    jump chinese_phoneScene

label chinese_abby_selfdoubt_knowYouWell:
    n "Lilith wipes away some tears as she gives you a big smile."
    l "Thank you [name], I'd like to know you the same way you seem to know me.
    I know it is strange but somehow I can see in your eyes that you truly seem to know me quite well already."
    jump chinese_phoneScene




label chinese_lostSomeone_confideStranger:
    n "Lilith scratches her head and gives you a nice smile."
    l "I suppose you are right, I might take you up on that offer eventually."
    n "You are not really sure if she means it."
    jump chinese_phoneScene
label chinese_lostSomeone_questions:
    n "Lilith begins to laugh."
    l "I'm not sure it really works like that [name].
    I can't really think of any combination of questions that would make me feel like this isn't our first date.
    You get to know someone over the span of all your time together, not by seeing them one time."
    n "But thanks for the sugestion either way!"
    l "Lilith gives you a cute little smile."
    jump chinese_phoneScene
label chinese_phoneScene:
    l "I'll be right back [name], I just need to go to the bathroom real quick."
    n "Lilith stands up from her chair and pushes it back under the table."
    n "As she enters the bathroom stall you see that she has forgotten her phone, it is still laying on the table."
    if persistent.lildeaths >= 7:
        if persistent.peeked_phone == True:
            n "You've already done it before, you might aswell do it again, right?"
            n "After all, this might help give you another lead on how to solve all of this."
            n "Is that what you are thinking? That she won't remember any of this so that it doesn't matter?"
            n "Go on. I won't stop you, not as long as this remains my story."
        else:
            $ nopeek = True
            n "You know it isn't right to do but maybe you could find a way to save her on her phone.
            If there is even the slightest chance that it will help her you owe it to her to try that out, right?"








    menu:
        "Take a quick peek at her phone.":
            jump chinese_phone_peek
        "Respect her privacy.":
            jump chinese_phone_noPeek

label chinese_phone_peek:
    n "As you open her phone you are greeted by a picture of a pug as the phone's background and a prompt.
    The prompt says \"Enter password\". "
    if persistent.pass_knowledge == True:
        n "You remember that her password is 81155"
    else:
        n "Suddenly it dawns on you that you do not know what Lilith her password is."
        $ persistent.need_pass_knowledge = True
        menu:
            "*Put the phone back.*":
                n "You put the phone back and try to act as natural as you can."
                n "You quickly glance around the restaurant to see if anyone might have caught you trying to check her phone."
                n "Everyone seems to be too busy enjoying their food to pay you any attention. You are saved by the excellent cuisine."
                n "Just as you let out a sigh of relief Lilith comes back to your table."
                l "Hey [name], I'm back."
                l "Did they not yet bring our food?"
                l "That's okay, I'm just really looking forward to it, the food here is to die for."
                if persistent.chinese_death_1 == True:
                    n "It indeed seems to be that way doesn't it [name]?"
                n "You play along with Lilith, hoping she doesn't suspect what you just did."
                l "..."
                n "Lilith squints her eyes and seems to be lost in thought for a moment."
                l "Is everything alright [name]? You look pretty nervous."
                menu:
                    "Uhm yeah, I'm totally fine. (Lie)":
                        n "Lilith squints her eyes slightly and looks at you with an almost soul-piercing look in her eyes."
                        $ love_points = -1
                        $ love_meter_updater()
                        l "Hmm, alright [name], if you say so."
                        n "You have to stop yourself from shaking in your seat, did she buy that lie? The alternative gives you so much fear that you try to convince yourself that she did."
                        n "Anyway, it's best to just move on now, you told the lie, you can always choose to not lie to her from now on, right?"
                        jump chinese_phone_noPeek


                    "I'm just a bit nervous about this date to tell you the truth. I just don't want to mess this up and lose you. (Half-truth)":
                        if love_meter >= 2:
                            l "Oh [name], I had no idea you felt that way! That's completly okay, I'm glad you told me."
                            l "To be entirely honest with you aswell I feel the same way."
                            l "This has been my first date in quite a while and I'm having a really good time."
                            l "So it would be a shame if I somehow lost this."
                            l "But right now we're both still here, right? So we should probably make the most out of it together."
                            n "Lilith gives you a cute smile."
                            n "You feel guilty for lying to her, because even if it was a half-truth, that still means it's a half-lie."
                            n "You try to ignore that feeling and just try to get the most of your remaining time with her."
                            jump chinese_phone_noPeek
                        else: 
                            l "Oh, I see."
                            l "{size=*0.5}That actually might explain some of your behaviour...{/size}"
                            l "{size=*0.5}Although it's definetly no excuse.{/size}"
                            l "Is that why you are acting quite \"tough\" [name]?"
                            l "If I can give you a small piece of advice, I don't really like being treated like that."
                            l "You seemed way nicer to me when we first talked about arranging this date. So I know there's someone nice underneath that mask you are wearing."
                            l "Just allow yourself to relax a bit and enjoy your time with me here, alright?"
                            l "You don't have to prove yourself to me. After all, I came here to go on a date with you, didn't I?"
                            n "Lilith flashes you a cute smile, you can see some slight worry in her eyes."
                            n "What affects you the most is that the worry does not seem to be for herself, it seems to be for you."
                            menu:
                                "I... I guess you're right. Sorry for that Lilith. I'm sorry if I hurt you by trying to act more tough.":
                                    l "It's alright [name]! I won't pretend that you didn't hurt me at all, but apoligizing is a good first step."
                                    l "I know it can sometimes be difficult dealing with insecurities, and sometimes they can manifest in ways that harm ourselves and other people."
                                    l "Just know that if you feel a thought like that pop up again you can always try to talk to me about it, alright?"
                                    l "I've been going through something similair a while ago and I find that talking it through really tends to help."
                                    l "I won't pretend that that fixes it completely, I'm even still sometimes dealing with it."
                                    l "But it helps me to control my own insecurity a little better."
                                    menu:
                                        "Thank you for being so patient with me. That means a lot.":
                                            n "Lilith gives you a cute smile."
                                            l "Hey, don't mention it [name]. I know I wouldn't be the same person I am now if a lot of people didn't have patience with me."
                                            l "I'm just glad that I was able to get through to you."
                                            jump chinese_phone_noPeek
                    "Okay, I'll be honest. I was going through your phone to attempt to learn more about you. But I have a good reason!":
                        menu: 
                            "I need to save you. You are repeatedly dying over and over in some sort of loop.":
                                l "Nope, I'm not having any of this [name]. First you go through my phone, without my consent, and then you make up some crazy argument to justify your action?"
                                l "Even if you think that thing about saving me is true, you have to see how going behind my back to do so is really not the way to do it, right?"
                                $ angryLilith = True
                                $ love_meter_updater(True)

            "*Try a code anyway.*":
                jump chinese_phone_peek_code
    label chinese_phone_peek_code:
        $ phonecode = renpy.input("Enter the password", length=5)
        $ phonecode = phonecode.strip()
        if phonecode == "81155":
            n "The code is correct."
            if persistent.pass_knowledge == False:
                n "... How did you know that? You haven't seen that code in this game yet, right?"
                n "Did you look the answer up online?"
                n "Or did you play this game before?"
                n "If it's the latter I'm flattered that you came back but if it's the first I'd like for you to engage with my puzzles more."
                n "Although, I suppose you were atleast engaged enough to keep playing and didn't give up..."
                n "Forget I said anything."
                n "Just promise me you'll try to look for the answers yourself first before looking stuff up, alright?"
            if persistent.passWrongOnPurpose_narratorRant == True:
                if persistent.passWrongOnPurpose_narratorRant_wrongTimesInARowCounter >= 5:
                    n "... Wait, you entered the right password? I forgot how it felt to have that happen."
                    n "I'm so happy I finally get to narrate something different."
                    n "Let's just forget that torture ever happened at all and move on to with the story."
                $ persistent.passWrongOnPurpose_narratorRant_wrongTimesInARowCounter = 0

            jump chinese_phone_peek_numbers
        else:
            n "Wrong password."
            if persistent.pass_knowledge == True:
                #TODO: Add a line here where it just says: Again? each time you see this text again.
                if persistent.passWrongOnPurpose_narratorRant == False:
                    n "Wait, that can't be right."
                    n "You knew the password, right?"
                    n "I even told you what it was in case you would have forgotten it."
                    n "Did you just want to see the scene where you get caught once again?"
                    n "I guess you win, I can't afford to derail this story even more, not for something so minor."
                    n "I'll just jump forward to that scene and then we can all pretend nothing happened."
                else:
                    
                    n "Again?"
                    n "Fine, as you wish."
                    if persistent.passWrongOnPurpose_narratorRant_counter == 1:
                        n "Just enter the right code next time, alright?"
                    elif persistent.passWrongOnPurpose_narratorRant_counter == 2:
                        n "You're really going to keep doing it aren't you?"
                    elif persistent.passWrongOnPurpose_narratorRant_counter <= 5:
                        n "Can you stop that please?"
                        if not persistent.beachroute_visited_knowledge:
                            n "You're not going to make any progress like this, can't you do something that will actually move the story further?"
                        else: 
                            n "I get that you're starved for more story but this can hardly be called story at this point, right?"
                            n "You just get an extra dialogue line, two if you're lucky."
                            n "Is that really worth all of this to you?"
                    else:
                        if persistent.passWrongOnPurpose_narratorRant_wrongTimesInARowCounter > 1:
                            if persistent.passWrongOnPurpose_narratorRant_counter !== persistent.passWrongOnPurpose_narratorRant_wrongTimesInARowCounter:
                                n "You've been doing this [persistent.passWrongOnPurpose_narratorRant_counter] times now, your current streak is [persistent.passWrongOnPurpose_narratorRant_wrongTimesInARowCounter]."
                            else:
                                n "Really?"
                                n "You're just going to keep doing this?"
                                n "You have a streak of [persistent.passWrongOnPurpose_narratorRant_wrongTimesInARowCounter] now, you didn't stop once since you started getting the answer wrong on purpose."
                                n "At this point I'm wondering if this is just a personal attack against me or something."
                            n "That's right, I'm keeping track."
                            n "And still, no matter what you do, this will always end the same way."
                            n "So why do you keep coming back?"
                $ persistent.passWrongOnPurpose_narratorRant_counter += 1
                $ persistent.passWrongOnPurpose_narratorRant_wrongTimesInARowCounter += 1 
                jump chinese_phone_caught
            n "You try to input a few other codes to see if those work instead."
            $ phone_wrongPassword_graceSystem = renpy.random.randint(1,80)
            $ phone_wrongPassword_graceSystem += (persistent.retry_counter* 10)
            if phone_wrongPassword_graceSystem == 100:
                n "Avoiding the previous wrong passwords you remember from your previous attempst you manage to somehow luck yourself into typing the correct password after a couple of tries."
                n "It is 81155."
                $ persistent.pass_knowledge = True
            else:
                n "None of the other codes seem to result in anything either. You are not sure how many you tried, you decide to close the phone in case Lilith will come back."
            jump chinese_phone_caught







label chinese_phone_caught:
    if peeked_phone_temp == True:
        $ persistent.peeked_phone = True
        if persistent.playerCalledAbigail == False and persistent.playerCalledDavid == False and persistent.playerCalledJames == False and persistent.playerCalledLila == False:
            n "You think you sucessfully memorised the phone-number, I guess only time will tell.
            Because if you've already gone this far you will only go further, right?"
            
        else:
            if persistent.restrainingorderfamily_knowledge == True:
                n "You succesfully memorised the number of the next person you are going to involve into this whole mess, the exact thing Lilith asked you not to do."
                n "How do you think that would make her feel if she knew?"
            else:
                n "You succesfully memorised the number of the next person you are going to involve into this already way too complicated situation."
                n "Do you really think that that's a good idea?"
    n "No need to answer that, it was rhetorical. What you need to do is to close that phone."
    n "Right at the moment when you close the phone and look back up you can see Lilith approaching."
    n "Another thing you can also see is the very angry expression on her face."
    n "As she walks up to the table she grabs her phone and puts it in her handbag"
    l "What you just did was inexcusable [name]. I really didn't expect this from you."
    l "I'm leaving, you can pay for our meals or try and cancel them but I am sticking up for myself."
    l "Goodbye and do not ever contact me again."
    if persistent.chinese_phone_noretry == True:
        n "And yet here you are once again, making the same mistake you've already made. And Lilith is none the wiser."
        n "Is that why you came back to do the same thing she told you she didn't want you to do? Would you have acted differently if she could remember every action you took?"
        n "Don't worry [name], this is just all a game, right? Your actions here don't mean anything at all, right?"
        n "..."
    else:
        $ persistent.chinese_phone_noretry = True
    jump car_death

label chinese_phone_noPeek:
    n "You didn't peek, this will just continue the events like they are meant to play out."
    #TODO: Make those events play out properly, don't just cut to the death.
    jump restaurant_death_1

label chinese_phone_peek_numbers:

    n "You see the family section of her phone numbers, four names are listed there."
    if persistent.restrainingorderfamily_knowledge == True:
        n "You remember that Lilith told you to not involve her family."
        n "She probably wouldn't appreciate this."
        n "But then again, it could really help you out in the long-term."
        $ restrainingorderfamily_violation_counter += 1
    else:
        n "If anyone besides Lilith will have some handy information about her it's them."
        n "You might just have enough time to learn one phone-number."

    $ peeked_phone_temp = True
    menu:
        "Learn Abigail's phone number." if not persistent.abigail_call_knowledge:
            $ persistent.abigail_call_knowledge = True
            jump chinese_phone_caught
        "Learn David's phone number." if not persistent.david_call_knowledge:
            $ persistent.david_call_knowledge = True
            jump chinese_phone_caught
        "Learn James' phone number." if not persistent.james_call_knowledge:
            $ persistent.james_call_knowledge = True
            jump chinese_phone_caught
        "Learn Lisa's phone number." if not persistent.lila_call_knowledge: 
            $ persistent.lila_call_knowledge = True
            jump chinese_phone_caught
        "Put the phone back." if persistent.abigail_call_knowledge and persistent.david_call_knowledge and persistent.james_call_knowledge and persistent.lila_call_knowledge:
            $ restrainingorderfamily_violation_counter -= 1
            jump chinese_phone_caught




label chinese_riddle_decline:
    l "No worries at all [name]!"
    l "Maybe you'd like giving me some riddles instead?"
    menu: 
        "Sure, that sounds good!":
            #TODO:  Make the riddles push you back on track to the normal stuff eventually.
            menu:
                "What has four legs in the morning, two legs at noon and three legs in the evening?":
                    l "Ah that's a real classic! The answer is humans. The question originated from the myth of Orpheus if I'm not mistaken."
                    l "I didn't know you were into mythology [name], that's really cool!"
                    menu:
                        "Thanks Lilith! From your response I gather you are also into mythology, right?":
                            l "Oh absolutely!"
                            l "I practically live and breathe mythology."
                            l "Ever since I was a little girl I just had a massive interest in all kinds of stories, then later my interest started to grow more towards myths when I revieved my first book about Greek and Roman myths."
                            l "And now recently I've been also interested in some other mythology. Right now I'm reading more about Finish mythology, the Kalevala to be specific."
                            l "That's why I'm happy to meet someone likeminded like you [name]!"
                            #TODO: Add a bit more text?
                        "Actually I just found that riddle on the internet a while back.":
                            n "Lilith looks slightly disappointed."
                            l "Oh... that's alright [name], I guess sometimes I forget that that riddle is practically used everywhere now."
                            l "Tons of movies, books and games now kind of use that riddle as a placeholder because it's so well known. It's the \"lorum ipsum\" of riddles."
                            n "Hey, is she complaining about my ability to write riddles? Uhm, I mean your ability to make riddles."
                            l "But still, thank you for your riddle! Regardless of how many times it has been used, it's still remains a clasic."
                            l "And I think you must've thought so aswell since you can still remember it after you first read it online."
                "What has five teeth, twelve eyes, four arms and a thousand legs?":
                    l "..."
                    n "Lilith scrathes her head, deep in thought."
                    l "I don't know [name], that's a really tough one."
                    l "What is the answer?"
                    menu:
                        "Well, the answer is that I don't know either.":
                            n "Lilith gives you a confused look before it all clicks and she burtst out in laughter."
                            l "You sure got me there [name]!"
                            l "Although, if you don't know the answer, and that is the answer, doesn't that mean that you know the answer?"
                            n "You are not entirely sure what she means."
                            n "Apparently Lilith must have been able to read just that from your face as she immediately turns beet-red and tenses up a bit."
                            l "I'm sorry, that was way too much for a first date wasn't it?"
                            l "I didn't mean to sound like a know-it-all."
                            l "Please just forget what I said, alright [name]?"
                            menu:
                                #TODO: Fill in.
                                "I don't mind at all Lilith, you just kind of threw me for a loop with what you just said. It does sound interesting though.":
                                    n "Lilith lets out a sigh of relief as she relaxes a bit more once again."
                                    l "I already was fearing the worst."
                                    l "A lot of people have told me that I come off as info-dumping way too much, especially when I get to know someone at first."
                                    l "It's just that I love to think about things a lot, especially if they fascinate me."
                                    l "And I enjoy sharing those thoughts, it's just, most people don't seem to enjoy listening to them."
                                    l "So thank you [name], now I know that I can release my full arsenal on you!"
                                    n "Lilith let's out a mischevious little chuckle."
                                    l "I'm only joking, I wouldn't want you to run away from me after all."
                                    #TODO: Add this line if she ever left you/ran away: n "Usually when it comes to running away it's the opposite way, isn't it player?"
                                    menu:
                                        "Running away? From such good company? I would never forgive myself of that.":
                                            n "And just like that she turns completely beetred once again."
                                            l "{size=*0.5}Uhm...uhm... uhm...{/size}"
                                            n "She covers her face for a short moment, takes a deep breath in and then continues."
                                            l "My, you are quite a flatterer aren't you?"
                                            l "But seriously, that means a lot to me, to hear that you consider me good company."
                                            l "Normally I probably wouldn't tell you that, but I'm trying to become a bit more direct lately."
                                            l "..."
                                            #TODO: Show the below line only if her love is high enough.
                                            l "You know, for what it is worth, I also really like your company [name]."
                                            l "I'm having a really good time here with you so far."
                                "Sure thing, if that's what you want. *Talk about something else.":
                                    "Filler"
                                    #TODO: Give like a few very lightweight questions and answers here before she moves on to something else.
                "A man is in a metal room without a door and with a barred window. How does he leave?":
                    l "Hmm, that seems to be a tough one, let me think about it for a second [name]!"
                    n "Lilith seems to happily be going through potential solutions."
                    l "{size=*0.5}Maybe he needs to do something with the window?{/size}"
                    l "{size=*0.5}But it's barred...{/size}"
                    l "{size=*0.5}Then again, it must have to do something with the window, right?{/size}"
                    l "{size=*0.5}After all, there is no door.{/size}"
                    l "{size=*0.5}But then how did he get in?{/size}"
                    l "{size=*0.5}Wait a second...{/size}"
                    l "I think I got the answer!"
                    n "She is practically bouncing on her seat as she is saying this."
                    l "I think the answer is that there is no door but there is a doorframe!"
                    l "So that means he just has to walk out through there."
                    l "Did I get it right?"
                    menu:
                        "Yes you did, great job Lilith!":
                            n "Lilith fist pumps the air."
                            l "Yes! That was a very fun riddle [name], not what I was expecting but it forced me to think outside the box a little bit."
return
