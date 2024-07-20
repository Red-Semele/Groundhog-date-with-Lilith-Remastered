
#TODO: Play through burger-path to be sure it's semi-bug free and also add the nightmare scenario to it etc.
label burger_start:
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
    n "You arrive a tad late, Lilith already has grabbed herself a seat and waves at you when she sees you."
    l "Heya! Almost was scared you wouldn't show up."

    $ burger = True
    if persistent.burgerwent == 0:
        if persistent.burgerstart == True:
            $ persistent.burgerwent += 1
        else:
            $ persistent.burgerstart = True


    menu:
        "I can't say no to burgers!":
            jump burger_start_choice1

        "I wouldn't want to miss this for the world!":
            jump burger_start_choice2

        "Sorry, traffic was quite bad.":
            jump burger_start_choice3

        "Hey glad to be here. Could we sit somewhere else though?" if persistent.burger_death_1:
            $ burger_alt = True
            n "Lilith gives you a smile and a thumbs up."
            l "Sure, where would you like to sit?"
            n "You quickly point to a table, it doesn't really matter which one, as long as she isn't sitting where she got shot before."
            l "Alright, that table it is then!"
            n "Lilith takes her handbag and follows you as you wander to the table."
            n "You feel relieved, knowing what horrors you just escaped from."
            n "The image of her laying there, on the brink of life and death, is burned into your mind."
            n "You shudder."
            n "It's probably best to try and focus on the present, not the past."
            l "Are you alright [name]?"
            l "You look like you have just seen a ghost."
            n "She's not far off."
            menu:
                "Oh yeah, I am fine, I was just thinking about the traffic jam I was stuck in.":
                    jump burger_start_choice3




label burger_start_choice1:
    n "Lilith chuckles."
    l "Ah, another burger fan!"
    l "We are at the right place I'd say, the burgers here are delicious."
    l "Did you already know that or is this the first time you've eaten here?"

    menu:


        "I've never been here before." if persistent.burgerwent == 0:
            jump burger_beenBeforeXTimes


        "I've been here before, only once though." if persistent.burgerwent == 1:
            jump burger_beenBeforeXTimes


        "I've been here exactly [persistent.burgerwent] times." if persistent.burgerwent > 1:
            jump burger_beenBeforeXTimes


label burger_beenBeforeXTimes:

    if persistent.burgerwent == 0:
        l "I'm sure you'll love it here then!
        Like I've said before, they have really amazing bugers here."

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
            n "Lilith lets out a small giggle."
        elif persistent.burgerwent < 22:
            n "Lilith lets out a joyful laugh."
            l "Wow! I almost feel like I should let you choose my burger with all that burger knowledge you must have."
            l "Almost though, this is far from my first rodeo either [name]!"
        else:
            l "Wow... is it weird to be impressed by that?"
            n "Lilith lets out a small laugh."
            l "It probably is but I'm quite impressed by the expertise you must have when it comes to the burgers here."



    l "So, which burger do you want to pick? I think I'll go for the juicy cheeseburger myself."
    jump burger_start_menu




label burger_start_choice2:
    l "Awwe, I'm flattered you are so happy to see me. Or is it the burgers you don't want to miss?"
    l "Lilith chuckles slightly."
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






label burger_ordering:
    n "Lilith and you go to order the burgers."
    if persistent.burgerwent == 0:
        n "You were expecting having to order them from a screen most fastfood places tend to have but as you looked around you couldn't spot any. Instead Lilith walks to a counter.
        You decide to follow her."
    if persistent.rosename_knowledge == True:
        $ roseName = "Rose"
        n "An old lady, who you remember is called Rose, smiles at the both of you."
    else:
        n "An old lady smiles at the both of you."
    r "Hey Lilith, glad to see you here once more!"
    r "I'm almost surprised to see you here, it's been quite a while hasn't it?"
    if persistent.rosename_knowledge == True:
        n "Rose looks at you for a brief moment and continues."
    else:
        n "The old lady looks at you for a brief moment and continues."

    r "Who did you bring along for the ride?"
    l "Oh right, you two haven't met. Rose, this is [name] and [name] this is Rose."
    $ persistent.rosename_knowledge = True
    n "Rose gives you a sincere smile."
    r "Nice to meet you [name]."
    r "So, what can I get the two of you?"
    n "You and Lilith tell her your choices."
    r "A juicy cheeseburger and a [burger_choice] coming up! I'll bring them to you when they are done alright?"
    r "That way you two can get to know each other some more."
    n "She gives Lilith a quick wink that you just barely manage to catch."
    n "Lilith's face turning beetred is a lot easier to notice."
    l "{size=*0.5}Uhm, thank you Rose... we uhm have to get back to our table now.{/size}"
    n "You can't help but chuckle to yourself as Lilith pratically darts back to the table."
    n "By the time you've reached the table she is already sitting down, still as red as she possibly could be."
    n "She quickly brushes one hand over her left cheek and somehow manages to turn even more red at the realisation that she is still blusing."
    n "Right then she lets out a few small coughs as she tries to somehow divert attention from what just happened."
    #TODO: Add a better segway?
    l "Thank you for choosing this place [name].
    It has been too long since I've been here, to tell you the truth I actually was avoiding this place.
    But now the happy memories come flooding back to me."

    n "Lilith pauses for a moment, she seems unsure whether to continue or not."

    l"You know, my brother really used to love this place before..."

    n "Lilith freezes before she can continue the sentence."
    l "{size=*0.5}Why did I have to bring that up now?{/size}"

    menu :
        "What was his name?":
            jump burger_brother_question

        "Are you alright Lilith? You don't need to share this story if it hurts you too much.":
            $ love_points = 1
            $ love_meter_updater()
            l "Honestly I'm not sure if I'll ever be fully alright because of what happened."
            l "And I think telling that story will always hurt."
            l "But that doesn't mean I wouldn't like to tell you about it."
            l "In fact, I think it might be good for me to eventually tell you."
            l "Just..."
            l "I just would like to wait a little before I do that, maybe some other time [name]?"
            l "I do really appreciate your concern for me though!"
            #TODO: Talk about something slightly different after this and then move back to the main path so that everything goes smoothly again.
            #Add one piece of extra conversation you can have here, not sure what yet, add it where you normally ask about the brother



label burger_brother_question:

    $ askedbrother = True
    n "Lilith tries to compose herself as well as she can but from the look in her eyes you can tell this is all a bit much for her."


    menu:

        "Try to alleviate tension with a joke.":
            jump burger_joke

label burger_joke:

    menu:

        "So a priest, a monk and a rabbit enter a bar. Says the rabbit :\"Whoops, did you slip your tongue there [name]?\"" if persistent.joke_knowledge:
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
    $ love_meter_updater()
    n "Lilith bursts out in laughter."
    l "I really love that joke, my sister Abigail told me it once and I kept laughing and laughing for hat seemed like an eternity.
    Just thinking about it again, it fills me with a warm feeling, like a blanket you wrap around yourself in the coldest of winters."
    l "Thank you for cracking me up [name]!"
    n "Lilith flashes you a cute smile, she seems pretty much completely composed once again."
    jump burger_living



label burger_joke_response:
    n "A slight smile forms on Lilith's face.
    She doesn't seem to find your joke that funny but from the gratitude in her eyes you can tell she is thankful for your effort.
    She seems to have become slightly more composed."
    #Typewriter:
    l "Thank you."
    n "Lilith continues as if nothing happened."
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

        "Thanks for the tip Lilith, I'll keep it in mind!":
            jump burger_living_writer_thankTip


label burger_living_unemployed:
    l "Oh, do you like to write? That's pretty cool!"
    l "Lilith seems to be quite enthusiastic, her eyes have a certain shimmer to them that wasn't there just a moment ago."
    l "I also like to write something from time to time, it's one of my hobby's actually."
    menu:
        "Would you like to show something you've written?":
            jump burger_living_showWriting


label burger_living_showWriting:
    $ persistent.burger_poem_knowledge = True
    n "A wide smile grows on Lilith's face."
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
        n "Lilith seems thankful that you cleaned your fingers.
        You take the notebook out of her hand and begin to read.
        You can read the entire thing in her voice somehow."
    else:
        $ love_points = -1
        $ love_meter_updater()
        n "Lilith frowns when she sees your dirty fingers.
        Nontheless you take the notebook out of her hand and begin to read.
        You can read the entire thing in her voice somehow."

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
        n "When you get done reading your eyes linger on the notebook a bit longer before returning it to Lilith."
        l "So [name], what did you think of it?"
        n "She seems eager to find out what your thoughts are on her writing."
        jump burger_poem_rating
    else:
        n "When you get done reading your eyes linger on the now dirtied notebook a bit longer before returning it to Lilith."
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
            "Filler"
            #TODO: Fll this in with her forgetting that not everyone is that good with mythology and her casually explaining.
            #Also set a knowledge flag for that.


label burger_poem_rating_terrible:
    $ love_points = -1
    $ love_meter_updater()
    n "Lilith begins to frown slightly.
    She looks hurt by your words."
    l "Oh...
    No need to be a douche about it."
    jump burger_Brotherasked



label burger_poem_rating_fantastic:
    l "A wide smile appears on Lilith's face."
    l "Thanks [name]! I'm glad you like it so much."
    #TODO: Maybe put some extra text here since it feels a bit barren right now. She can talk about how she was in a edgy stage of her life when she wrote it for example.
    jump burger_Brotherasked







label burger_living_writer_thankTip:
    n "Lilith gives you a big smile."
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
    n "Lilith laughs."
    l "No worries, I really like music and I will always treasure my memories with the trombone."
    $ persistent.musiclover_knowledge = True
    $ musiclovertalked = True
    l "But if I kept playing it I think I would slowly grow to resent it, sometimes it's just better to end things on a good note."
    n "Lilith lets out a small giggle."
    l "That pun wasn't intended, I swear!"
    jump burger_deathBuildup

label burger_Brotherasked:
    if askedbrother == True:
        if love_meter >= 3:
            $ persistent.brother_knowledge = True
            n "Lilith pauses for a moment."
            l "You asked what my brother's name was, right?
            I don't know why but I feel like I can trust you enough to tell you about him.
            I might tear up, it's been a long time since I've told his story to anyone."
            l "His... his name was James."
            l "He was the best brother I could have asked for.
            He was five years older than me but we always played together.
            We used to be the best of friends, playing hide and seek, video games, making our own stories to act out, you name it."
            l "He was always there for me, he supported me however he could and appreciated me."
            n "When she talks about her brother you can see one of the biggest smiles you've ever seen growing on her face."
            l "But that's when it happened..."
            n "Lilith pauses for a moment as she gasps for air, you can see tears dripping off her face."
            l "He was only seventeen when he got hit by a speeding car.
            He didn't die immediately, they say he must have layed there for an hour before..."
            l "My... father..."
            n "She seems to test the taste of those words, looking at her expression, they seem to taste quite bitter."
            l "David couldn't accept James dying and left us.
            That day two people were taken away  from me by a car.
            Actually, scratch that, David had a choice in the matter, James was the only one really taken away from me."
            l "Mom really tried her best to fill the void left by them but the presence of their absence has always haunted us since that horrible day."
            if persistent.joke_knowledge == True:
                l "My sister, Abigail, the one from the joke you just told, is 5 years younger than me so she doesn't really remember much of what happened."

            else:
                l "My sister, Abigail, is 5 years younger than me so she doesn't really remember much of what happened."
            #TODO Make this a flag. Also rewrite that line slightly.
            n "She lets out a sigh of relief."
            l "As much as it hurts me to talk about James it feels good to finally let it all out once again.
            Thank you for listening to me ramble on [name]."
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
    l "Oh, I'm glad you asked [name]!"
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
        "I'll definetly have to check some of those bands out one day, thank you for the tip Lilith!":
            l "You're totally welcome [name], I always love recommending music to people, I like to think music has a really strong impact."
            l "After all, it can make you feel all kinds of emotions, calm you down, energise you, even relief pain slightly."
            l "Isn't that wonderful?"
    l "But anyway, what are your favourite bands and genres of music [name]? "
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
    l "I also really enjoy to read Haruki Murakami's works, an old friend of mine introduced me to them and since then I've read 'First person singular', 'After dark' and '1q94'."
    l "He has a hauntingly beautiful way of describing even the most mundane things. It's like I can see the world for the first time again but not through my eyes, through his instead."
    l "I love it when someone can make me look at mundane things in a whole new perspective."
    l "So, which books do you like to read [name]?"
    menu:
        "I really like-":
            jump restaurant_death_2
