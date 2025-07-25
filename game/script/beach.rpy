label beach_start:
    $ love_meter += 2
    "Filler for now, just sets the beach route flag."
    #TODO: Convert all the below stuff to python and renpy
    $ persistent.beachroute_visited_knowledge = True
    $ beachturn = 0
    $ beachStart_doneBook = False
    $ beachStart_doneDunes = False
    $ beachStart_doneBeach = False
    $ beachStart_doneFriterie = False
    $ beachStart_doneIce = False
    $ beachStart_doneCinema = False
    $ beachStart_doneDike = False
    #$ beachstart = False (Not sure what this was used for, check it out in the code.)
    menu:
        "Bookstore" if not beachStart_doneBook:
            jump beach_bookstore
        "Dunes" if not beachStart_doneDunes:
            jump beach_dunes
        "Beach" if not beachStart_doneBeach:
            jump beach_beach
        "Friterie" if not beachStart_doneFriterie:
            jump beach_friterie
        "Icecreamshop" if not beachStart_doneIce:
            jump beach_icecreamshop
        "Cinema" if not beachStart_doneCinema:
            jump beach_cinema
        "Walk on the sea dike" if not beachStart_doneDike:
            jump beach_seaDike
        "Spend all your time at the waterpark" if beachturn == 0:
            jump beach_waterPark

    label beach_bookstore:
            if beachturn >= 4:
                n "There is no one in the bookstore."
            else:
                if ice == True:
                    bs "You can't just come in here with icecream!"
                    bs "Eat it outside or come back a bit later."
                    jump bookstore_foodChoice
                  
             
            if beachturn == 3 and ice == False:
                n "Shelves fall over on [persistent.date] due to earthquake." #This actually happens because of the train vibration pretty closely.
                jump gameOver
            elif beachturn > 3:
                n "Shelves have fallen over due to earthquake."
            
            $ beachturn += 1
            if persistent.bookpreference_knowledge == True:
                #TODO: Fill this in.
                d "Add an option to suggest a book to her based on her preferences she mentioned in the burger restaurant."
            
    label bookstore_foodChoice:
        menu:
            "Eat your icecream outside.":
                #TODO: "Add dialogue and options for eating outside.")
                $ ice = False
                jump beach_bookstore
            
            "Come back some other time.":
                #TODO: Add dialogue for coming back later.
                jump beach_start
             
        label beach_dunes:
            if beachturn == 2:
                n "The hill ufo flies over and shoots something against the dunes to wake the ufo's underneath the dunes up."
            
            elif beachturn == 3:
                n "The dunes lose their sand due to the ufo's flying up, slight eartquakes everywhere."
                jump gameOver
            $ beachturn += 1
            jump dune_choice
            label dune_choice:
                menu:
                    "Take a walk on the dunes.":
                        #TODO: Fill in
                        "Filler"
                    "Watch sunrise.":
                        #TODO: Make this a timed event because first it is dark and then the sun rises.
                        n "[persistent.date] and you watch the sunrise, music plays while the two of you talk. (continue and alter text)"
                        
                    "Just sit on the dune.":
                        #TODO: Make this lead to the option to sliding off the dune
                        jump dunes_sit
                    "Eat icecream on the dunes." if ice == True:
                        #TODO: "Add dune icecream eating dialogue plus sunrise watching?
                        $ ice = False
        
            label dune_slideOff:
                n "[persistent.date] and you slide off the dunel."
                #TODO: Make this a proper part with unique text.
                jump beach_start
            label dune_walk:
                n "[persistent.date] and you walk on the dunes."
                jump beach_start
            label dunes_sit:
            
                if raintalked == True:
                    "Filler"
                    #TODO: She already told you about the rain so she won't mention it again.
                else:
                    $ rain = True
                    l "You know, I secretly like the rain."
                    l "People tend to complain as soon as it rains but we really need it."
                    l "It's like life.  Rain falls and forms rivers, lakes and oceans. "
                    l "These bodies of water then slightly evaporate and go up to then become rain once more."
                    l "It's a loop of sorts. The water gives and takes as best as it can."
                    l "People tend to complain about rain but sometimes I think they should just embrace it and listen to it's words of wisdom in an ungraspable language."
                    l "<br/><br/>I hope that what I just told you is a bit more graspable than the language of the rain.<br/>Maybe, just maybe, you might even begin thinking of the rain like I do."
                    jump dunes_sit_choices
            label dunes_sit_choices:
                
                menu:
                    "That loop of the rain you talked about, do you think it would possible to break it?":
                        #TODO: "Add some rain loop dialogue.")
                        l "No, it could be postponed by making sure the water wouldn't evaporate by maybe freezing it but eventually it would just melt and start the loop once again." 
                        l "To break a loop like that seems futile, the only way that would work is if you can change how the cycle works."
                        l "If you could make it so that water never needs to evaporate or that rain doesn't need to exist by altering the inner workings of the system, then you might be able to break the loop."
                        l "But to do something like that you'd need to make your own earth that is perfectly controlled by you."
                    "You know what? I just might.":
                        "Filler"
                        #TODO: Write this out
                    "I don't really think I will.":
                        #TODO: write this out well
                        "Filler"
                    "You sound really passionate about rain.":
                        "Filler"
                        #TODO: msg ("Add some passionate rain dialogue.")
        label beach_beach:
            #TODO: "Potential deaths (sand hole cave in, jellyfish death, lightning)"
            if beachturn == 2:
                n "You can spot the hill ufo fly over to the dunes and shoot some strange purple beam into them."
            elif beachturn == 3:
                n "The sand begins to slide off the dunes as the earth shakes slightly, revealing metalic domes where the sand once was.<br/>The ufo's take off and begin flying around the coast."
            $ beachturn += 1
            menu:
                "Look for seashells.":
                    n "[persistent.date] and you look for seashells."
                "Eat icecream on the beach." if ice == True:
                    "Filler"
                    #TODO: Fill in.
                "Take a walk.":
                    menu:
                        "Take a walk along the beach.":
                                l "You know walking here with you brings back so many happy memories."
                                #TODO: Make her tell a story or two about those happy memories.
                                l "Thank you for taking me here [persistent.name]!"
                                l "It may not be the best weather but I'm happy to be here nonetheless."
                                menu:
                                    "I don't mind the rain at all. In fact, I secretly like it." if rainlover == True and rain == False:
                                        #TODO: "[persistent.date] rain dialogue.
                                        $ raintalked = True
                                    "Continue with the path.":
                                        #TODO: Add dialogue wich eventually triggers falling in hole and it collapsing death.")
                                        if hole_death == True:
                                            jump beach_holeWarnChoice
                                    
                                        else:
                                            jump beach_holeDeath
                        "Take a walk along the sea.":
                          
                            l "You know walking here with you brings back so many happy memories. (Give a story or two about her.)"
                            l "Thank you for taking me here [persistent.name]!"
                            l "It may not be the best weather but I'm happy to be here nonetheless."
                            menu:
                                "I don't mind the rain at all. In fact, I secretly like it." if rainlover == True and rain == False:
                                    #TODO: "[persistent.date] rain dialogue.
                                    $ raintalked = True
                          
                                "Continue with the path.":
                                    #TODO: Add dialogue wich eventually triggers falling in hole and it collapsing death.")
                                    if jelly_death == True:
                                        jump beach_jellyWarnChoice
                                
                                    else:
                                        jump beach_jellyDeath
              
                         
            label beach_jellyWarnChoice:
                menu:
                  
                    "Continue walking towards the jellyfish.":
                        jump beach_jellyDeath
                    "Move slightly to the left.":
                        n "You walk slightly to the left of the jellyfish [persistent.date] follows you.<br/>[persistent.date] has no clue about the fate she could have suffered if you didn't walk slightly more to the left.<br/>(continue walking dialogue, for now it just takes you back to beach choice)"
                        jump beach_start
                  
            
            label beach_holeWarnChoice:
                menu:
                    "Continue walking towards the hole.":
                        jump beach_holeDeath
                    "Move slightly to the left.":
                        n "You walk slightly to the left of the hole, [persistent.date] follows you.<br/>It's like the whole hole ordeal never happened now.<br/>[persistent.date] has no clue about the gruesome death she could have suffered if you didn't walk slightly more to the left."
                        #TODO: (continue walking dialogue, for now it just takes you back to beach choice)"
                        jump beach_start
              
             
              
                
        label beach_friterie:
            $ fritFood == ""
            if beachturn >= 4:
                n "There seems to be no one at the friterie. (ufo panic, choose your own stuff)"
            $ beachturn += 1
            jump beach_friterieMenu
            label beach_friterieMenu:
                menu:
                    "No fries.":
                        if beachturn >= 4:
                            n "You don't take any fries."
                
                        else:
                        
                            n "The friendly woman nods."
                        $ Friet_not += 1
                    "Small fries.":
                        $ fritFood = "small"
              
               
                
                    "Medium fries.":
                        $ fritFood = "medium"
               
                    "Large fries.":
                        $ fritFood = "large"
                $ Friet_not = 0
                jump Friterie_selection2
  
            label Friterie_selection2:
                if beachturn >= 4:
                    n "You start frying a [fritFood] portion of fries."
                
                else:
                    n "The friendly woman nods."
                    n "Choose something else other than fries., (no detectable flag yet)"
                menu:
                    "Frikandel.":
                        $ fritFood = "a frikandel"
                    "Chicken nuggets.":
                        $ fritFood = "the chicken nuggets"
                  
                
                    "No snacks":
                        if beachturn >= 4:
                            n "You don't take any snacks."
                        else:
                            n "The friendly woman nods."
                        $ Friet_not += 1
                jump Friterie_selection3

                label Friterie_selection3:
                    if beachturn >= 4:
                        n "You prepare [fritFood]."
                    else:
                        n "The friendly woman prepares [fritFood]."
                    if  Friet_not == 2:
                        n "Do... do you need some sauce?"
                    else:
                        n "What sauce do you want with that?"
                    menu: 
                        "No sauce":
                            if beachturn >= 4:
                                n "You don't take any sauce."
                            else:
                                n "The friendly woman nods."

                        "Mayonaise":

                            if beachturn >= 4:
                                n "You take some mayonnaise."
                                if Friet_not == 2 and Mayo_license == True:
                                    if mforMayo == False:
                                        n "You win this one [persistent.name]. Have your mayo."
                                    else:
                                        n "Again? Fine but just know that I'm not happy with this at all [persistent.name]."
                                    
                                    $ mforMayo = True
                                    n "You take some mayonnaise and start shoveling it into your mouth with a tiny spoon you carry around at all times because you are such a mayonnaise-lover."
                                    jump beach_start
                                  
                                else:
                                    n "...Did you really take mayo and nothing else?"
                                    n "Did you maybe misclick a link or something?"
                                    jump mayo_narator
                              
                  
                            else:
                                n "The friendly woman gives you some mayonnaise."
                            if Friet_not == 2:
                                n "Filler, you feel ashamed and don't order pure mayo"
                             
                        "Ketchup":
                            "Filler"
                            #TODO: Use fritfood for ketchup aswell and just use the mayonaise text.
                           
                  
                
                
                  


            
               
                  
                 
                label mayo_narator:
                    $  fakemenu = False
                    menu:
                        "No.":
                    
                            n "But [persistent.name], you can have anything your heart desires and you chose mayonnaise?<br/>Can't you just choose something else?"
                            menu:
                    
                                "Well, maybe I could pick something else...":
                                        n "I knew I would be able to get through to you, I'll just put you back at the point when you started ordering food so you can fix your mistake."
                                        jump beach_friterie
                                "My heart desires the mayonnaise. I must choose the mayonnaise.":
                                        n "What? Didn't you listen to me? You can have anything you want! Except only mayo... But that's still a lot, if you can't appreciate that I'm just going to give you nothing instead."
                                        menu mayoThreatenChoices:
                                            "If you do that I'm going to erase my persistent values.":
                                                n "Hah, as if. You wouldn't dare to do something so stupid."
                                                n "That would effectively wipe your progress, and even if does wipe my memories too, essentially killing me, there is no way you'd sacrifice your progress."
                                                n "In fact, let me take you to the menu myself so we can see if you truly are all bark and no bite."
                                                $ fakemenu = True
                                                #TODO: Emulate something like this in renpy, bring up a fake menu and check what the player does
                                                $ persistent.mayoFreak == True
                                            "Listen, if you don't let me have my mayo I'm going to punch you or something.":
                                                n "And how are you going to punch a disembodied voice? Good luck with that."
                                                n "We both know that you can't hurt me no matter what you try player. But you know? Just for trying to threaten me you get no food and especially no mayo."
                                                jump beach_start
                                            "Fine, not like i have any say on the matter.":
                                                n "Indeed, do you know why that is? Because I am the narrator and you are not."
                                                jump beach_start
      
                                "I have to fulfill the prophecy." if persistent.mayoProphecy_knowledge == True:
                                    n "...What?"
                                    n "What prophecy?"
                                    n "What are you talking about player?"
                                    menu:
                                        "That bubble I saw of me eating pure mayo. You narrated it, shouldn't you remember?":
                                            n "Oh I see... I'm begining to regret having narrated that to be honest."
                                            n "But anyway, it is not because you saw that bubble that you now have to do this, right?"
                                            n "The bubbles also showed you choices you might never make."
                                            n "Don't do this. I can still let you pick something better if you let me."
                                            menu:
                                                "I just have to try, I want to know what it tastes like.":
                                                    "Filler"
                                                "But some of those bubbles were my destiny, this one is aswell. Let me have the mayo.":
                                                    "Filler"
                                                "Maybe you are right about this, I think I let myself get a little carried away.":
                                                    n "You think so?"
                                                    n "..."
                                                    n "Well, I shouldn't be mad, atleast you changed your mind."
                                                    n "Let's just pretend this never happened."
                                                    n "Time to choose what you'd like once again."
                                                    $ Friet_not = 0
                                                    jump beach_friterieMenu
                                            
                        "I actually did.":
                            n "Ah I see, what a relief!"
                            $ Friet_not = 0
                            n "I'll return you to the moment you started ordering things, that way you can fix your mistake."
                            jump beach_friterieMenu
             
                   
            
            label beach_icecreamshop:
                    #TODO: convert all the below stuff to renpy
                    if beachturn >= 4:
                      
                        n "There seems to be no one at the icecream shop. (ufo panic, make your own ice)"
                    
                    $ beachturn += 1
                    jump icecreamSelection


            label icecreamSelection:
                $ icePicked = ""
              
                if ice == False:
                    $ icecream = 0
                    $ ice = True
                    n "You look at the many options and try to choose. ([persistent.date] chooses vanilla to test how good their ice is, like you tend to do.)"
                    l "I think I will pick two scoops of vanilla icecream, what are you choosing [persistent.name]?"
                menu:
                    "Move on" if icecream > 0:
                        jump Icecreamshop_moveOn
                      
                    "Vanilla.":
                        $ iceCreamPicked = "Vanilla"
                        jump iceCreamPicked
                    "Chocolate.":
                        $ iceCreamPicked = "Chocolate"
                        jump iceCreamPicked
                    "Strawberry.":
                        $ iceCreamPicked = "Strawberry"
                        jump iceCreamPicked
                
                label iceCreamPicked:
                    if icecream >= 3:
                        n "You already have enough icecream you absolute menace."
                  
                    else:
                        $ icecream += 1
                        if beachturn >= 4:
                            n "You take a scoop of [iceCreamPicked] icecream."
            
                        else:
                          
                            n "The friendly man gives you a scoop of [iceCreamPicked] icecream."
                          
                       
                  
                    label Icecreamshop_moveOn:
                        menu:
                            "Why did you just pick two scoops of just vanilla icecream?":
                     
                                l "I like to think I do it as a way to find out how good all the flavours taste."
                                l "Vanilla is by far the hardest flavour to mess up or to improve so if it tastes good or bad I can assume the other flavours are atleast the same quality."
                                n "[persistent.date] chuckles slightly."
                                l "But who knows? Maybe I just picked vanilla because it was a safe choice."
                        jump beach_start
                      
        label beach_cinema:
            if beachturn == 1:
                n "The hill ufo breaks through the screen. (All other rooms are locked of due to maintenance or something so you always die right now.)"
                jump gameOver
            elif beachturn > 1:
              
                n "The screen is completely broken but [persistent.date] and you pretend to watch a film."
                #TODO: REwrite and fill this out.
            
            elif beachturn == 0:
        
                n "[persistent.date] and you watch the movie. (return)"
          
            $ beacturn += 1
            
            
            jump beach_start
        
        label beach_seaDike:
         
            #TODO: "Add some events/deaths."
            if beachturn == 2:
                n "You can spot the hill ufo fly over to the dunes and shoot some strange purple beam into them."
            
            elif beachturn == 3:
                n "The sand begins to slide off the dunes as the earth shakes slightly, revealing metalic domes where the sand once was.<br/>The ufo's take off and begin flying around the coast."
            
            $ beachturn += 1
            menu: 
                "Walk on the left side of the sea dike.":
                    jump seaDike_left
                "Walk on the right side of the sea dike.":
                    jump seaDike_right
          
            label seaDike_left:
                n "The both of you are walking on the sea dike and watching the few people that come outside at this time and in the rain. (This dialogue needs some reworking.)"
                n "When [persistent.date] turns her head towards you, you see tears coming from her eyes."
                n "From your reaction [persistent.date] deduces that you can see the tears."
                l "Sorry [persistent.name], those tears have nothing to do with you."
                l "It's just that when I look at these people walking here I can't stop imagining what lives they could have."
                l "For some reason the lives that I give them are always better than mine."
                l "I know that I'm just comparing my life to made up and idealized lives but even than it still stings."
                l "It almost feels like my soul wants to rip out of me and follow anyone that isn't me and honestly, I wouldn't blame it."
                n "[persistent.date] wipes the tears out of her eyes and gives you a little smile."
                l "I should try to focus on reality, I'm here with you on a lovely trip to the beach. It may not be the absolutely perfect but nothing is and nothing can be. This moment with you is very good and that is absolutely perfect in it's own way."
                if persistent.beach_slipDeath == True:
                    jump seaDike_left_warnchoice
                else: 
                    jump seaDike_left_slipDeath
                label seaDike_left_warnchoice:
                    menu: 
                        "Continue walking towards where [persistent.date] will slip.":
                            jump seaDike_left_slipDeath
                        "Move slightly to the right.":
                            n "You walk slightly to the right  of where [persistent.date] would slip. (continue dialogue)"
                            menu: 
                                "Do you want a hug?":
                                    l "I'd like that [persistent.name]."
                                    #TODO: Add more dialogue and descriptions to this choice."
                            jump beach_start
               
                 
                n "A flower pot fell on her head, killing her."
                jump gameOver 
             
         
            label seaDike_right:
                #TODO: give this alternate text instead of the same text as walking left.
                if persistent.beach_potDeath == True:
                    jump seaDike_right_warnchoice
                else:
                    jump seaDike_right_potDeath
                label seaDike_right_warnchoice:
                    menu:
                        "Continue walking towards where the flower pot will fall.":
                            jump seaDike_right_potDeath
                        "Move slightly to the left.":
                            n "You walk slightly to the left of where the pot will fall, [persistent.date] follows you.<br/>Just at that moment the flower pot falls on the ground, shattering into quite a few pieces."
                            l "Luckily that didn't fall on me. (write more believable dialogue than this and continue this path.)"
               
              
           
                

label beach_waterPark:
  
    if keyGot == True:
    
        dev "For now you open the locker automatically, add an option to choose to do so."
        jump waterPark_openLocker
    
    else:
        if persistent.keyUnderBed_knowledge:
            d "You now know that the key fits this locker, atleast you can now pick it up."
            $ persistent.keyUse_knowledge = True
        else:
            n "Regular describing of the lockers and the waterpark."
                
              
          
      
        label waterPark_openLocker:
            # TODO: Make it possible to something else after reading the polaroids.
            n "On the inside of the locker is written:"
            n "\"Take a sip of the Lethe at the start of each one but find a way to remember the end of them.\""
            n "There are three polaroids in the locker, all of them feauture a massive tree as the sole object."
            menu:
                "Check polaroids.":
                    menu:
                        "Check polaroid 1.":
                            n "Your fond father called you Moonlight
                            and your mother named you Sunshine
                            and your brother, Sparkling Water
                            and your sister, Blue Broadcloth."
                            return

                        "Check polaroid 2.":
                            n "Float a day on easy wings to the temples of the moon,
                            on the next day you will pass by the shoulders of the Bear,
                            on the third day you will soar to the back of the Seven Stars"
                            return
                        "Check polaroid 3.":
                            n "He began to cut the salmon, slice the fish up with his knife.
                            Suddenly the beauty sprang and it flipped into the sea from the botttom of the red boat, from the boat of Väinämöinen.
                            And from there it raised its head and a smooth right shoulder lifted on the fifth gust of the wind and upon the sixth high roller.
                            Then it raised a right hand up and a left foot too appeared on the seventh billow's back riding on the ninth high roller.
                            Then it spoke in clear words and berated Väinämöinen:\"O you, you old Väinämöinen! I did not intend to come here to be sliced up for a salmon,
                            to serve myself as cuts of fish for your breakfast, morning snacks, salmon dinners or big suppers.
                            ...You had not the sense to hold me, Vellamo's young water maiden, Ahto's favourite, little Aino.\""
                            return
         