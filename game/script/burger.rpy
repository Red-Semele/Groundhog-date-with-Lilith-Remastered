
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
                $ burgerFanatic = True
                jump burger_start_choice1

            "I wouldn't want to miss this for the world!":
                jump burger_start_choice2

            "Sorry, traffic was quite bad." if not persistent.rockMode:
                jump burger_start_choice3

            "Sorry, I think traffic was quite bad? It was pretty hard to tell underneath a shoe." if persistent.rockMode:
                jump burger_start_choice3

            "Hey glad to be here. Could we sit somewhere else though?" if persistent.burger_death_1 and not persistent.rockMode:
                $ burger_alt = True
                $ get_lilith_current_loop_memory()["burger_alt"] = True
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
            $ get_lilith_current_loop_memory()["beenBefore"] = "never"
            jump burger_beenBeforeXTimes

        "I actually didn't know that, I've never been here before. (Lie)" if persistent.burgerwent > 0:
            $ get_lilith_current_loop_memory()["beenBefore"] = "never"
            jump burger_beenBeforeXTimes

        "I knew that, I've been here a couple of times. (Lie)" if persistent.burgerwent < 2:
            $ get_lilith_current_loop_memory()["beenBefore"] = "true"
            $ get_lilith_current_loop_memory()["beenBeforeMultiple"] = True
            jump burger_beenBeforeXTimes

        "I knew, I've been here before, only once though." if persistent.burgerwent == 1:
            $ get_lilith_current_loop_memory()["beenBefore"] = "true"
            jump burger_beenBeforeXTimes

        "I'm well aware, I've been here exactly [persistent.burgerwent] times." if persistent.burgerwent > 1 and not persistent.rockMode:
            $ get_lilith_current_loop_memory()["beenBefore"] = "true"
            $ get_lilith_current_loop_memory()["beenBeforeMultiple"] = True
            n "It sounds a bit weird if you phrase it like that, doesn't it?"
            jump burger_beenBeforeXTimes

        "I knew, I've actually been here a couple of times." if persistent.burgerwent > 1:
            $ get_lilith_current_loop_memory()["beenBeforeMultiple"] = True
            $ get_lilith_current_loop_memory()["beenBefore"] = "true"
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
                $ get_lilith_current_loop_memory()["hypotheticalBurger"] = True

            jump burger_start_menu

label burger_beenBeforeXTimes: #TODO: Probably add some more choices like the once_greatTaste one. I feel like that'd add a lot more variety.
    $ burgerBeenBefore = get_lilith_current_loop_memory().get("beenBefore", "")

    if persistent.burgerwent == 0 or burgerBeenBefore == "never":
            l "I'm sure after today that will change. They have really great burgers like I said before."
            if love_meter >= 3:
                l "So something tells me you will come here often after this. Maybe... some of those times with me?"
            else:
                l "You might find yourself coming back more often than you'd have expected. The burgers might just be magic."
        
            

    elif persistent.burgerwent == 1:
        if persistent.rockMode:
            l "Oh, you've been here before? Is that why you wanted to come back here so much? I must admit, I can't blame you at all."
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
        $ get_lilith_current_loop_memory()["hypotheticalBurger"] = True
    jump burger_start_menu

label burger_beenBeforeXTimes_once_greatTaste:
    l "I see, in that case you have great taste!"
    $ get_lilith_current_loop_memory()["greatTaste"] = True
    n "[date_sub!c] [conj('date', 'lets', 'let')] out a hearty chuckle."
    menu:
        "Of course, afterall, I am here with you, aren't I?":
            $ love_points += 1
            $ record_attitude_event("tasteCompliment", True)
            $ love_meter_updater(False)
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
        $ get_lilith_current_loop_memory()["hypotheticalBurger"] = True
    jump burger_start_menu

label burger_start_menu:
    if not get_lilith_current_loop_memory().get("hypotheticalBurger", False):
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
            $ get_lilith_current_loop_memory()["onlyBurgers"] = True
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
                            $ lilithAliveEnding = True
                            $ ending_check = "food ending"
                            jump gameOver

label burger_ordering:
    if persistent.rockMode == False:
        if burger_choice == "juicy cheeseburger":
            if get_lilith_current_loop_memory().get("greatTaste", False):
                l "So you really do have great taste! I knew it!"
            else: 
                l "I can't say I'm surprised, great minds think alike after all, don't they?"
        else:
            l "That's a great choice [persistent.name]!"
        if get_lilith_current_loop_memory().get("beenBeforeMultiple", False) and love_meter >= 2:
            l "Do you usually pick the [burger_choice] when you come here?"
            menu:
                "Oh yeah, all the time honestly." if persistent.burgerwent > 0:
                    jump burger_orderingAllthetime
                
                "Oh yeah, all the time honestly. (Lie)" if persistent.burgerwent == 0:
                    jump burger_orderingAllthetime
                    label burger_orderingAllthetime:
                        if burger_choice == "juicy cheeseburger":
                            $ get_lilith_current_loop_memory()["repeatCheese"] = True
                            $ love_points += 1
                            $ record_attitude_event("commonTaste", True)
                            $ love_meter_updater(False)
                            n "[persistent.date]'s eyes light up like fireworks as [date_sub] almost [conj('date', 'bounces', 'bounce')] out of [date_pos] seat."
                            l "Really? No way! I also always go for the cheeseburger!"
                            l "It's just too irresistable to pass up on, isn't it?"
                            
                        else:
                            n "[persistent.date] gives you a playful wink."
                            l "You can't go wrong with the classics I suppose."
                            l "I'm honestly very much the same, I don't think I can ever muster up the strength to pick anything other than that cheeseburger."
                    
                "Actually, it's my first time.":
                    if burger_choice == "juicy cheeseburger":
                        l "Really? I totally convinced you to get one, didn't I?"
                        n "[persistent.date] lets out a playful laugh."
                        l "Don't worry [persistent.name], you won't regret it, I promise!"
                        l "Or maybe you will regret not being able to go back after you grow addicted to this one."
                    else:
                        l "Oh I see! I hope it'll be to your liking then."
                        l "Picking new things can be a bit scary sometimes as it's always a surprise."
                        l "Yet then again, if you like the other burgers here, there is a good chance you might like this one too!"
                        l "Rose really is incapable of making a bad burger as I'm sure you must have tasted by now."
            l "All this food talk is just making me hungrier and hungrier, let's go order something before I eat you."
            jump hungryBurgerTransition
        else:
            l "Let's go order, alright?"
            define move_out_left = MoveTransition(3.0, leave=offscreenleft, leave_time_warp=_warper.easeout)
            hide lilith talk_closed with move_out_left #move_out_left is a custom defined move transition since this is the only way to not have it hapen in 0.5 seconds
            if persistent.burgerwent == 0:
                n "You look around to search for a self-service screen like most fastfood places have however, you can't spot any."
                if get_lilith_current_loop_memory().get("beenBefore", "") == "true":
                    n "As you turn around to check if you maybe missed the screen you catch [persistent.date] giving you a confused look before she turns around and walks straight to the counter."
                    $ get_lilith_current_loop_memory()["beenBefore"] = "lie"
                else:
                    n "As you turn around to check if you maybe missed the screen you catch [persistent.date] flashing you an understanding smile as [date_obj] beckons you and walks straight to the counter."
                n "You decide to follow [date_obj]."

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
            jump burger_ordering_normal
        else:
            jump burger_ordering_nightmare
           
    else:
        jump burger_ordering_rockMode

label hungryBurgerTransition:
    if love_meter < 4:
        n "[date_sub!c] [conj('date', 'rushes', 'rush')] off so fast you actually lose track of [date_obj]."
        if persistent.burgerwent > 0:
            n "Luckily you already know where [date_sub] will be."
            n "You calmly make your way to the counter."  
        else: 
            n "You figure [date_sub] probably went to the nearest screen to order."
            n "Yet you spend a minute or so without managing to locate one."
            n "You are this close to questioning your own sanity when-" (multiple=2) #TODO: Have this somehow first type it's line and then trigger the second one
            if get_lilith_current_loop_memory().get("beenBefore", "") == "true":
                l "Heya [persistent.name], are you alright?" (multiple=2)
                n "You practically jump up in suprise."
                $ get_lilith_current_loop_memory()["beenBefore"] = "lie"
                n "[date_sub!c] [conj('date', 'gives', 'give')] you a strange look."
                l "I was just with Rose just now, are you coming?"
                n "You nod and follow [persistent.date]. Soon enough the both of you reach a counter."
                n "An old lady, who you presume is Rose, gives you a peculiar look before her face shifts into a warmer smile."
            else:
                l "Sorry [persistent.name], I forgot you don't know your way around here yet." (multiple=2)
                l "I guess I was so excited to order that I abandoned you for a moment."
                l "Come with me."
                n "[date_sub!c] [conj('date', 'beckons', 'beckon')] you. Thankful for the salvation you follow."
                n "[persistent.date] stops when she reaches a counter, behind it is an old lady who gives you a warm smile."
                jump burger_ordering_normal
    else:
        n "[date_sub!c] practically [conj('date', 'drags', 'drag')] you with [date_obj] as [date_sub] [conj('date', 'rushes', 'rush')] off."
        #Here she never finds if you lied about coming here before
        if persistent.burgerwent > 0:
            n "In a blink of an eye, you find yourself at the counter, where Rose has to hold back a laugh before she gives the both of you a warm smile."
        else:
            n "In the blink of an eye, you find yourself at a counter. An old lady seemingly has to hold back a laugh before she gives the both of you a warm smile."
        jump burger_ordering_normal

label burger_ordering_normal:
    r "Hey [persistent.date], glad to see you here once more!"
    r "I'm almost surprised to see you here, it's been quite a while hasn't it?"
    l "I'm so sorry. I really wanted to come back but after [persistent.date_ghost[:2]]-"
    r "Oh... I see. I'm sorry sweetie, I really hadn't thought before I ran my mouth."
    r "It's perfectly alright [persistent.date], I really didn't want this to come off as judgemental at all."
    r "In fact, I'm glad you're out and about again, you and-"
    if persistent.rosename_knowledge == True:
        n "Rose turns towards you."
    else:
        n "The old lady turns towards you."
    if love_meter >= 2:
        n "She flashes you a smile that seems to be filled with nothing but warmth and kindness."
    else:
        n "She gives you a somewhat odd look. She seems almost... disappointed?"
        n "Then she turns back to [persistent.date] and gives her a pitiful look."

    r "Who did you bring along for the ride?"
    if get_lilith_current_loop_memory().get("beenBefore", "") != "true" and get_lilith_current_loop_memory().get("beenBefore", "") != "lie":
        if love_meter >= 2:
            l "Oh right, you two haven't met. Rose, this is [persistent.name] and [persistent.name] this is Rose."
            $ persistent.rosename_knowledge = True
            $ roseName = "Rose"
            n "Rose gives you a sincere smile."
            r "Nice to meet you [persistent.name]."
        else:
            l "Oh right... This is [persistent.name]."
            r "I see..."
            jump burger_ordering_roseOrder
    else:
        l "Oh, do you not recognize [persistent.name] Rose?"
        r "No, their face is not ringing any bells I'm afraid, should I recognize them?"
        l "I suppose not necessarily, but with how good your memory is I thought you would remember them, they've eaten here before."
        if get_lilith_current_loop_memory().get("repeatCheese", False) and persistent.burgerwent > 1:
            l "Besides, they have the same impeccable taste as I do! Always picking the juicy cheeseburger."
            r "While there certainly is no doubting either of your great taste I must admit it's still not ringing any bells."
        else:
            r "Really? Huh... Still not ringing any bells I'm afraid."
        r "Might be my age slowly catching up on me."
        r "The woman lets out a hearty chuckle."
        r "Anyway [persistent.name], consider your face remembered from now on out!"
        if persistent.burger_faceRemembered == False:
            $ persistent.burger_faceRemembered = True
        else:
            n "Yet she never remembers you doesn't she?"
            n "No matter how hard she might try. No matter how many times she says she will."
            n "You will always be a stranger to her."
        jump burger_ordering_roseOrder

label burger_ordering_roseOrder: 
    if love_meter >= 2:
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
        jump burger_ordered
    else:
        r "So, have the two of you had a chance to {i}think about what you want{/i} to get?"
        l "..."
        l "Honestly I'm having some doubts. Let me look over the menu real quick."
        r "That's totally alright dear, take as much time as you need! I wouldn't want you to pick something that is not right for you afterall."
        n "While [persistent.date] is looking over the menu plastered on the wall behind the counter, Rose turns to you."
        r "How about you [persistent.name]? {i}Do you know what you want?{/i} Because you look rather indecisive."
        r "I'd hate for you to just pick any burger without thinking about it and end up regretting it and wasting a perfectly good burger."
        r "You might not be used to having to put so much care and thought into something like this, so if you don't think that's for you it's still not too late to {i}go somewhere else{/i}."
        r "So, what will it be?"
        menu:
            "*Tell her your order*":
                jump changeMindBurger


            "*Tell [persistent.date] you can't do this anymore.*":
                l "...What do you mean [persistent.name]?"
                menu:
                    "I have not been treating you as you deserve.":
                        jump burger_breakup_notTreatingWell
                        
                    "Rose is scaring me into ending this date.":
                        l "Well... do you know why she is doing that?"
                        menu:
                            "I have not been treating you as you deserve.":
                                jump burger_breakup_notTreatingWell

                            "I don't know but she's looking at me like she might kill me!":
                                n "[persistent.date] lets out a deep sigh."
                                l "Look [persistent.name], this is not going to work out at all."
                                l "The only reason Rose is looking at you like that is because she is worried about me."
                                l "The truth is, you have been acting quite poorly during this entire date and I was {i}this{/i} close to just walking out."
                                l "Yet something in me wanted to sit it out, hoped that you would somehow turn things around."
                                l "Yet now I understand that was foolish of me to think. You can't see what you have done wrong."
                                l "If you won't take accountability for your actions then I think it's just best we end things here."
                                #TODO: Fill in more
                                jump burger_breakup_leave


menu changeMindBurger:
    "I'll stick with my first choice, the [burger_choice].":
        r "I see... I would strongly advise against that choice if I were you."
        r "You know, after so many years serving customers I can tell just what they want."
        r "Perhaps you yourself don't know it yet, but I can tell this is not the right choice for you."
        r "Then again, I guess I'm just an old lady and can't exactly stop you."
        jump changeMindBurger_changedMind

    "I'll actually go for the veggie burger!" if not burger_choice == "veggie burger":
        $ burger_choice = "veggie burger"
        jump changeMindBurger_changedMind

    "I'll actually go for that juicy cheeseburger!" if not burger_choice == "juicy cheeseburger":
        $ burger_choice = "juicy cheeseburger"
        jump changeMindBurger_changedMind

    "I'll actually go for the fish burger!" if not burger_choice == "fish burger":
        $ burger_choice = "fish burger"
        jump changeMindBurger_changedMind

    "I'll actually go for the beef burger!" if not burger_choice == "beef burger":
        $ burger_choice = "beef burger"
        jump changeMindBurger_changedMind
    
    "I think I will go for some chicken tenders!" if persistent.chickenTendiesUnlock and not onlyBurgers and not burger_choice == "chicken tenders":
        $ burger_choice = "chicken tenders"
        jump changeMindBurger_changedMind

label changeMindBurger_changedMind:
    r "Now you are talking! It's never too late to change your mind [persistent.name]."
    r "Never..."
    n "Things turn awkardly silent between the two of you before Rose points her attention back to [persistent.date]."
    jump changeMindBurger_changedMind_date

label changeMindBurger_changedMind_date:
    r "What about you [persistent.date]? Will you order something else?"
    l "Actually, I think I'll stay with my original choice. As much as I am having doubts, I think I have to see this through for myself."
    r "...That's alright dear, I suppose you have to see for yourself to make up your mind."
    r "Just know that if you don't like it you can always come to me if need be, alright?"
    l "Thank you Rose, I really appreciate it."
    r "Any time, now, would you like to stay here while I prepare the burgers?"
    l "We'll go back to our table I think, if there's anything I'll give you a call."
    r "As you wish, I'll try to come as soon as I can."

label burger_ordered:
    show lilith talking_happy at burgerSit
    n "By the time you've reached the table [date_sub] [conj('date', 'is', 'are')] already sitting down, still as red as [date_sub] possibly could be."
    n "[date_sub] quickly brushes one hand over [date_pos] left cheek and somehow manages to turn even redder realising that [date_sub] [conj('date', 'is', 'are')] still blushing."
    n "Right then [date_sub] lets out a few small coughs as [date_sub] [conj('date', 'tries', 'try')] to somehow divert attention from what just happened."
    if get_lilith_current_loop_memory().get("beenBefore", "") == "lie" and persistent.burgerwent == 0:
        n "As you sit back down [date_sub] begins speaking once again."
        l "You had a hard time finding your way back there, didn't you?"
        n "[date_sub!c] [conj('date', 'tries', 'try')] to come off joking but [date_pos] eyes seem to study your face."
        menu:
            "It's just been so long since I last came here.":
                l "I suppose that makes sense, yet I also haven't been here in a while and had no trouble at all."
                l "Also Rose still knew me, just like she does all her customers. Then why doesn't she know you?..."
                menu:

                    "I lied about coming here before, I just wanted to make a good impression.":
                        jump burger_beenBefore_confession

                    "Maybe when I came here it just was really busy? I can't really remember anymore though... (Lie)":
                        l "I suppose that could be right..."
                        l "Even someone as great as Rose is only human."
                        l "Although it's a shame, Rose loves all her returning customers and that really seeps into her burgers."
                        l "I suppose we will have to come back here again some other time so you can taste the difference for yourself."
                        n "[date_sub!c] [conj('date', 'lets', 'let')] out a big chuckle."
                        jump burger_roseDeliversAtTable

                    "Perhaps she's begining to lose it? She's anything but young afterall. (Lie)":
                        l "What? I will not have you say such things about Rose! She is an absolute sweetheart."
                        l "I cannot do this anymore [persistent.name], if this is how you treat other people then I don't want any part in it."
                        if persistent.love_meter >= 2:
                            l "To think I actually thought this was promising for a moment."
                        else:
                            l "I knew things were bad, but I didn't think they were this horrible."
                        $ love_meter_updater(True)

            "I lied about coming here before, I just wanted to make a good impression.":
                label burger_beenBefore_confession:
                    l "Really? So you chose to lie to me? About something so simple?"
                    l "Not only that, you lied again when I asked you if you order the same burger each time."
                    if get_lilith_current_loop_memory().get("repeatCheese", False):
                        l "Did you specifically pick the cheeseburger because you knew it was my favorite?"
                    else:
                        l "Who knows what else you have been lying about?"
                        
                    l "All this to make me like you? If you hadn't already made a good impression I wouldn't even have been on this date with you in the first place!"
                    l "I'm really sorry if you somehow felt you needed to lie to me to be liked by me but I don't deserve that treatment."
                    l "Coming clean to me just now was a good step, I just wish you had took it from the start."
                    $ love_meter_updater(True)
                
    else:
        n "You sit back down a little slower than usual to give [date_obj] a chance to gather [date_pos] thoughts."
        n "Yet by the time you're back on your seat [date_sub] [conj('date', 'is', 'are')] still struggeling so you decide to help out."
        #TODO:  Possibly add one extra option?
        menu:
            "What was that about with Rose?":
                if love_meter >= 2:
                    l "Well... it's true that I haven't been here for quite a long time. Even though I really like it here."
                    l "I suppose that's why I brought this place up when we were looking for a place to meet up."
                    n "[persistent.date] pauses for a moment, [date_sub] [conj('date', 'seems', 'seem')] unsure whether to continue or not."
                    l "You see, my [ghost_sib] really used to love this place before..."
                    n "[persistent.date] freezes before [date_sub] can continue the sentence."
                    l "{size=*0.5}I'm sorry, I just- it's hard for me to say out loud...{/size}"
                    jump burger_brother
                else:
                    l "Honestly, I don't really want to talk about that right now."
                    menu:
                        "You seemed to want to with Rose though.":
                            $ love_points -= 2
                            $ record_attitude_event("limitIgnore", False)
                            l "Alright, I've had it! That is it. I can't do this anymore."
                            $ love_meter_updater(True)

                        "I'm sorry if I pryed too much.":
                            n "[date_sub!c] [conj('date', 'lets', 'let')] out a deep sigh."
                            n "It's fine really, it's just that we don't know each other well enough to talk about something like that."
                            menu:
                                "*Talk about something else.*":
                                    "Filler"
                                    #TODO: Have this lead to a few small topics. Not the ones she can talk about if you never ask about the brother though.

                                "But I feel as if I know you very well!":
                                    n "[date_pos!c] face sinks a little at your words."
                                    l "Look [persistent.name], if this is you knowing me well then I don't think I want to know you at all."
                                    l "If you knew me well you would be able to tell this is not how I want to be treated."
                                    l "Even if you didn't know me well, I doubt {b}anyone{/b} wants to be treated like this!"
                                    l "I'm out."
                                    $ love_meter_updater(True)


            "Don't worry, I'm excited about this date aswell!":
                l "You are?..."
                n "[date_sub!c] [conj('date', 'lets', 'let')] out a deep sigh of relief."
                l "I'm sorry [persistent.name], it's just been so long since I last did this."
                l "To tell you the truth I was really scared of messing things up."
                l "Although I suppose I am worrying about nothing, am I?"
                l "We are both having a good time and that is all that matters."
                $ love_points += 1
                $ record_attitude_event("honestExcitement", True)
                $ love_meter_updater(False)
                #TODO: Probably have this lead to something else, perhaps a conversation you can't have if you aquire about James since otherwise she will be too downtrodden.
               
            
                    
    label burger_ordering_rockMode:
        if get_lilith_current_loop_memory().get("fakeBurger", False):
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

menu burger_brother:
    "What was [ghost_pos] name?":
        jump burger_brother_question

    "Are you alright [persistent.date]? If this story hurts too much you don't have to continue.":
        $ love_points += 1
        $ record_attitude_event("noPryBrother", True)
        $ love_meter_updater(False)
        l "I don't think I'll ever be fully alright because of what happened. I think telling the story will always hurt."
        l "However that doesn't mean I wouldn't like to tell you about it."
        l "In fact, I think it might be good for me to eventually tell you."
        l "Just... maybe some other time [persistent.name]?"
        l "I do really appreciate it though. Thank you for being so considerate."
        n "Things grow quiet for a moment. It's not necessarily a bad quiet, it's one [date_sub] needed."
        n "You can tell so by [date_obj] body slowly relaxing into the state [date_sub] [conj('date', 'was', 'were')] in before."
        n "Then, when [date_sub] [conj('date', 'is', 'are')] properly recouped, the silence once again makes room for conversation."
        jump burger_roseDeliversAtTable
        label burger_roseDeliversAtTable:
            if burger_choice == "juicy cheeseburger":
                r "There you go! Two juicy cheeseburgers. The two of you have great taste."
            else:
                r "There you go! The juicy cheeseburger and the [burger_choice]. A lovely combination if I do say so myself."
            n "Rose winks at the both of you, [persistent.date] almost immediately flares up in embarassment again."
            l "Uhm, thank you Rose- Oh, could we pay already?"
            r "Don't worry about it hon. These are on the house. I'm just glad you're out again, and in such good company too!"
            n "She gives you a playful wink before turning around and heading back to the counter."
            n "[persistent.date] is left behind a blushing mess not able to form a coherent sentence or look you in the eyes."
            n "Deciding to spare her a little you pick up your [burger_choice] and dig in."
            n "As [persistent.date] follows [date_sub] [conj('date', 'lets', 'let')] out a small sigh of relief."
            n "The two of you get so lost in the delicious food you barely say a word until you're both halfway done."
            n "[date_sub!c] [conj('date', 'rubs', 'rub')] her tummy in contentment as [date_sub] [conj('date', 'chuckles', 'chuckle')]."
            l "Phew, she can be quite intense sometimes, can't she? But, I do think she likes you, [persistent.name]."
        l "Oh, I almost forgot to ask."
        l "How are you liking your burger [persistent.name]?"
        jump burger_burgerRate

label burger_breakup_notTreatingWell:
    l "...You're right. You have been quite lousy during this date."
    l "If anything I'm surprised you are taking some accountability for your actions now. However that doesn't make any of this okay."
    l "Although there is a part of me that has one question that I can't seem to shake off."
    l "Why? Back when we first started talking you seemed so different from this."
    l "Was I so wrong about you? Or did I do something wrong?"
    menu:
        "It's not you, some things just aren't meant to be.":
            l "What are you saying? That we're fated to be apart?"
            l "So that made you decide to take it out on me?"
            l "I think the only way standing between us is you."
            l "Yet if you really feel like things should end I can't say I disagree with you."
            l "However do not make a mistake, this was your doing, not fate."
            
        "I just have been feeling pretty stuck lately, I shouldn't have taken it out on you.":
            l "I'm sorry to hear that [persistent.name], I wish you had confided in me earlier."
            l "However, you are right. You shouldn't have taken that out on me."
            l "If this is how you'll treat me during hard times then I think it's for the best we never see each other again."

        "All of this was just not what I expected.":
            l "So you take it out on me? I had higher hopes for you than that."
            l "You know you can just talk to me about such things, right? We could have ended our date at any time."
            l "Instead you just toy with me and my feelings? It's not as if I can cater to all your expectations, right?"
    jump burger_breakup_leave
    label burger_breakup_leave:
        n "With that she leaves you standing at the counter as she first fetches her purse from the table and then walks out of the restaurant."
        n "Perhaps this was the right thing to do after treating her so badly?"
        n "Then again, perhaps the right thing would have been to not treat her like that in the first place."
        n "Rose gives you an unapologetic shrug."
        r "Believe me, it was for the best. Also, if you're not ordering anything could you leave? I have other customers to attend to."
        n "You look behind you and see no one else standing in line."
        l "With your head held low you leave the restaurant, never to come back or hear from [persistent.date] again."
        if persistent.lildeaths >= 1:
            n "Well, until the next time at least."
        $ lilithAliveEnding = True
        if persistent.lildeaths >= 1:
            $ ending_check = "good ending?"
        else:
            $ ending_check = "bad ending"
        jump gameOver

label burger_ordering_nightmare:
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
    
menu burger_burgerRate:
    "It's the best one I ever had!":
        call burger_burgerRate_best from _call_burger_burgerRate_best
           
    "It's pretty good.":
        call burger_burgerRate_prettyGood from _call_burger_burgerRate_prettyGood
       
    "It's a nothing burger, literally.":
        call burger_burgerRate_nothingBurger from _call_burger_burgerRate_nothingBurger
     
    "It's really bad.":
        call burger_burgerRate_reallyBad from _call_burger_burgerRate_reallyBad

jump burger_deathBuildup
      
label burger_burgerRate_best:
    if get_lilith_current_loop_memory().get("beenBefore", "") != "true" and get_lilith_current_loop_memory().get("beenBefore", "") != "lie":
        l "That great? I honestly can't say I'm surprised. Rose's burgers are the best for a reason after all."
        n "[persistent.date] let's out a small chuckle."
        l "I'm glad you like them so much [persistent.name]!"
        l "Although I hope this didn't ruin other burgers for you, it's hard to go back to regular burgers after you tasted these isn't it?"
        l "The thing is, even if this burger is perfect, there will be days we have to make due with good enough. In days like that we will need to try to atleast be satified with what we have."
        l "Afterall, you can't eat nothing but these burgers, I don't think that'd be healthy."
        menu:
            "At least we'll have eachother, I'm sure anything would taste good if I'm enjoying your company.":
                $ love_points += 1
                $ record_attitude_event("companyCompliment", True)
                $ love_meter_updater(False)
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
                l "And if you keep eating Rose's [burger_choice]s for the rest of your life they will grow very stale quicker than you think."
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
                l "I'm sure we wouldn't have to limit ourselves to just going back in time to eat burgers earlier, we could do so many great things."
                #TODO: Add some more dialogue here, it's a perfect spot for it.
                menu:
                    "I could make sure to never go on this date.":
                        "Filler"

                    "I could enjoy this date over and over again.":
                        "Filler"

                    "I could find the perfect thing to say on this date.":
                        if love_meter > 2:
                            l "Really? You'd have this super cool machine to do whatever you want and you'd use it to say the right things to me?"
                            l "As silly as that is on it's own I'm not sure if I should be flattered or worried."
                            l "The whole point of a date is to see if you are compatible with someone, isn't it?"
                            l "If you have to conform yourself to their norms just to have a chance with them, are you really being yourself?"
                            l "If not, do you really want to be with someone who only likes you for someone you are not?"
                            l "Besides, you shouldn't see a date like something that can be won [persistent.name]. This isn't some videogame where picking specific options wins or loses you points."
                            l "Just be your authentic self like you are now and I promise you, you'll be more than enough."
                        else:
                            l "Honestly, I feel like you might not be able to find it even with all the time in the world..."
                            l "If this is you trying to make this work then I don't think it will work out at all."
                            l "Instead, I think you'll have to work more on yourself to fix whatever is holding you back."
                            l "It is genuinely a shame, because when we first talked you seemed so different."
                            l "I suppose I hadn't yet glimpsed behind the mask, but now I have seen it crystal clear."
                            l "Goodbye [persistent.name], I think it's best we never see each other again."
                            $ love_meter_updater(True)
                            
                

            "I'm sure it's the lovely company that makes it even better.":
                if love_meter > 2:
                    $ love_points += 1
                    $ record_attitude_event("companyCompliment2", True)
                    $ love_meter_updater(False)
                    l "You really are a charmer aren't you [persistent.name]?"
                    l "Although I have to admit that I feel the same way."
                    l "Sure, I have been craving one of these burgers for a very long time...but I think you might be a very likely culprit aswell."
                    l "It just feels... more special? So I'm really happy to hear that you think the same thing [persistent.name]!"
                else:
                    $ love_points -= 1
                    $ record_attitude_event("companyCompliment2_failed", False)
                    l "{b}{size=+10}Really?{/size}{/b} Look, while that would have been a sweet sentiment you have to know it's kind of wasted on this date."
                    l "You have been completely different than how you were when we first met! I honestly don't recognize you anymore."
                    l "What happened to the person that would make such comments like the one you just made feel sincere?"
                    l "Why have you been treating me like this? Even now I can't help but think you might be sarcastic."
                    l "I tried to sit this out, since I thought I owed it to myself but I can't stand this any longer."
                    $ love_meter_updater(True)
                
    return                        

label burger_burgerRate_prettyGood:
    $ persistent.burger_nothingIsPerfect = True
    l "Pretty good, huh? That's high praise!"
    n "[persistent.date] gives you a warm smile, clearly pleased by your response."
    l "I think \"pretty good\" is often better than \"perfect\"."
    l "How many things do you know that are perfect? Many of those tend to not remain perfect upon closer inspection."
    l "Because in reality, almost nothing is truly perfect, which it doesn't need to be."
    l "I would say \"pretty good\" is more than good enough in most cases."
    menu:
        "But doesn't that mean we can never find anything better than \"pretty good\"?":
            l "Absolutely not [persistent.name]! What I mean with perfection not really being attainable is in a more objective sense."
            l "Every rose has it's thorns, nothing is flawless. Yet to us, on a subjective scale, that rose can be perfect."
            l "Perhaps smelling it gave us nostalgia to a time long gone, or admiring it's beauty sparked something in our hearts."
            l "In that way we can ascribe perfection to something inherently imperfect."
            l "You see it all the time with how people rate things, a 10/10 is not necessarily without any faults but the person still feels very strongly for it."

        "Some things {b}can{/b} be perfect though. Like getting a perfect score on a test.":
            l "I suppose that is true, although personally I'd argue that is a very constructed form of perfection."
            l "It's a concept made up by people, isn't it? I'd say in that sense the perfection is very subjective, even if almost everyone would agree that it is perfect."
            l "Objective perfection is a really hard thing to properly emulate or wrap your head around."
            l "It might even be a little unbelievable if you were to encounter it yourself. Almost as if you couldn't possibly feel as if you've earned it."
            l "So while some things can definitely be considered truly perfect, I think it's a very manufactured concept of it."

    n "[date_sub!c] [conj('date', 'takes', 'take')] a thoughtful bite of [date_pos] own burger, as if savoring the moment."
    l "Philosophy aside, I'm glad you're enjoying it, [persistent.name]."
    if get_lilith_current_loop_memory().get("beenBefore", "") != "true" and get_lilith_current_loop_memory().get("beenBefore", "") != "lie":
        l "Maybe next time we can try some of the other things on the menu and see if they measure up?"
    else:
        l "Maybe next time we can go to that Chinese restaurant I talked about and see how you like the food there? It's really really good."
    return

label burger_burgerRate_nothingBurger:
    n "[persistent.date] tilts [date_pos] head, a small frown tugging at the corner of [date_pos] lips."
    l "A \"nothing burger\" huh? I guess that means it's... okay?"
    n "[date_sub!c] [conj('date', 'tries', 'try')] to mask [date_pos] disappointment with a soft chuckle."
    l "Maybe it just didn’t live up to the hype. I hope it wasn’t too underwhelming, though."
    if get_lilith_current_loop_memory().get("beenBefore", "") != "true" and get_lilith_current_loop_memory().get("beenBefore", "") != "lie":
        l "Rose makes all her burgers with as much love as is feasibly possible but maybe her [burger_choice] isn't really your thing?"
        n "You can tell [date_sub] [conj('date', 'was', 'were')] hoping you would enjoy it more."
        l "If you'd like, we can come back and try something different next time. There's so much more on the menu here that might be more your style."
        if get_lilith_current_loop_memory().get("burgerFanatic", False):
            l "Or maybe it's just better to try one of the other restaurants? Maybe burgers just aren't your thing?"
        else:
            l "Or maybe we should just try one of the other restaurants? Although... you did say you like burgers, right? Perhaps we should go to a place where they have the ones you like?"
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
                n "You shake your head. Even if you don't like the burger, you have to admit it was quite filling."
                #TODO: Perhaps fill this out a bit more aswell. Not entirely sure where it could lead to for now.

            "Oh, I usually don't pick a burger, I tend to always pick chicken tenders.":
                n "[persistent.date] can't help but chuckle slightly at your accidental joke."
                l "I see [persistent.name], that's totally fine."
                l "I just wonder what made you change your mind this time? Why did you pick a [burger_choice]?"
                menu:
                    "I was in for a change.":
                        l "That makes sense, sometimes it's good to have a little change here and there isn't it?"
                        l "It can truly make for a breath of fresh air. Of course, sometimes it can be a bit of a dissapointment."
                        l "However, never trying anything new and just doing the same things over and over is going to end up in a lot more dissapointment eventually than trying something new."
                        l "Believe me, sometimes you might stick with something because it's all you have ever known and you already invested so much time into it."
                        l "However hard it might be, sometimes you have to acknowledge you fell victim to the sunk cost fallacy and try to let go."
                        
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
    n "[persistent.date] freezes for a moment, taken aback by your comment."
    if get_lilith_current_loop_memory().get("beenBefore", "") != "true" and get_lilith_current_loop_memory().get("beenBefore", "") != "lie":
        l "Really? Oh no, I'm so sorry, [persistent.name]."
        l "I hyped this place up very much, didn't I? Maybe that set your expectations too high."
        n "[date_sub] [conj('date', 'looks', 'look')] genuinely upset."
        l "I guess taste is pretty subjective. At least now we know, right?"
        n "[date_sub!c] [conj('date', 'tries', 'try')] to force a smile, but it's clear [date_sub] [conj('date', 'is', 'are')] more dissapointed than [date_sub] expected."
        l "Maybe next time we could go somewhere else?"
        l "Hopefully the chinese restaurant or the cafe will be more to your liking."
    else:
        l "Really?... But you've been here before, right?"
        l "What is different now?"
        n "[persistent.date] gives you a confused look."
        menu:
            "I never picked this burger before.":
                l "Oh I see, so the [burger_choice] isn't really your thing?"
                l "That's totally fine, I suppose not every kind of burger can be everyone's favourite after all."
                l "It's good of you to try something else though, picking the same thing over and over can get bland real fast."
                l "Although, sometimes it can be hard to do that, in the fear that the other experience will be worse than the familiar and comfortable thing you always pick."
                l "Maybe if we come here next time you can tell me what kind of burger you tend to like and I can recomend a few ones that I think you will like based on that?"

            "I think there was something wrong with my burger.":
                l "Really?"
                l "Was there something you didn't order in there?"
                l "Or did it just not taste good?"
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
                    n "[date_sub!c] [conj('date', 'does', 'do')] make a good point, even if [date_sub] [conj('date', 'does', 'do')] not know the full extent of it."
                    n "You are trying to save [date_obj], aren't you?"
                    n "Is that why you are treating [date_obj] like that?"
                    if persistent.lilithAliveAndRetriedCounter > 0:
                        n "Because you think it might be the key to saving [date_obj]?"
                        n "Even if it hypothetically was, would it be worth it?"
                        n "You would be seen as horrible in [date_pos] eyes."
                    else:
                        n "No, that can't be it. You already saved [date_obj] before. So this is rather pointless, isn't it?"
                        n "I could understand if you maybe were trying to find a better outcome for the both of you, but this is not how you would reach something like that."
                        n "Then why are you putting [date_obj] through this?..."
                        n "Perhaps just to see what reaction you will get out of it?"
                        n "Is that what this is, just an excuse to get some new dialogue?... Don't answer that, I want to pretend like I don't know your what you'd say."

                l "You weren't like this at all when we talked before, is this how you really are?"
                l "Either way, I won't stick around to find out."
                l "Goodbye [persistent.name]."
                $ angryLilith = True
                $ noTalkAngryLilith = True
                $ love_points -= 1
                $ record_attitude_event("companyRoast", False)
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
        $ get_lilith_current_loop_memory()["askedbrother"] = True
        
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
    $ record_attitude_event("abigailJoke", True)
    $ love_meter_updater(False)
    $ get_lilith_current_loop_memory()["playerToldAbbyJoke"] = True

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
        n "It was not necessarily the joke doing this, you feel. Moreso the gesture behind it."
    $ _player_cps = float(getattr(_preferences, "text_cps", 35) or 35)
    $ _thanks_target_cps = 35.0 * 0.33
    $ _thanks_cps = min(_player_cps, _thanks_target_cps)
    l "{cps=[_thanks_cps:.2f]}Thank you [persistent.name], I mean it.{/cps}"
    n "[persistent.date] continues as if nothing happened."
    jump burger_living

label burger_living:
    if not persistent.rockMode:
        l "So, what do you do for a living?"
        $ persistent.booklover_knowledge = True
        $ get_lilith_current_loop_memory()["bookloverTalked"] = True
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
                        $ changeableWord = player_input("Maybe...").strip()
                        $ get_lilith_current_loop_memory()["rockBandName"] = changeableWord if changeableWord else ""
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
        l "Do you know how frustrating it is to have a version of something in mind while missing the means to bring it into reality just right?"
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
                                                $ record_attitude_event("beachSuggestion", False)
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
                                                $ neverEndingVariety = "time"
                                                l "For now though, instead of thinking of stories, let's continue writing ours, starting with this date"
                    
                                            "Do you have another idea for a story?":
                                                l "...Maybe something simple? I think I'd like a fantasy story."
                                                l "It could be about a merchant and a princess who is also a leader of a thieves' guild."
                                                l "Together they have to save the kingdom from a tyrant king, who's rule would lead the kingdom only to ruin."
                                                l "To do so they would need to usurp the king, something seemingly impossible."
                                                l "First they would need to defeat the evil jester who is also a bit of a magic trickster, protecting the castle with a forcefield."
                                                l "I'm not sure exactly how they would do that, but I'm sure we could brainstorm a statisfying way to do so later."
                                                l "For now though, I'd like to be in the moment with you. Maybe we could write that story together during our next date?"
                                                $ neverEndingVariety = "fantasy"

            "I think I know quite well. It seems as if no matter what I try there is no way to reach my goal.":
                l "Really? I suppose it's no wonder you of all people, uhm rocks, can relate."
                l "What do you do in a situation like that though? When it feels as if your goal is just always out of reach?"
                menu:
                    "You stop trying for that goal and adjust for a realistic one.":
                        l "That seems like the best thing you could possibly do in those situations."
                        l "A lot of people have very ambitious goals that are very overscoped, only for the goalpost to continually move even further away."
                        l "I think the kindest thing someone can do to themselves is to downscale their gigantic goals a fair bit so they become more achievable."
                        l "Then again, it's also very important to not make them too easily doable, since some people would grow bored if there is not a big enough challenge."
                        l "If you are like that I would suggest splitting your big aspirations up in a few smaller ones that act as stepping stones for the larger goal."
                        l "That way you can tackle a tough challenge while feeling like you are making progress step by step."
                        menu:
                            "But what if I only ever can get close to my goal without ever reaching it?":
                                l "To me that seems like a sign that perhaps your main goal is still too ambitious."
                                l "Perhaps it is not feasible with your current skills, or maybe it's even completely impossible."
                                l "I think you should probably try considering which one of the two it is and accordingly adjust your approach."
                                l "Either way, you still got as close as you did to your goal, and that is something to be proud of aswell."
                                l "You got further than anyone who didn't try."

                    "You give up.":
                        l "Really? Just like that? I suppose trying for an unachievable goal without any success is going to be very unsatisfying."
                        l "Then again, I do believe we need a goal to replace the one we gave up on."
                        l "Although it is a very hard balancing act. When do we call it and quit?"
                        l "Perhaps victory is right around the corner or perhaps it never existed at all."
                        l "That's why perseverance is so important, because otherwise you risk giving up on all of your goals before ever reaching any of them."
                        l "Ofcourse, sometimes the best and only action you can really do is quit and start anew somewhere else."
                        menu:
                            "How do you know when to quit?":
                                l "That is a very difficult question which might be even harder to answer."
                                l "I don't think there is a specific point at which everyone should."
                                l "It genuinely varies from situation to situation and person to person."
                                l "Although I think my answer would be when it doesn't give you any sense of progress, hapiness or purpose anymore."
                                l "Do not let the sunk cost fallacy dictate your decisions. If you do feel that, it might precisely be the sign that you need to stop."
                                l "Your time is yours and you do not owe it to anyone or anything to spend it on them."
                                l "Afterall, time you volontarily spend on someone or on something is so much more meaningful than when you are forced to do so."

                    "Anything is possible, you just need to try hard enough.":
                        l "Do you really think so? I suppose in general if you really work for something you are more likely to achieve it."
                        l "However, that does not really apply to everything, some things are just beyond our control."
                        l "For example, I can't grow hands, no matter how hard I would try to."
                        l "Sometimes the effort we need to achieve a goal is also not proportionate to how much someone else might need."
                        l "If it came between me and a human in running a marathon, the human would very clearly have a better shot at doing so."
                        l "So it's not because something is achievable for one person that it automatically means anyone can do it."
                        l "Sometimes you need the right circumstances or conditions to succeed."
                        l "However, that's also not everything. Some people who get the perfect conditions will flop regardless of their chances."
                        l "Others without any favorable circumstances might still make it through sheer determination."
                        l "I don't believe that anything is possible if you try hard enough."
                        l "However, I do believe that {i}a lot{/i} is."
                        l "So if you have dreams, I would encourage you to pursue them as much as is feasible."
                        l "Just be aware that even if you fail you still did more than those that do not dare to try."
                        l "Besides, perhaps you can pick the dream back up later when the time is right or maybe it shows you the path to another aspiration."

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
            $ burger_poem_cleancheck = "clean"
            $ get_lilith_current_loop_memory()["poemFingerState"] = "clean"
            jump burger_living_showWriting_poem
        "*Don't clean your fingers and just take the notebook*":
            $ burger_poem_cleancheck = "dirty"
            $ get_lilith_current_loop_memory()["poemFingerState"] = "dirty"
            jump burger_living_showWriting_poem

label burger_living_showWriting_poem:
    $ burger_poem_cleancheck = get_lilith_current_loop_memory().get("poemFingerState", burger_poem_cleancheck)
    $ mark_tracker_scene(1)
    if burger_poem_cleancheck == "clean":
        n "[persistent.date] seems thankful that you cleaned your fingers."
        n "You take the notebook out of [date_pos] hand and begin to read."
        n "You can read the entire thing in [date_pos] voice somehow."
    else:
        $ love_points = -1
        $ record_attitude_event("dirtiedNotebook", False)
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
    if burger_poem_cleancheck == "clean":
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
            jump burger_deathBuildup

label burger_poem_rating_terrible:
    $ love_points = -1
    $ record_attitude_event("harshPoem", False)
    $ love_meter_updater(False)
    if love_meter >= 2 and get_lilith_current_loop_memory().get("poemFingerState", "") == "clean":
        n "[persistent.date] begins to frown slightly."
        n "[date_sub!c] [conj('date', 'looks', 'look')] hurt by your words."
        l "Really?..."
        l "It's probably not my best work ever since I did write it years ago in a pretty edgy phase of my life."
        l "Then again, I think it definitely has some merit to it. If only as to serve as some sort of timecapsule to catch a glimpse of past me's soul."
        l "Although I understand if you don't really like my older stuff. Perhaps some of my newer poems would be more your style?"
        l "I could show you some another time if you'd like."
    else:
        l "Look, I know this is definetly not one of my best works. But you were the one asking to read something of mine!"
        l "To then treat not only it but also me with so little respect by dirtying it both literally and figuratively..."

        if get_lilith_current_loop_memory("attitude").get("minor_love_offence", 0) <= 2:
            l "I really don't seem to understand [persistent.name]. Other than this you actually were really nice."
            l "Still, I can't just ignore what you did just now."
            $ love_meter_updater(True)
        else:
            l "You actually have not been treating me well at all pretty much this entire time."
            l "I'm not sure what has gotten into you since you used to be so nice when we first met."
            l "However, whatever this is, I want nothing to do with it."
            $ angryLilith
            $ love_meter_updater(True)

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
    $ get_lilith_current_loop_memory()["musicloverTalked"] = True
    l "But if I kept playing it I think I would slowly grow to resent it, sometimes it's just better to end things on a good note."
    n "[persistent.date] lets out a small giggle."
    l "That pun wasn't intended, I swear!"
    jump burger_Brotherasked

label burger_Brotherasked:
    if get_lilith_current_loop_memory().get("askedbrother", False) == True:
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
            if get_lilith_current_loop_memory().get("playerToldAbbyJoke", False) == True:
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
    $ burger_alt_in_loop = get_lilith_current_loop_memory().get("burger_alt", False)
    n "Suddenly you hear screaming from a few shops further."
    l "What was that?"
    menu:
        "It's probably not our concern.":
            jump burger_deathBuildup_choice1

        "Maybe there is a sale going on somewhere?":
            jump burger_deathBuildup_choice2

        "This is important, duck now." if persistent.burger_death_1 and not burger_alt_in_loop and not persistent.rockMode:
            jump restaurant_death_1_prevented

label burger_deathBuildup_choice1:
    if not get_lilith_current_loop_memory().get("burger_alt", False):
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
    if not get_lilith_current_loop_memory().get("burger_alt", False):
        jump restaurant_death_1
    else:
        jump burger_alt_askHerAQuestion

label burger_alt_askHerAQuestion:
    $ get_lilith_current_loop_memory()["burger_alt"] = False
    $ musiclover_talked = get_lilith_current_loop_memory().get("musicloverTalked", False)
    $ booklover_talked = get_lilith_current_loop_memory().get("bookloverTalked", False)

    menu:
        "*Ask [date_obj] a question.*":
            menu:
                "So you mentioned that you really like music. Which music do you listen to?" if persistent.musiclover_knowledge and musiclover_talked:
                    jump burger_alt_askHerAQuestion_musicLover
                "Which music do you like to listen to?" if persistent.musiclover_knowledge and not musiclover_talked:
                    jump burger_alt_askHerAQuestion_musicLover
                "So you mentioned that you like writing. That made me curious, which books do you like to read?" if persistent.booklover_knowledge and booklover_talked:
                    jump burger_alt_askHerAQuestion_bookLover
                "Which books do you like to read?" if persistent.booklover_knowledge and not booklover_talked:
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
