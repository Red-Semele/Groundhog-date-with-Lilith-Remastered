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
                        #TODO: Add extra text here, to make the "the answer is "x" not feel so robotic.
                            if rw3 == 0:
                                if rw2 == 0:
                                    if rw1 == 0:
                                        "Error, you are not supposed to be here or something went wrong."
                                    else:
                                        $ persistent.r1_knowledge = True
                                        l "The answer is Arachne."
                                        l "Let's move on to the next riddle."
                                        jump chinese_riddle_second
                                else:
                                    $ persistent.r2_knowledge = True
                                    l "The answer is Europa."
                                    l "Let's move on to the next riddle."
                                    jump chinese_riddle_third

                            else:
                                $ persistent.r3_knowledge = True
                                l "The answer is Orpheus."
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
            if persistent.r1_knowledge == False and persistent.r2_knowledge == False and persistent.r3_knowledge == False and NMdetect == False: #TODO: Does this work? Check it out.
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
        #TODO: Make these only appear at certain points. Add some extra text on each path to make for better segways.
        #Also change the text between brackets.
        menu:
            "They were pretty easy actually. (Rude version)" if rw_total == 0:
                $ easy_rude = True
                jump chinese_riddle_easy

            "They were pretty easy actually. (Non-rude version)" if rw_total == 0:

                jump chinese_riddle_easy

            "They were pretty well made, I like them a lot!":
                jump chinese_riddle_good

            "The riddles were really hard to be honest with you." if rw_total > 0:

                jump chinese_riddle_hard

            "How was I ever supposed to get those riddles? You made them way too hard." if rw_total > 0:
                $ hard_rude = True
                jump chinese_riddle_hard
    label chinese_riddle_easy:
        if easy_rude == True:
            #TODO: Fill in the rude path here.
            l "Oh I see..."
            l "I was fearing that I might had asked you some impossible questions."
            l "So atleast that wasn't the case."
            l "{size=*0.5}But you didn't have to act so high and mighty [name].{/size}"
            $ love_points = -1
            $ love_meter_updater()
        else:
            l "Oh phew, what a relief!"
            l "I was kind of scared that I made my riddles too hard."
            l "But you handled them like a champ!"
            l "Have you ever learned about Greek and Roman myths before?"
            #TODO: (Make the narrator say that you had in the previous loops at the very least.)
            #TODO: Also make this a jump to a choice because this choice is asked twice in this part I think.
            
        jump chinese_riddle_railroad
    label chinese_riddle_hard:
        if hard_rude == True:
            $ love_points = -1
            $ love_meter_updater()
            l "Oh I suppose they are quite hard...
            But did you have to say it so rudely?..."
        else:
            l "I see, that makes total sense [name].
            Sometimes I forget that not everyone is as into Greek and Roman myths as I am.

            I hope you had fun trying to find the answers though!"
        jump chinese_riddle_railroad
    label chinese_riddle_good:
        l "I'm really happy to hear that you liked them!
        I was kind of scared that I might have made them too hard."
        l "I'm really happy to hear that you liked them!"
        #TODO: Add some varying text from here based on how many times you had to try.
        if rw_total == 0:
            l "But you seem like a natural with riddles. Have you ever learned about Greek and Roman myths before?"
            #TODO: (Make the narrator say that you had in the previous loops at the very least.)
        else:
            l"But you seem to like a challenge." 
            #TODO:(Make the narrator mention that maybe that's why you keep coming back to this game.)
        jump chinese_riddle_railroad

label chinese_riddle_railroad:
    #TODO: Make this dialogue vary based on the amount of love points she has in her meter.
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
    if tracker == 2:
        $ tracker2 = True
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
        if peeked_phone == True:
            #TODO:Add some different text based on if you've reached a dead-end with the other numbers or not.
            n "You've already done it once, you might aswell do it again, right?
            Is that what you are thinking? That she won't remember any of this so that it doesn't matter?"
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
                "Filler"
                #TODO: Fill in this part. Make this still be salvageable, Lilith comes back and doesn't notice you were using your phone, she just seems to notice that something is up though.
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
            jump chinese_phone_peek_numbers
        else:
            n "Wrong password."
            if persistent.pass_knowledge == True:
                #TODO: Add a line here where it just says: Again? each time you see this text again.
                n "Wait, that can't be right."
                n "You knew the password, right?"
                n "I even told you what it was in case you would have forgotten it."
                n "Did you just want to see the scene where you get caught once again?"
                n "I guess you win, I can't afford to derail this story even more, not for something so minor."
                n "I'll just jump forward to that scene and then we can all pretend nothing happened."
                jump chinese_phone_caught
            n "You try to input a few other codes to see if those work instead."
            #TODO: Check if this works and write it out a bit better.
            $ phone_wrongPassword_graceSystem = renpy.random.randint(1,80)
            $ phone_wrongPassword_graceSystem += (persistent.retry_counter* 10)
            if phone_wrongPassword_graceSystem == 100:
                n "You manage to somehow luck yourself into getting the correct password."
                n "It is 81155."
                $ persistent.pass_knowledge = True
            #TODO: Add a random chance that you accidentally type in the correct password. The chance increases at each attempt. (This way you give the player a way to get the phone number in an alternate way.)
            #Never let it work the first time though.

            #This is the code for if you don't get the random chance:
            n "None of the other codes seem to result in anything either. You are not sure how many you tried, you decide to close the phone in case Lilith will come back."
            jump chinese_phone_caught







label chinese_phone_caught:
    if peeked_phone_temp == True:
        $ peeked_phone = True
        #TODO: Add some varying text the other times you take the phone.
        n "You think you sucessfully memorised the phone-number, I guess only time will tell.
        Because if you've already gone this far you will only go further, right?"
        #TODO: Make the narrator mention this the first time you call aswell.
        n " No need to answer that, it was rhetorical. What you need to do is to close that phone."
    n "Right at the moment when you close the phone and look back up you can see Lilith approaching.
    Another thing you can also see is the very angry expression on her face.
    As she walks up to the table she grabs her phone and puts it in her handbag"
    l "What you just did was inexcusable [name]. I really didn't expect this from you.
    I'm leaving, you can pay for our meals or try and cancel them but I am sticking up for myself.
    Goodbye and do not ever contact me again."
    if persistent.chinese_phone_noretry == True:
        #TODO: Make this text slightly different based on how many times you've went through her phone.
        n "And yet here you are once again, making the same mistake you've already made. And Lilith is none the wiser.
        Is that why you came back to do the same thing she told you she didn't want you to do? Would you have acted differently if she could remember every action you took?"
        n "Don't worry [name], this is just all a game, right? Your actions here don't mean anything at all, right?"
        n "..."
    else:
        $ persistent.chinese_phone_noretry = True
    jump car_death

label chinese_phone_noPeek:
    n "You didn't peek, this will just continue the events like they are meant to play out."
    jump restaurant_death_1

label chinese_phone_peek_numbers:

    n "You see the family section of her phone numbers, four names are listed there.
    If anyone besides Lilith will have some handy information about her it's them.
    You might just have enough time to learn one phone-number."

    $ peeked_phone_temp = True
    #TODO: For some reason this menu throws some lint errors.
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
        "Learn Lisa's phone number." if not persistent.lisa_call_knowledge: 
            #TODO: For some reason it does not think this flag is defined.
            $ persistent.lisa_call_knowledge = True
            jump chinese_phone_caught
        "Close the phone." if persistent.abigail_call_knowledge and persistent.david_call_knowledge and persistent.james_call_knowledge and persistent.lisa_call_knowledge: #TODO: Rewrite this line slightly.
            jump chinese_phone_caught




label chinese_riddle_decline:
    l "No worries at all [name]!"
    l "Maybe you'd like giving me some riddles instead?"
    n "You nod." #TODO: Rework this line slightly
    #TODO: Add one extra riddle.
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
                "Actually I found that riddle on the internet a while back and just kind of remembered it just now.":
                    "Filler"
                    #TODO: Fill in.
        "What has five teeth, twelve eyes, four arms and a thousand legs?":
            l "..."
            n "Lilith scrathes her head, deep in thought."
            l "I don't know [name], that's a really though one."
            l "What is the answer?"
            menu:
                "Well, the answer is that I don't know either.":
                    n "Lilith gives you a confused look before it all clicks and she burtst out in laughter."
                    l "You sure got me there [name]!"
                    l "Although, if you don't know the answer, and that is the answer, doesn't that mean that you know the answer?"
                    n "You are not entirely sure what she means."
                    n "Apparently Lilith must have been able to read just that from your face as she immediately turns beet-red."
                    l "I'm sorry, that was way too much for a first date wasn't it?"
                    l "Sometimes I just can't help myself and just say stuff like that way too soon."
                    l "Please just forget what I said, alright [name]?"
                    menu:
                        #TODO: Fill in.
                        "I don't mind at all Lilith, you just kind of threw me for a loop with what you just said. It does sound interesting though.":
                            "Filler"
                        "Sure thing, if that's what you want. *Talk about something else.":
                            "Filler"



return
