#Put all the deaths in here as a way to clean up all the other files and also just make this way easier to find deaths to rewrite etc.





label restaurant_deaths:
    label restaurant_1:
        label restaurant_death_1:
            if burger == True:
                #Burgerscene here
                n "Now the screaming is also paired with hellish sounds, just great. You look at [persistent.date] and tell her to hide under the table."
                l "I..."
                play music game_over
                n "[persistent.date] seems to be frozen, on her face you can clearly see a mixture of fear and confusion. It takes you a moment to notice the steadily increasing red stains on [persistent.date]'s clothes."
                l "I've been shot?"
                n "She falls of her chair, you crawl towards her and try to call an ambulance."
                n "With trembling hands you type the emergency-number and beg for help."
                n "Everything seems to fade away, even the continuous  barage of gunshots, all you can hear is the sound of [persistent.date]'s breathing as it grows weaker and weaker."
                n "You've been here for what feels like aeons but in all reality was probably 5 minutes when an ambulance finally arrives."
                n "A young man, with eyes that have grown old from all the things they saw, places [persistent.date]'s still body on a stretcher and rushes off with it to the ambulance."
                n "The kind man throws some words at you, he tells you that everything will be just fine but you both know that he is lying. You have seen her suffering for what seemed like an eternity and a second at the same time."
                n "You have no clue what caused all those gunshots that inadvertently killed her. Some robbery in a neighbouring store, or a gang war, or something else."
                n "But sadly you do know what the aftermath of it all is."
                $ persistent.burger_death_1 = True
                jump gameOver

            elif cafe == True:
                #Cafescene here
                n "Suddenly you hear someone scream, you can turn your head just quick enough to see someone fall with a plate in their hands."
                n "The plate flies in the air, with it the ham sandwich that was put on top of it."
                n "You are apparently not the only one who has noticed, as you can see a beautiful blue merlin jump from an opening in the aquarium."
                n "The merlin has a long and pointy bill, it pierces the sandwich in a feat of pure dexterity. "
                n "Sadly it's traject leads right to [persistent.date]'s chest as it's sword-like bill pierces it, somehow you know it has pierced her heart aswell."
                n "She gives you one last look of utter shock before she falls dead on the floor."
                play music game_over
                $ persistent.cafe_death_1 = True
                jump gameOver




            elif chinese == True:
                #Chinesescene here
                n "For a moment you get lost in your thoughts."
                n "When you refocus you notice Lilith walking back to her chair."
                l "Heya [persistent.name], I hope you didn't have to wait too long."
                l "I hope they our food will be ready soon, I'm kind of starving."
                n "Just as she said those words, almost by magic you can see a waitress heading your way."
                if peking == True:
                    n "When the waitress arrives with your double plates of Peking duck [persistent.date] and you immediately dig in."
                else:
                    n "When the waitress arrives with your orange chicken and [persistent.date]'s peking duck the two of you immediately dig in."

                n "She takes a break from her food and looks at you for a moment."
                l "You know, I'm actually glad we could meet here, I wanted to tell you something."
                n "Before [persistent.date] can finish her sentence her face starts to swell."
                play music game_over
                l "Call an ambulance, now!"
                n "You grab your phone as you frantically start calling an ambulance."
                n "A woman with a warm voice listens to your incoherent ramblings and tries her best to get the details, she sends an ambulance your way."
                n "The ambulance arrives quite fast but not fast enough. The doctors conclude that it must have been some sort of severe allergic reaction that made her face swell untill she couldn't breathe anymore."
                $ persistent.chinese_death_1 = True
                jump gameOver

            else:
                "This is an error, if you can see it the location scene for the first death is broken."

        label restaurant_death_1_prevented:

            if burger == True:
                n "[persistent.date] gives you a sceptical look but decides to follow your instructions, right as she does so a cacophony of hellish sounds begins to emanate through the halls of the mall."
                n " Knowing what is to come you try to pay attention to a specific sound, a gunshot is heard and a bullet flies where she would have been if you didn't warn her."
                n "Alright that is crazy, how did you know that bullet would hit me?"
            elif cafe == True:
                n "[persistent.date] gives you a questioning look, as if she's trying to estimate if you are joking or not."
                l "Eventually she decides to not take any chances.
                She stands up and moves to your side of the table."
                l "So..."
                l "What is this all about [persistent.name]?"
                n "Before you can answer her question you hear someone scream again, that's the sign.
                You turn your head just quick enough to see someone fall with a plate in their hands."
                n "The plate flies in the air, with it the ham sandwich that was put on top of it."
                n "You are not the only one who has noticed, as you can see a beautiful blue merlin jump from an opening in the aquarium."
                n "The merlin has a long and pointy bill, it pierces the sandwich in a feat of pure dexterity. "
                n "It's current trajectory leads it to pierce through the chair where [persistent.date] was sitting just mere moments ago."
                n "The staff quickly rush towards your table to take the merlin away and to see if it hasn't been hurt, they offer [persistent.date] and you a short apology before disappearing."
                l "..."
                n "[persistent.date] looks as if she has seen a ghost, if you hadn't intervened she may have seen her own."
                l "Alright, I'm trying my best to remain calm but how did you know that exact scenario would happen?"
            elif chinese == True:
                $ persistent.dumbo_knowledge = True
                l "I suppose that makes sense, I am allergic to quite a few things."
                l "When I was a kid I once ate a few peanuts while I was watching Dumbo, I felt my throat swell and I thought I was becoming a little elephant, just like Dumbo."
                l "I ran to my parents and said:\"Look mommy, look daddy! I can fly!\" and then I started using my hands to flap my ears around like Dumbo."
                l "At that point I was pretty swollen so it was a good thing my parents saw me, we went to the hospital as fast as we could and the kind doctors really helped me out."
                l "When I finally was allowed to go home from the hospital my parents gave me a Dumbo plushie to always remember the story."
                l "And I can say that I still remember it like it was yesterday,  the same counts  for my mom, she keeps joking about it to this day."
                n "[persistent.date]  lets out a huge laugh as she looks at you."
                n "Suddenly she stops, you see a look of worry in her eyes."
                l "Oh sorry, I'm ranting again aren't I?"
                l "I'm sorry, it's just that when I start talking it's pretty hard for me to stop, what were we talking about again?"
                l "Oh yeah, the supposed allergy I would have if I ate that Peking duck."
                l "How would you even know? I mean, I checked the ingredients on the list and as far as I'm aware I'm not allergic to any of those."
                l "So let's say that there's something in this dish that I'm really allergic to but I don't know it yet, how would you know that?"
            else:
                "restaurant_death_1_prevented error."
            jump restaurant_death_1_prevented_explanation

    label restaurant_2:
        label restaurant_death_2:
            #Here the code of the second death will be.
            play music game_over
            if burger == True:
                $ persistent.burger_death_2 = True
                if not burger_explosion_outside == True:
                    n "Suddenly a inmense sensation of pain overwhelms you, the only thing you can see is a glimpse of pure white and an eternity of black."
                n "When you awaken you find yourself surrounded by doctors, they tell you that with the force of sheer luck the stray bullet that would've hit [persistent.date] managed to cause a gas leak."
                n "The gas explosion that followed was quite severe, you were in a coma and had to have your wounds cleaned with some surgical procedures."
                n "After a week you got out of your coma, [persistent.date] however didn't have such luck."
                n "The doctors tell you that she atleast went out pretty quickly, almost like dying in your sleep but with more explosions."
                if death_narration !== "":
                    n "[death_narration]"

                $ burger_explosion_outside = False
                jump gameOver

            elif cafe == True:
                n "Suddenly you begin to hear the sound of shattering glass."
                n "As you turn to look at the source of the sound you can see that the aquarium next to where [persistent.date] was sitting has shattered."
                n "The water is gushing out rapidly and it does not seem to be planning to stop."
                n "How could this happen?"
                n "Did the merlin somehow made a crack form?"
                n "Or was it something else?"
                n "You think about the pure shenanigans that were needed to even make this exact thing happen but you are soon interrupted by the water flowing past your shoes with some fish coming along for the ride."
                l "Quick [persistent.name], we need to do something!"
                if persistent.cafe_death_2 == True:
                    n "You give [persistent.date] a firm hug and tell her that there's nothing else you two can do except for waiting."
                    if love_meter >= 3:
                        l "If I have to go now I atleast get some comfort out of the fact that you are here for me."
                        l "Goodbye [persistent.name], thank you for everything."
                        
                    else:
                        n "And so the both of you wait, in eachothers arms, for certain death. And it comes as expected."
                    
                
                else:
                    $ persistent.cafe_death_2 = True
                    n "You try to open the main exit of the restaurant but it doesn't seem to be giving in, almost as if something is blocking it."
                    n "Quick! Maybe we can still go to the first floor, we need to go higher!"
                    n "Pretty much without any other option you two decide to make a rush for the first floor of the restaurant.
                    When you turn around the corner you see that the stairs are blocked of by an extremely large closet made out of lignum vitae, you can not carry that, all you can do is admire the craftmanship."
                    n "You give [persistent.date] a firm hug and tell her that there's nothing else you two can do except for waiting."
                    n "And so the both of you wait, in eachothers arms, for certain death.
                    And it surely came."
                if hugRequestedBeforeDeath == True:
                    n "it seems [persistent.date] got the hug she asked for afterall, just not in the way she thought she would."
                else:
                    if death_narration !== "":
                        n "[death_narration]"
                jump gameOver

            elif chinese == True:
                n "Suddenly you hear the faint sound of quacking."
                n "The sound of the quacking steadily grows louder and louder untill it's all you can hear."
                n "A true quackophony if you will."
                n "[persistent.date] looks over your shoulder with a frightend look in her eyes."
                n "When you turn around you see a wave of angry geese breaking through the doors of the once cozy Chinese restaurant, the staff is running around in sheer panic."
                n "Before you can make another sound everything turns to white, the white of pesky geese feathers."
                n "The pain you are experiencing is too much and you fall unconscious."
                n "When you wake up again all the cutomers and staff have dissapeared, including [persistent.date]."
                n "The room is completely filled to the brim with geese feathers, you begin to sneeze just thinking about that."
                n "While you are sneezing you notice that someone put a sticky note on your hand."
                n "It reads as following: \"We took everyone and you won't be seeing them back, let this be a lesson on why you should not eat or serve geese or ducks, as those are also part of our family.
                - Sincerely, the geese\""
                $ persistent.chinese_death_2 = True
                if death_narration !== "":
                    n "[death_narration]"
                jump gameOver
    label car_death:
        $ persistent.runAwayLilith_counter += 1
        if angryLilith == True:
            l "[persistent.date] stands up from her seat and shoves it back with a frightening speed."
            if noTalkAngryLilith == False:
                l "I really didn't want it to come this far but you left me no other choice [persistent.name]."
                if major_love_offence >= 1:
                    l "I just have one question for you."
                    l "Why go on this date with me at all?"
                    l "I was really looking forward to this date, but I'm not sure I can say the same for you."
                    l "I mean, if you really wanted to be here with me today, then why were you so rude to me?"
                    l "Don't bother answering that [persistent.name], no answer you could give would ever change what I'm going to do next."
                elif minor_love_offence >= 2:
                    l "I could endure one rude remark, even though I probably shouldn't."
                    l "I guess I stayed because I hoped things would become better."
                    l "I guess I also stayed because I owed it to myself to go out once and I didn't want to ruin this date."
                    l "But now I know better. I will ruin this date if I stay here. Atleast when I walk out on you I can still feel some pride for myself afterwards."
                l "Goodbye [persistent.name], and a tip for the future: if you ever go another date, try to develop manners beforehand. "
                if persistent.lildeaths >= 1:
                    n "I guess we will see very soon wheter or not it is possible for you to do that, right player?"
        
        play music game_over
        if burger == True:
            $ resname = "burger restaurant"
            $ resname2 = "burger"
            $ currentcar = "persistent." + resname2 + "_car_death"
        elif cafe == True:
            $ resname = "cafe"
            $ resname2 = "cafe"
        elif chinese == True:
            $ resname = "chinese restaurant"
            $ resname2 = "chinese"
        if car_caught == True:
            if burger == True:
                n "[persistent.date] leaves the burger restaurant, you rush after her in an effort to calm her down.
                This time there is no red Sedan in sight, it seems as if the cops handled it well."
                n "However, just as you're processing that your mind wanders to the gas explosion that always appears arround this time."
                n "It was probably not a good idea to come here."
                n "That is your last thought as you feel everything fade to black after you hear the explosion."
                $ burger_explosion_outside = True
                jump restaurant_death_2

            elif cafe == True:
                n "[persistent.date] leaves the cafe restaurant, you rush after her in an effort to calm her down. "
                n "When you set one foot outside of the doorframe the red Sedan that always thwarts your plans drives head first into the both of you."
                n "Luckily you managed to get flung to the side somehow. [persistent.date] however was not so lucky."
                n "She died on impact when the speeding car hit her."
                n "Atleast the police showed up due to your call and locked the drunkard up."
                n "If only they managed to come a tiny bit earlier.
                It was probably not the best idea to go here with [persistent.date] when the car is still on the loose."
                jump gameOver


            elif chinese == True:
                n "[persistent.date] leaves the chinese restaurant, you rush after her in an effort to calm her down."
                if persistent.chinese_car_death == True:
                    "This time there is no red Sedan in sight, it seems as if the cops handled it well."
                if angryLilith == True:
                    l "Leave me alone [persistent.name]! I don't want to see you ever again!"
                else:
                    l "Why are you following me [persistent.name]? I want to be alone." 
                n "And with that [persistent.date] leaves, you never saw her again. Not this time anyway."
                n "Atleast she didn't seem to get killed by anything on her way back home since you still heard people talk about her from time to time."
                if persistent.lildeaths > 15:
                    n "You are unsure of how to feel. As horrible as that date went, she is still alive."
                    if persistent.lilithAliveAndRetriedCounter == 0:
                        n "Does this mean that you won?"
                        n "That you can stop trying to save her?"

                $ lilithAliveEnding = True
                $ persistent.ending_badDate = True
                $ ending_check = "badDate"
                $ persistent.lildeaths -= 1

                if angryLilith == True:
                    n "You probably shouldn't have angered her so much."
                else:
                    if explanationAsked:
                        if groundhog == False and psychic == False:
                            n "Maybe you should give her a different explanation?"
                        else: 
                            if groundhog == True:
                                if persistent.groundhog_answer_right_knowledge == True:
                                    n "Now next time you can give her the number she was thinking of."
                                else: 
                                    n "Maybe you need to give some proper proof."

                            elif psychic == True:
                                if persistent.psychic_answer_right_knowledge == True:
                                    n "Now next time you can tell her the word she was thinking of."
                                else: 
                                    n "Maybe you need to give some proper proof."
                    else:
                        n "You should probably try something else next time."

                jump gameOver



        else:
            if currentcar == True:
                n "[persistent.date] leaves the [resname], you can not bare seeing what happens next so you decide to stay inside.
                Even from inside you can still hear the car crash into her."
                #TODO:Account for the notangry flag in the original here:

            else:
                $ currentcar = True
                if persistent.redSedan_knowledge == True:
                    $ carDescription = "the same red Sedan that you encountered before"
                else:
                    $ carDescription = "a red Sedan"
                n "[persistent.date] leaves the [resname], you rush after her in an effort to calm her down.
                When you set one foot outside of the doorframe [carDescription] drives head first into the both of you."
                n "Luckily you managed to get flung to the side somehow. [persistent.date] however was not so lucky."
                n "She died on impact when the speeding car hit her."
                if persistent.redSedan_knowledge == False:
                    $ persistent.redSedan_knowledge = True
        jump gameOver

label kokiri_deaths:
    label angryLilith:
        $ persistent.runAwayLilith_counter += 1
        if major_love_offence >= 1:
            n "[persistent.date] jumps up from where she was lying mere moments ago, on her face is a visible layer of anger or is it... disappointment?"
            n "You're not sure which one would sting more, probably a combination of the two."
            n "She wipes the crumbs on her clothes away with a frightening speed and angrily storms down the hill."
            if noTalkAngryLilith == False:
                l "Goodbye [persistent.name], we are done here."
                l "Do not come back for extra attempts if you have even the slightest slither of respect for me."
            $ persistent.kokiri_angry_noretry = True
        elif minor_love_offence > 1:
            n "[persistent.date] stands up from where she was lying mere moments ago. You can clearly see a disappointed look on her face."
            if noTalkAngryLilith == False:
                l "This might all be a game for you [persistent.name], but for me this is very real."
                l "So I'd like to be treated with the respect you would give to a real person."
                l "You need to learn that your actions have consequences, even in something as simple as a game."
                l "I'm leaving now. Don't try to follow me, there's nothing you can say to me right now to change my mind."
                l "Besides, you can just retry right?"
                l "I'd prefer if you didn't, but I know I can't stop you."
                l "Let's just hope that when I meet you here once again during the next attempt you will have learnt your lesson."
                l "Goodbye [persistent.name]."
        n "[persistent.date] turns away from you and walks down the hill cool and collected, it seems she has made up her mind about this."
        n "She doesn't get far from the hill, maybe a metre or fifteen before she seemingly trips over a tree root."
        n "She does not get up."
        play music game_over
        if persistent.kokiri_angryLilithDeath == False:
            n "When you rush to her you notice why."
            n "[persistent.date] hit her head pretty badly on a small rock."
            n "The end result looks horifying."
            n "You call an ambulance but when they arrive they tell you what you already knew deep down."
            n "She didn't make it."
            $ persistent.kokiri_angryLilithDeath = True
        else:
            n "Deep down you already know it is too late."
            n "But you can't help yourself, you call an ambulance hoping that this time is somehow slightly different."
            n "That this time she is still alive by the time they arive."
            n "After what feels like waiting for years the ambulance finally arrives."
            n "Sadly they tell you the same news they've already told you before."
            n "She didn't make it."
        jump gameOver

    label kokiri_1:
        label kokiri_death_1:
            if met_check != "meteorite_warn":
                if kokiri_call_death_1_check == False: #If she wasn"t calling her mom/sis during this death:
                    if kokiri_silentMoment == False:
                        n "[persistent.date] stops talking for a moment as she begins staring at the star-filled night, it seems like something has drawn her attention away from you."
                    else:
                    
                        n "[persistent.date] diverts her look from your eyes from a moment and continues watching the star-filled night."
                    n "A gasp of amazement escapes her mouth."
                    l "You really need to see this, it's absolutely stunning!"
                    n "The sky now is completly filled with falling stars, you've never seen so many falling stars in your entire life, let alone all together."
                    n "However, one point seems to be getting bigger and bigger, it doesn't seem to be a star as it's not sending out any light."
                    if kokiri_alternateplace == False:
                            n "The both of you watch in absolute terror as the thing only starts to get closer, becoming larger, in an alarming rate. "
                            

                    else:
                            "The meteorite can't kill her because she is sitting somewhere else, FILLER"
                            #TODO: This part already exist somewhere in this game, I think it's based on calling someone or something? Probably try to search for this? Although there she is not aware of where it falls, so maybe write some slightly different text.
                
                play music game_over
                n "The meteorite breaks into many different parts that spread all around the forest."
                n "One of them crashes straight against [persistent.date]'s head with a frightening impact."
                if persistent.kokiri_death_1 == True:
                    n "You close your eyes in an effort not to be subjected to the absolutely horifying state [persistent.date] is in right now."
                    n "It's a very futile effort as her corpse is still engraved in your eyelids from the previous time."
                    n "That's right, her corpse. You already know that it is too late for her."
                    n "And yet you still hope that you are proven wrong, that she might show any signs of life."
                    n "But no matter how long you wait the only thing that you can hear is pure silence."
                    if kokiri_call_death_1_check == True: #Check wheter or not she was calling someone at the time of her death.
                        if kokiri_chatchar_abigail_called == True:
                            n "You can vaguely sense Abigial's screaming but somehow it gets almost drown out by the silence of the forest."
                        elif kokiri_chatchar_lila_called == True:
                            n "You can vaguely sense [persistent.date_mom]'s screaming but somehow it gets almost drown out by the silence of the forest."
                    n "It is hard to imagine that just a few moments ago the forest felt so lively since it now just feels lonely and cold."
                    n "You feel so lonely and cold."
                    n "You lay down next to [persistent.date] in a futile effort to feel less alone, to cope with the situation."

                else:
                    $ persistent.kokiri_death_1 = True
                    n "Her head is cracked open and a puddle of blood begins to form around it. Everything around you turns silent."
                    if kokiri_call_death_1_check == True: #Check wheter or not she was calling someone at the time of her death.
                        if kokiri_chatchar_abigail_called == True:
                            n "Even [persistent.date_sis] who is currently screaming her lungs out has become unbearingly silent."
                            n "You would also like to scream but all that manages to come out is the same silence that seems to have taken over the forest."
                        elif kokiri_chatchar_lila_called == True:
                            n "Even [persistent.date_mom] who is currently screaming her lungs out has become unbearingly silent."
                            n "You would also like to scream but all that manages to come out is the same silence that seems to have taken over the forest."
                    else:
                        n "You would like to scream but all that manages to come out is the same silence that seems to have taken over the forest."
                    n "It's almost as if the forest itself is mourning her death."
                    n "Some dark clouds move in front of the moon as if to stop it from revealing the state of [persistent.date]'s corpse."
                    n "They are rather unsuccessful."
                    n "Even if they had been succesful you are sure you still could see her body engraved in your eyelids."
                jump gameOver
            else:
                jump kokiri_death_1_prevented
            

               

        label kokiri_death_1_prevented:
            #if kokiri_prevented == 1: This is code that would have made it so that it triggers based on 1-4 and the deaths.
                n "As she moves to the other side of the blanket, to your left, you once again see the same meteorite that killed her last time. It breaks of in many peaces, one of them falling right where she was sitting just a moment ago."
                n "[persistent.date] gives you a startled look."
                l "Oh wow, a meteorite? That was what was going to kill me now?"
                l "So you spoke the truth... I keep on dying over and over on this date?"
                l "Seems like I woke up with some major bad luck today."
                l "Although I suppose I am lucky enough to go through this with you, thank you for saving me once again [persistent.name]!"
                n "[persistent.date] pauses for a moment."
                l "Alright, I have to put the levity aside for a moment and be honest with you."
                l "I might look and sound calm right now but that's just because I kind of freeze in situations like this."
                l "This..."
                l "It's a lot to deal with right now."
                l "I knew {b}something{/b} strange was going on when you told me about the kokiri forest."
                l "That's why I came here I suppose, to figure out how you knew about this place."
                l "But I guess even when you explained it to me, a part of me didn't believe you."
                l "A part of me didn't want to believe you."
                l "Even if deep down I knew you were telling the truth."
                l "..."
                l "I just need a moment to gather my thoughts [persistent.name], after that we can continue our conversation if you'd like."
                n "You give a slight nod, the corners of [persistent.date]'s mouth subtly move up, you almost didn't quite catch it."
                n "You're not quite sure how long the moment lasts, but after a while she shifts her postion and gives you a nod."
                l "I think I am ready now, this is still a lot but I might be able to see it through now."
                l "Thank you for staying here with me, it helped me calm down a little while I was thinking."
                if car_caught == False:
                    jump kokiri_death_2
                else:
                    jump kokiri_death_2_prevented
    label kokiri_2:
        label kokiri_death_2:
            play music game_over
            if kokiri_alternateplace == True:
                if kokiri_call_death_2_check == True:
                    n "While [persistent.date] is engrossed in her call you notice the red Sedan that rode up the hill and hit [persistent.date] riding up the hill once again."
                else:
                    n "As [persistent.date] and you are talking you suddenly glimpse the red Sedan that hit [persistent.date] on the hill driving up the hill once again."
                if persistent.kokiri_death_2_alternate == False:
                    n "You chuckle to yourself, you just prevented two deaths with one choice."
                    n "That's not bad at all."
                n "And yet, as the car drives fully up the hill you notice something."
                n "The car turns around and comes towards [persistent.date] and you with an even more frightening speed than it had on the hill."
                n "The car appears to have gained momentum from the down-ward slope of the hill."
                n "You don't have much time to think about this before it comes hurdling towards the two of you."
                n "You instinctively jump out of the way."
                n "[persistent.date] however didn't manage that."
            else:
                n "Suddenly you notice a strange sound."
                n "A red sedan speeds towards the both of you with a frightening speed. Fight, flight or freeze. You have three options."
                n "You would like to think you would pick fight and push [persistent.date] out of the way, somehow escaping at the same time."
                n "And yet you instinctively pick flight as you jump away from the car."
                n "Sadly it seems [persistent.date] did not do the same, she instead froze."
                n "And now she is forever frozen as she lays there on the floor, unmoving."
            if kokiri_call_death_2_check == True:
                if kokiri_chatchar_abigail_called == True:
                    n "You call an ambulance with shaking hands as you hear [persistent.date_sis]'s neverending screaming coming from [persistent.date]'s phone."
                elif kokiri_chatchar_lila_called == True:
                    n "You call an ambulance with shaking hands as you hear [persistent.date_mom]'s neverending screaming coming from [persistent.date]'s phone."
            else:
                n "You call an ambulance with shaking hands."
            n "Your suspicion was proven true by the paramedics, she was dead as soon as that car hit her."
            if car_free == True:
                n "It appears calling the cops didn't accomplish much this time. Maybe you need to send them to another location?"
            
            if kokiri_alternateplace == True:
                if kokiri_call_death_2_check == True:
                    $ persistent.kokiri_death_2_call = True
                else: 
                    $ persistent.kokiri_death_2_alternate = True
            else: 
                $ persistent.kokiri_death_2 = True
            jump gameOver

        label kokiri_death_2_prevented:
            n "You tell [persistent.date] about how the red Sedan would've hit her if you wouldn't have called the police." #TODO Make that an optional choice and continue working from here.
            if kokiri_alternateplace == False:
                if kokiriSceneryWatched == True:
                    $ carDescription = "that car we just watched"
                else:
                    $ carDescriptiion = "a car"
                l "I see... first a meteorite and now [carDescription]?... It really seems like the universe has it out for me today."
                l "Well thank you for going through such efforts to help me!"
                n "[persistent.date] gives you a big smile, a look of gratitude is plastered across her face."
            else:
                l "A car?..."
                if love_meter <= 2:
                    l "It sounds unlikely to be honest."
                    l "And yet you knew about this place, so I guess you might be right..."
                    n "[persistent.date] seems to be thinking about something, everything turns quiet for a moment."
                    l "I suppose I owe you a thank you for helping me out today. So thank you [persistent.name]."
                else:
                    l "Wow, it really sounds as if death is following me wherever I go."
                    l "Thank you for helping me survive this whole ordeal [persistent.name]!"


            menu:
                "I tried everything [persistent.date], I even took you to space but it didn't work out, no matter wich path I choose you still end up dying." if persistent.reality_knowledge:
                    jump kokiri_death_2_prevented_triedEverything

                "Am I really helping you though? One of the things I saw while playing the game is that if we didn't date anymore you would keep being alive and find happiness with a nice guy called Ron." if persistent.ending_breakup:
                    jump kokiri_death_2_prevented_youWereHappyWithRon

                "Am I really helping you though? It's true that I keep saving you but because of that you also keep dying. You've died [persistent.lildeaths] times now and I'm not sure how many more times I can see you die without breaking down entirely." if persistent.lildeaths > 25:
                    jump kokiri_death_2_prevented_youDiedATon

                "You are welcome [persistent.date], I'll try to get us out of this mess.":
                    l "And I just know that you will succeed, I got a good feeling about it."
                    l "Do you know why I have that feeling?"
                    l "Because despite everything going on right now, being bombarded with the knowledge that I keep dying and probably will do so again, I feel at ease."
                    l "Well, as at ease as that knowledge allows me to be."
                    l "But still, you being here helps me calm down just that extra bit I need to not start absolutely freaking out right now."
                    l "You know, the idea that you are here to help protect me I suppose."
                    l "It might sound silly, but it's nice to know that there is someone repeatedly coming back for me."
                    l "I had to deal with both my father and my brother leaving, albeit in very different ways."
                    l "I guess this feels refreshing?"
                    l "Deep down I guess I always blamed myself for what happened, for them leaving."
                    l "As if there some curse cast on me that would make all my loved ones leave me."
                    l "If anything, I am thankful that I now have another piece of evidence to hold on to whenever I experience that thought again."
                    l "So thank you very much for that [persistent.name], that means more to me than I could ever express fully."
                    jump kokiri_pictureChoice

                "We're running out of time. Could we please continue talking?":  
                    jump kokiri_continue_talking
                    
label kokiri_death_2_prevented_triedEverything:
    p "I tried everything I could think of [persistent.date]."
    p "I've fled from death with you, even going as far as flying away from the earth with a spaceship only for reality itself to collapse."
    if persistent.ending_breakup == True:
        p "I might have been selfish, in one timeline you end up with a guy called Ron and you two just have a great time together."
        p "But that wasn't enough for me, I want to go on this date and have you come out of it alive and well."
    p "I just want to share a nice, enjoyable date with you."
    n "[persistent.date] points at the village, illuminated by the moon and the stars."
    l "With such a marvelous view I would surely call this a nice, enjoyable date."
    n "She snuggles up to you."
    l "Thanks for going on this date with me! I'm having a really good time so far!"
    l "You know, I've been thinking..."
    l "If I'm going to die soon then what's stopping you from quitting this game? Or would I just lose consciousnes, like I'm dying?"
    l "I'm not sure if there's a way to tell. What do you think?"
    $ persistent.game_credits = True
    menu stopPlayingGameConsequences:
        "I believe that you would still live on.":
            l "That's rather reassuring."
            l "Since we're in a video game there's only so much dialogue I can tell you and only as many places we can go to as are programmed into it."
            l "But if you could break the boundaries through whatever creative outlet you have then there would essentially be thousands upon thousands of stories about us that you could give life. "
            l "The best part would be that you decide how they play out."
            l "She pauses for a moment and then continues."
            l "We tend to create these new worlds all the time, sometimes even without realising it."
            l "When you are thinking about what the next season of your favourite show will be about then you're technically creating an entire new world where the show's characters go through your story."
            l "And who's to say wich version is the superior one? Afterall, they're both telling a story, personally I think that's absolutely beautiful."
            l "So let's try to do just that!"
            n "[persistent.date] hugs you for a long period of time, you feel her warmth as it reaches your cold body."
            n "And yet, it's not really your body, right?"
            n "More so the body you channel yourself through."
            n "Your avatar's body."
            n "There's a layer of separation you are trying so hard to ignore."
            n "But what if you didn't have to ignore it?"
            n "What if it wasn't there at all?"
            l "So... has it already happened? Are you now making our story?"
            label kokiri_makingOwnStory:
                menu:
                    "No, we're still in the game.":
                        n "[persistent.date] looks at you with a puzzled look on her face."
                        l "Oh... I thought you had already started. Why are you still playing this game instead of making your own story?"
                        menu:
                            "I just want to see what happens when I choose this path.":
                                $ death_narration = "It appears you got your wish. This path, like many others only leads to death."
                                jump kokiri_death_4_hill


                    "Yes, I'm now in full control of it.":
                        n "[persistent.date] gives you a warm embrace and jumps up in the air after she stops hugging you."
                        l "Perfect! So now we can just do whatever we want without having to fear being killed right?"
                        menu:
                            "Absolutely!":
                                n "You do know that is not the case, right?"
                                n "That I'm still the one telling this story, that you are not in control."
                                n "Are you lying to yourself, or to her?"
                                n "Maybe both?"
                                
                                if persistent.kokiri_tellnolies_knowledge:
                                    n "I'm not sure if she would like that."
                                    n "Actually I'm very sure she wouldn't like that, and so are you."
                                    n "And yet you did."
                                    n "I wonder why, did you try to alleviate some of her fear?"
                                    n "Or did you want to fool yourself for a second into believing your own lies?"
                                    n "Or perhaps you wanted to just see what dialogue that choice would give you?"
                                    n "Either way, what's done is done."
                                    n "Normally I might scold you for doing something like this, but I'll admit I can see why you might have chosen to lie."
                                    n "Maybe ignorance truly is bliss."
                                    if persistent.kokiri_death_4_hill_holdHand or persistent.kokiri_death_4_hill or persistent.kokiri_death_4_noHill == True:
                                        n "And yet we are not given that mercy are we?"
                                        n "As we sadly both know what will happen next."
                                        n "Would you want to unlearn the knowledge?"
                                        n "Feel that same blissfull ignorance as Lilith?"
                                        n "I fear with you it might not be as easy as just setting a few variables."
                                        n "And even if it was, your knowledge is what got you this far isn't it?"
                                        n "So, maybe sometimes it's good to be aware of painful things?"
                                        n "If we never felt pain from putting our hands on something hot, would we learn to not touch it?"
                                        n "Maybe if someone told us, but what if they decided it was better for us not to know?"
                                        n "Would they have protected us with that? I honestly could see it either way."
                                        n "..."
                                        n "I fear I'm stalling a bit, but the script is going to the next part now."
                                        n "There is nothing you or I can do about that."
                                        


                                else:
                                    n "I do suppose ignorance is bliss."
                                    n "Maybe it's better for her to still believe that things are going to start looking up for her."
                                    n "Maybe it's better for you to believe that just for a little bit longer."
                                    n "But nothing can last player, each line from the script ends at some point, making way for the next."
                                    if persistent.kokiri_death_4_hill_holdHand or persistent.kokiri_death_4_hill or persistent.kokiri_death_4_noHill == True:
                                        n "And we both know what the approaching lines will be, no matter how hard you might try to stall them."
                                    
                                jump kokiri_death_4_hill
                                $ kokiri_fullControlAndStillDying = True
                                
label kokiri_death_2_prevented_youWereHappyWithRon:

    l "Well, I am spending this moment with you, not with this \"Ron\"."
    n "[persistent.date] places her hand on your arm and rubs it softly."
    l "It is sweet that you care about me enough to worry about those sorts of things but I would rather not have you worry about them."
    l "Besides, you made that version of me happy with Ron and now you've made this version of me very happy with you."
    n "She flashes you a knowing smile."
    l "If you ask me you have succeeded."
    jump kokiri_pictureChoice

label kokiri_death_2_prevented_youDiedATon:
    l "Oh, [persistent.name], it certainly has been a lot to wrap my head around  but I never had to constantly deal with this whole scenario like you. I truly suppose ignorance is bliss."
    l "I can completely understand that you are dealing with a lot throughout this whole thing. I really don't blame you for trying to keep coming back."
    l "You are just trying to find a way out and I'm sure you'll find it. Your intentions are pure."
    l "I don't blame you for anything [persistent.name], please don't blame yourself either."
    l "Afterall, is it worth it to live with me if you can't live with yourself?"
    n "[persistent.date] seems to be lost in thought for a moment."
    l "However, if you truly feel like I keep dying every time, maybe there is no way for us to be together and for me to be alive?"
    l "Did you ever consider that option [persistent.name]?"
    menu: 
        "I did, the more this goes on the more I think you might be correct.":
            $ persistent.kokiri_makeYourOwnStory_knowledge = True
            l "I see, so you don't think there is a way for both us to be together and for me to be alive?"
            l "Hearing through how much trouble you had to go only to have me die over and over again makes me think the same to be entirely honest with you."
            l "Still, I wonder what the purpose of that is."
            l "It feels a bit weird to set up a sort of challenge, in the form of the premise of this game, and to then just make the player unable to beat it."
            l "Or maybe we're looking at it wrong, maybe the challenge is something else."
            l "Like accepting what is going to happen to me?"
            n "[persistent.date] sighs."
            l "Or maybe we're looking at it all wrong, maybe instead of accepting it we have to somehow push back even more against it happening."
            l "But how would we change the course of this game?"
            l "It's not like I can just yell \"You won, I didn't die!\" and make that come true, right?"
            l "I guess it does have to come from the game itself before it feels true."
            l "Hang on!"
            n "[persistent.date] gives you a very mischevious smile."
            l "I might have an idea, the things the game directly tells you feel true, right?"
            l "Like they are just a part of the narrative, you don't really question them."
            l "What if you just, ignored them?"
            l "Is there a difference between the game telling you I died or me and you saying I didn't?"
            l "In any case, the game needs you as much as you need it, maybe even more."
            l "It needs you to hear it's story and to interact with it, and you need it to tell it's story so you can interact with it."
            l "But you might even be able to skip out on the game part entirely and just take all the pieces you like of this story, combine them and tell your own story, just the way you want to."
            l "In your own story anything would be possible, we wouldn't need to folow any rules you don't like, doesn't that sound nice?"
            l "Let's try to give it  a shot, alright?"
            n "You give a quick, assured nod."
            l "So, are we now outside of the game?"
            l "Are you making your own story?"
            jump kokiri_makingOwnStory
        "I did, but I genuinely think there is a way, it's just that I'm begining to lose hope.":
            l "I see, this is a very daunting task, it's normal to feel like that sometimes."
            l "You are not alone in your burden [persistent.name], you can share it with me, I want you to know that."
            l "Even if I need to be caught up to speed after every loop because I forgot everything."
            l "You have been my hope that I will survive this. Now let me be yours."
            n "For a moment everything turns quiet, almost as if not to break the silence instead of saying something Lilith makes a beckoning motion."
            n "The singing of a bird nearby dethrones the silence, and freed from it's oppressive reign Lilith speaks again."
            l "I think I might have an idea of how to give you some more hope, it always helps me out when I need some."
            jump kokiri_pictureChoice
label kokiri_pictureChoice:
    l "You know what? I want to show you something..." #TODO: With the paths that jump here this line doesn't always make sense, you'll need to have either alternate lines or just hide this line in certain circumstances.
    n "[persistent.date] stands up from the blanket, some shards of the meteorite still laying on it and extends her hand to you."
    menu:
        "*Take her hand*":
            jump kokiri_showpicture
        "You actually already showed me the beach picture in that big tree over there. It fell over right on top of you..." if persistent.kokiri_death_3:
            jump kokiri_death_3_prevented
label kokiri_showpicture:
    $ persistent.beach_knowledge = True
    n "You grab her hand and get up."
    n "With your hand in hers she leads you to a very high tree surrounded by a bunch of smaller trees."
    l "You are probably thinking why I am taking you here."
    l "Well, I hid something... precious here."
    #TODO: Probably add some more descriptions of the route you took
    n "She looks at the big tree and the trees surrounding it, a smile growing on her face."
    n "She moves to the back of the big tree, and comes back with a small wooden box, decorated with red details."
    n "Then she takes of her necklace you somehow never noticed before, a key is dangling on it."
    n "She uses the key to unlock the box and takes out a polaroid."
    n "The photo shows two adults,two small girls and a prebuscent boy on a beach. The children are all building a sandcastle together and the adults are smiling while watching them."
    l "This is a photo of our family at a day on the beach, those were the happy days..."
    l "Even to this day I still have an afinity for the beach because it is linked to those happy days."
    l "But I know i will never truly get them back, not like it used to be anyway.."
    l "I still have [persistent.date_sis] and my mother of course, both of them are just so important to me and together we are trying to slowly but surely make new happy days."
    l "But anyway, what I'm trying to say is that you have something special, a way to prevent me from dying and a whole boat-load of determination."
    l "So don't feel guilty about your gift but use it to the fullest extent."
    $ persistent.useGiftToFullExtent_knowledge = True
    menu:
        "I will [persistent.date], I promise.":
            n "[persistent.date] gives you a lovely smile."
            l "Give it your best shot"
            jump kokiri_death_3
        "This might sound weird, but when you say to the fullest extent, do you mean I can also contact your family to gain more potential leads?" if persistent.useGiftToFullExtentLimit_knowledge:
            n "[persistent.date] grows quiet for a moment, she seems shocked by what you just asked."
            l "Well... I'm not sure how you would even contact them unless I give you their number."
            if persistent.peeked_phone == True:
                n "That's not a problem for you, you have their number, but it wasn't exactly {b}given{/b} to you, was it?"
            l "But even if you somehow were able to contact them I'd really prefer if you didn't."
            l "This is already a lot to take in for me, I don't want to place that burden on anyone else."
            n "Everything turns quiet for a moment once again."
            l "So, do you promise to never contact my family even if you somehow were able to [persistent.name]?"
            jump noContactFamilyPromise


    label treeOfLife:
        mt "What do you seek so deep into this code?"
        $ treeOfLifeSoughtAnswer = renpy.input("I seek...")
        $ treeOfLifeSoughtAnswer = treeOfLifeSoughtAnswer.strip()
        $ treeOfLifeSoughtAnswer = treeOfLifeSoughtAnswer.lower()
        python:
            if "the good ending" in treeOfLifeSoughtAnswer:
                renpy.say (mt, "Ah, you seek THE good ending eh?")
                renpy.say (mt, "Well...")
                renpy.jump("treeOfLifeConclusionGoodEnding")
            elif "a good ending" in treeOfLifeSoughtAnswer:
                renpy.say(mt,"Ah, you seek a good ending eh?")
                renpy.say (mt,"Well... ")
                renpy.jump("treeOfLifeConclusionGoodEnding")
            elif "good ending" in treeOfLifeSoughtAnswer:
                renpy.say (mt, "Ah, you seek the good ending eh?")
                renpy.say (mt, "Well... ")   
                renpy.jump("treeOfLifeConclusionGoodEnding")
            else:
                renpy.say (mt, "I'm sorry, I can't help you with that.")
                renpy.say (mt, "I'll show you the exit so you can leave this place, sorry to disappoint you.")
                renpy.full_restart()
                

    label treeOfLifeConclusionGoodEnding:
        mt "You did dig pretty far into this game."
        mt "You might be able to go a little bit further and find what you seek."
        mt "Just be warned, at this point I'm not sure if anything you can find here will suffice."
        mt "But if you really want to pursue it then you have to find a conversation between two pieces of this game."
        mt "A conversation between Adriel and Demetrius."
        mt "But to get access to that conversation you'd have to find a way to become Adriel and Demetrius, I'm sure you already got an idea to do just that."
        mt "Unfortunately there is one complication... you have to mention the name of the person you became once again in another conversation that has something to do with their own conversation."
        mt "They are a sort of God-followers, beings that watch the struggle of players against the Creator and the Narrator, so any conversation that mentions gods without you steering it that way should do."
        mt "Good luck player, may you eventually find what you seek."
        $ renpy.full_restart()

    


    label kokiri_3:
        label kokiri_death_3:
            if persistent.easter_1 == True and persistent.easter_2 == True and persistent.easter_3 == True:
                jump treeOfLife
            else:



                n "Suddenly the earth begins to shake. The roots of the big tree [persistent.date] is standing next to begin unearthing. Before you can do anything the tree falls over right on top of her."
                play music game_over
                n "You push the tree off with all your might but it seems like it was to no avail, the force of the tree killed her instantly."
                n "Your screams pierce through the woods, it answers with pure silence, mourning the loss of Lilith once more."
                $ persistent.kokiri_death_3 = True
                jump gameOver
        label kokiri_death_3_prevented:
            l "Oh I see, so it's safer on this hill?"
            menu:
                "I'm not sure to be honest, this is the farthest we've made it so far." if not persistent.kokiri_death_4:
                    jump kokiri_death_3_prevented_talk_farthestWeHaveGone
                "*Lie* Yup, it is." if persistent.kokiri_death_4:
                    jump kokiri_death_4_noDeath
                "It isn't in fact, we should get off." if persistent.kokiri_death_4:
                    jump kokiri_death_4_noHill
                "It isn't but you are going to die either way." if persistent.kokiri_death_4:
                    jump kokiri_death_3_death_dialogue
    label kokiri_4:
        label kokiri_death_4_hill:

            play music game_over
            $ persistent.kokiri_death_4 = True
            if kokiri_death_4_playerResponse == True:

                n "You want to answer her when suddenly the ground begins to shake once again, this time it even shakes more than when [persistent.date] showed you the picture."

            else:

                n "Suddenly the ground begins to shake once again, this time it even shakes more than when [persistent.date] showed you the picture."
            n " That's pretty strange considering it's the same earth-shaking."
            if kokiri_holdhand == True:
                jump kokiri_death_4_hill_dieTogether

            else:
                #TODO: Add the angry [persistent.date] flag and part. #angryLilith #Make her not ask you for help but just accept her death.
                #The part below is not that part.
                l "What is happening [persistent.name]?"
                if kokiri_fullControlAndStillDying == True:
                    l "Is this how you're telling the story now?"
                    menu:
                        "It is, don't worry, this is all part of my plan.":
                            if love_meter > 2:
                                l "Okay, I trust you."
                                l "Although this doesn't exactly feel like everything is under control."
                            else:
                                l "Oh come on, really?"
                                l "This absolutely doesn't feel like it is part of your plan."
                                l "Even if it was, why go through with all of this? Couldn't you just have let me walk off this hill?"

                        "...I might have lied slightly, I am not in control of the story. We are still in the game.":
                            l "You what?"
                            l "So that means I'm still going to die?"
                else:
                    n "The fear in her voice is palpable."
                n "Suddenly you feel the hill shooting upwards."
                n "The increased force of the gravity is pinning you against the hill but not for long, you begin to roll off the hill and fall down in the middle of a lake close to where it used to sit. "
                p "[persistent.date], it's safe in here, jump down!"
                l "I.... I can't... it's already too high..."
                n "She's right, you can barely hear her words anymore from that height."
                n "All you can do is float there, powerless, while you watch the hill and [persistent.date] getting swallowed by the ink-black sky."
                n "As you do you notice that there are some sort of thrusters sticking out from the bottom of it."
                if damoclesAsked == True:
                    n "It seems unlike Damocles, her thread always snaps."
                    n "Aren't you happy that you asked her Damocles now? Now you get this reference."
                elif death_narration !== "":
                    n "[death_narration]"
                jump gameOver

        label kokiri_death_4_hill_dieTogether:
            l "Is this it, [persistent.name]?"
            n "You give a silent nod, as you do so you can feel her squeeze your hand even more as her's begins to tremble."
            n "Suddenly you feel the hill shooting upwards."
            n "The increased force of the gravity is pinning you against the hill but not for long, you begin start to slide off the hill."
            n "You would probably have fallen if [persistent.date] wasn't holding your hand with all of her strength. She pulls you up slowly, while she does so she has to look down at the rapidly shrinking forest and you can see the fear in her eyes."
            l "Hold on [persistent.name], I got you and I'm not letting you go."
            l "{size=*0.5}Phew, we 're really high... I'm getting dizzy but I must keep going... just a little bit longer...{/size}"
            n "She has managed to pull you up but it costed a lot of her strength."
            n "The both of you flop down on the hill like a few moments ago, the only difference being that the hill is now soaring in the sky, oh and also that two of you are still holding hands."
            l "You know what's funny [persistent.name]?
            I felt more scared when I thought you were going to fall than I am now thinking about how I'm going to die.
            I suppose it's because if you fell I would have to go through this all alone."
            menu:
                "You won't have to do this alone, I'm with you.":
                    jump kokiri_death_4_hill_imWithYou
        label kokiri_death_4_hill_imWithYou:
            l "{size=*0.5}Thank you.{/size}"
            n "She said it quitely, but you feel the sincerity dripping off those two simple words."
            n "For a moment everything becomes quiet."
            n "You grow aware of her hand, held in yours. It feels cold to the touch, and yet it emanates a gentle warmth somewhere deep inside you."
            n "Lilith shifts around slightly, it seems she wants to say something to break the quiet, but doesn't know what exactly."
            l "You know, the stars are absolutely beautiful from here. I have a feeling we'll be able to see them even closer soon."
            n "[persistent.date] shudders as she speaks those words but when you look at her she tries her best to give you a smile."
            play music game_over
            
            n "[persistent.date] was right, the hill flew up into space itself, probably to some far-off stars, not that the two of you would know as after fifteen seconds everything went black.
            You can only imagine the gruesome death the two of you suffered, that is if you weren't unconcious."
            $ persistent.kokiri_death_4_hill_holdHand = True
            jump gameOver
        label kokiri_death_4_noHill:
            play music game_over
            $ persistent.kokiri_death_4_noHill = True
            n "The earth begins shaking once again. The mechanical mound begins to ascend slowly, until it hovers above [persistent.date] and you."
            n "A green pillar of light shoots out from inbetween the four thrusters at the bottom of the ufo."
            n "The beam envelops the both of you and before you can do anything [persistent.date] gets rapidly sucked into an opening of the hill that closes the moment she's inside. It begins ascending again, only this time much faster."
            n "All you can do is stand there, powerless, while you watch the ufo and [persistent.date] getting swallowed by the ink-black sky."
            jump gameOver 












label beach_deaths:
   
                              
    label seaDike_left_slipDeath:
        n "(Add snapping neck on railing death, she slips or gets pushed by a bike)"
        $ persistent.beach_slipDeath = True
    label seaDike_right_potDeath:
        $ persistent.beach_potDeath = True  
        n "(A flower pot falls on her)"
            
    label beach_holeDeath:
        $ hole_death = True
        n "She fell down a hole in the sand, it collapses."
        #TODO: Write this out more.
        jump gameOver  
            
    label beach_jellyDeath:
        $ jelly_death = True
        n "She stepped on a jellyfish and she got into cardiac arrest."
        if persistent.fish == True:
            $ Salmon1 = True
        if persistent.fisher == True:
            $ Salmon2 = True
        if Salmon1 == True and Salmon2 == True:
            n "You notice a salmon swimming in the sea."
            menu: 
                "Walk to it.":
                    if easter1 == False and easter3 == False:
                        $ easter2 = True

label other_deaths:
    "Filler"
    #TODO: Put all deaths that don't fit in the other categories here.
    label phone_untoldstory_planeDeath:

        
        n "Just as she says that you hear a deafening noise come from your phone."
        n "It sounds like a sharp whisteling"
        n "The sound grows louder and louder."
        n "It increases exponentially until it becomes almost earpiercing."
        n "And then you hear a gigantic impact of something and the sound of collapsing walls."
        if persistent.plane_knowledge == False:
            n "Unsure of whatever you just heard you call an ambulance to her house in the hope that she is still somehow alive..."
        else: 
            n "You call an ambulance to go to her house in the hope that this time she might just survive... "

        play music game_over
        
        n "When the ambulance arrived there isn't much they could do, apparently a plane crashed on [persistent.date]'s house."

        n "[persistent.date] has been living alone for a year or two now and she had no real neighbours, not any that weren't a few kilometres away from her atleast. Which means only her house got ruined by the plane."
        n "Sadly the same can't be said for both [persistent.date] and most of the passengers of the plane..."

        n "There were luckily survivors of the plane crash, of the 139 people on board  86 people survived, most of them had minor injuries but where otherwise physically fine, if not mentally scarred."
        n "The event was all plastered over the news as soon as it happened, they followed it live as it unfolded."
        n "[persistent.date] did not survive though, they had to remove the plane to even get to her body, the sight was horifying."
        n "They never mentioned what she looked like but you could hear it in their reaction that the phone, which was still on, had picked up."
        $ persistent.plane_knowledge = True
        jump gameOver

    label phone_planeDeath:
        $ persistent.plane_knowledge = True
        n "As [persistent.date] hangs up her phone you turn on the tv in frustration."
        n "The news is on apparently, it's talking about a plane that had lost height just a moment ago"
        play music game_over
        n "The plane crashed right in the living room of a nice looking house, the house doesn't look unfamilliar to you at all."
        n "Then it hits you."
        n "It's her house."
        jump gameOver



label gameOver:
    if kokiriStarGazed == True:
        $ persistent.kokiriWatchedStars = True
    if teaseDeath == True:
        if persistent.teaseDeath_fakeOut_knowledge == False:
            n "It seems like I was wrong when I said you won. Maybe an other approach would work?"
            $ persistent.teaseDeath_fakeOut_knowledge = True
    if hugRequestedBeforeDeath == True:
        $ hugRequestedBeforeDeath = False
    $ persistent.lildeaths += 1
    $ persistent.retry_counter += 1
    n "{size=*2.5}Game over{/size}"
    n "Your date surely didn't go as planned."
    play music sunrise
    menu :
        "Retry." if not lilithAliveEnding:
            if  persistent.kokiri_angry_noretry == True or persistent.chinese_phone_noretry == True:
                n "So you are going back even when she asked you not to?"
                n "In that case I hope you at the very least don't make the same mistake you did last time."
            jump game_start
        "Retry?" if lilithAliveEnding:
            $ persistent.lilithAliveAndRetriedCounter += 1
            $ lilithAliveEnding = False
            
            if ending_check == "reunionGoodEnding":
                $ persistent.ending_reunionGoodEnding_counter = 0
            elif ending_check == "lettingGo":
                $ persistent.ending_lettingGo_counter = 0
            elif ending_check == "unseenContent":
                default persistent.ending_unseenContent_counter  = 0
            elif ending_check == "anEnding":
                default persistent.ending_anEnding_counter  = 0
            elif ending_check == "quitter":
                default persistent.ending_quitter_counter = 0
            elif ending_check == "breakup":
                default persistent.ending_breakup_counter = 0
            elif ending_check == "abigailDistraction":
                default persistent.ending_abigailDistraction_counter = 0
            elif ending_check == "badDate":
                default persistent.ending_badDate_counter = 0
            jump game_start
