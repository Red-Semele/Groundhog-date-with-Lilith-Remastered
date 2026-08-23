#Put all the deaths in here as a way to clean up all the other files and also just make this way easier to find deaths to rewrite etc.

init python:
    def ending_title_from_check(ending_id):
        ending_titles = {
            "reunitedGood": "Reunited",
            "lettingGo": "Letting Go",
            "unseenContent": "Unseen Content",
            "anEnding": "An Ending",
            "quitter": "Quitter",
            "quitter extraodinaire": "Quitter Extraordinaire",
            "breakup": "Breakup",
            "abigailDistraction": "Abigail Distraction",
            "badDate": "Bad Date",
            "traumaReunion": "Traumatized Reunion",
            "Voided": "No More A-Voiding",
            "food ending": "Food Ending",
        }
        return ending_titles.get(ending_id, "")

    def increment_ending_retry_count(ending_id):
        if not ending_id:
            return

        ending_retry_counts = getattr(persistent, "ending_retry_counts", None)
        if ending_retry_counts is None:
            ending_retry_counts = {}
            setattr(persistent, "ending_retry_counts", ending_retry_counts)

        ending_retry_counts[ending_id] = ending_retry_counts.get(ending_id, 0) + 1

    def get_ending_retry_count(ending_id):
        if not ending_id:
            return 0

        ending_retry_counts = getattr(persistent, "ending_retry_counts", None)
        if ending_retry_counts is None:
            return 0

        return ending_retry_counts.get(ending_id, 0)

label restaurant_deaths:
    label restaurant_1:
        label restaurant_death_1:
            if burger == True:
                #Burgerscene here
                label burger_death_1:
                    n "Now the screaming is also paired with hellish sounds, just great."
                    
                    if not persistent.rockMode:
                        $ _death_seen = check_death_skip("burger_death_1")
                        if is_death_skipped("burger_death_1"):
                            play music game_over
                            jump gameOver
                        elif _death_seen >= death_skip_threshold:
                            play music game_over
                            n "[death_skip_prompt('burger_death_1')]"
                            menu:
                                "Always skip this from now on.":
                                    $ set_death_always_skip("burger_death_1")
                                    jump gameOver
                                "Show the death narration.":
                                    pass
                        n "You look at [persistent.date] and tell [date_obj] to hide under the table."
                        window hide
                        $ flash_screen()
                        window show
                        $ renpy.restart_interaction()
                
                        l "I..."
                        play music game_over
                        
                        $ show_cinematic_bars(sides=["top", "bottom"], size=180, duration=5, curve="ease")
                        $ enable_cinematic_textbox_shift(True)
                        n "Suddenly, the sound of shattering glass. You turn your head to see the window next to your table shatter in a million smaller pieces. The sound of the glass falling on the floor is deafened by the loud murmuring of the other people in the restaurant."

                        n "[persistent.date] seems to be frozen, on [date_pos] face lays a mixture of fear and confusion, clearly displayed. Then something else takes you attention away from [date_obj] face. [persistent.date!c]'s clothes are becoming stained with red the flow rapidly increasing."
                        l "I've been shot?"
                        hide lilith talk_closed with moveoutbottom
                        show burgerRestaurant_bg with hpunch
                        n "[date_sub!c] [conj('date', 'falls', 'fall')] of [date_pos] chair, crashing onto the cold floor."
                        n "Almost immediately all hell breaks loose, the murmuring of the other people has now traded places for panicked screaming as they notice [persistent.date]'s fate."
                        n "You crawl towards [date_obj]. With trembling hands you fish your phone out of your pocket, almost dropping it. You dial the emergency number and beg for help."
                        n "As you stay by [date_obj]'s side, everything seems to fade away. Yes, even the chaotic cries of the crowd. You are purely focused on the dwindling sound of [persistent.date]'s breathing."
                        n "Finally an ambulance arrives after what feels like aeons but in all reality was closer to a minute or five."
                        n "A young man, with eyes that have grown old from all the things they saw, places [persistent.date]'s still body on a stretcher. Dutiful he rushes off with it to the ambulance, you follow closely behind, your legs driven by the adrelaline."
                        n "The kind man throws some words at you, assuring you things will be fine but you can tell he is lying. It's not exactly clear to who. Either he wants to ease your mind or his own."
                        if persistent.lildeaths >= 12:
                            n "It's not exactly like you can blame him, can you? I'm sure you can relate to him with all the death you have seen. Only, he has a chance to save the people he encounters."
                            n "For you it seems as if you are doomed to watch the people you care about in peril perpetually, powerless to protect them."
                        else:
                            n "You have seen [date_obj] suffering for what seemed like an eternity and a second at the same time."
                            n "You have no clue what caused all those gunshots that inadvertently killed [date_obj]. Some robbery in a neighbouring store, or a gang war, or something else."
                            n "Sadly enough you do know what the aftermath of it all is."
                            $ persistent.burger_death_1 = True
                            jump gameOver
                    else:
                        n "This time though, things will turn out different, since [persistent.date] and you are hiding safe and sound under the table. Also, since you are rocks."
                        if persistent.burger_death_2:
                            n "However, the situation is far from over. Still, maybe now things will turn out differently?"
                            n "Surely this rock mode has to be the answer you were looking for, right?"
                        jump restaurant_death_1_prevented
            elif cafe == True:
                #Cafescene here
                label cafe_death_1:
                    if not persistent.rockMode:
                        $ _death_seen = check_death_skip("cafe_death_1")
                        if is_death_skipped("cafe_death_1"):
                            play music game_over
                            jump gameOver
                        elif _death_seen >= death_skip_threshold:
                            play music game_over
                            n "What's to come next is etched into your mind I'm sure, maybe it's better we just skip to how it ends?"
                            menu:
                                "Always skip this from now on.":
                                    $ set_death_always_skip("cafe_death_1")
                                    jump gameOver
                                "Show the death narration.":
                                    pass
                        n "Suddenly someone screams, you barely manage to turn your head fast enough to see a woman fall down with a plate in her hands."
                        n "The plate catapults the ham sandwich that was put on top of it towards the aquarium."
                        n "It appears you aren't the only one who noticed, as a beautiful blue merlin jumps from out from the opening in the aquarium."
                        n "In the middle of both their trajectories, the merlin's long and pointy bill pierces the sandwich in a feat of pure dexterity."
                        n "In a way it's truly magnificent. Sadly it's trajectory ends right in [persistent.date]'s chest, bill first."
                        n "[date_sub!c] [conj('date', 'gives', 'give')] you one last look of utter shock before [date_sub] [conj('date', 'drops', 'drop')] dead on the floor."
                        #TODO: Explore more how the guests themselves react on this death. Also maybe just flesh it out a little bit more?
                        play music game_over
                        $ persistent.cafe_death_1 = True
                        jump gameOver
                    else:
                        jump restaurant_death_1_prevented

            elif chinese == True:
                #Chinesescene here
                label chinese_death_1:
                    if not persistent.rockMode:
                        $ _death_seen = check_death_skip("chinese_death_1")
                        if is_death_skipped("chinese_death_1"):
                            #TODO: Rewrite these death skip prompts for all the deaths.
                            play music game_over
                            jump gameOver
                        elif _death_seen >= death_skip_threshold:
                            play music game_over
                            n "What's to come next is etched into your mind I'm sure, maybe it's better we just skip to how it ends?"
                            menu:
                                "Always skip this from now on.":
                                    $ set_death_always_skip("chinese_death_1")
                                    jump gameOver
                                "Show the death narration.":
                                    pass
                        n "For a moment you get lost in your thoughts."
                        n "You don't have much time to think, as pretty much right at that moment [persistent.date] walks back to [date_pos] chair."
                        l "Heya [persistent.name], I hope you didn't have to wait too long."
                        l "I hope our food will be ready soon, I'm kind of starving."
                        n "Just as [date_sub] [conj('date', 'speaks', 'speak')] those words, almost by magic you can see a waitress heading your way." #TODO: It would be funny if you could ask her not to say those words because "as by magic" the waitress appeared giving her the food she can't eat. This would not end up working but it would be a funny one-off joke.
                        if peking == True:
                            n "She arrives with your double plates of Peking duck, [persistent.date] and you immediately dig in."
                        else:
                            n "She arrives with your orange chicken and [persistent.date]'s peking duck, the two of you immediately dig in."

                        n "[date_sub!c] [conj('date', 'takes', 'take')] a break from [date_pos] food and looks at you for a moment."
                        l "I'm actually glad we could meet here, there's something I want to tell you."
                        n "Before [persistent.date] can finish [date_pos] sentence [date_pos] face starts swelling."
                        play music game_over
                        l "Call an ambulance, now!"
                        n "You frantically grab your phone and dial the number to call one."
                        n "A woman with a warm voice listens to your incoherent ramblings and tries her best to get the details, she sends an ambulance your way." #TODO: Always call this woman? So also when the burger shot happens. Maybe even add some choices? I feel like she could be an interesting side character.
                        n "It arrives quite fast but not fast enough. The doctors conclude the swelling must have been caused by some kind of severe allergic reaction."
                        n "It is odd that [date_sub] still ordered the peking duck. Perhaps [date_sub] [conj('date', 'did', 'did')] not know [date_sub] was allergic to it?"
                        $ persistent.chinese_death_1 = True
                        jump gameOver
                    else:
                        jump restaurant_death_1_prevented
            else:
                "This is an error, if you can see it the location scene for the first death is broken."

        label restaurant_death_1_prevented:
            if persistent.rockMode == False:
                if burger == True:
                    label burger_death_1_prevented:
                        n "[persistent.date] gives you a sceptical look but decides to follow your instructions, right as [date_sub] [conj('date', 'does', 'do')] so a cacophony of hellish sounds begins to seep through the restaurant's entrance."
                        n "You knowingly ignore the noise and instead focus on the window next to your table. It once again shatters in a million smaller pieces. This is where [persistent.date] would have gotten shot, had you not intervened."
                        n "The light of the restaurant gently dances on the shards of glass, almost as if to celebrate your victory."
                        n "Alright that is crazy, how did you know that would happen?"
                elif cafe == True:
                    label cafe_death_1_prevented:
                        n "[persistent.date] studies your face, as if [date_sub] [conj('date', 'is', 'are')] trying to estimate if you are joking or not."
                        l "Eventually [date_sub] [conj('date', 'decides', 'decide')] to not take any chances.
                        [date_sub!c] [conj('date', 'stands', 'stand')] up and moves to your side of the table."
                        l "So..."
                        l "What is this all about [persistent.name]?"
                        n "Before you can answer [date_pos] question you hear a familiar scream, right on cue."
                        n "You turn your head to look at the woman accidentally catapulting the ham sandwhich with her plate as she falls."
                        n "The same trajectorial dance you saw before, the merlin and the sandwhich meeting in the middle."
                        n "This time however the merlin pierces through the chair where [persistent.date] was sitting just mere moments ago instead of [date_obj]."
                        n "The staff quickly rush towards your table they offer [persistent.date] and you a short apology then focus entirely on whether or not the merlin is safe before rushing off with it to a door behind the counter."
                        l "..."
                        n "[persistent.date] looks as if [date_sub] [conj('date', 'has', 'have')] seen a ghost, if you hadn't intervened [date_sub] may have glimpsed [date_pos] own."
                        l "Alright, I'm trying to remain calm but {size=+20}how the {sc=10}{size=+20}hell{/size}{/sc} did you even know that would happen?{/size}"
                elif chinese == True:
                    label chinese_death_1_prevented:
                        $ persistent.dumbo_knowledge = True
                        $ dumboStoryTold = True
                        l "I suppose that could be possible... I am allergic to quite a few things."
                        l "Once as a kid I ate a few peanuts while watching Dumbo, I began swelling up and thought I was becoming a little elephant, just like Dumbo."
                        l "I ran to my parents and said:\"Look mommy, look daddy! I can fly!\" and started using my hands to flap my ears around."
                        l "At that point I was severely swollen so I was lucky my parents saw me before it was too late."
                        l "They rushed me to the hospital where the kind doctors really helped me out."
                        l "When I finally was allowed to go home from the hospital my parents gave me a Dumbo plushie to always remember the story."
                        l "Although I even without the plushie I can remember like it was yesterday, the same counts for my [mom_parShort], she keeps joking about it to this day."
                        n "[persistent.date]  lets out a huge laugh as [date_sub] [conj('date', 'looks', 'look')] at you."
                        n "Suddenly [date_sub] [conj('date', 'stops', 'stop')], you catch a look of worry in [date_pos] eyes."
                        l "Oh... I'm rambling on again aren't I?"
                        l "I'm sorry, it's just that when I start talking it's pretty hard for me to stop, what were we talking about again?"
                        l "Oh yeah, the supposed allergy I would have if I ate that Peking duck."
                        l "How would you even know? I mean, I checked the ingredients on the list and as far as I'm aware I'm not allergic to any of those."
                        l "So let's say that there's something in this dish that I'm really allergic to that I don't know about, how would you?"
                else:
                    "restaurant_death_1_prevented error."
                jump restaurant_death_1_prevented_explanation
            else:
                if burger == True:
                    l "I would have been shot?..."
                   
                    label preventedRockDeath1:
                        l "That image in your mind... That's me as a human?"
                        n "It seems as if your thoughts are not as well hidden as you might like."
                        n "Yet [date_pred] are even harder to pick up on than ever. You can feel them racing all over the place."
                        l "What is going on [persistent.name]?"
                        menu preventedRockDeath1_choice:
                            "You and me are both human in other worlds. In those worlds you kept dying during our dates. That's why I entered this world.":
                                l "There are other worlds?... Where I am human... and I die repeatedly?"
                                l "That's quite a lot to take in all at once. Although it does make me wonder about the logistics."
                                l "You actively chose to enter this world? How did you do that? That hardly seems like something just about anyone could do."
                                menu:
                                    "This is a game and I am the one playing it. I accessed this world via a cheatcode.":
                                        l "...I really shouldn't believe that. It is so outlandish."
                                        l "Alternate worlds were something I could still buy slightly into, but this, it's so far fetched, it couldn't possibly be true, right?"
                                        l "Yet, I can sense it in your mind, you are telling the truth. So all of this is fake? This world, this place, me?"
                                        l "This- this is a lot to process. First the alternate worlds where I'm human and a timeloop, now this?..."
                                        l "Everything I believed turns out to be false."
                                        l "I suppose you did save me by turning me into a rock, since death can't reach me in this form."
                                        l "But is this worth it? I have felt so alone for so long. Wheter or not you meant to, you caused that. Because you wanted to save me."
                                        l "It doesn't even end there, does it? Now even the people I so desperately wanted to reach out to turn out to be nothing but drawings and words on a screen?"
                                        l "Maybe it wouldn't matter so much to me if I already had a connection with them, maybe I would have been able to look past it. But now I can't help but see past the illusion."
                                        l "I wish I could just forget all of this. Ignorance really is bliss."
                                        $ rockMode_toldGame = True
                                        jump restaurant_death_2

                                    "Trust me, telling you now would be way too much to handle.":
                                        l "It would? That only makes me more curious honestly. What is harder to handle than alternate worlds and perpetually dying?"
                                        l "I could read your mind to find out... but I suppose I'll take your word for it."
                                        l "You did lift the veil a little bit so I'll just trust you that this is for the best... for now atleast."
                                        l "I do wonder though, Death can't get me in this form, can it? I'm not even sure if I can die at all."
                                        l "So that means you did it, right? That means you saved me."
                                        l "I guess you did in more ways than just one. With us here together I don't have to feel so alone anymore."
                                        l "It is quite a nice idea isn't it? That we always find eachother, no matter if we are humans, rocks or something else."
                                        l "So thank you [persistent.name], for finding and saving me."
                                        jump restaurant_death_2

                elif cafe == True:   
                    l "I would have drowned?..."
                    jump preventedRockDeath1
                elif chinese == True:
                    l "I would have suffocated?..."
                    jump preventedRockDeath1
                else:
                    "restaurant_death_1_prevented error."
                jump restaurant_death_1_prevented_explanation

    label restaurant_2:
        label restaurant_death_2:
            #Here the code of the second death will be.
            play music game_over
            if persistent.rockMode == False:
                if burger == True:
                    label burger_death_2:
                        $ persistent.burger_death_2 = True
                        $ _death_seen = check_death_skip("burger_death_2")
                        if is_death_skipped("burger_death_2"):
                            $ burger_explosion_outside = False
                            jump gameOver
                        elif _death_seen >= death_skip_threshold:
                            n "What's to come next is etched into your mind I'm sure, maybe it's better we just skip to how it ends?"
                            menu:
                                "Always skip this from now on.":
                                    $ set_death_always_skip("burger_death_2")
                                    $ burger_explosion_outside = False
                                    jump gameOver
                                "Show the death narration.":
                                    pass
                        if not burger_explosion_outside == True:
                            n "Suddenly an immense sensation of pain overwhelms you, you catch a glimpse of pure white that gets replaced by an eternity of black."
                        n "When you awaken you find yourself surrounded by doctors. From what they tell you it sounds like the bullet that would've hit [persistent.date] caused a gas leak instead."
                        n "The gas explosion that followed was quite severe. It ended up destroying most of the restaurant."
                        n "You were in a coma and had to have your wounds cleaned with some surgical procedures. After a week you got out of your coma, [persistent.date] however didn't have such luck."
                        n "The doctors tell you that [date_sub] atleast went out pretty quickly, almost like dying in your sleep... but with more explosions."
                        if death_narration != "":
                            n "[death_narration]"

                        $ burger_explosion_outside = False
                        jump gameOver

                elif cafe == True:
                    label cafe_death_2:
                        $ _death_seen = check_death_skip("cafe_death_2")
                        if is_death_skipped("cafe_death_2"):
                            jump gameOver
                        elif _death_seen >= death_skip_threshold:
                            n "What's to come next is etched into your mind I'm sure, maybe it's better we just skip to how it ends?"
                            menu:
                                "Always skip this from now on.":
                                    $ set_death_always_skip("cafe_death_2")
                                    jump gameOver
                                "Show the death narration.":
                                    pass
                        n "Suddenly you begin to hear the sound of shattering glass."
                        n "As you turn to look at the source of the sound you can see that the aquarium next to where [persistent.date] was sitting has shattered."
                        n "The water is gushing out rapidly and it does not seem to be planning to stop."
                        n "How could this happen?"
                        n "Did the merlin somehow made a crack form?"
                        n "Or was it something else?"
                        n "You think about the pure shenanigans that were needed to even make this exact thing happen but you are soon interrupted by the water flowing past your shoes with some fish coming along for the ride."
                        l "Quick [persistent.name], we need to do something!"
                        if persistent.cafe_death_2 == True:
                            n "You give [persistent.date] a firm hug and tell [date_obj] that there's nothing else you two can do except for waiting."
                            if love_meter >= 3:
                                l "If I have to go now I atleast get some comfort out of the fact that you are here for me."
                                l "Goodbye [persistent.name], thank you for everything."
                                
                            else:
                                n "And so the both of you wait, in eachothers arms, for certain death. And it comes as expected."
                            
                        
                        else:
                            $ persistent.cafe_death_2 = True
                            n "You try to open the main exit of the restaurant but it doesn't seem to be giving in, almost as if something is blocking it."
                            n "Quick! Maybe we can still go to the first floor, we need to go higher!"
                            n "Pretty much without any other option you two decide to make a rush for the first floor of the restaurant."
                            n "When you turn around the corner you see that the stairs are blocked of by an extremely large closet made out of lignum vitae, you can not carry that, all you can do is admire the craftmanship."
                            n "You give [persistent.date] a firm hug and tell [date_obj] that there's nothing else you two can do except for waiting."
                            n "And so the both of you wait, in eachothers arms, for certain death."
                            n "And it surely came."
                        if hugRequestedBeforeDeath == True:
                            n "it seems [persistent.date] got the hug [date_sub] asked for after all, just not in the way [date_sub] thought [date_sub] would."
                        else:
                            if death_narration != "":
                                n "[death_narration]"
                        jump gameOver

                elif chinese == True:
                    label chinese_death_2:
                        $ _death_seen = check_death_skip("chinese_death_2")
                        if is_death_skipped("chinese_death_2"):
                            jump gameOver
                        elif _death_seen >= death_skip_threshold:
                            n "What's to come next is etched into your mind I'm sure, maybe it's better we just skip to how it ends?"
                            menu:
                                "Always skip this from now on.":
                                    $ set_death_always_skip("chinese_death_2")
                                    jump gameOver
                                "Show the death narration.":
                                    pass
                        n "Suddenly there is this faint sound of... quacking?"
                        n "The sound steadily grows louder and louder untill it's all you can hear."
                        n "A true {i}quackophony{/i} if you will."
                        n "[persistent.date] looks over your shoulder at the source of the sound. [date_obj!c] eyes dart wide open in sheer panic."
                        n "When you turn around you see a wave of angry geese breaking through the doors of the once cozy Chinese restaurant."
                        n "Both the guests and staff are running around in utter fear, those that do not blindly panic are trying to make it to the exit. It does not seem like they will make it."
                        n "Before you can make another sound everything turns white, the white of pesky geese feathers."
                        n "You experience a horrible rapid stinging in your side, almost like a thousand tiny pecks. The pain is too much to bear and you fall unconscious."
                        n "When you wake up again all the customers and staff have dissapeared, including [persistent.date]."
                        n "The room is completely filled to the brim with geese feathers, you begin to sneeze just looking at them."
                        n "While you are sneezing you notice that someone put a sticky note on your palm."
                        n "It reads as following: \"We took everyone and you won't be seeing them back. Let this be a lesson on why you should not eat or serve geese. Also ducks, as those are part of our family as well."
                        n "- Sincerely, the geese\""
                        $ persistent.chinese_death_2 = True
                        if death_narration != "":
                            n "[death_narration]"
                        jump gameOver
            else:
                if burger == True:
                    label burger_death_2_prevented:
                        $ persistent.burger_death_2 = True
                        n "Suddenly you are enveloped in a flash of pure white. That must be the explosion. The force of it is enough to send you flying, yet this time you are spared of the pain." #TODO: If you always were outside the restaurant then it probably shouldn't talk about the pain of the explosion.
                        n "When the white subsides you find all that remains are the ruins of the restaurant. The wooden tables are flipped over, flames eating away at them."
                        n "There is screaming and sobbing, but most of all there is death. Even with all the noise in the midst of the chaos the cold and looming silence of death is deafening."
                        n "The burned and scarred survivors are fleeing, dragging their loved ones from underneath the flaming tables, pretending they're still alive."
                        n "However you have enough experience with death to know that it is merely that, pretending."
                        n "Amidst the cacaphony of noises you do manage to pick up one more thing. A voice, calling out to you. [date_pred!c]."
                        l "[persistent.name], are you... alright?"
                        n "However loud the haunting silence of death is, it seems this time it's not [date_pred]."
                        n "Yet that does not mean it isn't yours to carry."
                        jump restaurant_death_2_preventedRockChoice
                
                elif cafe == True:
                    n "Suddenly you hear the sound of shattering glass."
                    n "For a brief moment everyone still remains in blissful ignorance, the conversations obscuring the noise."
                    n "The water begins to stream rapidly, flooding the ground centimeter by centimeter in seconds."
                    n "It does not take long for the talking to die down as people feel their shoes soak up water."
                    n "Most of them are still just mostly annoyed. If they are worried at all, it is merely about the fact their shoes are ruined."
                    n "They all get up from their seats and walk to the exit. However, when the first person in line tries to open the door it doesn't budge at all."
                    n "Another man pushes the man to the side, annoyed that this is going on for longer than it has to. When he too tries to open the door to find it unmoving he audibly gulps."
                    n "The barista barely manages to utter the words \"Don't panic.\" through his stutters."
                    n "In truth, nothing he could have said would have helped. However, hearing the sheer stress in his voice only further drives the people into blind panic."
                    n "One group attempts to smash through the double glazed windows with the heaviest things they can find."
                    n "Another group is trying to move away the closet blocking the stairs so they can escape to higher grounds."
                    n "Sadly both groups make close to zero progress when the water already is up to their chests."
                    n "For some this literal deadline motivates them to try even harder and yet others seem to lose all will to fight because of it."
                    n "They seek their friends, partners, or just about anyone who gives them some semblance of comfort in this hell and embrace eachother, exchanging their final goodbye."
                    n "The water has now fully swallowed everyone, reaching up unto the ceiling. You can see the people slowly extend their last breaths as they then lay motionless on the floor."
                    n "Where merely moments ago the cafe was filled with screams of pure panic, now merely rests a haunting silence."
                    n "Then you hear it, [date_obj]. [date_pos!c] voice echoing in your mind."
                    l "Are you alright [persistent.name]?"
                    jump restaurant_death_2_preventedRockChoice

                elif chinese == True:
                    n "You once again hear the faint sound of quacking."
                    n "It steadily grows louder and louder until it's all you can hear."
                    n "A true {i}quackophony{/i} if you will."
                    n "[persistent.date] mind races with pure panic."
                    n "Yet you stay relatively calm, as you already know what will happen. When the staff begins running around in sheer panic you know {b}they{/b} have arrived."
                    n "Before you can think another thought everything turns to white, the white of pesky geese feathers."
                    n "You get flung far away from the sheer force of an army of geese. This time however, you don't feel any pain and stay fully conscious. However, the others are not so lucky."
                    n "Enveloped in the pure whiteness you hear the bloodcurdling screams of all the people overpower the loud quacking, if only for a brief moment."
                    n "You are not sure whether the screams quieted because the people fell unconscious or because they died. Somehow you know that the first option might be the worst fate."
                    n "When the feathers finally clear you once again find the entire restaurant empty."
                    n "Empty of people that is, because the room is filled to the brim with feathers."
                    n "This time, the geese did not leave a note in your hand. This time you also do not have any hands for them to do so."
                    n "Then you hear it, [date_obj]. [date_pos!c] voice echoing in your mind."
                    l "Are you alright [persistent.name]?"
                    jump restaurant_death_2_preventedRockChoice

menu restaurant_death_2_preventedRockChoice:
    "I'm fine, but what about you?":
        l "Thank god, I was so worried I'd have lost you."
        if burger:
            l "I'm mostly fine I think, I got flung across the restaurant but it didn't hurt at all."
            l "I suppose not feeling anything has some perks afterall."
        elif cafe:
            l "I'm mostly fine I think, the stream just slightly carried me away."
            l "I'm for once glad I don't have lungs, or a mouth, or... well you get the point."
        elif chinese:
            l "I'm mostly fine I think, just burried underneath all these... feathers?"
            l "This might be one of the few times I'm glad I don't have a nose."
        jump preventedRockChoice_casualties

    "I'm fine, but what about these other people?":
        #TODO: Don't have him go through this narration each time, it is a one-off thing. Probably make an array for narrator rants so I can more easily check if they have already been seen or not instead of using a bunch of booleans.
        n "Curious. I do wonder what makes you care for these people now."
        n "You didn't think the restaurant was empty all those other times, did you?"
        n "So what makes now any different from those [persistent.burgerwent] other times?"
        n "I suppose our problems only become problems when we become aware of them."
        n "Otherwise it's just a blur right outside of the corner our eye."
        n "Now it will be even harder to pretend that you are doing this for selfless reasons, won't it?"
        n "I suppose ignorance truly is bliss to you, isn't it player?"
        n "Because to not know is to believe what you want. Yet to know is to define, to confine."
        n "Now the truth can't be conveniently altered, can it? From now on, these people will suffer, they will die, each time you come here."
        n "I do wonder if that matters to you though, and if it does I wonder how long that will last."
        n "Because at the end of the day, they are just words and images to you, aren't they player?"
        n "I suppose I can't blame you for viewing them like that. Still, you do know [persistent.date] is the same, don't you?"
        n "Then what makes you go through all this trouble? Through all this death?"
        n "Are you doing this just to see everything this game has to offer? Or is this truly about saving [date_obj]?"
        n "Don't bother answering, we've already been at this for too long and the result is the same either way."
        n "Now, let's move on."
        l "It's horrible isn't it?"
        jump preventedRockChoice_casualties

label preventedRockChoice_casualties:
    if burger:
        l "I'm glad we are fine, but the people, god- they once were people but now it's hard to see them as such while they are covered in debris and ash."
        l "Is it always like this? I just hope this time no-one... died."
        l "We are fine, well, as fine as one can be after something like this, but when I see all of them suffering I wish I could do something, anything, to help."
        l "Yet they can't hear us, nor can we reach out to them to try to comfort them. Even then, I don't think that would work, not at a time like this."
        l "They will need time, although they might never be the same again. That explosion blasted them away from their lives trajectory."
        l "Seeing this... Is all of that worth it just to save me?"
    elif cafe:
        l "I'm glad we are fine, but these people, god- it's hard to see them as such. Mere moments ago they were still people, but now they are just corpses."
        l "The life in their lungs having been replaced by fishwater."
        l "The fish that needed that water also passed. They were so beautiful swimming around and now it's hard to even imagine they ever moved at all."
        l "We are fine, well, as fine as one can be after something like this, but an aura of death has unmistakably marked this place. There is no pretending otherwise."
        l "Seeing this... Is all of that worth it just to save me?"
    elif chinese:
        l "I'm glad we are fine, but those people, god- their screams were too much to bear."
        l "What did those geese do to them? Are they dea- Are they fine?"
        l "On one hand maybe it's for the better we can't see what happened to them."
        l "Still, not seeing also makes your mind just think up much worse scenarios."
        l "Somehow I get the feeling that if they are alive they might wish they weren't."
        l "It's this distant pain coming from my liver... which is strange since I'm fairly certain we don't have livers."
        l "I have to ask... Is all of this worth it just to save me?"
    jump preventedRockChoice_casualties_2

label preventedRockChoice_casualties_2:
    l "In that other world you were talking about, the one where we are both human, couldn't we have warned them?"
    l "Couldn't we have prevented this? Yet you abandoned that world for this one where we can't?"
    #TODO: Make this an option in the restuarants itself? (Think about it beforehand whether or not it is meaningful.)
    l "...I- I need some time to think about this [persistent.name]. I think it's better if we took some time apart."
    #TODO: Add a little bit of narration inbetween here.
    n "Eventually you hear back from [date_obj] again."
    if rockMode_toldGame == True:
        l "I have made up my mind. This is not worth it at all, [persistent.name]."
        l "What is the point of this? You have saved me but you did so at the cost of locking me in a cage of loneliness."
        l "At the cost of all those innocent people we otherwise might have been able to warn."
        l "I know they are not real, that you might use that as an excuse."
        l "However, I'm not real either [persistent.name]. What makes my life worth more than all of theirs?"
        l "..."
        l "Can't you see? In whatever world we meet death and destruction always follow."
        l "I think it's better if we go our separate ways."
        l "Now leave me be, I have to mourn for all these people equally real as myself."
        n "Mourn for them [date_sub] did, for all of eternity. No matter how many times you tried to reach out all you felt in [date_pos] mind was a deep sadness."
        l "Sadness for the souls [date_sub] knew were merely words like [date_obj]. Less words, but words all the same."
        jump gameOver
        
    else:
        l "I'm sorry for dissappearing for so long."
        l "Knowing what happened to all those people, that we could have maybe prevented it..."
        l "...that was just too much to bear. Still, we can't undo what has been done."
        l "We can however try to make sure it never happens again."
        l "Please promise me you'll try to save as many people as you can each time."
        menu:
            "I promise.":
                l "Thank you [persistent.name], that means a lot."
                l "Besides, if I am being honest I did miss talking to you."
                l "It's strange, I've been on my own for so long. You'd think I got used to it, but it's hard to go back."
                l "So you've never seen past this point before, right? Does that mean the timeloop is broken?" #TODO: How does she know that? Did the player tell her? Check that to make sure.
                l "If so we better make the best out of it, right?"
                jump rockMode_neverEnding

label rockMode_neverEnding:
    n "So [persistent.date] and you did exactly that, living each new unseen day as if it were your first and last."
    n "The death and destruction that the loop brought along did not seem to cease. Through all your time travelling together disaster always was the third travelpartner in your duo."
    if rockMode_rockBand:
        #Changeableword here is the rockband name
        n "Together you started dreaming up songs based on the things you saw for [changeableWord]. These songs were intimate, projects only ever heard in your minds."
        n "There was always some hope that someone else might hear, but if they did they never made it known to you. Still, in truth the two of you knew the songs were just for you so it really didn't matter much."
    n "Your adventures grew more and more isolated from other people as to not have them accidentally be involved in that destruction."
    n "You could say that it was a deeply lonely existence. Luckily you had [date_obj] as [date_sub] had you."
    n "That made it a whole lot less lonely. Together you'd watch the world you knew slowly but undeniably replace bits and pieces of itself until there's nothing left of the original world you remembered."
    n "Around this time it grew harder and harder to find things to tell [persistent.date]. Based on the sometimes weekslong silences, you guess [date_sub] felt the same."
    if rockMode_rockBand:
        n "Even the music the two of you once constantly made had been slowly dwindling down in its rapid creation."
    n "It's not that you don't want to desperately break that silence but you have already spoken every possible sentence you could think of a hundred times before. Every unique moment has already been relived countless times."
    n "The two of you have delved deeper into eachother than anyone ever had or would, and you have reached the bottom."
    n "Luckily the new world brought some distraction from that truth. It brought something to delve into other than eachother." 
    n "The two of you explored the new world, every piece your unwanted tag-along permitted you to. That new world gave you new things to discuss once more."
    n "However that only was a temporary solution, the new things of that world ran out more rapidly than one would have thought."
    n "Then the process repeats itself with the next new world, and the one after that. Afterall, you got nothing but time."
    n "This went on and on until you began seeing patterns in these worlds that were supposed to be fresh and exciting."
    n "At first you didn't mind, as it was merely some aspects you began to recognise here and there, others were still plenty unknown and exciting to discover."
    n "Still, sooner than later you began to recognise more things than you didn't."
    n "Eventually things began to grow stale, boring. The few things the two of you could still talk about grew as repetive as the rest."
    n "The two of you stopped talking, not just for weeks, but for months, years. Possibly decades, at this point it was very hard to tell the flow of time."
    n "Most of the time you just found yourself tuning all of reality out, sleeping without needing to sleep. Letting it all wash over you without ever even being conscious of whatever washed over you."
    n "One of the only things that drew you out of your daze were disasters, those were harder to predict than afterall. Those still were something to marvel at, albeit with a slight bit of shame for watching something so sick."
    n "Floods, supervolcanic eruptions, gigantic earthquakes, the evaporation of the oceans. The end of all complex life."
    n "Yet you kept existing, so did [date_sub]. The two of you only awoken during these horrible disasters. After a while the smaller ones even not disturbing your deep slumber anymore."
    n "During these moments of waking you were confused, dazed. Not sure of who, or what you were anymore. Even then the pain in your mind deterred you from trying to figure that out for too long."
    n "The only thing you are sure of is that you were once human, then you were a rock and now you are merely atoms that once were a rock that once was a human."
    n "The flow of time combined with these disasters not killing you, but slowly eroding you into many different pieces. Each piece being sentient, enough to be aware of the pain of being so."
    n "Those pieces don't float, or fly, or anything like that. They just are, sometimes in different places than where they were."
    n "Sometimes one of those pieces, out of sheer coincidence happens to be somewhere where a part of [persistent.date] is."
    n "They know each piece of [date_obj] better than themselves. Likewise, that piece knows them better than [date_pred]."
    n "So they just silently float by. Reacting no different than if either party weren't part of this meeting of pure chance."
    n "But one day this meeting goes differently. One of your pieces suddenly feels something bubble up inside of them."
    n "A sense of recognition. A deep loneliness it tried sleeping through."
    n "Yet most importantly, a promise it had made. In this lifetime, or in another? It was hard to say."
    n "Even the promise itself was hard to think of, except that it was just that, a promise. The concept was almost too big to grasp but this tiny piece of sentient rock found itself thinking one word."
    n "One word that would start it all over again."
    #Ending
    $ persistent.ending_quitter = True
    $ lilithAliveEnding = True
    $ ending_check = "neverEnding"
    $ persistent.rockMode = False
    jump gameOver             

label car_death:
    $ persistent.runAwayLilith_counter += 1
    if angryLilith == True:
        n "[persistent.date] stands up from [date_pos] seat, shoving it back with a frightening speed."
        if noTalkAngryLilith == False:
            l "I really didn't want it to come this far but you left me no other choice [persistent.name]."
            if major_love_offence >= 1:
                l "I just have one question for you."
                l "Why go on this date with me at all?"
                l "I was really looking forward to this date, but I'm not sure I can say the same for you."
                l "If you really wanted this, then why were you so rude to me?"
                l "Don't bother answering that [persistent.name], no answer you could give would ever change what I'm going to do next."
            elif minor_love_offence >= 2:
                l "I could endure one rude remark, even though I probably shouldn't."
                l "I guess I stayed because I hoped things would get better."
                l "Perhaps I also did because it's been so long since my last date..."
                l "Yet now I see that's just sunk cost fallacy speaking. Sometimes it's just better to rip off the bandaid, even if it might hurt a little."
                l "Besides, as much as I owed it to myself to go on this date, I also owe it to myself to cut it short right now."
            l "Goodbye [persistent.name], and a tip for the future: if you ever go another date, try to develop manners beforehand. "
            if persistent.lildeaths >= 1:
                n "I guess we will very soon see whether or not that's possible, right player?"
    else:
        n "[persistent.date] stands up from [date_pos] seat and starts heading for the exit without paying."
        l "Goodbye [persistent.name]."
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
            n "[persistent.date] leaves the burger restaurant, you rush after [date_obj] in an effort to calm [date_obj] down."
            n "This time there is no red Sedan in sight, it seems as if the cops handled it well."
            n "However, just as you're processing that your mind wanders to the gas explosion that always appears arround this time."
            n "It was probably not a good idea to come here."
            n "That is your last thought as you feel everything fade to black after you hear the explosion."
            $ burger_explosion_outside = True
            jump restaurant_death_2

        elif cafe == True:
            $ _death_seen = check_death_skip("car_death_cafe")
            if is_death_skipped("car_death_cafe"):
                jump gameOver
            elif _death_seen >= death_skip_threshold:
                n "What's to come next is etched into your mind I'm sure, maybe it's better we just skip to how it ends?"
                menu:
                    "Always skip this from now on.":
                        $ set_death_always_skip("car_death_cafe")
                        jump gameOver
                    "Show the death narration.":
                        pass
            n "[persistent.date] leaves the cafe, you rush after [date_obj] in an effort to calm [date_obj] down. "
            n "When you set one foot outside of the doorframe the red Sedan, which always thwarts your plans, drives head first into the both of you."
            n "Luckily you managed to get flung to the side somehow. [persistent.date] however was not so lucky."
            n "[date_sub!c] died on impact when the speeding Sedan hit [date_obj]."
            n "Atleast the police showed up due to your call and locked the drunkard up. If only they managed to do so a little earlier..."
            n "It was probably not the best idea to go here with [persistent.date] with the car still on the loose."
            jump gameOver


        elif chinese == True:
            n "[persistent.date] leaves the chinese restaurant, you rush after [date_obj] in an effort to calm [date_obj] down."
            if persistent.chinese_car_death == True:
                "This time there is no red Sedan in sight, it seems as if the cops handled it well."
            if angryLilith == True:
                l "Leave me alone [persistent.name]! I don't want to see you ever again!"
            else:
                l "Why are you following me [persistent.name]? I want to be alone." 
            n "With that [persistent.date] leaves, never to be seen again. Not this time anyway."
            n "Atleast [date_sub] seems to have survived since you still hear people talk about [date_obj] from time to time."
            if persistent.lildeaths > 15:
                n "You are unsure of how to feel. As horrible as that date went, [date_sub] [conj('date', 'is', 'are')] still alive."
                if persistent.lilithAliveAndRetriedCounter == 0:
                    n "Does this mean that you won?"
                    n "That you can stop trying to save [date_obj]?"
                #TODO:: If you have seen "better" endings and retried, comment on this

            $ lilithAliveEnding = True
            $ persistent.ending_badDate = True
            $ ending_check = "badDate"
            $ persistent.lildeaths -= 1
            $ persistent.gallery_unlocked = True

            if angryLilith == True:
                n "You probably shouldn't have angered [date_obj] so much."
            else:
                if explanationAsked:
                    if groundhog == False and psychic == False:
                        n "Maybe you should give [date_obj] a different explanation?"
                    else: 
                        if groundhog == True:
                            if persistent.groundhog_answer_right_knowledge == True:
                                n "Now next time you can give [date_obj] the number [date_sub] [conj('date', 'was', 'were')] thinking of."
                            else: 
                                n "Maybe you need to give some proper proof."

                        elif psychic == True:
                            if persistent.psychic_answer_right_knowledge == True:
                                n "Now next time you can tell [date_obj] the word [date_sub] [conj('date', 'was', 'were')] thinking of."
                            else: 
                                n "Maybe you need to give some proper proof."
                else:
                    n "You should probably try something else next time."

            jump gameOver



    else:
        if currentcar == True:
            n "[persistent.date] leaves the [resname], you can not bare seeing what happens next so you decide to stay inside."
            n "Even from inside you can still hear the car crash into [date_obj]."
        else:
            $ currentcar = True
            if persistent.redSedan_knowledge == True:
                $ carDescription = "the same red Sedan that you encountered before"
            else:
                $ carDescription = "a red Sedan"
            if angryLilith == True:
                n "[persistent.date] leaves the [resname], you rush after [date_obj] in an effort to calm [date_obj] down."
                
            else:
                n "[persistent.date] follows you to the exit of the [resname]." #TODO: For some reason if you make her angry and she leaves in the chiense restaurant this part also plays while this shouldn't play
            n "When you set one foot outside of the doorframe [carDescription] drives head first into the both of you."
            label car_death_result:
                $ _death_seen = check_death_skip("car_death_" + resname2)
                if is_death_skipped("car_death_" + resname2):
                    jump gameOver
                elif _death_seen >= death_skip_threshold:
                    n "What's to come next is etched into your mind I'm sure, maybe it's better we just skip to how it ends?"
                    menu:
                        "Always skip this from now on.":
                            $ set_death_always_skip("car_death_" + resname2)
                            jump gameOver
                        "Show the death narration.":
                            pass
                n "Luckily you managed to get flung to the side somehow. [persistent.date] however was not so lucky."
                n "[date_sub!c] died on impact when the speeding car hit [date_obj]."
                if persistent.redSedan_knowledge == False:
                    $ persistent.redSedan_knowledge = True
    jump gameOver

label kokiri_deaths:
    label angryLilith:
        if angryLilith:
            $ persistent.runAwayLilith_counter += 1
            if major_love_offence >= 1:
                n "[persistent.date] jumps up from where [date_sub] [conj('date', 'was', 'were')] lying mere moments ago, on [date_pos] face a visible layer of anger or... disappointment?"
                n "You're not sure which one would sting more. [date_sub!c] [conj('date', 'wipes', 'wipe')] the crumbs on [date_pos] clothes away with a frightening speed and angrily [conj('date', 'storms', 'storm')] down the hill."
                if noTalkAngryLilith == False:
                    l "Goodbye [persistent.name], we are done here."
                    l "Do not come back for extra attempts if you have even the slightest sliver of respect for me."
                $ persistent.kokiri_angry_noretry = True
            elif minor_love_offence > 1:
                n "[persistent.date] stands up from where [date_sub] [conj('date', 'was', 'were')] lying mere moments ago. Displayed on [date_pos] face is a disappointed look."
                if noTalkAngryLilith == False:
                    l "This might all be a game for you [persistent.name], but it's my life."
                    l "So I'd like to be treated with the respect you would give a real person."
                    l "You need to learn that your actions have consequences, even in something as simple as a game."
                    l "I'm leaving now. Don't try to follow me, there's nothing you can say to me right now to change my mind."
                    l "Besides, you can just retry right? I'd prefer if you didn't, but it's not like I can stop you."
                    l "Let's just hope that if you come back here you will have learnt your lesson."
                    l "Goodbye [persistent.name]."
        n "[persistent.date] turns her back to you and walks down the hill cool and collected. It seems [date_sub] [conj('date', 'has', 'have')] made up [date_pos] mind about this."
        n "[date_sub!c] [conj('date', 'does', 'do')]n't get much further than a meter or ten before tripping over a tree root."
        n "[date_sub!c] [conj('date', 'does', 'do')] not get up."
        play music game_over
        $ _death_seen = check_death_skip("angryLilith_death")
        if is_death_skipped("angryLilith_death"):
            jump gameOver
        elif _death_seen >= death_skip_threshold:
            n "What's to come next is etched into your mind I'm sure, maybe it's better we just skip to how it ends?"
            menu:
                "Always skip this from now on.":
                    $ set_death_always_skip("angryLilith_death")
                    jump gameOver
                "Show the death narration.":
                    pass
        if persistent.kokiri_angryLilithDeath == False:
            n "When you rush to [date_obj] you notice why. [persistent.date] horribly hit [date_pos] head pretty on a small rock."
            n "The end result looks horifying. You call an ambulance but when they arrive they tell you what you already knew deep down." #TODO: Here add a choice menu where it's the same lady as the other times you call an ambulance.
            n "[date_sub!c] didn't make it."
            $ persistent.kokiri_angryLilithDeath = True
        else:
            n "Deep down you already know it is too late."
            n "Yet you can't help yourself, you call an ambulance hoping that this time is somehow slightly different."
            n "That [date_sub] will still be alive by the time they arrive."
            n "After what feels like waiting for years the ambulance finally arrives."
            n "Sadly they tell you the same news they've already told you before."
            n "[date_sub!c] didn't make it."
        jump gameOver

    label kokiri_1:
        label kokiri_death_1:
            if met_check != "meteorite_warn":
                if kokiri_call_death_1_check == False: #If she wasn"t calling her mom/sis during this death:
                    if kokiri_silentMoment == False:
                        n "[persistent.date] stops talking for a moment as [date_sub] [conj('date', 'stares', 'stare')] at the star-filled night."
                    else:
                    
                        n "[persistent.date] diverts [date_pos] eyes from yours for a moment and continues watching the star-filled night."
                    n "A gasp of amazement escapes [date_pos] mouth."
                    l "Look, isn't it absolutely amazing?"
                    n "The sky is completely filled with falling stars. Throughout all of your life you haven't seen that many, let alone all at once."
                    n "What does catch your eye however is one growing point of light that seems to get bigger and bigger."
                    if kokiri_alternateplace == False:
                        n "The both of you watch in absolute terror as the thing still increases in size at an alarming rate, it's trajectory seemingly leading to the hill the two of you are sitting on."
                        n "You can now clearly make out what is a decently sized meteorite."

                    else:
                        n "The both of you watch as it comes closer and closer, rapidly growing in size."
                        n "You can now clearly make out what is a decently sized meteorite."
                        n "Eventually due to the energy exerted on the meteorite it breaks into many different chunks that spread all around the forest."
                        n "None of the pieces manage to hit [persistent.date] this time."
                        n "For a brief flash you are reminded of how things ended before."    
                        n "But then you realise something, now that [date_sub] [conj('date', 'is', 'are')] safe this is actually a lovely sight."
                        n "Something you could only experience once in a lifetime."
                        n "Yet you will experience it a lot more than that, won't you?"      
                        jump kokiri_death_1_prevented
                
                play music game_over
                $ _death_seen = check_death_skip("kokiri_death_1")
                if is_death_skipped("kokiri_death_1"):
                    jump gameOver
                elif _death_seen >= death_skip_threshold:
                    n "What's to come next is etched into your mind I'm sure, maybe it's better we just skip to how it ends?"
                    menu:
                        "Always skip this from now on.":
                            $ set_death_always_skip("kokiri_death_1")
                            jump gameOver
                        "Show the death narration.":
                            pass
                n "Eventually, due to the energy exerted on the meteorite it breaks into many different chunks that spread all around the forest."
                n "One of them crashes against [persistent.date]'s head with a frightening impact."
                n "[date_sub!c] immediately [conj('date', 'goes', 'go')] limp and [date_pos] body falls down on the picnic blanket."
                if persistent.kokiri_death_1 == True:
                    n "You close your eyes in an effort not to subject them to the straight up terrifying state [persistent.date] is in right now."
                    n "The effort is futile as [date_pos] your eyelids are still engraved with the sight they now try to hide."
                    n "How could they not? [date_pos!c] corpse haunts your every waking thought."
                    n "Deep down you already know it's too late. In your mind you have already categorised [date_pos] corpse, designated [date_pos] as dead."
                    n "Yet you still hope you will be proven wrong, that [date_sub] might give any signs of life."
                    n "However, no matter how long you wait in all usurping silence, not a single sign shows itself."
                    if kokiri_call_death_1_check == True: #Check whether or not she was calling someone at the time of her death.
                        if kokiri_chatchar_abigail_called == True:
                            n "You can vaguely sense [persistent.date_sis]'s screams but the silence almost completely drowns them out."
                        elif kokiri_chatchar_lila_called == True:
                            n "You can vaguely sense [persistent.date_mom]'s screams but the silence almost completely drowns them out."
                    n "It's hard to imagine the forest felt so lively mere moments ago since now all that remains is loneliness and cold."
                    n "You lay down next to [persistent.date] in a futile effort to get rid of that terrible feeling, to cope with the situation."

                else:
                    $ persistent.kokiri_death_1 = True
                    n "Hurriedly making your way closer you worriedly watch over the scene. [date_pos!c] head cracked open and a puddle of blood is pooling beneath it. Everything around you turns silent."
                    if kokiri_call_death_1_check == True: #Check whether or not she was calling someone at the time of her death.
                        if kokiri_chatchar_abigail_called == True:
                            n "Even [persistent.date_sis] who is currently screaming [sis_pos] lungs out has become unbearingly silent. Yet make no mistake, [sis_sub] is still going strong."
                            n "You would like to join [sis_obj] but all that manages to come out is the same silence that seems to have overtaken the forest."
                        elif kokiri_chatchar_lila_called == True:
                            n "Even [persistent.date_mom] who is currently screaming [mom_pos] lungs out has become unbearingly silent. Yet make no mistake, [mom_sub] is still going strong."
                            n "You would like to join [mom_obj] but all that manages to come out is the same silence that seems to have overtaken the forest."
                    else:
                        n "You would like to scream but all that manages to come out is the same silence that seems to have overtaken the forest."
                    n "It's almost as if the forest itself is mourning [persistent.date]."
                    n "Some dark clouds move in front of the moon as if to stop it from revealing the scene any further."
                    n "They are rather unsuccessful.Even if they had succeeded you surely still could see [date_pos] body engraved in your eyelids."
                jump gameOver
            else:
                jump kokiri_death_1_prevented
        
        label kokiri_death_1_prevented:
            #if kokiri_prevented == 1: This is code that would have made it so that it triggers based on 1-4 and the deaths.
            if not kokiri_alternateplace:
                n "[persistent.date] nods as [date_sub] [conj('date', 'moves', 'move')] more to the left of the blanket."
                l "Odd request, but I guess we will see why I needed to do that soon enough, right?"
                n "Right at that moment something catches [date_pos] eye. The sky is once again filled with bright falling stars."
                l "Look, I never saw that many in my entire life!"
                n "That's rather a funny thought since [date_sub] [conj('date', 'has', 'have')] sees this many in all [date_pos] lifetimes here."
                n "Yet those are not the important ones.Soon [date_sub]'ll get to see one from really close, let's hope this time it doesn't kill [date_obj]."
                n "It doesn't take long at all before you notice a familiar point in the sky getting bigger and bigger at a frightening speed."
                n "[persistent.date] watches in absolute terror as [date_sub] now can clearly make out a decently sized meteorite heading straight to the hill the two of you are sitting on."
                n "Meanwhile all you can do is hope that things are going to be different this time. They should, but you still find yourself fearing the worst."
                n "Eventually due to the energy exerted on the meteorite it breaks into many different chunks that spread all around the forest. One of those very pieces would have hit [persistent.date]'s head if [date_sub] hadn't moved, instead it now fell into the lake next to the hill."
                n "[persistent.date] gives you a startled look. Even only lit by the moon and the stars it is not hard to tell [date_sub] [conj('date', 'has', 'have')] become as pale as the light."
                l "...A meteorite? That was what was going to kill me now?"
                n "[date_sub!c] [conj('date', 'goes', 'go')] quiet for a moment."
            else:
                l "That was beautiful... I've never seen anything like that."
                n "[date_sub!c] [conj('date', 'has', 'have')] many many times, and will many many times more. Even then, [date_sub] will get to experience it for the first time on each date. I suppose ignorance is bliss isn't it?"
                l "...So we sat here because of the meteorite? Would it have killed me?" #TODO: If you asked about a different place during this run have her say something like "so you asked to sit somewhere else because of that meteorite?"
                n "[date_sub!c] [conj('date', 'looks', 'look')] you straight into your eyes, seemingly having found the answer in them."

            l "So you spoke the truth... I keep on dying over and over on this date?"
            l "Huh... seems like luck is not on my side today."
            l "Although with you on my side things are looking up. Once again, thank you for saving me."
            n "[persistent.date] pauses for a moment and gives you an odd look."
            l "Can I put the levity aside for a moment and be honest with you?"
            l "You might think I'm taking this remarkably well, but that's just how I come off under pressure."
            l "I have a bad tendency to minimise things, probably so they feel more under control. I have been working on it lately but it still flares up from time to time."
            l "This- It's a lot to deal with right now."
            l "I knew {i}something{/i} strange was going on when you told me about the kokiri forest."
            l "I suppose that's why I even agreed to meet up, to figure out what that something was."
            l "Yet even just now when you explained it, a part of me didn't believe you."
            l "No, it didn't want to believe you. Because deep down it knew you were telling the truth..."
            l "Can you give me a moment to collect my thoughts, [persistent.name]?"
            l "We can continue talking after that, but right now I feel like I'd be a pretty lousy conversationalist."
            n "As you give a slight nod, the corners of [persistent.date]'s mouth move up with a thankful smile, it's so subtle it almost slipped by."
            n "After a while [date_sub] [conj('date', 'shifts', 'shift')] slightly wand [conj('date', 'gives', 'give')] you a nod."
            l "I think I'm ready, well, as ready as I'll ever be anyway."
            l "Thank you for that, and for staying with me. It helped me feel a bit better, as much as someone in this situa- you get what I mean."
            if car_caught == False:
                jump kokiri_death_2
            else:
                jump kokiri_death_2_prevented

    label kokiri_2:
        label kokiri_death_2:
            play music game_over
            $ _death_seen = check_death_skip("kokiri_death_2")
            if is_death_skipped("kokiri_death_2"):
                jump gameOver
            elif _death_seen >= death_skip_threshold:
                n "What's to come next is etched into your mind I'm sure, maybe it's better we just skip to how it ends?"
                menu:
                    "Always skip this from now on.":
                        $ set_death_always_skip("kokiri_death_2")
                        jump gameOver
                    "Show the death narration.":
                        pass
            if kokiri_alternateplace == True:
                if kokiri_call_death_2_check == True:
                    n "While [persistent.date] is engrossed in [date_pos] call you notice the red Sedan that rode up the hill and hit [persistent.date] riding up the hill once again."
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
                n "You would like to think you would pick fight and push [persistent.date] out of the way, sacrificing yourself for [date_obj]."
                n "And yet you instinctively pick flight as you jump away from the car."
                n "Sadly it seems [persistent.date] did not do the same, [date_sub] instead froze."
                n "And now [date_sub] [conj('date', 'is', 'are')] forever frozen as [date_sub] [conj('date', 'lays', 'lay')] there on the floor, unmoving."
            if kokiri_call_death_2_check == True:
                #TODO: Here add a choice menu where it's the same lady as the other times you call an ambulance. Also have an option to not call the ambulance and instead spend more time with her dying.
                if kokiri_chatchar_abigail_called == True:
                    n "You call an ambulance with shaking hands as you hear [persistent.date_sis]'s neverending screaming coming from [persistent.date]'s phone."
                elif kokiri_chatchar_lila_called == True:
                    n "You call an ambulance with shaking hands as you hear [persistent.date_mom]'s neverending screaming coming from [persistent.date]'s phone."
            else:
                n "You call an ambulance with shaking hands."
            n "Your suspicion was proven true by the paramedics, [date_sub] [conj('date', 'was', 'were')] dead as soon as that car hit [date_obj]."
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
            n "You tell [persistent.date] about how the red Sedan would've hit [date_obj] if you wouldn't have called the police."
            if kokiri_alternateplace == False:
                if kokiriSceneryWatched == True:
                    $ carDescription = "that car we just watched"
                else:
                    $ carDescriptiion = "a car"
                l "I see... first a meteorite and now [carDescription]?... It almost seems like the universe has it out for me today..."
                l "Thank you for going through such efforts to help me [persistent.name]."
                n "[persistent.date] gives you a big smile, a look of gratitude is plastered across [date_pos] face."
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
                "I tried everything [persistent.date], I even took you to space but it didn't work out, no matter which path I choose you still end up dying." if persistent.reality_knowledge:
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
                    l "I had to deal with both my [dad_par] and my [ghost_sib] leaving, albeit in very different ways."
                    l "I guess this feels refreshing?"
                    l "Deep down I guess I always blamed myself for what happened, for them leaving."
                    l "As if there some curse cast on me that would make all my loved ones leave me."
                    l "If anything, I am thankful that I now have another piece of evidence proving the opposite whenever I experience that thought again."
                    l "So thank you very much for that [persistent.name], that means more to me than I could ever express fully."
                    n "Things grow quiet for a little. You see [persistent.date] thinking about something."
                    l "I'd like to show you something."
                    jump kokiri_pictureChoice

                "We're running out of time. Could we please keep talking?":  
                    l "Sure, what would you like to talk about?"
                    $ showContinueTalk()
                    if showContinueTalkKokiri:
                        menu:
                            "*Continue talking.*":
                                jump kokiri_continue_talking
                            "*Talk about something else.*":
                                jump kokiri_talkAboutSomethingElse
                    else:
                            jump kokiri_talkAboutSomethingElse
                    
label kokiri_death_2_prevented_triedEverything:
    p "I tried everything I could think of [persistent.date]."
    p "I've fled from death with you, even going as far as flying away from the earth with a spaceship only for reality itself to collapse."
    if persistent.ending_breakup == True:
        p "I might have been selfish, in one timeline you end up with a guy called Ron and you two just have a great time together."
        p "But that wasn't enough for me, I want to go on this date and have you come out of it alive and well."
    p "I just want to share a nice, enjoyable date with you."
    n "[persistent.date] points at the village, illuminated by the moon and the stars."
    l "With such a marvelous view I would surely call this a nice, enjoyable date."
    n "[date_sub!c] [conj('date', 'snuggles', 'snuggle')] up to you."
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
            l "[date_sub!c] [conj('date', 'pauses', 'pause')] for a moment and then [conj('date', 'continues', 'continue')]."
            l "We tend to create these new worlds all the time, sometimes even without realising it."
            l "When you are thinking about what the next season of your favourite show will be about then you're technically creating an entire new world where the show's characters go through your story."
            l "And who's to say which version is the superior one? After all, they're both telling a story, personally I think that's absolutely beautiful."
            l "So let's try to do just that!"
            n "[persistent.date] hugs you for a long period of time, you feel [date_pos] warmth as it reaches your cold body."
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
                        n "[persistent.date] looks at you with a puzzled look on [date_pos] face."
                        l "Oh... I thought you had already started. Why are you still playing this game instead of making your own story?"
                        menu:
                            "I just want to see what happens when I choose this path.":
                                $ death_narration = "It appears you got your wish. This path, like many others only leads to death."
                                if kokiri_alternateplace == False:
                                    
                                    if kokiri_conversation == 1:
                                            jump kokiri_death_1
                                    elif  kokiri_conversation == 4:
                                        jump kokiri_death_4_hill
                                else:
                                    if kokiri_conversation == 4:
                                        jump kokiri_death_4_noHill
                                if love_meter < 3:
                                    l "Really? I think that settles it then. This really all is a game to you."
                                    l "You kept me in this loop for your own wants. Even when I'm offering you a potential way out of it."
                                    if persistent.lilithAliveAndRetriedCounter > 0:
                                        n "[date_sub!c] [conj('date', 'is', 'are')] more correct than [date_sub] might know in this moment, isn't [date_obj] player?"
                                        if persistent.lilithAliveAndRetriedCounter == 1:
                                            n "Or are you going to pretend like that time you came back even when [date_sub] survived was for [date_pos] sake?"
                                        else:
                                            n "Or are you going to pretend like the times you came back even when [date_sub] survived were for [date_pos] sake?"
                                        n "...Or even worse, perhaps you aren't pretending. Maybe some part of you genuinely believes that?"
                                        n "Either way, it doesn't matter in the end. The result still is the same."
                                    l "Look, if you don't atleast attempt to try this potential escape from the loop, then I might aswell try to escape on my own."
                                    l "Goodbye [persistent.name]. Until never again if everything goes right."
                                else:
                                    l "Really? So this is all just a game to you?... I know it literally is, but I had hoped that we could have tried to escape this loop together."
                                    l "But now I see you don't have my best interests at heart like I had hoped you would."
                                    l "In that case I think I'm better of taking my chances on my own."
                                    l "Goodbye [persistent.name]. It really is a shame things have to go like this, I was really enjoying our time together."
                                $ noTalkAngryLilith = True
                                jump angryLilith
                                
                    "Yes, I'm now in full control of it.":
                        n "[persistent.date] gives you a warm embrace and jumps up in the air after [date_sub] [conj('date', 'stops', 'stop')] hugging you."
                        l "Perfect! So now we can just do whatever we want without having to fear being killed right?"
                        menu:
                            "Absolutely!":
                                n "You do know that is not the case, right?"
                                n "That I'm still the one telling this story, that you are not in control."
                                n "Are you lying to yourself, or to [date_obj]?"
                                n "Maybe both?"
                                
                                if persistent.kokiri_tellnolies_knowledge:
                                    n "I'm not sure if [date_sub] would like that."
                                    n "Actually I'm very sure [date_sub] wouldn't like that, and so are you."
                                    n "And yet you did."
                                    n "I wonder why, did you try to alleviate some of [date_pos] fear?"
                                    n "Or did you want to fool yourself for a second into believing your own lies?"
                                    n "Or perhaps you wanted to just see what dialogue that choice would give you?"
                                    n "Either way, what's done is done."
                                    n "Normally I might scold you for doing something like this, but I'll admit I can see why you might have chosen to lie."
                                    n "Maybe ignorance truly is bliss."
                                    if persistent.kokiri_death_4_hill_holdHand or persistent.kokiri_death_4_hill or persistent.kokiri_death_4_noHill == True:
                                        n "And yet we are not given that mercy are we?"
                                        n "As we sadly both know what will happen next."
                                        n "Would you want to unlearn the knowledge?"
                                        n "Feel that same blissfull ignorance as [persistent.date]?"
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
                                    n "Maybe it's better for [date_obj] to still believe that things are going to start looking up for [date_obj]."
                                    n "Maybe it's better for you to believe that just for a little bit longer."
                                    n "But nothing can last player, each line from the script ends at some point, making way for the next."
                                    if persistent.kokiri_death_4_hill_holdHand or persistent.kokiri_death_4_hill or persistent.kokiri_death_4_noHill == True:
                                        n "And we both know what the approaching lines will be, no matter how hard you might try to stall them."
                                $ kokiri_fullControlAndStillDying = True   
                                jump kokiri_death_4_hill
                                                              
label kokiri_death_2_prevented_youWereHappyWithRon:

    l "Well, I am spending this moment with you, not with this \"Ron\"."
    n "[persistent.date] places [date_pos] hand on your arm and rubs it softly."
    l "It is sweet that you care about me enough to worry about those sorts of things but I would rather not have you worry about them."
    l "Besides, you made that version of me happy with Ron and now you've made this version of me very happy with you."
    n "[date_sub!c] [conj('date', 'flashes', 'flash')] you a knowing smile."
    l "If you ask me you have succeeded."
    l "You know what? I want to show you something..."
    jump kokiri_pictureChoice

label kokiri_death_2_prevented_youDiedATon:
    l "Oh, [persistent.name], it certainly has been a lot to wrap my head around  but I never had to constantly deal with this whole scenario like you. I truly suppose ignorance is bliss."
    l "I can completely understand that you are dealing with a lot throughout this whole thing. I really don't blame you for trying to keep coming back."
    l "You are just trying to find a way out and I'm sure you'll find it. Your intentions are pure."
    l "I don't blame you for anything [persistent.name], please don't blame yourself either."
    l "After all, is it worth it to live with me if you can't live with yourself?"
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
            n "For a moment everything turns quiet, almost as if not to break the silence instead of saying something [persistent.date] makes a beckoning motion."
            n "The singing of a bird nearby dethrones the silence, and freed from it's oppressive reign [persistent.date] speaks again."
            l "I think I might have an idea of how to give you some more hope, it always helps me out when I need some."
            jump kokiri_pictureChoice

label kokiri_pictureChoice:
    n "[persistent.date] stands up from the blanket, some shards of the meteorite still laying on it and extends [date_pos] hand to you."
    menu:
        "*Take [date_pos] hand*":
            jump kokiri_showpicture
        "You actually already showed me the beach picture hidden in the big tree. It fell over right on top of you..." if persistent.kokiri_death_3:
            jump kokiri_death_3_prevented

label kokiri_showpicture:
    $ persistent.beach_knowledge = True
    n "You grab [date_pos] hand and get up."
    l "But close your eyes, alright?"
    l "I don't want to reveal where we are going."
    n "You let your eyelids fall shut."
    n "With your hand in [date_pos] [date_sub] [conj('date', 'leads', 'lead')] you down the hill and [conj('date', 'takes', 'take')] you to the left. You feel a bush brush against your legs."
    n "[date_sub!c] [conj('date', 'brings', 'bring')] you deeper and deeper into the forest. You take a few more turns along the way, one left and two right."
    n "Suddenly [date_sub] [conj('date', 'stops', 'stop')]."
    l "Alright, you can open your eyes now [persistent.name]!" 
    n "As you do you find yourself in front of a very high tree surrounded by a bunch of smaller trees."
    l "You are probably thinking why I am taking you here."
    l "Well, I hid something... precious here."
    n "[date_sub!c] [conj('date', 'looks', 'look')] at the big tree and the trees surrounding it, a smile growing on [date_pos] face."
    n "[date_sub] [conj('date', 'moves', 'move')] to the back of the big tree, and [conj('date', 'comes', 'come')] back with a small wooden box, decorated with red details."
    n "Then [date_sub] takes off [date_pos] necklace you somehow never noticed before, a key is dangling on it."
    n "[date_sub!c] uses the key to unlock the box and takes out a polaroid."
    n "The photo shows a man and a woman with a wide smile on both of their faces. They are standing behind three children, one boy and two daughters, you can quite easily tell the eldest daugther is [persistent.date]. The children are all building a sandcastle together."
    l "This is a photo of our family at a day on the beach, those were the happy days..."
    l "Even to this day I still have an afinity for the beach because it is linked to those happy days."
    l "But I know I will never truly get them back, not like it used to be anyway.."
    l "I still have [persistent.date_sis] and my [mom_par] of course, both of them are just so important to me and together we are trying to slowly but surely make new happy days."
    l "But anyway, what I'm trying to say is that you have something special, a way to prevent me from dying and a whole boat-load of determination."
    l "So don't feel guilty about your gift but use it to the fullest extent."
    $ persistent.useGiftToFullExtent_knowledge = True
    menu:
        "I will [persistent.date], I promise.":
            n "[persistent.date] gives you a lovely smile."
            l "Give it your best shot"
            jump kokiri_death_3
        "This might sound weird, but when you say to the fullest extent, do you mean I can also contact your family to gain more potential leads?" if persistent.useGiftToFullExtentLimit_knowledge:
            n "[persistent.date] grows quiet for a moment, [date_sub] [conj('date', 'seems', 'seem')] shocked by what you just asked."
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
    #TODO: if you say you seek an end and are seen as the ravenprince by the trinity, then you will get the option to cut the tree of life. The tree of life are all the branches of the story.
    #If you cut the root then this world and all worlds sprouting from it will ceease, causing no more suffering but also no more joy.
    # "Thou areth wwhat thou seeketh and thy seeketh the end. Areth thou the reaper? Then soweth what thou reaps."
    #"This world was birthed for one like you and now it will die for one like you."
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
            n "Suddenly the earth begins to shake. The roots of the big tree [persistent.date] is standing next to begin unearthing. Before you can do anything the tree falls over right on top of [date_obj]."
            play music game_over
            $ _death_seen = check_death_skip("kokiri_death_3")
            if is_death_skipped("kokiri_death_3"):
                $ persistent.kokiri_death_3 = True
                jump gameOver
            elif _death_seen >= death_skip_threshold:
                n "What's to come next is etched into your mind I'm sure, maybe it's better we just skip to how it ends?"
                menu:
                    "Always skip this from now on.":
                        $ set_death_always_skip("kokiri_death_3")
                        $ persistent.kokiri_death_3 = True
                        jump gameOver
                    "Show the death narration.":
                        pass
            n "You push the tree off with all your might but it seems like it was to no avail, the force of the tree killed [date_obj] instantly."
            n "Your screams pierce through the woods, it answers with pure silence, mourning the loss of [persistent.date] once more."
            $ persistent.kokiri_death_3 = True
            jump gameOver

label kokiri_death_3_prevented:
    l "...Wow, I'm not sure what to say to that. This is all a lot to take in."
    l "So I died there?..."
    l "Are we safer here?"
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
        $ _death_seen = check_death_skip("kokiri_death_4_hill")
        if is_death_skipped("kokiri_death_4_hill"):
            jump gameOver
        elif _death_seen >= death_skip_threshold:
            n "What's to come next is etched into your mind I'm sure, maybe it's better we just skip to how it ends?"
            menu:
                "Always skip this from now on.":
                    $ set_death_always_skip("kokiri_death_4_hill")
                    jump gameOver
                "Show the death narration.":
                    pass
        if kokiri_death_4_playerResponse == True:
            n "You want to answer [date_obj] when the ground begins to shake once again, even more severely than when [date_sub] showed you the picture."

        else:
            n "Suddenly the ground begins to shake once again, this time even more severely than when [date_sub] showed you the picture."
        n "...Which is pretty odd, isn't it? Perhaps this isn't a mere earthquake, but something else entirely."
        #TODO: If you have seen this ufo death don't treat it as odd and have the narrator treat it as the ufo causing the shaking where on the other optin you are further away from the source.
        if kokiri_holdhand == True:
            jump kokiri_death_4_hill_dieTogether

        else:
            l "What is happening [persistent.name]?"
            if kokiri_fullControlAndStillDying == True:
                l "Are you in control of the story now? Is this part of it?"
                menu:
                    "It is, don't worry, it's all going according to plan.":
                        if love_meter > 2:
                            l "Okay, I trust you."
                            l "Although it doesn't exactly feel like it is."
                        else:
                            l "Oh come on, really? It absolutely doesn't feel like that's true."
                            l "Even if it was, why go through with all of this? Couldn't you just let us walk off this hill?"

                    "...I might have lied slightly, I am not in control of the story. We are still in the game.":
                        #TODO: Have her react more harsh on this if her love is low. If she specifically told you not to lie to her in the begining of the path have her react even harsher on this.
                        l "You... what?"
                        l "So that means I'm still going to die?"
            else:
                n "The fear in [date_pos] voice is palpable."
            n "Then without warning the hill shoots straight upwards. The increased force of the gravity pinning you against it, but not for long."
            n "Through fighting the force you manage to roll off the hill, falling down in the middle of a lake close to where it used to sit."
            p "[persistent.date], it's safe in here, jump down!"
            l "I.... I can't... it's already too high..."
            n "[date_sub!c] [conj('date', 'is', 'are')] right, you can barely hear [date_pos] words anymore from that height, jumping down now would be a terrible idea."
            n "All you can do is float there, powerless, while you watch the hill and [persistent.date] getting swallowed by the ink-black sky."
            n "As you stare at the sight your eyes fall on some sort of thrusters on the bottom of it." #TODO: Change this dialogue after you have seen this.
            n "Whatever that thing is, it's anything but a hill."
            if damoclesAsked == True:
                n "It seems unlike Damocles, [date_pos] thread always snaps."
                n "Aren't you happy that you asked [date_obj] Damocles now? Now you get this reference."
            elif death_narration != "":
                n "[death_narration]"
            jump gameOver

label kokiri_death_4_hill_dieTogether:
    l "Is this it, [persistent.name]?"
    n "You silently nod, not being able to say it out loud. [date_pos!c] trembeling hand squeezes yours even more."
    n "Then without warning the hill shoots straight upwards. The increased force of the gravity pinning you against it, but not for long."
    n "The vibrations of the hill are so strong that you can barely keep your balance and begin sliding off."
    n "However [persistent.date] keeps you safe, holding your hand with all of [date_pos] strength."
    n "[date_sub!c] slowly [conj('date', 'pulls', 'pull')] you up. In the middle of this [date_sub] [conj('date', 'looks', 'look')] down, despite the fear in [date_pos] eyes [date_pos] grip never loosens."
    l "Hold on [persistent.name], I got you and I'm not letting you go."
    l "{size=*0.5}Phew, we 're really high... I'm getting dizzy but I must keep going... just a little bit longer...{/size}"
    n "[date_sub!c] [conj('date', 'has', 'have')] managed to pull you up but it cost all of [date_pos] strength."
    n "The both of you exhaustedly flop down on the hill like a few moments ago, the only difference being that the hill is now soaring in the sky. The two of you haven't let each other go, your hands still intertwined."
    l "You know what's funny [persistent.name]?"
    l "I felt more scared when I thought you were going to fall than I am now thinking about how I'm going to die."
    l "I suppose it's because if you fell I would have to go through this all alone."
    menu:
        "You won't have to do this alone, I'm with you.":
            jump kokiri_death_4_hill_imWithYou

label kokiri_death_4_hill_imWithYou:
    l "{size=*0.5}Thank you.{/size}"
    n "While spoken quietly, quite some sincerity drips off those two simple words."
    n "Those two words fade, leaving only silence for a few moments. It's quite enjoyable actually."
    n "You grow aware of [date_pos] hand once more, held in yours. It feels cold to the touch, yet emanates a gentle warmth somewhere deep inside you all the same."
    n "[date_sub!c] shifts around slightly, it seems [date_sub] [conj('date', 'wants', 'want')] to say something to break the quiet, but [date_sub] [conj('date', 'does', 'do')]n't know what exactly."
    n "You let [date_obj] search for a little while, afterall there is no rush. This might be the last moment you get to spend together, atleast this loop."
    l "You know, the stars are absolutely beautiful from here. I never thought I would get to watch them this closely."
    n "[persistent.date] shudders speaking those words yet when you look at [date_obj] [date_sub] [conj('date', 'attempts', 'attempt')] [date_pos] a smile."
    play music game_over
    $ _death_seen = check_death_skip("kokiri_death_4_hill_holdHand")
    if is_death_skipped("kokiri_death_4_hill_holdHand"):
        $ persistent.kokiri_death_4_hill_holdHand = True
        jump gameOver
    elif _death_seen >= death_skip_threshold:
        n "What's to come next is etched into your mind I'm sure, maybe it's better we just skip to how it ends?"
        menu:
            "Always skip this from now on.":
                $ set_death_always_skip("kokiri_death_4_hill_holdHand")
                $ persistent.kokiri_death_4_hill_holdHand = True
                jump gameOver
            "Show the death narration.":
                pass
    
    n "[persistent.date] was right, the hill flew up into space itself, to some far off stars- perhaps to a distant planet?"
    n "Not that the two of you would know as after fifteen seconds everything went black."
    n "You can only imagine the gruesome death the two of you suffered, that is if you weren't unconscious."
    $ persistent.kokiri_death_4_hill_holdHand = True
    jump gameOver

label kokiri_death_4_noHill:
    play music game_over
    $ persistent.kokiri_death_4_noHill = True
    $ _death_seen = check_death_skip("kokiri_death_4_noHill")
    if is_death_skipped("kokiri_death_4_noHill"):
        jump gameOver
    elif _death_seen >= death_skip_threshold:
        n "What's to come next is etched into your mind I'm sure, maybe it's better we just skip to how it ends?"
        menu:
            "Always skip this from now on.":
                $ set_death_always_skip("kokiri_death_4_noHill")
                jump gameOver
            "Show the death narration.":
                pass
    n "The earth begins shaking once again. The mechanical mound moves up slowly but surely, until it hovers above [persistent.date] and you."
    n "A green pillar of light shoots out from inbetween the four thrusters at the bottom of the ufo."
    n "It envelops both of you and [persistent.date] rises up, getting swallowed up by an opening in the bottom that closes the moment [date_sub] [conj('date', 'is', 'are')] inside. It shoots straight up once again, only this time much faster."
    n "All you can do is stand there powerlessly as you watch [persistent.date] disappear into the ink-black sky."
    jump gameOver 

label beach_deaths: 
    #TODO: Once you start work on the beach part fill in these deaths.                    
    label seaDike_left_slipDeath:
        n "(Add snapping neck on railing death, she slips or gets pushed by a bike)"
        $ persistent.beach_slipDeath = True
    label seaDike_right_potDeath:
        $ persistent.beach_potDeath = True  
        n "(A flower pot falls on her)"
            
    label beach_holeDeath:
        $ persistent.beach_hole_death = True
        n "She fell down a hole in the sand, it collapses."
        jump gameOver  
            
    label beach_jellyDeath:
        $ persistent.beach_jelly_death = True
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
    #Put all deaths that don't fit in the other categories here.
    label phone_untoldstory_planeDeath:
        n "Suddenly a horrible noise comes out of your phone, almost like a sharp whistling."
        n "The sound only growing louder and louder, growing exponentially until it becomes almost earpiercing."
        n "Then you hear a huge crash, the sound of something collapsing and then screaming from further away."
        if persistent.plane_knowledge == False:
            n "Unsure of whatever that was you call an ambulance to [date_pos] house in the hope that [date_sub][conj('date', 'is', 'are')] still somehow alive..."
            #TODO: For the ambulance dialogue that later will be a thing, have the narrator ask, if you know she won't make it, why do you call an ambulance? Is it ethical? Afterall it can't help someone else durign that time.
            #Also, if you say the right things to the ambulance lady you can convince her at the start of the loop to send someone in certain situations so lilith can be saved. You can choose to stay with her in the ambulance but it will have an accident if you do so.
            #Also, you can maybe go on a date with her instead? Not sure if she should live through this or not though. Dying means the curse fully is yours but living means lilith was never meant ti survive and be together with you and you moved on, which better fits the themes.
            #Personality is probably quite no nonsense, she won't really buy your timeloop explanation and will need another way to convince her.
        else: 
            n "You call an ambulance to go to [date_pos] house in the hope that this time [date_sub] might just survive... "

        play music game_over
        $ _death_seen = check_death_skip("plane_death_untoldstory")
        if is_death_skipped("plane_death_untoldstory"):
            $ persistent.plane_knowledge = True
            jump gameOver
        elif _death_seen >= death_skip_threshold:
            n "What's to come next is etched into your mind I'm sure, maybe it's better we just skip to how it ends?"
            menu:
                "Always skip this from now on.":
                    $ set_death_always_skip("plane_death_untoldstory")
                    $ persistent.plane_knowledge = True
                    jump gameOver
                "Show the death narration.":
                    pass
        
        n "When the ambulance arrived there isn't much they could do. Not for [date_obj] anyway. Apparently a plane crashed on [persistent.date]'s house."
        n "[persistent.date] has been living alone for a year or two now and [date_sub] had no real neighbours, not any that weren't a few kilometres away from [date_obj] atleast. Which means only [date_pos] house got ruined by the plane."
        n "Sadly the same can't be said for both [persistent.date] and most of the passengers of the plane..."
        n "There were luckily survivors of the plane crash, of the 139 people on board 86 people survived, most of them had minor injuries but where otherwise physically fine, if not mentally scarred."
        n "There would have probably been less survivors had you not called the ambulance, as gargantuan as the task was they tried to help the most severe cases while backup arrived to help the others."
        n "The event was all plastered over the news as soon as it happened, they followed it live as it unfolded."
        n "[persistent.date] did not survive though, [date_obj] body being the one they found last, under the crash site, the sight was horrifying."
        n "They never mentioned what a description on the news but you could hear it in their reaction through her phone, which was miraculously still working."
        $ persistent.plane_knowledge = True
        jump gameOver

    label phone_planeDeath:
        $ persistent.plane_knowledge = True
        n "As [persistent.date] hangs up you turn the tv on in frustration."
        n "It seems there's an emergency broadcast, it's mentions a plane losing height just mere moments ago."
        n "Everything anyone can do is just watch in terror as the plane loses more and more altitude as the news anchor urges everyone in the nearby area to take cover."
        
        play music game_over
        $ _death_seen = check_death_skip("plane_death_phone")
        if is_death_skipped("plane_death_phone"):
            jump gameOver
        elif _death_seen >= death_skip_threshold:
            n "What's to come next is etched into your mind I'm sure, maybe it's better we just skip to how it ends?"
            menu:
                "Always skip this from now on.":
                    $ set_death_always_skip("plane_death_phone")
                    jump gameOver
                "Show the death narration.":
                    pass

        n "Then the horrible sound of the plane as it crashes into a isolated house."
        n "You realise the house doesn't look unfamiliar to you at all."
        n "Then it hits you."
        n "It's [date_pos] house."
        if death_narration != "":
            n "[death_narration]"
        jump gameOver

    label reunion_death:
        n "Suddenly you spot a {i}very{/i} familiar red Sedan speeding towards all of you."
        n "Things are hectic, everyone is screaming and everything seems to happen in a blur."
        n "You can't react in time before you meet the immense force of the car."
        n "Everything turns to black."
        n "After drifting around in the dark for what feels like a decade you awaken, finding yourself on a hospital bed."
        n "When you look around to check for any nurses or doctors your gaze instead lands on a half familiar figure."
        n "It's [persistent.date_dad]."
        #TODO: David's dialogue might need to be a little bit rewritten since I find it quite bland, mostly the begining.
        d "Hello [persistent.name], I'm happy to see that you've finally awoken."
        d "It's been quite a while, you've been in a coma for about 2 years."
        n "2 years? You ponder the implications for a bit before your train of thought gets interrupted by a more urgent one."
        menu:
            "What happened to [persistent.date]? Is everyone fine?":
                n "[dad_sub] [conj('dad', 'slinks', 'slink')] more inwards upon hearing [date_pos] name."
                n "You already know the answer to your question just by reading [dad_pos] body language."
                d "[persistent.date] didn't make it..."
                d "[persistent.date_mom] and [persistent.date_sis] are fine, as fine as they could be after losing [persistent.date]."
                d "I am also trying to move on, I tell myself it's what [date_sub] would have wanted."
                d "Besides, I won't make the same mistake as last time, my family needs me more than ever."
                d "These past two years, most days, I get up and after eating breakfast and brushing my teeth I see them in the mirror, [persistent.date_ghost] and [persistent.date]."
                d "The thing is, the first time I saw them I expected them to be angry, but they weren't, they were smilling at me."
                d "They were asking me to keep living, because they couldn't anymore."
                d "Ofcourse I will, but I was hoping [date_sub] could get a second chance at living just like I got."
                d "That's why I came to visit everyday these past 2 years, to beg you to undo all of this."
                d "If it's possible I'd like to still have the reunion we had but with [date_obj] surviving."
                d "Maybe if you didn't talk that long with us we would've walked away somewhere where that car wouldn't hit us?"
                d "However, if [date_sub] [conj('date', 'dies', 'die')] whatever choice you make at the reunion, please don't reunite us again."
                d "If I have to let [date_obj] go to keep [date_obj] safe, then so be it. Still, if there is another way I am begging you to find it."
                d "Can you promise me you'll try your best?" 
                menu:
                    "I promise.":
                            d "Thank you [persistent.name], thank you for everything!"
                            jump reunion_ending_davidLeavesSegway

                    "Actually it doesn't work like that, [date_sub] will stay dead in this world but survive in another one.":
                            d "Then please go through with it, make sure my [date_child] from another world is safe."
                            d "I'm fine living my life like this, I can be there for [persistent.date_sis] and [persistent.date_mom] as I should have been before."
                            d "So go and be there for [persistent.date]."
                            d "I'll live my life here with a smile, both for what I still have and what my other self will gain without knowing."
                            jump reunion_ending_davidLeavesSegway

                    "Oh, [date_sub] [conj('date', 'survives', 'survive')] in another outcome, I've already seen it." if persistent.ending_reunionGoodEnding:
                            d "What?..."
                            d "So you went back after you had already sucesfully reunited us?"
                            d "Can I ask you why you did?"
                            menu:
                                "I hadn't seen what happened if I kept talking to all of you.":
                                    d "So out of curiosity you just undid our perfect little ending?"
                                    d "Why would you do that? Is this just some kind of game to you?"
                                    d "I thought you wanted the best for my [date_child], for all of us."
                                    d "However, it seems this hasn't been about [date_obj] for quite a while now."
                                    menu:
                                        "Of course not, I just wanted to see if there was a better ending somewhere for [date_obj].":
                                                d "Oh spare me the nonsense. A better ending than being reunited with [date_pos] family and surviving?" #TODO: Does he know lilith dies each time? Might need to change this dialogue a bit.
                                                d "I assume the only one that ending didn't pan out for as hoped was you [persistent.name]."
                                                d "Which meant you couldn't help but alter things."
                                                d "I'm not sure what's worse, lying about doing this for [date_obj], or truly believing so."
                                                d "Eitherway I want nothing to do with someone like you."
                                                d "I might have been a coward when it mattered, but you aren't any different at all."
                                                d "Undoing a world where all of us were happy just so you can chase a happy ending you're not even sure exists. Does this seem like that happy ending to you [persistent.name]?"
                                                d "Well, I hope you heed these words and go back to the other ending, [date_sub] [conj('date', 'deserves', 'deserve')] that one, you know?"
                                                d "Or at the very least [date_sub] [conj('date', 'deserves', 'deserve')] one where [date_sub] [conj('date', 'does', 'do')]n't die."
                                                d "Somewhere deep down you must know that too, right? I'm not sure if you still feel that way but at some point you at the very least must've felt it."

                                        "Of course, after a while repeating the same dialogue over and over got boring. This however is very interesting.":
                                                d "... What do you mean?"
                                                menu:
                                                    "This is extra content, can't you see [persistent.date_dad]? Did you really think I reunited all of you out of the kindness of my heart?":
                                                        d "..."
                                                        menu:
                                                            "To me you all are just lines of text, entertainment to stave off the boredom.":
                                                                    d "..."
                                                                    menu:
                                                                        "When one set of lines becomes boring, I move on to the next. In this case that's you [persistent.date_dad]. Soon it will be the others.":
                                                                            d "..."
                                                                            d "{size=*2.5}No!{/size}"
                                                                            d "No."
                                                                            d "There is no way in {b} {i}hell{/i}{/b} that I'm going to let you play with my family like that." #TODO: Make the hell shake and probably a bit bigger, I think lilith already has one like this, could be an intersting symmetry.
                                                                            d "I have abandoned them for too long, I won't do that again."
                                                                            menu:
                                                                                "Oh but you do so over and over and over again [persistent.date_dad]. Every restart means you've abandoned them once again.":
                                                                                        d "... Maybe you are right."
                                                                                        d "So I should really make this time count."
                                                                                        d "This time I will not abandon them."
                                                                                        n "[persistent.date_dad] takes a pillow that was resting next to you on the bed and presses it into your face, hard."
                                                                                        n "You try to fight against [dad_obj] but your arms that haven't moved for years are no strength against [dad_pos] anger."
                                                                                        n "Soon everything becomes black."
                                                                                        jump gameOver
                                                                                        
                    "I have had this conversation with you multiple times already. I'm not promising you anything." if persistent.davidPromise:
                            d "... You did? Then why did you make the same choice once again?"
                            d "Why did you once again let everything go wrong?"
                            d "Couldn't you have prevented it this time by doing literally anything else?"
                            d "I really don't know what to make of you [persistent.name], you reunited us, right?"
                            d "That must mean you want the best for all of us, or atleast for [persistent.date]."
                            d "Otherwise, you wouldn't go through all the effort that undoubtedly took."
                            n "[dad_sub!c] [conj('dad', 'is', 'are')]n't exactly wrong... That took quite a few steps to set up. Your motivations are hard to get a grasp on."
                            n "Especially since a lot of those steps were... less than ethical, yet you kept going."
                            n "Now here you are, having this same conversation with [persistent.date_dad], once again."
                            n "So [dad_sub!c] [conj('dad', 'is', 'are')] hitting the nail on the head with [dad_pos] question, why {b}are{/b} you back here?"
                            menu:
                                "To see if there is some new dialogue.":
                                    d "Really?"
                                    d "That's all we are to you? Just some text on a screen?"
                                    d "I can excuse and even accept that if that's how you view me. But [persistent.date]?"
                                    d "The two of you must have been on countless dates for you to pull of our reunion, did all of that mean nothing to you?"
                                    d "Was it all just nothing but words? Just empty chatter that didn't matter?"
                                    d "Did you even reunite us because you cared for us, or did you just want to see what dialogue that would get you aswell?"
                                    d "I can't- I can't stay here for any longer."
                                    d "You let my [date_child] die- no, killed [date_obj], for some extra dialogue?"
                                    d "[date_pos!c] life being in your hands is a fate worse than dying."

                                "I am trying to find a better ending.":
                                    d "A better ending than the one where me and my family get reunited and [persistent.date] survives?"
                                    d "What exactly are you looking for in that case?"
                                    d "What could possibly be better?"
                                    n "[dad_sub!c] [conj('dad', 'does', 'do')] have a point, that ending is as good as they come, isn't it?"
                                    n "Do you really think there is something that is better for [date_obj], for them, in here?"
                                    n "Or do you think there is something better for you in here?"
                                    n "Perhaps an ending where the both of you end up together?"
                                    d "I'm done. I genuinely thought you wanted the best for [date_obj], for us."
                                    d "But now I see you as you are, and I want nothing to do with it."
                                    d "Thank you for reuniting me with my family, but for nothing else."
                                    d "At the very least we will be able to comfort eachother during our loss."
                
                                d "Goodbye [persistent.name]. And stay away from my [date_child] next time if [date_sub] only [conj('date', 'means', 'mean')] so little to you."
                
                label reunion_ending_davidLeavesSegway:
                    d "I'll give you some time to recover, you'll need it."  
                    d "Take it easy and once you are fully recovered you can try again."   
                    n "[persistent.date_dad] gets up from [dad_pos] chair and walks towards the door, [dad_pos] hand rests on the doorhandle."
                    d "Once again I'd like to thank you [persistent.name]."      
                    d "Goodbye, and perhaps we'll meet again? Just, some other time."  
                    n "With that [dad_sub] left."   
                    n "Now you're once again alone." 
                    n "Especially without [persistent.date]."
                    n "Laying there, waiting, it is too much for you." 
                    n "You want to see [date_obj] again, and preferably now."
                    $ persistent.davidPromise = True
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
    n "Your date surely didn't go as planned."
    $ show_cinematic_bars(sides=["top", "bottom"], size=550, duration=8, curve="ease")
    pause 8

    $ ending_title_card = ""
    if lilithAliveEnding and ending_check != "":
        $ ending_title_card = ending_title_from_check(ending_check)

    transform gameover_zoom:
        alpha 0.0
        zoom 1.2
        ease 1.2 alpha 1.0 zoom 1.0

    transform endingcard_zoom:
        alpha 0.0
        zoom 1.08
        ease 1.0 alpha 1.0 zoom 1.0

    scene black
    $ hide_cinematic_bars(animate=False, duration=0, curve="ease")
    #TODO: Right before the retry screen the foreground isn't cleared, make sure that works correctly.

    if ending_title_card != "":
        show text "{color=#336600}{size=72}{b}ENDING{/b}{/size}\n{size=56}[ending_title_card]{/size}{/color}" at truecenter, endingcard_zoom
    else:
        show text "{color=#d00000}{size=90}{b}GAME OVER{/b}{/size}{/color}" at truecenter, gameover_zoom

    pause 3

    hide text
    with Dissolve(1.0)
    play music sunrise fadein 1.5
    show screen retry_wall
    pause 4
    
   
    #TODO: Add like a glitch effect here maybe? The first time it is definetly allowed to be longer, after that I'd like it to be more subtle but it shows the game "broken" in a way, allowing the player to retry.
    
    menu:
        "Retry." if not lilithAliveEnding and ending_check != "Voided":
            hide screen retry_wall
            if  persistent.kokiri_angry_noretry == True or persistent.chinese_phone_noretry == True:
                n "So you are going back even when [date_sub] [conj('date', 'asked', 'ask')] you not to?"
                n "In that case I hope you at the very least don't make the same mistake you did last time."
            jump game_start
        "Retry?" if lilithAliveEnding and ending_check != "Voided":
            hide screen retry_wall
            $ persistent.lilithAliveAndRetriedCounter += 1
            $ lilithAliveEnding = False
            $ increment_ending_retry_count(ending_check)
            jump game_start

        "Let go." if ending_check == "Voided":
            $ start_over_reset()
            $ persistent.pictureBookUnlocked = True #Upon the next boot up of the game it should just become a picture book with all kinds of screenshots from the game while you played. Maybe some new art etc.
            $ renpy.quit()