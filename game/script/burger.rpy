
label burger_start:
    $ burger = True
    if persistent.lildeaths > 0:
        if no_nightmare == False:
            if perm_nightmare == True:
                #Set the nightmare flag always since perm_nightmare is true.
                $ burger_nightmare = True #The flag that will be checked in the burger path for what kind of nightmare triggers.
            else:
                    if persistent.lildeaths <= 40:
                        $ nightmare_max = 60 + persistent.lildeaths
                    else:
                        $ nightmare_max = 100
                    $ nightmare_chance = renpy.random.randint(1, nightmare_max)
                    if nightmare_chance >= 80:
                        $ burger_nightmare = True
                    else: 
                        $ burger_nightmare = False
    l "Burgers sure sound good, see you there!"
    n "You arrive a tad late, [persistent.date] already has grabbed herself a seat and waves at you when she sees you."
    l "Heya! Almost was scared you wouldn't show up."

    if persistent.burgerstart == False:
        $ persistent.burgerstart = True
    else: 
        $ persistent.burgerwent += 1


    menu:
        "I can't say no to burgers!":
            jump burger_start_choice1

        "I wouldn't want to miss this for the world!":
            jump burger_start_choice2

        "Sorry, traffic was quite bad.":
            jump burger_start_choice3

        "Hey glad to be here. Could we sit somewhere else though?" if persistent.burger_death_1:
            $ burger_alt = True
            n "[persistent.date] gives you a smile and a thumbs up."
            l "Sure, where would you like to sit?"
            n "You quickly point to a table, it doesn't really matter which one, as long as she isn't sitting where she got shot before."
            l "Alright, that table it is then!"
            n "[persistent.date] takes her handbag and follows you as you wander to the table."
            n "You feel relieved, knowing what horrors you just escaped from."
            n "The image of her laying there, on the brink of life and death, is burned into your mind."
            n "You shudder."
            n "It's probably best to try and focus on the present, not the past."
            l "Are you alright [persistent.name]?"
            l "You look like you have just seen a ghost."
            n "She's not far off."
            menu:
                "Oh yeah, I am fine, I was just thinking about the traffic jam I was stuck in.":
                    jump burger_start_choice3




label burger_start_choice1:
    n "[persistent.date] chuckles."
    l "Ah, another burger fan!"
    l "We are at the right place I'd say, the burgers here are delicious."
    l "Did you already know that or is this the first time you've eaten here?"

    menu:


        "I actually didn't know that, I've never been here before." if persistent.burgerwent == 0:
            jump burger_beenBeforeXTimes

        "I did know that, I've been here before a couple of times. (Lie)" if persistent.burgerwent == 0:
            $ burgerBeforeLie = True
            jump burger_beenBeforeXTimes


        "I did know that yes, I've been here before, only once though." if persistent.burgerwent == 1:
            jump burger_beenBeforeXTimes


        "I'm well aware, I've been here exactly [persistent.burgerwent] times." if persistent.burgerwent > 1:
            n "It sounds a bit weird if you phrase it like that, doesn't it?"
            jump burger_beenBeforeXTimes

        "I did know that actually, I've been here a couple of times." if persistent.burgerwent > 1:
            $ burgerBeenBefore = True
            l "Oh you have? That makes sense, these burgers are the best of this state, scratch that, of the world!"
            n "While she is enthusiastically exclaiming this her arms kind of seem to have a life of their own, making all kinds of gestures to get the point across even more. "
            n "When she catches her arms in the act she blushes slightly, quiets for a moment and places them back down on the table."
            l "So, what are you going to pick? I think I'll go for the juicy cheeseburger myself."
            jump burger_start_menu

label burger_beenBeforeXTimes:

    if persistent.burgerwent > 0:
        $ burgerBeenBefore = True

    if persistent.burgerwent == 0:
        if burgerBeforeLie == False:
            l "I'm sure you'll love it here then!
            Like I've said before, they have really amazing bugers here."
        else: 
            l "Oh I see, you have great taste in that case!"
            n "She lets out a hearty chuckle."

    elif persistent.burgerwent == 1:
        l "Ah, I hope you liked your previous meal here!"

    else:
        if persistent.burgerwent <= 4:
            l "Ah, you've been here a few times already.
            Then you surely know how good the burgers are here."

        elif persistent.burgerwent <= 6:
            l "Wow, you've been here quite a few times already!
            You must really like it here then, I knew we were on the same wavelength!"
        elif persistent.burgerwent <=9:
            l "Wow, you've been here a lot of times!"
            l "... Come to think of it, you might have visited this place more than I have."
            n "[persistent.date] lets out a small giggle."
        elif persistent.burgerwent < 22:
            n "[persistent.date] lets out a joyful laugh."
            l "Wow! I almost feel like I should let you choose my burger with all that burger knowledge you must have."
            l "Almost though, this is far from my first rodeo either [persistent.name]!"
        else:
            l "Wow... is it weird to be impressed by that?"
            n "[persistent.date] lets out a small laugh."
            l "It probably is but I'm quite impressed by the expertise you must have when it comes to the burgers here."



    l "So, which burger do you want to pick? I think I'll go for the juicy cheeseburger myself."
    jump burger_start_menu




label burger_start_choice2:
    l "Awwe, I'm flattered you are so happy to see me. Or is it the burgers you don't want to miss?"
    l "[persistent.date] chuckles slightly."
    l "Sorry, I'm just messing with you."
    l "So, what do you want to order of the menu?  I think I am going to go with a juicy cheesburger."
    jump burger_start_menu


label burger_start_choice3:
    l "Now that you mention it, I think I heard something about it on the radio, they said some ghostrider caused  the traffic jam."
    l "If I'm not mistaken I think it was a Sedan or something like that?"
    l "Anyway, what do you want to order of the menu?  I think I am going to go with a juicy cheesburger."
    jump burger_start_menu

label burger_start_menu:

    menu:
        "I could go for a veggie burger!":
            $ burger_choice = "veggie burger"
            jump burger_ordering

        "Hmm, that juicy cheeseburger sounds good!":
            $ burger_choice = "juicy cheeseburger"
            jump burger_ordering

        "I think I'll pick the fish burger.":
            $ burger_choice = "fish burger"
            jump burger_ordering

        "A beef burger sounds good.":
            $ burger_choice = "beef burger"
            jump burger_ordering
        
        "I think I will go for some chicken tenders." if persistent.chickenTendiesUnlock:
            $ burger_choice = "chicken tenders"
            jump burger_ordering







label burger_ordering:
    n "[persistent.date] and you go to order the burgers."
    if persistent.burgerwent == 0:
        n "You were expecting having to order them from a screen like most fastfood places tend to have but as you looked around you couldn't spot any."
        n "Instead [persistent.date] walks to a counter.
        You decide to follow her."
    if persistent.rosename_knowledge == True:
        $ roseName = "Rose"
        n "An old lady, who you remember is called Rose, smiles at the both of you."
    else:
        n "An old lady smiles at the both of you."
    r "Hey [persistent.date], glad to see you here once more!"
    r "I'm almost surprised to see you here, it's been quite a while hasn't it?"
    if burger_nightmare == False:
        if persistent.rosename_knowledge == True:
            n "Rose looks at you for a brief moment and continues."
        else:
            n "The old lady looks at you for a brief moment and continues."

        r "Who did you bring along for the ride?"
        if not burgerBeenBefore:
            l "Oh right, you two haven't met. Rose, this is [persistent.name] and [persistent.name] this is Rose."
            $ persistent.rosename_knowledge = True
            $ roseName = "Rose"
            n "Rose gives you a sincere smile."
            r "Nice to meet you [persistent.name]."
        else:
            l "Oh, do you not recognize [persistent.name] Rose?"
            r "No, their face is not ringing any bells I'm afraid, should I recognize them?"
            l "I suppose not necesarilly, but with how good your memory is I thought you would remember them, they've eaten here before."
            r "Really? Huh... Still not ringing any bells I'm afraid. Might be my age slowly catching up on me."
            r "The woman lets out a hearty chuckle."
            r "Anyway [persistent.name], consider your face remembered from now on out!"
            if persistent.burger_faceRemembered == False:
                $ persistent.burger_faceRemembered = True
            else:
                n "And yet she never remembers you doesn't she?"
                n "No matter how hard she might try. No matter how many times she says she will."
                n "You will always be a stranger to her."
            
        
        r "So, what can I get the two of you?"
        n "[persistent.date] and you tell her both of your choices."
        r "A juicy cheeseburger and a [burger_choice] coming up! I'll bring them to you when they are done, alright?"
        r "That way you two can get to know each other some more."
        n "She gives [persistent.date] a quick wink that you just barely manage to catch."
        n "[persistent.date]'s face turning beetred is a lot easier to notice."
        l "{size=*0.5}Uhm, thank you Rose... we uhm have to get back to our table now.{/size}"
        n "You can't help but chuckle to yourself as [persistent.date] practically darts back to the table."
        n "By the time you've reached the table she is already sitting down, still as red as she possibly could be."
        n "She quickly brushes one hand over her left cheek and somehow manages to turn even more red at the realisation that she is still blushing."
        n "Right then she lets out a few small coughs as she tries to somehow divert attention from what just happened."
        n "As you sit back down she begins speaking once again."
        l "Thank you for choosing this place [persistent.name].
        It has been too long since I've been here, to tell you the truth I actually was avoiding this place.
        But now the happy memories come flooding back to me."

        n "[persistent.date] pauses for a moment, she seems unsure whether to continue or not."

        l"You know, my brother really used to love this place before..."

        n "[persistent.date] freezes before she can continue the sentence."
        l "{size=*0.5}Why did I have to bring that up now?{/size}"
        jump burger_brother

        menu burger_brother:
            "What was his name?":
                jump burger_brother_question

            "Are you alright [persistent.date]? You don't need to share this story if it hurts you too much.":
                $ love_points = + 1
                $ love_meter_updater(False)
                l "Honestly I'm not sure if I'll ever be fully alright because of what happened."
                l "And I think telling that story will always hurt."
                l "But that doesn't mean I wouldn't like to tell you about it."
                l "In fact, I think it might be good for me to eventually tell you."
                l "Just..."
                l "I just would like to wait a little before I do that, maybe some other time [persistent.name]?"
                l "I do really appreciate your concern for me though!"
                l "Oh, by the way, almost forgot to ask!"
                l "How are you liking your burger [persistent.name]?"
                menu:
                    "It's the best one I ever had!":
                    
                        if not burgerBeenBefore:
                            l "That good huh?"
                            n "Lilith let's out a small chuckle."
                            l "Rose's burgers are indeed extrememly tasty."
                            l "I'm glad you like them so much [persistent.name]!"
                            l "Although I hope this didn't ruin other burgers for you, it's hard to go back to regular burgers after you tasted these isn't it?"
                            l "The thing is, even if this burger is perfect, there will be days we have to make due with good enough. And in days like that we will need to try to atleast be satified with what we have."
                            menu:
                                "At least we'll have eachother, I'm sure anything would taste good if I'm enjoying your company.":
                                    l "You flatterer!"
                                    n "She just turned close to beetred."
                                    l "You are in luck though, I'd love to check out the other restaurants I mentioned together with you."
                                    if persistent.cafe_death_1 and persistent.chinese_death_1:
                                        n "Little does she know that she already did just that. Or well, a version of her I suppose."
                                        n "But you will never forget, will you?"
                                        n "How could you? Her deaths play out in front of your eyes every time you try to close them."
                                        if not persistent.burger_death_2:
                                            n "Do you think things will be better from here on out?"
                                            n "I guess only time will tell."
                                        elif lildeaths > 9:
                                            n "It seems her wish will be granted, over and over and over, she is lucky that she doesn't know what consequences that always brings."
                                            n "You can't help but feel slightly jealous of her for her ignorance."
                                            n "I suppose ignorance truly is bliss, isn't it?"
                                            n "You really would prefer if you didn't know what happens next here, what always happens."
                                        else:
                                            n "Just like how what will come next plays over and over in your head."
                                            n "You can't help but hope that this time will be different. You need to hope it, otherwise..."
                                            n "You don't want to finish that thought."

                                    l "But let's not get ahead of ourselves,let's focus on this beautiful moment first and then we can see how things go from there."
                                "I don't think I can ever part ways with this burger.":
                                    n "Lilith giggles, but as she does you think you can spot some concern in her eyes."
                                    l "I totally understand [persistent.name], sometimes it can be really hard to let go of something great."
                                    l "But if you never finish this burger and keep clutching on to it, it will begin to grow moldy."
                                    l "And if you do not clutch on to it but keep eating Rose's [burger_choice]s for the rest of your life they will grow very stale quicker than you think."
                                    l "I think sometimes we just need to enjoy what we have in the moment and when we don't enjoy something anymore, let go of it."
                                    l "It's easy to fool ourselves into thinking that if we liked something in the past we must like it now aswell."
                                    l "But sometimes it's just nostalgia, to how things were before, not even necesarilly to whatever you feel the need to hold on to."
                        else:
                            l "Really? That's very sweet of you to say [persistent.name]!"
                            l "But you've been here before, right? What makes this burger better?"
                            menu:
                                "I have never ordered this burger before, now I'm wishing I had.":
                                    n "She laughs quite loudly."
                                    l "If only you had a time machine, then you could."
                                    l "Wouldn't that be wonderful? To be able to go back in time as you please, maybe even change a few things?"
                                    if lildeaths > 9:
                                        n "That's the tricky part isn't it? To create any meaningful change at al. You've noticed it firsthand many times now."
                                    l "I'm sure we wouldn't have to stop on going back in time to eat burgers sooner, we could do so many great things."
                                "I never went here ith you before, it's the lovely company that makes it taste better.":
                                    l "You really are a charmer aren't you [persistent.name]?"
                                    if love_meter > 2:
                                        l "Although I have to admit that I feel the same way."
                                        l "It could also be that it's been such a long time since I've been here that the burgers taste even better but I think you have something to do with it aswell."
                                        l "It just feels... more special?"
                                        l "So I'm really happy to hear that you think the same thing [persistent.name]!"
                    
                    "It's pretty good.":
                        l "Pretty good, huh? That's high praise!"
                        n "Lilith gives you a warm smile, clearly pleased by your response."
                        l "I think \"pretty good\" is better than \"perfect\"."
                        l "How many things do you know that are perfect? Many of those tend to not remain perfect the harder and longer you begin to look."
                        l "Because in reality, almost nothing is truly perfect, and it also doesn't need to be."
                        l "I would say \"pretty good\" is more than good enough in most cases."
                        n "She takes a thoughtful bite of her own burger, as if savoring the moment."
                        l "I'm glad you're enjoying it, [persistent.name]."
                        if not burgerBeenBefore:
                            l "Maybe next time we can try some of the other things on the menu and see if they measure up?"
                        else:
                            l "Maybe next time we can go to that Chinese restaurant I talked about and see how you like the food there? It's really really good."

                    "It's a nothing burger, literally.":
                        label burger_nothingBurger:
                            n "Lilith tilts her head, a small frown tugging at the corner of her lips."
                            l "A \"nothing burger\" huh? I guess that means it's... okay?"
                            n "She tries to mask her disappointment with a soft chuckle."
                            l "Maybe it just didn’t live up to the hype. I hope it wasn’t too underwhelming, though."
                            if not burgerBeenBefore:
                                l "Rose makes all her burgers with as much love as is feasibly possible but maybe her [burger_choice] isn't really your thing?"
                                n "You can tell she was hoping you would enjoy it more."
                                l "If you'd like, we can come back and try something different next time. There's so much more on the menu here that might be more your style."
                            else:
                                l "Although I am slightly confused, to be honest with you."
                                l "You have been here before, right?"
                                l "Did you like the burger you had then?"
                                l "Because personally, the last word I would associate with Rose's burgers would be \"bland\"."
                                menu:
                                    "To be honest with you, the burgers I had here before were also quite bland. I just thought I should give it another chance since you were really enthusiastic about this place when you mentioned it.":
                                        l "Oh I see..."
                                        l "While I do appreciate you giving it another shot, I wish you wouldn't have felt the need to choose this place."
                                        l "You don't need to sacrifice yourself for my wants, alright [persistent.name]?"
                                        l "If you really don't like the burgers here we could have went to the cafe or to that chinese restaurant."
                                        if love_meter > 2:
                                            l "Afterall, I want this date to be nice for the both of us."
                                        l "But now that we are here, would you like to order something else?"
                                        l "Maybe some chicken tenders?"
                                        n "You shake your head. Even if you don't like the burger, you have to admit it fills you quite well."


                                    "Oh, I usually don't pick a burger, I tend to always pick chicken tenders.":
                                        n "Lilith can't help but chuckle slightly at your accidental joke."
                                        l "I see [persistent.name], that's totally fine."
                                        l "I just wonder what made you change your mind this time? Why did you pick a [burger_choice]?"
                                        menu:
                                            "I was in for a change.":
                                                l "I see, sometimes it's good to have a little change here and there isn't it?"
                                                l "That can truly be a breath of fresh air."
                                                l "Ofcourse, sometimes it can be a bit of a dissapointment."
                                                l "But good of you for trying something new, you never know what great things might come from that."

                                            "You were really enthusiastic about the burgers here and I didn't want you to think less of me because I picked chicken tenders.":
                                                l "Oh [persistent.name], I'm very sorry you felt that way."
                                                l "I would never judge you for what you order here."
                                                l "If anything I'm just happy to share your company here today."
                                                l "So next time"

                                            "Because the game only let me pick burgers." if persistent.kokiri_death_1 == True and persistent.burgerGameJoke == False:
                                                l "... What?"
                                                l "What are you talking about, what game?"
                                                l "Are you saying that this is all not real?"
                                                l "I would say that that sounds absurd..."
                                                l "But somehow..."
                                                n "She seemingly tries to study your face."
                                                l "You are not joking, right?"
                                                l "Oh god, so I am in a game?"
                                                l "We all are?"
                                                l "The ramifications of that are-"
                                                n "I'll have to stop her there, you aren't supposed to be able to tell her the truth in any of the restaurants, that she is inside of a game."
                                                n "Trust me, it's for the best."
                                                n "She needs a more calm place to properly process it fully."
                                                n "It seems that that dialogue choice was still a leftover from a time where you could tell her about that anywhere."
                                                n "Most of them were removed due to the Creator wanting to focus on it more in the woods."
                                                n "Let's just rewind to before you made this choice and remove it."
                                                if persistent.mayoFreak == True:
                                                    n "..."
                                                    n "I can already tell you that you are not happy about me railroading you like that."
                                                    n "Normally I would not care in the slightest."
                                                    n "But I don't want another mayo situation..."
                                                    n "So how about this? From now on you can order chicken tenders here if you'd like."
                                                    n "Yes, that should be fine for me to add, right? It doesn't change anything too major in the story afterall."
                                                    n "Isn't that cool? You unlocked a super secret menu option!"
                                                    n "{size=*0.5}It definetly wasn't always an option that I just didn't let you pick...{/size}"
                                                    n "Alright, back we go."
                                                    $ persistent.chickenTendiesUnlock = True

                                                $ persistent.burgerGameJoke = True
                                                jump burger_nothingBurger

                                        
                    "It's really bad.":
                        n "Lilith freezes for a moment, taken aback by your bluntness. Test"
                        $ love_points = -1
                        $ love_meter_updater(False)
                        if not burgerBeenBefore or not burgerBeforeLie:
                            l "Really bad? Oh no, I'm so sorry, [persistent.name]."
                            l "I hyped this place up so much, didn't I? Maybe that set your expectations too high."
                            n "She looks genuinely upset."
                            l "I guess taste is pretty subjective. But hey, at least now we know, right?"
                            n "She tries to force a smile, but it's clear your words stung more than she expected."
                            l "Maybe next time we could go somewhere else?"
                        else:
                            l "Really?..."
                            l "But you've been here before, right?"
                            l "Is something different now?"
                            n "Lilith gives you a confused look, she is clearly stumped."
                            menu:
                                "I never picked this burger before.":
                                    l "Oh I see, so this [burger_choice] isn't really your thing?"
                                    l "That's totally fine, I suppose not every kind of burger can be everyone's favourite after all."
                                    l "{size=*0.5}Although you could have been a little less blunt about it.{/size}"
                                    l "It's good of you to try something else though, picking the same thing over and over can get bland real fast."
                                    l "Although, sometimes it can be hard to do that, in the fear that the other experience will be worse than the familiar and comfortable thing you always pick."
                                    l "Maybe if we come here next time you can tell me what kind of burger you tend to like and I can recomend a few ones that I think you will like based on that?"

                                "I think there is something wrong with my burger.":
                                    l "Really?"
                                    l "Is there something you didn't order in there?"
                                    l "Or does it just not taste good?"
                                    l "Either way, it's very rare for Rose to mess up a burger."
                                    l "Of course mistakes can always happen."
                                    l "Would you like to see if she can make you another one of those burgers? I'm sure she wouldn't mind if you ask her nicely."
                                "I think the true problem here is the company.":
                                    
                                    l "Okay, I do not know what makes you think that you can talk to me like that [persistent.date]."
                                    l "If you have just come here to be mean to me than why did you even come here at all?"
                                    if persistent.lildeaths == 0:
                                        n "She does have a point, this game after all is called \"Great date with Lilith\". I wouldn't exactly call this date great at all..."
                                    else:
                                        n "She does make a good point, even if she does not know the full extent of it. You tried playing the game again to save her, didn't you?"
                                        n "Then why are you treating her like that?"
                                        n "Even if it could hypothetically save her, would it be worth it?"
                                    l "You weren't like this at all when we talked before, is this how you really are?"
                                    l "Either way, I won't stick around to find out."
                                    l "Goodbye [persistent.date]."
                                    $ angryLilith = True
                                    $ noTalkAngryLilith = True
                                    $ love_meter_updater(True) 
                jump burger_deathBuildup
    else:
        #TODO: Polish this nightmare slightly more
        r "I'm ofcourse also glad to see you here [persistent.name]!"       
        n "This startles you, she is not supposed to know your name."
        n  "It is true that you went to this restaurant before but that was only in loops so it's almost like it never happened now."
        n "You tell Rose that she's not supposed to know your name."
        r "Oh but how could I forget you?"      
        r "You are her killer right?"           
        r "You shot her."
        r "You blew her to smithereens."
        r "And I had to watch it. Over and over again."          
        n "You try to argue that you didn't pull the trigger, that it was someone else. That the explosion was out of your control."               
        r "It may not have been you causing all of those things directly."
        r "But that doesn't matter."
        r "You knew what would happen. And you still returned."
        r "You are responsible for what happened."
        r  "You tell yourself you do it to save her."
        r "But tell me the truth, isn't there a part of you that likes to watch her die again and again?"
        r "Well you're in luck you coldblooded killer, this time you can warm your hearth by eating her."
        n "She hands you a bloody clump that almost resembles a burger."
        r "I made it from Lilith herself, so there's plenty more for you."
        r "We have so many of her corpses lying around in the back, do you want to see your work?"
        $ nightmare = True
        $ burger_nightmare = False
        jump game_start


label burger_brother_question:

    $ askedbrother = True
    n "[persistent.date] tries to compose herself as well as she can but from the look in her eyes you can tell this is all a bit much for her."


    menu:

        "Try to alleviate tension with a joke.":
            jump burger_joke

label burger_joke:

    menu:

        "So a priest, a monk and a rabbit enter a bar. Says the rabbit :\"Whoops, did you slip your tongue there [persistent.name]?\"" if persistent.joke_knowledge:
            jump burger_joke_Abigail

        "You know, I've dated rocks before but they always tend to take things for granite.":
            jump burger_joke_1

        "The triangle thought about dating a circle but ultimately it seemed too pointless.":
            jump burger_joke_2

        "The computer mouse wanted to date someone who clicked with them.":
            jump burger_joke_3

label burger_joke_1:
    jump burger_joke_response

label burger_joke_2:
    jump burger_joke_response

label burger_joke_3:
    jump burger_joke_response

label burger_joke_Abigail:
    $ love_points = 1
    $ love_meter_updater(False)
    $ burger_jokeFromAbigailTold = True
    n "[persistent.date] bursts out in laughter."
    l "I really love that joke, my sister [persistent.date_sis] told me it once and I kept laughing and laughing for hat seemed like an eternity.
    Just thinking about it again, it fills me with a warm feeling, like a blanket you wrap around yourself in the coldest of winters."
    l "Thank you for cracking me up [persistent.name]!"
    n "[persistent.date] flashes you a cute smile, she seems pretty much completely composed once again."
    jump burger_living



label burger_joke_response:
    n "A slight smile forms on [persistent.date]'s face.
    She doesn't seem to find your joke that funny but from the gratitude in her eyes you can tell she is thankful for your effort.
    She seems to have become slightly more composed."
    #Typewriter:
    l "Thank you."
    n "[persistent.date] continues as if nothing happened."
    jump burger_living

label burger_living:
    l "So, what do you do for a living?"

    $ persistent.booklover_knowledge = True
    $ booklovertalked = True

    menu:
        "I'm an aspiring writer looking for a golden opportunity.":
            jump burger_living_writer

        "I'm currently unemployed but I sure like to write!":
            jump burger_living_unemployed

label burger_living_writer:
    l "That's pretty cool, you probably still have a whole journey to make to get from aspiring writer to a professional one."
    l "I also like to write something here and there in my free time, I'm not really wanting to become a writer, it's just something to put my emotions into. "
    l "I'd assume that's also a reason why you write, otherwise you probably wouldn't be dreaming of becoming a writer, right?"
    l "Well, try to never forget why you started writing in the first place, alright?
    And then maybe you'll find an opportunity, maybe you won't, but in the end you'll always have your passion for writing."
    menu:
        "Would you like to show something you've written?":
            jump burger_living_showWriting

        "Thanks for the tip [persistent.date], I'll keep it in mind!":
            jump burger_living_writer_thankTip


label burger_living_unemployed:
    l "Oh, do you like to write? That's pretty cool!"
    l "[persistent.date] seems to be quite enthusiastic, her eyes have a certain shimmer to them that wasn't there just a moment ago."
    l "I also like to write something from time to time, it's one of my hobbies actually."
    menu:
        "Would you like to show something you've written?":
            jump burger_living_showWriting


label burger_living_showWriting:
    $ persistent.burger_poem_knowledge = True
    n "A wide smile grows on [persistent.date]'s face."
    l "You want to read something of me?"
    l "I'd love that!"
    l "She eagerly digs in her handbag, retrieving a small notebook with a picture of a pug on it."
    l "I think you'll like this one!"
    n "She pushes the notebook, now flipped open, towards you.
    Suddenly you are reminded of the burger sauce that is all over your fingers."
    menu:
        "*Clean your fingers with a napkin before taking the notebook.*":
            $ burger_poem_cleancheck = True
            jump burger_living_showWriting_poem
        "*Don't clean your fingers and just take the notebook*":
            jump burger_living_showWriting_poem

label burger_living_showWriting_poem:
    if persistent.tracker == 1:
        $ persistent.tracker1 = True
    if burger_poem_cleancheck == True:
        n "[persistent.date] seems thankful that you cleaned your fingers.
        You take the notebook out of her hand and begin to read.
        You can read the entire thing in her voice somehow."
    else:
        $ love_points = -1
        
        n "[persistent.date] frowns when she sees your dirty fingers.
        nonetheless you take the notebook out of her hand and begin to read.
        You can read the entire thing in her voice somehow."
        $ love_meter_updater(False)

    l "Oh Moon
    here we are again, or rather, here I am again."
    l "Staring at my, our green horizon that never seems to cross with your silver.
    And yet every now and then it looks like you're waiting for me there, due to a trick of the light."
    l "Then I hear Orpheus' sweet sounds rise once more from the gap between Life and Death.
    But Orpheus' tune is quickly twisted into something else."
    l "And then I'll be here and you’ll be there once again.
    I don't know whether to cry or laugh when I look at my, our, green horizon."
    l "All I know is that we better not listen to the dwindling of Orpheus' tune."
    l "Has something that has not been seen or heard really happened?"
    if burger_poem_cleancheck == True:
        n "When you get done reading your eyes linger on the notebook a bit longer before returning it to [persistent.date]."
        l "So [persistent.name], what did you think of it?"
        n "She seems eager to find out what your thoughts are on her writing."
        jump burger_poem_rating
    else:
        n "When you get done reading your eyes linger on the now dirtied notebook a bit longer before returning it to [persistent.date]."
        l "So, what did you think of it?"
        n "She seems irritated by your actions but is asking out of politeness."
        jump burger_poem_rating


label burger_poem_rating:
    menu:
        "That was really terrible.":
            jump burger_poem_rating_terrible
        "Wow, you really impressed me. That was fantastic!":
            jump burger_poem_rating_fantastic
        "I liked it a lot! Though could you explain who Orpheus is?":
            l "His music was so beautiful that it could charm anyone or anything. People, animals, even rocks and trees would stop to listen when he played his lyre."
            l "He fell in love with a woman named Eurydice, and they were incredibly happy together."
            l "But one day, Eurydice was bitten by a snake and died. She was taken to the Underworld, which is like, you know, the place of the dead in Greek mythology."
            l "Orpheus was heartbroken, so he decided to he travel to the Underworld to get her back."
            l "He played his lyre for Hades and Persephone, the rulers of the Underworld. His music was so moving that even they were brought to tears."
            l "They agreed to let Eurydice return with him to the world of the living, but there was one condition."
            l "He wasn't allowed to look back at her until they had both reached the surface. If he did, she would be lost to him forever."
            l "So they started their journey back, with Orpheus leading the way. He could hear her footsteps behind him, but he couldn’t see her."
            l "Just as they were about to reach the surface, doubt and fear got the better of him. He turned around to make sure she was really there..."
            l "...and in that moment, she vanished. Forever."
            l "Something about that story really intrigues me, I can't entirely put it into words though."
            #TODO: Attempt to put it into words slightly, try to make it thematic. Something about two figures that are so close to getting together, to being free and yet it all goes wrong. Also, wRewrite the above stuff some more.
            l "Anyway, that’s the short version. I hope I didn't make you regret asking that too much [persistent.name]..."
            $ persistent.burger_Orpheus_knowledge = True



label burger_poem_rating_terrible:
    $ love_points = -1
    $ love_meter_updater(False)
    n "[persistent.date] begins to frown slightly.
    She looks hurt by your words."
    l "Oh...
    No need to be a douche about it."
    jump burger_Brotherasked



label burger_poem_rating_fantastic:
    l "A wide smile appears on [persistent.date]'s face."
    l "Thanks [persistent.name]! I'm glad you like it so much."
    l "It's funny isn't it? I wrote that poem many years ago, when I was in a slightly edgy phase."
    l "And now, everytime I read it again or show it to someone else it is like a timecapsule of how I was at that time."
    l "I think that it is beautiful how writing more than any other form of art can so delicately capture the imprints of the people we were at the time we made it."
    l "Isn't that amazing? How you could capture one moment and freeze it in place?"
    if persistent.lildeaths > 3:
        n "And yet, what wouldn't you give to thaw that moment out of it's stagnancy?"
        n "A frozen moment is only beautiful to those that can admire it for a while and then move on. It is horifying for those that are trapped inside it."
    jump burger_Brotherasked







label burger_living_writer_thankTip:
    n "[persistent.date] gives you a big smile."
    l "You're more than welcome!
    This tip applies to all sort of things, not only writing."


    l "I would have loved to have been given the same advice when I needed to hear it the most."
    l "You see, I actually used to play the trombone.
    I loved playing music on that thing, you could say it was my passion."

    l "But after nine years of music lessons I caught myself just playing music for the sake of getting it done."
    l "I quit that year.
    Now I barely play the trombone anymore."
    menu:

        "Oh, I'm sorry that you lost a hobby.":
            jump burger_living_writer_thankTip_sorryHobbyLost

label burger_living_writer_thankTip_sorryHobbyLost:
    n "[persistent.date] laughs."
    l "No worries, I really like music and I will always treasure my memories with the trombone."
    $ persistent.musiclover_knowledge = True
    $ musiclovertalked = True
    l "But if I kept playing it I think I would slowly grow to resent it, sometimes it's just better to end things on a good note."
    n "[persistent.date] lets out a small giggle."
    l "That pun wasn't intended, I swear!"
    jump burger_Brotherasked

label burger_Brotherasked:
    if askedbrother == True:
        if love_meter >= 3:
            $ persistent.brother_knowledge = True
            n "[persistent.date] pauses for a moment."
            l "You asked what my brother's name was, right?
            I don't know why but I feel like I can trust you enough to tell you about him.
            I might tear up, it's been a long time since I've told his story to anyone."
            l "His... his name was [persistent.date_ghost]."
            l "He was the best brother I could have asked for.
            He was five years older than me but we always played together.
            We used to be the best of friends, playing hide and seek, video games, making our own stories to act out, you name it."
            l "He was always there for me, he supported me however he could and appreciated me."
            n "When she talks about her brother you can see one of the biggest smiles you've ever seen growing on her face."
            l "But that's when it happened..."
            n "[persistent.date] pauses for a moment as she gasps for air, you can see tears dripping off her face."
            l "He was only seventeen when he got hit by a speeding car.
            He didn't die immediately, they say he must have layed there for an hour before..."
            l "My... father..."
            n "She seems to test the taste of those words, looking at her expression, they seem to taste quite bitter."
            l "David couldn't accept [persistent.date_ghost] dying and left us.
            That day two people were taken away  from me by a car.
            Actually, scratch that, David had a choice in the matter, [persistent.date_ghost] was the only one really taken away from me."
            l "Mom really tried her best to fill the void left by them but the presence of their absence has always haunted us since that horrible day."
            if burger_jokeFromAbigailTold == True:
                l "My sister, [persistent.date_sis], the one from the joke you just told, is 5 years younger than me so she doesn't really remember much of what happened."

            else:
                l "My sister, [persistent.date_sis], is 5 years younger than me so she doesn't really remember much of what happened."
            #TODO Make this a flag. Also rewrite that line slightly.
            n "She lets out a sigh of relief."
            l "As much as it hurts me to talk about [persistent.date_ghost] it feels good to finally let it all out once again.
            Thank you for listening to me ramble on [persistent.name]."
            $ persistent.brother_knowledge = True
            jump burger_deathBuildup

label burger_deathBuildup:
    n "Suddenly you hear screaming from a few shops further."
    l "What was that?"

menu:
    "It's probably not our concern.":
        jump burger_deathBuildup_choice1

    "Maybe there is a sale going on somewhere?":
        jump burger_deathBuildup_choice2

    "This is important, duck now." if persistent.burger_death_1 and not burger_alt:
        jump restaurant_death_1_prevented

label burger_deathBuildup_choice1:
    if burger_alt == False:
        l "You're probably right, it's probably not even a big deal anywa-"
        jump restaurant_death_1
    else: 
        l "You're probably right, it's probably not even a big deal anyway."
        jump burger_alt_askHerAQuestion


label burger_deathBuildup_choice2:
    l "Let's hope it's just that."
    if burger_alt == False:
        jump restaurant_death_1
    else:
        jump burger_alt_askHerAQuestion

label burger_alt_askHerAQuestion:

    $ burger_alt = False

    menu:
        "*Ask her a question.*":
            menu:
                "So you mentioned that you really like music. Which music do you listen to?" if persistent.musiclover_knowledge and musiclovertalked:
                    jump burger_alt_askHerAQuestion_musicLover
                "Which music do you like to listen to?" if persistent.musiclover_knowledge and not musiclovertalked:
                    jump burger_alt_askHerAQuestion_musicLover
                "So you mentioned that you like writing. That made me curious, which books do you like to read?" if persistent.booklover_knowledge and booklovertalked:
                    jump burger_alt_askHerAQuestion_bookLover
                "Which books do you like to read?" if persistent.booklover_knowledge and not booklovertalked:
                    jump burger_alt_askHerAQuestion_bookLover

label burger_alt_askHerAQuestion_musicLover:
    l "Oh, I'm glad you asked [persistent.name]!"
    l "I like quite a few genres and bands, it mostly depends on how I am feeling at the time."
    l "The genres I tend to listen to the most are jazz, rock, and heavy metal."
    l "My favourite bands shift around all of the time but for this moment I think King Crimson, I Monster and Smashing Pumpkins are in my top three."
    l "I think that the reason they are in my top three is how much they tend to innovate with every song they make."
    l "Now that I think about it, Kishi Bashi is also excellent at innovating, he's definetly also worth checking out!"
    l "It's very hard to keep adding to something like an album with song after song and still make it as special as the first one someone has heard."
    l "After a while it might seem like some artists are just going through the motions of pumping out song after song that they know will do great, but that they aren't happy with."
    l "And their fans will be going through the motions of listening to each and every single song to relive that sense of wonder they had at first, but it is never going to be the same."
    menu: 
        "What do you think is the best way to restore that feeling of wonder?":
            l "Honestly? I think it would be to break the loop. To just try something else."
            l "It could be as simple as listening to a cover of the song that got stale but in a different style."
            l "Or you might need to be more drastic and find another band with different songs."
            l "I think as long as you can enjoy yourself once again, that you're not just going through the motions of pretending, then you are on the right track."
            l "After all, there is no shame in falling out of love with a certain band or number, as long as you don't get something out of them anymore, why should you listen to them?"
        "I'll definetly have to check some of those bands out one day, thank you for the tip [persistent.date]!":
            l "You're totally welcome [persistent.name], I always love recommending music to people, I like to think music has a really strong impact."
            l "After all, it can make you feel all kinds of emotions, calm you down, energise you, even relief pain slightly."
            l "Isn't that wonderful?"
    l "But anyway, what are your favourite bands and genres of music [persistent.name]? "
    menu:
        "My favourite band is-":
            jump restaurant_death_2


label burger_alt_askHerAQuestion_bookLover:
    $ persistent.bookpreference_knowledge = True
    l "Oh, that's a very good question."
    l "Well, to begin I always liked reading about mythology."
    l "It started when I was about ten years old and got the Percy Jackson books as a gift."
    l "They sucked me into the world of Greek and Roman myths, they are essentially the reason I studied Latin in my high-school."
    l "During that time, probably in my first or second year I got this lovely book with a collection of a ton of Greek and Roman myths."
    l "I have read that thing so many times that you can see the wear and tear of pretty much every page."
    l "Recently I've been expanding my reach by learning about Finnish mythology, I picked up the Kalevala and haven't been to put it down until I finished it."
    l "I am less familiar with those myths since I picked it up for the first time about a week ago but I'd love to read it again for quite a few times until I'm as familiar with it as the Roman myths."
    l "I also really enjoy to read Haruki Murakami's works, an old friend of mine introduced me to them and since then I've read 'First person singular', 'After dark' and '1q84'."
    l "He has a hauntingly beautiful way of describing even the most mundane things. It's like I can see the world for the first time again but not through my eyes, through his instead."
    l "I love it when someone can make me look at mundane things in a whole new perspective."
    l "So, which books do you like to read [persistent.name]?"
    menu:
        "I really like-":
            jump restaurant_death_2
