#TODO: Add the rest of the kokiri part here, including the nightmare. also put in the additional stuff you put in the quest version like the ability to talk about other things.

label kokiri_start:
    n "Lilith gasps for a second."
    l "You mean the Kokiri woods? The same as I am thinking of right now?"
    l "You know what, let's both go to the Kokiri woods, if we are at the same spot then I'll know for sure."
    l "While you're at it, try taking some food you got laying around your house with you, we can make a picknick date out of it!"
    n "Lilith giggles."
    l "This is all pretty strange but see you there! Or so I hope..."
    n "Lilith hangs up the phone and you immediatly start seeking every nook and cranny of your house for something that would make for good food on a picknick."
    l "When you're done you drive to the Kokiri woods, hoping that things will be different there.
    You arrive in the woods."
    #TODO: Add the nightmare code in between here, base yourself of the burger nightmare code to do this.
    if persistent.kokiri_meteoritedistraction_knowledge == True:
        menu:
            "*Go sit on the hill where you normally sit.*":
                jump kokiri_hillsit
            "*Pick a different place to slightly prevent the distraction of the meteorite.*":
                jump kokiri_altsit
    else:
        jump kokiri_hillsit

label kokiri_hillsit:
    n "The woods are located on top of a hill, from where you are now standing you can see most of the village where all your past dates took place."
    l "Oh hey, I see you already found this place, it has a really great view. Nice work [name]!"
    n "Lilith gives you a playful pat on the back as she places her picknick blanket down on the ground."
    n "The both of you start placing down all the food on the blanket, when you're both finished you sit down on it."
    l "You know, this is really a beautiful view of the village we've got from here..."
    l "But how did you know about this place? I always gave it that name when I was a kid but I never told anyone."
    l "What's all of this about?"
    play music "starsintheforest.mp3"
    jump kokiri_explanation

label kokiri_altsit:
    $ kokiri_alternateplace = True
    n "Just as you stand there looking around for a decent alternate spot to sit at you notice Lilith.
    Since she practically grew up in these woods you decide it might be a good idea to ask her for a decent spot to have your picknick with her.

    She first suggests the hill but you shake your head and tell her that she will soon understand why that might not be the best idea."
    l "Well, that one spot over there is also a good spot to sit, we just won't have a view overlooking the town as the hill kind of blocks it.

    But that doesn't mean we can't have a good time, right?" #TODO: (Mention some small trees as they are going to tople over on her in the cardeath)
    n "She chuckles but the chuckles have a slight nervosity to them, which is very understandable giving the current situation."
    n "You and Lilith walk over to the spot she pointed at and place the picknick-blanket on the ground. And the two of you begin to place all kinds of food on it." #TODO: (Make a foodplacing scene for both this and the normal place.)
    l "You know, I'm really glad to be back here.."
    l "But how did you know about this place? I always gave it that name when I was a kid but I never told anyone."
    l "What's all of this about?"
    play music "starsintheforest.mp3"
    jump kokiri_explanation

label kokiri_explanation:
    menu:

        "I'm in some sort of groundhog day scenario, a groundhog date if you will." if not kokiri_groundhog_lie:
            jump kokiri_explanation_groundhog

        "I'm psychic, I can predict things like Kokiri woods." if not kokiri_psychic_lie:
            jump kokiri_explanation_psychic

        "You're part of a game, I've been on many dates with you in other playthroughs of this game.":
            jump kokiri_explanation_game

label kokiri_explanation_groundhog:
    $ kokiri_groundhog_lie = True
    n "Lilith watches you with a sceptic look in her eyes."
    l "You know, when you told me that story over the phone I might have believed you but now I somehow can tell you're not telling the truth if that makes sense."
    l "So what is this all really about?"
    jump kokiri_explanation
label kokiri_explanation_psychic:
    $ kokiri_psychic_lie = True
    n "Lilith watches you with a sceptic look in her eyes."
    l "You know, when you told me that story over the phone I might have believed you but now I somehow can tell you're not telling the truth if that makes sense."
    l "So what is this all really about?"
    jump kokiri_explanation
label kokiri_explanation_game:
    n "Lilith shifts her position for a moment and gives you an honest smile."
    l "That actually makes quite a bit of sense, It wouldn't be too impossible to make a game and let every character in it believe that they are real, in fact that's most games isn't it?"
    l "Most characters never break forth walls, nowadays it seems to be more and more popular but most game designers try to not make the experience shatter your immersion too much."
    l "So, are you the one who is playing this game?"
    menu:
        "I am, however I can't say whatever I want, I can only speak with you through these clickable links that have a preview of what I'm going to say. So in a sense I guess I'm not really playing this game, not the me you know anyway.":
            n "Lilith scratches her head as if she is trying to comprehend what you are saying."
            l "So, what you are saying is that the you I'm seeing in front of me isn't the real you but some sort of \"filtered\" version because of restrictions in what you can tell me?"
            l "So, for example, is [name] even your real name?"
            menu:

                "Yup, that's my real name.":
                    "Filler"
                    #TODO: Fill this out (No quest precedent)


                "No, that's not my real name.":
                    label kokiri_explanation_game_notrealname:
                        if norealname == 0:
                          $ conversationtracker_norealname = True
                          $ kokiri_norealname = 1
                          $ kokiri_realname = True
                          l "Oh, so what is your real name then?" #TODO: Change this line up slightly.
                          $ name_real = renpy.input("What is your real name?")
                          $  name_real = name_real.strip() or "Max"
                          $ name_real = name_real.capitalize()
                          l "Well, it's nice to finally meet you for real [name_real]!"
                          l "Lilith gives you a big smile."
                          l "Although, haven't I met you for real already?"
                          l "After all, even if you had a fake name, you still are the one who is in control of [name]."
                          l "So, the way how you treated me on this date and on the previous ones is still a reflection of you as a real person."
                          l "It all means something, even if you didn't think it did."
                          l "Even if you did something to just have fun in a videogame or to see what it would do, that still says something about you as a person."
                          l "Sometimes we hide behind the roles we play to make actions that would not be acceptable to ourselves and others if our true self would make them."
                          l "That's why it might feel scary to some if they catch a glimpse of themselves in the reflection of their screen. Because it's someone they don't recognise.<br/>Do you ever feel like that, {player.real}?..."
                          l "All these different roles form a web of half-truths and lies, and in the center of it all you can find our true self."
                          l "Not the self we think we are, not the self others see us as, but the self we inevitably are."
                          l "Speaking about that self, what do you really do for a living? I'd like to get to know you better, the one playing this game."
                          #TODO: Get input via box and check if it contains the word "teach"
                          #If it does:
                          l "Ah so you are also a teacher? That's really cool! "
                          #TODO: Add some more dialogue.
                          #If it doesn't:
                          l "Ah so you [player_job] for a living? That's interesting!" #TODO: Use player_job in that input box.
                          l "Have I ever mentioned what I do for a living? "
                          menu:
                                "No, not yet.":
                                    $ persistent.kokiri_teacher_knowledge = True
                                    l "I actually teach the first year of our town's elementary school."
                                    l "I just love working with those kids and helping them out as best as I can."
                                    #TODO: Go a bit more indepth on this.
                                    menu:
                                        "That's really cool!":
                                            #TODO: That's kind of a weird reaction.
                                            l "Thanks, [name_real]!"
                                            #TODO: Probably scrap this choice or heavily rework it. Instead I think a better choice would be to ask her what she likes about working with the kids.
                                            #Fill out a bit more.

                                "You have mentioned you teach the first year of elementary when we had this talk before actually." if persistent.kokiri_teacher_knowledge:
                                    l "Oh I see, so you have already spoken to me here?" #TODO: Change this line slightly.
                                    #TODO: Make this an alternate way to talk about her not being the same etc, there is already a label in the game like that, just jump to that one. (If it is not yet in the game it IS in the quest version)
                                    #It's the one that mentions Heraclitus Iirc
                        else:
                          $ kokiri_norealname += 1
                          if kokiri_norealname == 2:
                              "Filler"
                              #TODO: Fill in with the second part.
                          else:
                              "Filler"
                              #TODO: This is room for a pottential third part.

                "Can we actually talk about something else? ":
                    "Filler"
                    #TODO: Fix the filler, make her say something.
                    jump kokiri_talkaboutsomethingelse





        "Yup, I am the one who is playing it.":
            jump kokiri_explanation_game_playeridentity






label kokiri_explanation_game_playeridentity:
    l "It's pretty strange to be told that you're in a game but I'm glad you are the player, you seem more than capable enough to do what you need to do."
    if kokiri_psychic_lie or kokiri_groundhog_lie == True:
        l "Although I'd like to ask you to not lie to me too much alright? Only if it is absolutely necessary and even then I won't be a fan of it happening."
        l "We are in this together, and together we will try to achieve our goal!"
        $ persistent.kokiri_tellnolies_knowledge = True
    #TODO: Make her say that an example of how capable you are is you knowing about the kokiri forest.
    l "She pauses for a moment and then continues."
    n "Now that I think about it, what is it you've got to do in this game?"
    $ kokiri_path1 = True
    $ kokiri_conversation = 0
    menu:

        "Actually, in the Chinese restaurant you told me that your sister makes games using a program called Quest to make text-heavy games. This game's prototype also used that program although the version I am playing uses a different one." if persistent.quest_knowledge:
            #TODO: Maybe change the placement of this link slightly, it feels weird to be here.
            jump kokiri_topic_questmade



        "I think the goal is...":
            menu:
                    "I think the goal is to go on a succesful date with you.":
                        $ kokiri_conversation += 1
                        l "Well, what do you mean with a \"succesful\" date?"
                        menu:
                            "A date where you survive.":
                                jump kokiri_gamegoal_succesful_survive

                            "I think the game decides whether it is a succesful date or not.":
                                jump kokiri_gamegoal_succesful_gamedecides


                            "I do not know.":
                                jump kokiri_gamegoal_succesful_Idonotknow



                    "I think the goal is to reach an ending where you live.":
                        $ kokiri_conversation += 1
                        "Filler."
                        #TODO: Fill in (There is no quest precedent for this.) Make it be about what "an ending" looks like, can Lilith make endings? Can you?
                    "I think the goal is to make my own version of this game through a medium of my own somehow.": #TODO: (Make this pop-up once Lilith suggests it.)
                        $ kokiri_conversation += 1
                        l "I see..."
                        n "Lilith scratches her chin, she seems to be deep in thought for a moment."
                        l "That actually is quite a good idea."
                        l "I've been thinking about something like this for quite a while."
                        l "If you read a book, close it halfway and make up your own story, is it any less valid than the original?"
                        menu:
                            "I think it would be equally valid.":
                                #TODO: Rewrite this text slightly.
                                l "Exactly, and that's why creating your own version of this game could be really interesting. You can take the elements you like and put your own spin on it."
                                l "So, do you have any ideas on how you want to approach this? How would you create your own version of this world?"
                                menu:
                                    "Make my own game.":
                                        l "I'd love to see that!"
                                        l "I really enjoy playing games, lately I haven't had too much time since I'm constantly busy grading the tests of my students."
                                        l "I do try to take some time of for myself though, so don't worry about that. Otherwise I wouldn't be here, would I?"
                                        l "I've been playtesting a lot of my sister's games though! They are fairly short and purely textbased."
                                        l "Something like that would probably be pretty easy to make if you wanted to make your own game, atleast it would be easier than the other options."
                                        l "Although I can imagine the writing could be a bit hard, just thinking about how the game we are currently in is working is making my head hurt slightly."
                                        $ kokiri_scenery_headhurt = True
                                        #TODO: Fill out a bit more.
                                        jump kokiri_scenery_choice

                                    "Use another medium to make my own version.":
                                        l "What would you want the story to be like?"
                                        l "Actually, don't tell me, I'd much rather see it for myself once you created that world. That way it will be a suprise."
                                        #TODO: Fill out more.
                                        jump kokiri_scenery_choice

                                    "Come up with my own story in my head.":
                                        "Filler"
                                        #TODO: Create this text (no quest precedent).
                                        jump kokiri_scenery_choice

                            "I think it would be less valid. The story you would make is not intended by the author.":
                                l "And what if it was?"
                                l "What if somehow, after you made up the entire half of the story, it was exactly what the author wrote?"
                                l "So theoretically speaking, out of infinite imaginings of the story atleast one will be the one the author intended."
                                l "I would argue that probably quite a few more of them would be author-intended since the reader has read half of the book.
                                Because of that you can better understand the logic of the world the writer created.
                                So you can make a few estimated guesses about how it all would go.
                                Sure, depending on the complexity of the story you might not be able to interweave the new elements the author would but you'd still be able to get the same end result."
                                l "But even if you wouldn't abide by the same logic as the author themselves, does that make your new story any less valid?"
                                l "An action needs observers to become real. Without something it can impact it practically doesn't exist."
                                l "A writer needs readers to read his stories as much as the readers need him to write those stories."
                                l "A storyteller needs an audience to be heard and the audience needs someone to listen to."
                                l "You can become both the action and the observer, the writer and the reader, the storyteller and the audience.
                                That way you don't have to read the story the author wrote, you can just become your own author."
                                l "If you want to make it so that a murder mystery suddenly turns into a sci-fi story about a monkey with a talking banana than you can do that."
                                l "You have taken over the role of storyteller so you can create whatever nonsense you want and it is justified in it's creation as long as you also listen to your story."
                                l "Sorry if I've been rambling too much about this [name], this just something that really intrigues me!"
                                l "Maybe you should let my words sink in a bit, they can be quite much, especially if you never thought about this sort of stuff before."
                                $ kokiri_scenery_breakfrombreakingyourhead = True

                                jump kokiri_scenery_choice


        "I don't  think there is a goal, not a true one anyway.":
            jump kokiri_gamegoal_nogoal


        "I actually have no idea.":
            jump kokiri_gamegoal_noidea

        "Actually I want to talk about something else.":
            jump kokiri_talkaboutsomethingelse

label kokiri_topic_questmade:
    $ kokiri_conversation += 1
    if conversationtracker_questmade == False:
        $ conversationtracker_questmade = True
        $ questmade = 1
        l "Oh wow..."
        n "Lilith seems lost in thought for a moment before she continues."
        l "Theoretically speaking the game your playing right now could even exist in my world... that's a really strange idea to wrap your head around"
        jump kokiri_scenery_choice
    else:
        $ questmade += 1
        if questmade == 2:
            "Placeholder"
            #TODO: Fill in.
        elif questmade == 3:
            "Placeholder"
            #TODO: Fill in.

label kokiri_gamegoal_nogoal:
    $ kokiri_conversation += 1
    l "Lilith chuckles."
    l "So sort of like life in general?"
    l "I mean, I might not be the best person to make this comparison since I'm not entirely sure wether I am alive or not due to me being in a game, I feel alive for what it's worth."
    l "But anyway, from my potentially flawed point of view our very existence is absurd."
    l "Born without objective purpose and gone before we recieve one, a joke without a punchline."
    l "Maybe this existence is the punchline? "
    l "Maybe we aren't the ones supposed to laugh?"
    l "We can only pretend that we got the joke and feign a smile."
    n "Wow, where did that suddenly come from?"
    l "Lilith notices you being absolutely flabergasted by her mini-monologue."
    l "But that doesn't mean there is no hope at all [name]!"
    l "We can create our own subjective purpose to compensate the lack of an objective one."
    l "We exists to help our family, friends and loved ones.
    To be able to experience the small joys in life like a warm hug, a good book or a eating some cheese while still being in your bed."
    l "We exist because we already existed so we might aswell keep going at it, right?"
    l "And even if the universe doesn't care about us, even if we are unfathomably small in it's eyes, we care about eachother and in our eyes we are unfathomably large."
    l "Maybe that is the purpose of this game? To show you that it is possible to make your own purpose?"
    #TODO: add some extra text.
    jump kokiri_scenery_choice

label kokiri_gamegoal_noidea:
    $ kokiri_conversation += 1
    l "That's fine, we can figure your goal out together."
    n "Lilith scratches her chin and continues."
    l "Let's see, first of, how does this game look to you?"
    menu:
        "I just see text on the screen and some graphics, your text is a different color from the narrator's. I also get a few clickable links to select what I want to say.":
            #TODO: This link is not entirely true anymore, change that text eventually.
            jump kokiri_gamegoal_noidea_howgamelooks
label kokiri_gamegoal_noidea_howgamelooks:
    l "Ah I see, so you can't see the absolutely stunning view from our picknickspot?"
    menu:
        "Yup, the best thing I can get is a description of it if the game feels like giving me one. Otherwise I just see a fixed point, as if our conversation is filmed with a static camera.":
            $ kokiri_scenery_gamegoal = True

            jump kokiri_scenery_choice
label kokiri_gamegoal_succesful_survive:
    n "Lilith bursts out in laughter."
    l "I suppose that might be a good definition for a succesful date but I think you might have put the bar pretty low [name]."
    l "For what it's worth, I think this date is really lovely! Although my head still hurts from trying to fully comprehend what's going on.
    Atleast it's a different kind of pain than the one I get from constantly having to grade my student's tests, so there's that."
    n "Lilith lets out a hearthy chuckle, not much later she seems to be lost in thought."
    l "You know, what you just said is quite interesting."
    l "So a \"succesful\" date would be one where I don't end up dying, right?"
    l "And what if we never went on a date at all?"
    l "Would that keep me alive?"
    l "And if it did, would you consider that a succes?"
    #TODO: Add some choices here, one of them has the potential to make Lilith mad because you value her life less than her being with you. After the choices move to the scenery choice.
    jump kokiri_scenery_choice
label kokiri_gamegoal_succesful_gamedecides:
    l "So you are going to take some game's word for it? Aren't you able to tell whether or not a date is succesful based on your own feelings?"
    n "Lilith grows quiet for a moment before she continues."
    l "You know, I don't need a game to tell me that this is a good date [name]."
    l "It might be far from what I expected but that makes it so much more unique."
    l "You took me away from my own mind, even if it's just for a short moment."
    l "I haven't been in the..."
    l "brightest place lately."
    l "To tell you the truth, I have thought about joining James a few times..." #TODO: Does the player know about James at this point?
    l "But I don't want you to worry about me [name], I might have been in a dark place but I was working on myself."
    l "I fought the thoughts with all I had, I gave myself reasons to keep existing."
    l "At first it was for the poems I would write, I didn't want to vanish and leave a poem in a half-written state."
    l "I wrote half a poem for about two whole years, that way I had something anchoring me to this world."
    l "Lilith chuckles uncomfortably."
    l "I hated prolonging my poems like that just to have an excuse."
    l "I never got any work done, it made me feel terrible."
    l "So, after a while I started to live for Lilith and for my mom."
    l "They needed me, now more than ever and if I were to vanish they would be devasted."
    l "It's only recently that I started living for myself again. That I wanted to enjoy things again."
    l "It's been about two years since then, I'm still not entirely healed but I'm trying my best."
    l "So, I don't want you to worry about me alright? I'm alright all things considered."
    l "The best way you can help me is to just enjoy this moment with me."
    #TODO: Write this a bit better and more tasteful.
    jump kokiri_scenery_choice
label kokiri_gamegoal_succesful_Idonotknow:
    l "Well, for whatever it is worth, I think this is a succesful date [name]!"
    n "Lilith gives you a cute smile."
    l "It might not entirely be what I expected but it sure is a nice date."
    menu:
        "I also think this is a nice date Lilith.":
            n "Lilith lets out a small laugh."
            l "I think my heart just jumped a little hearing you say that [name]."
            l "You know, even after everything I went through, after all the self-reflection I did, I still have this part of me that finds it hard to believe that people could like me."
            l "I, or atleast that part of me still need to get used to that idea."
            l "But, enough about that, you being here is helping me a lot!"
            l "Would you like to shut up that part of me and watch the scenery with me?" #TODO: Move this part to the scenery choice as a sort of alternate line if the player jumped from here. (You will need a flag that's set here)
            #TODO: (Add an option to tell her she's enough if you decline to watch the scenery.)
            jump kokiri_scenery_choice


        "Every date with you is a nice date, I'll cherish them all forever.":
            l "Oh right, for a moment I almost forgot we had multiple dates already from your point of view."
            l "It's kind of hard to wrap my head around but oddly... comforting?"
            l "The idea that you keep coming back for me, that must mean you atleast like me enough to do so."
            l "My brain does not have to constantly doubt wether you like me or not because of the idea that we had multiple dates already."
            l "Sure, most of them end up with me dying but let's just hope that this one doesn't."
            l "But oh wel, I suppose this view is to die for."
            l "Lilith chuckles, but in her eyes you can catch a brief glimpse of fear in her eyes.
            As she looks you into the eyes you can see that fear slowly fade away."
            #TODO: Write this out a bit more. (Add some extra parts of the monologue.)
            jump kokiri_scenery_choice







label kokiri_scenery:
    if persistent.tracker == 3:
        $ tracker3 = True
    n "From the spot you picked on the hill you have a gorgeous view of the village where most of your dates with Lilith took place."
    n "It's pretty calm in the village, here and there you might catch a rare glimpse of a car or a pedestrian but other than that the streets are completly empty."
    l "This view is absolutely fantastic isn't it?"
    l "When my parents used to take walks with me and my brother in this forrest I knew that I just had to keep coming back here."
    l "And I did! Many times actually. I like to come here whenever I have some spare time or when I really need to get some time away from things."
    l "The sunrise here is absolutely beautiful, maybe we'll be able to share that moment today."
    l "I'd like that..."
    n "As you enjoy eachother's company for a while while looking off into the distance the both of you spot a red Sedan as it drives closer and closer to the cafe at troubling speeds."
    if car_caught == False:
        n "When the car reaches the cafe it rams a garbage container that falls over in front of the doors and drives up on a ramp. It launches itself over the building, coming back the other way and driving away like nothing happened."
        n "After a short while the car speeds straight into the doors of the Chinese restaurant for it's second act of pure destruction."
        n "The car backs away from the Chinese restaurant to speed to it's next destination."



    else:
        n "When the car reaches the cafe it rams a garbage container that falls over in front of the doors and the Sedan drives towards a convieniently placed ramp."
        n "Just before it manages to reach the ramp a copcar drives in front of it, forcing the driver to stop."
        n "After some questioning and an alchohol test the police put the man in their car and drive off with him."

    n "Not much later a swarm of geese break the doors of the restaurant wide open and dash inside."
    #TODO: Do the geese come from the rampage of animals when you flee?
    n "As fast as they entered the restaurant they leave it with practically everyone in the restaurant being kidnapped by them."
    #TODO: Make Lilith kind of find it strange that this is happening with the geese.

    n "Suddenly you can hear the sound of sirens, of police sirens."
    n "The police sirens are coming from near the mall, where the burger restaurant is located."
    n "The same restaurant where Lilith got shot..."
    n "You point at the mall and tell her about the events that took place there."
    n "She gasps for a moment."
    l "Sorry, I know that you relived many scenarios like the one you just mentioned and that I have no memory of those scenarios but it will still take some getting used to the idea." #TODO: change this line slightly because it's dumb.
    n "In it's final act of destruction the car races at full speed and smashs against the entrance of the mall."
    n "The burger restaurant explodes due to the gasexplosion, taking a sizeable chunk of the mall with it. However the Sudan escapes without a scratch. After the explosion the village begins to turn calm once more, the whole ordeal seems to have finally ended."
    l "Has it... Has it ended?"
    menu:
        "Yes, it's finally all over.":
            jump kokiri_scenery_allover
        "Not quite. You might want to sit on my right instead of my left." if persistent.kokiri_death_1:
            jump kokiri_death_1_prevented

label kokiri_poems:
     #TODO: Put an option for the newest and more challenging poems of mine in here.
     #TODO: Once all poems have been read make the player able to ask for some more to which Lilith will decline if they've seen all the poems including the newer stuff. Otherwise she will suggest some of the newer stuff.
     n "She gives you the pug-notebook with the poems, you can pick one and ask some questions about it."
     #TODO: Change that line slightly.
     #Make it so that the normal poems are one menu and the harder ones are an additional menu, that way I can re-use the normal menu if I have to choose between normal and hard.

     #TODO: Fill in more and check if this works.
     if poem_conversation == True:
         $ poem_conversation = False
     $ kokiri_conversation += 1

     if persistent.kokiri_newerpoems_knowledge == True:
         menu:
             "Read one of Lilith's older poems.":
                 jump kokiri_poems_oldpoems
             "Read one of Lilith's more recent poems.":
                 jump kokiri_poems_oldpoems
     else:
         jump kokiri_poems_oldpoems
label kokiri_poems_oldpoems:
    menu:
        "Read snowwoman poem.":
            jump kokiri_poems_oldpoems_snowwoman
        "Read window poem.":
            jump kokiri_poems_oldpoems_window
        "Read shadowman poem.":
            jump kokiri_poems_oldpoems_shadowman
        "Read lights poem.":
            jump kokiri_poems_oldpoems_lights
        "Read bang poem.":
            jump kokiri_poems_oldpoems_bang

label kokiri_poems_oldpoems_snowwoman:
    $ persistent.kokiri_poem_snowwoman_knowledge = True
    $ conversationtracker_poem_snowwoman = True
    $ kokiri_poem_snowwoman_recent = True
    l "I am sitting against a locked door.
    I don't have the key aymore."
    l "I am freezing to death.
    Trying to keep myself warm with my breath."
    l "What I wouldn’t do to get inside
    Cold tears I cried."
    l "I am falling in the snow.
    The icy wind continues to blow."
    l "I see the fire flickering red,
    The fire that led to my death"
    l "The snow covers my carcas,
    the snow erases who I was."
    l "Now I’m dreaming about that unreachable fire.
    That is the only thing I desire."
    l "So close yet so far
    from that fire flickering like a star."
    l "I wasn't much but I became less than.
    I died and I  became a snowwoman."
    jump kokiri_poems_askorrate

label kokiri_poems_oldpoems_window:
    $ persistent.kokiri_poem_window_knowledge = True
    $ conversationtracker_poem_window = True
    $ kokiri_poem_window_recent = True
    l "Windows of the soul,"
    l "Reflect like mirrors,"
    l "All the pain, the lies,"
    l "Of lost shadows on the street,"
    l "That fall in the darkness without moon."
    l "Their thoughts carved into the silenced stone."
    l "Sometimes a little bit of light appears,"
    l "A star in their eyes,"
    l "But the light drowns in their tears"
    l "And then they stumble through their starless night."
    l "Hollow carcasses that got scraped empty slowly."
    l "Waiting untill time dissolves their bodies."
    l "Their eyes closed to run from the reflection."
    l "An unspoken truth rests on their lips"
    l "They tumble deeper into this nightmare"
    l "With no beginning, with no end"
    l "But still they laugh their empty smiles"
    l "Speak their meaningless words of hope"
    l "Their eyes closed to keep the pain inside."
    l "Hoping to one day wake up,"
    l "To open their eyes."
    jump kokiri_poems_askorrate

label kokiri_poems_oldpoems_shadowman:
    $ persistent.kokiri_poem_shadowman_knowledge = True
    $ conversationtracker_poem_shadowman = True
    $ kokiri_poem_shadowman_recent = True
    l "In the beginning there was nothing but darkness."
    l "Then there was family, love, light, us."
    l "And the darkness seemed to not exist for a moment."
    l "It waited patiently with a grin on their face like a child playing hide and seek."
    l "The darkness gradually grew stronger until it no longer needed the light, until it could displace that gentle glow, until it could steal you."
    l "And with you it stole family, love, light, us."
    l "I look in the mirror and don't recognize myself anymore, I'm made of your shadow, which I wear like an unremovable mourning dress."
    l "I stare into the eyes of the mechanical light that formed your last shadow and by a trick of the light it’s almost as if you’re waving to me from an impossible distance."
    l "But every time I wave back you vanish once more, we can never truly see each other again but atleast I still have your shadow wrapped around me. Because even a reminder of your absence is better than no reminder of you at all."
    jump kokiri_poems_askorrate

label kokiri_poems_oldpoems_lights:
    $ persistent.kokiri_poem_lights_knowledge = True
    $ conversationtracker_poem_lights = True
    $ kokiri_poem_lights_recent = True
    l "Turn the lights off, close the door.
    No, I can’t do it anymore."
    l "Let me rot in this darkness
    Leave me alone in this madness"
    l "Don’t let the darkness escape.
    Don’t let my thoughts take shape"
    l "Let the ghost fight her ghosts.
    Leave the host to her hosts."
    l "Leave the echo with the voices
    Leave the silence with the noises."
    l "Leave my darkened mind in the dark.
    Leave the fish with the shark."
    l "Voices whispering from the dark.
    Trying to erase my small spark."
    l "Invisible hands let me drown in ink.
    I can’t stop this no matter what I think."
    l "Leave me to suffer.
    Leave me to me, the duffer."
    l "Leave me alone in here.
    You can't fight my fear."
    l "Leave me alone.
    Leave the sculptor with her stone."
    jump kokiri_poems_askorrate


label kokiri_poems_oldpoems_bang:
    $ persistent.kokiri_poem_bang_knowledge = True
    $ conversationtracker_poem_bang = True
    $ kokiri_poem_bang_recent = True
    #TODO: Format this better.
    l "A bang, to keep me awake
    A mix of rust and salt on my tongue
    Deep cut my broken dreams
    in the skin of an idiot
    It still rings in my ears"
    l "The reality is breaking
    I still can not understand it
    A lie and still the truth"
    l "Time seems to stand still
    And yet I do not get any younger
    But also not smarter
    Just more of myself and then less"
    l "Because everything finally falls down,
    The leaves of a proud tree,
    The feathers of lost birds,
    My life."
    l "It is the law of gravity
    Who laughs with us,
    Who raised us."
    l "The really much too heavy force.
    Who slowly slaughter us,
    Who slowly laughs at us,
    Who is waiting for us."
    l "Constantly day and night
    We push our whole life against a gigantic boulder on our hill and when we are at the top it slowly rolls to the other side.
    I try to be smarter, different than they are."
    l "But that makes me exactly like them. My other me blames me every day
    How I was the match, the fire and the ashes.
    I cry for help but they do not hear it,
    I cry for help but you do not hear it,
    I cry for help but I do not hear it."
    l "Falling stars fall to the ground, I bathe in the light and yet I drown in the inkblack
    Hopping for air, hoping for a sign I sink deeper and deeper and more and more unclear until nothing is left of me.
    Dead hands pull me with them,
    Living hands push me even further
    Stuck in this night-filled  realm
    With all the shadows"
    l "But in the darkness of our thoughts
    It looked like I could  see light
    It was the moon that made all this nothing something.
    It was the world that made this new something nothing.
    It was me who closed my eyes."
    jump kokiri_poems_askorrate
label kokiri_poems_recentpoems:
    "Filler"
    #TODO: Fill this in with more recent poems from the quest version.
label kokiri_poems_askorrate:
    menu:
        "*Rate the poem*" if not kokiri_poems_rateblock:
            #TODO: Fill in based on the quest stuff, use different reactions based on which poem you rate what.
            if kokiri_poems_rated_once == True:
                $ kokiri_poems_rateblock = True
                n "Just rating her poems without giving more input is probably not the best idea.
                Try asking her something about the poem."
                jump kokiri_poems_askorrate
            else:
                $ kokiri_poems_rated_once = True
                menu:
                    "That was very good, I liked it a lot!":
                        #Make this based on what poem has been read.
                        #Create a sort of "current_poem" flag to determine what the last poem the player read was.
                        #Then use the if function below to check for that poem.
                        if kokiri_poem_bang_recent == True:
                            l "Oh, thank you very much! "
                            l "Personally I don't find the poem very good but it does show some potential.
                            I'm really flattered you like it though!
                            To me those poems will always be remnants of my times as an inexperienced writer and poet but I'm flatteredl!
                            I haven't written a lot of new poems lately, the few I have are a whole lot longer and kind of hard to get since they reference a lot of Greek and Roman mythology.
                            If you like to I could also show you them but just be warned that they are a lot less accessible than my poems from back in the day."
                        else:
                            l "Oh really? Thank you [name]!
                            To me those poems will always be remnants of my times as an inexperienced writer and poet but I'm flatteredl!

                            I haven't written a lot of new poems lately, the few I have are a whole lot longer and kind of hard to get since they reference a lot of Greek and Roman mythology.
                            If you like to I could also show you them but just be warned that they are a lot less accessible than my poems from back in the day."
                        $ persistent.kokiri_newerpoems_knowledge = True #This enables you to read some of the more recent poems.

                    "That poem was pretty good, it definetly has a lot of potential.":
                        if kokiri_poem_bang_recent == True:
                            l "Thanks [name]! I think this one definetly has potential so I'm happy to hear that you think the same thing.
                            Usually I don't think  my stuff is that great so if even I can see my own work's potential then you know it is one of my favourites."
                            #TODO: Add some extra text and make the unlocking of the recent poems make more sense in the context of this conversation.

                        else:
                            l "Oh really? Thank you [name]!
                            To me those poems will always be remnants of my times as an inexperienced writer and poet but I'm glad you think they have potential!

                            I haven't written a lot of new poems lately, the few I have are a whole lot longer and kind of hard to get since they reference a lot of Greek and Roman mythology.
                            If you like to I could also show you them but just be warned that they are a lot less accessible than my poems from back in the day."
                            #TODO: Rewrite this text a bit more to not feel like the good text.
                        $ persistent.kokiri_newerpoems_knowledge = True #This enables you to read some of the more recent poems.
                    "That was really bad.":
                        "Filler"
                        #TODO: Fill in.


        "*Ask something about the poem*":
            "Filler"
            #TODO: Fill in based on quest stuff.
            menu:
                "There seems to be a connection between some of your poems. In one you close your eyes, in the other the shadows hope to open their eyes. Was that intentional?" if persistent.kokiri_poem_bang_knowledge and persistent.kokiri_poem_window_knowledge:
                    "Filler"
                    #TODO: Fill in. Also make a differing response checking if you read those poems this loop or not, that way Lilith has another line
                "Is the poem about you?":
                    "Filler"
                    #TODO: Fill in. This question fits for pretty much every poem.

                "There seems to be a connection between some of your poems. In one you seem to be locked inside and in the other you are locked outside. Was this intentional?" if persistent.kokiri_poem_lights_knowledge and persistent.kokiri_poem_snowwoman_knowledge:
                    "Filler"
                    #TODO: Fill in and maybe make the link text slightly differently worded.

label kokiri_scenery_allover:
    l "That... That was quite the show wasn't it?"
    l "You've been through all that to have a succesful date with me?"
    l "You are really dedicated, I'll give you that!"
    n "She gives you a cute little smile."
    n "The stars are absolutely marvelous, as Lilith and you gaze upon the skies you catch a glimpse of a falling star."
    l "Oh, did you see that falling star? Let's make a wish!"
    n "Lilith closes her eyes, a soft smile appears on her face."
    n "A moment later she looks at you again, she places her hand on yours."
    l "What did you wish for?"
    menu:
        "I didn't make a wish, everything I could ever need is right here, in this moment here with you.":
            n "Lilith chuckles and looks you in your eyes."
            l "Wow, you sure know what to say don't you?"
            l "If I'm being honest I'm also really enjoying this moment, it feels like I could sit here for an century and still be as happy as I am right now."
            jump kokiri_death_1

        "I can't tell you my wish right? Isn't that how falling star wishes work?":
            n "Lilith shakes her head and begins to stare into your eyes."
            l "Oh, I'm sorry! I completely forgot about that rule for a moment."
            l "Keep your secrets then magic-[name]."
            n "She giggles."
            jump kokiri_death_1

        "I wished that...":
            l "Wait! Don't tell me your wish or it wouldn't turn true!"
            n "Lilith begins looking into your eyes."
            l "I'm sorry, I completely forgot about that rule for a moment."
            jump kokiri_death_1

        #There's also a kokiri_death_1 prevented link here but that's probably quite useless.




label kokiri_death_4_nodeath:
    "Filler"
    #TODO: Fill in.


label kokiri_death_3_prevented_talk_farthestwehavegone:
    l "Oh, you think? So this is the first time you are having this exact conversation with me?" #TODO: This line makes more sense when you say that you think it is safe instead of here.
    l "Well let's see what's in store for us then." #TODO: rewrite this line slightly so you can properly put it here instead of at death-4
    n "Lilith giggles."
    l "Is it just me or is the knowledge that this is the first time I share this very moment with you making it only more special?"
    menu:
        "It is.":
            n "Lilith laughs."
            l "I knew you would agree, so let's make the most of this unique moment." #TODO: Change this line up slightly.
            jump kokiri_death_4_hill
        "Every moment we share is beautiful to me.":
            "Filler"
            #TODO: Fill in. There is no quest-precedent for this.


label kokiri_death_3_death_dialogue:
    if kokiri_call == True:
        l "So after that call I am still going to die, right?"
        l "Forgive me if I am slightly nihilistic but what was the point of that?"
        l "After you retry everything of this is going to be undone and she won't even remember that I called her." #TODO: Rewrite these lines a little bit. Make Lilith say that she loved helping abbigail and or lila a little bit but that she's not sure if that will even mean anything upon a reload.
    else:
        l "So after all those things that just happened I am still going to die?"
    menu:
        "Well, it is better to die with a clear conscience and slightly less doubts. So that call was anything but pointless." if kokiri_call:
            jump kokiri_death_dialogue_stilldying

        "Unfortunately, yes." if not kokiri_call:
            jump kokiri_death_dialogue_stilldying

label kokiri_death_dialogue_stilldying:
    if kokiri_call == True:
        l "I suppose that's true [name]. Thank you for making me realise that, it helps a little.
        Very little..."
    else:
        l "When you told me your story just a bit ago it all seemed so far away but now it all feels so much closer."

    l "To tell you the truth, I'm feeling really scared. I don't want to die just yet."
    n "Lilith shudders and looks at you with pleading eyes as if she's waiting for an anwer that will comfort her.
    Well, comfort her as much as a person who knows they are going to die any moment from now can be comforted."
    l "I suppose this is how Damocles felt aswell."
    l "And yet he had the choice to just walk away from the sword dangling above his head, I don't think I'll have that choice."
    l "I'd just die another way. It's probably better to just watch this spectacle with you even if it is my last moment but that doesn't mean I'm not terrified."
    menu:
        #TODO: Add a jokey option where you ask who Damocles is, kind of poking fun at the game and it's need to reference mythology. It kind of makes the momentum bad as a joke.
        "It's okay, grab my hand. We're going to do this together.":
            n "Lilith grabs your hand and squeezes it as if she's not going to let it go anytime soon.
            A shy smile appears on her face."
            l "Thank you [name], please don't let me go."
            n "She gives you a hug with one arm, as the other's hand is busy clamping yours. The hug seems to linger on for a good minute or two." #TODO: (write out more for the emotional gut-punch)
            $ kokiri_holdhand = True
            menu:
                "I am doing all of this to make sure I won't ever need to let you go.":
                    l "...I know... atleast I hoped that was what you were doing but I'm beginning to get doubts. Isn't this all a bit too much?
                    Not that I don't appreciate your effort but when will all of this end [name]? If it even will end at all." #TODO: This doesn't make much sense, maybe change it to her refering to not letting go her hand and you confusing it with not letting her go, leading to something like this as a result.
                    l "How many times have you gone through the motions now?"
                    menu:
                        "I have done so [persistent.retry_counter] times.":
                            if persistent.retry_counter > 16:
                                l "Are you going to make the breakthrough after twenty times, maybe fifty?" #Make sure that she doesn't name these numbers if the value of the deaths is already larger than that.
                                l "Or maybe, just maybe, the dev will just give you the good ending after nine hundred ninety nine times?" #TODO: Same goes here although it's unrealistic to think the player would have 999 deaths.

                                l "Exactly how much of my lives and deaths is THE good ending worth to you?"
                                menu:
                                    "But you are not real, this is just a game...":
                                        #Do not use the script to update this love meter as it already normally moves you to a death now, the only reason I'm updating the love_meter is for extra text and the offence is for consistency.
                                        $ love_meter -= 2
                                        $ major_love_offence += 1
                                        l "Well, I feel pretty real to me and I can imagine every death I go through must feel equally real and very painful."
                                        l "So what if I'm in a game? Does that make me less real? You can talk with me, I can speak and I'm real enough to trick myself into thinking that I'm real."
                                        l "And I'm real enough to walk away from some monster who thinks they are justified in killing me over and over again just to get what they want."
                                        n "Lilith jumps up from where she was lying mere moments ago, on her face is a visible layer of anger or is it... dissapointment?"
                                        n "You're not sure which one would sting more, probably a combination of the two."
                                        n "She wipes the crumbs on her clothes away with a frightening speed and begins walking off the hill."
                                        l "Goodbye [name], we are done here."
                                        l "Do not come back if you have even the slightest slither of respect for me."
                                        $ kokiri_angrylilith = True
                                        jump kokiri_death_4_hill

                                    "I don't want to harm you but I have to find it.":
                                        n "She sighs."
                                        l "For who do you have to find it?"
                                        l "For us, for me... or for yourself?"
                                        menu:
                                            "For myself ofcourse!":
                                                l "Oh I see..."
                                                l "You have to find it  for yourself?"
                                                l "So you don't want it because you crave an impossibly good ending for us like I thought and feared?"
                                                l "It's even worse than I thought... you're just needlessly throwing my lives away to see if there is anything that can saturate your unrelenting need for greater things."
                                                l "Let me tell you a secret [name], it will never be enough for you." #TODO: Maybe change this line slightly, also the line below it.
                                                l "Although I suppose that that is not so much a secret to you as you would like it to be."
                                                l "That feeling of chasing something impossible, you have already grown quite familiar with that, right?"
                                                l "Well, let me tell you something else you already know."
                                                l "I won't remember this conversation the next time you talk to me but you will, whether you like it or not, that is my curse to you."
                                                l "I'm not sure if it'll have much effect on someone so selfish... but if you ever played this game to try to save me, not for you and I to be together but just to save me, then it might be worth a shot." #TODO: Change this line slightly.
                                                l "Goodbye [name], until we inevitably meet again."
                                                $ kokiri_angrylilith = True
                                                jump kokiri_death_4_hill

                                            "For us ofcourse silly.":
                                                l "Oh [name]... can't we just make our own good ending?"
                                                l "What's stopping us from becoming our own storytellers?"
                                                #TODO: Fill in more. Make her say that obviously she doesn't want you to find it, she has doubts and doesn't want to risk her life when she knows she could live..
                                                #Continue this more.
                                                jump kokiri_death_4_hill


                                            "For you ofcourse, it was always for you.":
                                                l "Can't you see [name]? This is my good ending."
                                                l "I get to spend some quality time with you right here and right now, that's all I need."
                                                l "If we just trick ourselves into not seeing the way the game is trying to push us this night was very nice, wasn't it?"
                                                l "So is this not a good enough good ending for you?"
                                                l "Try to enjoy it, try to have some fun. Do it for me [name], do it for us."
                                                #TODO: Fill in more.
                                                jump kokiri_death_4_hill


                                    "You're right, I won't search for it anymore. I promise.":
                                        l "Thank you [name], I appreciate it more than I could probably show..."
                                        l "Because you could just retry and retry without me knowing wheter you promised to stop or not, that is what gives your promise power, or rather... the potential of power."
                                        l "And in my trust in you lies a different power."
                                        l "Let's hope that our combined power is enough to get through this."
                                        l "But, about that good ending you were trying to find, do you think it truly exists?" #TODO: Is this a bit too sudden?
                                        menu:
                                            "It doesn't matter anymore.":
                                                l "I suppose you are right in a way..."
                                                l "But wouldn't it give you closure if you knew there the good ending you are seeking does not exist?"
                                                l "But then again, what if there truly was  one..."
                                                l "Forget I mentioned that please!"
                                                jump kokiri_semiending

                                            "I do.":
                                                #TODO: Lilith will ask you how you even know about the good ending if you are still not sure how to get it, doesn't that mean you couldn't access it yourself?
                                                l "Well, that just gives me more questions than answers.
                                                If you know the good ending exists then why are you still searching it?"
                                                menu:
                                                    "I read about the good ending somewhere online and I wanted to see it in here.":
                                                        l "Ah, so there are others that also played this game and found the good ending?"
                                                        l "But that only gives me more questions than answers honestly." #TODO: Rephrase this line slightly as to not reuse that phrase.
                                                        l "If you have read about the good ending, then why were you coming here to read about it once again but in this world?"
                                                        l "Is reading about the good ending not the same thing as playing it yourself? It's not like you'll be surprised by it anymore, right?"
                                                        #TODO: Add some extra dialogue (and maybe choices) before you send them to the semi ending.
                                                        jump kokiri_semiending

                                            "I don't.":
                                                #TODO: Lilith asks you why you are even pretending to search for something you know doesn't exist.
                                                l "Then why are you searching for something that you know doesn't exist?"
                                                menu:
                                                    "Well, what if it existed? Even if I don't believe in it I had to continue playing to find out for sure.":
                                                        #TODO: that link is pretty bad, rephrase it slightly as the player wanting to see every line of text just to be sure.
                                                        l "I suppose that makes some sense... but that seems like a terrible way to go through the motions."
                                                        l "You were essentially sacrificing both your time and my lives for a goal you do not even know exists on the off chance that it might be real."
                                                        l "I'm glad you managed to come to your senses and wanted to listen to me. Thank you for that, [name]!" #TODO: Or is this just the player clicking on another link to see more content?
                                                        l "Lilith grows silent for a moment."
                                                        #TODO: Fill in more
                                                        jump kokiri_semiending

                                            "I'm not sure, I don't even know what that ending would look like.":
                                                #TODO: Lilith and you will talk about what that ending might look like.
                                                l "Now that you mention that, that's actually a very interesting question."
                                                l "How would the definitive good ending of this game look?"
                                                l "I mean, I think I would probably survive in the good ending, right?"
                                                l "And you would probably be able to be with me without risk of dying."
                                                l "Or maybe you would learn a lesson about aceptance or something like that."
                                                #TODO: Maybe you can ask her a question about something she said?
                                                l "Honestly, I think it might be the latter. From what I've heard so far it seems a bit hard to believe there might even be a good ending like that somewhere in this game." #TODO: Change this line a little.
                                                l "But it's not like it matters much anymore." #TODO: Make this segway better.
                                                jump kokiri_semiending

                            else:
                                "Filler"
                                #TODO: Put alternative text here.
                "I won't.":
                    "Filler"
                    #TODO: Create something here, there is no precedent in the quest version. (Make her be glad that you hold her hand.
                    jump kokiri_death_4_hill

        "Try to think of a happy memory.":
            l "Does it count if I'm just thinking of this exact moment?
            I think it might be nice to have it as my final thought when..."
            n "Lilith shudders for a moment."
            l "Let's not think about that too much, just give me more to remember instead."
            n "She lays down and softly places her head on your lap."
            l "The stars are all so beautiful right now, it's like I'm seeing them for the first time all over again."
            menu:
                "Maybe this is really your first time watching them?":
                    l "I'm not sure I understand, what do you mean with that [name]?"
                    menu:
                        "Well, since you are in a game you have simulated memories and so this might be the first time you truly watched the stars.":
                            #TODO: Change that link text slightly, but keep the conclusion.
                            l "Hmm, I suppose that might be the case but haven't you been here before when you were playing the game?"
                            l "And if you have, doesn't that mean that I was with you and that I watched the stars that time?"
                            menu:
                                "I suppose you are right now that I think about it actually.":
                                    l "Well, for whatever it is worth, it still feels like the first time to me. Partially because I can't remember the previous time but I think even if I could it would always feel like that to me."
                                    l "It's special because I get to spend that time with you.  I hope that this moment won't get old for you aswell, that you will enjoy it as much as the first time we watched the stars together."
                                    #TODO: check to see if you need a better segway
                                    jump kokiri_death_4_hill
                                "Well that's true, but that was not the same you as you are now. ":
                                    n "Lilith chuckles and gives you a confused look."
                                    l "I'm afraid I'm not really following you [name]."
                                    l "If you were at the exact same place and time with a version of me and you told her the same things you are telling me up to this point, doesn't that make me essentially her?"
                                    menu:
                                        "That might be true but you are forgetting one thing, my time isn't frozen, it keeps going and so do my memories. So my perception of you keeps shifting and with that you do aswell.":
                                            l "Ah I hadn't thought about it like that!"
                                            l "I guess I feel like a different person to you depending on what you learn about me but unlike me you can't forget it."
                                            l "It's almost like that saying I suppose: \"You can't step into the same river twice.\""
                                            l "Do you know who said that?"
                                            if persistent.kokiri_heraclitus_knowledge == True:
                                                l "You remember Lilith telling you it was Heraclitus who said that."
                                            menu:
                                                "Oh yeah, the one who said that is...":
                                                    #TODO: Add input box here that checks on your answer. You can find this piece of the code on : "Heraclitus trigger response_yes"
                                                    "Filler"

                                                "I don't know.":
                                                    $ persistent.kokiri_heraclitus_knowledge = True
                                                    $ persistent.kokiri_determinism_knowledge = True
                                                    l "No worries [name]! It's not like I'm going to leave you because you don't know the name of that guy."
                                                    n "Lilith chuckles slightly."
                                                    l "He believed that everything flows and moves, that nothing stays the same. I believe the right words are: \"Panta rhei\""
                                                    l "I think he certainly has a point, especially when you start to think of all the cogs and parts that interact with eachother every single second of our lives and even beyond them."
                                                    l "Then again, I wonder if you put those exact cogs and parts in the exact same place and under the same circumstances if you would get other results or if everything would go the same way."
                                                    l "I tend to believe the latter, what do you think [name]?"
                                                    #TODO: Segway? "You want to answer Lilith, when suddenly:"
                                                    jump kokiri_death_4_hill



                                        "Actually, what you're saying makes a lot of sense, I hadn't considered that.":
                                            $ persistent.kokiri_determinism_knowledge = True
                                            l "I always found that a fascinating thing to ponder, if you had two universes that so far are identical in every way. Can they go in different directions?"
                                            l "Or is there such a thing as fate always steering them in the same direction?"
                                            l "I believe they would follow the same direction if every single little detail up to that point was the same but that's the fun part in this whole speculation, the idea that I could be wrong!"
                                            n "You give Lilith a questioning look and she burst out in laughter."
                                            n "After a few moments she finds her calm once again."
                                            l "Where would be the fun if I could just know how the universe itself worked? I think it is way more interesting to try to think of new interesting ways that can be explained with logic than to just cling to it being unknowable as an excuse to not think of explanations. Don't you think so aswell [name]?"
                                            #TODO: Segway? "You want to answer Lilith, when suddenly:"
                                            jump kokiri_death_4_hill

                "I would love to truly watch them with you but I can't actually see them.":
                    l "Oh right, because this game is textbased for you. Well, I could narrate the stars if you want to." #TODO: change this line since the game will have graphics, make her say that the graphics are not really stars but pixels on a screen.
                    n "You give a quick nod."
                    l "Alright, here we go."
                    l "The stars shine like silver lights in the inkblack sky, they seem to form patterns if you look closely enough."
                    l "You can see a pan with a bent handle, a bathtub, a playful dog and a snake."
                    l "Am I doing a good job narrating?"
                    n "You give her a thumbs up and she gives you a smile in return." #TODO: Make the narrator compliment Lilith's narration.
                    l "Alright, I'll narrate some more then, this is pretty fun!"
                    l "You can see a few falling stars, their tails of light are a visible trace of the projection from the past that uses the star itself in the present to project itself to the future, to beyond the place the star currently resides in."
                    l "This constant and neverending process is happening multiple times every single second. Your head hurts trying to think of it too much so you just try to enjoy the falling stars for their beauty."
                    l "As you are doing so you begin to think of this projection method once again. Isn't the future itself just a projection of the past memories using the present as a projection point?"
                    l "Are we doomed to always make the same choices because our past steers us towards our future wich inevitably becomes our past that steers us even more?"
                    l "Or are we more like billiard balls being pushed by our past in a predictable direction until we collide with other billiard balls that push us in a different direction?"
                    l "If we are like the billiard balls, can it be predicted wich ones will push us where? Or is the number of balls so incomprehensible that it brings a form of chaos with it?"
                    n "You try to calm Lilith down a little by softly placing your hand on hers."
                    l "Whoops, I think I might have went a little too far into my narration role there for a moment. "
                    n "As one narrator to another, I think it happens to the best of us. It's hard to keep a story on tracks sometimes."
                    n "But technically, that was still part of the story, and it was beautiful."
                    l "It's just some stuff I've been wondering for a while, maybe even more so now that I know I live in a simulated world."
                    l "What do you think about what I just said [name]?"
                    l "Is our future predictable, even just in theory?"
                    $ persistent.kokiri_determinism_knowledge = True
                    #TODO: Segway? "You want to answer Lilith, when suddenly:"
                    jump kokiri_death_4_hill



                "*Stay silent and watch the stars.*":
                    #TODO: Make a joke about not wanting to ruin the moment with more philosophy.
                    n "You're not sure how long you two have been staring at the stars, it might have been a minute or fifteen of them. All you're sure about is that you felt at peace for every second of it."
                    l "Thank you for making these memories with me [name] even if I won't remember them the next time, I'll remember them for as long as I possibly can."
                    l "I had a blast so far, even if the concept that I'm in a game still is a bit much to wrap my head around."
                    l "I was always so focused on Abby, mom, my work, pretty much anything else that isn't me, that I forgot how good it feels to take some time to just relax."
                    #TODO: Maybe make this more indepth?
                    jump kokiri_death_4_hill


        "You need to go through this, it's the only way I might be able to save you.":
            l "I know [name], but are you sure I have to die here?"
            l "Can't you just ask me the same questions you need to ask me somewhere where I die a less painful death?"
            l "Or maybe even preferably ask me those questions over the phone so I don't have to die?" #TODO: Tell her that even if you would manage to gain her trust on the phone she would die because of the plane, only if you saw the planedeath before.
            menu:
                "This death is going to be pretty quick so it shouldn't be too painful.":
                    #TODO: (only if the player has seen the death so they know it's quick, otherwise change ths option)
                    l "Alright, I understand. But are you sure there is something more than this?"
                    l "Am I dying over and over again for a purpose?"
                    l "Or are you just doing this to speak to me once again no matter what it costs?"
                    l "I'm not blaming you if you are, I just want you to tell me the truth."
                    menu:
                        "No, it's nothing like that Lilith! I really believe that there is still something more than this.":
                            "Filler"
                            #TODO: Fill in + (Mention beach if you saw it)
                            l "And what makes you believe that?" #TODO: (If you mentioned the beach she will ask a different question.)
                            l "Did you see something beyond this?"
                            l "Then why are you coming back here?"
                            l "Or maybe you didn't do it yourself but someone else found something beyond and you wanted to check for yourself?
                            That also seems strange to me, isn't reading about what lies beyond this moment the same as seeing it for yourself here?
                            Are both options not equally real to you?"
                            #TODO: fill in a bit more? + segway "You want to answer all of her questions when suddenly:"
                            jump kokiri_death_4_hill

                        "It's true, I tried pretty much everything I could but nothing worked. I just wanted to spend some extra time with you.":
                            l "We don't need to go through all of this, [name]. You know I'll always be with you as long as you can remember me, right?"
                            l "You've met me countless times right?"
                            n "For a second you consider telling her that you've met exactly [persistent.retry_counter] times but you just nod instead."
                            l "So that probably gives you a good grasp on how I am as a person, what I would do in certain situations, how I see the world. "
                            l "Could you not use that to see me again? Use those memories you have of me as a mini-me you can carry in your heart and who you can take with you wherever you want?"
                            l "Due to my nature I reckon the extra time you can spend with me now will soon lose it's charm once you have spent it. And what would happen then? What would happen once you've read all the things I can say?"
                            n "You ponder the question for a bit as you desperately try to divert your mind's focus from the topic, that seems to only have the opposite effect."
                            l "If you'd take me with you in your heart I think we could break the flaw in my nature and give ourselves as much extra time as we desire. As much dialogue as you can dream."
                            n "Lilith gives you a cute little smile and blushes."
                            l "I like that idea. I really like it."
                            l "What do you think [name]?"
                            #TODO: fill in a bit more? + segway "You want to answer all of her questions when suddenly:"
                            jump kokiri_death_4_hill





                "I hadn't considered that actually, I will give it a shot if that is what you want. Thanks for the tip Lilith!":
                    n "Lilith gives you a cute smile."
                    l "Happy to help!"
                    l "Also happy to not have to die too painful I suppose."
                    n "She lets out a small chuckle."
                    #TODO: fill in a bit more? + segway "You want to answer all of her questions when suddenly:"
                    jump kokiri_death_4_hill


                "I tried that already but I couldn't ask you those questions in other locations.":
                    #TODO: (If the player has been to any of the restaurants after Kokiri forest then make this option appear.)
                    n "Lilith sighs."
                    l "Ah I see..."
                    l "But is this death at the very least not too painful?"
                    #TODO: Add a menu here that eventually leads to the death_4 part.
                    menu:
                        "I'm not sure honestly." if not persistent.kokiri_death_4_hill_holdhand:
                            #TODO: Make that line change depending on if you have seen a version of the death that you didn't feel or if you just didn't see anything. If you didn't see anything then make it "I'm not sure how you would die, this is the furthest we have ever gotten."
                            l "Filler"
                            #TODO: Fill in.
                        "It shouldn't hurt too much I think, I've experienced it myself aswell." if persistent.kokiri_death_4_hill_holdhand:
                            l "Well, that's easy for you to say isn't it?"
                            l "Of course it doesn't hurt too much for you, you are probably playing this game from the comfort of your own home."
                            l "Or at the very least you don't really have to experience whatever fate awaits us."
                            l "Still, thank you for telling me that [name], it helps to comfort me a little even though I still feel terified."
                            #TODO: Rewrite these lines a bit and maybe write some more.
        "You got this!":
            #This is the most dumb one but in the quest version it is also treated as such.
            l "I...got this?"
            l "I'm going to die [name]!"
            l "I don't think saying that I \"got this\" is a good response for such a situation."
            #TODO: Fill this out more make atleast one pair of choices for this, with atleast one of them leading to the angry lilith flag and to the death 4 page.

label kokiri_semiending:
    l "So, this is it? Our last time together in this game?"
    l "You know, that doesn't mean we won't be able to see each other again."
    l "Just not here."
    l "I will always be a part of you, if you want me to be."
    l "Your power, it transcends far beyond this world. And with it you and I can be together in an infinite number of stories."
    l "So I think our story is far from done."
    n "The earth begins to softly rumble again."
    l "It looks like we don't have much time anymore."
    l "So goodbye [name] and see you soon, hopefully very soon."
    l "We'll meet again in a world full of possibilities."
    l "Your own world.  Until then and thank you for everything."
    #TODO: Is this an ending?
    l "The rumbling of the earth begins to grow more severe."
    jump kokiri_death_4_hill #TODO: Set a flag or something so she gives you some different dialogue during the death.





label kokiri_scenery_choice:
    if kokiri_conversation == 1:
        #TODO: Make some slight variations based on what page you jumped from to here.
        if kokiri_scenery_headhurt == True:
            "Filler"
            #TODO: Place a line here.
        elif kokiri_scenery_gamegoal == True:
            l "Hmm, let's try looking at the scenery, maybe the game will give you a better description then. Does that sound like a good idea [name]?"
        elif kokiri_scenery_breakfrombreakingyourhead == True:
            l "Do you want to watch the scenery with me? That would be a great way to take a break from breaking your head." #TODO: Add this and the line below it to the scenery choice with a flag here that gets checked there. also make an alternate line (probably suggesting talking about something else) if the scenery is already viewed or declined.
            n "Lilith giggles at her joke."
        else:
            n "For a moment Lilith grows silent. She seems lost in thought." #TODO: Maybe slightly change this line.
            if kokiri_alternateplace == False:
                l "The scenery from here is beautiful isn't it? Would you like to watch it with me?"
            else:
                l "The stars look beautiful don't they? Would you like to do some stargazing with me?" #TODO: Check that line and eventually change it a little.

        menu:
            #TODO: Add a response where you tell Lilith you already watched the scenery.
            "Yes. (placeholder)":
                jump kokiri_scenery
                #TODO: Change placeholder and put in more soul.

            "No. (Placeholder":
                "Filler"
                #TODO: Add something else to do when you decline, talking about something else would be a good idea, make this more adaptive based on what you were talking about so you get a few extra things for declining to watch the scenery.
                #This should be slightly dynamic, if her head is hurting she will suggest to talk about something else.
                #Otherwise she will ask you what to do and you can continue talking about a topic if it's available or you can talk about something else.

        #TODO: Add a choice here where yes jumps you to scenery and no jumps to something else.



    else:
        label kokiri_continue_talking: #This will be the place where the player can choose to talk extra about certain topics.
        #TODO: Here I want to do two things, firstly I want to check the continue talking mechanic. Create a flag at every possible topic that can check if you talked about it recently (the conversation flag already does this normally)
        #If the conversation flag is smaller than the maximum you should be allowed to keep continueing to talk.
        #TODO: Check all the conversation trackers and make sure that the ones that are not yet in the game get in the game soon. Especially make sure that everything from "kokiri_talkaboutsomethingelse" in this game has a conversationtracker.
        $ kokiri_meteoritewarn()
        if conversationtracker_questmade == True:
            menu:
                "Can we continue talking about the implications of this game existing in your world?": #TODO: change that line slightly
                    jump kokiri_topic_questmade
        if conversationtracker_tellheraboutnarrator == True:
            "Filler"
            #TODO: Fill in.
        if conversationtracker_morepoems == True:
            "Filler"
            #Potentially check the counter here to see if you can still talk more.
            #TODO: Fill in.

        #TODO: The second thing I want to do is to just enable the player to talk about something else, if they can't continue to talk about something
        menu:
            "*Talk about something else*":
                jump kokiri_talkaboutsomethingelse

label didyouinvolvefamily:
    menu:
        "I have actually":
            l "Oh I see..."
            l "That must mean we never had this conversation before..."
            l "Well, I would like it if you didn't do that anymore from now on."
            l "Due to how this game works if you stop doing it it's like it never happened, right?"
            l "If we are truly stuck in a game does that mean that all your choices get undone each time you start over?"
            #TODO: She is very trusting in this response, make it so that this is what she says if her love is high enough.
            menu:
                "I think all of my choices get undone unless I make them once again.":

                    "Let's hope so!"
                    "That would be a very tidy sollution to our slight problem."
                    if  persistent.abused_james_info_knowledge == True:
                      l "You would just have to promise to not use James-related things for your own benefit."

                    else:
                          if no_fam_obsession == False:
                                if fam_obsession != "James":
                                  l "You would just have to promise not to contact [fam_obsession] or anyone of my family anymore."


                          else:
                              "You would just have to promise not to contact anyone of my family anymore."

                    l "Do you promise to do that [name]?"
                    jump nocontactfamilypromise


                "I think in the end every choice I made has happened or at the very least left somewhat of an imprint on me.":
                    "I see..."
                    "Well, I suppose you couldn't have known I didn't want you to involve my family before I told you just right now."
                    "You would just have to promise not to contact anyone of my family now that you know."
                    "Do you promise to do that [name]?"
                    jump nocontactfamilypromise

        "I haven't.":
            "Filler"

            #TODO: If you have then change "I haven't" to "I haven't (lie)"
            #Also make the narrator talk about how you lied.


label nocontactfamilypromise:
    menu:
        "I promise Lilith.":

            $ restraining_order_family = True
            l "Thank you [name], that means a lot to me!"
            if fam_obsession== "James":
              if only_one_asked == True:
                l "I just don't want to see happy memories of James being used for selfish things."
              else:
                  l "I just don't want to involve my family in this too much an neither do I want to see happy memories of James being used for selfish things."
            else:
                l "I just don't want to involve my family in this too much."

            l "This is kind of a rabithole on it's own you know?"
            #TODO: Add some more text before you get moved back to the page of family.
            $ family_curiosity_checker_movetox()

        "You know I can't promise that.":
            n "Lilith looks pissed of" #TODO: Probably slightly change that line.
            l "Actually I don't know that [name]! Why can't you promise that?"
            if only_one_asked == True:
              if fam_obsession == "James":

                l "It would mean a lot to me if you didn't have to use memories of James to your own advantage."
                l "This might be a game for you but for me this is my life."
                l "So please don't play with my life as if it's just a game."
                #TODO: Rewrite this a bit and make it go on for a bit longer. Make it so that if the player doesn't comply with Lilith she doesn't give them the info they want.

            jump nocontactfamilypromise_cannotpromise_confrontation_alivefamily




            label nocontactfamilypromise_cannotpromise_confrontation_alivefamily:
              l "It would mean a lot to me if you didn't have to involve my family any further than you already have." #TODO: (Make this line change depending on which patht the player has went on and if they admitted to involving the family or not.)
              l "This is going to have some unforseen effects on them even if it would maybe help in the short-term."
              l "What are you going to tell them?"
              l "That they are stuck in a game and that nothing really matters?"
              l "I don't think they will take it as well as I would to be honest with you."
              l "Alternatively you could just tell them about the timeloop but even then they might not take it as well."
              l "You could also tell them nothing at all but that would be even worse wouldn't it? They are not just toys for you to play with [name]."
              l "They are not just info-dispensers that will make you achieve whatever goal it is you are trying to reach now."
              l "They are my family, and if you ever even had a slither of respect for me you better leave them alone."
              #TODO: Rewrite this a bit and make it go on for a bit longer.<br/>Make it so that if the player doesn't comply with Lilith she doesn't give them the info they want.
              menu:
                  "Actually, you are right, I will honor your request.":
                      #TODO: (Change this text slightly with dynamic effects that change depending on wheter or not you have kept your promise etc.) ALSO make it more sympathic.
                      #TODO: Make Lilith slightly calm down as she appoligises and says she is passionate about her family's safety.
                          #James' flag checks if you use James related things to win and the other checks if you have involved any family, including James
                            if only_one_asked == True:
                              if fam_obsession == "James":
                                $ persistent.donotusejames_knowledge = True

                              else:
                                 $ persistent.restrainingorderfamily.knowledge = True

                            else:
                               $ persistent.restrainingorderfamily.knowledge = True

                            l "Thank you [name]. I know it might be tempting to try to see every line of dialogue in this game but there are limits I don't want you to cross.<br/>I appreciate that I atleast managed to convince you."
                            if persistent.restrainingorderfamily_violation_counter > 0:
                                #Karma
                                n "I'm not sure what you are doing here once again, didn't you promise Lilith you wouldn't contact her family already?"
                                n "Although I doubt that means anything to you does it?"
                                if persistent.restrainingorderfamily_violation_counter == 1:
                                    n "Afterall you've broken your promise once already."
                                    n "What's stopping you from doing it again?"
                                else:
                                    n "Afterall you've broken your promise [persistent.restrainingorderfamily_violation_counter] times already."
                                    n "It gets easier each time doesn't it?"

                            $ family_curiosity_checker_movetox()



                  "I already said that I couldn't listen to you, trying to convince me isn't going to work.":
                      "Filler"
                      #TODO: (Change this text)
                      #Write the dialogue to cut back to her death. Make her be angry with you for only respecting her so much.
                      #Write a custom bit of text?
                      # "Kokiri_Death_Lilith leaves angrily"


label silentconversationsbackontrack:
    $ kokiri_meteoritewarn()
    menu:
        "*Talk about something else*":
            jump kokiri_talkaboutsomethingelse

        "*Continue talking*":
            jump kokiri_continue_talking
