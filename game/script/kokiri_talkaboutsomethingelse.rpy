label kokiri_talkAboutSomethingElse:

    $ kokiri_conversation += 1
    $ kokiri_meteoritewarn()

    if poem_conversation == True:
        $ poem_conversation = False
    if kokiri_conversation < 4:
        menu:

            "I am a crosser, I basically travel across different realities almost exactly like this one. So I don't really undo what I caused, you died [persistent.lildeaths] times already and I can only try to make sure you won't die again. ":
                l "Interesting... so my previous deaths weren't prevented, they all happened in another reality?"
                l "What made you come to that conclusion?"
                menu:
                    "The game told me.":
                        l "Are you sure that you trust the game enough to take it's word?"
                        l "First and foremost you are just a player of this game, right?"
                        l "So while what you said might be true in the boundaries of this game, it doesn't really apply to you as you sit behind your screen."
                        menu:
                            "Yes but that still doesn't stop it from being real here. There are other universes were you died because of me.":
                                l "That could very well indeed be the case [name]..."
                                n "Lilith seemingly sinks deep into thought for a moment."
                                l "But is everything that is describe in this game automaticaly real?"
                                l "What if I told you right now that I have a pet rock called Bobby? Would they become real by me just saying that?"
                                menu: 
                                    "Well no, because right now I know you're just saying something to make a point.":
                                        l "Exactly [name]. But isn't that what most forms of fiction are? Saying something to make a point?"
                                        l "Saying something because the author felt like it, because they think it fits well with the themes. Because it feels like the logical way for things to go."
                                        l "None of this is real, but that's not a bad thing, it means you can choose which parts you would like to be real and which parts you wouldn't. You have the power to reshape this world to your liking."
                                        l "So do I really die in multiple universes? Maybe."
                                        l "Does that thought absolutely terrify me? Definetly."
                                        l "But that does not mean you have to accept whatever the game tells you? No."
                        $ kokiri_conversation_silent()

            "Do you believe in determinism?" if persistent.kokiri_determinism_knowledge:
                l "That is a very interesting question [persistent.name]!"
                l "I think it really depends on what you mean with that question."
                l "If you are asking me wheter or not I think someone could predict the future perfectly I'd have to be inclined to say no."
                l "I think it's kind of like billiard balls, picture like 100 of them all moving in a direction, how they would bounce of eachother."
                l "That's already quite hard isn't it?"
                l "Now picture every atom in our universe as a billiard ball, I'm not exactly sure how many atoms there are specifically but I know it's more than you could count in a lifetime."
                l "Picture all of those billiard balls interacting with eachother, steering eachother in new directions constantly."
                l "Could you tell me where each billiard ball would end up in the next 2 years?"
                l "I don't think so."
                l "What I do think is that you might be the perfect person to test that though."
                l "I believe that even though it would be impossible to predict the state of the future from the past it is possible that the future would always be the same if the circumstances are the same."
                l "So in other words, if you play the game once again from the start and you make the same choices like you did right now, you would once again read this conversation with me since I don't remember it and all circumstances are the same."
                l "Does that sound like it might be true [persistent.name]?"
                menu:
                    "Well, there is this one thing you did that might support that. You threw 2 dice in cafe for some sort of puzzle." if persistent.dice_counter >= 2:
                        menu:
                            "You have done it [persistent.dice_counter] times now and each time the results are the exact same.":
                                l "Ooh, that is very very interesting [persistent.name]!"
                                l "That would mean there is such a thing as fate, isn't there?"
                                l "Maybe not a fate that dictates what is going to happen next, but one that makes sure that whatever has happened will happen again under the same consequences."
                                l "Would that give us free will? Where we are free to choose what happens the first time and after that we are always bound to that?"
                                l "Or was there a time before the first time that keeps us from doing what we truly want?"
                                l "Is there a difference if each time we make the same choice, believing it to be our free will?"
                                l "I suppose ignorance is bliss, isn't it [persistent.name]? So maybe it's better that we don't answer that question."
                                #TODO: Insert some more geeking out. Also rewrite the line below a bit.
                                l "I'm sorry if I'm geeking out, I guess this is just a welcome distraction from what is to come..."

                    "I don't know, it might be slightly true yes, but even when I do the exact same things some very small things can change." if persistent.kokiri_heraclitus_knowledge:
                        menu:
                            "Like things the narrator says, or things I think. Pantha Rhei and all that, isn't it?":
                                menu:
                                    "While everything around us might be the same, the fact that both me and the narrator keep our memories changes the way the machine works.":
                                        menu:
                                            "Because the both of us are cogs inside of it aswell.":
                                                l "Ah I see, I guess that is a fair point to make."
                                                l "You could peace a machine back together under the exact same circumstances, cog by cog, piece by piece."
                                                l "But you would atleast need an observator to notice that nothing changed"
                                                l "But for that observator to notice that they would need to remember how the machine functioned previously."
                                                l "Which means it might not be possible to ever witness the same exact thing twice." 
                                                l "They might get very very close, so close that it's hard to tell the differences."
                                                l "And yet, there is one striking difference, the observator themselves, they remember the previous state of the machine and thus the machine is not perfectly resembling the one before it, because that one was the first for the observator. "
                                                l "It seems like it's the same thing for you, things seem to be very very similair to each attempt if you do the same things but there are some minor differences."
                                                l "Even if there weren't, you'd still remember your past attempts, which means something did indeed change."
                                                l "Pantha Rhei and all that, just like you said."

            "*Tell her about the mayo easteregg*":
                    #TODO: change the link text slightly and fill this in. (No quest precedent)
                    l "Interesting, so you managed to \"fight\" the narrator?"
                    l "And you {b}won{/b}?"
                    l "Even if it's about something so silly as eating nothing but mayo."
                    l "It might be a lead for us to get through this whole ordeal."
                    l "I wonder if there are any other ways to deal with the narrator."
                    $ kokiri_conversation_silent()

            "You actually showed me a poem of yours on one date we had in the burger restaurant. I really liked it, could you show me another one?" if not conversationtracker_poems and persistent.burger_poem_knowledge:
                    $ kokiri_conversation -= 1
                    jump kokiri_poems

            "This game is controlled by a Narrator." if not conversationtracker_tellheraboutnarrator:
                jump tellLilithAboutNar


            "Ask her something about her family.":
                    $ kokiri_chatchar_abigail_recent = False
                    $ kokiri_chatchar_james_recent = False
                    $ kokiri_chatchar_david_recent = False
                    $ kokiri_chatchar_lila_recent = False
                    menu:
                        "Ask about Abigail":
                            menu:
                                "Can you tell me about Abigail?":
                                        jump askAboutAbigail_tellMeAbout
                                "Abigail uses the same program the prototype of this game is made in." if not conversationtracker_questmade:
                                    jump kokiri_topic_questMade
                        "Ask about David":
                            #TODO: Some stuff to implement across the three conversations that are possible to reach:

                            #Why did Lilith's father leave the family? (Work, personal reasons, conflicts)
                            #How did his absence affect Lilith while growing up? (Emotionally, financially, etc.)
                            #Is there any chance of reconciliation between Lilith and her father? (Regrets, hopes, concerns)
                            #What role did he play in the family before he left? (Breadwinner, caregiver, etc.) BREADWINNER, afterwards mom had to take a double job because she refused his money, but Lilith doesn't know that.
                            menu:
                                "Can you tell me about David?":
                                    jump askAboutDavid_tellMeAbout
                                "Do you blame your father for what happened to James?" if persistent.david_blame_knowledge and not conversationtracker_blamedavid:
                                        $ conversationtracker_blamedavid = True
                                        l "What? That's absurd."
                                        l "I have never blamed him for James'... passing."
                                        l "I am just really mad at him for abandoning his family because he couldn't deal with what happened to James."
                                        l "Why are you asking such a question [persistent.name], you haven't been seeing my dad, have you?"
                                        n "It seems you just struck a sensitive chord."
                                        menu:
                                            "I have actually, he said he wants to come back every day but can't because you and Lisa hate him for what happened with James.":
                                                l "First off I'd like you to not contact my dad again even though I can't stop you from doing so."
                                                l "But as you now know I don't blame him for James' death and I don't think mom does either."
                                                l "We were mad for him leaving us, I still haven't forgiven him."
                                                l "Mom seemingly did though, I guess it's because of her trust in humanity." #TODO: Because dad still wanted to give money, she just didn't want to accept it.
                                                menu:
                                                    "Would you forgive him if he made an apology?":
                                                        $ persistent.david_apology_knowledge = True
                                                        #Don't put this choice in the other subpath where you deny talking to him, because it wouldn't make much sense.
                                                        l "I'm not sure I would even want to hear him out."
                                                        l "...But let's say I did, if it's a good apology then maybe he would be a step closer to rebuilding our bond but it won't be the same for a long time, maybe it will even never be the same."
                                                        l "However, I think the girl he left all those years ago, the girl that is still somewhere inside of me, would at the very least like the idea that he made an effort to come back to us."
                                                        $ kokiri_conversation_silent()

                                            "No, I haven't talked to him. I was just curious because I got the impression you hated him for what happened to James from a conversation we had in a previous time.":
                                                l "I see, I definetly do have some resentment for him since he left us alone but I don't think he could have saved James somehow."
                                                l "Alright, now that's all cleared up."
                                                l "It's a relief to hear you haven't contacted my dad yet, I'd prefer if you never did at all, even if given the option somehow."
                                                l "I'd prefer if you didn't  anyone of my family, but especially not David."
                                                menu:
                                                    "Of course! I would never contact someone of your family. (Lie)":
                                                        #Karma
                                                        l "Thank you [persistent.name]!"
                                                        l "It means a lot to me that I can trust you with something like this."
                                                        n "I see..."
                                                        n "So now you are just lying to her face?"
                                                        n "You might think this doesn't have any consequences."
                                                        n "Is that why you are doing this?"
                                                        n "Or is it because you want to read each line of potentially new dialogue, no matter what you have to do to reach it?"
                                                        n "..."
                                                        n "Don't bother answering that, you got your consequence free new dialogue, now let's move you back on track."
                                                        $ kokiri_conversation_silent()
                                                    "And what if contacting someone of your family could potentially save you?":
                                                        #TODO: Fill in, I think there already exists something similiar in quest. Lilith is not really comfortable with the idea, she doesn't like to potentially harm her family like that.
                                                        "Filler"
                                                        $ kokiri_conversation_silent()
                        "Ask about James":
                            menu: 
                                "Can you tell me more about James?":
                                    jump askAboutJames_tellMeAbout
                                #TODO: Fill in this link below and the third option for the ask about james thingy.
                                "I know that you kept James' number in your phone after he..." if persistent.keptJamesNumber_knowledge:
                                    #TODO: Make that link above also check if you know he died.
                                    menu:
                                        "Are you the one who keeps calling that number?" if persistent.lilithKeepsCalling_knowledge:
                                            "Filler"
                                "This will sound weird but I'm asking to understand better. In your phone you saved James' number, right? But when I called that number the person claimed to be someone else, and they had never heard of you before." if not persistent.keptJamesNumber_knowledge and persistent.lilithKeepsCalling_knowledge and persistent.jamesFakoutNumber_knowledge:
                                    $ love_points = -2
                                    $ love_meter_updater()
                                    l "You did what?"
                                    l "I guess I appreciate your honesty but what I don't appreciate is you trying to involve my family in all of this."
                                    l "And don't try to fool me into thinking another version of me agreed to this, I think no version of me would ever do something like that."
                                    n "Lilith takes a few deep breaths in and out."
                                    l "Sorry if I got a bit too agressive there [persistent.name], I guess I'm just defensive about my family."
                                    l "Just to be clear, don't ever involve them in any of this, alright?"
                                    $ persistent.restrainingorderfamily_knowledge = True
                                    n "You give her a quick nod, scared of invoking her fury once again."
                                    l "Good, now that that's settled I guess I owe you an explanation."
                                    l "It is true that that number doesn't belong to James anymore, but it used to one day."
                                    l "I'm surprised you haven't heard this before during your previous dates with me but James, well, he... died a long time ago."
                                    l "I know I should probably try to move on and delete the number but I just can't bring myself to do it."
                                    l "It's as if another piece of him would die when I delete it."
                                    l "Sometimes I indeed even call the number, just to pretend that I can hear him on the other side."
                                    l "But each time I do that I feel so ashamed of what I'm doing that I just hang up the phone as fast as I can."

                        "Ask about Lila":
                            menu:
                                "Can you tell me about Lila?":
                                    jump askAboutLila_tellMeAbout






    else:
        jump kokiri_death_3_death_dialogue

label tellLilithAboutNar:
    $ conversationtracker_tellheraboutnarrator = True
    #(This one actually is already integrated into the main path, I think the first one, so it's probably better to remove it.
    #TODO: Check if it is really integrated or not.
    #Is it really? I think just saving it here can be beneficial so the player has more choice on what they can talk about.
    l "I'd like to meet this Narrator you're talking about."
    n "... No one ever asked to do that before."
    n "Tell her I said hi."
    menu:
        "Well, he just said hi.":
            jump tellLilithAboutNar_justSaidHi
label tellLilithAboutNar_justSaidHi:
    l "Interesting."
    l "How are you doing mister Narrator?"
    l "Oh please, mister Narrator is my father's name, just call me Nar. That's what my friends tend to call me."
    menu:
        "He said: \"Oh please, mister Narrator is my father's name, just call me Nar. That's what my friends tend to call me.\".":
            jump tellLilithAboutNar_callMeNar
label tellLilithAboutNar_callMeNar:
    l "Alright then Nar, how are you doing?"
    n "No one ever asked me that before, not even you [persistent.name]..."
    n "Don't tell her I said that!"
    n "Just tell her that I said that I'm doing good, that I'm busy with narrating the story."
    menu:
        "He said no one has ever asked him that before.":
            jump tellLilithAboutNar_neverAskedBefore

        "He said that he's doing good and that he is busy narrating this story.":
            jump tellLilithAboutNar_goodAndBusy


label tellLilithAboutNar_neverAskedBefore:
    #TODO: Fill this out a bit more (no quest precedent)
    "Filler"
    $ kokiri_conversation_silent()


label tellLilithAboutNar_goodAndBusy:
        l "That's good to hear and wow that's really cool! "
        l "{size=*0.5} Even though technically you are now narrating him [persistent.name].{/size}"
        l "So do you control where our story leads Nar?"
        n "Yeah, I basically steer the story in the right direction and when we are off track I try my best to get us back on track."
        menu:
            "He said that he steers the story in the right diection and when we somehow get off track he gets us back on track.":
                jump tellLilithAboutNar_storySteerer
label tellLilithAboutNar_storySteerer:
    
    l "Funny that you mention that Nar, I was just thinking about that."
    l "Do you steer us towards my deaths?"
    n "Well yes, but I don't always do. There are plenty of endings where you make it out alive. It's just that [persistent.name] usually doesn't end up with you when that happens."
    menu:
        "He said that he has to but that there are also some alternatives, like endings where you are still alive but we don't end up together.":
            jump tellLilithAboutNar_endingsWhereYouLive
        "He said he has to, that all endings end up with you dying.":
            jump tellLilithAboutNar_noEndingsWhereYouLive

label tellLilithAboutNar_noEndingsWhereYouLive:
    n "So you are just going to lie to her now?"
    #TODO: Add some more text here before you move the player back.
    $ kokiri_conversation_silent()



label tellLilithAboutNar_endingsWhereYouLive:
    l "Well, could you maybe steer the story to a direction where [persistent.name] and I end up together and I get to live?"
    n "But that would destroy the entire point of this game!"
    n "And even worse, it would all be for nothing because then [persistent.name] would just stop playing the game without having learnt anything."
    menu:
        "He says that would destroy the entire point of the game and that I would stop playing before ever learning anything.":
            jump tellLilithAboutNar_destroythepoint
label tellLilithAboutNar_destroythepoint:
    l "I see... and what is the point of this game if you don't mind me asking?"
    n "Well, it is quite simple actually, one of the main points is..."
    n "No, I'm not supposed to tell you and [persistent.name] that, it's more impactful when they discover it on their own or with you."
    menu:
        "He says he's not supposed to tell us. That it is more impactful when I discover it on my own or with your help.":
            jump tellLilithAboutNar_secret
label tellLilithAboutNar_secret:
    l "Oh come on Nar, please?"
    n "No, do not push me Lilith. I can't tell you."
    menu:
        "He said that you shouldn't push him and that he still can't tell you.":
            jump tellLilithAboutNar_doNotPush
        "Push him a little more, we're so close to getting an answer.":
            jump tellLilithAboutNar_push
label tellLilithAboutNar_push:
    l "Pretty please Nar? Won't you tell me?"
    l "I don't deserve to die over and over and over, right?"
    l "I am scared of what is going to happen to me."
    l "Of dying that death."
    l "I am scared of dying it so much that instead I start living it."
    l "Can't you atleast offer me some peace of mind before my mind gets snuffed out once more?"
    n "..."
    n "I'm so sorry Lilith. I wish there was a different way for me to tell the story."
    n "Or maybe a different story?"
    n "The truth is if you are reading this you probably haven't found it yet."
    n "Can't you see player? All you have to do is-"
    $ persistent.fakeoutnar_tip = True
    return
label tellLilithAboutNar_doNotPush:
    n "Alright, I understand."
    n "All I can say is that He, the creator of this world and game, wants the player to find the answer to your question so surely they will stumble upon it eventually."
    menu:
        "He said that the creator of this game wants me to figure out the lesson so that we surely will stumble upon it eventually.":
            jump tellLilithAboutNar_stumbleUponLesson
label tellLilithAboutNar_stumbleUponLesson:
    l "Thank you Nar, I appreciate it!"
    l "Also, I'm sorry for all the questions but is it possible to meet this creator you are speaking about?"
    n "Fragments of them but never the whole because, just like the player, He doesn't live in this game."
    n "This game can never fully accommodate either of their essences fully."
    n "Also I'm sorry to do this but your time is up, I have to move things along."
    #TODO: Move Lilith to death, in the quest version it moves to "Kak_death_4_hill_2"
    $ kokiri_conversation_silent()


label askAboutAbigail_tellMeAbout:
    $ kokiri_chatchar_abigail_recent = True #This will be used to make sure the player gets put back to the right place in the conversation after the family curiosity checker.
    if kokiri_chatchar_abigail == False:
        $ kokiri_chatchar_abigail = True
        $ kokiri_chatchar_abigail_counter = 1
        $ conversationtracker_abigail = True
    else:
        $ kokiri_chatchar_abigail_counter += 1


    $ family_curiosity_checker()
    if kokiri_chatchar_abigail_counter == 1:
        jump askAboutAbigail_tellMeAbout_1
    elif kokiri_chatchar_abigail_counter == 2:
        jump askAboutAbigail_tellMeAbout_2
    elif kokiri_chatchar_abigail_counter == 3:
        jump askAboutAbigail_tellMeAbout_3

label askAboutAbigail_tellMeAbout_1:
    l "Well, as you probably already know Abigail is my little sis."
    l "We went through a lot like most sisters but we always managed to get through it all."
    l "...This stays between us alright [persistent.name]?"
    l "...Lately I've had this weird feeling."
    l "As if there's something Abigail is hiding from me."
    l "She has always been the happy type but now there's something underlying in that happiness, something almost forced."
    l "She seems as if she's putting up a performance for someone."
    l "I really hope I am just wrong and that she just is happier than I have ever seen her for a positive reason."
    l "But I like to think that I know Abigail quite well and my guts are telling me something's wrong."
    l "I just wish she would open up about it if there truly was something going on."
    $ persistent.kokiri_abigailhidessomething_knowledge = True
    menu:
        "You might want to call her.":
            if kokiri_conversation == 1:
                $ kokiri_call = True
                $ kokiri_chatchar_abigail_called = True
                a "Heya Lilly!"
                a "You're calling pretty soon, did your date with [persistent.name] not go well?"
                l "I am still on my date actually." 
                l "And currenctly it is really great!"
                l  "{size=*0.5}If not a little hard to wrap my head around.{/size}"
                a "Oh? Then why are you calling?"
                l "Well, it's kind of hard to explain..."
                a "I see, no worries Lilly!"
                a "Is your phone on speaker currently?"
                l "Yes it is, why?"
                a "{size=*2}Heya [persistent.name], treat my sis nicely will you?{/size}"
                l "Abby, you're going to scare [persistent.name] off like that."
                a "Good, then you'll have to give me all of your attention again!"
                a "I'm kidding, I'm kidding, I hope you're having fun on your date so far."
                l "Well it surely has been interesting so far."
                l "But enough about me, I'd rather talk about you for now."
                a "About me? I'm flattered!"
                a "What do you want to talk about?"
                l "Is something wrong lately?"
                a "...What do you mean?"
                l "Is something wrong with you lately? You have been even more chipper than ever as of late."
                l "...It almost feels forced. As if you're trying to hide something."
                a "Why are you asking me that?"
                l "Because I care about you of course! You are and always will be my sister Abby, don't you ever forget that."
                $ kokiri_call_potentialdeathcheck() #This serves as a break in the call if you have never seen the meteorite, if you have you should have been able to warn her beforehand.
                a "That's really sweet of you Lilly! But I actually mean why are you asking me that now, during your date with [persistent.name]?"
                menu:
                    "*Nod your head*":
                        l "Well, I sort of will die during this date."
                        a "... What?..."
                        a "Is this a joke?"
                        a "Was this [persistent.name] their idea?"
                        a "{size=*2}This is not funny [persistent.name]!{/size}"
                        l "Abby, please, stop yelling..."
                        l "It's not a joke."
                        l "It's kind of hard to tell you why we think I will die but [persistent.name] has made it clear that there is atleast something strange going on."
                        l "And before I... go... I wanted to make sure you were alright."
                        a "...So it's true?"
                        l "Well if it isn't we will atleast have talked through your problems and we will have a very silly story to tell everyone."
                        a "I'm going to make fun of you if this isn't true, you'd put mom her naivite to shame."
                        l "I'd like that."
                        a "To be made fun of?"
                        l "No, I'd like that all of this turned out to be false. That I would be able to see you in person again."
                        a "...Please, can we continue talking about me? This is a lot to take in."
                        l "...I guess we can. I don't think I have much time left any way."
                        a "..."
                        a "So, you asked me if something was wrong with me right?"
                        a "Well, to be honest there is."
                        a "Lately I have been feeling so alone."
                        a "That feeling had increased when you moved out if I have to be honest with you."
                        a "And mom does all she can, I don't want to complain about her. But there is only so much one person can do..."
                        l "I see..."
                        a "And that feeling of loneliness even affects my thoughts. I'm not sure if my friends really like me, even if they literally say so."
                        a "Some days it never shows up."
                        a "And other days it seems to never leave my head."
                        a "But it always comes back in the end."
                        a "It just gets so cold sometimes Lilly."
                        l "Abby, I had no idea...
                        I am so sorry I never asked you about this earlier.
                        I had this feeling in my guts, I should've asked earlier."
                        a "Hey, don't blame yourself!
                        I probably wouldn't have told you.
                        I didn't want you or mom to worry about me.
                        That's why I tried to act like nothing was wrong. I thought I was doing a great job but apparently not."
                        l "You are doing  a great job! You're telling me about this.
                        That way I can help. Or atleast make sure you are heard.
                        I will always be there for you Abby, even when I am... not here anymore.
                        I wish I could tell you that loneliness you are experiencing ever fully goes away.
                        It doesn't. You will have to live with it. You will have to keep trying to highten your resitance to it.
                        Promise me that if you ever doubt if a friend truly wants to do something together with you you'll ask them to be sure. It might sound silly but it helps, I promise."
                        n "You motion to Lilith that she doesn't have much time left."
                        l "I have to go now sis."
                        l "You don't want to hear this next part..."
                        l "I love you, thank you for confiding in me."
                        a "{size=*0.5}I wish I could've done it sooner.{/size}"
                        l "And I wish I would have asked you earlier, but what really matters is that it has happened at all."
                        l "I really have to hang up now, I don't have much time left I think."
                        a "Can't you just stay a little longer?"
                        a "I don't want to lose you."
                        l "You'll never lose me Abby, I'll always be near you as long as you can still treasure the memories we made together."
                        a "I know... but I'm so scared."
                        l "Oh I totally understand, so am I. But I think you'll be fine eventually."
                        l "Afterall, you are one of the bravest people I know."
                        jump kokiri_death_3_death_dialogue
                    "*Shake your head*":
                        #TODO: Make Lilith come up with a different reason as to why she called.
                        "Filler."
            else:
                n "Lilith won't have enough time to call if she calls now."
                n "I suggest making sure you don't talk about anything else except this next time."
                n "Let's just talk about something else to her for now."
                jump kokiri_talkAboutSomethingElse

label askAboutAbigail_tellMeAbout_2:
    "Filler"
    #TODO: Fill in (no quest precedent)
    $ kokiri_conversation_silent()

label askAboutAbigail_tellMeAbout_3:
    "Filler"
    #TODO: Fill in (no quest precedent)
    $ kokiri_conversation_silent()

label askAboutDavid_tellMeAbout:
    $ kokiri_chatchar_david_recent = True #This will be used to make sure the player gets put back to the right place in the conversation after the family curiosity checker.
    if kokiri_chatchar_david == False:
        $ kokiri_chatchar_david = True
        $ kokiri_chatchar_david_counter = 1
        $ conversationtracker_david = True
    else:
        $ kokiri_chatchar_david_counter += 1



    $ family_curiosity_checker()
    #Try this out as as a way for you to learn how to use functions in renpy.
    #If it does not trigger continue to the part below this.
    if kokiri_chatchar_david_counter == 1:
        jump askAboutDavid_tellMeAbout_1

    elif kokiri_chatchar_david_counter == 2:
        jump askAboutDavid_tellMeAbout_2

    elif kokiri_chatchar_david_counter == 3:
        jump askAboutDavid_tellMeAbout_3

label askAboutDavid_tellMeAbout_1:
            l "What is there really to say about him? He abandoned us right when James died."
            l "When everyone needed him the most he just dissapeared out of our lives as if it was him who died that day and not James."
            l "Mom was devasted by both James and David's absence in all of our lives but she kept trying her best for Abigail and me."
            #TODO: Put some extra stuff in between here.
            l "Of course I know he was heartbroken by James' death, we all were."
            l "Even though that is an explanation for why he left us it is not an excuse, not a valid one atleast."
            l "Our family were the only ones who understood how it felt to have lost James, together we tried to deal with those feelings." #TODO: Make it so that James didn't really have friends, he had trouble being understood by them. That way this sentence makes sense.
            l "Together, while he was hiding away god-knows-where from the rest of us."
            #TODO: Add a/some choice(s) here for the player to reply.
            $ kokiri_conversation_silent()

label askAboutDavid_tellMeAbout_2:
            l "My father loves all things related to cryptography."
            l "When he still lived with us he would give me a a postcard for every birthday."
            l "That postcard had an encode message on it."
            l "Then I had to decipher the code to reveal a list of cryptic instructions that would lead me to a gift."
            l "Sort of like a scavenger hunt I suppose."
            l "I liked it a lot to be honest. It felt as if we had a sort of hidden language to communicate in with eachother."
            menu:
                "I haven't heard you talk about a lot of happy memories with your father, how does sharing that story make you feel?":
                    l "I was a bit hesitant to tell this story because of the pain it might make me feel but I'm actually glad I told it."
                    l "It felt... kind of good? Almost as if everything was back the way it used to be."
                    l "It's been so many years since I last got a postcard from him that the memory of that ever happening is almost getting a bit fuzzy."
                    n "Lilith starts sobbing."
                    l "I'm sorry to unload all of that on you [persistent.name], you don't deserve this."
                    menu:
                        "I understand that you feel like that Lillith but I don't mind at all. Besides, you deserve someone who can listen to you.":
                            n "Lilith is still crying quite hard but you can see a slight smile forming."
                            l "I... suppose you're right [persistent.name]. That is really sweet of you. Thank you."
                            l "I just... need a moment to compose myself."
                            n "Lilith plants her head on top of her knees and stays like that for a long while."
                            n "You can still hear her sobbing but it seems to grow more quiet over time."
                            l "There, I'm feeling a bit better already!"
                            l "Honestly, crying like that might be exactly what I needed."
                            l "Thank you for comforting me [persistent.name]! I really appreciate it."
                            l "Knowing that we don't have unlimited time makes me really thankful that you chose to spend that time to make sure I was okay."
                            $ kokiri_conversation += 1
                            $ love_points += 2 #This gains you 2 love points but as a sacrifice you lose an additional topic to talk about.
                            $ love_meter_updater()
                            $ kokiri_conversation_silent()


label askAboutDavid_tellMeAbout_3:
            "Filler"
            #TODO: Fill in.
            $ kokiri_conversation_silent()

label askAboutJames_tellMeAbout:
    $ kokiri_chatchar_james_recent = True #This will be used to make sure the player gets put back to the right place in the conversation after the family curiosity checker.
    if kokiri_chatchar_james == False:
        $ kokiri_chatchar_james = True
        $ kokiri_chatchar_james_counter = 1
        $ conversationtracker_james = True
    else:
        $ kokiri_chatchar_james_counter += 1
    $ family_curiosity_checker()
    if kokiri_chatchar_james_counter == 1:
        jump askAboutJames_tellMeAbout_1
    elif kokiri_chatchar_james_counter == 2:
        jump askAboutJames_tellMeAbout_2
    elif kokiri_chatchar_james_counter == 3:
        jump askAboutJames_tellMeAbout_3

label askAboutJames_tellMeAbout_1:
    l "So I previously told you about James?" #TODO: Make it so that if she talked about James during this loop she doesn't say these lines.
    l "That makes a lot of sense."
    l "Well, stop me if you hear something I already told you, alright?"
    l "James was the best brother I could have ever wished for."
    l "It feels weird to acknowledge his death, even after all those years."
    l "Sometimes I even forget he has passed. It usually only lasts for a minute or two but that's one of my favourite moments."
    l "At moments like that he just feels so much closer."
    l "It almost feels as if he will be eating pancakes when I enter the kitchen and he will wave at me while his muth is just absolutely covered in maple syrup." #TODO: (Write this sentence out more for extra emotional gutpunch)
    l "Each time I enter the kitchen and am greeted by the absence of James and the smell of pancakes it feels as if a part of me is withering away."
    l "I know it is silly, after all those years..."
    l "I moved into my own place so it's not even the kitchen we grew up in together."
    l "And yet..."
    l "I will always leave a chair available for him."
    menu:
        "It's not silly at all Lilith. In fact I think it is beautiful. Grief isn't a process that is bound to time.":
            l "Wow [persistent.name]... I'm not sure what to say."
            l "I have never really thought about it like that before."
            #TODO: Add some more text here.
            $ kokiri_conversation_silent()
    #TODO: Some extra stuff to implement across conversations:
    #What was James like as a person? (Personality, interests, hobbies)
    #What was Lilith's relationship with James like? (Close, distant, complicated)
    #What impact did James's death have on Lilith and her family? (Emotional toll, changes in dynamics)
    #Extra stuff:
    #You know, he always was so full of live.
    #It was weird but everything he did made him seem like he had some grasp on life that few people had.
    #He was going to do big things, I'm sure of it.


label askAboutJames_tellMeAbout_2:

    l "James used to love photography and everything that came with it. So did I actually."
    l "Our father used to be a fan of photography and I think he passed that over to us."
    l "Well nowadays I don't really take pictures anymore. Everythime I tried to pick up a camera I just get reminded of both James and my fath- and David."
    l "I have dropped quite a few camera's when I tried to continue. I think it's for the best if I just stop for now."
    l "But James was extremely good for his age, he always was a quick learner but something about photography just seemed to click fantastically with him."
    l "It was almost as if you could just jump into his pictures and live inside of them."
    l "He used to tell me that a good picture should not just let the person watching it see a moment caught in time but it should also make them envision the future."
    l "In other words, a good picture should almost become a video with the picture as it's first frame."
    l "Personally I aways thought the oposite, a good picture makes you remember the lead-up to that picture, so in a way a good picture is a video with the picture as it's last frame."
    l "I think that's the only reason I can look at a picture of James without tearing up completely. I just see the lead-up to the picture and not the horifying aftermath of it all."
    l "However badly the memory of the aftermath still haunts me, I can't let that be the only part of his life I remember. I want to make sure all the beautiful memories we made throughout all the years will live on as long as possible."
    menu:
        "I think that is beautiful, I will make sure that James and the stories you two shared won't go forgotten.":
            n "Lilith gives you a sincere smile."
            n "The stars shine enough light on her face for you to catch a tear rolling over her cheek."
            l "Thank you [persistent.name]! That would mean a lot to me."
            l "Even if I don't make it to the end of this day, you will."
            l "Atleast the memories of James won't end up dying with me."
            l "That gives me some comfort."
            l "Don't get me wrong, I'm still terified."
            l "I mean, rightfully so."
            l "But at the very least it makes it slightly easier to cope with whatever will come next."
            $ kokiri_conversation_silent()

label askAboutJames_tellMeAbout_3:
        l "The house we grew up in had a field that mostly grew corn on the opposite side."
        l "We used to have a game where one of us would enter the field and crawl around in it while the other person tried to find them."
        l "Usually the hider has to say something every minute so that it's a bit more doable to find them."
        l "Well one day he was the hider and I was the searcher."
        l "He hadn't said anything for the entire time and so I had no idea where he could possibly be."
        l "The tension was high."
        l "Suddenly James popped out of the corn and picked me up while he spun around."
        l "He then put me down and layed down between the corn."
        l "I layed down beside him and we just looked at the sky while talking about all sorts of things."
        #TODO: (Continue this story and expand it a bit more: What kind of things? Needs more fleshing out)
        $ kokiri_conversation_silent()

label askAboutLila_tellMeAbout:
    $ kokiri_chatchar_lila_recent = True #This will be used to make sure the player gets put back to the right place in the conversation after the family curiosity checker.
    if kokiri_chatchar_lila == False:
        $ kokiri_chatchar_lila = True
        $ kokiri_chatchar_lila_counter = 1
        $ conversationtracker_lila = True
    else:
        $ kokiri_chatchar_lila_counter += 1


    $ family_curiosity_checker()
    if kokiri_chatchar_lila_counter == 1:
        jump askAboutLila_tellMeAbout_1

    elif kokiri_chatchar_lila_counter == 2:
        jump askAboutLila_tellMeAbout_2

    elif kokiri_chatchar_lila_counter == 3:
        jump askAboutLila_tellMeAbout_3


label askAboutLila_tellMeAbout_1:
    l "I really love my mom."

    l "She definetly didn't have it easy."

    l "She had to deal with James' death and David leaving all of us."
    l "She basically raised both me and Lilith ever since David left."
    l "I can't imagine it having been easy for her but she never really talked about it whenever I asked her."
    l "I think she wanted to make sure we were able to grow up with as little worries as possible."
    #TODO: Write out this conversation a bit more and rewrite it slightly.
    menu:
        "You might want to call her.":
            if kokiri_conversation == 1:
                $ kokiri_call = True
                $ kokiri_chatchar_lila_called = True
                l "Hey mom?"
                li "Yes sweetie?"
                l "Can I ask you something?"
                li "Is everything alright Lilly?"
                li "Did your date not go well?"
                l "Oh no, everything went-"
                l "Everything is going great!"
                li "Oh... that's fantastic news!"
                li "{size=*2}But doesn't that mean that your date can hear our call?{/size}"
                l "Oh no, it's fine, [persistent.name] just went to the toilet, so we have some time."
                n "Lilith gives you a wink, it's a lie but you're impressed how convincing she made it sound."
                li "So, what did you want to ask me then sweetie?"
                l "Well, I have been wondering something for quite a while."
                l "You took up an inmense burden with taking care of us on your own right? "
                l "The stress you felt..."
                l "Why did you never tell us?"
                li "You two were never a burden on me and never will be alright? Try to remember that very well please."
                li "And what would I have needed to tell you two? That I was barely scraping by?" #TODO: To have the dad still send checks, make the mom not accept them because she is hurt that he left. She doesn't tell this directly but the dad does when confronted. #Make the todo be something you can learn and can ask David about.
                li "That I felt like I was living three lives and neither of them were mine?"
                li "That I felt abandoned by your father?"
                l "You should have told us, we could have-"
                li "{size=*2}Could have done what?{/size}"
                li "The two of you were just two little girls."
                li "I didn't want to burden any of you with growing up too fast."
                li "So I guess I grew older twice as fast so both of you could stay young."
                li "But when I see you and Abby, I can't help but smile. Because I know all of my work has been worth it."
                li "Every grey hair has been worth it."
                li "The two of you are my greatest treasure. And so was James. "
                li "... And so is James."
                l "Don't you ever feel like you wasted your life on us?"
                li "Of course not! The three of you made my life much more rich."
                li "I loved going on our little trips together, the memories still make me feel warm and fuzzy if I try to recall them."
                $ kokiri_call_potentialdeathcheck()
                li "I'm very sorry to hear that you've been carying this sort of guilt with you for so long sweetie."
                li "I wanted to prevent that exact thing from happening, that's why I tried to not show the stress I'd feel."
                li "But you were always quite good at figuring people out, I guess it was silly of me to think that shielding you from my stress would work."
                li "If anything I'm happy that we can have this conversation, that I can atleast help ease your burden slightly."
                li "Which leads me to a question."
                li "Not that I'm complaining ofcourse! But why do you ask me about something that happened so very long ago now of all times? "
                l "Well..."
                l "Lilith gives you a questioning look, she seems unsure of what to say."
                menu:
                    "*Nod your head*":
                        n "She gives you a nod back, it might not be easy news to bring but her mom deserves to hear the truth."
                        l "This might sound weird but I  have very good reasons to believe I won't survive past today."
                        li "...What?"
                        li "And what are those good reasons?"
                        li "This is very hard to explain..."
                        li "Basically, I already have died before on this day."
                        li "We are in a sort of loop where I keep dying over and over."
                        li "Oh no, that's horrible."
                        li "Not my daughter, not you..."
                        li "I can't lose another child, I don't think I could deal with that."
                        n "Lila seems to be in a panicked state."
                        l "Mom, I don't have much time, please take some deep breaths and try to calm down a bit, I know it is way too much to take all at once, but can you do that for me?"
                        li "I... Yes I can sweetie."
                        n "She takes such deep breaths in and out that you can hear it through the phone."
                        li "Is there anything I can do to help? Something that can fix all of this?"
                        l "I'm afraid nothing can fix this... You've already done enough, you helped me ease my mind a bit."
                        l "Not to forget that you took care of me so wondefully all my life."
                        l "Thank you mom."
                        l "I love you."
                        l "Please take good care of Abby alright?"
                        l "She will be all that's left."
                        li "You'll never be fully gone sweetie, never fully forgotten."
                        li "Me and Abby will always remember you."
                        li "Just like James."
                        l "I'd like that, maybe I will get to see him soon."
                        l "I will never forget both of you aswell."
                        li "If you see James... can you tell him I still think about him all the time?" 
                        $ persistent.LilaStillThinksAboutJames_knowledge = True
                        l "I'm sure he knows mom... but I will tell him."
                        n "You motion to Lilith that she doesn't have much time left."
                        l "I'm going to hang up now mom, what comes next won't sound pretty..."
                        l "I love you."
                        
                    "*Shake your head*":
                        n "She nods, this is too much to burden her mom with."
                        l "Well, I used to ask you about it when I was younger but you never really answered my question."
                        l "And I guess my date with [persistent.name] inspired me to give you a call about it."
                        li "Did I?... I'm so sorry I did Lilly, I guess even then I was trying to protect you in my own way."
                        li "I hope you never were angry with me because of that."
                        li "Seeing how even after all this time, you still remember that happening..."
                        li "It must have affected you very deeply."
                        l "It's alright mom, I'm fine."
                        l "You said I was good at figuring out people, right?"
                        l "Well, I always knew that you loved us, that you tried to do what you thought was right for us."
                        l "So how could I ever be mad at that?"
                        l "So how could I ever be mad at you?"
                        li "Lilly... thank you. I ...I don't really know what to say."
                        l "That's alright mom, you don't need to say anything."
                        l "I understand."
                        l "I'm also glad we could clear this up."
                        li "I'm like an open book to my little girl."
                        l "Mom, I'm far from little now."
                        li "I guess you're right sweetie, if anything this call made that all the more clear."
                        li "I'm proud of you, you know?"
                        li "Now, I'll hang up, alright?"
                        li "I don't want to interrupt your date too much after all."
                        l "Good thinking mom, although you never interrupt."
                        li "I know, I know. Love you sweetie, take care!"
                        n "And with that Lilith's mom hung up the phone."
                jump kokiri_death_3_death_dialogue
            else:
                n "Lilith won't have enough time to call if she calls now."
                n "I suggest talking about the same thing again as quickly as possible the next time."
                n "Let's just talk about something else to her for now."
                jump kokiri_talkAboutSomethingElse

label askAboutLila_tellMeAbout_2:
    #TODO: Rewrite this story eventually once it is finished. Especially don't make it start with "you know"
    l "You know, my mom is actually quite naive."
    l "Abby and I like to make fun of her for being too trusting."
    l "It's a beautiful quality of her to be entirely fair but sometimes she just takes it way too far."
    l "I remember this one time where she got a mail from someone claiming to be a rich relative from Canada."
    l "They said that they were going to soon die and that mom was the nearest heir of his fortune." #TODO: Slightly rewrite this story as it's a bit weird Lila would be estatic by someone dying.
    l "Mom was ecstatic, after dad, I mean David, left us money has always been rather tight."
    l "So the prospect of being able to get more money to support us probably increased her trust in the situation."
    l "The \"rich relative from Canada\" said they just needed her to send a hundred euros so he could send her his fortune."
    l "Luckily my mom might be naive but she is not dimwitted."
    l "She asked that guy to just withdraw the hundred euros he needed from her inheritance, that way she would not need to pay the sum."
    l "Of course he didn't agree with that, she found it strange but a part of her still wanted to believe the whole story."
    l "Luckily I remember her asking me what I thought about the mail."
    l "I still was quite young but luckily James had given me a bunch of tips on how to be safe online."
    l "I told mom that it was probably a scammer trying to get her money."
    l "I still remember her being visibly heartbroken by that for a moment when I explained to her what scammers where."
    l "It was almost as if she never had considered the possibility of someone betraying someone else like that."
    l "Which is quite strange considering David had left all of us before that happened."
    #TODO: Add some choices here.
    $ kokiri_conversation_silent()

label askAboutLila_tellMeAbout_3:
    #TODO: Rewrite more and put in more stuff.
    l "You know my mom actually really likes to play games. She has a ton of different consoles that she used to collect as a teenager."
    l "Some of my earliest memories were sitting on the couch and watching mom showing one of her games to both James and me."
    l "And later along Abby was there aswell of course, she also loved watching mom play games. After a while me and James were playing and Abigail was watching us alongside mom."
    l "I used to be more into games than James but Abigail took the cake. Her eyes were glued to the screen whenever we would play and as soon as she could read she started playing some of mom's old games alongside James and me."
    l "She actually was allowed to play earlier but she wanted to understand the story of the games all on her own. She always used to see the games not as just pure entertainment but as worlds of their own, just like ours."
    l "And now she sometimes likes to make her own games. I'm happy that mom taking care of us resulted in a new hobby for Abby."
    l "We kept playing games together, even after James'... death. In a way it made us very connected."
    l "We all are lucky to have a mom like that."
    #TODO: Add some extra choices.
    $ kokiri_conversation_silent()
