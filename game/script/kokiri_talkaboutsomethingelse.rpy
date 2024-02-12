label kokiri_talkaboutsomethingelse:

    $ kokiri_conversation += 1
    $ kokiri_meteoritewarn()
    "kokiri_conversation = [kokiri_conversation]"
    #TODO: Fill in. Also make a very similair page for when you say that you want to continue talking, base yourself of the quest version for this. Most times she'sd get distracted by her prevented death to the point that you could ask her to continue.

    if poem_conversation == True:
        $ poem_conversation = False
    if kokiri_conversation < 4:
        #TODO: Add a function here based on the quest version that throws the deaths at you if you have a certain conversation value.
        menu:

            "I am a crosser, I basically travel across different realities like this one. So I don't really undo what I caused, you died [persistent.lildeaths] times already and I can only try to make sure you won't die again. ":
                #TODO: Rewrite this into something better and write more info.
                l "So you're playing this game and you're a crosser? Is it possible to be both at once?" #TODO: Make her instead say something like "Well, you are a player of a game, right?" "So that story might be true in this game but outside of it it isn't."
                menu:
                    "Well the game told me I am a crosser so I suppose it is possible.":
                        l "Are you sure that you trust the game enough to take it's word?"
                        #TODO: (Put this somewhere else that better fits it. The link text.)
                        $ kokiri_conversation_silent()



            "*Tell her about the mayo easteregg*":
                 #TODO: change the link text slightly and fill this in. (No quest precedent)
                 "Filler"
                 $ kokiri_conversation_silent()

            "You actually showed me a poem of yours on one date we had in the burger restaurant. I really liked it, could you show me another one?" if not conversationtracker_morepoems and persistent.burger_poem_knowledge:
                 $ kokiri_conversation -= 1
                 jump kokiri_poems

            "This game is controlled by a Narrator." if not conversationtracker_tellheraboutnarrator:
                jump telllilithaboutnar


            "(Needs to be made entirely) Ask her something about her family.":
                 $ kokiri_chatchar_abigail_recent = False
                 $ kokiri_chatchar_james_recent = False
                 $ kokiri_chatchar_david_recent = False
                 $ kokiri_chatchar_lila_recent = False
                 #TODO: Remove the text between brackets in this link and also make only the names you already know about appear. If you have seen her phone all the names unlock, if she tells you about david and james only they unlock.
                 #Paste the text here underneath each character from the quest game, I made that system a bit tricky so try to make sure it works here.
                 menu:
                      "Ask about Abigail":
                          menu:
                              "Can you tell me about Abigail?":
                                    jump askaboutabigail_tellmeabout











                              "Abigail uses the same program the prototype of this game is made in.":
                                  #TODO: Make this jump to the thing that already exists and only pop up if the conversationtracker for questmade is not already active.
                                  "Temporary filler to make the game open."
                                  #TODO: Fill in.
                                  $ kokiri_conversation_silent()


                      "Ask about David":
                          #TODO: Some stuff to implement across the three conversations that are possible to reach:

                          #Why did Lilith's father leave the family? (Work, personal reasons, conflicts)
                          #How did his absence affect Lilith while growing up? (Emotionally, financially, etc.)
                          #Is there any chance of reconciliation between Lilith and her father? (Regrets, hopes, concerns)
                          #What role did he play in the family before he left? (Breadwinner, caregiver, etc.) BREADWINNER, afterwards mom had to take a double job because she refused his money, but Lilith doesn't know that.
                          menu:
                               "Can you tell me about David?":
                                   jump askaboutdavid_tellmeabout


                               "Do you blame your father for what happened to James?" if persistent.david_blame_knowledge and not conversationtracker_blamedavid:
                                   #TODO: Check if these are real flags
                                    $ conversationtracker_blamedavid = True
                                    l "What? That's absurd."
                                    l "I have never blamed him for James'... passing."
                                    l "I am just really mad at him for abandoning his family because he couldn't deal with what happened to James."
                                    l "Why are you asking such a question [name], you haven't been seeing my dad, have you?"
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
                                                    #TODO: Figure out how to keep gameflow from this point, maybe move back to talk about something else?
                                                    $ kokiri_conversation_silent()




                                        "No, I haven't talked to him. I was just curious because I got the impression you hated him for what happened to James from a conversation we had in a previous time.":
                                            l "I see, I definetly do have some resentment for him since he left us alone but I don't think he could have saved James somehow."
                                            l "Alright, now that's all cleared up."
                                            l "It's a relief to hear you haven't contacted my dad yet, I'd prefer if you never did at all, even if given the option somehow."
                                            l "I'd prefer if you didn't  anyone of my family, but especially not David."
                                            menu:
                                                "Of course! I would never contact someone of your family":
                                                    #TODO: Fill this in, the narrator calls you a liar etc.
                                                    "Filler"
                                                    $ kokiri_conversation_silent()
                                                "And what if contacting someone of your family could potentially save you?":
                                                    #TODO: Fill in, I think there already exists something similiar in quest. Lilith is not really comfortable with the idea, she doesn't like to potentially harm her family like that.
                                                    "Filler"
                                                    $ kokiri_conversation_silent()



                      "Ask about James":
                          jump askaboutjames_tellmeabout

                      "Ask about Lila":
                         menu:
                             "Can you tell me about Lila?":
                                 jump askaboutlila_tellmeabout






    else:
        #TODO: Make this function as sort of a emergency railroad to move you back to the kokiri death.
        jump kokiri_death_3_death_dialogue

label telllilithaboutnar:
     $ conversationtracker_tellheraboutnarrator = True
     #(This one actually is already integrated into the main path, I think the first one, so it's probably better to remove it.
     #TODO: Check if it is really integrated or not.
     #Is it really? I think just saving it here can be beneficial so the player has more choice on what they can talk about.
     l "I'd like to meet this Narrator you're talking about."
     n "... No one ever asked to do that before."
     n "Tell her I said hi."
     menu:
         "Well, he just said hi.":
             jump telllilithaboutnar_justsaidhi
label telllilithaboutnar_justsaidhi:
    l "Interesting."
    l "How are you doing mister Narrator?"
    l "Oh please, mister Narrator is my father's name, just call me Nar. That's what my friends tend to call me."
    menu:
        "He said: \"Oh please, mister Narrator is my father's name, just call me Nar. That's what my friends tend to call me.\".":
            jump telllilithaboutnar_callmenar
label telllilithaboutnar_callmenar:
    l "Alright then Nar, how are you doing?"
    n "No one ever asked me that before, not even you [name]..."
    n "Don't tell her I said that!"
    n "Just tell her that I said that I'm doing good, that I'm busy with narrating the story."
    menu:
        "He said no one has ever asked him that before.":
            jump telllilithaboutnar_neveraskedbefore

        "He said that he's doing good and that he is busy narrating this story.":
            jump telllilithaboutnar_goodandbusy


label telllilithaboutnar_neveraskedbefore:
    #TODO: Fill this out a bit more (no quest precedent)
    "Filler"
    $ kokiri_conversation_silent()


label telllilithaboutnar_goodandbusy:
        l "That's good to hear and wow that's really cool! "
        #TODO: SetFontSize (6)
        l "Even though technically you are now narrating him [name]."
        #TODO: SetFontSize (12)
        l "So do you control where our story leads Nar?"
        l "Yeah, I basically steer the story in the right direction and when we are off track I try my best to get us back on track." #TODO: This is not entirely true, the dev controls the story, the narrator controls the flow.
        menu:
            "(Tell her about how he steers the story back on track.)":
                jump telllilithaboutnar_storysteerer
label telllilithaboutnar_storysteerer:
    #TODO: rewrite this link-text.
    l "Funny that you mention that Nar, I was just thinking about that."
    l "Do you steer us towards my deaths?"
    n "Well, I have to, but I don't always do so, there are plenty of endings where you make it out alive. It's just that [name] usually doesn't end up with you when that happens." #TODO: He doesn"t HAVE to, change this line slightly.
    menu:
        "He said that he has to but that there are also some alternatives, like endings where you are still alive but we don't end up together.":
            jump telllilithaboutnar_endingswhereyoulive
        "He said he has to, that all endings end up with you dying.":
            jump telllilithaboutnar_noendingswhereyoulive

label telllilithaboutnar_noendingswhereyoulive:
    n "So you are just going to lie to her now?"
    #TODO: Add some more text here before you move the player back.
    $ kokiri_conversation_silent()



label telllilithaboutnar_endingswhereyoulive:
    l "Well, could you maybe steer the story to a direction where [name] and I end up together and I get to live?"
    n "But that would destroy the entire point of this game!"
    n "And even worse, it would all be for nothing because then [name] would just stop playing the game without having learnt anything."
    menu:
        "He says that would destroy the entire point of the game and that I would stop playing before ever learning anything.":
            jump telllilithaboutnar_destroythepoint
label telllilithaboutnar_destroythepoint:
    l "I see... and what is the point of this game if you don't mind me asking?"
    n "Well, it is quite simple actually, one of the main points is..."
    n "No, I'm not supposed to tell you and [name] that, it's more impactful when they discover it on their own or with you."
    menu:
        "He says he's not supposed to tell us. That it is more impactful when I discover it on my own or with your help.":
            jump telllilithaboutnar_secret
label telllilithaboutnar_secret:
    l "Oh come on Nar, please?"
    n "No, do not push me Lilith. I can't tell you."
    menu:
        "He said that you shouldn't push him and that he still can't tell you.":
            jump telllilithaboutnar_donotpush
        "Push him a little more, we're so close to getting an answer.":
            jump telllilithaboutnar_push
label telllilithaboutnar_push:
    "Filler"
    #TODO: Make the narrator answer your question? He will never narrate again until you erase his memories by resetting the game. ANSWERing the question probably isn't the best idea.)
    #Make the narrator begin to tell what it is and then the game just closes itself or goes back to the menu.
    $ kokiri_conversation_silent()
label telllilithaboutnar_donotpush:
    n "Alright, I understand."
    n "All I can say is that He, the creator of this world and game, wants the player to find the answer to your question so surely they will stumble upon it eventually."
    menu:
        "He said that the creator of this game wants me to figure out the lesson so that we surely will stumble upon it eventually.":
            jump telllilithaboutnar_stumbleuponlesson
label telllilithaboutnar_stumbleuponlesson:
    l "Thank you Nar, I appreciate it!"
    l "Also, I'm sorry for all the questions but is it possible to meet this creator you are speaking about?"
    n "Fragments of them but never the whole because,  just like the player, He doesn't live in this game." #TODO: Rewrite this line a bit.
    n "Also I'm sorry to do this but your time is up." #TODO: Do something about having to cut the line before the narrator shows too much info instead of here time running out.
    #TODO: Move Lilith to death, in the quest version it moves to "Kak_death_4_hill_2"
    $ kokiri_conversation_silent()













 #TODO: Fill this in.

label askaboutabigail_tellmeabout:
      $ kokiri_chatchar_abigail_recent = True #This will be used to make sure the player gets put back to the right place in the conversation after the family curiosity checker.
      if kokiri_chatchar_abigail == False:
          $ kokiri_chatchar_abigail = True
          $ kokiri_chatchar_abigail_counter = 1
          $ conversationtracker_abigail = True #TODO: Is this the right flag?
      else:
          $ kokiri_chatchar_abigail_counter += 1


      $ family_curiosity_checker()
      #Try this out as as a way for you to learn how to use functions in renpy.
      #If it does not trigger continue to the part below this.
      if kokiri_chatchar_abigail_counter == 1:
          jump askaboutabigail_tellmeabout_1
      elif kokiri_chatchar_abigail_counter == 2:
          jump askaboutabigail_tellmeabout_2
      elif kokiri_chatchar_abigail_counter == 3:
          jump askaboutabigail_tellmeabout_3

label askaboutabigail_tellmeabout_1:
              l "Well, as you probably already know Abigail is my little sis."
              l "We went through a lot like most sisters but we always managed to get through it all."
              l "...This stays between us alright [name]?"
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
                          a "You're calling pretty soon, did your date with [name] not go well?"
                          l "I am still on my date actually." #TODO: (Rewrite this line)
                          a "Oh? Then why are you calling?"
                          l "Well, it's kind of hard to explain..."
                          a "I see, no worries Lilly!"
                          a "Is your phone on speaker currently?"
                          l "Yes it is, why?"
                          a "Heya [name], treat my sis nicely will you?" #TODO: Do this line in a bigger font.
                          #TODO: Revert to normal size afterwards.
                          l "Abby, you're going to scare [name] off like that."
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
                          a "That's really sweet of you Lilly! But I actually mean why are you asking me that now, during your date with [name]?"
                          l "Well, I sort of will die during this date." #TODO: "(Make this one of two reactions possible) " What did past me mean by that?
                          a "... What?..."
                          a "Is this a joke?"
                          a "Was this [name] their idea?"
                          a "This is not funny [name]" #TODO: Increase fonsize again
                          l "Abby, please, stop yelling..."
                          l "It's not a joke."
                          l "It's kind of hard to tell you why we think I will die but [name] has made it clear that there is atleast something strange going on."
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
                          a "And that feeling of loneliness even affects my thoughts. I constantly doubt wheter or not my friends really like me, even if they literally say so." #TODO: (Rewrite this line definetly)
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
                          #TODO: Write her putting the phone down and saying goodbye to Abigail.
                          jump kokiri_death_3_death_dialogue
                      else:
                          n "Lilith won't have enough time to call if she calls now."
                          n "I suggest talking about the same thing again as quickly as possible the next time."
                          n "Let's just talk about something else to her for now."
                          jump kokiri_talkaboutsomethingelse





  #TODO: Rewrite this dialogue a bit more.

label askaboutabigail_tellmeabout_2:
              "Filler"
              #TODO: Fill in (no quest precedent)
              $ kokiri_conversation_silent()

label askaboutabigail_tellmeabout_3:
              "Filler"
              #TODO: Fill in (no quest precedent)
              $ kokiri_conversation_silent()

label askaboutdavid_tellmeabout:
    $ kokiri_chatchar_david_recent = True #This will be used to make sure the player gets put back to the right place in the conversation after the family curiosity checker.
    if kokiri_chatchar_david == False:
        $ kokiri_chatchar_david = True
        $ kokiri_chatchar_david_counter = 1
        $ conversationtracker_david = True #TODO: Is this the right flag?
    else:
        $ kokiri_chatchar_david_counter += 1



    $ family_curiosity_checker()
    #Try this out as as a way for you to learn how to use functions in renpy.
    #If it does not trigger continue to the part below this.
    if kokiri_chatchar_david_counter == 1:
        jump askaboutdavid_tellmeabout_1

    elif kokiri_chatchar_david_counter == 2:
        jump askaboutdavid_tellmeabout_2

    elif kokiri_chatchar_david_counter == 3:
        jump askaboutdavid_tellmeabout_3

label askaboutdavid_tellmeabout_1:
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

label askaboutdavid_tellmeabout_2:
            "Filler"
            #TODO: Fill in (Cryptography with codes on birthday-cards)
            l "My father loves all things related to cryptography."
            l "When he still lived with us he would give me a a postcard for every birthday."
            l "That postcard had an encode message on it."
            l "Then I had to decipher the code to reveal a list of cryptic instructions that would lead me to a gift."
            l "Sort of like a scavenger hunt I suppose."
            l "I liked it a lot to be honest. It felt as if we had a sort of hidden language to communicate in with eachother."
            #TODO: Make the text below linked to a choice where you ask Lilith how she feels telling that story since you usually only hear bad stories about her dad from her.
            menu:
                "I haven't heard you talk about a lot of happy memories with your father, how does sharing that story make you feel?":
                    l "I was a bit hesitant to tell this story because of the pain it might make me feel but I'm actually glad I told it."
                    l "It felt... kind of good? Almost as if everything was back the way it used to be."
                    l "It's been so many years since I last got a postcard from him that the memory of that ever happening is almost getting a bit fuzzy."
                    n "Lilith starts sobbing."
                    l "I'm sorry to unload all of that on you [name], you don't deserve this."
                    menu:
                        "I understand that you feel like that Lillith but I don't mind at all. Besides, you deserve someone who can listen to you.":
                            n "Lilith is still crying quite hard but you can see a slight smile forming."
                            l "I... suppose you're right [name]. That is really sweet of you. Thank you."
                            l "I just... need a moment to compose myself."
                            n "Lilith plants her head on top of her knees and stays like that for a long while."
                            n "You can still hear her sobbing but it seems to grow more quiet over time."
                            l "There, I'm feeling a bit better already!"
                            l "Honestly, crying like that might be exactly what I needed."
                            l "Thank you for comforting me [name]! I really appreciate it."
                            l "Knowing that we don't have unlimited time makes me really thankful that you chose to spend that time to make sure I was okay."
                            $ kokiri_conversation += 1
                            $ love_points = 2 #This gains you 2 love points but as a sacrifice you lose an additional topic to talk about.
                            $ love_meter_updater()
                            $ kokiri_conversation_silent()


label askaboutdavid_tellmeabout_3:
            "Filler"
            #TODO: Fill in.
            $ kokiri_conversation_silent()

label askaboutjames_tellmeabout:
    $ kokiri_chatchar_james_recent = True #This will be used to make sure the player gets put back to the right place in the conversation after the family curiosity checker.
    if kokiri_chatchar_james == False:
        $ kokiri_chatchar_james = True
        $ kokiri_chatchar_james_counter = 1
        $ conversationtracker_james = True #TODO: Is this the right flag?
    else:
        $ kokiri_chatchar_james_counter += 1
    $ family_curiosity_checker()
    if kokiri_chatchar_james_counter == 1:
       jump askaboutjames_tellmeabout_1
    elif kokiri_chatchar_james_counter == 2:
         jump askaboutjames_tellmeabout_2
    elif kokiri_chatchar_james_counter == 3:
          jump askaboutjames_tellmeabout_3

label askaboutjames_tellmeabout_1:
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
            l "Wow [name]... I'm not sure what to say."
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
    #(The stuff that comes next are puzzle pieces that you need to fit together)
    #(What were his hobbies?-> Photography, he and Lilith were into photography)
    #James used to love photography and everything that came with it. So did I actually.
    #Our father used to be a fan of photography and I think he passed that over to us.
    #Well nowadays I don't really take pictures anymore. Everythime I tried to pick up a camera I just get reminded of both James and my fath- and David.
    #I have dropped quite a few camera's when I tried to continue. I think it's for the best if I just stop for now.
    #But James was extremely good for his age, he always was a quick learner but something about photography just seemed to click fantastically with him.
    #It was almost as if you could just jump into his pictures and live inside of them.
    #He used to tell me that a good picture should not just let the person watching it see a moment caught in time but it should also make them envision the future.
    #In other words, a good picture should almost become a video with the picture as it's first frame.
    #Personally I aways thought the oposite, a good picture makes you remember the lead-up to that picture, so in a way a good picture is a video with the picture as it's last frame.
    #I think that's the only reason I can look at a picture of James without tearing up completely. I just see the lead-up to the picture and not the horifying aftermath of it all.
    #However badly the memory of the aftermath still haunts me, I can't let that be the only part of his life I remember. I want to make sure all the beautiful memories we made throughout all the years will live on as long as possible. (Use that as a framing device for her telling you a few stories about him.)
    #So you wanted to hear about James right?
    #I'll tell you some stories if you'd like, since if the stories only stay in my memories they can only exist for one more day. (rewrite this line)
    #TODO: (Maybe rewrite this a bit becomes he comes of as too idealised)
    #1: (Hide and seek in corn fields) (Add some links to this story for different paths of info)
    #TODO: 2. (Code/cipher breaker on birthday cards.) (Don't do this one, scrap it.) NO, USE THIS FOR DAVID
    #1: The house we grew up in had a field that mostly grew corn on the opposite side. We used to have a game where one of us would enter the field and crawl around in it while the other person tried to find them. Usually the hider has to say something every minute so that it's a bit more doable to find them. Well one day he was the hider and I was the searcher. He hadn't said anything for the entire time and so I had no idea where he could possibly be.The tension was high. (Continue this story and expand it a bit more) Suddenly James popped out of the corn and picked me up while he spun around. He then put me down and layed down between the corn. I layed down beside him and we just looked at the sky while talking about all sorts of things. (What kind of things? Needs more fleshing out.)

label askaboutjames_tellmeabout_2:

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
   l "However badly the memory of the aftermath still haunts me, I can't let that be the only part of his life I remember. I want to make sure all the beautiful memories we made throughout all the years will live on as long as possible." #TODO: (Use that as a framing device for her telling you a few stories about him.)
   #TODO: Add some choice(s) here.
   menu:
       "I think that is beautiful, I will make sure that James and the stories you two shared won't go forgotten.":
           n "Lilith gives you a sincere smile."
           n "The stars shine enough light on her face for you to catch a tear rolling over her cheek."
           l "Thank you [name]! That would mean a lot to me."
           l "Even if I don't make it to the end of this day, you will."
           l "Atleast the memories of James won't end up dying with me."
           l "That gives me some comfort."
           l "Don't get me wrong, I'm still terified."
           l "I mean, rightfully so."
           l "But at the very least it makes it slightly easier to cope with whatever will come next."
           $ kokiri_conversation_silent()

label askaboutjames_tellmeabout_3:
     l "The house we grew up in had a field that mostly grew corn on the opposite side."
     l "We used to have a game where one of us would enter the field and crawl around in it while the other person tried to find them."
     l "Usually the hider has to say something every minute so that it's a bit more doable to find them."
     l "Well one day he was the hider and I was the searcher."
     l "He hadn't said anything for the entire time and so I had no idea where he could possibly be."
     l "The tension was high."
     l "Suddenly James popped out of the corn and picked me up while he spun around."
     l "He then put me down and layed down between the corn."
     l "I layed down beside him and we just looked at the sky while talking about all sorts of things."
     #TODO: (What kind of things? Needs more fleshing out.)
     #TODO: (Continue this story and expand it a bit more)
     #TODO: Fill in.
     #TODO: Fill in.
     $ kokiri_conversation_silent()

label askaboutlila_tellmeabout:
    $ kokiri_chatchar_lila_recent = True #This will be used to make sure the player gets put back to the right place in the conversation after the family curiosity checker.
    if kokiri_chatchar_lila == False:
        $ kokiri_chatchar_lila = True
        $ kokiri_chatchar_lila_counter = 1
        $ conversationtracker_lila = True #TODO: Is this the right flag?
    else:
        $ kokiri_chatchar_lila_counter += 1


    $ family_curiosity_checker()
    if kokiri_chatchar_lila_counter == 1:
        jump askaboutlila_tellmeabout_1

    elif kokiri_chatchar_lila_counter == 2:
        jump askaboutlila_tellmeabout_2

    elif kokiri_chatchar_lila_counter == 3:
        jump askaboutlila_tellmeabout_3


label askaboutlila_tellmeabout_1:
           l "I really love my mom."

           l "She definetly didn't have it easy."

           l "She had to deal with James' death and David leaving all of us."
           l "She basically raised both me and Lilith ever since David left."
           l "I can't imagine it having been easy for her but she never really talked about it whenever I asked her."
           l "I think she wanted to make sure we were able to grow up with as little worries as possible."
           #TODO: Write out this conversation a bit more and rewrite it slightly.
           menu:
                "You might want to call her.":
                    $ kokiri_meteoritewarn() #TODO: Remove this after testing
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
                        li "So, what did you want to ask me then sweetie?"
                        l "Well, I have been wondering something for quite a while."
                        l "You took up an inmense burden with taking care of us on your own right? "
                        l "The stress you felt..."
                        l "Why did you never tell us?"
                        li "You two were never a burden on me and never will be alright? Try to remember that very well please."
                        li "And what would I have needed to tell you two? That I was barely scraping by?" #TODO: To have the dad still send checks, make the mom not accept them because she is hurt that he left.
                        #Make the todo be something you can learn and can ask David about.
                        li "That I felt like I was living three lives and neither of them were mine?"
                        li "That I felt abandoned by your father?"
                        l "You should have told us, we could have-"
                        #TODO: Increase fontsize for next line and then revert to normal.
                        li "Could have done what?"
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
                        #Put that in this version of the game.
                        #TODO: Write a little bit extra conversation between these two grene blocks
                        li "I'm very sorry to hear that you've been carying this sort of guilt with you for so long sweetie."
                        li "I wanted to prevent that exact thing from happening, that's why I tried to not show the stress I'd feel."
                        li "But you were always quite good at figuring people out, I guess it was silly of me to think that shielding you from my stress would work."
                        li "If anything I'm happy that we can have this conversation, that I can atleast help ease your burden slightly."
                        li "Which leads me to a question."
                        li "Not that I'm complaining ofcourse! But why do you ask me about something that happened so very long ago now of all times? "
                        l "Well..."
                        l "This might sound weird but I  have very good reasons to believe I won't survive past today." #TODO: make this an alternate option you can choose to let her say, the other one would be that she tried to talk to her mom about this as a child but that she wouldn't listen and she now has to do it as an adult.
                        li "...What?"
                        li "And what are those good reasons?"
                        li "This is very hard to explain..."
                        li "Basically, I already have died before on this day."
                        li "We are in a sort of loop where I keep dying over and over."
                        li "Oh no, that's horrible"
                        li "Is there anything I can do to help?"
                        l"You've already done enough, you helped me ease my mind a bit."
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
                        li "If you see James... can you tell him I still think about him all the time?" #TODO: Make this a flag you can learn and then later tell James' ghost about.
                        l "I'm sure he knows mom... but I will tell him."
                        n "You motion to Lilith that she doesn't have much time left."
                        l "I'm going to hang up now mom, what comes next won't sound pretty..."
                        l "I love you."
                        #TODO: Narate her hanging up.
                        jump kokiri_death_3_death_dialogue
                    else:
                        n "Lilith won't have enough time to call if she calls now."
                        n "I suggest talking about the same thing again as quickly as possible the next time."
                        n "Let's just talk about something else to her for now."
                        jump kokiri_talkaboutsomethingelse


                "Go back":
                    #TODO: Remove this
                    jump kokiri_talkaboutsomethingelse



        #TODO: Rewrite this dialogue a bit more.

label askaboutlila_tellmeabout_2:
     #Make this a story about how she is pretty naive. Let Lilith tell a story about a scamcaller that almost tricked her mom before James helped them.
     #TODO: Rewrite this story eventually once it is finished. Especially don't make it start with "you know"
     l "You know, my mom is actually quite naive."
     l "Abby and I like to make fun of her for being too trusting."
     l "It's a beautiful quality of her to be entirely fair but sometimes she just takes it way too far."
     l "I remember this one time where she got a mail from someone claiming to be a rich relative from Canada."
     l "They said that they were going to soon die and that mom was the nearest heir of his fortune."
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
     menu:
         "Go back":
             #TODO: Remove this
             jump kokiri_talkaboutsomethingelse

label askaboutlila_tellmeabout_3:
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
