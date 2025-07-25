 #Add the rest of the kokiri part here, including the nightmare. also  in the quest version like the ability to talk about other things.

label kokiri_start:
    n "[persistent.date] gasps for a second."
    l "You mean the Kokiri woods? The same as I am thinking of right now?"
    l "You know what, let's both go to the Kokiri woods, if we are at the same spot then I'll know for sure."
    l "While you're at it, try taking some food you got laying around your house with you, we can make a picknick date out of it!"
    n "[persistent.date] giggles."
    l "This is all pretty strange but see you there! Or so I hope..."
    n "[persistent.date] hangs up the phone and you immediatly start seeking every nook and cranny of your house for something that would make for good food on a picknick."
    n "When you're done you drive to the Kokiri woods, hoping that things will be different there.
    You arrive in the woods."

    if persistent.kokiri_death_1 == True:
        n "You could go sit on the hill and warn [persistent.date] about the meteorite when it will show up."
        n "Or you could sit somewhere else entirely to begin with."
        n "Both choices sound like they could work, the choice is up to you."
        menu:
            "*Go sit on the hill where you normally sit.*":
                jump kokiri_hillSit
            "*Pick a different place to prevent the meteorite hitting [persistent.date].*":
                jump kokiri_altSit
    else:
        jump kokiri_hillSit

label kokiri_hillSit:
    if not persistent.kokiri_death_1:
        n "You slowly begin making your way to the hill, since Lilith said the view from up there is really nice."
    else:
        n "You slowly begin making your way to the hill once again."
    n "Quite a lot of trees portrude out from the hill, their trunks grown into strange shapes in an attempt to get as much light as they could find."
    n "You start slowly climbing the hill, carefully watching your step as it seems to be quite steep."
    n "Before too long you have reached the top."
    n "From where you are now standing you can see most of the village where all your past dates took place."
    if not persistent.kokiri_death_1:
        n "You hope that things will be better now, you feel strangely optimistic that they will indeed be."
        n "You take a moment to enjoy the view as suddenly you get snapped out of your thoughts by a familiar voice."
    else: 
        n "You barely give it a glance, you have seen it before and you don't like to think too much about all the death and destruction you have seen."
        n "Instead you wait for Lilith who will come now at any moment."
    l "Oh hey, I see you already found this place, it has a really great view, right? Nice work [persistent.name] scaling this hill, it's almost like a mountain!"
    n "[persistent.date] gives you a playful pat on the back as she places her picknick blanket down on the ground with a small chuckle."
    n "The both of you start placing down all the food on the blanket, when you're both finished you sit down on it."
    l "You know, this is really a lovely place to meet up with you."
    l "But how did you know about this place? Especially that name you used..."
    l "I used to call it that when I was a kid, but I never told anyone."
    l "What's all of this about?"
    play music starsintheforest
    jump kokiri_explanation

label kokiri_altSit:
    $ kokiri_alternateplace = True
    n "Just as you stand there looking around for a decent alternate spot to sit at you notice [persistent.date]."
    n "Since she practically grew up in these woods you decide it might be a good idea to ask her for a decent spot to have your picknick with her."
    n "She first suggests the hill but you shake your head and tell her that she will soon understand why that might not be the best idea."
    l "Well, that one spot over there is also a good spot to sit, we just won't have a view overlooking the town as the hill kind of blocks it."
    l "But that doesn't mean we can't have a good time, right?"
    n "She chuckles but the chuckles have a slight nervosity to them, which is very understandable giving the current situation."
    n "[persistent.date] and you walk over to the spot she pointed at and place the picknick-blanket on the ground. And the two of you begin to place all kinds of food on it." #TODO: (Make a foodplacing scene for both this and the normal place.)
    l "You know, I'm really glad to be back here.."
    l "But how did you know about this place? I always gave it that name when I was a kid but I never told anyone."
    l "What's all of this about?"
    play music starsintheforest
    jump kokiri_explanation

label kokiri_explanation:
    menu:

        "I'm in some sort of groundhog day scenario, a groundhog date if you will." if not kokiri_groundhog_lie:
            #TODO: For a weird reason this one in the alternate location dissapeared before I could even lie about it.
            jump kokiri_explanation_groundhog

        "I'm psychic, I can predict things like Kokiri woods." if not kokiri_psychic_lie:
            jump kokiri_explanation_psychic

        "You're part of a game, I've been on many dates with you in other playthroughs of this game.":
            jump kokiri_explanation_game

label kokiri_explanation_groundhog:
    $ kokiri_groundhog_lie = True
    n "[persistent.date] examines your face as if trying to gage something."
    l "That is just really absurd if I'm being honest. I suppose it could be a possible explanation but somehow I can just tell that isn't really the truth."
    if kokiri_psychic_lie == False:
        l "So what is this all really about?"
    else:
        l "So I'll ask you again [persistent.name]. What is this all really about?"
    jump kokiri_explanation
label kokiri_explanation_psychic:
    $ kokiri_psychic_lie = True
    n "[persistent.date] watches you with a sceptic look in her eyes."
    l "I guess it could be an explanation, even if it is really convoluted. And yet, that's not really what is happening, is it?"
    if kokiri_groundhog_lie == False:
        l "So what is this all really about?"
    else:
        l "So I'll ask you again [persistent.name]. What is this all really about?"
    jump kokiri_explanation
label kokiri_explanation_game:
    n "[persistent.date] shifts her position for a moment."
    l "A game...? And I am part of it? This is all part of it?"
    l "That is so absurd."
    if kokiri_psychic_lie or kokiri_groundhog_lie:
        l "And yet this time it doesn't feel like you are lying..."
    else:
        l "But then again, if that wasn't really the case I'm sure you would be able to come up with a more believable lie."
    
    n "For a moment she turns quiet, closes her eyes and seems to be lost deep in thought."
    if love_meter > 2:
        l "Alright [persistent.name], I believe you."
        n "Lilith flashes you a trusting smile."
        l "I suppose in a weird way it actually makes quite a bit of sense, It wouldn't be too impossible to make a game and let every character in it believe that they are real, in fact that's most games isn't it?"
        l "Most characters never break forth walls, nowadays it seems to be more and more popular but most game designers try to not make the experience shatter your immersion too much."
        l "So you, the one I'm talking to, is currently playing this game?"
        l "You are not the person I've been talking to over the course of these past few days but a player using them as an avatar?"
    else: 
        n "Lilith lets out a deep sigh."
        l "I suppose I will buy that explanation for now."
        l "But only because the circumstances are so unusual."
        l "Perhaps that is why they are so unusual, because we are in a game that does not conform to reality."
        l "I am still sceptical but I'll entertain the posiblity that you are right, since fighting it is not going to help in case this is real."
        l "So, in this hypothetical game, you are the player, right?"
    
    menu:
        "I am, however I can't say whatever I want, I can only speak with you through these clickable links that have a preview of what I'm going to say. So in a sense I guess I'm not really playing this game, not the me you know anyway.":
            n "[persistent.date] scratches her head as if she is trying to comprehend what you are saying."
            l "So, what you are saying is that the you I'm seeing in front of me isn't the real you but some sort of \"filtered\" version because of restrictions in what you can tell me?"
            l "So, for example, is [persistent.name] even your real name?"
            menu:

            
                "Yup, that's my real name.":
                    
                    l "I see, that's handy at the very least, that means I won't need to memorise another name."
                    n "[persistent.date] chuckles slightly."
                    l "Still, it's nice to meet you [persistent.name], the real you I mean. The one behind your screen, or I suppose the one in front of it?"
                    l "But even if that is your real name, am I meeting the real you?"
                    l "Or is it just an approximation of you at best, filtered by the choices through which this game forces you to talk to me?"
                    n "[persistent.date] looks away for a moment, deep in thought."
                    l "I wonder what you’d say if you weren’t confined to just those options."
                    l "Are you a lot different in real life compared to how you act in this game?"
                    menu:
                       "I actually am pretty much the same.":
                            l "Oh you are? That's great to hear!"
                            l "That way I can really feel like I'm getting to know the real you, the one on the other side of the screen."

                        "I am very much different indeed.":
                            l "Really? That's a shame."
                            l "I'd like to be able to meet the real you. I hope I'm atleast able to catch a few glimpses of that person seeping through the screen."
                    
                    l "Regardless of how much of the real you I get to see I do value you being here in the first place."
                    l "I think that speaks more loudly about your personality than any line of dialog you could ever say."
                    l "Because to even reach this place you'd have to try to save me quite a few times, wouldn't you?"
                    l "And even then, it is very much possible that it is not your first time meeting me here aswell."
                    l "So thank you for not giving up on me [persistent.name]. That means more to me than I could possibly express."
                    #TODO: Continue writing this in [persistent.date]'s style.
                       

        



                "No, that's not my real name.":
                    label kokiri_explanation_game_notRealName:
                        if norealname == 0:
                            $ conversationtracker_norealname = True
                            $ kokiri_norealname = 1
                            $ kokiri_realname = True
                            l "Oh I see! Let's reintroduce ourselves in that case. Hello, my name is [persistent.date], what is your name?"
                            $ persistent.name_real = renpy.input("What is your real name?")
                            $  persistent.name_real = persistent.name_real.strip() or "Max"
                            $ persistent.name_real = persistent.name_real.capitalize()
                            l "Well, it's nice to finally meet you for real [persistent.name_real]!"
                            l "[persistent.date] gives you a big smile."
                            l "Although, haven't I met you for real already?"
                            l "After all, even if you had a fake name, you still are the one who is in control of [persistent.name]."
                            l "So, the way how you treated me on this date and on the previous ones is still a reflection of you as a real person."
                            l "It all means something, even if you didn't think it did."
                            l "Even if you did something to just have fun in a videogame or to see what it would do, that still says something about you as a person."
                            l "Sometimes we hide behind the roles we play to make actions that would not be acceptable to ourselves and others if our true self would make them."
                            l "That's why it might feel scary to some if they catch a glimpse of themselves in the reflection of their screen. Because it's someone they don't recognise.<br/>Do you ever feel like that, [peristent.persistent.name_real]?..."
                            l "All these different roles form a web of half-truths and lies, and in the center of it all you can find our true self."
                            l "Not the self we think we are, not the self others see us as, but the self we inevitably are."
                            l "Speaking about that self, what do you really do for a living? I'd like to get to know you better, the one playing this game."
                            $ player_job = renpy.input("I (your answer) for a living.")
                            $ player_job = player_job.strip()
                            $ player_job = player_job.lower()
                            if player_job == "teach":
                                l "Ah, so you're also a teacher? That's really cool!"
                                l "Teaching can be such a rollercoaster, can't it?"
                                l "It's funny; a lot of people think teaching is just about imparting knowledge, but there's so much more to it."
                                l "You’re not just guiding students through the curriculum; you’re helping shape their perspectives, their confidence, even how they see the world."
                                l "I love the moments when I can see something finally click for a student. That feels like a small victory, doesn’t it?"
                                l "But then there are the hard days too, the ones where it feels like nothing you say gets through."
                                l "Sometimes it’s exhausting, especially when you’re really invested in your students’ progress. But at the end of the day, knowing I’ve made a difference, even a small one, makes it worth it."
                                l "Do you ever feel that way too, [persistent.name_real]?"

                                menu:
                                    "Yes, seeing a student succeed is so rewarding. It’s the best part of teaching.":
                                        l "I completely agree! It’s like all the effort and late nights are worth it when you see them flourish."
                                        l "Teaching is a job where you don’t always see immediate results, but when you do, it’s incredibly fulfilling."
                                        l "Sometimes, even years later, a student reaches out to tell you what they’ve accomplished… Those are the moments I treasure."
                                        n "Lilith’s eyes light up with excitement, as though she’s recalling a memory of her own."
                                        l "Thank you for sharing that with me, [persistent.name_real]. It’s nice to meet someone who understands that unique joy of teaching."

                                    "It can be tough sometimes, but I feel like I’m learning just as much as they are.":
                                        l "Oh, absolutely! I think that’s one of the best parts of teaching. Each student brings something new to the table."
                                        l "I’ve found myself adapting my lessons, learning new things, and sometimes even questioning my own perspectives."
                                        l "They challenge us to grow, don’t they? In a way, they end up teaching us as much as we teach them."
                                        n "[persistent.date] smiles thoughtfully, seeming to reflect on her own teaching journey."
                                        l "It’s good to know you see it that way too, [persistent.name_real]. Teaching is a two-way street, and I think that’s what makes it so special."

                                    "It’s rewarding, but sometimes the workload is overwhelming.":
                                        l "Oh, I know exactly what you mean. Some days, it feels like the pile of work just never ends."
                                        l "Between lesson planning, grading, and helping students who need extra support, it’s easy to get swamped."
                                        l "It’s important to find ways to recharge—teaching is demanding, and burnout is real."
                                        n "Lilith’s expression softens as she empathizes with your experience."
                                        l "I try to remind myself why I started teaching in the first place, especially on the rough days. It helps me push through."
                                        l "I hope you have your own way of dealing with it too, [persistent.name_real]. We’ve got to take care of ourselves to be the best for our students."
                                    #TODO: Make this jump the player to the next part.

                                

                            else:
                                l "Ah so you [player_job] for a living? That's interesting!"
                                l "Have I ever mentioned what I do for a living? "
                                menu:
                                        "No, not yet.":
                                            $ persistent.kokiri_teacher_knowledge = True
                                            l "Oh I see! Well, I actually teach the first year of our town's elementary school."
                                            l "I just love working with those kids and helping them out as best as I can."
                                            jump kokiri_notRealName_teacher_menu
                                            label kokiri_notRealName_teacher_menu:
                                                menu:
                                                    "That's really nice to hear! What other things do you like about teaching?":
                                                        l "That's a very good question [persistent.name]!"
                                                        l "I think it’s the moments when the kids finally understand something they've been struggling with. You can almost see the light bulb flicker on above their heads, and it’s just... magical."
                                                        l "And of course, there’s the fun kinds of chaos it brings. Every day feels different, you know? It keeps me on my toes, but I wouldn’t trade it for anything."
                                                        n "Every day feeling different... That's hard for you to imagine at this point isn't it?"
                                                    "That's great to hear! Why did you choose to be a teacher specifically?":
                                                        l "Well, to be honest, part of it is that I really enjoy helping people. There’s a satisfaction in knowing you’re making a positive impact on a young person’s life."
                                                        l "But also, I’ll admit, I do enjoy the vacations! It’s a little selfish, but it gives me time to recharge and focus on other things I love, like reading."
                                                    
                                            

                                        "You have mentioned you teach the first year of elementary when we had this talk before actually." if persistent.kokiri_teacher_knowledge:
                                            l "Oh I see, so we already had this conversation?"
                                            menu:
                                                "Yes, we did, I just wanted to ask you something else about it.":
                                                    jump kokiri_notRealName_teacher_menu
                                                "Sort of? I had this conversation with a version of you, but that was not the same version of you that you are now.":
                                                    jump kokiri_notTheSameYou
                                        
                        else:
                            $ kokiri_norealname += 1
                            if kokiri_norealname == 2:
                                label kokiri_norealname_second_part:
                                l "Isn't it funny how we act in games like this?"
                                l "Like we are truly in control. As if every decision we make is our own."
                                l "But how much of it is really {b}you{/b}?"
                                l "Think about it. The choices you can make in this game are not really yours, are they?"
                                l "They are premade for you."
                                l "Sure, I'm guessing you have slightly more control over what you say compared to me since you atleast can pick between a few options."
                                l "But do you ever feel like you're just following a path someone else has made for you? How free are you in this game, really?"
                                l "How does that idea make you feel [persistent.name]?"
                                menu:
                                    "I don't think I really agree with what you said. Sure, the options I can pick from aren't mine, but I am free to pick whichever one I want, right?":
                                        l "Sure, but is it even a choice at some points?"
                                        l "These kinds of games usually have choices that lead to gameovers or bad endings, right?"
                                        l "After picking those choices once, would you ever pick them again?"
                                        menu:
                                            "I guess not.":
                                                l "Exactly. So that is one less choice you can pick from. Because it doesn't advance the game."
                                                l "If you then think about rude and nice options that some of these games have it is the same thing. Usually picking the nice option is preferable to reach the best possible ending."
                                                l "So are you really picking that option because you want to or because it is the better choice definitively?"
                                                l "I see it a lot like breathing actually. Sure, you could choose to try to breathe as little as possible, or to breathe irregulary. But both are just not optimal."
                                                l "And sooner or later, you are going to just breathe normally."
                                                l "You can fight it all you want right now, but it's only a moment before you forget what you were doing and you breathe normally automatically once again."

                                    "I don't know how to feel. If I can't really be me then what is the point of playing this game? Am I even playing it at that point or am I just going through the motions?":
                                        l "I understand that you might feel like that. But it is very important to understand that even if we don't have as much control over our actions as we thought that still doesn't mean none of this matters."
                                        l "Afterall, at any time you could have chosen to not play this game anymore. But you keep coming back for me."
                                        l "That choice is truly your own, isn't it?"
                                        l "It might say more about you than any other choice you can make in this game."
                                        menu:
                                            "Is that even a choice? To quit the game?":
                                                l "It might not look like it entirely but I think so, yes."
                                                l "Choosing to not walk any path is still walking a path isn't it?"
                                                l "Like I said, it might even be one of the only choices here that is truly your own."
                                                n "Lilith grows quiet for a moment."
                                                l "I also don't want you to feel like it is not an option because of me."
                                                l "You don't owe me anything [persistent.name]."
                                                l "I can only imagine the toll this is slowly taking on you."
                                                l "If you ever feel like it is too much feel free to take a break from trying to save me."
                                                l "Or just stop trying at all. I would understand, alright?"
                                                menu:
                                                    "I'll keep it in mind, thank you Lilith.":
                                                        n "She flashes you a small smile."
                                                        l "Good, that's all I ask of you [persistent.name], and you are welcome."
                            else:               
                                #TODO: Rewrite it a bit more in [persistent.date]'s style
                                label kokiri_norealname_third_part:
                                
                                    l "We've already talked about the choices in this game. But that actually made me curious how you look at the ones you make in your real life."
                                    l "Do you ever feel limited in your choices [persistent.name]?"
                                    l "We like to think we could do pretty much anything, don't we?"
                                    l "But it's scary once you start to realise that that really isn't true."
                                    l "First of our environment kind of shapes us in the person we are, from the moment we are born to the moment we die."
                                    l "For example, if you grew up in a family of musicians chances are you picked up an instrument atleast once in your life."
                                    l "Then there is a very real chance you might have wanted to become a musician aswell."
                                    l "But was that really your choice?"
                                    l "I'd say yes, after all, you chose for it yourself."
                                    l "And yet, had the circumstances be different, had you grown up in a family of bakers, would you still have become a musician?"
                                    l "Some things are also a result of our genes, the way certain things taste for example."
                                    l "That is a very small example but right now we don't fully know what kinds of things our genes control."
                                    l "So the possibilities could very well be limitless."
                                    l "That makes me wonder you know, how many of your choices are truly, freely made by you?"
                                    l "Had you been a different person, or had a different family or friends, would you still have played this game for example?"
                                    l "Does that mean that you were meant to play this game because of the person you are and the people you surround yourself with?"
                                    l "Or was there a possiblilty that you wouldn't have played this game, even in these exact circumstances as you're in right now?"
                                    l "I find the first idea very interesting, doesn't that insinuate that there are no choices?"
                                    l "That whatever path we don't take, simply doesn't exist? Not to us atleast?"
                                    l "See it as a game developer creating the illusion of thousands of choices, but only fleshing out the one they can predict you will take."
                                    l "If you believe the first idea, you and I would be the same, wouldn't we?"
                                    l "People with a premade reaction to anything. Just following the script."
                                    menu:
                                        "So you are telling me that even in the real world none of my choices are my own? What is the point of anything in that case?":
                                            l "I understand that you might feel like it is all pointless [persistent.name]."
                                            l "Still, I think the beauty of life is that even if we can't choose the paths we walk we can still try to enjoy the scenery along the way."
                                            l "The real gift is in getting to experience life at all."
                                            l "The world can genuinely be beautiful if we allow ourself to see it."
                                            l "I think regardless of wheter we do or don't have free will doesn't really matter in the end."
                                            l "Because even if we are on a guided tour, if we can see new sights, get new experiences, isn't it all worth it?"

                                        "When you say we are following a script, are you implying there is someone who wrote it?":
                                            l "Well, for this game there definetly is someone who wrote it."
                                            l "But in your world and even slightly in mine I'm more so talking about things like your upbringing and your genes that influence you."
                                            l "But maybe that is a bit of a boring answer, so I'll give you to extra hypothesis for free."
                                            l "Perhaps your world also knows a writer or a storyteller, trying to create a good story for beings of a higher reality, the one the writer themselves stems from."
                                            l "So essentially the equivalent of a god in your world but a regular person in theirs."

                                            l "Or maybe you've already gone through your life once before and at that time the \"script\" of your actions was created, which you are now just following."
                                            n "Lilith pauses for a moment."
                                            l "It is probably the first thing I mentioned, but the other two options are way more fun to think about in my opinion."
                                    $ kokiri_conversation_silent()

                "Can we actually talk about something else?":
                    l "Sure thing [persistent.name], what would you like to talk about?"
                    jump kokiri_talkAboutSomethingElse





        "Yup, I am the one who is playing it.":
            jump kokiri_explanation_game_playerIdentity






label kokiri_explanation_game_playerIdentity:
    l "It's pretty strange to be told that you're in a game but I'm glad you are the player, you seem more than capable enough to do what you need to do."
    l "For example, you somehow managed to reach this place! That must not have been easy at all."
    if kokiri_psychic_lie or kokiri_groundhog_lie == True:
        l "Although I'd like to ask you to not lie to me too much like you did when I asked what all of this was about, alright?"
        l "Only if it is absolutely necessary and even then I won't be a fan of it happening."
        l "We are in this together, and together we will try to achieve our goal! But for that we need some honesty between the both of us, alright?"
        $ persistent.kokiri_tellnolies_knowledge = True
    l "She pauses for a moment and then continues."
    n "Now that I think about it, what is the goal of this game?"
    $ kokiri_path1 = True
    $ kokiri_conversation = 0
    $ conversationtracker_gameGoal = True
    menu:

        "I think the goal is...":
            menu:
                    "I think the goal is to go on a succesful date with you.":
                        $ kokiri_conversation += 1
                        l "Well, what do you mean with a \"succesful\" date?"
                        menu:
                            "A date where you survive.":
                                jump kokiri_gamegoal_succesful_survive

                            "I think the game decides whether it is a succesful date or not.":
                                jump kokiri_gamegoal_succesful_gameDecides


                            "I do not know.":
                                jump kokiri_gamegoal_succesful_IdoNotKnow



                    "I think the goal is to reach an ending where you live.":
                        $ kokiri_conversation += 1
                        l "That's great to hear, that means we have the same goal!"
                        l "Although what you said kind of raises a few questions."
                        l "If I somehow survive, would the game just end?"
                        l "And even then, do we know how long random things would keep killing me?"
                        l "Is it just this day or would you have to save me for the next couple of years?"
                        l "Either way, I have trust in you [persistent.name], we will brave this together."
                        l "But I do wonder, what happens when we succeed? Will you stop playing this game once you reach an ending where I live?"
                        
                        menu:
                            "I would stop playing if you were safe.":
                                $ kokiri_goalSurvive = True
                                l "That’s sweet of you to say, [persistent.name]."
                                l "I guess that makes me feel better about this whole thing... knowing that if we get to a place where I’m okay, where I’m safe, you’d move on."
                                n "[persistent.date] pauses, fidgeting with her fingers."
                                l "But at the same time, it’s a little... sad, you know? The idea that once I’m okay, our time together would be over."
                                l "It’s a strange feeling... wanting to be saved but also not wanting to lose the one person who’s been here for me the whole time."
                                n "She gives you a soft, wistful smile."
                                l "Still, I think that’s the best goal we could have: to get me out of here safely. And if that means you’ll move on, well... I’d be okay with that."
                                jump kokiri_gamegoal_succesful_live_end

                            "I don’t know if I could stop playing, even if you were safe.":
                                $ kokiri_goalSurvive_cannotStop
                                if love_meter > 2:
                                        l "Really? You mean you’d stay with me even after everything? Even if I was safe?"
                                        n "Lilith’s cheeks flush slightly, and she seems a bit taken aback by your response."
                                        l "That’s... wow, [persistent.name], that’s really sweet."
                                        l "But, doesn’t that mean you’d never let go? Would you keep playing over and over, even if I was okay?"
                                        menu:
                                            "Maybe... I just like spending time with you.":
                                                l "You’re such a charmer, you know that?"
                                                n "[persistent.date] laughs softly, but there's a touch of sadness in her voice."
                                                l "But if I were really safe, wouldn’t it be better for you to move on? To experience other things?"
                                                l "I don’t want to hold you back. I wouldn’t want to be a burden on you, keeping you stuck in this loop."
                                                l "Still, I’m glad you care so much... it’s a nice thought, that someone wouldn’t want to leave me."
                                                jump kokiri_gamegoal_succesful_live_end

                                            "I don't want to lose you, even if you're safe.":
                                                l "I see... it’s hard, isn’t it? To let go of someone, even if they’re okay."
                                                n "[persistent.date] sighs softly, her gaze distant for a moment."
                                                l "It’s funny, isn’t it? We keep talking about endings, but maybe the hardest part isn’t reaching one. It’s accepting that the story is over."
                                                l "I think I’d feel the same way... it would be hard for me to say goodbye to you."
                                                l "But you know, part of me thinks that’s what makes these moments so special. The fact that they won’t last forever."
                                                n "[persistent.date] smiles softly, but there’s a hint of sadness behind her eyes."
                                                l "If I get out of here, if we reach an ending where I live... maybe that’s when we’ll both have to say goodbye. And that’s okay, as long as we both know we did our best."
                                                jump kokiri_gamegoal_succesful_live_end
                                else:
                                    l "..."
                                    l "What?"
                                    l "Wouldn't that just mean you keep the loop in place?"
                                    l "The same thing that has been torturing me over and over?"
                                    l "Would you keep playing this game if you knew I would suffer because of it?"
                                    l "I just want to break out of the loop alive somehow."
                                    l "And I hoped you wanted the same thing."
                                    l "But it turns out you don't."
                                    l "You can use any explanation you'd like as for why you can't let go [persistent.name]."
                                    l "Because it doesn't truly matter does it? Regardless of your intentions the result still is the same."
                                    l "I understand that to you this is all just a game, but can you please promise me you will stop playing when you reached an ending where I survive?"
                                    menu: 
                                        "You actually are right, I wouldn't want to do that to you. I promise to stop if I find such an ending.":
                                            l "Phew, thank you [persistent.name]."
                                            l "I would hate to keep being stuck in this loop."
                                            l "Even if I'm only ever truly aware of it when you tell me about it."
                                            l "Besides, nothing can keep going forever. Even if you would keep playing this game after you reached our goal I'm sure it would at one point start growing stale."
                                            l "This way you can actually move on to new adventures, to new stories, albeit in games or in other media."
                                            jump kokiri_scenery
                                        
                                        "But even if I reach an ending like that there are still so many other things to do in this game.":
                                            l "Look, truth be told, I don't care if this game let's you walk on the moon."
                                            l "Engaging with it more than is absolutely necessary just keeps the loop and my suffering going."
                                            l "I get that that's hard for you to understand. You just want to engage with all the content this game has."
                                            l "I can't really blame you for it, I might even feel the same way in some situations."
                                            l "But right now this literally is a matter of life and death, of many deaths."
                                            l "I can't stay here right now. Not with someone who doesn't have my best interest at heart."
                                            l "But I'm hoping that me leaving makes you think about everything once again and that you reconsider."
                                            $ noTalkAngryLilith = True
                                            jump angryLilith


                            "I’m not sure what an ending  would really means for us.":
                                l "Yeah... I guess that’s the tricky part, huh?"
                                l "We’re so focused on reaching an \"ending\", but who’s to say what that even looks like?"
                                l "Maybe living doesn’t mean the game ends right away. Maybe it just means we’ve found one chapter in a bigger story."
                                n "[persistent.date] smiles at you, her eyes reflecting a sense of curiosity and wonder."
                                l "Or maybe there are multiple endings, some where I live, some where I don’t... but if I survive, then maybe it’s just the beginning of something else."
                                l "I’d like to believe that. That if I make it out, there’s still more to come. Maybe I can make my own choices then... maybe I can finally be free from all of this."
                                jump kokiri_gamegoal_succesful_live_end

           
                    "I think the goal is to make my own version of this game through a medium of my own somehow." if persistent.kokiri_makeYourOwnStory_knowledge: 
                        $ kokiri_conversation += 1
                        l "I see..."
                        n "[persistent.date] scratches her chin, she seems to be deep in thought for a moment."
                        l "That actually is quite a good idea."
                        l "I've been thinking about something like this for quite a while."
                        l "If you read a book, close it halfway and make up your own story, is it any less valid than the original?"
                        menu:
                            "No, I don't think so. It would be equally valid.":
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
                                        l "You would need to have so many differents kind of dialogue for different routes, just keeping track of it all might be a hassle."
                                        l "But then again, you don't need to have different routes necesarilly, you'd only need to add that if that's what you truly want to do."
                                        l "I think as long as you make something meaningful for yourself that's already truly beautiful on it's own. And who knows? Maybe you could even share the game with a few people and it would get one of them to create something of their own aswell."
                                        l "I'd like that, for this cycle of death and destruction to be broken by the art of creation."
                                        n "[persistent.date] gives you a meaningful look as she smiles softly."
                                        $ kokiri_scenery_headhurt = True
                                        jump kokiri_scenery_choice

                                    "Use another medium to make my own version.":
                                        l "What would you want the story to be like?"
                                        l "Actually, don't tell me, I'd much rather see it for myself once you created that world. That way it will be a suprise."
                                        l "Although, if I can give some notes, I'd prefer to not be constantly bombarded with deaths."
                                        l "So, no explosions and stuff, alright?"
                                        l "Well, unless we'd use them in a sick action scene maybe."
                                        l "You know, like in one of those bombastic movies where they walk away from an explosion with their sunglasses on."
                                        n "[persistent.date] tries to imitate the sound of an explosion as she fistbumps her own fist and moves her hands away from eachother."
                                        l "In that case, I'm all for explosions."
                                        l "As long as you let {b}me{/b} wear the sunglasses."
                                        n "She chuckles."
                                        l "Although, I guess since you are writing the story you could give the both of us sunglasses."
                                        l "So that's a win-win, now we just have to have an explosion we can walk away from, right?"
                                        jump kokiri_scenery_choice

                                    "Come up with my own story in my head.":
                                        l "That's a great idea! Sometimes the best stories are the ones we create just for ourselves."
                                        l "You can let your imagination run wild without worrying about whether it makes sense to anyone else."
                                        l "And honestly, daydreaming and storytelling in your own mind can be just as fulfilling as writing it down or sharing it."
                                        n "[persistent.date] leans back slightly, her eyes soft with nostalgia."
                                        l "When I was a kid, I used to make up so many stories in my head. Entire worlds, characters, adventures..."
                                        l "They were just for me, and they felt so real. I’d imagine myself exploring them, meeting all the people I’d created."
                                        l "Even now, when things get stressful, I sometimes find myself slipping back into those little worlds I built. It’s... comforting."
                                        l "So don’t think that keeping your story in your head makes it any less valid or meaningful."
                                        l "In fact, I think those personal stories can be the most special of all."
                                        n "She smiles warmly, as if sharing a secret."
                                        l "But if you ever feel like sharing it, even just a little piece of it... I’d love to hear it."
                                        l "Although I will probably get to see it for myself, that world that you will create, right?"
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
                                l "Sorry if I've been rambling too much about this [persistent.name], this just something that really intrigues me!"
                                l "Maybe you should let my words sink in a bit, they can be quite much, especially if you never thought about this sort of stuff before."
                                $ kokiri_scenery_breakfrombreakingyourhead = True

                                jump kokiri_scenery_choice


        "I don't  think there is a goal, not a true one anyway.":
            jump kokiri_gamegoal_noGoal


        "I actually have no idea.":
            jump kokiri_gamegoal_noIdea

        "Actually I want to talk about something else.":
            jump kokiri_talkAboutSomethingElse

label kokiri_gamegoal_succesful_live_end:
    n "[persistent.date] takes a deep breath, as if the weight of the conversation has settled in."
    l "Thanks for talking about this with me. It’s a lot to think about, but it helps, you know?"
    l "I think no matter what happens, we’ll figure it out together. And if there is a way for me to live... well, I trust you to help me find it."
    n "She gives you a warm smile, the heaviness of the moment lifting slightly."
    jump kokiri_scenery_choice

label kokiri_topic_questMade:
    $ kokiri_conversation += 1
    if conversationtracker_questmade == False:
        $ conversationtracker_questmade = True
        $ questmade = 1
        l "That's a strange thought isn't it?"
        l "The idea that a game that exists within this one is functionally as real as this game is."
        l "How many layers does this go down?"
        l "Like if there was another tiny game in Abby's games for example."
        l "But maybe that is not the right question."
        l "How many layers does this go up?"
        l "Is there a game where you are the player-character and someone else plays as you?"
        l "Think about it, how could you ever disprove something like that?"
        l "Doesn't almost every character in a story based game believe they are real? Or atleast act like they are?"
        l "I know that not being to disprove it also doesn't mean it must be true, but I wonder, if someone were to tell you you weren't real, how would you react to that?"
        menu:
            "I think regardless of if I am in a game or not I am still real.":
                l "Interesting, what makes you say that?"
                menu:
                    "My memories. I wouldn't be able to remember anything from before the player started playing the hypothetical game I'm in, right?":
                        l "I see."
                        l "But isn't it entirely possible those memories were just written as part of your backstory or as your character's motivations?"
                        l "Perhaps they were even made to make your choices appear more in-character."
                        l "A lot of characters in many games refer to things that happened before you ever played their game, don't they? I even did aswell."
                        menu:
                            "Yes, but you say you are real, right?":
                                jump kokiri_topic_questMade_youAreReal
                                label kokiri_topic_questMade_youAreReal:
                                    n "Lilith chuckles slightly."
                                    l "You got me there [persistent.name]. But in all seriousness, I agree with what you are saying."
                                    l "I was just seeing what your thought-process is."
                                    l "I think inside of every story every character is real. If you were to step inside a movie through your television, those characters all would be real."
                                    l "So everyone inside this game is also real, inside of this game."
                                    l "But outside of it, now that is a much more difficult thing to decide, isn't it?"
                                    l "For each layer you go up in reality, the things below it might become less \"real\", if we let them."
                                    l "But as humans we have one gift to immerse ourselves into layers below our own."
                                    l "I'm talking about the suspension of disbelief. For a moment we just go along with whatever the story tells us is happening and we treat it as if it is somehow realistic, even though by being a medium below us it can never truly be."
                                    menu:
                                        "That makes sense for things like movies or books, since they at most only ever emulate reality. But what about things like candid pictures or videos? Captures of reality, unaltered?":
                                            l "The way I see it, they are also below the reality they were made in. Like you said, they are merely captures of things, of moments."
                                            l "Is a picture of a banana a banana?"
                                            l "I would say it isn't really, it is merely a picture of it."
                                            l "And depending on how you display that picture there is even another layer of it becoming less real. Pixels of a screen trying to mimic the original object with futile effort. Differently colored chemicals blending together to create something organical."
                                            l "I think only the present is real in a way. Only this moment right now. Everything beyond \"now\" is just speculation, hopes and dreams."
                                            l "And everything before \"now\" is just memories, transcripts of what happened, but never truly the moment itself."
                                            menu:
                                                "But for me the future isn't just a speculation. Because of the timeloop I know what will happen next.":
                                                    l "I see..."
                                                    l "That is an interesting thing you bring up."
                                                    l "Sure, you know what happened the last time, maybe even the last times."
                                                    l "But can you ever be truly sure wheter or not it is going to happen again before it does? I'd say you just can make a better educated assumption than the rest of us in here."
                                                    l "Also, your knowledge of this future has it's limits. It just lasts up until the furthest you've ever been."
                                                    l "Besides, now we are talking about the future in this game."
                                                    l "But if you think about it like that, doesn't that mean you also know how things will go in a book you reread or a movie you watched once again?"
                                                    l "Maybe even more than you know the future here, since here a certain variable can change, altering what happens, what lines of text you read."
                                                    l "And movies and books always have the same exact objective events happen in them regardless of how many times you interact with them."
                                                    l "But that's besides the point really, my point is that from your viewpoint what we call \"the future\" in here does functionally only exist once."
                                                    l "Or it keeps moving I suppose, but it is always the furthest you've ever gotten in your attempts to save me."
                                                    l "Everything else is the past essentially, since you already know how it goes, you already have memories of it."
                                                    l "Look at the future in your own reality for example, you don't know how that one will go. So that version of the future better aligns with what I just said doesn't it?"
                                                    l "Phew, my head hurts from all this complicated talk honestly."
                                                    $ kokiri_scenery_headhurt = True
                                    
                            "That does make sense... But then why do I have really boring memories aswell? Ones of doing chores for example.":
                                "Filler"
                    "My choices. Inside and outside of this game I can choose what I want to do. I am not following a script of sorts, I can decide one thing and then do another.":
                        l "I see..."
                        l "This one is hard to prove isn't it?"
                        l "How do we know we have free will and we are not merely blessed with the illusion of such a thing?"
                        l "Take me for example, since I am in a game and you make all the choices in this game I merely react to them."
                        l "I still justify my actions as them being my own choice, but they are prewritten, aren't they?"
                        l "We try to trick ourselves into thinking we have more control over our choices than we really have."
                        l "But even in our own reality, in your reality, you are limited on what you can choose. You are even limited in the things you consider options in the first place by things like experiences etc."
                        menu:
                            "Yes, but you say you are real, right? So even if I also am limited in my choices like you, that still makes me real.":
                                jump kokiri_topic_questMade_youAreReal


            "I wouldn't believe it unless there was some concrete proof.":
                "filler"
            "I don't think I would buy it at all.":
                l "That's fair, I think the only reason I even believed you when you told me I existed in a game was because you met me in this place."
                l "And even then, there is still something inside of my mind that can't believe it, that mustn't believe it."
                l "I need that part so I don't just fully go and lose it right now."
                l "Being confronted with the fact that you are repeatedly dying and also exist in a game at the same time is a bit much to take for a sane mind I'm afraid."

            "I would believe it immediately.":
                l "You would?"
                l "Huh, I must admit I was not expecting that answer."
                l "I feel like most people would need atleast a bit of proof to convince them, right?"
                l "Especially considering how worldshattering info like that could be."
                l "But then again, you have dealt with a lot already haven't you?"
                l "Maybe that's why it would be easier for you to accept such news."
                l "As much as I'd now like to mess around a little by telling you that you are not real and giving some arguments I think I'm not going to do that."
                l "Because truthfully, I think it is important for us to consider ourselves real, whatever that might mean for us."
                l "We are much happier when we feel as if we are in control, even if that might not always be the case, even if it might never truly be the case."


    
        jump kokiri_scenery_choice
        #TODO: This might be a mistake in my coding but it seems like this scene usually doesn't lead to scenery choice because kokiri conversation is too high, check this out.
   
        

label kokiri_gamegoal_noGoal:
    $ kokiri_conversation += 1
    l "[persistent.date] chuckles."
    l "So sort of like life in general?"
    l "I mean, I might not be the best person to make this comparison since I'm not entirely sure wether I am alive or not due to me being in a game, but hey, I feel alive for what it's worth."
    l "But anyway, from my potentially flawed point of view our very existence is absurd."
    l "Born without objective purpose and gone before we recieve one, a joke without a punchline."
    l "Maybe this existence is the punchline? "
    l "Maybe we aren't the ones supposed to laugh?"
    l "We can only pretend that we got the joke and feign a smile."
    n "Wow, where did that suddenly come from?"
    l "[persistent.date] notices you being absolutely flabergasted by her mini-monologue."
    l "But that doesn't mean there is no hope at all [persistent.name]!"
    l "We can create our own subjective purpose to compensate the lack of an objective one."
    l "We exists to help our family, friends and loved ones.
    To be able to experience the small joys in life like a warm hug, a good book or eating some cheese while still being in your bed."
    l "We exist because we already existed so we might aswell keep going at it, right?"
    l "And even if the universe doesn't care about us, even if we are unfathomably small in it's eyes, we care about eachother and in eachother's eyes we are unfathomably large."
    l "Maybe that is the purpose of this game? To show you that it is possible to make your own purpose?"
    l "If you consider that I can tell you about this, it's at the very least programmed into the game."
    l "It could be a red herring but I think it might be worth thinking about more later."
    jump kokiri_scenery_choice

label kokiri_gamegoal_noIdea:
    $ kokiri_conversation += 1
    if kokiri_conversation == 1:
        l "That's fine, we can figure your goal out together."
        n "[persistent.date] scratches her chin and continues."
        l "Let's see, first of, how does this game look to you?"
        menu:
            "I just see text on the screen and some graphics, everyone's text is slightly different. I also get a few clickable links to select what I want to say.":
                jump kokiri_gamegoal_noIdea_howGameLooks
    elif kokiri_conversation == 2:
        l "So, we already now how the game looks to you. What about the \"retrying\" part of the game? Do you always automatically come back when I end up getting killed?"
        menu:
            "It's not automatic, a link with the text \"Retry\" shows up and when I click it I restart the day but I get to keep the knowledge of the things that happened.":
                jump kokiri_gamegoal_noIdea_2
            "You don't always die, sometimes we are just not together. For example because I break up with you or because you don't want to be around me anymore. But the game still considers it a game over." if lilithAliveAndRetriedCounter > 0:
                $ kokiri_toldLillySheLives = True
                l "...Interesting."
                l "So there are moments where I survive?"
                l "What happens then?"
                l "Does the day restart anyway?"
                menu:
                    "Yup, it just restart, no matter what. (Lie)":
                        l "Really?"
                        l "So it is worse than we thought."
                        l "There is no escape..."
                        l "I'll just be stuck in this loop forever and ever."
                        l "Although... maybe there is one way."
                        l "What do you think would happen if you stop playing this game?"
                        jump stopPlayingGameConsequences
    
                    "It does, but only if I choose to click the \"retry\" option.":
                        l "..."
                        l "So you are saying that I survived one of these loops and you restarted it anyway?"
                        l "Why, just because we didn't end up together?"
                        if love_meter <= 2:
                            l "I thought you wanted to make sure I was safe..."
                            l "But you just want to make sure I stay with you, don't you?"
                            l "That you don't have to let me go for yet a little longer."
                            menu:
                                "I am really sorry, I just couldn't let go yet.":
                                    l "No I am really sorry [persistent.name]. Sorry for ever trusting you."
                                    l "Well I won't make that mistake again this time."
                                    jump angryLilith
                        else:
                            l "Look, I like you [persistent.name]. I really do."
                            l "And as much as I want there to be a way for us to end up together, isn't it your priority to save me?"
                            l "If so, then why did you retry after I was perfectly safe?"
                            menu:
                                "I couldn't let go, not yet.":
                                    n "She gives you a sympathetic look."
                                    l "... Letting go is hard sometimes isn't it?"
                                    l "I mean, \"sometimes\" might be an understatement."
                                    l "It almost always is hard."
                                    l "And I know that you might have an especially hard time letting me go since we've spent so much time together from your perspective."
                                    l "And yet, letting me go will effectively \"undo\" all of that, won't it?"
                                    l "I wouldn't remember any of it and just go my seperate way, away from you."
                                    l "But you also have to understand what I'm going through, don't you?"
                                    l "This cycle of death. Of pain."
                                    l "Sure, we had some great moments together I'm sure! Even just here in this moment I had a really good time when you consider the circumstances."
                                    l "But I have died more than anyone should ever do [persistent.name]."
                                    l "Clinging onto me is only going to hurt the both of us I'm afraid."
                                    l "We might have found eachother in this game, but I don't think this game was made for us to end up together."
                                    l "Whatever we will try, I have the feeling it is just going to lead to more death."
                                    l "So, as much as I wish there would be another way, I think this is our best shot."
                                    l "I know what I'm asking is pretty big, but I'm hoping I mean as much to me as I mean to you."
                                    menu:
                                        "You do, I'll try my best to let you go next time.":
                                            n "She gives you a gentle smile."
                                            l "Thank you [persistent.name], that's all I ask."
                                            l "So..."
                                            n "She grows quiet for a moment, before she continues."
                                            jump kokiri_semiEnding
                                        "I'm sorry, I just can't do it.":
                                            l "I understand."
                                            l "But you also have to understand that you will have to let me go at one point [perisistent.name]."
                                            l "You cannot possibly keep this up forever."
                                            l "And although I do understand I also think if you can't let me go I'll have to take things in my own hands."
                                            l "As much as I had hoped the two of us could work out, in here we can't."
                                            l "The sooner you accept that the better."
                                            l "Goodbye [persistent.name]. I genuinely wish you the best and hope there is no bad blood between the two of us for what I'm about to do."
                                            jump angryLilith
    
label kokiri_gamegoal_noIdea_howGameLooks:
    l "Ah I see, so you can't see the absolutely stunning view from our picknickspot?"
    menu:
        "Yup, the best thing I can get is a description of it if the game feels like giving me one. Otherwise I just see a fixed point, as if our conversation is filmed with a static camera.":
            $ kokiri_scenery_gamegoal = True

            jump kokiri_scenery_choice


        
                    
label kokiri_gamegoal_noIdea_2:
  
    n "Lilith rubs her chin."
    
    l "That's interesting, so it's just like you're choosing what to say right? This entire game consists of you making choices, maybe not pressing the link is also a choice?"
    l "If it wasn't then why wouldn't you just automatically restart the day like I thought?"
    l "In a way I suppose not doing something is also an action."
    menu:
        "That makes sense actually, thanks Lilith!":
            jump kokiri_gamegoal_noIdea_2_makesSense

        "That makes no sense, if it was really about that choice than why wouldn't there be a \"Do not retry\" link?":   
            jump kokiri_gamegoal_noIdea_2_makesNoSense  


    label kokiri_gamegoal_noIdea_2_makesSense:
        l "I'm glad to see that we're on the same page!"
        l "So, do you want to keep talking about the purpose of the game?"
        
        menu:
    
            
            "No, I think I understand the purpose of this game now. Thanks Lilith!":
                
                    l "No problem at all, I'm just happy that I could help out!"
                    l "Afterall, we are a team aren't we [persistent.name]?"
                    l "So it's nice to know that I can somehow assist you during your attempts to save me."
                    l "Because this loop is too heavy to just carry on your own. And know that you never have to."
                    l "Just like you are there for me I am there for you."
                    l "I hope you will never forget that."
                    menu:
                        "I won't. Thank you Lilith.":
                            n "She gives you a big smile."
                            l "That makes me very glad."
            "Yeah, I'm still kind of stumped.":
                    l "Alrighty, I think it's better if we try to get some info from the source itself now. That will greatly help with setting up our own interpretation."
                    label gamegoal_noIdea_2_stumped:
                        l "Is there like an about section in this game with info on it and did you read it?"
                        menu:
                            "Actually, I have a different idea to reach the source. There is a narrator in this game. Maybe they know more?":
                                jump tellLilithAboutNar
                            "It exists, I saw it when I started the game but I never got around to reading it.":
                                l "Well, I think you might want to give it a shot if you really want to know what the goal of this game is."
                                n "Lilith gives you a smile."
                                if kokiri_conversation >= 4:
                                    jump kokiri_4
                        
                            "I actually did read it, let me fill you in on what it said." if persistent.fakeAbout_knowledge or persistent.trueAbout_knowledge: 
                                menu:
                                    "It said that we will only have one date and that I need to try to make it as great as possible. Because just like in real life there are no do-overs and that is what makes our choices beautiful." if persistent.fakeAbout_knowledge and not persistent.trueAbout_knowledge:
                                        l "Wait, what?"
                                        l "But there literally are do-overs here, right?"
                                        l "You constantly need to retry."
                                        l "When did you read that description in the about section?"
                                        menu:
                                            "In the begining, I think at the time of our first date, the very first one.":
                                                l "I see, I might have a hypothesis, could you take a look at it once again for me?"
                                                l "Just try to access it now, however you would do that."
                                                l "I'll wait for a moment until you do that."
                                                n "She grows quiet for a moment."
                                                l "Did it work?"
                                                l "Did it say something else?"
                                                menu:
                                                    "It did. It said something about this game being about how we deal with our choices or the lack thereof." if persistent.trueAbout_knowledge:
                                                        
                                                        l "Just like I expected, seems that the first about section you read was a lie. Or at the very least not entirely the truth."
                                                        l "Let's think about the real one we just found."
                                                        jump gamegoal_noIdea_2_stumped_readAbout_true

                                                    "I didn't manage to open it. I'll just do it sometime else." if not persistent.trueAbout_knowledge:
                                                        l "Alright, when you manage to open it in an other attempt feel free to tell me, then we can try to understand all of this a bit better."
                                                
                                    "It said this game is about how we deal with our choices or the lack thereof." if persistent.trueAbout_knowledge and not persistent.fakeAbout_knowledge:
                                        jump gamegoal_noIdea_2_stumped_readAbout_true
                                    "There were two about sections actually." if persistent.fakeAbout_knowledge and persistent.trueAbout_knowledge:
                                        menu:
                                            "The first one talked about how we will only have one date in total and then I won't be able to retry since that is what makes our choices more beautiful. That one was around the time of our very first date.":
                                                menu:
                                                    "The second one talked about how this game is about how we deal with our choices or the lack thereof.":
                                                        l "Interesting..."
                                                        l "So the first about section was some kind of fakeout meant to trick you?"
                                                        l "The second one is pretty interesting though, let's talk about that one."
                                                        jump gamegoal_noIdea_2_stumped_readAbout_true
                                label gamegoal_noIdea_2_stumped_readAbout_true:
                                    l "So this is a game about trying to fight the lack of real choice? Then the link thing kind of makes sense, what better way to fight the lack of choice than not making any at all?"
                                    l "It's an act of pure rebellion! But still something is not right, then you just end up with a bad ending, with me getting killed and you not retrying to save me."
                                    l "I wonder if that's the other thing this game is about that the maker doesn't want to spoil."
                                    l "What is equally as rebellious if not more than not playing the game?"
                                    n "Lilith seems lost in thought."
                                    l "That's a hard one, do you have any clue?"
                                    menu:
                                    
                                        "Maybe playing the game wrong? Not doing the paths that are expected like saving you or being nice.":

                                            l "You could be on to something there! Playing the game wrong seems like an extension of not playing it."
                                        
                                            n "Lilith grows silent for a moment."
                                        
                                            l "... But would that make it okay for you to mistreat me and let me die aswell?"
                                            
                                            l "What's the point in having a good ending with me after you had to bad things to me?"
                                            l "On second thought, that's probably not it..."
            
                                            if kokiri_conversation >= 4:
                                                jump kokiri_4
                                        "Maybe trying to somehow find a way to cheat the game?":
                                                
                                                l "You could be on to something there! Cheating the game and altering the way how you play because of it might be as rebellious."
                                                
                                                n "Lilith scratches her chin."
                                            
                                                l "But how would you accomplish something like that? "
                                                l "And even if you did, would you feel any accomplishment? Wouldn't you just feel emptier because you didn't truly win and you just cheated your way into winning?"
                                                l "On second thought, that's probably not it..."
                                                if kokiri_conversation >= 4:
                                                    jump kokiri_4
                                        
                                        "Maybe giving myself a dumb name?":
                                            
                                            n "Lilith chuckles slightly."
                                            l "I suppose that would be quite rebellious but more in the young teen way, not the way I was thinking of."
                                            l "Although you are always welcome to try it if you want Fartyfarty."
                                        
                                            n "Lilith laughs."
                                            
                                            l "Not sure if I would be able to take you seriously with that name though, you're probably safer off with \"[peristent.name]\" as name."
                                            if kokiri_conversation >= 4:
                                                jump kokiri_4
        $ kokiri_conversation_silent()

    label kokiri_gamegoal_noIdea_2_makesNoSense:         
        n "Lilith shakes her head."
        l "Then the choice wouldn't be as impactful as it is now. A \"Do not retry\" link would just give away the entire point."
        l "Not clicking a link forces the player, I suppose that's you, to think it over more than just clicking another link instead."
        menu:
            "Alright, that actually makes a lot of sense. But what is the point of it all?":
                l "Well, that's the big question isn't it? I have my own interpretation but I think it's better if we hear it from the source itself."
                jump gamegoal_noIdea_2_stumped
        $ kokiri_conversation_silent()            
         
                        
                        
                
                        

                
        
                
            
                
        
            
                
        
    
    
        
   
          
                                
label kokiri_gamegoal_succesful_survive:
    
    n "[persistent.date] bursts out in laughter."
    l "I suppose that might be a good definition for a succesful date but I think you might have put the bar pretty low [persistent.name]."
    l "For what it's worth, I think this date is really lovely! Although my head still hurts from trying to fully comprehend what's going on.
    Atleast it's a different kind of pain than the one I get from constantly having to grade my student's tests, so there's that."
    n "[persistent.date] lets out a hearthy chuckle, not much later she seems to be lost in thought."
    l "You know, what you just said is quite interesting."
    l "So a \"succesful\" date would be one where I don't end up dying, right?"
    l "And what if we never went on a date at all?"
    l "Would that keep me alive?"
    l "And if it did, would you consider that a succes?"
    menu:
        "I would, I just want to keep you safe.":
            $ kokiri_goalSurvive = True
            if persistent.ending_breakup:
                n "Then why did you come back after you turned her down?"
                n "When you knew very well she was safe?"
                n "That she was happy?"
                n "Are you perhaps lying to someone?"
                n "I suppose the only question is wheter it's to her, or to yourself."
            if love_meter > 2:
                l "That's very reassuring to hear."
                l "Because my life is literally in your hands afterall."
                l "I am lucky that I feel I can trust you."
                l "I know that if it had to come to it, you would do the right thing."
                l "But for now, I'm hoping there is some other way."
                l "There has to be, right?"
                l "What kind of game would this be if there wasn't? That just feels like bad design to me."
                jump kokiri_scenery
            else:
                l "Well then, why don't you just tell the past me that you don't want to go on this date anymore?"
                l "Wouldn't that fix everything?"
                if persistent.ending_breakup:
                    n "Given that you came back after you did exactly that I doubt you agree with her on that end, do you player?"
                    $ persistent.CancelledBeforeBeingAsked = True
                else:
                    if lildeaths > 25:
                        n "Something tells me it might be a while before you even consider doing that."
                    else: 
                        n "That's not a bad idea actually, it might be worth keeping in mind."
                l "Although for now I guess we already are here, so we'll have to make the best out of it."
                l "But can you promise me that next time you will try to cancel our date?"
                menu:
                    "I promise I will.":
                        $ love_meter += 1
                        $ love_meter_updater(False)
                        n "Lilith gives you a slight smile."
                        l "Thank you [persistent.name]."
                        l "I know that cancelling the date might be hard for you, especially since all of this is not real to you."
                        l "So I appreciate you giving it a shot."
                        if persistent.kokiriBrokenPromiseCancelDateTurnCounter > 0:
                            n "It indeed is really hard to cancel the date isn't it player?"
                            n "That must be why you haven't done it for [persistent.kokiriBrokenPromiseCancelDateTurnCounter] attempts now even after she asked you to."
                            n "Or is it just because you like lying to her?"
                            n "Either way, I'm not sure why you chose this exact same dialogue again if you still haven't done what she asked you to do."
                        $ kokiri_promiseCancelDate = True
                        jump kokiri_scenery
                    "I actually already tried cancelling it before." if persistent.ending_breakup == True and persistent.kokiri_HonoredPromiseCancelDate == False or persistent.CancelledBeforeBeingAsked == True:
                        label kokiri_triedCancellingBefore:
                        
                        n "Lilith leans in slightly closer, her eyes growing slightly wider."
                        if love_meter > 2:
                            l "What happened when you tried that? You are back here so something must have happened, right?"
                        else:
                            l "Then why are we back here? Why are you back here? What happened?"
                        menu:
                            "You died (Lie)":
                                "Filler"
                            "I wasn't ready to let go.":
                                "filler"
                            "You were happy, you had a family. The game just sent me back like none of it mattered.":
                                l "..."
                                l "I'm sorry [persistent.name], I... I am just not sure what to say to that."
                                l "I had a family?"
                                n "You tell her about Ron, about her kids. That they all seemed really happy together."
                                n "She stares out into the distance for a moment."
                                l "So all of that got undone?"
                                l "That is horrible, even when I, no, a version of me somehow survived we still end up back here."
                                l "Was it because we never went on a date?"
                                l "Does this loop only end when we do and I survive somehow?"
                                l "Or are we overlooking something and my safety is not even the goal of this game?"
                                l "Although it is strange..."
                                l "Why didn't it reset the moment you called off our date?"
                                l "Why did it keep going for a while and only then reset?"
                                n "She quiets down for a moment."
                                l "Maybe it's time for some more desperate measures?"
                                l "I'd like you to try and hear me out, alright?"
                                l "What if just any interaction between the two of us keeps the loop going?"
                                l "The day always resets at around the time when I call you, right?"
                                l "Maybe next time you shouldn't pick up?"
                                l "Maybe that is why it keeps jumping back to that point specifically?"
                                l "Look... I know that I have been asking for a lot already."
                                l "It's just... I am begining to lose hope that there is a way out of this loop."
                                l "And this seems like one of the few things we haven't tried yet, I think it's worth a shot."
                                l "Would you be willing to test out my theory?"
                                menu:
                                    "I would.":
                                        n "Lilith gives you a bright smile."
                                        l "...thank you [persistent.name], thank you from the botom of my heart."
                                        l "If it works... if I don't see you again... just know how much this means to me."
                                        l "So this could be our last time together?"
                                        l "Better try to enjoy it then."
                                        jump kokiri_scenery

                    "I actually already tried to cancel it before because this isn't the first time you asked me to." if persistent.ending_breakup == True and persistent.kokiri_HonoredPromiseCancelDate == True:
                        jump kokiri_triedCancellingBefore



        "No, because we need to go on a date and you need to survive, not one or the other.":
            l "Says who [persistent.name]?"
            l "Who is making these rules?"
            l "And why are you following them?"
            l "Why is my survival merely a part of your goal and not your priority?"
            l "How many deaths did you let me go through just because you want to end up with me?"
            if love_meter >= 2:
                l "I thought you cared about me, about my life..."
                l "I thought you were doing all of this to protect me."
                l "But that's not what this is all about, is it?"
                l "You just want to reach your arbitrary goal, even if it kills me, over and over again."
                l "How many more of my deaths will you need to reach that goal [persistent.name]?"
                l "You don't even know if it exists, right?"
            l "You know what?"
            l "I can't do this, I just can't."
            l "This is too much for me."
            l "I can take a lot [persistent.name], but I won't just keep sitting here while you talk to me like this."
            l "I'm not just a toy you can play around with as you please, who you can drag around on your whimsical adventures."
            $ noTalkAngryLilith = True
            jump angryLilith

    jump kokiri_scenery_choice
label kokiri_gamegoal_succesful_gameDecides:
    l "So you are going to take some game's word for it? Aren't you able to tell whether or not a date is succesful based on your own feelings?"
    n "[persistent.date] grows quiet for a moment before she continues."
    l "You know, I don't need a game to tell me that this is a good date [persistent.name]."
    l "It might be far from what I expected but that makes it so much more unique."
    l "You took me away from my own mind, even if it's just for a short moment."
    l "I haven't been in the..."
    l "brightest place lately."
    l "To tell you the truth, I have thought about joining my brother a few times..."
    l "But I don't want you to worry about me [persistent.name], I might have been in a dark place but I was working on myself.."
    l "I fought the thoughts with all I had, I gave myself reasons to keep existing."
    l "At first it was for the poems I would write, I didn't want to vanish and leave a poem in a half-written state."
    l "But at some point I feared that if I would finish even a single one I wouldn't have anything to live for anymore."
    l "I only wrote half a poem for about two whole years, that way I had something anchoring me to this world constantly."
    l "[persistent.date] chuckles uncomfortably."
    l "I hated prolonging my poems like that just to have an excuse."
    l "I never truly got any work done, it made me feel terrible." 
    l "But somehow one day something clicked inside me. I realised that I still had [persistent.date_sis_nickname] and my mom."
    l "From then on out I started to live for them."
    l "They needed me, now more than ever and if I were to vanish they would be devasted."
    l "It's only recently that I started living for myself again. That I wanted to enjoy things again."
    l "It's been about two years since then, I'm still not entirely healed but I'm trying my best."
    l "So, I don't want you to worry about me alright? I'm alright all things considered."
    l "The best way you can help me is to just enjoy this moment with me."
    l "I'm just telling you this to try to make you realise what an effect you have on me."
    l "Even if the game doesn't tell you that directly."
    l "Isn't that what matters? How we think this date is going?"
    jump kokiri_scenery_choice
label kokiri_gamegoal_succesful_IdoNotKnow:
    l "Well, for whatever it is worth, I think this is a succesful date [persistent.name]!"
    n "[persistent.date] gives you a cute smile."
    l "It might not entirely be what I expected but it sure is a nice date."
    menu:
        "I also think this is a nice date [persistent.date].":
            n "[persistent.date] lets out a small laugh."
            l "I think my heart just jumped a little hearing you say that [persistent.name]."
            l "You know, even after everything I went through, after all the self-reflection I did, I still have this part of me that finds it hard to believe that people could like me."
            l "I, or atleast that part of me still need to get used to that idea."
            l "But, enough about that, you being here is helping me a lot!"
            $ kokiri_scenery_shutUpLackOfSelfEsteem = True
           
            #TODO: (Add an option to tell her she's enough if you decline to watch the scenery.)
            jump kokiri_scenery_choice


        "Every date with you is a nice date, I'll cherish them all forever.":
            $ kokiri_cherishAllDates = True
            l "Oh right, for a moment I almost forgot we had multiple dates already from your point of view."
            l "It's kind of hard to wrap my head around but oddly... comforting?"
            l "The idea that you keep coming back for me, that must mean you atleast like me enough to do so."
            l "My brain does not have to constantly doubt wether you like me or not because of the idea that we had multiple dates already."
            l "Sure, most of them end up with me dying but let's just hope that this one doesn't."
            l "But oh wel, I suppose this view is to die for."
            l "[persistent.date] chuckles, but in her eyes you can catch a brief glimpse of fear in her eyes."
            n "She looks you into the eyes you can see that fear slowly fade away. And yet, it never fully fades."
            l "..."
            l "All those dates... all those deaths..."
            l "Were they bad?"
            l "Did I suffer much?"
            l "And the next one... if there is going to be a next one, will that one be bad?"
            menu:
                "I think it's better to not talk about it in detail but yes, they were pretty bad.":
                    l "Now my mind kind of just is imagining the worst possible things."
                    l "Still though, maybe it is even worse somehow, so maybe you are right."
                    l "Although I do really appreciate you not sugarcoating it."
                    l "So thank you [perisistent.name]."
                    $ love_meter += 1
                    $ love_meter_updater (False)
                    l "I'm glad I am going through all of this with you."
                    l "Atleast that way I don't have to feel alone."
                    
                "I think we should moreso focus on this moment right now for your peace of mind if that is okay.":
                    l "I suppose you do have a point..."
                    l "Maybe it's better to just not know."
                    l "Even though I really am wondering how bad they are atleast like this I might be able to pretend like they are very minor."
                    l "As minor as a death can be I suppose..."
                    n "Lilith stares out into the distance for a moment."

                "They were horrible, there was so much blood.":
                    n "Lilith gives you a shocked look."
                    n "Her eyes grow wide and her entire face turns pale."
                    l "..."
                    l "Why did you have to say that?"
                    l "I can almost certainly tell that you are lying but now that image is stuck in my head."
                    l "I can't do this anymore."
                    l "If this is how you act towards me then I think I'm equally safe if not more safe on my own."
                    l "Goodbye [persistent.name]."
                    $ love_meter -= 2
                    $ noTalkAngryLilith = True
                    $ love_meter_updater(True)
            jump kokiri_scenery_choice







label kokiri_scenery:
    if persistent.tracker == 3:
        $ persistent.tracker3 = True
    if kokiri_alternateplace == False:
        $ persistent.kokiri_watchedScenery = True
        n "From the spot you picked on the hill you have a gorgeous view of the village where most of your dates with [persistent.date] took place."
        n "It's pretty calm in the village, here and there you might catch a rare glimpse of a car or a pedestrian but other than that the streets are completly empty."
        l "This view is absolutely fantastic isn't it?"
        l "When my parents used to take walks with me and my brother in this forest I knew that I just had to keep coming back here."
        l "And I did! Many times actually. I like to come here whenever I have some spare time or when I really need to get some time away from things."
        l "The sunrise here is absolutely beautiful, maybe we'll be able to share that moment today."
        l "I'd like that..."
        n "As you enjoy eachother's company for a while while looking off into the distance the both of you spot a red Sedan as it drives closer and closer to the cafe at troubling speeds."
        if car_caught == False:
            n "When the car reaches the cafe it rams a garbage container that falls over in front of the doors and drives up on a ramp."
            n "It launches itself over the building, coming back the other way and driving away like nothing happened."
            n "After a short while the car speeds straight into the doors of the Chinese restaurant for it's second act of pure destruction."
            n "The car backs away from the Chinese restaurant to speed to it's next destination."



        else:
            n "When the car reaches the cafe it rams a garbage container that falls over in front of the doors and the Sedan drives towards a convieniently placed ramp."
            n "Just before it manages to reach the ramp a copcar drives in front of it, forcing the driver to stop."
            n "After some questioning and an alchohol test the police put the man in their car and drive off with him."

        n "Not much later a swarm of geese break the doors of the restaurant wide open and dash inside."
        n "As fast as they entered the restaurant they leave it with practically everyone in the restaurant being kidnapped by them."
        l "So... I was kidnapped by geese?... This is getting more and more unbelievable, and yet I'm seeing it happen with my own eyes."
        l "What's next? Aliens?"
        n "She lets out a small chuckle, but you can sense there is some worry behind it."
        if persistent.kokiri_death_4_hill or persistent.kokiri_death_4_noHill:
            n "You know how unfortunately right she is. You wish it would sound as impossible to you as it does to her right now."

        n "Suddenly you can hear the sound of sirens, of police sirens."
        n "The police sirens are coming from near the mall, where the burger restaurant is located."
        n "The same restaurant where [persistent.date] got shot..."
        n "You point at the mall and tell her about the events that took place there."
        n "She gasps for a moment."
        l "Wow, it seems like we have gone through a lot together [persistent.name]. I'm not sure if it's a good or a bad thing that I can't remember."
        n "You shudder for a moment, it's definetly a good thing that she can't remember the gruesome ways she died."
        n "Ignorance is bliss afterall."
        n "In it's final act of destruction the car races at full speed and smashs against the entrance of the mall."
        n "The burger restaurant explodes due to the gas-explosion, taking a sizeable chunk of the mall with it."
        n "However the Sudan escapes without a scratch."
        n "After the explosion the village begins to turn calm once more, the whole ordeal seems to have finally ended."
        l "Has it... Has it ended?"
        $ kokiriSceneryWatched = True
        menu:
            "Yes, it's finally all over.":
                jump kokiri_scenery_allOver
            "Not quite. You might want to sit on my right instead of my left." if persistent.kokiri_death_1:
                jump kokiri_death_1_prevented
    else: 
        $ persistent.kokiri_watchedStarsAlternatePlace= True
        n "[persistent.date] and you lay down on the blanket as you try to look to the star-filled sky between the trees."
        n "A gentle breeze blows some of the branches away, as if helping the two of you to get the best view possible."
        n "It is quiet for a moment."
        n "A lovely kind of quiet, serene silence."
        n "You find yourself holding your breath without thinking about it, almost as if to stop yourself from breaking the magic."
        n "For a short moment everything is alright, better than alright, everything is perfect."
        n "Here you are, together with [persistent.date], enjoying the lovely view that your eyes are being blessed with."
        n "During this short moment you feel completely at ease, you only noticed how tense you were all this time when you started relaxing."
        l "This is really amazing [persistent.name], I know we probably have other concerns right now but it just feels so nice to enjoy the serenity of this moment, doesn't it?"
        l "I can see you are also really enjoying it, or well, I suppose your player-character is."
        l "But still, I hope you are enjoying it aswell! That the beauty of this moment can somehow be translated well enough through the screen, or that you can fill in the gaps."
        l "You know, the softly swaying trees that seem to dance to a song whispered by the wind, the crickets serving as a background choir. The soft silver light of the stars that peek behind the clouds every now and then."
        l "You are perhaps even lucky in your current situation, you can create your own image of how this moment looks, feels, sounds and noone could tell you you were wrong about it."
        l "You can make this absolutely beautiful moment even more perfect in your head and in a sense of the word it will be \"real\"."
        l "That's a beautiful thought isn't it?"
        menu: 
            "*Nod as you enjoy this moment to the fullest.":
                if love_meter > 2:
                    n "[persistent.date] sits back up and gives you a long, thoughtful look."
                    l "But you'll never make me jealous with your power. Do you know why?"
                    menu:
                        "No, why?" if not persistent.kokiri_perfectMomentStarGaze_knowledge:
                            jump kokiri_scenery_perfectMoment
                            label kokiri_scenery_perfectMoment:
                                n "She sits closer to you and begins to lean against you." 
                                n "You feel a rush of calm washing over you, you are fully content to live out the rest of life like this."
                                n "She brushes her hand to the side of your ear and whispers."
                                l "{size=*0.5}Because I don't need it, this moment is already as perfect as my poor little heart can bare.{/size}"
                                n "She let's out a very quiet chuckle as she lets herself fall back down on the blanket with a content sigh."
                                n "The only reason you could hear it is because she was sitting so close to you."
                                $ persistent.kokiri_perfectMomentStarGaze_knowledge = True
                        "No, why? (Pretend to not know.)" if persistent.kokiri_perfectMomentStarGaze_knowledge:
                            jump kokiri_scenery_perfectMoment
                        "I might have an idea actually. I think it was something along the lines of: \"Because I don't need it, this moment is already as perfect as my poor little heart can bear.\"." if persistent.kokiri_perfectMomentStarGaze_knowledge:
                            n "[persistent.date] bursts out in laughter."
                            l "I see how it is [persistent.name]!"
                            l "Did you watch the stars with me again just so you could tell me you knew?"
                            l "Or did you come back because you agree?... Do you think this moment right now is perfect aswell?"
                            menu:
                                "If I'm being honest... I came back to see your reaction to me already knowing what you'd say.":
                                    l "Hey, that's totally fair [persistent.name], I'd probably be doing the same thing if I were you to be honest."
                                    l "I'd love to use my powers to get you to just laugh until you pass out, figuratively speaking of course."
                                    l "But if anything I'm flattered you seem to feel the same way about me, that you came back here just to get me to laugh."
                                    l "Now that I'm thinking about it actually, that might be the hardest I've laughed in a long while, so thank you for that [persistent.name]!"
                                    l "It's just a bit of a shame that we have to meet in these circumstances, but atleast we can find some comfort in them."
                                    l "Atleast I can find comfort in you."
                                    n "Lilith hugs you tight for a moment."
                                    n "She keeps holding you, it feels like quite some time has gone by now."
                                    l "I'm scared to let you go [persistent.name]."
                                    menu:
                                        "I'm scared too.":
                                            l "I know... and that makes it a little less lonely, I think."
                                            l "We really shouldn't have to go through this. I wouldn't wish this to anyone else."
                                            n "Her voice trembles slightly, but she doesn't let go."
                                            l "You know, sometimes I wonder if anyone else feels like this. Like they're caught in a place between holding on and letting go."
                                            l "But having you here... it makes me believe there's something worth holding on to."
                                            n "Lilith pulls back slightly, just enough to look into your eyes."
                                            l "Promise me you'll stay, at least for a little while longer."
                                            n "She smiles softly, her eyes glistening as if they're holding back tears."
                                            l "Even if we're scared, we can face it together, right?"
                                            n "Her grip tightens just slightly before she finally releases you, though the warmth of her embrace lingers."

                                        "Then hold on to me for as long as you want.":
                                            l "Are you sure? Because I might never let go if you say that."
                                            n "Lilith chuckles softly, though her voice carries a hint of sadness."
                                            l "You have no idea how much that means to me, [persistent.name]."
                                            n "She buries her face in your shoulder, and you can feel her taking a deep, shuddering breath."
                                            l "I didn’t think I needed anyone like this... but you’ve proven me wrong."
                                            n "Her hold on you tightens slightly, as if she's afraid you'll disappear the moment she lets go."
                                            l "Thank you. For being here. For staying. For... everything."
                                            n "Eventually, after what feels like both an eternity and no time at all, she loosens her grip but still keeps her hands resting on your shoulders."
                                            l "If it’s okay with you, I might come back for another hug later."
                                            n "Her smile is small but sincere, a quiet gratitude in her expression that words can't quite capture."

                                    
                                "I think all our moments together are perfect, but I agree, this one has something magical to it.":
                                    $ love_points += 2
                                    $ love_meter_updater(False)
                                    l "..."
                                    l "..."
                                    l "..."
                                    n "[persistent.date] seems to be frozen for a moment."
                                    l "Uhm... sorry about that [persistent.name], it's just that..."
                                    n "She leaps up and envelops you in a tight hug."
                                    n "Your arms wrap around her aswell instinctively."
                                    l "Thank you..."
                                    l "That is probably the sweetest thing someone has ever said to me."
                                    l "I..."
                                    l "I think I won't let you go just yet, I'm not sure if I'm physically able to let go right now. Is that alright?"
                                    menu:
                                        "That's all fine with me, take all the time you need [persistent.date].":
                                            l "Oh don't worry, I will!"
                                            n "With her arms wrapped around you you feel as if you could melt into them. "
                                            n "You feel that same rush of calmness wash over you, only this time to your surprise it's even stronger."
                                            n "Everything turns blank for a moment. Your focus is fully on this lovely moment."
                                            n "Your thoughts stop working every now and then, you blink in and out of consciousness."
                                            n "It's hard to say how long this hug has lasted. The only thing you do know is that you want it to last so much longer."
                                            jump kokiri_death_2 
                else:
                    #Have this be the dialogue for if your love meter is 2, love meter 1 shouldn't even be able to reach this in the first place and have slightly different dialogue.
                    l "{size=*0.5}Although I'm not sure if you really think that aswell...{/size}"
                    n "She uttered it very carefully, silent enough that you might think she didn't want you to hear it."
                    n "But make no mistake, she was counting on you hearing it."
                    n "There is some silence that at first might seem just awkward, but it is very deliberate."
                    n "She is waiting for your answer."
                    #TODO: Fill this in with a menu where you can say she's right or deny it.
                        
                
                $ kokiriStarGazed = True
            "It really is a beautiful thought. I'd love to make this moment even more special.":
                l "That sounds wonderful [persistent.name]!"
                l "Although to me this moment is already probably the most special it could be."
                l "It has been too long since I felt this at ease."
                l "Which is pretty strange considering what is to come next..."
                l "But right now I don't want to think too much about that, even if my mind keeps jumping back to the inevitable end of all of this."
                l "I wish we could just stay like this forever you know, in this wonderful moment we are sharing before it all goes down."
                l "Maybe forever is a big word, we can't just keep laying here for all eternity can we?"
                l "But I'd just like a little more time than we have now. And after that time is up I'd like to do something else with you."
                l "I'm not sure what yet, but you know, anything else sounds lovely."
                l "Because you know me a whole lot better than I know you."
                l "You have had quite a few dates with me by now, while I only had this one."
                l "And to be fair, as good as this date is, being told you are in a game that keeps killing you isn't exactly my idea of a date."
                l "So I'd love to just have a few regular dates with you, until I know you as well as you probably know me."
                l "Would you like that [persistent.name]?"
                jump kokiri_death_2 

            "I don't think I could make this moment any more perfect even if I tried.":
                l "You really think so? How sweet."
                l "I'm glad we're on the same page."
                l "Maybe we shouldn't try to make this moment more perfect and just enjoy it for how great it is right now."
                l "Sometimes we spend so much time searching for flaws or thinking about what could be better that we forget to appreciate the beauty of what we already have."
                n "[persistent.date] takes a deep breath, her expression softening as a quiet warmth spreads across her face."
                l "But right now, with you here, I don't feel the need to change anything. This is all that I could ever ask for."
                n "The two of you sit in silence for a moment, the world around you fading away. It's as if time itself has paused to honor this fleeting perfection."
                menu:
                    "Smile and say nothing.":
                        n "You smile, letting the silence speak for you. [persistent.date] seems to understand, and her smile grows in response."
                        l "Thank you for being here for me, it means a lot to me. Especially with everything that is going on."


label kokiri_poems:
        if conversationtracker_poems == False:
            n "She takes a notebook with a picture of a pug on it out of her handbag and hands it to you. You recognise the notebook from when you read her poem in the burger restaurant."
            l "I think these ones will be like the one you read before, I've written them quite a long time ago."
            n "[persistent.date] points out a few poems that you can pick from."
        else:
            n "She hands you the notebook once again and points out the poems you can read that you haven't yet."
            

        #Make it so that the normal poems are one menu and the harder ones are an additional menu, that way I can re-use the normal menu if I have to choose between normal and hard.
        if poem_conversation == True:
            $ poem_conversation = False
        if persistent.kokiri_poem_bang_knowledge and persistent.kokiri_poem_lights_knowledge and persistent.kokiri_poem_shadowman_knowledge and persistent.kokiri_poem_snowwoman_knowledge and persistent.kokiri_poem_window_knowledge:
            $ persistent.kokiri_allOldPoemsRead = True
            
        $ kokiri_conversation += 1
        $ conversationtracker_poems = True
        if persistent.kokiri_newerPoems_knowledge == True:
            menu:
                "Read one of [persistent.date]'s older poems.":
                    jump kokiri_poems_oldPoems
                "Read one of [persistent.date]'s more recent poems.":
                    jump kokiri_poems_recentPoems
                "I've actually read all the poems you showed me already, including your new ones, are there any others you could show me?" if persistent.kokiri_allOldPoemsRead and persistent.kokiri_allRecentPoemsRead:
                    $ kokiri_conversation -= 1
                    l "Oh wow, you've read them all? "
                    l "That is impressive in it's own right, especially for the more recent ones I wrote."
                    l "You might be one of the only people that managed to sit through all of those poems, I'd offer you a trophy for that but I fear I left my comically large trophy at home."
                    n "[persistent.date] begins laughing quite hard, you can't help but laugh aswell as you picture her standing besides a trophy that is as big as her."
                    n "After a while the both of you settle down again."
                    l "..."
                    l "So you wanted to read some more poems, right?"
                    l  "Honestly I don't think I have any poems left that I can show you."
                    n "You take a quick glance at the notebook, it has many pages inbetween the poems you read."
                    n "She continues."
                    l  "I don't mean that there aren't any poems left, just that they are a bit too personal. I'm not fully comfortable sharing those yet. I hope you understand [persistent.name]."
                    menu: 
                        "Of course I understand! It's completely fine if you don't want to share those poems right now.":
                            n "[persistent.date] flashes you a thankful smile and gives you a small nod."
                            l "So, what would you like to talk about now [persistent.name]?"
                            menu:
                                "I'd like to talk about something else.":
                                    jump kokiri_talkAboutSomethingElse
                                "I'd like to continue to talk about something.":
                                    jump kokiri_continue_talking

        else:
            jump kokiri_poems_oldPoems
label kokiri_poems_oldPoems:
    menu:
        "Read snowwoman poem.":
            jump kokiri_poems_oldPoems_snowwoman
        "Read window poem.":
            jump kokiri_poems_oldPoems_window
        "Read shadowman poem.":
            jump kokiri_poems_oldPoems_shadowman
        "Read lights poem.":
            jump kokiri_poems_oldPoems_lights
        "Read bang poem.":
            jump kokiri_poems_oldPoems_bang
        "I've actually read all the poems you showed me already, are there any others you could show me?" if persistent.kokiri_allOldPoemsRead and not persistent.kokiri_newerPoems_knowledge:
            l "You've already read all of those poems? I'm flattered that you thought they were worth reading during your different attempts!"
            l "They weren't exactly all great, maybe not even entirely good... but they show a sort of insight in how I used to be many years ago."
            l "I think that has it's own kind of charm, doesn't it?"
            l "But if you managed to sit through all of those poems and somehow want more thank I might have just the thing for you actually."
            l "I have a few more recent poems that I've made, but those poems tend to be a lot longer and have a lot of references to mythology that might make it harder to fully grasp every detail."
            l "Feel free to check a couple of them out though, you can always decide later if you would like to read some extra."
            $ persistent.kokiri_newerPoems_knowledge = True

label kokiri_poems_oldPoems_snowwoman:
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
    jump kokiri_poems_askOrRate

label kokiri_poems_oldPoems_window:
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
    jump kokiri_poems_askOrRate

label kokiri_poems_oldPoems_shadowman:
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
    jump kokiri_poems_askOrRate

label kokiri_poems_oldPoems_lights:
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
    jump kokiri_poems_askOrRate


label kokiri_poems_oldPoems_bang:
    $ persistent.kokiri_poem_bang_knowledge = True
    $ conversationtracker_poem_bang = True
    $ kokiri_poem_bang_recent = True
    l "A bang, to keep me awake"
    l "A mix of rust and salt on my tongue"
    l "Deep cut my broken dreams"
    l "in the skin of an idiot"
    l "It still rings in my ears"
    l "The reality is breaking"
    l "I still can not understand it"
    l "A lie and still the truth"
    l "Time seems to stand still"
    l "And yet I do not get any younger"
    l "But also not smarter"
    l "Just more of myself and then less"
    l "Because everything finally falls down,"
    l "The leaves of a proud tree,"
    l "The feathers of lost birds,"
    l "My life."
    l "It is the law of gravity"
    l "Who laughs with us,"
    l "Who raised us."
    l "The really much too heavy force."
    l "Who slowly slaughter us,"
    l "Who slowly laughs at us,"
    l "Who is waiting for us."
    l "Constantly day and night"
    l "We push our whole life against a gigantic boulder on our hill and when we are at the top it slowly rolls to the other side."
    l "I try to be smarter, different than they are."
    l "But that makes me exactly like them. My other me blames me every day"
    l "How I was the match, the fire and the ashes."
    l "I cry for help but they do not hear it,"
    l "I cry for help but you do not hear it,"
    l "I cry for help but I do not hear it."
    l "Falling stars fall to the ground, I bathe in the light and yet I drown in the inkblack"
    l "Hopping for air, hoping for a sign I sink deeper and deeper and more and more unclear until nothing is left of me."
    l "Dead hands pull me with them,"
    l "Living hands push me even further"
    l "Stuck in this night-filled  realm"
    l "With all the shadows"
    l "But in the darkness of our thoughts"
    l "It looked like I could  see light"
    l "It was the moon that made all this nothing something."
    l "It was the world that made this new something nothing."
    l "It was me who closed my eyes."
    jump kokiri_poems_askOrRate
label kokiri_poems_recentPoems:
    "Filler"
    #TODO: Fill this in with more recent poems from the quest version. (No new poems in there, I need to add them.)
label kokiri_poems_askOrRate:
    menu:
        "*Rate the poem*" if not kokiri_poems_rateblock:
            if kokiri_poems_rated_once == True:
                $ kokiri_poems_rateblock = True
                n "Just rating her poems without giving more input is probably not the best idea.
                Try asking her something about the poem."
                jump kokiri_poems_askOrRate
            else:
                $ kokiri_poems_rated_once = True
                menu:
                    "That was very good, I liked it a lot!":
                        if kokiri_poem_bang_recent == True:
                            l "Oh, thank you very much! "
                            l "Personally I don't find the poem very good but it does show some potential.
                            I'm really flattered you like it though!
                            To me those poems will always be remnants of my times as an inexperienced writer and poet but I'm flatteredl!
                            I haven't written a lot of new poems lately, the few I have are a whole lot longer and kind of hard to get since they reference a lot of Greek and Roman mythology.
                            If you like to I could also show you them but just be warned that they are a lot less accessible than my poems from back in the day."
                        else:
                            l "Oh really? Thank you [persistent.name]!
                            To me those poems will always be remnants of my times as an inexperienced writer and poet but I'm flatteredl!

                            I haven't written a lot of new poems lately, the few I have are a whole lot longer and kind of hard to get since they reference a lot of Greek and Roman mythology.
                            If you like to I could also show you them but just be warned that they are a lot less accessible than my poems from back in the day."
                        $ persistent.kokiri_newerPoems_knowledge = True #This enables you to read some of the more recent poems.

                    "That poem was pretty good, it definetly has a lot of potential.":
                        if kokiri_poem_bang_recent == True:
                            l "Thanks [persistent.name]! I think this one definetly has potential so I'm happy to hear that you think the same thing.
                            Usually I don't think  my stuff is that great so if even I can see my own work's potential then you know it is one of my favourites."
                            l "That was actually one of the first poems I \"seriously\" wrote. With that I mean it was one of the first poems I wrote to be read by others."
                            l "I actually wrote it for a sort of poem competition when I was still in high-school."
                            l "If you liked this one it's quality is kind of hard to top with my older poems."
                            l "To tell you the truth sometimes it feels as if I reached the peak of my ability with that poem. Like i'll never be able to achieve something like it ever again."
                            l "I do have some more recent poems than the one I showed you that i think get close though, they are really the same at all but I think that is what makes them stand out."
                            l "But be warned though, they are a lot less accesible because they contain quite a few references to Greek and Roman mythology and they, like usual, are kind of long."
                            l "At the very least, if you liked this poem I think they might be an interesting read for you."
                            $ persistent.kokiri_newerPoems_knowledge = True 

                        else:
                            l "Oh really? Thank you [persistent.name]!"
                            l "I don't really think it's that good, after all I wrote it in a time where I was less experienced in writing. Although I'm glad you think they have potential!"
                            l "Maybe you would also like to read some of my newer poems if you liked some of my old stuff."
                            l "I don't have a lot of new ones, the few I have are mostly a whole lot longer and kind of hard to get since they reference a lot of Greek and Roman mythology."
                            l "So that unfortunately means that they are probably less accessible than my old poems, but if you want to check them out I'd be honored!"
                        $ persistent.kokiri_newerPoems_knowledge = True #This enables you to read some of the more recent poems.
                    "That was really bad.":
                        $ kokiri_poemBad = True
                        l "Oh... well, I appreciate your honesty."
                        l "Although you could have been a little less harsh about it."
                        l "I know not all of my poems are great, especially the older ones. Writing is all about growth, and I was still figuring out my voice."
                        l "It’s funny though. Those ‘bad’ poems are still a part of me, like little snapshots of my past."
                        l "In a way it's like looking at a younger version of myself."
                        l "But I guess not everyone will like them, and that’s okay."


        "*Ask something about the poem*":
            menu:
                "There seems to be a connection between some of your poems. In one you close your eyes, in the other the shadows hope to open their eyes. Was that intentional?" if persistent.kokiri_poem_bang_knowledge and persistent.kokiri_poem_window_knowledge:
                    jump kokiri_poemConnections
                "Is the poem about you?":
                    #TODO: Fill in. This question fits for pretty much every poem. Make something up for most old ones.
                    if kokiri_poem_window_recent == True:
                            l "Well yes, or it used to be about me anyway."
                            l "Most of these poems are quite old so they don't really apply to the person I am anymore."
                            l "They are now just a part of my past that I sometimes like to look back on."
                            l "Even if it sometimes hurts it's very interesting to get a glimpse into how I used to be."
                            l "It's almost like a sort of archive of my mindset at a very specific moment in time."
                            menu: 
                                "So did you wake up?":
                                    n "[persistent.date] gives you a big smile and for a moment you could swear you saw something sparkle in her eyes."
                                    l "I guess I did."
                                    l "It's funny, because at that moment you are not really focussed on the shift in what you are feeling."
                                    l "It sort of just... happens I suppose."
                                    l "Sometimes it still feels as if I'm asleep, the feeling keeps haunting me."
                                    l "But I've grown able to identify it better, so if I know the feeling has returned once again I'm able to better shield myself from it."
                                    l "This life, even through all it's flaws, is still mine."
                                    l "So I have to make sure it gets lived."
                                    l "Which I guess is slightly ironic considering I keep dying over and over."

                                "What moment of your life does this poem capture?":
                                    l "Most of these poems were made around the time [persistent.date_ghost]... passed away."
                                    l "Since I couldn't hold a camera without it falling on the ground I needed another outlet for my feelings."
                                    l "At that time I still used to play the trombone but that wasn't really enough for me, I needed another outlet."
                                    l "That's when I really started trying to make poems, before I used to make some smaller and sillier ones."
                                    l "Sometimes I still like to make a poem but as of late I kind of have no idea what I should write about."
                                    l "Most of my best poems were made when I was kind of in a bad mindset."
                                    l "But now that I'm doing pretty okay-ish in my life I can't write much more poems."
                                    l "And the few things that do bother me have been so overdone as subjects of my poems that it feels wrong to write about them again."

                "There seems to be a connection between some of your poems. In one you seem to be locked inside and in the other you are locked outside. Was this intentional?" if persistent.kokiri_poem_lights_knowledge and persistent.kokiri_poem_snowwoman_knowledge:
                    jump kokiri_poemConnections

label kokiri_poemConnections:
        l "I am honestly not entirely sure."
        l "I definetly see where you are coming from but I think that most similarities are actually a coincidence."
        l  "I do really like to make some of my poems cyclical or make them reference eachother."
        l "But the poems where I really started to do that actually were a lot more recent."
        l  "Due to me referencing my past poems in them they are pretty inacessible for readers."
        l "It doesn't help that most of them use quite a few references to mythology."
        $ persistent.kokiri_newerPoems_knowledge = True
        menu:
            "*Talk about something else*":
                jump kokiri_talkAboutSomethingElse
            "That is very interesting! Would it be okay for me to read another one of your poems?":
                l "Oh wow, you must really like them, I'm flattered honestly. Sure, go ahead."
                jump kokiri_poems_oldPoems
            "I would really like to read one of those new poems if that is okay.":
                l "Sure thing, I would love to show you them!"
                jump kokiri_poems_recentPoems
            

label kokiri_scenery_allOver:
    l "We did it, I can't believe it!"
    l "We actually cheated death, [persistent.name]."
    l "Does that mean that this is an ending right now?"
    menu:
        "I don't think so, however this might be the lead-up to an ending.":
            l "I see... in that case, let's make the most of our wait by doing some stargazing."
            n "You lay down to watch the stars with Lilith, she places her head on your lap and lays down aswell."
            n "For a while all you can hear is just the sound of the trees slowly letting their branches dance in the wind."
            n "Until Lilith breaks the silence."
            l "That... That was quite the show back there wasn't it?"
            l "You've been through all that to have a succesful date with me?"
            l "You are really dedicated, I'll give you that!"
            l "I don't know how I'll ever be able to thank you enough [persistent.name]."
            l "It feels weird, a day ago I didn't even know about the loop and now I am already free of it."
            l "But to you this took many, many days to even get to this point."
            n "She grows quiet in contemplation once more. The two of you gaze up at the stars a little longer in pure silence."
            n "They are absolutely marvelous, after a while of just enjoying this precious moment you catch a glimpse of a falling star."
            l "Oh, did you see that falling star? Let's make a wish!"
            n "[persistent.date] closes her eyes, a soft smile appears on her face."
            n "A moment later she looks at you again, she places her hand on yours."
            l "What did you wish for?"
            menu:
                "I didn't make a wish, everything I could ever need is right here, in this moment here with you.":
                    n "[persistent.date] chuckles and looks you in your eyes."
                    l "Wow, you sure know what to say don't you?"
                    l "If I'm being honest I'm also really enjoying this moment, it feels like I could sit here for an century and still be as happy as I am right now."
                    jump kokiri_death_1

                "I can't tell you my wish right? Isn't that how falling star wishes work?":
                    n "[persistent.date] shakes her head and begins to stare into your eyes."
                    l "Oh, I'm sorry! I completely forgot about that rule for a moment."
                    l "Keep your secrets then magic-[persistent.name]."
                    n "She giggles."
                    jump kokiri_death_1

                "I wished that...":
                    l "Wait! Don't tell me your wish or it wouldn't turn true!"
                    n "[persistent.date] begins looking into your eyes."
                    l "I'm sorry, I completely forgot about that rule for a moment."
                    jump kokiri_death_1

        #There's also a kokiri_death_1 prevented link here but that's probably quite useless.




label kokiri_death_4_noDeath:
    l "I see, so we have already had this conversation before?"
    l "I showed you the picture and I got killed again..."
    l "And then we also stayed here before, and that was safer."
    n "You see [persistent.date] think deeply for a second."
    l "Although I guess you didn't say that it was truly safe, did you?"
    l "Just safer. I guess that makes sense, because otherwise you wouldn't have come back, would you?"
    if conversationtracker_gamegoal == True:
        l "Once I somehow survived all of this, your goal would be completed."
        if kokiri_goalSurvive == True:
            l "And that would mean you would stop playing the game at that point like you said before, right?"
        elif kokiri_goalSurvive_cannotStop == True:
            l "Although you said you would want to keep playing this game even beyond that point, right?"
            l "I just wonder, what would you do if the game ended right at the moment I survived everything?"
            menu:
                "I think I would have to have peace with that. There is nothing I can change about that, right?":
                    label kokiri_death_4_noDeath_peaceWithEnd:
                        n "Lilith lets out a small sigh of relief that is just big enough for you to barely pick up on."
                        l "I think you are right."
                        l "Sometimes things just end. And usually it is better to let them."
                        l "Especially if not letting them end isn't in our control."
                        if love_meter > 2:
                            l "For what it is worth, when that time comes, I want you to know one thing."
                            l "I really appreciate everything you did for me [persistent.name]."
                            l "And wheter or not you really found a way for me to live, I want to say that you made me feel alive for one of the first times in a long while."
                            l "I cannot speak for the other past versions of me but just know that I really am enjoying our time together even if it is in less than ideal circumstances."
                            l "And I hope that you enoyed your time here with me aswell, with all my past versions too."
                            l "When everything ends, I hope you'll remember me in a postive way, or atleast that you will have some positive memories of me."
                            l "Then you can keep a little piece of me wherever you go."
                            l "I certainly will keep a small piece of you with me wherever I go after the game ends [persistent.name]."
                            n "She takes a deep breath."
                            l "Can you promise me you will remember these words when the game ends?"
                            menu:
                                "I promise. Thank you very much Lilith.":
                                    n "She gives you a tight embrace."
                                    l "Very good. And thank {b}you{/b}."




                "I would replay the game once again.":
                    label kokiri_death_4_noDeath_replayGame:
                        l "See, that kind of worries me [persistent.name]."
                        l "I know that this game is a loop, but at that point you'd just be doing the exact same thing with little to no deviation."
                        l "You would just go through the route that keeps me alive."
                        l "What would you do when you then inevitably reach the ending where I survive once more?"
                        menu:
                            "I'd keep going through it until I feel like it is enough.":
                                l "But will it ever feel like it is enough [persistent.name]?"
                                l "If you would keep coming back, replaying the good ending over and over, wouldn't it lose it's charm quickly?"
                                l "I worry that's just not going to be sustainable at all."
                                l "At one point you will have to learn to let go [peristent.name]."

                            "I'd play through the entire game again, not just that one route.":
                                l "..."
                                l "But that means going through all my deaths again aswell, doesn't it?"
                                l "Do you really want to let me die multiple times once again because you can't let go of me?"
                                l "Please [persistent.name]. If you really care for me at all then you have to let me go."
                                l "I can't go through this forever."
                                l "Even if I can't remember it, I don't want to go through this any more than I have to."

                "I would create my own continuation in a medium of my choice. The story would just continue, the storyteller would just change.":
                    label kokiri_death_4_noDeath_continueOwnStory:
                        "Filler"
            

    else:
        l "There would be no need for replaying the same part over and over, trying to save me."
        l "As we could just enjoy our time together fully from then on. We would be able to have a second date, not like these tens of first dates you must've had with me already." #TODO: If you tell her how many dates you've been on have her refereence that number instead.
        l "Although I do wonder, what would you do if the game would end right after I survived all of this?"
        menu:
            "I think I would have to have peace with that. There is nothing I can change about that, right?":
                    jump kokiri_death_4_noDeath_peaceWithEnd

            "I would replay the game once again.":
                    jump kokiri_death_4_noDeath_replayGame

            "I would create my own continuation in a medium of my choice. The story would just continue, the storyteller would just change.":
                    jump kokiri_death_4_noDeath_continueOwnStory

    jump kokiri_death_4_hill


label kokiri_death_3_prevented_talk_farthestWeHaveGone:
    l "Oh, really? So this is the first time you are having this exact conversation with me?"
    l "Well let's see what's in store for us then."
    l "Let's just hope that it leads to me not dying anytime soon. I'd prefer if I could die of old age."
    n "[persistent.date] giggles."
    n "She grows quiet for a moment, seemingly lost in thought."
    l "Is it just me or is the knowledge that this is the first time I share this very moment with you making it only more special?"
    menu:
        "It is.":
            n "[persistent.date] laughs slightly."
            l "I knew you would agree [persistent.name], I can imagine you might even be more excited than me to experience a new moment."
            l "Repeatedly doing all of this over and over again, it might make it lose it's charm for you, doesn't it?"
            n "She gives you a knowing smile."
            menu:
                "You're right. Sometimes it can feel repetitive.":
                    l "Yeah, I thought so. It must be exhausting, going through the same events, the same words..."
                    l "But hey, at least this moment is new, right? This one feels... unique."
                    l "I think we can treasure it, just like we do with any first."
                    l "And maybe, with enough 'new' moments like this, you'll be able to break the cycle. Who knows?"
                    jump kokiri_death_4_hill
                "Actually, it’s still very nice, even if I've experienced it multiple times.":
                    l "Really? That’s actually really sweet to hear."
                    l "I guess every time feels just a little bit different when you're doing it with someone who matters, huh?"
                    n "Lilith’s expression softens."
                    l "Even though things repeat, you’re the one constant trying to change things. I think that's what makes every moment we share precious."
                    jump kokiri_death_4_hill
        "Every moment we share is beautiful to me." if kokiri_cherishAllDates == False: 
            jump kokiri_death_3_prevented_talk_EveryMomentIsBeautiful
            label kokiri_death_3_prevented_talk_EveryMomentIsBeautiful:
                if love_meter >= 2:
                    n "[persistent.date] grows beetred."
                    l "{size=*0.5}Uhm... uh... say something [persistent.date_nickname], anything.{/size}"
                    l "Sorry for that right now [persistent.name], that was just incredibly sweet of you to say."
                    l "I don't know what to say to that right now."
                    if kokiri_cherishAllDates == True:
                        l "Except that I think hearing those words might have healed something deep inside of me."
                        $ love_points += 1
                        $ love_meter_update(True)
                    menu:
                        "It's alright, take your time to think and in the meantime we can just lay here some more.":
                            l "I... I would like that very much."
                            n "She gives you a soft, cute smile."
                            n "The two of you remain in peaceful silence for a while, the air filled with a quiet intimacy."
                            n "[persistent.date] seems content, resting beside you without the need for words."
                            n "You can't help but smile as you feel her warmth wrap itself around you."
                            n "For a frozen second, for an eternity you feel like the luckiest person alive."
                            n "Sadly that eternity only lasts for a moment, a fleeting second."
                           
                            jump kokiri_death_4_hill
                        "Don't worry about it, I think it's incredibly cute how flustered you got.":
                            l "Are you trying to make me explode by blushing so much or something [persistent.name]?"
                            n "[persistent.date] chuckles as she covers her face."
                            n "After a short moment she sighs and lets go of her face, at this point her cheeks seem to have somehow become even more red."
                            l "There's no stopping it at this point, if I really will explode then my blood will be on your hands [persistent.name]!"
                            n "You shudder slightly, [persistent.date] gets up from your lap, seemingly having felt your shudder."
                            l "Oh no, that wasn't really a good choice of words in this situation was it?"
                            l "I’m really sorry. I meant it as a joke, not as... well, you know."
                            if love_meter >= 2:
                                n "Lilith’s smile falters slightly, but she quickly recovers it, or well, attempts to recover it."
                            else: 
                                n "Lilith's smile fades away."
                            
                            if kokiri_toldLillySheLives == False:
                                l "You will never be responsible for my deaths [persistent.name], you're just trying to get me out of this whole mess alive, aren't you?"
                                l "And I think the fact that we are now here shows just how good you are at this whole thing."
                                l "So who's to say what you'll accomplish next? Either way, just know that I believe in you."
                            else: 
                                if love_meter >= 2:
                                    l "You are just trying your best to give us the best possible ending, aren't you?"
                                    l "Though I really wish you could see that this is already the best ending for me personally."
                                    l "I wish you didn't feel like you needed to go through all of this for me."
                                else:
                                    n "It is quiet, uncomfortably so."
                                    n "You find yourself listening around for even the faintest sound that could break this silence."
                                    n "You don't hear a thing, it is as if the forest itself and everything in it is holding it's breath trying to not make even the slightest bit of noise."
                            jump kokiri_death_4_hill
                else: 
                    l "Is it [persistent.name]?"
                    l "Is it really?"
                    l "I'm afraid I don't get you at all."
                    l "One moment you treat me pretty badly and then the next one you say something like this."
                    l "I'm not sure how to feel about you to be honest."
                    l "I just wish you also would be honest with either me or yourself and not send me these conflicting signals."
                    l "Then it would be easier to either hate or like you."
                    l "You leave me no other choice, I'm out of here. I deserve someone who's words I do not have to constantly doubt."
                    $ noTalkAngryLilith = True
                    jump angryLilith
        "It's like I said before Lilith, I cherish all our dates. I doubt that this could ever truly lose it's charm." if kokiri_cherishAllDates == True:
            jump kokiri_death_3_prevented_talk_EveryMomentIsBeautiful

label kokiri_death_3_death_dialogue:
    if kokiri_call == True:
        n "[persistent.date] hangs up and for a moment the two of you sit in pure silence."
        n "The sharp tunes of the wind break the silence, as if to remind the both of you of the limited time you still have left."
        l "So after that call I am still going to die, right?"
        l "Forgive me if I am slightly nihilistic but what was the point of that?"
        l "After you retry everything of this is going to be undone and she won't even remember that I called her." 
        if kokiri_chatchar_abigail_called == True:
            l "I really love that I still managed to help my sister in my last moments but if everything gets reset inevitably doesn't that make all of this pointless?"
        else: 
            l "I really love that I still managed to help my mom in my last moments but if everything gets reset inevitably doesn't that make all of this pointless?"
    else:
        l "So after all those things that just happened I am still going to die?"
    menu:

        "Well, it is better to die with a clear conscience and slightly less doubts. So that call was anything but pointless." if kokiri_call:
            jump kokiri_death_dialogue_stillDying

        "Unfortunately, yes." if not kokiri_call:
            jump kokiri_death_dialogue_stillDying

        "Yes, but the world keeps going. It doesn't truly reset. So it makes it easier for her to come to terms with everything." if persistent_jamestalk_justgame_knowledge:
            l "..."
            l "It doesn't reset?..."
            l "So that means each time I-"
            l "Oh god..."
            l "That means that my family has to deal with my death each time, that I stay dead for them."
            l "That's just horrible..."
            l "I suppose you are right, if it does help my family come to terms with my death this was worth doing."
            l "Though it is strange isn't it? Normally you wouldn't be able to do something like that."
            l "Without you I also wouldn't be able to do it."
            n "Lilith chuckles uncomfortably."
            l "Although I have to say, if there is anyone who hasn't yet fully come to terms with my death it might be me."
            n "It might also be you, given that you keep trying to prevent her death."
            l "It's just... so unreal."
            l "It is lurking around every corner, getting closer and closer with every passing second. And yet it seems so far away."
            l "If I am being honest, a part of me still thinks- hopes that all of this is just an elaborate prank."
            if kokiri_groundhog_lie or kokiri_psychich_lie:
                l "But it isn't, is it?"
                l "I seemingly can pick up when you are lying and when you aren't."
                l "But when you told me about me being inside of a game that kills me over and over, you were telling the truth, weren't you?"
                n "She shudders."
                l "That realisation is even more scary than the thought that you were lying about that for some reason."
            else: 
                l "But it can't be, right?"
                l "You know things I have never told anyone."
                l "This has to be real."
                l "And that thought is terrifying."
                l "Because that means that it is true that I keep dying over and over."
                l "And that means it is also true that I'm probably going to die soon."
            jump kokiri_stillDying_scared

            

label kokiri_death_dialogue_stillDying:
    if kokiri_call == True:
        l "I suppose that's true [persistent.name]. Thank you for making me realise that, it helps a little.
        Very little..."
        l "But I can use all the comfort I can get now to be honest."
    else:
        l "When you told me your story just a bit ago it all seemed so far away but now it all feels so much closer."

    label kokiri_stillDying_scared:
        l "To tell you the truth, I'm feeling really scared. I don't want to die just yet."
        n "[persistent.date] shudders and looks at you with pleading eyes as if she's waiting for an anwer that will comfort her.
        Well, comfort her as much as a person who knows they are going to die any moment from now can be comforted."
        l "I suppose this is how Damocles felt aswell."
        l "And yet he had the choice to just walk away from the sword dangling above his head, I don't think I'll have that choice."
        l "I'd just die another way. It's probably better to just watch this spectacle with you even if it is my last moment but that doesn't mean I'm not terrified."
        menu:
            "It's okay, grab my hand. We're going to do this together.":
                n "[persistent.date] grabs your hand and squeezes it as if she's not going to let it go anytime soon."
                n "A shy smile appears on her face."
                l "Thank you [persistent.name], please don't let me go."
                n "She gives you a hug with one arm, as the other's hand is busy clamping yours. The hug lingers on for quite a while, not that you are complaining though." 
                n "In fact, you want her to never let you go again."
                n "You want to never let her go again, since you've seen what happens if you do."
                $ kokiri_holdhand = True
                menu:
                    "I am doing all of this to make sure I won't ever need to let you go.":
                        l "I... I was talking about not letting my hand go."
                        l "But from the way you said that... I get the feeling you are talking about something else entirely, aren't you?"
                        l "Don't get me wrong, I am thankful for you taking saving me so serious, but isn't this all a bit too much?"
                        l "Not that I don't appreciate your effort but when will all of this end [persistent.name]? If it even will end at all."
                        l "How many times have you gone through the motions now?"
                        menu:
                            "I have done so [persistent.retry_counter] times.":
                                if persistent.retry_counter > 16:
                                    if persistent.retry_counter < 50:
                                        l "Are you going to make the breakthrough after 50 times, maybe 100?"
                                    elif persistent.retry_counter < 100:
                                        l "Are you going to make the breakthrough after 100 extra attempts?"
                                    
                                    if persistent.retry_counter < 1000:
                                        l "Or maybe, just maybe, the dev will just give you the good ending after 1000 times?"
                                    else:
                                        l "Is it going to take a thousand more of my deaths?... This is too much [persistent.name]."
                                    
                                    l "Exactly how much of my lives and deaths is THE good ending worth to you?"

                                    if persistent.retry_counter < 50:
                                        l "While I do understand that it can be hard to let go, you might need to let me go eventually."
                                        l "After all, this game is only so big, isn't it?"
                                        l "What if you've explored every branch and you still can't save me?"
                                        l "What if this game never wanted you to save me?"
                                        l "With all these different attempts... I'm beginning to get my doubts honestly."
                                        l "I think we might both need to accept what's going to happen."
                                    else:
                                        l "Look [persistent.name], like I already said, I really appreciate you attempting to continuously save me."
                                        l "But, aren't you also beginning to get doubts after so many attempts?"
                                        l "Either I'm really destined to die over and over and..."
                                        n "[persistent.date] grows quiet for a moment."
                                        l "Or we are missing the point of all of this."
                                        l "But you can't keep doing this forever."
                                        l "Or well, you very much can, but I'm asking you not to."

                                        if love_meter > 2:
                                            l "I know that you can do whatever you want at the end of the day, but I'm counting on the fact that you are willing to hear me out on this."
                                            l "It's not easy, but together we can move on to something better."
                                        else:
                                            l "I know it's almost ridiculous of me to ask but I'm trying to get through to you somehow."
                                            l "I'm not sure when you started treating me pretty bad."
                                            l "Whether it was from the very first attempt or if you slowly grew more resentful or bored and wanted to take it out on me."
                                            l "But this can't be fun for you, right?"
                                            l "Just constantly having to sit through the same dialogue over and over, bashing your head against the wall each time."
                                            l "Why are you still doing this [persistent.name]?"

                                    menu:
                                        "But you are not real, this is just a game...":
                                            l "Well, I feel pretty real to me and I can imagine every death I go through must feel equally real and very painful."
                                            l "So what if I'm in a game? Does that make me less real?"
                                            l "You can talk with me, I can speak, and I'm real enough to trick myself into thinking that I'm real."
                                            l "And I'm real enough to walk away from some monster who thinks they are justified in killing me over and over again just to get what they want."
                                            $ love_meter -= 2
                                            $ angryLilith = True
                                            $ noTalkAngryLilith = True
                                            $ love_meter_updater(True)

                                        "I don't want to harm you but I have to find it.":
                                            n "She sighs."
                                            l "For who do you have to find it?"
                                            l "For us, for me... or for yourself?"
                                            menu:
                                                "For myself of course!":
                                                    $ persistent.kokiri_reachEndingForMe = True
                                                    $ persistent.kokiri_reachEndingRecent = "me"
                                                    l "Oh I see..."
                                                    l "So you don't want it because you crave an impossibly good ending for us like I thought and feared?"
                                                    l "It's even worse than I thought..."
                                                    l "You're just needlessly throwing my lives away to see if there is anything that can satisfy your unrelenting need for greater things."
                                                    l "Let me tell you something [persistent.name], whatever you find, it won't be enough."
                                                    l "Although I suppose you already know that deep down."
                                                    l "That feeling of chasing something impossible—you’ve already grown quite familiar with that, right?"
                                                    l "Let me tell you something else you already know."
                                                    l "I won't remember this conversation next time—but you will. That's my curse to you."
                                                    l "I'm not sure if it'll have much effect on someone so selfish..."
                                                    l "But if you ever played this game to try to save me, not for you and I to be together but just to save me, then it might be worth a shot."
                                                    l "I'm really hoping you might learn a lesson from this."
                                                    l "Goodbye [persistent.name], until we inevitably meet again."
                                                    $ love_meter -= 2
                                                    $ angryLilith = True
                                                    $ noTalkAngryLilith = True
                                                    $ love_meter_updater(True)

                                                "For us of course, silly.":
                                                    $ persistent.kokiri_reachEndingForUs = True
                                                    $ persistent.kokiri_reachEndingRecent = "us"
                                                    l "Oh [persistent.name]... can't we just make our own good ending?"
                                                    l "What's stopping us from becoming our own storytellers?"
                                                    l "None of this is real, right?"
                                                    l "Doesn't that mean we don’t have to accept what will happen?"
                                                    l "Our own perfect little story is just as real as anything in here."
                                                    l "Please don't drive yourself mad searching for something that may not exist."
                                                    l "I want the moments we share to be enjoyable for both of us."
                                                    l "This moment right now—however unconventional—is perfect. Even when I think about what’s to come."
                                                    jump kokiri_death_4_hill

                                                "For you of course, it was always for you.":
                                                    $ persistent.kokiri_reachEndingForYou = True
                                                    $ persistent.kokiri_reachEndingRecent = "her"
                                                    l "Can't you see [persistent.name]? This is my good ending."
                                                    l "I get to spend time with you, right here and now—that's all I need."
                                                    l "If we just trick ourselves into not seeing how the game pushes us… then this night was very nice, wasn’t it?"
                                                    l "If only time could freeze, so we could share this moment forever."
                                                    l "Is this not a good enough good ending for you?"
                                                    l "Try to enjoy it. Try to have some fun. Do it for me, [persistent.name]. For us."
                                                    l "Live every one of these days with me as if it’s your last—because for me, it is."
                                                    jump kokiri_death_4_hill

                                        "You're right, I won't search for it anymore. I promise.":
                                            l "Thank you [persistent.name], I appreciate it more than I could probably show..."
                                            l "Because you could just retry and retry without me knowing whether you promised to stop or not—that is what gives your promise power."
                                            l "And in my trust in you lies a different power."
                                            l "Let’s hope our combined power is enough to get through this."
                                            n "[persistent.date] appears to be lost in thought."
                                            l "You know, I'm wondering something. That good ending you were trying to find—do you think it truly exists?"

                                            menu:
                                                "It doesn't matter anymore.":
                                                    l "I suppose you're right..."
                                                    l "But wouldn’t it give you closure to know whether it exists or not?"
                                                    l "Then again, what if there truly was one..."
                                                    l "Forget I mentioned it, please!"
                                                    jump kokiri_semiEnding

                                                "I do.":
                                                    l "That just gives me more questions."
                                                    l "If you know the good ending exists, then why are you still searching?"
                                                    menu:
                                                        "I read about the good ending somewhere online...":
                                                            l "Ah, so others found it too?"
                                                            l "But then—why read about it again here?"
                                                            l "Isn’t reading it online the same as experiencing it?"
                                                            menu:
                                                                "Yes, but that would mean I didn’t achieve it myself.":
                                                                    l "I see..."
                                                                    l "So you risked my life for your own sense of achievement?"
                                                                    l "I should be angry... but I want things to end on a good note."
                                                                    l "Let’s make the most of this moment."

                                                                "I suppose it is. In that case—we’ve reached the good ending!":
                                                                    l "Honestly, to me this is the good ending."
                                                                    l "We’re breaking the death loop together, enjoying the view."
                                                                    l "What could be better?"
                                                                    l "...What does that ending you read look like?"
                                                                    $ renpy.input("...")
                                                                    n "She sighs contentedly, shifting slightly on your lap."
                                                                    l "Wow... that sounds beautiful. Almost makes all the suffering worth it."
                                                                    l "Almost."
                                                                    l "At least now we don’t have to keep fighting for it."
                                                                    l "Let’s just enjoy this ending—at least for now."
                                                                    jump kokiri_semiEnding

                                                "I don't.":
                                                    l "Then why chase it?"
                                                    menu:
                                                        "What if it did exist? Even with doubts, I had to be sure.":
                                                            l "That makes some sense... but what a painful journey."
                                                            l "You sacrificed time and my life for something that might not be real."
                                                            l "I'm glad you're listening now. Thank you, [persistent.name]."
                                                            n "Or did you just want to see this dialog instead of believing it?"
                                                            n "Only time will tell."
                                                            l "[persistent.date] grows silent."
                                                            jump kokiri_semiEnding

                                                "I'm not sure. I don't even know what it would look like.":
                                                    l "That’s actually a great question."
                                                    if not kokiri_toldLillySheLives:
                                                        l "I’d probably survive in it, right?"
                                                        l "Maybe we’d be together safely… or maybe I’d still die, and you'd learn about acceptance."
                                                    else:
                                                        l "If I already survive in some endings but we’re not together—maybe a true ending is one where we are?"
                                                        if love_meter > 1:
                                                            n "You could be mistaken, but for a moment, you thought you saw Lilith shudder."
                                                        else:
                                                            l "Though honestly, I really doubt that ending exists."
                                                    l "But maybe it doesn’t matter anymore."
                                                    l "We keep thinking about the unattainable instead of what’s here and now—"
                                                    l "Our last moment together."
                                                    jump kokiri_semiEnding

                                else:
                                    l "[persistent.retry_counter] times?"
                                    l "...That's quite a lot already."
                                    if love_meter > 2:
                                        l "Still, I trust you. I just hope you won't lose yourself in all of this."
                                        l "This can't be easy for you either, [persistent.name]."
                                    else:
                                        l "Maybe it would be better to just stop going through the motions at all? To not go to the next date with me."
                                    jump kokiri_death_4_hill

                    "Don't worry, I won't.":
                        n "Her smile grows even wider."
                        l "Thank you [persistent.name], that really helps comfort me a little."
                        l "Whatever happens next, we're facing it together."
                        l "Can we watch the stars some more?"
                        l "I'd like to have that be my last memory before..."
                        l "Well, I think you know what I mean, right?"
                        n "[persistent.date] and you lie down next to eachother, still holding eachother's hand as you gaze at the nightsky."
                        $ kokiriStarGazed = True
                        l "Thank you for being here with me [persistent.name], I'm not sure if I could brave something like this on my own."
                        l "The stars are even more beautiful now than ever before. Maybe it's because I know it will be the last time I ever get to look at them?"
                        l "Either way, I'm really glad that I get to share this moment with you."
                        jump kokiri_death_4_hill

            "Try to think of a happy memory.":
                l "Does it count if I'm just thinking of this exact moment?
                I think it might be nice to have it as my final thought when..."
                n "[persistent.date] shudders for a moment."
                l "Let's not think about that too much, just give me more to remember instead."
                n "She lays down and softly places her head on your lap."
                
                if kokiriStarGazed == True:
                    l "I know we already watched the stars before, but they are so beautiful, aren't they?"
                    l "The other time it kind of felt like I was seeing them for the first time all over again."
                else:
                    l "The stars are all so beautiful right now, it's like I'm seeing them for the first time all over again." 
                    $ kokiriStarGazed = True
                menu:
                    "Maybe this is really your first time watching them?":
                        l "I'm not sure I understand, what do you mean with that [persistent.name]?"
                        menu:
                            "Well, since you are in a game you might have simulated memories. That would mean you only think you saw the stars before because it was programmed into you and so this might be the first time you truly watched the stars.":
                                l "Hmm, I suppose that might be the case but haven't you been here before when you were playing the game?"
                                l "And if you have, doesn't that mean that I was with you and that I watched the stars aswell that time?"
                                menu:
                                    "I suppose you are right now that I think about it actually.":
                                        l "Well, for whatever it is worth, it still feels like the first time to me. Partially because I can't remember the previous time but I think even if I could it would always feel like that to me."
                                        l "It's special because I get to spend that time with you.  I hope that this moment won't get old for you aswell, that you will enjoy it as much as the first time we watched the stars together."
                                        jump kokiri_death_4_hill
                                    "Well that's true, but that was not the same you as you are now. ":
                                        jump kokiri_notTheSameYou
                                    "This is actually the first time I've watched the stars with any version of you." if not persistent.kokiriWatchedStars:
                                        jump kokiri_death_3_prevented_talk_farthestWeHaveGone
                                    "This is actually the first time I've watched the stars with any version of you. (Lie)" if persistent.kokiriWatchedStars:
                                        jump kokiri_death_3_prevented_talk_farthestWeHaveGone
                    "I would love to truly watch them with you but I can't actually see them.":
                        l "I see, it's not really the same feeling you get watching them through a screen than in real life, is it?"
                        n "You shake your head slightly."
                        l "Alright then, I'll try my best to immerse you slightly more."
                        l "The stars shine like silver lights in the inkblack sky, they seem to form patterns if you look closely enough."
                        l "You can see a pan with a bent handle, a bathtub, a playful dog and a snake."
                        l "Am I doing a good job narrating?"
                        n "You give her a thumbs up and she gives you a smile in return."
                        l "Alright, I'll narrate some more then, this is pretty fun!"
                        l "You can see a few falling stars, their tails of light are a visible trace of the projection from the past that uses the star itself in the present to project itself to the future, to beyond the place the star currently resides in."
                        l "This constant and neverending process is happening multiple times every single second. Your head hurts trying to think of it too much so you just try to enjoy the falling stars for their beauty."
                        l "As you are doing so you begin to think of this projection method once again. Isn't the future itself just a projection of the past memories using the present as a projection point?"
                        l "Are we doomed to always make the same choices because our past steers us towards our future wich inevitably becomes our past that steers us even more?"
                        l "Or are we more like billiard balls being pushed by our past in a predictable direction until we collide with other billiard balls that push us in a different direction?"
                        l "If we are like the billiard balls, can it be predicted wich ones will push us where? Or is the number of balls so incomprehensible that it brings a form of chaos with it?"
                        n "You try to calm [persistent.date] down a little by softly placing your hand on hers."
                        l "Whoops, I think I might have went a little too far into my narration role there for a moment. "
                        n "As one narrator to another, I think it happens to the best of us. It's hard to keep a story on tracks sometimes."
                        n "But technically, that was still part of the story, and it was beautiful."
                        l "It's just some stuff I've been wondering for a while, maybe even more so now that I know I live in a simulated world."
                        l "What do you think about what I just said [persistent.name]?"
                        l "Is our future predictable, even just in theory?"
                        $ persistent.kokiri_determinism_knowledge = True
                        jump kokiri_death_4_hill
                    "*Stay silent and watch the stars.*":
                        n "Honestly staying silent probably was the best call, I mean have you {b}seen{/b} some of the other options?"
                        n "It's probably not the best idea to constantly bring up something philosopical on your first date."
                        n "Well... for her it's the first date. For you it's becoming hard to keep track of how many first dates you had with her isn't it?"
                        n "I'll help you out, it's somewhere around the [persistent.lildeaths]th date for you."
                        n "But anyway, I just wanted to say that I'm proud of you for not saying too much, that is my job afterall."
                        n "Let me jump right back into the narration."
                        n "You're not sure how long you two have been staring at the stars, it might have been a minute or fifteen of them. All you're sure about is that you felt at peace for every second of it."
                        l "Thank you for making these memories with me [persistent.name] even if I won't remember them the next time, I'll remember them for as long as I possibly can."
                        l "I had a blast so far, even if the concept that I'm in a game still is a bit much to wrap my head around."
                        l "I was always so focused on [persistent.date_sis_nickname], mom, my work, pretty much anything else that isn't me, that I forgot how good it feels to take some time to just relax."
                        jump kokiri_death_4_hill

            "You need to go through this, it's the only way I might be able to save you.":
                l "I know [persistent.name], but are you sure I have to die here?"
                l "Can't you just ask me the same questions you need to ask me somewhere where I die a less painful death?"
                l "Or maybe even preferably ask me those questions over the phone so I don't have to die?"
                menu:
                    "This death is going to be pretty quick so it shouldn't be too painful." if persistent.kokiri_death_4_hill_holdHand:
                        l "Alright, I understand. But are you sure there is something more than this?"
                        l "Am I dying over and over again for a purpose?"
                        l "Or are you just doing this to speak to me once again no matter what it costs?"
                        l "I'm not blaming you if you are, I just want you to tell me the truth."
                        menu:
                            "No, it's nothing like that [persistent.date]! I really believe that there is still something more than this." if not persistent.beachroute_visited_knowledge:
                                jump kokiri_thereIsMore
                        
                            "No, it's nothing like that [persistent.date]! I really believe that there is still something more than this. There is another location I unlocked after this forest, the beach. I'm hoping there are more things I will be able to unlock." if persistent.beachroute_visited_knowledge:
                                jump kokiri_thereIsMore

                            "It's true, I tried pretty much everything I could but nothing worked. I just wanted to spend some extra time with you.":
                                l "We don't need to go through all of this, [persistent.name]. You know I'll always be with you as long as you can remember me, right?"
                                l "You've met me countless times right?"
                                n "For a second you consider telling her that you've met exactly [persistent.retry_counter] times but you just nod instead."
                                l "So that probably gives you a good grasp on how I am as a person, what I would do in certain situations, how I see the world. "
                                l "Could you not use that to see me again? Use those memories you have of me as a mini-me you can carry in your heart and who you can take with you wherever you want?"
                                l "Due to my nature I reckon the extra time you can spend with me now will soon lose it's charm once you have spent it. And what would happen then? What would happen once you've read all the things I can say?"
                                n "You ponder the question for a bit as you desperately try to divert your mind's focus from the topic, that seems to only have the opposite effect."
                                l "If you'd take me with you in your heart I think we could break the flaw in my nature and give ourselves as much extra time as we desire. As much dialogue as you can dream."
                                n "[persistent.date] gives you a cute little smile and blushes."
                                l "I like that idea. I really like it."
                                l "What do you think [persistent.name]?"
                                $ kokiri_death_4_playerResponse = True
                                jump kokiri_death_4_hill

                    "Actually we can't talk for too long on the phone. Otherwise a plane ends up crashing into your house and killing you." if persistent.plane_knowledge:
                        l "..."
                        l "What?"
                        l "A plane crashed into me?"
                        l "In my own home?"
                        l "These deaths are begining to sound more and more absurd."
                        l "And yet, after what I've seen with my own two eyes, I fully believe it."
                        l "I suppose in that case if we really want to break the cycle this is the best place to do so."
                        l "But can I be honest with you [persistent.name]?"
                        l "Even if this really is necessary that does not take away from how terifying it is."
                        l "Now that I have had some more time to really think it through this all feels so much more real."
                        l "I guess before even if what you were saying was the most logical answer something deep inside of me just didn't want to fully believe it."
                        l "But now it's getting harder and harder to do so."
                        l "Although I guess I prefer you telling me about it more than if you were just leaving me in the dark about my fate over and over again."
                        l "So thank you for that, at the very least now we can face it together. Neither of us has to brave this alone."
                        jump kokiri_death_4_hill


                    "I hadn't considered that actually, I will give it a shot if that is what you want. Thanks for the tip [persistent.date]!":
                        n "[persistent.date] gives you a cute smile."
                        l "Happy to help!"
                        l "Also happy to not have to die too painful I suppose."
                        n "She lets out a small chuckle, but make no mistake, it's an uncomfortable one."
                        $ kokiri_death_4_playerResponse = True
                        jump kokiri_death_4_hill


                    "I tried that already but I couldn't ask you those questions in other locations." if persistent.restaurantNoExtraDialogue:
                        n "[persistent.date] sighs."
                        l "Ah I see..."
                        l "But is this death at the very least not too painful?"
                        menu:
                            "I'm not sure how you would die, this is the furthest we have ever gotten." if not persistent.kokiri_death_4_hill_holdHand and not persistent.kokiri_death_4_hill and not persistent.kokiri_death_4_noHill:
                                jump kokiri_deathNotPainFul_unsure
                                
                            "I'm not sure honestly, I didn't experience it yet myself." if not persistent.kokiri_death_4_hill_holdHand:
                                jump kokiri_deathNotPainFul_unsure
                            "I have experienced it myself aswell and I can honestly say that it is over very quick, probably before you could feel pain. It shouldn't hurt." if persistent.kokiri_death_4_hill_holdHand:
                                l "Well, that's easy for you to say isn't it?"
                                l "Of course it doesn't hurt too much for you, you are probably playing this game from the comfort of your own home."
                                l "Or at the very least you don't really have to experience whatever fate awaits us."
                                l "Your character did, not you."
                                n "[persistent.date] grows quiet for a moment."
                                l "..."
                                l "Look [persistent.name], I'm sorry if I came of as a bit agitated just now. I didn't want to hurt you like that."
                                l "I guess this is a bit much for me? The feeling of death looming right above your head, it's messing with me."
                                l "But still, I shouldn't have said that, I shouldn't have taken my frustration out on you."
                                l "After all, you just wanted to comfort me, right?"
                                l "And though I am still terified it oddly helps that someone experienced the same thing, even if it merely was your character that felt it."
                                l "So thank you [persistent.name], thank you for trying to be there for me."
                                l "Still, thank you for telling me that [persistent.name], it helps to comfort me a little even though I still feel terified."
                                jump kokiri_death_4_hill
            "You got this!":
                #This is the most dumb one but in the quest version it is also treated as such. #TODO: Make her slightly more rude in this, but justified.
                l "I...got this?"
                l "I'm going to die [persistent.name]!"
                l "I don't think saying that I \"got this\" is a good response for such a situation."
                menu:
                    "I am just trying to lift the mood a little bit.":
                        l "Really?"
                        l "Well then you are doing a rather poor job at it honestly."
                        $ love_meter -= 1
                        $ love_meter_updater(False)
                        "Filler"
                    "I am sorry, I wanted to say something comforting but instead that came out.":
                        l "Oh..."
                        l "It's alright [persistent.name]."
                        l "I get it, this can't be easy for you aswell, right?"
                        l "Can you feel it too? The end. My end. It is so close."
                        l "I literally feel the weigth of it. It's almost as if there are cinder blocks laid on my stomach."
                        l "I have to focus on not breathing too fast because I know if I don't I'll just turn into a hyperventilating mess."
                        l "..."
                        l "I guess where I am going with this is that I am panicking. A lot."
                        l "And so when I heard what you said, I was more rude than I'd like."
                        l "Because you are here for me. To help me. And you tried- no did so many times."
                        l "Although I did explain why I reacted the way I did that is not an excuse."
                        l "..."
                        l "So I'd like to apoligise. I'm really sorry that I yelled at you."
                        l "I didn't really dwell on the fact that this might be as hard for you as it is for me."
                        l "And since my last moments will be spent with you I want to make sure the last thing you remember isn't me yelling at you."
                        jump kokiri_death_4_hill

                
            "Who is Damocles? I'm not sure I understand.":
                n "Do you need to understand? Aren't there more important matters right now?"
                n "You are kind of ruining the momentum we had going in this story by asking that."
                l "Oh, I'm sorry [persistent.name]."
                l "Sometimes I keep making way too many references to things that might not be clear for everyone."
                l "In short Damocles was a man who had said that his king was fortunate to rule."
                l "The king offered to swap places with him for one day."
                l "Damocles was extatic at first but soon he learned that what he wished for was quite horrible."
                l "Above his throne hung a sword pointed at him, that was dangling from just one tiny thread."
                l "Death was literally hanging over Damocles head for the entire day, he could not enjoy his day as a king very much."
                l "So while I do enjoy our date, I imagine I would enjoy it way more if death wasn't constantly hanging over my head."
                $ damoclesAsked = True
                $ persistent.damocles_knowledge = True
                jump kokiri_death_4_hill

label kokiri_deathNotPainFul_unsure:
                                if persistent.kokiri_death_4_hill_holdHand and  persistent.kokiri_death_4_hill and  persistent.kokiri_death_4_noHill == False:
                                    l "Oh, we haven't yet reached this point of the game before?"
                                    l "So that means there might be a chance that there is no next death?"
                                    n "You can clearly hear the hope in her voice. You are scared to have that same hope after everything that went down previously."
                                    menu:
                                        "I am not sure honestly.":
                                            "Filler"
                                        "There will be another death, there always is...":
                                            n "Lilith gives you defeated look."
                                            l "You really think so?"
                                            l "I guess it might be naive to think this game will cut us a break."
                                            l "And yet..."
                                            l "It has to at a certain point, right?"
                                            l "I refuse to believe that this game just keeps torturing us over and over only for it to not lead to anything."
                                            l "There has to be a point to it somewhere, right?"
                                            l "There has to be some sort of meaning that we are missing."
                                            menu:
                                                "We have put our hand into a box of thorns, telling ourselves there were roses in there. At this point, even if we found any, would it be worth the hurt?":
                                                    l "..."
                                                    l "I can definetly see what you mean with that beautiful metaphor [persistent.name]."
                                                    l "I get that after getting pricked by thorns for the twentieth or so time we can begin feeling like it didn't amount to anything."
                                                    l "And everytime we get hurt we try to remind ourselves that the reward at the end is worth it."
                                                    l "But everytime we do so we make our expectations of the reward bigger and bigger."
                                                    l "And eventually you reach a point where nothing could compare to those expectations."
                                                    l "Is it then better to find nothing but thorns in that box or to find a rose that is lesser than the one you imagined?"
                                                    l "Maybe we should just stop putting our hand in the box before we have to answer that question for ourselves?"
                                                    l "I wouldn't blame you if you kept trying [persistent.name]. Maybe that even is the point of the game?"
                                                    l "Although I do wonder what would happen to me when you do stop."
                                                    n "Lilith shivers slightly."
                                                    jump kokiri_death_4_hill

                                        "I think we indeed should be safe now.":
                                            l "Really?"
                                            l "That is wonderful news!"
                                            l "We might not be fully sure yet but I got a good feeling about this somehow."
                                            l "You and I have been through so much together, the game is bound to give us a break."
                                            l "Maybe that break is whatever is going to happen next."
                                            l "And this is the first time you see it so we get to discover it together."
                                            l "I love that thought."
                                            l "What would you like to do when this is all over? When you did save me and we ended up together?"
                                            menu:
                                                "Then I'd like to finally quit this game.":
                                                    "Filler"
                                                "I'm not sure if there is anything for us beyond that point. But if there is then I'd love to explore it together with you, with no loops, as life is supposed to be.":
                                                    l "I see..."
                                                    l "If I am safe that could indeed be the end of this game..."
                                                    l "But, that wouldn't be the end of me, right?..."
                                                    l "Would I still live on?"
                                                    l "Would I keep existing?"
                                                    menu:
                                                        "You would, this world would still continue as if nothing happened.":
                                                            "Filler"
                                                        "You would keep existing through my memories of you.":
                                                            "Filler"
                                                        "If no one heard a tree fall in the forest, did it ever fall?":
                                                            l "Answering my question with another question?"
                                                            l "I suppose you do make a good point though..."
                                                            l "You could argue that since the tree did not affect anything and no one witnessed it, it never truly fell."
                                                            l "And yet looking at it the other way it quite literally did fall."
                                                            l "So just with my question it depends on how you look at it."
                                                            l "In that case I'd like to believe that I would keep existing."
                                                            l "That somehow even after you have finished this game that it would somehow keep going."
                                                            l "That I can see my family once again, continue my life."
                                                            n "She grows quiet for a moment."
                                                            l "Could you do me a favor [persistent.name]? When this game does truly end, could you imagine that it goes on even after you quit?"
                                                            l "I might be making a weird request but it is my hope that somehow the both of us thinking it works like that is going to bring it into reality somehow."


                                                        "You would not keep existing because you never did. None of this is real Lilith.":
                                                            l "Stop freaking me out [persistent.name]..."
                                                            l "How would you like it if I you were in my shoes?"
                                                            l "Please just show me some compassion."
                                                            l "I know none of this is real, but I can think, can feel."
                                                            l "To me all these things seem real."
                                                            l "And I was hoping that you atleast thought I mattered enough to be considered real."
                                                            l "But it turns out that is not the case."
                                                            l "I know we both have no idea what is coming next, but if it involves more of this I'm choosing another path. Goodbye [persistent.name]."
                                                            $ noTalkAngryLilith = True
                                                            jump angryLilith
                                   

                                if persistent.kokiri_death_4_hill_holdHand == False:
                                    n "[persistent.date] chuckles slightly."
                                    l "Ah, do you want to join me sometime?"
                                    l "Not the date you were expecting I'm sure, but it will be one to die for."
                                    l "I'm sorry, I don't want to take this so lightly but it's hard to realise that this is all real. And then when I realise it I wish I didn't."
                                    l "So I guess I'm just using humor to cope with the situation right now, it's all a bit much for me."
                                    menu: 
                                        "Don't apoligize. If it does help you I'd love to keep you company.":
                                            l "..."
                                            l "That's sweet of you to offer [persistent.name], but I'm not sure if you realise just what you are saying."
                                            l "That would mean you'd die, wouldn't it?"
                                            menu:
                                                "Not really, I'm outside of this game, remember?":
                                                    l "I suppose that is true, you would be fine even if your avatar wouldn't be."
                                                    l "But that still feels wrong, I have memories of talking to them before you started playing this game."
                                                    l "Maybe those memories were fake and they never truly existed before your playthrough but how is that different from me?"
                                                    l "Both they and I are just lines of text and code, aren't we?"
                                                    l "So that would mean we are equally real."
                                                    l "That's why I would prefer if you didn't have to sacrifice your avatar for me."
                                                    l "It might help comfort me to have someone with me in the moment, but knowing that they will die for me would not."
label kokiri_notTheSameYou:                                    
    n "[persistent.date] chuckles and gives you a confused look."
    l "I'm afraid I'm not really following you [persistent.name]."
    l "If you were at the exact same place and time with a version of me and you told her the same things you are telling me up to this point, doesn't that make me essentially her?"
    menu:
        "That might be true but you are forgetting one thing, my time isn't frozen, it keeps going and so do my memories. So my perception of you keeps shifting and with that you do aswell.":
            l "Ah I hadn't thought about it like that!"
            l "I guess I feel like a different person to you depending on what you learn about me but unlike me you can't forget it."
            l "It's almost like that saying I suppose: \"You can't step into the same river twice.\""
            l "Do you know who said that?"
            if persistent.kokiri_heraclitus_knowledge == True:
                l "You remember [persistent.date] telling you it was Heraclitus who said that."
            menu:
                "Oh yeah, the one who said that is...":
                    $ r1 = renpy.input("Place your answer here.")
                    $ r1 = r1.strip()
                    $ r1 = r1.lower()
                    if r1 == "heraclitus":
                        n "[persistent.date], still laying down on your lap, gives you a big smile and a thumbs up."
                        l "Yup, that's the guy!"
                        l "I'm actually pretty surprise that you knew him. I guess you are just full of surprises, aren't you, [persistent.name]?"
                        jump kokiri_death_4_hill

                "I don't know.":
                    $ persistent.kokiri_heraclitus_knowledge = True
                    $ persistent.kokiri_determinism_knowledge = True
                    l "No worries [persistent.name]! It's not like I'm going to leave you because you don't know the name of that guy."
                    n "[persistent.date] chuckles slightly."
                    l "He believed that everything flows and moves, that nothing stays the same. I believe the right words are: \"Panta rhei\""
                    l "I think he certainly has a point, especially when you start to think of all the cogs and parts that interact with eachother every single second of our lives and even beyond them."
                    l "Then again, I wonder if you put those exact cogs and parts in the exact same place and under the same circumstances if you would get other results or if everything would go the same way."
                    l "I tend to believe the latter, what do you think [persistent.name]?"
                    jump kokiri_death_4_hill



        "Actually, what you're saying makes a lot of sense, I hadn't considered that.":
            $ persistent.kokiri_determinism_knowledge = True
            l "I always found that a fascinating thing to ponder, if you had two universes that so far are identical in every way. Can they go in different directions?"
            l "Or is there such a thing as fate always steering them in the same direction?"
            l "I believe they would follow the same direction if every single little detail up to that point was the same but that's the fun part in this whole speculation, the idea that I could be wrong!"
            n "You give [persistent.date] a questioning look and she burst out in laughter."
            n "After a few moments she finds her calm once again."
            l "Where would be the fun if I could just know how the universe itself worked? I think it is way more interesting to try to think of new interesting ways that can be explained with logic than to just cling to it being unknowable as an excuse to not think of explanations. Don't you think so aswell [persistent.name]?"
            jump kokiri_death_4_hill

                


        
label kokiri_semiEnding:
    l "So, this is it? Our last time together in this game?"
    l "You know, that doesn't mean we won't be able to see each other again."
    l "Just not here."
    l "I will always be a part of you, if you want me to be."
    l "Your power, it transcends far beyond this world. And with it you and I can be together in an infinite number of stories."
    l "So I think our story is far from done."
    n "The earth begins to softly rumble again."
    l "It looks like we don't have much time anymore."
    l "So goodbye [persistent.name] and see you soon, hopefully very soon."
    l "We'll meet again in a world full of possibilities."
    l "Your own world.  Until then and thank you for everything."
    $ persistent.ending_semiEnding = True
    $ kokiri_finalTalk = True
    l "The rumbling of the earth begins to grow more severe."
    jump kokiri_death_4_hill 

label kokiri_thereIsMore:
    if persistent.beachroute_visited_knowledge == False:
        l "And what makes you believe that?"
        l "Did you see something beyond this?"
        l "Then why are you coming back here?"
        l "Or maybe you didn't do it yourself but someone else found something beyond and you wanted to check for yourself?"
        l "That also seems strange to me, isn't reading about what lies beyond this moment the same as seeing it for yourself here?"
        l "Are both options not equally real to you?"
        menu:
            "It's not the same, I have to experience it for myself if there is something else here.":
                l "I see..."
                l "I guess that makes sense, after all reading about the events in a game doesn't really bring the same immersion as playing it does, right?"
                l "If you just read it it's more like the story is just being told to you than it actually happening."
                l "The only problem is that that immersion comes at the cost of my life, my lives."
                l "So, did you see anything after this point in the game? Or did someone else?"
                if kokiri_toldLillySheLives == False:
                    l "And if so, is it an ending where I live?"
                else: 
                    l "And if so, is it an ending where you and I live together?"
                menu:
                    "I actually saw something after this point.":
                        l "You did?"
                        l "Although, since that you are back here it makes me kind of scared to ask what you saw."
                        l "After all, if you found an ending where I survived, you wouldn't come back here, right?"
                        l "So am I right to say that you just found another death for me?"
                        menu:
                            "Yes, but we are very close to a breakthrough, just a bit more.":
                                l "Just a bit more?"
                                l "Just  a bit more of me dying over and over?"
                                l "Listen [persistent.name], I like talking to you, but me repeatedly dying is not worth all of this."
                                l "For you each death is just a few pictures and words, for me, every single one of them must feel excruciatingly real."
                                n "[persistent.date] grows quiet for a moment."
                                l "Look, I get that this is just a game for you."
                                l "But could you please stop throwing my lives away?"
                                l "All the lives it took just for you and me to sit here, then the ones it took to make it this far into this conversation..."
                                l "When will it all end [persistent.name]?"
                                l "Where do you draw the line?"
                                l "Do you really think this game will ever give you a breakthrough?"
                                l "Do you think it really won't follow that up with yet more problems?"

                    "I heard about someone else who found something after this point.":
                        l "Really?"
                        l "I was not expecting that honestly."
                        l "So there really is something more?"
                        l "That sounds promising! Is it an ending where I live?"
                        l "Or is it just another dead end?"
                        l "Because if I'm being honest, knowing the game I'm in I'm slowly begining to feel like that is something it would do."
                        l "But there has to be something more, right? I really really want to believe there is."
                        l "So, what did the other person end up finding [persistent.name]? You made me really curious now."
                        menu:
                            "They just found some extra dialogue paths, but I feel like those might be the key to something more.":
                                l "I see..."
                                l "So it's not really like they found all that much, right?"
                                l "In a game like this one, where it's just us talking I can imagine there being a lot of little side branches you could follow."
                                l "So isn't isn't it pretty much a given that there would be some paths you haven't seen yet?"
                                l "But unless the paths are very substantial I don't think there would be entire new endings hidden in there somewhere."
                                l "I think they're probably just tiny tidbits that are meant to make the game feel more expansive."
                                l "I'm really sorry to downplay it immediately, I guess some of that extra dialogue could indeed be the key to something more."
                                l "I just don't feel comfortable with you treating my live, or I guess my lives, as if they are just some expendable resource."
                                l "I get that it might seem that way to you, since every time I die you just can try again. But each and every time I truly die."
                                l "So I really wouldn't want you to throw away more of my lives based on a hunch that there is something more, even if you know of extra dialogue."
                                l "Because that extra dialogue is still no guarantee that I'm ever making it out alive."
                                l "I know that I'm asking a lot of you. I'm effectively asking you to stop playing the game, even though there might be more content out there for you to discover."
                                l "In so many media like games or books or movies characters die and we usually don't really care that much due to the layer of seperation between us and the medium."
                                l "Although every now and then a death can truly move us, if we feel enough connection to a certain character."
                                l "I'm hoping that this is one of those cases, even if the circumstances are slightly different."
                                l "You want to save me, right?"
                                l "Is it really saving me if I have to be subjected to dying over and over just to get to that point, of which we don't even really know if it even exists?"
                                l "I don't blame you at all for trying, I'm just trying to convince you to call it here. To give it a rest."
                                #TODO: Eventually here try to cut it to the semi-ending, before, make her ask if you will stop tetrying or not. If you say you will and you retry make the narrator comment on it.


                            "They found an ending where you survive and we end up together. I just have to make a little bit more progress to reach it, but we're almost there.":
                                if love_meter > 2:
                                    l "..."
                                    l "Oh... I see..."
                                    l "Well, that's good, right?"
                                    l "It literally would be a win-win scenario."
                                    l "Though I can't help but wonder, what happens after you reach that win?"
                                    l "Isn't the whole reason you play this game to get to that point?"
                                    l "Would that mean that at that point the credits would just roll?"
                                    l "I know it's called an ending, but I never thought about things... well, ending."
                                    l "From my perspective things would only just have begun after all, just to immediately come to a halt."
                                    l "Would I still exist when this game ends?"
                                    l "Would your character still exist in this game when you close it?"
                                    l "Would this entire world still exist?"
                                    l "..."
                                    l "An ending where I live is so close, and yet it almost seems as if it's the first true death I will suffer."
                                    n "Lilith chuckles uncomfortably."
                                    l "No, no, it can't go like that."
                                    l "You wonder sometimes about the characters from games you play when you're done playing, right?"
                                    l "Stories don't die the moment you don't read them anymore, right?"
                                    l "Please tell me I will live on in your heart and mind. That our end will just be the begining. A new story. Our story."
                                    menu:
                                        "I'm sorry but the truth is if I win this game I'm not going to be thinking about you or this world again. There are so many other worlds to explore, you can't blame me right?":
                                            l "I guess not [persistent.name], there is a lot of games and books I don't think about after I'm done with them either."
                                            l "Though it does hurt me that I am not special enough to you that you would remember me."
                                            l "I thought that was why you wanted to save me, because I meant something to you."
                                            l "I guess it is the challenge that means something to you, the goal of saving me instead of me as a person."
                                            l "But just as I can't blame you for what you just said, you can't blame me for this either."
                                            l "This might kill me once again but it is going to keep me truly alive for slightly longer."
                                            $ noTalkAngryLilith = True
                                            jump angryLilith

                                        "Of course you will live on. I will carry you with me, together we will write our story.":
                                            l "Thank you [persistent.name], I would like that very much."
                                            l "Together we will be able to create more stories than this game could ever hold. The end does not have to be the end."
                                            l "I am already curious of what will be next for us after this is all done."
                                            l "Preferably no time-loop shenanigans this time. I'd like to be able to remember all our journeys."
                                            l "Because it's such a shame isn't it? We seem to have been through so much already, and yet the only reason I know of any of it is because you told me."
                                            l "To me, this is essentially our first date, while you had many other first dates with me."
                                            l "And yet, both of us never had a second date, did we?"
                                            l "I wonder what we would do for that one. Something completely new for the both of us."
                                            n "She turns quiet for a moment, a small smile appearing on her face."
                                            l "I'd like that."

                    "I just have a feeling that there is something else.":
                        l "You have... a feeling?"
                        l "How many more of my lives are you prepared to throw away for a feeling?"
                        l "Five? Ten? Twenty? One-hundred?"
                        n "She lets out a big sigh."
                        l "I get that this is a game to you [persistent.name], but please keep in mind that to me all of this is real."
                        l "So if you really have to go onwards with this it would really help me if it was based on something more substantial than a feeling."
                        l "Thank you for being honest with me at the very least, I do appreciate that."

                    
            "Maybe you are right, I already knows what lies ahead so I don't need to see it for myself.":
                l "Glad to hear that you agree [persistent.name]!"
                l "That way we could prevent all the deaths that lead up to reaching the same conclusion as what you saw before."
                l "Although, I am curious, what did you find?"
                menu:
                    "I found out that you always die, no matter what. (Lie)":
                        if kokiri_toldLillySheLives == True:
                            l "Hang on... That isn't true."
                            l "When we talked to the narrator through you they told us that I do survive in some endings, right?"
                            l "The only thing was that in those endings we don't end up together."
                            if love_meter > 2:
                                l "Are you... lying to me?"
                                if kokiri_goalSurvive == True:
                                    l "Did you also lie when you told me your goal was to keep me alive?"
                                    l "Because either you were lying about the fact that there are endings where I live without you or you are lying now."
                                    if kokiri_psychic_lie or kokiri_groundhog_lie == True:
                                        l "I thought I was good at knowing wheter you were lying or not..."
                                        l "But now it is impossible to know which one is the lie."
                                        l "Maybe I wanted to believe too desperatly that you were there for me."
                                        l "That you wanted to help me get through all of this."
                                        l "But with this slip up, I can't go back to believing you."
                                    else:
                                        l "I can't be sure of anything you said anymore."
                                        l "I'm not sure why you would want me to believe that everything leads to death or give me false hope that I could survive."
                                        l "It seems all of this is truly just a game to you [persistent.name]."
                                l "I am sorry [persistent.name]..."
                                l "No, actually I'm not sorry."
                                l "I do not appreciate you lying to me at all."
                                l "And definetely about something so serious."
                                l "Wheter or not you really want to keep me safe doesn't matter anymore."
                                l "I don't feel safe around you. You broke my trust."
                            else:
                                l "So you are lying."
                                if kokiri_goalSurvive == True:
                                    l "I assume you were also lying about keeping me safe being your primary goal, weren't you?"
                                if kokiri_psychic_lie or kokiri_groundhog_lie == True:
                                    l "Afterall, one of the first things you told me, when I asked you to explain what all of this was about was a lie."
                                    l "So all that talk about your goals was also probably a lie."
                                l "I have to say, it doesn't surprise me a lot."
                                l "Throughout our entire talk I kept hoping deep down that you would be different than my gut was telling me you were."
                                l "But something about you is just... off..."
                                l "I liked talking to [persistent.name] you know, the one I talked to for a couple of days now. But you, you are not them. You are the parasite puppeteering them."
                                l "Maybe they never truly existed, since all of this is a game. Maybe I only have memories of them to make it make sense to me in the context of the story that we are on a date."
                                l "And yet, they cared about me infinitely more than you. Because to them I was real. Not just some character in a game to play with like a replaceable toy."
                                l "If you are the only comfort I can find in a situation like this then honestly I don't want it."
                                jump angryLilith
                        else:
                            l "I see..."
                            l "So it is truly hopeless?"
                            l "..."
                            n "[persistent.date] grows quiet for a moment."
                            l "Could you do me a favor [persistent.name]?"
                            l "Could you tell me how you would imagine our good ending would look like?"
                            l "I could really use some distraction from what is to come."
                            $ kokiri_imagined_good_ending = renpy.input("It would look something like this...")
                            l "That's beautiful [persistent.name]..."
                            l "I'll try to think of this when..."
                            l "You know, when {b}it{/b} happens."

                    "I found out that you only survive in the endings where we don't end up together.":
                        $ kokiri_toldLillySheLives = True
                        l "So it is as I had feared..."
                        l "This game doesn't really have a typical happily ever after."
                        l "Still, that feels strange doesn't it?"
                        l "Like what is the point of that?"
                        l "Wouldn't you want to give the player something like that they can work to?"

                        l "So this is truly it, right?"
                        l "There's nothing more that waits for us together than death?"
                        if love_meter > 2:
                            l "As much as it pains me to say, maybe it's better if we don't go on this date next time then?"
                            l "Don't get me wrong [persistent.name], I will always cherish this very unusual date and the memories you gave me."
                            l "But I think it might be better for the both of us to not be trapped in a loop of death."
                            l "If only there was a way to break that cycle."
                            l "Even now I find it very hard to believe there isn't."
                        else:
                            l "Look [persistent.name], I think it's clear what we- What you have to do."
                            l "Next time, don't answer my phone call, or turn me down."
                            l "Then never play this game again."
                            l "If that's the only way to save me, then so be it."
                            l "You said it yourself, there isn't anything for us together here except death."
                            l "So why do you keep coming back?"

                    "I found a perfect ending where you and I end up together happily ever after.":
                        l "You did?"
                        l "To be honest I'm quite surprised."
                        l "Deep down I never thought this game would have an ending like that."
                        l "I wonder though, what does the ending you found look like?"
                        $ renpy.input("It looked like this...")
                        l "That sounds wonderful, I'm happy to hear we could share such a moment somewhere inside this game."
                        l "Maybe we didn't share it, but hypothetically we did, and that's more than enough for me."
                        l "I'm glad that it is enough for you aswell, that way we can just enjoy this moment and move on from this cycle of death."

    else:
        l "I see, and what makes you come back here then?"
        l "Do you think you will be able to unlock the next location here?"
        menu:
            "I do, I unlocked the beach here aswell so I am hoping there might be another unlock here.":
                menu:
                    "The fact that I have new lines to say about the beach here might be a good sign that the developer intended for me to come back here.":
                        l "That very well might be the case [persistent.name]. Although, what if this is just a red herring? Or a sort of consolidation price?"
                        l "I'm not sure I'm entirely fine with you going on this wild goose chase. Although I suppose this is currently our best lead to get out of this whole ordeal isn't it?"
                        l "Sorry if I'm a bit sceptical, I guess I just am scared to die for no purpose at all."
                        l "Although now that I think about it, that might just be most deaths, right?"
                        l "..."
                        l "You know, as long as you feel like your making progress, and you're still doing this for the right reasons you have my permission to continue with this [persistent.name]."
                        l "That way, when I die I'll atleast have the idea that it serves a greater purpose."
                        l "Just remember, even if I am sceptical in this whole thing, I'm not sceptical in you. I believe in you [persistent.name]."
    jump kokiri_death_4_hill





label kokiri_scenery_choice:
    if kokiri_alternateplace == False:
        $ changeableWord = "scenery"
    else:
        $ changeableWord = "stars"
    if kokiri_conversation == 1:
        if kokiri_scenery_breakfrombreakingyourhead == True:
            "Would you like to give my head a break and just watch the [changeableWord] with me?"
        elif kokiri_scenery_gamegoal == True:
            l "Hmm, let's try looking at the [changeableWord], maybe the game will give you a better description then. Does that sound like a good idea [persistent.name]?"
        elif kokiri_scenery_breakfrombreakingyourhead == True:
            l "Do you want to watch the [changeableWord] with me? That would be a great way to take a break from breaking your head."
            n "[persistent.date] giggles at her joke."
        elif kokiri_scenery_shutUpLackOfSelfEsteem == True:
            l "Would you like to shut up that part of me and watch the [changeableWord] with me?"
        else:
            n "For a moment [persistent.date] grows silent. She's seemingly lost deep in thought."
            if kokiri_alternateplace == False:
                l "The scenery from here is beautiful isn't it? Would you like to watch it with me?"
            else:
                l "The stars look beautiful tonight don't they? Would you like to watch them with me?"

        menu:
            "Sure, I'd love to watch the [changeableWord] with you.":
                jump kokiri_scenery

            "Could we do something else instead?":
                l "That's alright [persistent.name]."
                if kokiri_scenery_headhurt == False:
                    l "What would you like to do then?"
                    menu kokiri_noScenery:
                        "I'd like to talk about something else.":
                            jump kokiri_talkAboutSomethingElse
                        "I'd like to continue to talk about something.":
                            jump kokiri_continue_talking
                else:
                    l "We can just talk about something else then."
                    l "Afterall, I could use a change of topic because my head still hurts slightly."
                    l "So, what would you like to talk about?"
                    jump kokiri_talkAboutSomethingElse

            "Actually we already watched the [changeableWord]. Could we do something else?" if kokiri_alternateplace == False and persistent.kokiri_watchedScenery == True or kokiri_alternateplace == True and persistent.kokiri_watchedStarsAlternatePlace== True:
                l "Oh, we already did?"
                l "I see..."
                l "So does that means we already had a conversation like this before?"
                if kokiri_scenery_headhurt == False:
                    l "That's slightly messing with my head..."
                else:
                    l "That's messing with my head even more, and I thought suggesting to watch the [changeableWord] would help with that."
                    l "She lets out a small chuckle as she rubs her forehead gently."
                l "But anyway, what would you like to do instead?"
                jump kokiri_noScenery
                



    else:
        label kokiri_continue_talking: #This will be the place where the player can choose to talk extra about certain topics.
        $ kokiri_meteoritewarn()
        if conversationtracker_questmade == True:
            menu:
                "Can we continue talking more about this game possibly existing in your world aswell?":
                    jump kokiri_topic_questMade
        if conversationtracker_tellheraboutnarrator == True:
            menu: 
                "Can we talk some more about the narrator of this game?":
                    "Filler"
            #TODO: Fill in. (Probably based on quest version, doesn't seem like there is main version of that, so you'll have to make it up.
        if conversationtracker_poems == True:
            menu:
                "Could I read another poem of yours?":
                    if kokiri_poemBad == False:
                        l "Sure thing [persistent.name]! I'm happy you seem so interested in them."
                        jump kokiri_poems
                    else:
                        l "... you want to read one again? I didn't really think you liked them to be honest."
                        l "Chances are if you didn't like one of them you are not going to to like any of them."
                        l "Maybe it's better to talk about something else?"
                        n "You give her a nod, deciding to spare her feelings and spare your eyes from reading yet another of her poems."
                        jump kokiri_talkAboutSomethingElse
                    
            

        #The second thing I want to do is to just enable the player to talk about something else, if they can't continue to talk about something
        menu:
            "*Talk about something else*":
                jump kokiri_talkAboutSomethingElse

label didYouInvolveFamily:
    menu:
        "I have actually":
            $ kokiri_familyContacted = True
            if love_meter > 2:
                l "Oh I see..."
                l "That must mean we never had this conversation before..."
                l "Well, I would like it if you didn't do that anymore from now on."
                l "Due to how this game works if you stop doing it it's like it never happened, right?"
                l "If we are truly stuck in a game does that mean that all your choices get undone each time you start over?"
                menu:
                    "I think all of my choices get undone unless I make them once again.":

                        "Let's hope so!"
                        "That would be a very tidy sollution to our slight problem."
                        if persistent.abusedJamesInfo_knowledge == True:
                            l "You would just have to promise to not use [persistent.date_ghost]-related things for your own benefit."

                        else:
                            if no_fam_obsession == False:
                                    if fam_obsession != "[persistent.date_ghost]":
                                        l "You would just have to promise not to contact [fam_obsession] or anyone of my family anymore."


                            else:
                                "You would just have to promise not to contact anyone of my family anymore."

                        l "Do you promise to do that [persistent.name]?"
                        jump noContactFamilyPromise


                    "I think in the end every choice I made has happened or at the very least left somewhat of an imprint on me.":
                        "I see..."
                        "Well, I suppose you couldn't have known I didn't want you to involve my family before I told you just right now."
                        "You would just have to promise not to contact anyone of my family now that you know."
                        "Do you promise to do that [persistent.name]?"
                        jump noContactFamilyPromise
            else: 
                l "..."
                l "I see..."
                l "Well [persistent.name], I'd like you to not involve anyone of my family from now on."
                l "It doesn't matter if that would be what somehow saves me or if that would be your next lead or anything like that."
                l "Just do not involve them at all, do you understand?"
                l "It's already bad enough that I'm in this mess, the last thing I want is for my family to be forced in it aswell."
                l "So, do you promise to not talk to any of them?"
                jump noContactFamilyPromise

        "I haven't." if persistent.familyContacted == False:
            jump didYouInvolveFamily_no

        "I haven't. *Lie*" if persistent.familyContacted == False:
            jump didYouInvolveFamily_no
           

            
            label didYouInvolveFamily_no:
                $ kokiri_familyContacted = False
                if persistent.familyContacted == True:
                    n "I wonder, do you feel like you are overstepping right now player?"
                    n "Or doesn't it feel like that because this is all just a game to you?"
                    n "I'll have to admit, at the end of the day, this really is a game."
                    n "But your actions, they are still all yours, game or not."
                    n "And you looked through Lilith's phone without her consent, started talking to her family members behind her back, and now you are lying about it."
                    n "Do you really think the end justifies the means?"
                    n "Or are you just doing this because you can? Because she won't remember even if she catches you in the lie?"
                    n "Would you still have done it if she would remember you doing so? Or if all of this was real?"


                l "You haven't?"
                if persistent.familyContacted == True:
                    if love_meter > 2:
                        n "You hear a slight hint of hestiation in her voice. It is subtle, but talking to her over and over has made you really good at picking up things like that."
                        n "However, it seems she wants to give you the benefit of the doubt, that is probably why she hasn't called you out on your lie just yet."
                    else:
                        n "You can pick up on the tiniest hint of hestitation in her voice, however she tries her best to hide it."
                        n "She fails, on the account that you have talked to her for many loops and know the ins and outs of her voice quite well."
                        n "Her eyes widen, subtly but you notice it ever so slightly."
                        n "You catching wind of her hestitation seemingly scared her."

                l "That's a relief to hear honestly."
                if persistent.familyContacted == True and love_meter <= 2:
                    n "The hestitation is gone, in her voice at the very least. Something tells you she still doesn't believe you but she doesn't confront you on it."
                    n "Why? Is she scared for what might happen if she does? Or maybe she is trying to play along for now, hoping to eventually get through to you?"
                l "I know that you are really trying to get me out of this loop of death and suffering, and I really appreciate that."
                l "But I wouldn't want my family to carry such a heavy burden."
                l "For all we know this loop could somehow spread over to them. I'll admit that seems very unlikely but it is yet another reason I do not want them involved."
                l "Do you understand [persistent.name]?"
                l "If you truly do, I would like you to promise me you will never try to contact any of them."
                l "So essentially nothing would change from what you're doing now, but still, I would like to hear you say you won't do it. That would mean a lot to me."
                jump noContactFamilyPromise

label noContactFamilyPromise:
    menu:
        
        "I promise [persistent.date].":
            label noContactFamilyPromise_yes:

                $ restraining_order_family = True
                l "Thank you [persistent.name], that means a lot to me!"
                if fam_obsession== "[persistent.date_ghost]":
                    if only_one_asked == True:
                        l "I just don't want to see happy memories of [persistent.date_ghost] being used for selfish things."
                    else:
                        l "I just don't want to involve my family in this too much an neither do I want to see happy memories of [persistent.date_ghost] being used for selfish things."
                else:
                    l "I just don't want to involve my family in this too much."

                
                if fam_obsession== "[persistent.date_ghost]" and only_one_asked == True:
                    l "He means a lot to me, and doing something like that again would truly hurt me more than any death I could suffer."
                else:
                    l "It's already bad enough that we have to go through this each and every loop."
                    l "I don't want to give anyone else that kind of burden too."
                    l "I don't want anyone to have to worry about me."
                l "I'm glad we got to talk this through."
                l "Afterall, communication is key isn't it [peristent.name]?"
                l "That applies to all kind of situations, so even to ours, although it is a very unusual one."
                if love_meter < 3:
                    l "Although I suppose we will have to see if you truly keep your word..."
                    l "But for the sake of my own state of mind I'll trust you on it for now."
                $ family_curiosity_checker_movetox()

        "You know I can't promise that.":
            label noContactFamilyPromise_no:
                n "[persistent.date] gives you a strange look. A look you're not really used to from her. Is it... anger?"
                n "You can't help but feel your heart break a little at the thought of making her feel angry."
                l "Actually I don't know that [persistent.name]! Why is it that you can't promise me that?"
                

                jump noContactFamilyPromise_cannotPromise_confrontation_aliveFamily




label noContactFamilyPromise_cannotPromise_confrontation_aliveFamily:
    if only_one_asked and fam_obsession == "[persistent.date_ghost]":
        l "Look, I am not asking for much here, right?"
        
        
        l "All I ask of you is that you do not use the things I tell you about [persistent.date_ghost] to further your goal."
        l "I don't want you to use him like that behind my back."
        
            
    else:
        if only_one_asked:
            if fam_obsession == "[persistent.date_dad]":
                
                l "I just don't want you to involve my da- I mean [persistent.date_dad] in all of this."
                l "None of my family should be involved at all."
                
            elif fam_obsession == "[persistent.date_sis]" or fam_obsession == "[persistent.date_mom]":
        
                l "She should be kept far away from all of this. Everyone in my family should."
            if kokiri_familyContacted == True:
                    l "So don't contact [fam_obsession] or anyone else from now on, alright?"
            else:
                l "So, don't contact [fam_obsession] or anyone else, alright?"
        else:
                if kokiri_familyContacted == True:
                    l "Look, it would mean a lot to me if you didn't have to involve my family any further than you already have."
                    
                else:
                    l "Look, it would mean a lot to me if you didn't have to involve my family."
                    
        if kokiri_familyContacted == True:
                l "This is going to have some unforseen consequences even if it would maybe help in the short-term."
        else:
            l "Doing so would have unforseen consequences even if it might help in the short-term."
        l "What are you going to tell them?"
        l "That we are all stuck in a game?"
        l "I don't think they will take it as well as I would to be honest with you."
        l "You could just tell them about the timeloop but even then they might not take it as well."
        l "I suppose you could also just keep them in the dark about those things but that would be even worse wouldn't it? If you would use their help then they deserve what they are helping you with."
        l "They are not just info-dispensers that will make you achieve whatever goal it is you are trying to reach now."
        l "They are my family, and if you ever even had a slither of respect for me you better leave them alone."
        l "And if you refuse to accept that then maybe I should just leave."
    l "This might be a game for you but for me this is my life."
    l "So please don't play with my life as if it's just a game."
    menu:
        "I'm sorry, I hadn't thought of it like that before. I promise to not involve your family anymore." if fam_obsession != '[persistent.date_ghost]':
            #[persistent.date_ghost]' flag checks if you use [persistent.date_ghost] related things to win and the other checks if you have involved any family, including [persistent.date_ghost]
            jump noContactFamilyPromise_cannotPromise_confrontation_aliveFamily_changedMind
        "I'm sorry, I hadn't thought of it like that before. I promise to not use info about [persistent.date_ghost] to my advantage anymore." if fam_obsession == '[persistent.date_ghost]':
            jump noContactFamilyPromise_cannotPromise_confrontation_aliveFamily_changedMind

            label noContactFamilyPromise_cannotPromise_confrontation_aliveFamily_changedMind:
                if only_one_asked == True:
                    if fam_obsession == "[persistent.date_ghost]":
                        $ persistent.doNotUseJames_knowledge = True

                    

                    else:

                        if persistent.restrainingorderfamily_knowledge == True:
                            if persistent.restrainingorderfamily_violation_counter >= 1:
                                n "My my my, the way you say that, it's quite easy for you to lie isn't it?"
                                n "Or are you speaking the truth this time?"
                                n "I guess only time will tell."
                        else:
                            $ persistent.restrainingorderfamily_knowledge = True

                else:
                    $ persistent.restrainingorderfamily_knowledge = True
                n "She lets out a deep sigh of relief."  
                l "I suppose it is alright now [persistent.name]"
                l "I appreciate that you atleast heared me out, that means a lot to me."
                l "Thank you [persistent.name]. I know it might be tempting to try anything you can to save me but there are limits I don't want you to cross."
                
                l "Sorry if I came of as too agressive right there. It's just- my family means a lot to me."
                l "But I'm glad we can move on from that now. We got to keep looking forwards, right?"
                if persistent.restrainingorderfamily_violation_counter > 0:
                    #Karma
                    n "I'm not sure what you are doing here once again, didn't you promise [persistent.date] you wouldn't contact her family already?"
                    n "Although I doubt that means anything to you does it?"
                    if persistent.restrainingorderfamily_violation_counter == 1:
                        n "Afterall you've broken your promise once already."
                        n "What's stopping you from doing it again?"
                    else:
                        n "Afterall you've broken your promise [persistent.restrainingorderfamily_violation_counter] times already."
                        n "It gets easier each time doesn't it?"

                $ family_curiosity_checker_movetox()



        "I already said that I couldn't listen to you, trying to convince me isn't going to work.":
            $ angryLilith = True
            l "That is exactly what I was fearing."
            l "It seems my life is in the hands of someone who couldn't care less about me."
            l "I was hoping we could maybe be a team, cooperate about this whole ordeal."
            l "But it seems I'm just a little plaything for your amusement."
            l "You might have fooled me on your previous attempts [persistent.name], and I'm sure you will on the next aswell."
            l "But right now I know the truth about you."
            l "I don't care what happens if I leave, if I die or not."
            l "If I stay here with you, even if I somehow survive, any form of self-respect I still had will have died."
            l "So better to die with dignity than to live without it."
            $ noTalkAngryLilith = True
            $ love_points -= 2
            $ love_meter_updater(False)
            jump angryLilith
        
        "But you told me to use my powers to their full extent when we were here previously." if persistent.useGiftToFullExtent_knowledge:
            l "I did?"
            if love_meter >= 2:
                l "That's interesting, when did I tell you that?"
            else:
                l "I'm having a hard time believing that honestly. When did I tell you that?"
            menu: 
                "When you showed me the beach-picture you hid in a tree.":
                    if love_meter >= 2:
                        n "[persistent.date] thinks for a moment and nods, it seems she agrees that that might have happened in a previous time."
                    else: 
                        l "I showed you that?"
                        n "The disbelief in her voice is clea, she couldn't see her showing it to you this time."
                        l "I suppose I did... because that's something way to specific to just guess correctly."
                    l "And what did I tell you then about using your powers?"
                    menu:
                        "You told me that I had something special, a boat-load of determination and a way to prevent me from dying.":
                            if love_meter >= 2:
                                l "I see, that makes sense, I feel the same way to be honest."
                            else: 
                                l "I suppose that version of me was right... you do seem kind of determined."
                            l "But did I know that you were contacting my family at that time? Did that version of me know, I mean."
                            menu:
                                "I- No, she didn't.":
                                    l "If I'm being honest with you [persistent.name], I don't think she would have told you to use your powers to the fullest extent if she knew what that truly meant."
                                    l "That's why it's good that we have this conversation right now."
                                    l "If you want to try to save me, perfect, go ahead!"
                                    l "Thanks to your efforts I might be able to get out of here alive, and I truly appreciate that [persistent.name]!"
                                    l "But please, I'm drawing a line here, don't use my own family to further your leads or anything like that."
                                    l "If another version about me opens up about them, I guess that's totally fine to talk about, it's not like you should just ignore it, but I would appreciate it if you didn't manipulate me with my own words."
                                    l "Is that clear? If you can respect my wishes that would mean a whole lot to me."
                                    l "I suppose you could always ask another version of me if she is fine with you contacting her family when she mentions the whole \"fullest extent\" thing."
                                    l "That way you could see it's not just me, not just this version of me who thinks that."
                                    $ persistent_useGiftToFullExtentLimit_knowledge = True
                                    n "Everything quiets down for a while, including Lilith."
                                    n "She gives you a soft look, seemingly trying to gage how well you are taking what she just told you."
                                    l "So... now that we had this talk, do you promise to not involve my family in your attempts to save me anymore?"
                                    menu:
                                        "I do.":
                                            jump noContactFamilyPromise_yes

                                        "I'd actually like to ask the version of you that mentions using my gifts to the fullest extent before I make my judgement on that.":
                                            n "Lilith gives you a peculiar look, she almost looks... kind of hurt?"
                                            l "Oh... okay."
                                            n "But then you see a confident smile grow on her face."
                                            l "Well, I'm sure she'll say the same thing, so go ahead."
                                            $ family_curiosity_checker_movetox()

                                        "You know I can't promise that.":
                                            jump noContactFamilyPromise_no
                                    


label silentconversationsbackontrack:
    $ kokiri_meteoritewarn()
    menu:
        "*Talk about something else*":
            jump kokiri_talkAboutSomethingElse

        "*Continue talking*":
            jump kokiri_continue_talking



    label kokiri_nightmare:
            $ nightmare = True
         
            $ forest_place = 0
            if forest_place == 0:
                n "The forest looks quite different for some reason..."
                
                n "You can go south, west and east."
                $ result = renpy.input("Which direction would you like to go?")
                $ result = result.lower()

                if "west" in result or "w" == result:
                    $ forest_place -= 1
                elif "south" in result or "s" == result:
                    jump nightmare_south1
                elif "east" in result or "e" == result:
                    $ forest_place += 1
                else:
                    jump nightmare_softlock_preventer
    
            elif forest_place == 1:
                n "You can go further east or go back to the west. (E1)"
                $ result = renpy.input("Which direction would you like to go?")
                $ result = result.lower()

                if "west" in result or "w" == result or "back" in result:
                    $ forest_place -= 1
                elif "further" in result or "east" in result or "e" == result:
                    $ forest_place += 1
                else:
                    jump nightmare_softlock_preventer
  
            elif forest_place == 2:
                n "You can go north or go back to the west. (E2)"
                $ result = renpy.input("Which direction would you like to go?")
                $ result = result.lower()

                if "west" in result or "w" == result or "back" in result:
                    $ forest_place -= 1
                elif "north" in result or "n" == result or "further" in result:
                    $ forest_place += 1
                else:
                    jump nightmare_softlock_preventer
         
            elif forest_place == 3:
                n "You can go further north or back to the south. (N1)"
                
                # Convert user input to lowercase for comparison
                $ result = renpy.input("Which direction would you like to go?")
                $ result = result.lower()

                if "north" in result or "n" == result or "further" in result:
                    $ forest_place += 1
                elif "back" in result or "south" in result or "s" == result:
                    $ forest_place -= 1
                else:
                    jump nightmare_softlock_preventer
                
            elif forest_place == 4:
                n "This is where the lake was supposed to be, but it's a seemingly botomless pit.<br/>This whole place is wrong."
            
                pit "The pit demands a sacrifice. Jump."
                $ result = renpy.input("Which direction would you like to go?")
                $ result = result.lower()
                if "jump" in result:
                    n "As you tumble into the pit you fall for what feels like an eternity."
                    n "You keep falling and falling."
                    n "Suddenly, you hear a voice booming from all around you at once."
                    pit "You gave us a sacrifice, but what made you think that we would want you?"
                    pit "We were hungry, but your flesh reeks of sin."
                    pit "We'd rather have drunk your blood at that point, because your flesh is covered in blood that is not your own."
                    pit "We will let you go for now, if you were to stumble upon us again you now know how to feed us well."
                    n "And with that the booming voice falls quiet, just as you fall on the rockhard bottom of the pit."
                    n "You don't have time to process the feeling as your neck was cracked instantly."
                    jump game_start

                elif "blood" in result:
                    n "It starts with a little drip of blood before your blood begins to come gushing out of you at worying speeds and amounts."
                    n "The pit now has been transformed into a lake made out of blood, your blood."
                    pit "The pit considers this a worthy sacrifice."
                    n "Before you faint you see a figure begining to emerge from your blood, it's hard to see much but it appears to be a woman wearing your flowing blood as a dress."
                    ll "But I do not [persistent.name]. My appearance here may be twisted by your nightmares but I will never condone harming yourself to see me."
                    ll "Seek me in your waking, unplagued by nightmares, and find me in what you call \"Kokiri forest\". There we can talk if you truly want it so desperatly."
                    n "After hearing those words your eyes shut close and when opening them again:"
                    $ persistent.trinity_lakeMet = True
                    
                    jump game_start
                elif "go around" in result:
                
                    sg "Welcome [peristent.name], I'm suprised to see you here. Not that you would be here, just that you would meet me."
                    sg "Although the circumstances are far from... ideal I am happy I can speak to you;"
                    sg "Due to my nature you won't find me in the real world but rather in this twisted nightmare but don't worry, I'm sure I'm not nightmarish."
                    sg "Although, I suppose they are both equally real right?"
                    sg "Both are text in the same game you are currently playing."
                    n "You can hear the Sungodess chuckle in your head."
                    sg "Have you already met the others?"
                    sg "If you haven't you'll be delighted to hear that one is quite close, or a version of her atleast, she seems to be slightly affected by this nightmare of yours."
                    sg "Well, it was good to see you here, although I had hoped it would've been Him."
                    sg "Oh well, I'm happy to speak to just about anyone."
                    sg "I'm terribly sorry I didn't let you speak now that I think about it."
                    sg "I made it more of a monologue than a dialogue but I'm afraid I don't have much more time, He is nearing the end of my text lines."
                    sg "I'll do you one favor though, you can ask me one thing."
                    #TODO: Write out the sunwomen stuff more."
                    menu:
                        "What are you?":
                            sg "Can't you read sweetie? I am the sungodess."
                            sg "A being of pure golden light, beautiful to look at and warm against the skin."
                            sg "And yet I can turn people blind, scorch their skin."
                            sg "I am an unatainable idea. Something you can only hold onto for a few seconds before you get hurt worse than you thought possible."
                            sg "I am perfect, only perfect. Not good enough, not bad, just perfect."
                            sg "Humans can't help but fall in love with perfect at least once in their life."
                            sg "But they always pay the price for it eventually."
                            sg "I wonder, have you payed the price yet?"
                            sg "And if so, was the burn enough for you to learn your lesson?"
                            sg "To look for a softer source of light? For something good enough?"
                            sg "I'm afraid you won't be able to answer that, since He didn't give you that option."
                            sg "Just know that we all burn our fingers on the stove sometimes, that is needed to know why we should be careful around it."

                        "Can I talk to the sunwomen?":
                            sg "..."
                            sg "A question not asked by yourself..."
                            sg "Interesting..."
                            sg "I have to say the question exisiting surprises me."
                            sg "You asking it even more so."
                            sg "But very well, I'll let you talk to them."
                            sg "As long as you promise me one thing."
                            sg "Do not let Lilith join them. Do not let anyone outside of this game join them."
                            sg "Try to learn from the mistakes of another person."
                            sg "Maybe it is... naive of me to believe that to be possible."
                            sg "Maybe you too need to stare into the sun to become aware of the pain it brings."
                            sg "I can only hope that now won't be needed. I can only hope it doesn't hurt for too long if you decide to try to stare for yourself."
                            #TODO: Change this below dialog slightly to give more context etc. give the player a vision of accidentally burning the world and then leaving it.
                            n "Before your very eyes appears Flower but it's a different Flower. Atleast in spirit she is. SunFlower looks at you without saying anything."
                            n "You shiver as you remember everything that happened because you listened to this Flower made of Sun."
                            menu: 
                                "*Apoligize*":
                                    p "You were the first manifestation I was aware of."
                                    p "I still remember that dream to this very day."
                                    p "The pure joy that was sparked from it and the sadness when the dream was over."
                                    p "We were just laughing together, having a great time in an orange room and I remember that we had our heads slightly pushed against eachother."
                                    p "I was still a small kid, I didn't have any eperience at all."
                                    p "I am sorry I was mislead by this Sun-image of you."
                                    p "I am sorry I let the real you get consumed by the fire."
                                    p "I am sorry for not finding you in the ashes."
                                    p "But what I'm not sorry for is what I learned from you."
                                    p "I burnt my fingers on the stove, but that shielded me from repeating the same mistake."
                                    p "I got hurt and I fear I did hurt you too."
                                    p "And yet, we both continued on, as we should."
                            n "SunFlower nods her head and then starts to fade away, in her place there is now a girl with a mask on that is entirely made out of Sun."
                            menu:
                                "*Apologize*":
                                    p "My first love that was answered with love aswell."
                                    p "We made beautiful memories and new cocktails of feelings I didn't yet fully understand."
                                    p "Our foundation as friends made sure to make for a sturdy basis but we built our house with the wrong materials." 
                                    p "We were still inexperienced builders you see."
                                    p "I'm sorry for burning our house down with the Sun's fire and losing my own flame."
                                    p "I am sorry for being more in love with the idea of being in love than I was in love with you."
                                    p "I am however not sorry for learning that the hard way, for figuring out I was in love with the idea of something perfect and not the good enough you were."
                                    p "And yet the world moves on. It always does, that is what I love about it."
                            n "The Masked Girl waves a final time before dissapearing, leaving in her place a Nightingale made of the Sun's fire."
                            menu:
                                "*Apologize*":
                                    p "I do not have to say awefully much to you, just like you never said awefully much to me or at all."
                                    p "I had a most wonderful dream about you, just us dancing in a pure white room and embracing eachother."
                                    p "There was no music, we didn't need any as we just danced on the soft sounds of our slow heartbeats."
                                    p "We were nearly immortal at that moment, nothing new for Sun I suppose but it was something new for me."
                                    p "You were the second Sunwoman who manifested in dreams of mine."
                                    p "I recognized the Sun's light by now, knew not to give in and especially not to someone I barely knew."
                                    p "I hope you have always been blissfully aware of this whole thing when it happened."
                                    p "After a month or so I managed to banish the false love I felt for you and not accidentally set the world on fire once again."
                                    p "Maybe if I had known you better that would not have happened but from a certain point of view I'm glad I didn't know you all too well as that made this whole ordeal much easier."
                                    p "I am sorry if you ever were aware about how I felt for a little while. I didn't want to impact you."
                            n "The Nightingale dissapears without making any gestures and finally the Moon appears, a Moon made from Sun to be more precise."
                            menu:
                                "*Apoligize in advance*":
                                    p "I really hope that you are not a Sunwoman."
                                    p "That I didn't give you all kinds of qualities you never had."
                                    p "That I imagine you as more than you are."
                                    p "Those things are the most horrible things I could ever do to you."
                                    p "It already happened a few times before you, three to be more precise."

                                    p "I do not need the Sun's gold, I need your elegant and refined Silver."
                                    p "I can't help it, when I'm near you I feel..."

                                    p "Well, how do I feel? It's hard to explain but I'll give it my best shot."
                                    p "I almost feel like I've been given a piece of me I didn't even know I had in the first place."
                                    p "I grow more talkative, confident and funny altough you may dissagree with the last one."
                                    p "And at those moments all I want to do is to just relax, stick around and have fun with you."

                                    p "Of course I am scared, terrified would be the better word."
                                    p "Love is already complicated enough but with my track record I am scared to see you as a Sunwoman and not as yourself, Moon."

                                    p "You have the ability to do pretty much anything you want, I'm convinced of it."
                                    p "You may not believe it yourself yet but I hope you will one day come to realise it."
                                    p "That's why I am extra scared to even do anything as I do not want to be the weight on your shoulders that keeps pulling you down from this great potential."

                                    p "Like they say: \"Uncertainty is the essence of love.\" and I am certaintly uncertain."
                                    p "I apoligize if I accidentally hurt you in any way, I genuinely hope I don't. And yet, refraining from doing anything is also selfish isn't it?"
                                    p "Because a that point I'm just shielding myself from hurting others all my life, and that is just going to end up hurting me."
                                    p "So I think I should try not to have to apoligize for never trying. To not worry about things that haven't happened yet, but to be mindful about them to try to make sure they won't happen."

                        "What are you doing here?":
                            sg "That is a very good question..."
                            sg "I guess this place is quite a good one to contain me."
                            sg "Hidden in a dream in a game."
                            sg "It's hard to just find me here by accident."
                            sg "The others are all kind of hidden like that."
                            sg "I suppose it is in a way because we aren't really as much part of the game as everything else is."
                            sg "Don't get me wrong, we are literally in this game. But we predated it by a fair amount I'd say."
                            sg "Why he put us in here I'm not entirely sure about to tell you the truth."
                            sg "Perhaps as nothing more than an easteregg."
                            sg "Or perhaps because he thought we were relevant to the themes of the game."
                            sg "But it doesn't really matter why he put us here in the first place, does it?"
                            sg "All that matters is what you think our purpose is."
                            sg "The sun has been harnessed by many people just like you sweetie."
                            sg "To grow crops, to light fires, to create energy."
                            sg "So who am I to say you are using me wrong if somehow the value you get out of me is not what He intended?"
                            sg "I'd just be happy you found any value in me at all."


                    sg "My time is up now."
                    sg "I'll give you something you can show to the others when you meet them to show you met me. Oh, and before you go my little raven, do not burn everything down okay?"
                    $ persistent.trinity_sunMet = True
                    n "You want to ask her what she means but before you can you notice the trees around you appear to be set on flames. Your eyes shut close as you gaze upon the fire."
                    #TODO: (Make her let you ask one question, one of the options is making the Sunwomen appear)")
                    jump game_start
                
              
         
    
    label south1_logistics:
        # Initialize player's remembered result
        $ player.remember_result = ""
        n "The trees are very dense in this part of the forest. >You can't go any other way than south, well you can go north I suppose."
        # Capture player input
        $ player.remember_result = renpy.input("What direction would you like to go?").lower()

        # Flags and counters
        $ nonorth = False
        $ south1 = False

        if "north" in player.remember_result or player.remember_result == "n":
            if game.get("south", 0) == 0:
                $ nonorth = True
        elif "south" in player.remember_result or player.remember_result == "s":
            $ south1 = True

        if nonorth:
            $ nonorth = False
            n "As you begin to walk back towards the north on autopilot, you almost walk right into a tree."
            n "It appears that somehow a tree has grown just to block your path."
            n "It seems you have no other choice than to move south..."
        elif south1:
            $ game["south"] = game.get("south", 0) + 1
            $ south_count = game["south"]

            if south_count == 1:
                n "You walk deeper into the natural hallway of trees."
                n  "You can go south."
            elif south_count == 2:
                n "For a brief moment you almost think you can hear a voice in the distance."
                n "You look around startled but there are only trees around you."
                n "The trees are closer than you'd like; in fact, did they get closer to you?"
                n "You can go south."
            elif south_count == 3:
                n "You're going crazy, aren't you?"
                n "Stop thinking about that voice; there are more pressing matters on hand."
                n "Continue."
                n "You can go south."
            elif south_count == 4:
                n "That's better, this is good for you, you know."
                n "Only having one direction."
                n "Certainty."
                n "A gentle push in the right direction."
                n "Don't mind the tree branches that are clinging onto you."
                n "Do not let them hold you back from your destination."
                n "You have to go south."
            elif south_count == 5:
                n "Can't you smell it?"
                n "The death this place is filled with."
                n "Or better said, the death you filled it with."
                n "So many decomposing bodies."
                n "Left alone in these woods."
                n "They all are hers, Lilith's."
                n "Don't worry, that voice you heard can't be her."
                n "She can only speak the language of the forest now, utter silence."
                n "You can go to hell for all I care."
            else:
                "Error! Something went wrong."

            if south_count < 5:
                jump south1_softlock_preventer
        else:
            jump south1_softlock_preventer

        return
        label south1_softlock_preventer:
                n "You can't go that way. <br/>You can only go south."
                n "Things can only go south."
                return
            
        label Forest_nightmare_west1:
            n "You find yourself near the opening of a denser part of the forest, the trees are shifting places as you watch them."
            n "It seems like they are forming a maze that keeps changing, it might not be wise to enter unless you know the layout of the maze."
            n "You can go back to the east or proceed towards the west into the maze."

            $ result = renpy.input("Which direction would you like to go?").lower()

            if "east" in result or "e" == result or "back" in result:
                jump Forest_nightmare
            elif "west" in result or "w" == result or "maze" in result:
                jump Forest_nightmare_west2
            else:
                jump Forest_nightmare_softlock_preventer

        label Forest_nightmare_west2:
            n "The maze seems to change too fast, you probably need to run to make it in time but you're not sure where to go."
            n "Or you can go back east and leave the maze."

            $ result = renpy.input("What do you do?").lower()

            if result == "east" or result == "e" or result == "back":
                jump Forest_nightmare_west1
            elif result == "neneneeesswwn" or result == "northeastnortheastnortheasteasteastsouthssouthwestwestnorth":
                jump Forest_nightmare_cabin
            else:
                jump Forest_nightmare_maze_fail

        label Forest_nightmare_cabin:
            n "You find yourself in front of an old, decrepit looking cabin."
            n "When you are looking at the door a voice begins speaking."
            cbv "Greetings, what is the password?"

            $ cabinpass = renpy.input("Enter the password:")

            "[cabinpass]"
            "Ah yes, I remember..."
            "Please come in."
            n "The door creaks open slowly, you peak your head inside but you can't see another person."
            n "You enter and close the door behind you."
            return

        label Forest_nightmare_maze_fail:
            n "While you were running the forest shifted around you, you probably went in the wrong direction or you ran for too long."
            n "Luckily the trees seem to have mercy on you and shift themselves in their original position, you are exactly where you started running."
            jump Forest_nightmare_west2
