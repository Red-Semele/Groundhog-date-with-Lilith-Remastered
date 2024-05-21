#Put all the deaths in here as a way to clean up all the other files and also just make this way easier to find deaths to rewrite etc.





label restaurant_deaths:
    label restaurant_1:
        label restaurant_death_1:
            if burger == True:
                #Burgerscene here
                n "Now the screaming is also paired with hellish sounds, just great. You look at Lilith and tell her to hide under the table."
                l "I..."
                play music game_over #TODO: turning the music file into gog with "https://audio.online-convert.com/convert-to-ogg" made it work great, do this for all music files.
                n "Lilith seems to be frozen, on her face you can clearly see a mixture of fear and confusion. It takes you a moment to notice the steadily increasing red stains on Lilith's clothes."
                l "I've been shot?"
                n "She falls of her chair, you crawl towards her and try to call an ambulance."
                n "With trembling hands you type the emergency-number and beg for help."
                n "Everything seems to fade away, even the continuous  barage of gunshots, all you can hear is the sound of Lilith's breathing as it gets harder and harder for her to live."
                n "You've been here for what feels like aeons but in all reality was probably 5 minutes when an ambulance finally arives."
                n "A young man with eyes that have grown old from all the things they saw places Liliths still body on a stretcher and rushes off with it to the ambulance."
                n "The kind man throws some words at you, he tells you that everything will be just fine but you both know that he is lying. You have see her suffering for what seemed like an eternity and a second at the same time."
                n "You've gotten no clue what caused all those gunshots that inadvertently killed her. Some robbery in a neighbouring store, or a gang war, or something else."
                n "But sadly you do know what the aftermath of it all is."
                $ persistent.burger_death_1 = True
                jump gameOver

            elif cafe == True:
                #Cafescene here
                n "Suddenly you hear someone scream, you can turn your head just quick enough to see someone fall with a plate in their hands."
                n "The plate flies in the air, with it the ham sandwich that was put on top of it."
                n "You are apparently not the only one who has noticed, as you can see a beautiful blue marlin jump from an opening in the aquarium."
                n "The marlin has a long and pointy bill, it pierces the sandwich in a feat of pure dexterity. "
                n "Sadly it's traject leads right to Lilith's chest as it's sword-like bill pierces it, somehow you know it has pierced her heart aswell."
                n "She gives you one last look of utter shock before she falls dead on the floor."
                play music game_over
                $ persistent.cafe_death_1 = True
                jump gameOver




            elif chinese == True:
                #Chinesescene here
                if peking == True:
                    n "When the waitress arives with your double plates of Peking duck you and Lilith immediately dig in."
                else:
                    n "When the waitress arives with your orange chicken and Lilith's peking duck the two of you immediately dig in."

                n "She takes a break from her food and looks at you for a moment."
                l "You know, I'm actually glad we could meet here, I wanted to tell you something."
                n "Before Lilith can finish her sentence her face starts to swell."
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
                n "Lilith gives you a sceptical look but decides to follow your instructions, right as she does so a cacophony of hellish sounds begins to emanate through the halls of the mall."
                n " Knowing what is to come you try to pay attention to a specific sound, a gunshot is heard and a bullet flies where she would have been if you didn't warn her."
                n "Alright that is crazy, how did you know that bullet would hit me?"
            elif cafe == True:
                n "Lilith gives you a questioning look, as if she's trying to estimate if you are joking or not."
                l "Eventually she decides to not take any chances.
                She stands up and moves to your side of the table."
                l "So..."
                l "What is this all about [name]?"
                n "Before you can answer her question you hear someone scream again, that's the sign.
                You turn your head just quick enough to see someone fall with a plate in their hands."
                n "The plate flies in the air, with it the ham sandwich that was put on top of it."
                n "You are not the only one who has noticed, as you can see a beautiful blue marlin jump from an opening in the aquarium."
                n "The marlin has a long and pointy bill, it pierces the sandwich in a feat of pure dexterity. "
                n "It's current trajectory leads it to pierce through the chair where Lilith was sitting just mere moments ago."
                n "The staff quickly rush towards your table to take the marlin away and to see if it hasn't been hurt, they offer Lilith and you a short apology before disappearing."
                l "..."
                n "Lilith looks as if she has seen a ghost, if you hadn't intervened she may have seen her own."
                l "Alright, I'm trying my best to remain calm but how did you know that exact scenario would happen?"
            elif chinese == True:
                $ persistent.dumbo_knowledge = True
                l "I suppose that makes sense, I am allergic to quite a few things."
                l "When I was a kid I once ate a few peanuts while I was watching Dumbo, I felt my throat swell and I thought I was becoming a little elephant, just like Dumbo."
                l "I ran to my parents and said:\"Look mommy, look daddy! I can fly!\" and then I started using my hands to flap my ears around like Dumbo."
                l "At that point I was pretty swollen so it was a good thing my parents saw me, we went to the hospital as fast as we could and the kind doctors really helped me out."
                l "When I finally was allowed to go home from the hospital my parents gave me a Dumbo plushie to always remember the story."
                l "And I can say that I still remember it like it was yesterday,  the same counts  for my mom, she keeps joking about it to this day."
                n "Lilith  lets out a huge laugh as she looks at you."
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
                n "Suddenly a inmense sensation of pain overwhelms you, the only thing you can see is a glimpse of pure white and an eternity of black."
                n "When you awaken you find yourself surrounded by doctors, they tell you that with the force of sheer luck the stray bullet that would've hit Lilith managed to cause a gas leak."
                n "The gas explosion that followed was quite severe, you were in a coma and had to have your wounds cleaned with some surgical procedures."
                n "After a week you got out of your coma, Lilith however didn't have such luck."
                n "The doctors tell you that she atleast went out pretty quickly, almost like dying in your sleep but with more explosions."
                jump gameOver

            elif cafe == True:
                n "Suddenly you begin to hear the sound of shattering glass."
                n "As you turn to look at the source of the sound you can see that the aquarium next to where Lilith was sitting has shattered."
                n "The water is gushing out rapidly and it does not seem to be planning to stop."
                n "It seems as if somehow the marlin must have made a crack form."
                n "You think about the pure shenanigans that were needed to even make this exact thing happen but you are soon interrupted by the water flowing past your shoes with some fish coming along for the ride."
                l "Quick [name], we need to do something!"
                if persistent.cafe_death_2 == True:
                    n "You give Lilith a firm hug and tell her that there's nothing else you two can do except for waiting."
                    if lilithlike == True:
                        l "If I have to go now I atleast get some comfort out of the fact that you are here for me."
                        l "Goodbye [name], thank you for everything."
                        jump gameOver
                    else:
                        n "And so the both of you wait, in eachothers arms, for certain death. And it comes as expected."
                        jump gameOver
                else:
                    $ persistent.cafe_death_2 = True
                    n "You try to open the main exit of the restaurant but it doesn't seem to be giving in, almost as if something is blocking it."
                    n "Quick! Maybe we can still go to the first floor, we need to go higher!"
                    n "Pretty much without any other option you two decide to make a rush for the first floor of the restaurant.
                    When you turn around the corner you see that the stairs are blocked of by an extremely large closet made out of lignum vitae, you can not carry that, all you can do is admire the craftmanship."
                    n "You give Lilith a firm hug and tell her that there's nothing else you two can do except for waiting."
                    n "And so the both of you wait, in eachothers arms, for certain death.
                    And it surely came."
                    jump gameOver

            elif chinese == True:
                n "Suddenly you hear the faint sound of quacking."
                n "The sound of the quacking steadily grows louder and louder untill it's all you can hear."
                n "A true quackophony if you will."
                n "Lilith looks over your shoulder with a frightend look in her eyes."
                n "When you turn around you see a wave of angry geese breaking through the doors of the once cozy Chinese restaurant, the staff is running around in sheer panic."
                n "Before you can make another sound everything turns to white, the white of pesky geese feathers."
                n "The pain you are experiencing is too much and you fall unconscious."
                n "When you wake up again all the cutomers and staff have dissapeared, including Lilith."
                n "The room is completely filled to the brim with geese feathers, you begin to sneeze just thinking about that."
                n "While you are sneezing you notice that someone put a sticky note on your hand."
                n "It reads a as following: \"We took everyone and you won't be seeing them back, let this be a lesson on why you should not eat or serve geese or ducks, as those are also part of our family.
                - Sincerely, the geese\""
                $ persistent.chinese_death_2 = True
                jump gameOver
    label car_death:
        play music game_over
        if car_caught == True:
            "Filler for now..."
            #TODO: Fill in.
        else:
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
                    n "Lilith leaves the burger restaurant, you rush after her in an effort to calm her down.
                    This time there is no red Sedan in sight, it seems as if the cops handled it well."
                    n "However, just as you're processing that your mind wanders to the gas explosion that always appears arround this time." #TODO: (Different dialogue if they have never seen the gas-explosion) Is that even a possibility?
                    n "It was probably not a good idea to come here."
                    n "That is your last thought as you feel everything fade to black after you hear the expolosion."
                    #TODO: Should this move the player to the gasexplosion death with some minor changes? Probably yeah!
                    jump gameOver

                elif cafe == True:
                    n "Lilith leaves the burger restaurant, you rush after her in an effort to calm her down. "
                    n "When you set one foot outside of the doorframe a red Sedan drives head first into the both of you." #TODO: You know this red sedan, change the line to reflect that.
                    n "Luckily you managed to get flung to the side somehow. Lilith however was not so lucky."
                    n "She died on impact when the speeding car hit her."
                    n "Atleast the police showed up due to your call and locked the drunkard up." #TODO: Is this something that happens irl?
                    n "If only they managed to come a tiny bit earlier.
                    It was probably not the best idea to go here with Lilith when the car is still on the loose."
                    jump gameOver


                elif chinese == True:
                    n "Lilith leaves the chinese restaurant, you rush after her in an effort to calm her down.
                    This time there is no red Sedan in sight, it seems as if the cops handled it well." #TODO: Only make that line about the red sedan show up if you've seen her get hit by it here.
                    if AngryLilith == True:
                        l "Leave me alone [name]! I don't want to see you ever again!"
                    else:
                        l "Why are you following me [name]? I want to be alone." 
                    n "And with that Lilith leaves, you never saw her again. Not this time anyway. Atleast she didn't seem to get killed by anything on her way back home."
                    if AngryLilith == True:
                        n "You probably shouldn't have angered her so much."
                    else:
                        n "You should probably get her to trust you somehow." #TODO: Make this line more properly showcase what went wrong, were you silent to her, did you anger her etc.
                    jump gameOver



            else:
                if currentcar == True:
                    n "Lilith leaves the [resname], you can not bare seeing what happens next so you decide to stay inside.
                    Even from inside you can still hear the car crash into her."
                    #TODO:Account for the notangry flag in the original here:

                else:
                    $ currentcar = True
                    n "Lilith leaves the [resname], you rush after her in an effort to calm her down.
                    When you set one foot outside of the doorframe a red Sedan drives head first into the both of you."
                    n "Luckily you managed to get flung to the side somehow. Lilith however was not so lucky."
                    n "She died on impact when the speeding car hit her."
            jump gameOver

label kokiri_deaths:
    label kokiri_angryLilith:

        if major_love_offence >= 1:
            n "Lilith jumps up from where she was lying mere moments ago, on her face is a visible layer of anger or is it... disappointment?"
            n "You're not sure which one would sting more, probably a combination of the two."
            n "She wipes the crumbs on her clothes away with a frightening speed and angrily storms down the hill."
            l "Goodbye [name], we are done here."
            l "Do not come back for extra attempts if you have even the slightest slither of respect for me."
            #TODO: "Check if the player has retryed after she says not to."
        elif minor_love_offence > 1:
            n "Lilith stands up from where she was lying mere moments ago. You can clearly see a disappointed look on her face."
            l "This might all be a game for you [name], but for me this is very real."
            l "So I'd like to be treated with the respect you would give to a real person."
            l "You need to learn that your actions have consequences, even in something as simple as a game."
            l "I'm leaving now. Don't try to follow me, there's nothing you can say to me right now to change my mind."
            l "Besides, you can just retry right?"
            l "I'd prefer if you didn't, but I know I can't stop you."
            l "Let's just hope that when I meet you here once again during the next attempt you will have learnt your lesson."
            l "Goodbye [name]."
            n "Lilith turns away from you and walks down the hill cool and collected, it seems she has made up her mind about this."
        #TODO: I feel as if there should be a line here because otherwise the flow is weird.
        n "She doesn't get far from the hill, maybe a metre or fifteen before she seemingly trips over a tree root."
        n "She does not get up."
        play music game_over
        if persistent.kokiri_angryLilithDeath == False:
            n "When you rush to her you notice why."
            n "Lilith hit her head pretty badly on a small rock."
            n "The end result looks horifying."
            n "You call an ambulance but when they arrive they tell you what you already knew deep down."
            n "She didn't make it."
            $ persistent.kokiri_angryLilithDeath = True
        else:
            n "Deep down you already know it is too late."
            n "But you can't help yourself, you call an ambulance hoping that this time is somehow slightly different."
            n "That this time she is still alive by the time they arive."
            n "After what feels like waiting for years the ambulance finally arives."
            n "Sadly they tell you the same news they've already told you before."
            n "She didn't make it."
        jump gameOver

    label kokiri_1:
        label kokiri_death_1:
            if kokiri_call_death_1_check == True: #If she was calling her mom/sis during this death:
                #TODO: Make this also trigger a persistent death flag.
                n "The meteorite breaks into many different parts that spread all around the forest." #TODO: Add a few lines before this one to make the jump from her calling to this less sudden.
                n "One of them crashes straight against Lilith's head with a frightening impact."
                play music game_over
                n "Her head is cracked open and a puddle begins to form around it. Everything around you turns silent."
                if kokiri_chatchar_abigail_called == True:
                    n "Even Abigail who is currently screaming her lungs out has become unbearingly silent."
                else:
                    n "Even Lila who is currently screaming her lungs out has become unbearingly silent."   
                n "You would also like to scream but all that manages to come out is the same silence that seems to have taken over the forest."
                n "It's almost as if the forest itself is mourning her death."
                n "Some dark clouds move in front of the moon as if to stop it from revealing the state of Lilith's corpse."
                n "They are rather unsuccessful."
                n "Even if they had been succesful you are sure you still could see her body engraved in your eyelids."
                jump gameOver

            else:

                #TODO: Make this death instead break the meteorite and make them land on places where she gets hit.
                n "Lilith stops talking for a moment as she begins staring at the star-filled night, it seems like something has drawn her attention away from you."
                #TODO: This is an alternate line for if she's not talking to you: n "Lilith diverts her look from your eyes from a moment and continues watching the star-filled night." thzt line will see a lot less use than the others but just to be safe use it.
                n "A gasp of amazement escapes her mouth."
                l "You really need to see this, it's absolutely stunning!"
                n "The sky now is completly filled with falling stars, you've never seen so many falling stars in your entire life, let alone all together."
                n "However, one point seems to be getting bigger and bigger, it doesn't seem to be a star as it's not sending out any light."
                if kokiri_alternateplace == False:

                        n "The both of you watch in absolute terror as the thing only starts to get closer, becoming larger, in an alarming rate. "
                        play music game_over
                        n "Before you can move away the meteorite smashes Lilith like a newspaper would smash a fly, miraculously it didn't even hit you." #TODO: change this, make it so that the meteorite splinters and one piece hits Lilith.

                        $ persistent.kokiri_death_1 = True
                        jump gameOver

                else:
                        "The meteorite can't kill her because she is sitting somewhere else, FILLER"
                        #TODO: This part already exist somewhere in this game, I think it's based on calling someone or something? Probably try to search for this? Although there she is not aware of where it falls, so maybe write some slightly different text.

        label kokiri_death_1_prevented:
            #if kokiri_prevented == 1: This is code that would have made it so that it triggers based on 1-4 and the deaths.
                n "As she moves to the other side of the blanket, to your left, a meteorite crashes down just where she was sitting before." #TODO: Make it splinter and not land in one big clump.
                l "Sorry, I can't get used to all this death stuff, even when I know it's coming." #TODO: change this line slightly because it is very dumb.
                #TODO: Create a better segway between these two parts.
                if car_caught == False:
                    jump kokiri_death_2
                else:
                    jump kokiri_death_2_prevented
    label kokiri_2:
        label kokiri_death_2:
            play music game_over
            $ persistent.kokiri_death_2 = True
            if kokiri_alternateplace == True:
                if kokiri_call_death_2_check == True:
                    n "While Lilith is engrossed in her call you notice the Red-Sedan that rode up the hill and hit Lilith riding up the hill once again."
                #TODO: Add one line here for when she's not calling, maybe you see the car over her shoulder?
                n "You chuckle to yourself, you just prevented two deaths with one choice." #TODO: Only make this line play if you haven't seen the death with the car in the alternate location.
                n "That's not bad at all."
                n "And yet, as the car drives fully up the hill you notice something."
                n "The car turns around and comes towards Lilith and you with an even more frightening speed than it had on the hill."
                n "The car appears to have gained momentum from the down-ward slope of the hill."
                n "You don't have much time to think about this before it comes hurdling towards the two of you."
                n "You instinctively jump out of the way."
                n "Lilith however didn't manage that."
            else:
                n "Suddenly you notice a strange sound."
                n "A red sedan speeds towards the both of you with a frightening speed. Fight, flight or freeze. You have three options."
                n "You would like to think you would pick fight and push Lilith out of the way, somehow escaping at the same time."
                n "And yet you instinctively pick flight as you jump away from the car."
                n "Sadly it seems Lilith did not do the same, she instead froze."
                n "And now she is forever frozen as she lays there on the floor, unmoving."
            if kokiri_call_death_2_check == True:
                n "You call an ambulance with shaking hands as you hear screaming coming from her phone." #TODO: Narrate who this screaming is from etc.
            else:
                n "You call an ambulance with shaking hands."
            n "Your suspicion was proven true by the paramedics, she was dead as soon as that car hit her."
            if car_free == True:
                n "It appears calling the cops didn't accomplish much this time. Maybe you need to send them to another location?"
            jump gameOver

        label kokiri_death_2_prevented:
            n "You tell Lilith about how the red Sedan would've hit her if you wouldn't have called the police." #TODO Make that an optional choice and continue working from here.
            l "I see...
            Well thank you for going through such efforts to help me!"
            n "Lilith gives you a big smile, a look of gratitude is plastered across her face."
            menu:
                "I tried everything Lilith, I even took you to space but it didn't work out, no matter wich path I choose you still end up dying." if persistent.reality_knowledge:
                    jump kokiri_death_2_prevented_youDiedATon

                "Am I really helping you though? One of the things I saw while playing the game is that if we didn't date anymore you would keep being alive and find happiness with a nice guy called Ron." if persistent.ron_knowledge:
                    jump kokiri_death_2_prevented_youWereHappyWithRon

                "Am I really helping you though? It's true that I keep saving you but because of that you also keep dying. You've died [persistent.lildeaths] times now and I'm not sure how many more times I can see you die without breaking down entirely." if persistent.lildeaths > 9:
                    jump kokiri_death_2_prevented_youDiedATon

                "You are welcome Lilith, I'll try to get us out of this mess.":
                    l "And I just know that you will succeed, I got a good feeling about it."
                    #TODO: Add some more dialogue.
                    jump kokiri_pictureChoice

                "We're running out of time, can we please continue talking?":  #TODO:Change line slightly
                    jump kokiri_continue_talking
                    
label kokiri_death_2_prevented_triedEverything:
    p "I tried everything I could think of Lilith."
    p "I've fled from death with you, even going as far as flying away from the earth with a spaceship only for reality itself to collapse."
    if persistent.ron_knowledge == True:
        p "I might have been selfish, in one timeline you end up with a guy called Ron and you two just have a great time together."
        p "But that wasn't enough for me, I want to go on this date and have you come out of it alive and well."
    p "I just want to share a nice, enjoyable date with you."
    n "Lilith points at the village, the sun is setting once again." #TODO: Was the sun setting? What time is it in game?
    l "With such a marvelous view I would surely call this a nice, enjoyable date."
    n "She cuddles up to you."
    l "Thanks for going on this date with me! I'm having a really good time so far!"
    l "You know, I've been thinking..."
    l "If I'm going to die soon then what's stopping you from quitting this game? Or would I just lose consciousnes, like I'm dying?"
    l "I'm not sure if there's a way to tell. What do you think?"
    $ persistent.game_credits = True
    menu:
        "I believe that you would still live on.":
            l "That's rather reassuring."
            l "Since we're in a video game there's only so much dialogue I can tell you and only as many places we can go to as are programmed into it."
            l "But if you could break the boundaries through whatever creative outlet you have then there would essentially be thousands upon thousands of stories about us that you could give life. "
            l "The best part would be that you decide how they play out."
            l "She pauses for a moment and then continues."
            l "We tend to create these new worlds all the time, sometimes even without realising it.
            When you are thinking about what the next season of your favourite show will be about then you're technically creating an entire new world where the show's characters go through your story.
            And who's to say wich version is the superior one? Afterall, they're both telling a story, personally I think that's absolutely beautiful.
            So let's try to do just that!"
            n "Lilith hugs you for a long period of time, you feel her warmth as it reaches your cold body."
            n "And yet, it's not really your body, right?"
            n "More so the body you channel yourself through."
            n "Your avatar's body."
            n "There's a layer of separation you are trying so hard to ignore."
            n "But what if you didn't have to ignore it?"
            n "What if it wasn't there at all?"
            l "So... has it already happened? Are you now making our story?"
            menu:
                "No, we're still in the game.":
                    n "Lilith looks at you with a puzzled look on her face."
                    l "Oh... I thought you had already started. Why are you still playing this game instead of making your own story?"
                    menu:
                        "I just want to see what happens when I choose this path.":
                            n "It appears you got your wish, this path only leads to death. " #TODO: (connect it to the appropriate kak death) + write that line after the death itself. And maybe add some more text from nar.


                "Yes, I'm now in full control of it.":
                    n "Lilith gives you a warm embrace and jumps up in the air after she stops hugging you."
                    l "Perfect! So now we can just do whatever we want without having to fear being killed right?"
                    menu:
                        "Absolutely!":
                            n "Just as you said that something kills Lilith since you lied to her and were actually still in the game that has a habbit of killing her of." #TODO: Link to the right death and also change this line.

label kokiri_death_2_prevented_youWereHappyWithRon:

    l "Well, I am spending this moment with you, not with this \"Ron\"."
    n "Lilith places her hand on your arm and rubs it softly."
    l "It is sweet that you care about me enough to worry about those sorts of things but I would rather not have you worry about them."
    l "Besides, you made that version of me happy with Ron and now you've made this version of me very happy with you."
    n "She flashes you a knowing smile."
    l "If you ask me you have succeeded."
    jump kokiri_pictureChoice

label kokiri_death_2_prevented_youDiedATon:
    l "Oh, [name], it certainly has been a lot to wrap my head around  but I never had to constantly deal with this whole scenario like you. I truly suppose ignorance is bliss."
    l "I can completely understand that you are dealing with a lot throughout this whole thing. I really don't blame you for trying to keep coming back."
    l "You are just trying to find a way out and I'm sure you'll find it. Your intentions are pure."
    l "I don't blame you for anything [name], please don't blame yourself either."
    l "Afterall, is it worth it to live with me if you can't live with yourself?"
    #TODO: Add some more text?
    #Probably make her react more heavily when she is told this.
    jump kokiri_pictureChoice

label kokiri_pictureChoice:
    #TODO: Add a few different ways to be shown this picture, as it unlocks the beach.
    l "You know what? I want to show you something..."
    n "Lilith stands up from the blanket, some shards of the meteorite still laying on it and extends her hand to you."
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
    l "I still have Abigail and my mother of course, both of them are just so important to me and together we are trying to slowly but surely make new happy days."
    l "But anyway, what I'm trying to say is that you have something special, a way to prevent me from dying and a whole boat-load of determination."
    l "So don't feel guilty about your gift but use it to the fullest extent."
    #TODO: Make it so that you can tell Lilith she mentioned to use your gift to the fullest extent when she says not to involve her family.
    menu:
        "I will Lilith, I promise.":
            n "Lilith gives you a lovely smile."
            l "Give it your best shot"
            jump kokiri_death_3

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



                n "Suddenly the earth begins to shake, in a flash the big tree Lilith is standing next to topples over right on top of her."
                play music game_over
                n "The force of the tree kills her instantly." #TODO: (Write this more out)
                $ persistent.kokiri_death_3 = True
                jump gameOver
        label kokiri_death_3_prevented:
            l "Oh I see, so it's safer on this hill?"
            menu:
                "Yeah, atleast I think so." if not persistent.kokiri_death_4: #TODO: Maybe word this a bit differently.
                    jump kokiri_death_4_noDeath
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
            n "The ground begins to shake once again, this time it even shakes more than when Lilith showed you the picture. That's pretty strange considering it's the same earth-shaking."
            if kokiri_holdhand == True:
                jump kokiri_death_4_hill_dieTogether

            else:
                #TODO: Add the angry lilith flag and part. #kokiri_angryLilith #Make her not ask you for help but just accept her death.
                #The part below is not that part.
                l "What is happening [name]?"
                n "The fear in her voice is palpable."
                "Suddenly you feel the hill shooting upwards. The increased force of the gravity is pinning you against the hill but not for long, you begin to roll off the hill and fall down in the middle of a lake close to where the hill used to sit. "
                p "Lilith, it's safe in here, jump down!"
                l "I.... I can't... it's already too high..."
                n "She's right, you can barely hear her words anymore from that height."
                n "All you can do is float there, powerless, while you watch the hill and Lilith getting swallowed by the ink-black sky. As you do you notice that there are some sort of thrusters sticking out from the bottom of the hill." #TODO: other words for hill, find them.
                jump gameOver

        label kokiri_death_4_hill_dieTogether:
            l "Is this it, [name]?"
            n "You give a silent nod, as you do so you can feel her squeeze your hand even more as her's begins to tremble.
            Suddenly you feel the hill shooting upwards. The increased force of the gravity is pinning you against the hill but not for long, you begin start to slide off the hill."
            n "You would probably have fallen if Lilith wasn't holding your hand with all of her strength. She pulls you up slowly, while she does so she has to look down at the rapidly shrinking forest and you can see the fear in her eyes."
            l "Hold on [name], I got you and I'm not letting you go."
            l "{size=*0.5}Phew, we 're really high... I'm getting dizzy but I must keep going... just a little bit longer...{/size}"
            n "She has managed to pull you up but it costed a lot of her strength."
            n "The both of you flop down on the hill like a few moments ago, the only difference being that the hill is now soaring in the sky, oh and also that two of you are still holding hands."
            l "You know what's funny [name]?
            I felt more scared when I thought you were going to fall than I am now thinking about how I'm going to die.
            I suppose it's because if you fell I would have to go through this all alone."
            menu:
                "You won't have to do this alone, I'm with you.":
                    jump kokiri_death_4_hill_imWithYou
        label kokiri_death_4_hill_imWithYou:
            #TODO: Write some more text in between here.
            play music game_over
            l "You know, the stars are absolutely beautiful from here. I have a feeling we'll be able to see them even closer soon."
            n "Lilith shudders as she speaks those words but when you look at her she tries her best to give you a smile."
            n "Lilith was right, the hill flew up into space itself, probably to some far-off stars, not that the two of you would know as after fifteen seconds everything went black.
            You can only imagine the gruesome death the two of you suffered, that is if you weren't unconcious."
            $ persistent.kokiri_death_4_hill_holdHand = True
            jump gameOver
        label kokiri_death_4_noHill:
            play music game_over
            $ persistent.kokiri_death_4_noHill = True
            n "The earth begins shaking once again. The mechanical hill begins to ascend slowly, until it hovers above Lilith and you."
            n "A green pillar of light shoots out from inbetween the four thrusters at the bottom of the hill."
            n "The beam envelops the both of you and before you can do anything Lilith gets rapidly sucked into an opening of the hill that closes the moment she's inside. The hill begins ascending again, only this time much faster."
            n "All you can do is stand there, powerless, while you watch the hill and Lilith getting swallowed by the ink-black sky." #TODO: (Search other words for hill.)
            jump gameOver 












label beach_deaths:
    "Filler"
    #TODO: Put beach deaths here.

label other_deaths:
    "Filler"
    #TODO: Put all deaths that don't fit in the other categories here.
    label phone_untoldstory_planeDeath:

        
        n "Just as she says that you hear a deafening noise come from your phone.
        It sounds like a sharp whisteling" #TODO: (how does a planecrash sound? Maybe research this a bit to be more accurate.) Also, make the segway between this and the text below a bit better.
        play music game_over
        n "You try calling an ambulance to go to her house to make sure that she survives... "
        n "When the ambulance arrived there isn't much they could do, apparently a plane crashed on Lilith's house."

        n "Lilith has been living alone for a year or two now and she had no real neighbours, not any that weren't a few kilometres away from her atleast. Which means only her house got ruined by the plane."
        n "Sadly the same can't be said for both Lilith and most of the passengers of the plane..."

        n "There were luckily survivors of the plane crash, of the 139 people on board  86 people survived, most of them had minor injuries but where otherwise physically fine, if not mentally scarred."
        n "The event was all plastered over the news as soon as it happened, they followed it live as it (unfolded?)
        Lilith did not survive though, they had to remove the plane to even get to her body, the sight was horifying, they never mentioned what she looked like but you could hear it in their voice when they where on the phone."
        $ persistent.plane_knowledge = True
        jump gameOver

    label phone_planeDeath:
        $ persistent.plane_knowledge = True
        n "As Lilith hangs up her phone you turn on the tv in frustration."
        n "The news is on apparently, it's talking about a plane that had lost height just a moment ago"
        play music game_over
        n "The plane crashed right in the living room of a nice looking house, the house doesn't look unfamilliar to you at all."
        n "Then it hits you."
        n "It's her house."
        jump gameOver



label gameOver:
    if teaseDeath == True:
        if persistent.teaseDeath_fakeOut_knowledge == False:
            n "It seems like I was wrong when I said you won. Maybe an other approach would work?"
            $ persistent.teaseDeath_fakeOut_knowledge = True
    
    $ persistent.lildeaths += 1
    $ persistent.retry_counter += 1
    n "{size=*2.5}Game over{/size}"
    n "Your date surely didn't go as planned."
    #TODO: Change the retry prompt based on wheter or not Lilith is alive. If she is alive, then why did you retry afterall? Make it then be "Retry?"
    play music sunrise
    menu :
        "Retry.":
            jump game_start
