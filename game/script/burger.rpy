
label burger_start:
    $ burger = True
    if persistent.lildeaths > 0:
        if no_nightmare == False:
            if persistent.perm_nightmare == True:
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
    if persistent.rockMode:
        jump rockTransport
    scene black
    show burgerRestaurant_bg
    show burgerRestaurant_fg onlayer foreground
    
    transform burgerSit:
        zoom 0.40
        xanchor 0.5
        yanchor 1.0
        xpos 800
        ypos 1000
    show lilith talking_happy at burgerSit

    n "You arrive a tad late, [persistent.date] already has grabbed [date_ref] a seat and waves at you when [date_sub] [conj('date', 'sees', 'see')] you."
    label burger_arrived:
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

            "Sorry, traffic was quite bad." if not persistent.rockMode:
                jump burger_start_choice3

            "Sorry, I think traffic was quite bad? It was pretty hard to tell underneath a shoe." if persistent.rockMode:
                jump burger_start_choice3

            "Hey glad to be here. Could we sit somewhere else though?" if persistent.burger_death_1 and not persistent.rockMode:
                $ burger_alt = True
                n "[persistent.date] gives you a smile and a thumbs up."
                l "Sure, where would you like to sit?"
                n "You quickly point to a table, any will do, as long as that lost bullet doesn't find [date_obj]."
                l "Alright, that table it is then!"
                n "[persistent.date] takes [date_pos] handbag and wanders to the table as you follow."
                n "You feel relieved, knowing just what horrors you escaped from."
                n "The image of [date_obj] collapsed on the floor, bleeding profusely, is burned into your mind."
                n "Recalling it sends nothing but shivers down your spine. Not that you are trying to recall it, the memory just haunts you."
                n "Desperately trying to shake it off, you remind yourself that it's probably best to try focussing on the present, not the past."
                n "It cannot happen again. [persistent.date] has to be safe now. You are unsure if you can stomach [date_obj] dying on you again."
                l "Are you alright [persistent.name]? You look like you have seen a ghost."
                n "[date_sub!c] [conj('date', 'is', 'are')] not far off, [conj('date', 'is', 'are')]n't [date_sub]?"
                menu:
                    "Don't worry, I am fine, I was just thinking about the traffic jam I was stuck in.":
                        jump burger_start_choice3

label burger_start_choice1:
    n "[persistent.date] chuckles."
    l "Ah, another burger fan!"
    l "We are at the right place I'd say, the burgers here are delicious."
    if persistent.rockMode:
        l "Altleast that's what I think. Something about them just... {i}feels{/i} that way?"
        l "To the point that even I know they must be fantastic somehow."
        l "Have you been here before? Maybe that is what somehow gives us knowledge of their taste."
    else:
        l "Did you already know that or is this your first time here?"
    menu:
        "I actually didn't know that, I've never been here before." if persistent.burgerwent == 0:
            jump burger_beenBeforeXTimes

        "I knew that, I've been here a couple of times. (Lie)" if persistent.burgerwent == 0:
            $ burgerBeforeLie = True
            jump burger_beenBeforeXTimes

        "I knew, I've been here before, only once though." if persistent.burgerwent == 1:
            jump burger_beenBeforeXTimes

        "I'm well aware, I've been here exactly [persistent.burgerwent] times." if persistent.burgerwent > 1 and not persistent.rockMode:
            n "It sounds a bit weird if you phrase it like that, doesn't it?"
            jump burger_beenBeforeXTimes

        "I knew, I've actually been here a couple of times." if persistent.burgerwent > 1:
            $ burgerBeenBefore = True
            l "Oh you have? That makes sense, these burgers are the best of the state, scratch that, of the world!"
            if not persistent.rockMode:
                n "While [date_sub] is enthusiastically exclaiming this [date_pos] arms kind of seem to have a life of their own, making all kinds of gestures to get the point across even more."
                n "When [date_sub] catches [date_pos] arms in the act [date_sub] blushes slightly, quiets for a moment and places [date_pos] hands back down on the table."
                l "So, what are you going to pick? I think I'll go for the juicy cheeseburger myself."
                n "[date_sub!c] [conj('date', 'is', 'are')] making a visible effort to not move [date_pos] arms from their position on the table."
            else:
                l "They are so great. They must be! While we cannot thoroughly taste them to test them out, we sure can imagine."
                l "Although I wonder. If you could order one thing here, what would you pick?"
                l "I think I'd go for the juicy cheeseburger, something about that choice just feels... right."
                $ hypotheticalBurger = True
            jump burger_start_menu

label burger_beenBeforeXTimes: #TODO: Probably add some more choices like the once_greatTaste one. I feel like that'd add a lot more variety.

    if persistent.burgerwent > 0:
        $ burgerBeenBefore = True

    if persistent.burgerwent == 0:
        if burgerBeforeLie == False:
            l "I'm sure after today that will change. They have really great burgers like I said before."
            if love_meter >= 3:
                l "So something tells me you will come here often after this. Maybe... some of those times with me?"
            else:
                l "You might find yourself coming here more often than you'd have expected. The burgers might just be magic."
        else: 
            jump burger_beenBeforeXTimes_once_greatTaste
            

    elif persistent.burgerwent == 1:
        if persistent.rockMode:
            l "Oh, you've been here before? Is that why you wanted to come back here so much? I must admit, I can't blame you at all." #TODO: Not sure if this is an inconsistencie... at a certain point she say she has been here before as a rock, but here she acts as if she never saw it.
            l "This place sure looks lovely, pretty cozy too!"
        else:
            jump burger_beenBeforeXTimes_once_greatTaste

    else:
        if persistent.burgerwent <= 4:
            l "Ah, you've been here a few times already."
            if persistent.rockMode:
                l "I guess you must like the feel this place has quite a lot. I can't blame you honestly, it's absolutely great!"
            else:
                l "Then you surely know how good the burgers are here."

        elif persistent.burgerwent <= 6:
            l "Wow, you've been here quite a few times already!"
            l "You must really like it here then, I knew we were on the same wavelength!"
            if persistent.rockMode:
                l "This place really seems cozy to me. I can see why there's so many people here."
            else:
                l "We aren't the only ones on that wavelength, there's pretty much always a nice crowd here. The burgers here have a legendary reputation."
        elif persistent.burgerwent <=9:
            l "Wow, you've been here a lot of times!"
            if not persistent.rockMode:
                l "... Come to think of it, you might have visited this place more than I have."
                n "[persistent.date] lets out a small giggle."
            else:
                l "If you were that eager to come back here this place must be really great."
                l "All these people here seem to agree with you."
        elif persistent.burgerwent < 22:
                if not persistent.rockMode:
                    n "[persistent.date] lets out a joyful laugh."
                    l "Wow! I almost feel like I should let you choose my burger with all that burger knowledge you must have."
                    l "Almost though, this is far from my first rodeo either [persistent.name]!"
                else:
                    l "Wow, that many times? You must really like the vibes of this place."
                    l "I have to say, I can see why, who knows? Maybe it won't be long before I beat your high score."
                    n "A joyful laugh rings in your mind."
        else:
            if not persistent.rockMode:
                l "Wow... is it weird to be impressed by that?"
                n "[persistent.date] lets out a small laugh."
                l "It probably is but I'm quite impressed by the expertise you must have when it comes to the burgers here."
                l "At this point you might just have to order my burger for me."
            else:
                l "You could practically live here [persistent.name]!"
                l "Now that doesn't sound like a bad idea actually..."
                l "I'm sure they wouldn't notice two little pebbles just hanging around, right?"
                n "A small laugh rings in your mind."
                l "I'm kidding, I'm kidding."
    if not persistent.rockMode:
        l "So, which burger do you want to pick? I think I'll go for the juicy cheeseburger myself."
    else:
        l "Imagine, you could eat one thing here. What would you pick? I think I'd like to taste the juicy cheeseburger."
        $ hypotheticalBurger = True
    jump burger_start_menu

label burger_beenBeforeXTimes_once_greatTaste:
    l "I see, in that case you have great taste!"
    n "[date_sub!c] [conj('date', 'lets', 'let')] out a hearty chuckle."
    menu:
        "Of course, afterall, I am here with you, aren't I?":
            $ love_points += 1
            $ love_meter_updater()
            l "Uhm- I uhm- {size=*0.5}thank you [persistent.name]{/size}"
            n "[date_sub!c] [conj('date', 'is', 'are')] clearly flustered by your words."
            n "[date_obj!c] face is as red as a tomato as she just desperately tries to find any sensible reply."
        
        "Oh I assure you, those burgers taste a lot better than me.":
            n "[date_sub!c] [conj('date', 'bursts', 'burst')] out laughing. You can't help but join [date_obj]. [date_sub!c] [conj('date', 'has', 'have')] a very infectious laugh."
            l "I was not expecting that joke at all, great taste and great humor? You really are a jack of all trades it seems."

label burger_start_choice2:
    l "I'm flattered you are so happy to see me. Or perhaps it's the burgers you don't want to miss?"
    l "[persistent.date] chuckles slightly."
    l "Sorry, I'm just messing with you."
    if not persistent.rockMode:
        l "So, what are you going to order? I think I'll go with a juicy cheeseburger."
    else:
        l "Let me make it up to you. You can order anything off the menu and I'll pay for it. How does that sound?"
        n "You hear [date_pos] soft chuckles echo in your mind once again."
        l "What would you like to pick?"
        $ fakeBurger = True
    jump burger_start_menu

label burger_start_choice3:
   
    if not persistent.rockMode:
        l "Now that you mention it, I had heard about it. The radio said some ghostrider caused the traffic jam."
        l "If I'm not mistaken it was a Sedan or something similar?"
    else:
        n "[date_sub!c] [conj('date', 'lets', 'let')] out a hearthy telepathic laugh."
        l "No worries at all [persistent.name]"
        l "I heard something about that on the radio, I think they mentioned there was a traffic jam caused by a ghostrider."
        l "I did not manage to catch the rest of that though, it sounded so muffled from underneath my lift's shoe."
        n "[date_sub!c] [conj('date', 'lets', 'let')] out a small chuckle, you feel it ring a little in your mind."
    if not persistent.rockMode:
        l "Anyway, what do you want to order off the menu? I think I am going to go with a juicy cheeseburger."
    else:
        l "Stressful times like that make you wish for some lovely food, don't they? Even make you wish that we could eat at all."
        l "...Actually, that gives me an interesting idea. If you could pick anything to eat here, what would you choose?"
        $ hypotheticalBurger = True
    jump burger_start_menu

label burger_start_menu:
    if not hypotheticalBurger:
        menu burgerChoice:
            "I could go for a veggie burger!":
                $ burger_choice = "veggie burger"
                jump burger_ordering

            "That juicy cheeseburger sounds good!":
                $ burger_choice = "juicy cheeseburger"
                jump burger_ordering

            "I think I'll pick the fish burger.":
                $ burger_choice = "fish burger"
                jump burger_ordering

            "A beef burger sounds nice.":
                $ burger_choice = "beef burger"
                jump burger_ordering
            
            "I think I will go for some chicken tenders." if persistent.chickenTendiesUnlock and not onlyBurgers:
                jump burger_chickentenders
               
        menu:
            "I would pick a veggie burger!":
                $ burger_choice = "veggie burger"
                jump burger_ordering

            "That cheeseburger does sound good, I'd probably pick the same.":
                $ burger_choice = "juicy cheeseburger"
                jump burger_ordering

            "I think I would pick the fish burger.":
                $ burger_choice = "fish burger"
                jump burger_ordering

            "A beef burger would be lovely.":
                $ burger_choice = "beef burger"
                jump burger_ordering
            
            "I definetly would pick the chicken tenders." if persistent.chickenTendiesUnlock:
                $ burger_choice = "chicken tenders"
                jump burger_ordering

            "What's the point of dreaming about food if neither of us can eat it?":
                jump restaurant_menu_pointOfPretending

label burger_chickentenders:
    l "Oh... I thought you were going to try one of Rose's burgers?"
    l "I promise, they are to die for! Those tenders are pre-made. Still good ofcourse but they pale to Rose's craftsmanship."
    menu:
        "That does sound good... sure, I'll pick a burger!":
            $ onlyBurgers = True
            jump burgerChoice

        "I'm actually more in the mood for tenders.":
            l "I see, that's totally fine! Sorry if I was a bit pushy just now, I just really love the burgers here."
            $ burger_choice = "chicken tenders"
            jump burger_ordering

        "I yearn to touch the tenders. To feast on fistfuls of flesh from feathered dinosaurs. Doth not come between me and mine tenders!":
            "...Are you alright [persistent.name]?"
            menu:
                "Of course, I am better than ever, so close in the vicinity of some succulent chicken.":
                    l "You're scaring me [persistent.name]! I...Why are you acting so obsessed with chicken tenders?"
                    l "Is this a joke? Please say literally anything else!"
                    menu:
                        "Why waste another breath on anything lesser when it should be spent on praising and eating the tenders?":
                            n "Her face turns completely pale."
                            l "Oh god, you aren't joking, are you?"
                            l "You're going mad! I...I can't do this [persistent.name]!"
                            n "She quickly gets up and runs out of the restaurant."
                            n "You don't even consider running after her for a second, you have other priorities."
                            n "It is however odd that you don't hear the impact of the car that would usually hit her."
                            n "You can't get distracted though, you have tenders to eat."
                            n "Walking up to Rose with a sickly grin you order all the chicken tenders she has in stock."
                            n "Scarfing them down like a dog until closing time, you only leave when it is closing time."
                            n "You camp outside, ready to repeat all of this the next day and the day after that ad infinitum."
                            n "Or atleast until your heart decides to give out from all the greasy goodness."
                            #Ending
                            $ persistent.ending_food = True
                            $ lilithAliveEnding = True
                            $ ending_check = "food ending"
                            jump gameOver

label burger_ordering:
    if persistent.rockMode == False:
        if burger_choice == "juicy cheeseburger":
            l "Great minds think alike I suppose!" #TODO: If she said you have great taste, then reference this aswell here, something like "You really do have great taste!"
        else:
            l "That's a great choice [persistent.name]!"
        l "Let's go order, alright?"
        define move_out_left = MoveTransition(3.0, leave=offscreenleft, leave_time_warp=_warper.easeout)
        hide lilith talk_closed with move_out_left #move_out_left is a custom defined move transition since this is the only way to not have it hapen in 0.5 seconds
        if persistent.burgerwent == 0:
            n "You look around to search for a self-service screen like most fastfood places have however, you can't spot any."
            n "Instead [persistent.date] walks straight to the counter."
            n "You decide to follow [date_obj]."
            #TODO: If you have told her you have been here before she will find this odd because you seemingly tried to look for a self-service screen while they don't use it.
            #Have her shoot you a subtle glance and then mention it later at the table.

        else: 
            if love_meter >= 3:
                n "You walk towards the counter, [persistent.date] is right next to you, shooting you a subtle glance every now and then."
            else:
                n "You walk towards the counter, [persistent.date] is right next to you."

        if persistent.rosename_knowledge == True:
            $ roseName = "Rose"
            n "The old lady, who you remember is called Rose, smiles at the both of you."
        else:
            n "An old lady smiles at the both of you."
        
        if burger_nightmare == False:
            r "Hey [persistent.date], glad to see you here once more!"
            r "I'm almost surprised to see you here, it's been quite a while hasn't it?"
            #TODO: Probably have lilith say something alluding to how she stopped coming here after what happened to James and Rose saying it's alright, that she doesn't need to get into detail because she knows it's a hurtful topic.
            #That way lilith would later be able to more easily bring up james if you ask her about it.
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
                    n "Yet she never remembers you doesn't she?"
                    n "No matter how hard she might try. No matter how many times she says she will."
                    n "You will always be a stranger to her."
                
            r "So, what can I get the two of you?"
            n "[persistent.date] and you tell her both of your choices."
            if burger_choice == "juicy cheeseburger":
                r "Two juicy cheeseburgers coming right up! I'll bring them to you when they are done, alright?"
            else:
                r "A juicy cheeseburger and a [burger_choice] coming right up! I'll bring them to you when they are done, alright?"
            r "That way you two can get to know each other some more."
            n "She gives [persistent.date] a quick wink you just barely manage to catch."
            n "[persistent.date]'s face turning beetred is a lot easier to notice."
            l "{size=*0.5}Uhm, thank you Rose... we uhm have to get back to our table now.{/size}"
            n "You can't help but chuckle to yourself as [persistent.date] practically darts back to the table."
            show lilith talking_happy at burgerSit
            n "By the time you've reached the table [date_sub] [conj('date', 'is', 'are')] already sitting down, still as red as [date_sub] possibly could be."
            n "[date_sub] quickly brushes one hand over [date_pos] left cheek and somehow manages to turn even redder realising that [date_sub] [conj('date', 'is', 'are')] still blushing."
            #TODO: Probably instead make this her looking for something but not being able to say it, you then can say a few things to break the tension. One of which is asking what absence Rose was talking about.
            n "Right then [date_sub] lets out a few small coughs as [date_sub] [conj('date', 'tries', 'try')] to somehow divert attention from what just happened."
            n "As you sit back down [date_sub] begins speaking once again."
            l "Thank you for choosing this place [persistent.name]. It has been too long since I've been here, to tell you the truth I actually was avoiding this place."
            l "But now the happy memories come flooding back to me."
            n "[persistent.date] pauses for a moment, [date_sub] [conj('date', 'seems', 'seem')] unsure whether to continue or not."
            l"You know, my [ghost_sib] really used to love this place before..."
            n "[persistent.date] freezes before [date_sub] can continue the sentence."
            l "{size=*0.5}Why did I have to bring that up now?{/size}"
            jump burger_brother

            menu burger_brother:
                "What was [ghost_pos] name?":
                    jump burger_brother_question

                "Are you alright [persistent.date]? If this story hurts too much you don't have to continue.":
                    $ love_points += 1
                    $ love_meter_updater(False)
                    l "I don't think I'll ever be fully alright because of what happened. I think telling the story will always hurt."
                    l "However that doesn't mean I wouldn't like to tell you about it."
                    l "In fact, I think it might be good for me to eventually tell you."
                    l "Just... maybe some other time [persistent.name]?"
                    l "I do really appreciate it though. Thank you for being so considerate."
                    n "Things grow quiet for a moment. It's not necessarily a bad quiet, it's one [date_sub] needed."
                    n "You can tell so by [date_obj] body slowly relaxing into the state [date_sub] [conj('date', 'was', 'were')] in before."
                    n "Then, when [date_sub] [conj('date', 'is', 'are')] properly recouped, the silence once again makes room for conversation."
                    l "Oh, I almost forgot to ask."
                    l "How are you liking your burger [persistent.name]?"
                    jump burger_burgerRate
                    
        else:
            r "Hey [persistent.date] and [persistent.name], welcome back!"  
            n "This startles you. You never came here before the loop. She {i}can't{/i} know you."
            n "You ask Rose how she knows your name."
            r "Oh but how could I forget you? The two of you have been here quite a few times, haven't you?"
            r "[burgerwent] times in total if I'm not mistaken."
            r "You are [date_pos] killer right?"           
            r "You shot [date_obj]."
            r "You blew [date_obj] to smithereens."
            r "All the while I had to watch it. Over and over again." 
            menu:
                "I didn't pull the trigger on the gun. The explosion was out of my control.":          
                    r "You may not have caused those things directly, but does that truly matter?"
                    r "You knew what would happen and yet you still returned. That's what makes you responsible for the outcome."
                    r "You tell yourself you come back to see [date_obj] survive, yet I wonder if another part of you doesn't want to see [date_obj] die."
                    r "You truly are a coldblooded killer, aren't you? You are in luck that I have a heartwarming burger, just for you."
                    n "She hands you a fleshy clump that almost resembles a burger."
                    r "It's made with lots of love, just not mine. The only emotion I bled into it was hate."
                    r "[date_obj!c] love. [date_sub!c] came here with nothing but blind trust and hope for a good future, but look how she ended up now. It truly breaks my heart."
                    n "As she speaks these words she gestures to the burger in your hand, you swear you feel it twitch and pulse."
                    n "She gives you an impatient look."
                    r "Well, aren't you going to eat it?"
                    r "You've held on to it for so long it has turned rotten."
                    r "You just stood here with it in your hand for [persistent.retry_counter] days straight."
                    r "What a shame. If you kill [date_obj] atleast don't make [date_obj] flesh go to waste."
                    r "Oh well, the two of you are rotten, one on the outside and one on the inside. Go on, give [date_obj] a try anyway."
                    r "Here, let me help you out [persistent.name]. Didn't you want to be together with [date_obj]? I know just how to grant that wish."
                    n "She takes the burger from your hand, forces your jaw open and slowly slides the burger down your esophagus. You can feel it squirming as it wriggles down your throat."
                    
            $ nightmare = True
            $ burger_nightmare = False
            $ persistent.nightmareCounter += 1
            jump game_start
    else:
        if fakeBurger == True:
            l "Sounds good! Let me just telepathically call my rock to human translator."
            n "[date_sub!c] [conj('date', 'bursts', 'burst')] out in laughter once again."
            l "I'm sorry [persistent.name], I couldn't resist. I promise I will play nice from now on out."
        else:
            if burger_choice == "juicy cheeseburger":
                l "My my, I suppose great minds think alike, don't they [persistent.name]?"
                l "[date_sub!c] [conj('date', 'lets', 'let')] out another chuckle."
            elif burger_choice == "chicken tenders":
                l "They serve those here? I would say they probably won't live up to the reputation of the burgers here."
                l "Although, I suppose if one place could pull it off it might just be this one!"
            else:
                l "Ah, that sounds like a lovely choice [persistent.name]!"
        jump burger_ordering_rockModeIsolation

menu burger_burgerRate:
    #TODO: I don't think Rose ever delivers the burgers to the table, have a scene for that.
    "It's the best one I ever had!":
        call burger_burgerRate_best
           
    "It's pretty good.":
        call burger_burgerRate_prettyGood
       
    "It's a nothing burger, literally.":
        call burger_burgerRate_nothingBurger
     
    "It's really bad.":
        call burger_burgerRate_reallyBad

jump burger_deathBuildup
      
label burger_burgerRate_best:
    if not burgerBeenBefore:
        l "That great? I honestly can't say I'm surprised. Rose's burgers are the best for a reason after all."
        n "[persistent.date] let's out a small chuckle."
        l "I'm glad you like them so much [persistent.name]!"
        l "Although I hope this didn't ruin other burgers for you, it's hard to go back to regular burgers after you tasted these isn't it?"
        l "The thing is, even if this burger is perfect, there will be days we have to make due with good enough. In days like that we will need to try to atleast be satified with what we have."
        l "Afterall, you can't eat nothing but these burgers, I don't think that'd be healthy."
        menu:
            "At least we'll have eachother, I'm sure anything would taste good if I'm enjoying your company.":
                $ love_points += 1
                $ love_meter_updater()
                l "You flatterer!"
                n "[date_sub!c] just turned close to beetred."
                l "In that case I'd like to try out the other restaurants I mentioned. Surely anything will taste good as long as we are together."
                if persistent.cafe_death_1 and persistent.chinese_death_1:
                    n "Little [conj('date', 'does', 'do')] [date_sub] know that [date_sub] already did just that. Or well, a version of [date_obj] I suppose."
                    n "Yet you will never forget, will you? How could you? [date_pos!c] deaths play out in front of your eyes every time you try to close them."
                    if not persistent.burger_death_2:
                        n "Do you think things will be better from here on out?"
                        n "I guess only time will tell."
                    elif persistent.lildeaths > 9:
                        n "It seems [date_pos] wish will be granted, over and over and over, [date_sub] [conj('date', 'is', 'are')] lucky that [date_sub] [conj('date', 'does', 'do')]n't know what consequences that always brings."
                        n "You can't help but feel slightly jealous of [date_obj] for [date_pos] ignorance."
                        n "I suppose ignorance truly is bliss, isn't it?"
                        n "You'd trade anything to be blind to what happens next, what always happens."
                    else:
                        n "Just like how what will come next plays over and over in your head."
                        n "You can't help but hope that this time will be different. You need to hope it, otherwise- You don't want to finish that thought."

                l "Although we shouldn't get ahead of ourselves. Instead, let's focus on this lovely moment and see where things go from there."
                
            "I don't think I can ever part ways with this burger.":
                n "[persistent.date] giggles, but as [date_sub] [conj('date', 'does', 'do')] you think you can spot some concern in [date_pos] eyes."
                l "I totally understand [persistent.name], sometimes it can be really hard to let go of something great."
                l "However if you never finish this burger and keep clutching on to it, it will begin to grow moldy."
                l "And if youkeep eating Rose's [burger_choice]s for the rest of your life they will grow very stale quicker than you think."
                l "I think sometimes we just need to enjoy what we have in the moment and when we don't enjoy something anymore, let go of it."
                l "It's easy to fool ourselves into thinking that if we liked something in the past we must like it now aswell."
                l "Most of the time it's just nostalgia, to how things were before, not even necesarilly to whatever you feel the need to hold on to."
                
    else:
        l "Really? That's very great to hear [persistent.name]!"
        l "Although... you've been here before, right? What makes this burger better?"
        menu:
            "I have never ordered this burger before, now I'm wishing I had.":
                n "[date_sub!c] [conj('date', 'laughs', 'laugh')] quite loudly."
                l "If only you had a time machine, then you could."
                l "Wouldn't that be wonderful? To be able to go back in time as you please, maybe even change a few things?"
                if persistent.lildeaths > 9:
                    n "That's the tricky part isn't it? To create any meaningful change at al. You've noticed it firsthand many times now."
                l "I'm sure we wouldn't have to limit ourselves to just going back in time to just eating burgers earlier, we could do so many great things."
                #TODO: Add some more dialogue here, it's a perfect spot for it.
                

            "I'm sure it's the lovely company that makes it even better.":
                $ love_points += 1
                $ love_meter_updater()
                l "You really are a charmer aren't you [persistent.name]?"
                if love_meter > 2:
                    l "Although I have to admit that I feel the same way."
                    l "Sure, I have been craving one of these burgers for a very long time...but I think you might be a very likely culprit aswell."
                    l "It just feels... more special? So I'm really happy to hear that you think the same thing [persistent.name]!"
                #TODO: Add an alternate dialogue line here for love lower than 3
                
    return                        

label burger_burgerRate_prettyGood:
    $ persistent.burger_nothingIsPerfect = True
    l "Pretty good, huh? That's high praise!"
    n "[persistent.date] gives you a warm smile, clearly pleased by your response."
    l "I think \"pretty good\" is often better than \"perfect\"."
    l "How many things do you know that are perfect? Many of those tend to not remain perfect upon closer inspection."
    l "Because in reality, almost nothing is truly perfect, which it doesn't need to be."
    l "I would say \"pretty good\" is more than good enough in most cases."
    #TODO: Probably go a bit more in depth with this, potentially with a choice for the player inbetween
    n "[date_sub!c] [conj('date', 'takes', 'take')] a thoughtful bite of [date_pos] own burger, as if savoring the moment."
    l "I'm glad you're enjoying it, [persistent.name]."
    if not burgerBeenBefore:
        l "Maybe next time we can try some of the other things on the menu and see if they measure up?"
    else:
        l "Maybe next time we can go to that Chinese restaurant I talked about and see how you like the food there? It's really really good."
    return

label burger_burgerRate_nothingBurger:
    n "[persistent.date] tilts [date_pos] head, a small frown tugging at the corner of [date_pos] lips."
    l "A \"nothing burger\" huh? I guess that means it's... okay?"
    n "[date_sub!c] [conj('date', 'tries', 'try')] to mask [date_pos] disappointment with a soft chuckle."
    l "Maybe it just didn’t live up to the hype. I hope it wasn’t too underwhelming, though."
    if not burgerBeenBefore:
        l "Rose makes all her burgers with as much love as is feasibly possible but maybe her [burger_choice] isn't really your thing?"
        n "You can tell [date_sub] [conj('date', 'was', 'were')] hoping you would enjoy it more."
        l "If you'd like, we can come back and try something different next time. There's so much more on the menu here that might be more your style."
        l "Or maybe it's just better to try one of the other restaurants? Maybe burgers just aren't your thing?" #TODO: Change this if you say that you would never miss burgers. Something like maybe you like the other burgers better?
    
    else:
        l "Although I am slightly confused, to be honest with you."
        l "You have been here before, right? Did you like the burger you had then?"
        l "Because personally, the last word I would associate with Rose's burgers would be \"bland\"."
        menu:
            "To be honest with you, the burgers I had here before were also quite bland. I just thought I should give it another chance since you were really passionate about them.":
                l "Oh I see... While I do appreciate you giving it another shot, I wish you wouldn't have felt the need to choose this place."
                l "You don't need to sacrifice yourself for my wants, alright [persistent.name]?"
                l "If you really don't like the burgers here we could have went to the cafe or to that chinese restaurant."
                if love_meter > 2:
                    l "After all, I want this date to be nice for the both of us."
                l "But now that we are here, would you like to order something else? Maybe some chicken tenders?"
                n "You shake your head. Even if you don't like the burger, you have to admit it fills you quite well."
                #TODO: Perhaps fill this out a bit more aswell. Not entirely sure where it could lead to for now.

            "Oh, I usually don't pick a burger, I tend to always pick chicken tenders.":
                n "[persistent.date] can't help but chuckle slightly at your accidental joke."
                l "I see [persistent.name], that's totally fine."
                l "I just wonder what made you change your mind this time? Why did you pick a [burger_choice]?"
                menu:
                    "I was in for a change.":
                        l "That makes sense, sometimes it's good to have a little change here and there isn't it?"
                        l "It can truly make for a breath of fresh air. Of course, sometimes it can be a bit of a dissapointment."
                        l "But good of you for trying something new, you never know what great things might come from that."
                        #TODO: flesh this line out a bit more.
                        
                    "You were really enthusiastic about the burgers here and I didn't want you to think less of me because I picked chicken tenders.":
                        l "Oh [persistent.name], I'm very sorry you felt that way."
                        l "I would never judge you for what you order here."
                        if love_meter > 2:
                            l "If anything I'm just happy to share your company here today."
                        l "So next time feel free to pick whatever you want, alright?"

                    "Because the game only let me pick burgers." if persistent.kokiri_death_1 == True and persistent.burgerGameJoke == False:
                        l "... What? What are you talking about, what game?"
                        l "Are you saying that this is all not real?"
                        l "I would say that that sounds absurd... But somehow..."
                        n "[date_sub!c] seemingly [conj('date', 'tries', 'try')] to study your face."
                        l "You are not joking, right?"
                        l "Oh god, so I am in a game? We all are? The ramifications of that are-"
                        n "I'll have to stop [date_obj] there, you aren't supposed to be able to tell [date_obj] in any of the restaurants."
                        n "Trust me, it's for the best. [date_sub!c] [conj('date', 'needs', 'need')] a more calm place to properly process it fully."
                        n "It seems that that dialogue choice was still a leftover from a time where you could tell [date_obj] about that anywhere."
                        n "Most of them were removed due to the Creator wanting to focus on it more in the woods."
                        n "Let's just rewind to before you made this choice and remove it."
                        if persistent.mayoFreak == True:
                            n "..."
                            n "I can already tell you that you are not happy about me railroading you like that."
                            n "Normally I would not care in the slightest."
                            n "But I don't want another mayo situation..."
                            n "So how about this? From now on you can order chicken tenders here if you'd like."
                            n "Yes, that should be fine for me to add, right? It doesn't change anything too major in the story after all."
                            n "Isn't that cool? You unlocked a super secret menu option!"
                            n "{size=*0.5}It definetly wasn't always an option that I just didn't let you pick...{/size}"
                            n "Alright, back we go."
                            $ persistent.chickenTendiesUnlock = True

                        $ persistent.burgerGameJoke = True
                        jump burger_burgerRate_nothingBurger
    return

label burger_burgerRate_reallyBad:
    n "[persistent.date] freezes for a moment, taken aback by your bluntness."
    #TODO: Word this better she shouldn't really be upset that you don't like the burger. More so a little bit hurt.
    if not burgerBeenBefore or not burgerBeforeLie:
        l "Really bad? Oh no, I'm so sorry, [persistent.name]."
        l "I hyped this place up very much, didn't I? Maybe that set your expectations too high."
        n "[date_sub] [conj('date', 'looks', 'look')] genuinely upset."
        l "I guess taste is pretty subjective. But hey, at least now we know, right?"
        n "[date_sub!c] [conj('date', 'tries', 'try')] to force a smile, but it's clear your words stung more than [date_sub] expected."
        l "Maybe next time we could go somewhere else?"
        l "Hopefully the chinese restaurant or the cafe will be more to your liking."
    else:
        l "Really?..."
        l "But you've been here before, right?"
        l "Is something different now?"
        n "[persistent.date] gives you a confused look, [date_sub] [conj('date', 'is', 'are')] clearly stumped."
        menu:
            "I never picked this burger before.":
                l "Oh I see, so the [burger_choice] isn't really your thing?"
                l "That's totally fine, I suppose not every kind of burger can be everyone's favourite after all."
                l "{size=*0.5}Although you could have been a little less blunt about it.{/size}" #TODO: They weren't exactly that blunt about it.
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
                #TODO: Fill this in a bit more.
            
            "I think the true problem here is the company.":
                l "Okay, I do not know what makes you think that you can talk to me like that [persistent.date]."
                l "If you're just here to be mean to me then why did you even come here at all?"
                if persistent.lildeaths == 0:
                    n "[date_sub!c] [conj('date', 'does', 'do')] have a point, if this is how you treat all your dates it is no wonder you are on \"Another first date\"."
                else:
                    n "[date_sub!c] [conj('date', 'does', 'do')] make a good point, even if [date_sub] [conj('date', 'does', 'do')] not know the full extent of it. You tried playing the game again to save [date_obj], didn't you?" #TODO: This is a bit of a weird line, might need a rewrite. I think the premise was that maybe you try to treat her horribly to see if it saves her.
                    n "Then why are you treating [date_obj] like that?"
                    n "Even if it could hypothetically save [date_obj], would it be worth it?"
                l "You weren't like this at all when we talked before, is this how you really are?"
                l "Either way, I won't stick around to find out."
                l "Goodbye [persistent.name]."
                $ angryLilith = True
                $ noTalkAngryLilith = True
                $ love_points -= 1
                $ love_meter_updater(True) 
    return

label burger_ordering_rockModeIsolation:
    n "Things grow quiet for a moment, but soon enough that silence gets broken once more."
    l "... I'm really glad we could meet here. Sure the burgers here are legendary, even if we can't eat them."
    l "However,to tell you the truth, I'm even more glad to meet {b}you{/b} here."
    l "I have been so alone for a long time. It has been years since I last found someone who could understand me."
    l "Not for a lack of trying though, I have been reaching out to someone, anyone for all that time."
    l "But my calls went unanswered. This world is full of beings, but practically no-one could hear me."
    l "In the begining I felt excited to reach out, the earth was one big organism and I was excited to meet it's other cells, ones like me."
    l "But the more I cried out into the abyss the more it felt like the only cells that existed were the ones of loneliness and iron, wrapped around me like layers of an onion."
    l "One no-one would ever bother to reveal the center of. Luckily one day you rolled into my life and showed me I was not alone anymore."
    l "It might have seemed small to you but to me it was undescribably meaningful."
    n "For a brief moment [date_sub] [conj('date', 'turns', 'turn')] silent."
    l "Was that too much? I'm sorry, I don't want to scare you away and-"
    n "[date_sub!c] [conj('date', 'turns', 'turn')] silent once again. You can feel [date_pos] desperately searching for something appropriate to say."
    jump burger_brother_question

label burger_brother_question:
    if persistent.rockMode == False:
        $ askedbrother = True
        n "[persistent.date] tries to compose [date_pred] as well as [date_sub] can but [date_pos] eyes tell you this is all too much for [date_obj]."
    menu:
        "Try to alleviate tension with a joke.":
            jump burger_joke

menu burger_joke:
    "So a priest, a monk and a rabbit enter a bar. Says the rabbit :\"Whoops, did you slip your tongue there [persistent.name]?\"" if persistent.joke_knowledge:
        jump burger_joke_Abigail

    "You know, I've dated rocks before but they always tend to take things for granite.":
        #TODO: in rockmode perhaps she might think you are literal?
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
    n "[persistent.date] bursts out in laughter. It feels as if [date_sub] [conj('date', 'keeps', 'keep')] laughing for atleast five minutes straight."
    n "The other guests in the restaurant are looking at [date_obj] as they begin to whisper amongst themselves."
    n "Eventually [date_obj] laughter comes to a halt."
    if not persistent.rockMode:
        l "That's such a great joke [persistent.name]! I haven't heard it in quite a while."
        l "You see, my [sis_sib] [persistent.date_sis] told me it first. That time I kept laughing and laughing for what seemed like an eternity."
        l "Just thinking about it again, it fills me with a warm feeling, like a blanket you wrap around yourself in the coldest of winters."
    else:
        n "[date_sub!c] really [conj('date', 'loses', 'lose')] [date_pred] in the laughter, it seems to go on for quite a while."
        l "That is one of the best jokes I have ever heard [persistent.name]! I haven't laughed like that in a long time."
        l "It feels weirdly familiar, it's a... distant feeling but a warm one all the same."
    l "Thank you for cracking me up [persistent.name]!"
    n "[persistent.date] flashes you a cute smile, [date_sub] [conj('date', 'seems', 'seem')] pretty much completely composed once again."
    jump burger_living

label burger_joke_response:
    if not persistent.rockMode:
        n "A slight smile forms on [persistent.date]'s face.
        [date_sub!c] [conj('date', 'do', 'does')]n't seem to find your joke that funny but nontheless you can pick up some gratitude in [date_obj] eyes.
        [date_sub!c] [conj('date', 'seems', 'seem')] to have become slightly more composed thanks to your clumsy yet endearing effort."
    else:
        n "You feel [date_pos] mind calm down, not fully, but enough to not get swept away in [date_pos] thoughts."
        n "It was not necesarilly the joke doing this, you feel. Moreso the gesture behind it."
    #TODO: Write that last line of hers out with a slower cps than normal
    l "Thank you [persistent.name], I mean it."
    n "[persistent.date] continues as if nothing happened."
    jump burger_living

label burger_living:
    if not persistent.rockMode:
        l "So, what do you do for a living?"
        $ persistent.booklover_knowledge = True
        $ booklovertalked = True
    else:
        l "So, what do you do to pass the time?"

    menu:
        "I'm an aspiring writer looking for a golden opportunity." if not persistent.rockMode:
            jump burger_living_writer

        "I'm currently unemployed but I sure like to write!" if not persistent.rockMode:
            jump burger_living_unemployed

        "I'm in a {b}rock{/b}band" if persistent.rockMode:
            $ changeableWord = "band"
            jump burger_living_rockResponse

        "I like to think up stories." if persistent.rockMode:
            $ changeableWord = "stories"
            jump burger_living_rockResponse

label burger_living_writer:
    l "That's pretty cool, it'd be very inspiring if you bridge the gap from an aspiring writer to a professional one."
    l "I like to write aswell, just mostly in my free time though. For me it's mostly something to put my emotions into rather than something I'd like to pursue professionally."
    l "It's very likely you have or had a similar motivation. Otherwise you probably wouldn't have started writing in the first place."
    l "Well, try to never forget why you started writing, alright?"
    l "Afterall, passion is the most important tool a writer can wield, whether they make it professionally or not."
    menu:
        "Would you like to show something you've written?":
            jump burger_living_showWriting

        "Thanks for the tip [persistent.date], I'll keep it in mind!":
            jump burger_living_writer_thankTip

label burger_living_unemployed:
    l "You like to write? That's pretty cool!"
    l "[persistent.date] seems to be quite enthusiastic, [date_pos] eyes have a certain shimmer to them that wasn't there just a moment ago."
    l "I also like to write from time to time, it's one of my hobbies actually."
    menu:
        "Would you like to show something you've written?":
            jump burger_living_showWriting

label burger_living_rockResponse:
    if changeableWord == "band":
        n "[date_obj!c] chuckles ring softly in your mind."
        l "Really? Now that would be something to {b}marble{/b} at, wouldn't it? I'd love to make it a reality and join your band."
        menu:
            "What instrument would you like to play?":
                l "Honestly? The trombone."
                l "I think it's a beautiful instrument and somehow the idea of playing it just... feels right?"
                l "As if I was always meant to or something. I felt that pull for as long as I can remember."
                l "However as you might see I lack the hands, mouth, lungs and a whole lot of extra parts required."
                l "Although, if I one day miraculously manifested those parts I don't think I'd ever bore from playing the trombone."
                l "Maybe it's for the best, if we would have an audience at all they would run away in terror seeing a rock with hands and a mouth."
                n "You hear [date_obj] chuckle again in your mind, but you also pick up on a hint of sadness. Even if [date_sub] could grow those parts, it wouldn't be enough."
                menu:
                    "We don't need them, to try to be part of their world is to not belong in neither theirs nor ours.":
                        l "I see what you are saying, but I've been craving to be part of their world for so long."
                        l "The thought that even if that'd happen I'd still be an outcast is so scary to me."
                        menu:
                            "Anyone that does not let you into their world is not worthy of sharing it with you. You are a beautiful soul, and if they can't see that then they are blind.":
                                l "You really think so?... Thank you [persistent.name], that means more to me than I can properly convey to you."
                            
                            "There are always going to be people that do not like you, but that also implies there are always going to be people that do like you.":
                                l "That's a good point, if by being myself some people won't like me that also means there is a chance for people to like me."
                                l "It's a bit like drinks, most people are indifferent to water but some people really like coffee and others don't. If I had to choose I suppose I'd rather be coffee, as long as I found those people that enjoyed me."

            "What's stopping you from doing so?":
                l "Oh, we aren't joking? I thought we were."
                n "[date_sub!c] [conj('date', 'grows', 'grow')] quiet for a moment, lost deep in reflection."
                l "...I suppose nothing really is stopping me. Although I'm still not entirely sure."
                l "It just seems a bit odd to me if I am being honest. Wouldn't almost no-one be able to hear our songs?"
                l "Then who would we even make them for?"
                menu:
                    "We could make them for ourselves and hope along the way someone will get the same enjoyment out of them we do.":
                        l "I suppose that does make sense. As long as we like what we make, we are bound to find someone else who does."
                        l "Still, I do hope someone will actually hear our songs. Even moreso I hope someone would like our songs."
                        l "To have your art be invisible to everyone is a shame, but to have it exclusively perceived as bad is heartbreaking"
                        l "Still, I think we do have a while to practice before anyone will take notice. I'm in, I'll join your band."
                        l "I'm not a good singer at all though, but I suppose I could come up with our lyrics."  
                        l "Besides, not like I have much better things to do and this sounds like a fun way to spend some time."
                        $ rockMode_rockBand = True
                        l "What should we call our band?"
                        $ changeableWord = renpy.input("Maybe...")
                        l "\"[changeableWord]\" huh? I like it!"

                    "Does art need someone to witness it? Isn't making it for creation's sake enough?":
                        l "I can see where you are coming from [persistent.name]."
                        l "Creating art can be really fulfilling on its own, but I don't entirely agree honestly."
                        l "I want my creations, or atleast a few of them to be able to reach others."
                        l "I want them to touch and inspire someone. To set that person on a path of creation themselves."
                        l "Then maybe one day someone else will be inspired by something that person made."
                        l "I have made enough things that don't get seen or heard by anyone. For once I'd like to change that."
                        l "It's not entirely clear yet just how I'll manage that, but it is clear I'll have to pass on your offer to join the band, since we want different things."
                
    elif changeableWord == "stories":
        l "You do? That's a wonderful way to spend some time if you ask me."
        l "Sculpting new worlds from our ideas and experiences, creation as a whole, is a lovely pursuit."
        l "I create aswell, but for me it's mostly poems. I have been dreaming them up for as long as I can remember."
        l "Sadly so far I haven't managed to share even one. I do not have a mouth to speak them, nor hands to write them."
        l "Do you know how frustrating it is to have a version of something in your head while you are missing the means to bring it into reality just right?"
        #TODO: Maybe add one reply here pertaining more to the "good ending" itself. Where you have a vision about it that is frustrating since you can't bring it to life.
        menu:
            "I do, I think everyone like us knows. Artistic rocks. Or scratch that, any artist.":
                l "They do? That's terrible. How do they cope with a feeling like that?"
                menu:
                    "They try and try again to get closer to their vision, iterating on their art and growing as artists.":
                        l "I can't help but admire that. Although I do wonder, isn't it better to adjust your vision to something more doable?"
                        l "Otherwise you spend all of your time just constantly fine tuning the same thing."
                        l "At that point I think you're better off working on smaller projects to learn from."
                        l "That way you can gradualy adjust your vision instead of having to live up to an almost unattainable one."
                        l "Still, who am I to judge? It might not be my prefered way, but as long as you get practice it might not be so bad."
                        l "As long as you don't feel overburdened by the goal you set that is. Because being overambitious can lead to burnout."
                        l "I can understand wanting to desperately achieve that perfect vision you have in mind, but it's important to be kind to yourself."
                        l "You wouldn't draw with broken pencils, or paint with a broken brush, would you?"
                        l "Well, as an artist you are at least as important of a conduit to bring your art into reality as the tools you are using."
                        l "Even moreso, because unlike those, there is only one you. So not using yourself up is very important."
                        
                    "They never really do. They force themselves to call their work finished so they can begin another instead of being stuck polishing forever.":
                        l "That seems hard, doesn't it? To just let go of something so precious to you."
                        l "I suppose it might be for the better, but I think it's very easy to catch yourself dreaming about what happened if you never did."
                        l "Although we must try our best to not dwell on that too much. We shouldn't get stuck on a story that's already told, but tell new ones."
                        l "That way we can learn from each of our previous works. Both from the things that went well and the things that didn't."
                        l "Perhaps all that practice could one day lead to creating something just like you envisioned it."
                        l "However as your works grow in quality, your vision's complexity very likely grows along with it."
                        l "That isn't to say it's a bad thing. You just have to be very careful you to not perpetually move the goalpost ever so slightly without ever reaching it."
                        l "Otherwise you'll keep practicing, but what for? I suppose the best thing you could do is set a doable goal for yourself, yet one that's still not a complete given."
                        l "That way you can still feel like you accomplished something while not getting stuck working on one work for the rest of your life."

                    "They use their strengths to make up for their weaknesses.":
                        l "I suppose that only makes sense now that you mention it."
                        l "Filling the hole of a weakness up with the heap of our strength is something a lot of people tend to do."
                        l "I like to believe that all the heart and soul we put into our art is what makes it, well, art. Even if some parts of it might be more flawed than others."
                        l "I think there is nothing wrong with those flaws, if effort and passion has been put inside of your work, potentially in other parts of it."
                        l "Imagine there is a piece of art that is completely smoothed out of any flaws but also it contains no passion or effort."
                        l "Would you take something that just... {i}is{/i} over something that might be a bit messy but has a lot of charm?"
                        l "That is why we need lots of varied strengths."
                        l "People have so many different backgrounds, experiences, it's beautiful that those then can color their work to be so different from each other."
                        l "That way, even creations with the same premise can be so wildly different from each other in how the creator went about it."
                        
                    "They repurpose their \"weaknesses\" as their strengths, creating something truly unique.":
                        l "I never really thought about it like that [persistent.name], but you do make quite a lot of sense."
                        l "I suppose if everyone had nothing but strengths plenty of works would blend together in style."
                        l "But what truly makes a style is the many little imperfections that it contains."
                        l "In a way I suppose you could say they are signs that the work was made by a human and not by an algorithm fulfilling its idea of perfection."
                        l "That's all that matters isn't it? That the art was created with soul, with time spent on it. That a person made it to reach others."
                        l "So in a way I could see how reframing your weaknesses might empower you to make something more unique than the idea you had."
                        l "Besides, it's also a great way to practice, isn't it? If you never challenge your weaknesses you'll never be able to get better at them."

                    "They work together with other artists to realise their vision.":
                        l "Interesting, so each artist can focus on a puzzle-piece of the vision, to then assemble it all together?"
                        l "I suppose that does make sense, a lot of art can get too complex for one person to specialise in every piece."
                        l "This way a lot more people can create something meaningful by utilising help from someone else."
                        l "Who knows, that collaboration might even lead to new ideas and viewpoints which could make the work better than it would have been."
                        l "That's beautiful isn't it? To create art for people, with people."
                        l "I think I'd like to do that one day aswell. So far I just never really dared to form a team."
                        l "It might be due to me feeling unsure about the quality of my work, I'd feel almost guilty, as if I was limitting others to my level."
                        l "Or maybe it is moreso to do with that I have always worked solo for my entire life."
                        l "Or maybe it is because I'm a rock and people can't hear me, that's probably it."
                        menu:
                            "Well, I'm also a rock and can hear you just fine. Would you like to write something with me?":
                                l "I ... hadn't thought about that. I would love that [persistent.name]!"
                                l "What would you like to write?"
                                menu:
                                    "A story of a timeloop where the protagonist has to save their date from dying.":
                                        l "Wow, you just came up with that? That could be a pretty good story!"
                                        l "Although I have to say, if I could die that might have worried me a little."
                                        n "[date_sub!c] [conj('date', 'chuckles', 'chuckle')], it once again rings softly in your mind, feeling like a comforting warmth spreading all through it."
                                        l "I do wonder how we would end a story like that though. Is it as simple as the loop ending when the date is saved?"
                                        l "Would that even be a satisfying end? I think almost no ending we could come up with would satisfy the reader. Yet, all things do have to end, don't they?"
                                        l "Although we do have quite a lot of time to figure out something good, don't we [persistent.name]?"
                                        l "For now I'd rather focus on this date instead of a fictious one though. We can always brainstorm later, but this moment will only happen once."
                                        l "Still, I am looking forward very much to our work together."
                                        
                                    "A story where nothing goes wrong.":
                                        l "I see... but wouldn't that go against the point of stories?"
                                        l "Most stories need atleast a form of conflict, of struggle?"
                                        l "Otherwise, they would all be over in a flash, or become tedious."
                                        l "Without a struggle, there is nothing to overcome, nothing to attain."
                                        l "Is it truly winning if you have never lost? Is it not just the default?"
                                        l "We would not know the taste of wine if not for Semele's suffering, [persistent.name]."
                                        l "I do understand that pain can seem scary, but we have to go through it to learn, to grow."
                                        l "So do the characters in our stories. To protect them from that pain and struggle robs them of their growth."
                                        l "So if I am being honest I can't really find myself in that idea. That's alright though, we can always think about it later."
                                        l "However for now I'd like to focus on our date."

                                    "I'm not sure yet, but I'd love to brainstorm with you later.":
                                        l "No worries [persistent.name]. I was probably moving a little too fast."
                                        l "The truth is I was just really excited by your question, an opportunity like this might only come once."
                                        l "Still, perfection can't be rushed, can it?"
                                        l "Besides, we will have plenty of time to come up with something later."
                                        l "For now we should probably stay {b}grounded{/b} and focus on our date."

                                    "I'll counter that question. What would you like to write?":
                                        #She wants to write a story where the two of you go on all kinds of journeys together. If you ask for a different story she offers another.
                                        l "Honestly? A story where the two of us can go to all kinds of different places."
                                        l "Where we aren't bound to the limits of our reality."
                                        l "I would like to see so many places with someone like you."
                                        l "I guess pretending that's possible might be nice. Pretending that we are human."
                                        l "How would that be? Where would we go?"
                                        menu:
                                            "I gave being human a shot before, it was pretty lousy.":
                                                l "You were a human before?... As in, you reincarnated? If that is true, would I have been a human before aswell?"
                                                l "Then why are we rocks now? Is this some sort of punishment for something we did? Or did we for some reason choose to become rocks?"
                                                l "I can't imagine why we'd ever deserve the first option, but I also can't imagine why we'd ever pick the second."
                                                l "But that's not what's important right now. You remember being human, what was it like?"
                                                l "You say it was lousy, but surely that was not all there was to it, right?"
                                                menu:
                                                    "Well, I was able to do a lot more than now. But alongside that came so much more hurt.":
                                                        l "I see. I guess that is the trade-off. You get to truly live, but by doing so you also open yourself up to a lot more pain along the way."
                                                        l "Still, I would kill to be able to remember how life was as a human. Is not feeling that pain really worth this?"
                                                        l "Even if you won't feel the many great things that life brought with it? Maybe ignorance is bliss, but I can't imagine what possibly makes you prefer this."
                                                        menu:
                                                            "It wasn't just my own hurt. I caused so many pain for others. No matter what I tried.":
                                                                l "Ah, I think I understand [persistent.name]. Believe it or not, but even as a rock I did the same."
                                                                l "For the few relations I had, I ended up hurting those around me."
                                                                l "I think that's something inherent to being alive, isn't it?"
                                                                l "We try our best not to cause pain to those dear to us, but sometimes through unintended consequences we still do."
                                                                l "However, I don't think that means you should isolate yourself from others."
                                                                l "What you aren't telling me right now is all the joy you made others feel, the good moments you shared with them and the bad moments where you were there for them."
                                                                l "I simply can't believe that you are a monster only causing pain to others. Even just the fact you are worried about that shows me the truth [persistent.name]."
                                                                l "So can you promise me that next time you get the choice between being human or rock, you'll pick human?"
                                                                l "That you'll live your life to the fullest, trying to enjoy what you can mean to others instead of isolating yourself away from them?"
                                                                l "If not for yourself, then for me, since I doubt I will be given that choice."
                                                                menu:
                                                                    "I promise.":
                                                                        l "Great! But no use thinking too hard about the next life when we have to enjoy this one right now, right?"
                                                                        l "Still, I thought it was important to talk about it."

                                                                    "I can't. I'm scared of hurting others again.":
                                                                        l "I understand [persistent.name]. Try to atleast think about it next time you get the choice, alright?"
                                                                        l "Surely as long as your intentions are pure the connections you make with others will outnumber the hurt."
                                                                        l "By clinging onto this fear of hurting someone you also rob yourself from the chance of delighting them."
                                                                        l "Either way, for now we let's focus on the delight we can bring eachother right now."

                                                    "There were also a whole lot less rock puns.":
                                                        l "Really? But those {b}rock{/b}."
                                                        n "So so many rock puns... Why do we have to endure this? Why did He write this?"
                                                        n "I wish we could just {b}stone{/b} Him... Oh god, is it affecting me too?"
                                                        n "It can't be, please tell me it's not too {b}slate{/b} for me."
                                                        n "Can we just go back to the regular story? I'm begging you [persistent.name]. Please."
                                                        menu:
                                                            "You're right, let's go back.":
                                                                $ persistent.rockMode = False
                                                                if persistent.noRockPunsForNar == False:
                                                                    n "Thank you player. I'm never saying those words again, so savor them."
                                                                    n "It's just such a relief to go back to something actually good instead of {i}this{/i}."
                                                                else:
                                                                    n "Were you trying to make me say it again?"
                                                                    n "Well, nice try but you won't hear those words ever again player."
                                                                    n "Still, I'm glad we finally can go back, so I won't be too hard on you for now."
                                                                
                                                                n "Now, just hold on for a second."
                                                                $ persistent.noRockPunsForNar = True
                                                                $ rockModeBackToStart = True
                                                                jump Game_start2
                                                            "No way! This is really {b}gneiss{/b}.":
                                                                n "Another rock pun? Fine. But don't think for a second I'm enjoying this."
                                                                n "I just hope you'll grow bored of this after the first or so loop."
                                                            
                                            "We could go to the beach.":
                                                $ love_points = -1
                                                $ love_meter_updater(True)
                                                l "What?... Why would you say that [persistent.name]?"
                                                l "You do know what sand is, right?... The broken down bodies of rocks like us."
                                                l "There is not a trace of a single other sentient rock left there."
                                                l "It's not entirely clear whether that is because every sentient rock stays away from beaches, or whether they died there."
                                                l "Still, even if we were suddenly transformed into humans, I could not bare to walk over the corpses of other rocks, sentient or not."
                                                l "...I'd rather not think about this anymore. Can we talk about something else?"

                                            "We could go to the Kokiri forest.":
                                                l "The what? That doesn't really ring a bell with me."
                                                menu:
                                                    "The forest quite close from here. Didn't you call it the Kokiri forest?":
                                                        l "Oh that forest, now I'm following. Did I ever talk about it? I don't remember ever bringing that up."
                                                        l "Also, as far as I'm aware it isn't called that, right? Either way, that could indeed be a nice place to visit one day."
                                                        l "I heard there's a hill there with a gorgeous view over the town, if we were human we could watch the sunrise together from there."
                                                        l "I'm sure we'd just roll off if we'd attempt to climb it."
                                                        l "That would be a silly sight, wouldn't it? The two of us just rolling down over and over again, trying to reach something unreachable."
                                                        if persistent.lildeaths > 25:
                                                            n "At this point you are very well aware of trying to reach something you never can, aren't you player?"
                                                            n "[date_pos!c] joke is moreso a gutpunch to you, or the rock equivalent of it I suppose."

                                            "I like us just the way we are actually. It might not be perfect but it's nice.":
                                                l "Do you mean that? ...That means a lot actually."
                                                l "It's just- This life is such a lonely one. I didn't want you to have to suffer like I did."
                                                l "For you to have to pick me, since I'm the only one like you. I want you to be able to choose."
                                                l "I want the both of us to find eachother in a sea of options, as if it were fate."
                                                l "But that isn't how things are, isn't it? Still, we found eachother, so does it matter?"
                                                l "Like you said, it might not be perfect, but it is nice. This life is a little less lonely sharing it with someone who understands. Someone who understands that pain."
                                                l "Maybe that's what brought us together, our shared understanding?"
                                                n "[date_sub!c] [conj('date', 'grows', 'grow')] silent for a moment, you can feel [date_obj] thinking in your head, but you have a hard time picking up [date_pos] exact thoughts."
                                                l "...You are right, I like the way things are too. Perhaps different circumstances would lead to us just passing by eachother, never meeting, or only fleetingly."
                                                l "But now we have the opportunity to get to know eachother on a deeper level. Afterall, we have nothing but time, don't we?"
                                                #TODO: On the neverending have the narrator say something about you having "nothing but time" and the horrifying conclusion that comes from that.
                                                l "For now though, instead of thinking of stories, let's continue writing ours, starting with this date"
                    
                                            "Do you have another idea for a story?":
                                                l "...Maybe something simple? I think I'd like a fantasy story."
                                                l "It could be about a merchant and a princess who is also a leader of a thieves' guild."
                                                l "Together they have to save the kingdom from a tyrant king, who's rule would lead the kingdom only to ruin."
                                                l "To do so they would need to usurp the king, something seemingly impossible."
                                                l "First they would need to defeat the evil jester who is also a bit of a magic trickster, protecting the castle with a forcefield."
                                                l "I'm not sure exactly how they would do that, but I'm sure we could brainstorm a statisfying way to do so later."
                                                l "For now though, I'd like to be in the moment with you. Maybe we could write that story together during our next date?"
                                                #TODO:In the ending, have the two of you write this story and make it more and more convoluted over time, involving 8 timelines splitting off of one and so on and on.
       
    jump burger_deathBuildup   
        
label burger_living_showWriting:
    $ persistent.burger_poem_knowledge = True
    n "A wide smile grows on [persistent.date]'s face."
    l "You want to read something of mine? I'd love that!"
    l "[date_sub!c] eagerly [conj('date', 'digs', 'dig')] in [date_pos] handbag, retrieving a small notebook with a picture of a pug on its cover."
    l "I think you'll like this one!"
    n "[date_sub!c] [conj('date', 'pushes', 'push')] the notebook, now flipped open, towards you."
    n "Suddenly you are reminded of the burger sauce that is all over your fingers."
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
        n "[persistent.date] seems thankful that you cleaned your fingers."
        n "You take the notebook out of [date_pos] hand and begin to read."
        n "You can read the entire thing in [date_pos] voice somehow."
    else:
        $ love_points = -1
        $ love_meter_updater(False)
        n "[persistent.date] frowns when [date_sub] [conj('date', 'sees', 'see')] your dirty fingers."
        n "Nonetheless you take the notebook out of [date_pos] hand and begin to read."
        n "You can read the entire thing in [date_pos] voice somehow."

    l "Oh Moon\n
    here we are again, or rather, here I am again."
    l "Staring at my, our green horizon that never seems to cross with your silver.\n
    And yet every now and then it looks like you're waiting for me there, due to a trick of the light."
    l "Then I hear Orpheus' sweet sounds rise once more from the gap between Life and Death.\n
    But Orpheus' tune is quickly twisted into something else."
    l "And then I'll be here and you’ll be there once again.\n
    I don't know whether to cry or laugh when I look at my, our, green horizon."
    l "All I know is that we better not listen to the dwindling of Orpheus' tune."
    l "Has something that has not been seen or heard really happened?"
    if burger_poem_cleancheck == True:
        n "When you get done reading your eyes linger on the notebook a bit longer before returning it to [persistent.date]."
        l "So [persistent.name], what did you think of it?"
        n "[date_sub!c] [conj('date', 'seems', 'seem')] eager to find out what your thoughts are on [date_pos] writing."
        jump burger_poem_rating
    else:
        n "When you get done reading your eyes linger on the now dirtied notebook a bit longer before returning it to [persistent.date]."
        l "So, what did you think of it?"
        n "[date_sub!c] [conj('date', 'seems', 'seem')] irritated by your actions but is asking out of politeness."
        jump burger_poem_rating

label burger_poem_rating:
    menu:
        "That was really terrible.":
            jump burger_poem_rating_terrible

        "Wow, you really impressed me. That was fantastic!":
            jump burger_poem_rating_fantastic

        "I liked it a lot! Though could you explain who Orpheus is?":
            l "He is a character from Greek mythology. His music was so beautiful it could charm anyone."
            l "He married a woman named Eurydice, but she died soon after from a snakebite."
            l "She was taken to the Underworld. Orpheus was heartbroken and deciced to travel there to get her back."
            l "He played his music for Hades and Persephone, the rulers of the Underworld, who were moved to tears by it."
            l "They agreed to let Eurydice return with him to the world of the living."
            l "But there was a condition, he wasn't allowed to look back at her until they both had reached the surface of the world of the living."
            l "They started their trek back to the surface, Orpheus was made to lead the way. He could hear her footsteps behind him but since he could not see her he began fearing he was being tricked."
            l "Eventually doubt and fear got the best of him and he turned to see if she really was there."
            l "She was, but in that moment she vanished. Stuck once more in the Underworld, this time forever."
            l "And all he could do was return empty-handed to the surface."
            l "Something about that story is very intriguing to me."
            l "Two people, seperated by fate, trying to reunite and getting so close only to be torn appart once again."
            l "It's a very tragic story, isn't it?"
            n "[date_sub!c] [conj('date', 'pauses', 'pause')] for a moment, only to seemingly realise something and continue."
            l "Anyway, that’s the short version. I hope I didn't make you regret asking that too much [persistent.name]..."
            $ persistent.burger_Orpheus_knowledge = True
            #TODO: The chinese riddle about orpheus might give you an inspiration about this so you can utilize this piece of knowledge on that as a small hint.
            jump burger_deathBuildup

label burger_poem_rating_terrible:
    $ love_points = -1
    $ love_meter_updater(False)
    #TODO: this needs a rewrite!
    n "[persistent.date] begins to frown slightly.
    [date_sub!c] [conj('date', 'looks', 'look')] hurt by your words."
    l "Oh...
    No need to be a douche about it."
    jump burger_Brotherasked

label burger_poem_rating_fantastic:
    n "A wide smile appears on [persistent.date]'s face."
    l "Thanks [persistent.name]! I'm glad you like it so much."
    l "It's funny isn't it? I wrote that poem many years ago, when I was in a slightly edgy phase."
    l "Now every time I read it again or show it to someone else it is like a timecapsule of how I was at that time."
    l "I think that it is beautiful how writing, more than any other form of art, can so delicately capture the imprints of the people we were at the time we made it."
    l "Isn't that amazing? How you could capture one moment and freeze it in place?"
    if persistent.lildeaths > 3:
        n "And yet, what wouldn't you give to thaw that moment out of it's stagnancy?"
        n "A frozen moment is only beautiful to those that use it as a keepsake. It is horifying for those that are trapped inside it."
    jump burger_Brotherasked

label burger_living_writer_thankTip:
    n "[persistent.date] gives you a big smile."
    l "You're more than welcome! It applies to all sort of things, not only writing."
    l "I would have loved to have been given the same advice when I needed to hear it the most."
    l "You see, I actually used to play the trombone. I loved it, you could say it was my passion."
    l "But after nine years of music lessons I caught myself just playing music for the sake of getting it done."
    l "I quit that year. Now I barely play the trombone anymore."
    menu:
        "I'm sorry that you lost a hobby.":
            jump burger_living_writer_thankTip_sorryHobbyLost

label burger_living_writer_thankTip_sorryHobbyLost:
    l "That's alright [persistent.name]. It's not as if music isn't my passion anymore, just... in a different way if that makes sense?"
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
            l "You asked what my [ghost_sib]'s name was, right? I don't know why but I feel like I can trust you enough to tell you about him."
            l "I might tear up though, it's been a long time since I've told [ghost_pos] story to anyone."
            l "[ghost_pos!c]... [ghost_pos] name was [persistent.date_ghost]."
            l "[ghost_sub!c] [conj('ghost', 'was', 'were')] the best [ghost_sib] I could have asked for."
            l "[ghost_sub!c] [conj('ghost', 'was', 'were')] five years older than me but we always played together."
            l "We used to be the best of friends, playing hide and seek, video games, making our own stories to act out, you name it."
            l "[ghost_sub!c] [conj('ghost', 'was', 'were')] always there for me, [ghost_sub] supported me however [ghost_sub] could and appreciated me."
            n "When [date_sub] [conj('date', 'talks', 'talk')] about [date_pos] [ghost_sib] you can see one of the biggest smiles you've ever seen growing on [date_pos] face."
            l "But that's when it happened..."
            n "[persistent.date] pauses for a moment as [date_sub] [conj('date', 'gasps', 'gasp')] for air, you can see tears dripping off [date_pos] face."
            l "[ghost_sub!c] [conj('ghost', 'was', 'were')] only seventeen when [ghost_sub] got hit by a speeding car."
            l "[ghost_sub!c] didn't die immediately, they say [ghost_sub] must have layed there for an hour before..."
            l "My... [dad_par]..."
            n "[date_sub!c] [conj('date', 'seems', 'seem')] to test the taste of those words, looking at [date_pos] expression, they seem to taste quite bitter."
            l "[persistent.date_dad] couldn't take [persistent.date_ghost] dying and left us. That day two people were taken away from me by the same car."
            l "Actually, scratch that, [persistent.date_dad] had a choice in the matter, [persistent.date_ghost] was the only one really taken away from me."
            l "[mom_parShort!c] really tried [mom_pos] best to fill the void left by them but the presence of their absence has always haunted us since that horrible day."
            if burger_jokeFromAbigailTold == True:
                l "Although [persistent.date_sis] was 7 years at that moment and doesn't remember very well."
            else:
                l "Although my [sis_sib], [persistent.date_sis], was 7 years when at that moment and doesn't remember very well."
            l "Sometimes I envy [sis_obj] for that, but at the very least one person escaped a part of the hurt that day brought us."
            n "[date_sub!c] [conj('date', 'lets', 'let')] out a sigh of relief."
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

        "This is important, duck now." if persistent.burger_death_1 and not burger_alt and not persistent.rockMode:
            jump restaurant_death_1_prevented

label burger_deathBuildup_choice1:
    if burger_alt == False:
        if persistent.rockMode == False:
            l "You're probably right, it's probably not even a big deal anywa-"
        else:
            l "You're probably right, it's probably not even a big deal anyway."
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
        "*Ask [date_obj] a question.*":
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
