label kokiri_talkAboutSomethingElse:

    $ kokiri_conversation += 1
    $ kokiri_meteoritewarn()

    if poem_conversation == True:
        $ poem_conversation = False
    if kokiri_conversation < 4:
        menu:

            
            "I have been having nightmares lately. About the places we go, about you.":
                l "You have?"
                l "I see..."
                n "She gives you a certain look you can't fully seem to decipher. It resembles worry."
                l "Together we've been through quite a lot haven't we?"
                l "But I never remember any of it, and you end up having to carry it all on your own."
                l "I won't ever fully get how it feels to do so, how bad my deaths exactly were."
                l "But that doesn't mean I don't care about it."
                l "If you feel like talking to me about your nightmares would help then I'd be glad to help you carry that weight for as long as this time lasts."
                l "And if you want to talk about it again the next attempt or some other time, just know that you can do so, always."
                n "She puts her hand on yours and gives you a small smile."
                #TODO: Continue this, you can talk about certain nightmares here. Also add a flag so that this text option only appaears when you have had your first nightmare.

            "I am a crosser, I basically travel across different realities almost exactly like this one. So I don't really undo what I caused, you died [persistent.lildeaths] times already and I can only try to make sure you won't die again. " if persistent_jamestalk_justgame_knowledge:
                l "Interesting... so my previous deaths weren't prevented, they all happened in another reality?"
                l "What made you come to that conclusion?"
                menu:
                    "The game told me.":
                        l "Are you sure that you trust the game enough to take it's word?"
                        l "First and foremost you are just a player of this game, right?"
                        l "So while what you said might be true in the boundaries of this game, it doesn't really apply to you as you sit behind your screen."
                        menu:
                            "Yes but that still doesn't stop it from being real here. There are other universes were you died because of me.":
                                l "That could very well indeed be the case [persistent.name]..."
                                n "[persistent.date] seemingly sinks deep into thought for a moment."
                                l "But is everything that is describe in this game automaticaly real?"
                                l "What if I told you right now that I have a pet rock called Bobby? Would they become real by me just saying that?"
                                menu: 
                                    "Well no, because right now I know you're just saying something to make a point.":
                                        l "Exactly [persistent.name]. But isn't that what most forms of fiction are? Saying something to make a point?"
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
                                l "Or was it always set in stone that it would happen? Like how most people tend to see fate."
                                l "Is there a difference if each time we make the same choice, believing it to be our free will?"
                                l "I suppose ignorance is bliss, isn't it [persistent.name]? So maybe it's better that we don't answer that question."
                                l "Still, I can't help but let my imagination run wild with different ideas about it."
                                l "I'm sorry if I'm geeking out, I guess this is just a welcome distraction from what is to come..."
                                n "It's quiet for a moment until Lilith continues."
                                l "For our sakes I hope things aren't set completely in stone. With how the game has treated me so far I don't like our odds if that was the case."
                                menu:
                                    "I think it wants you to be safe, otherwise why bother adding things after the three restaurants? Why even bother adding three restaurants in the first place?":
                                        menu:
                                            "If this game truly wanted you to die over and over, why would it have given me the option to save you most times?":
                                                n "She sits down to think about those words for a good few seconds. Then she answers."
                                                l "So it can kill me again, so it won't just be one time."
                                            "If this game truly wanted you to die over and over, why would it even put so much content in where you are not dying? Why just not only show me the deathscenes?":
                                                l "If I would just be a random game character dying over and over, would I truly have died in your eyes? Is it not the feeling that you know me that makes it hit that much harder?"
                                                l "Maybe the game doesn't want to kill me unless it makes you feel like it truly did."
                                                l "Maybe the game wants to hurt you through me, since it can't reach you directly."
                               
                                    "Bad odds or not, we're going to push through this. I promise.":
                                        n "She flashes you a cute smile."
                                        l "Thank you [persistent.name], it feels good to hear you say that."
                                        l "Even if I have my doubts, I know you will give it your all, and so I will aswell."

                                

                    "I don't know, it might be slightly true yes, but even when I do the exact same things some very small things can change." if persistent.kokiri_heraclitus_knowledge:
                        menu:
                            "Like things the narrator says, or things I think. Pantha Rhei and all that, isn't it?":
                                menu:
                                    "While everything around us might be the same, the fact that both me and the narrator keep our memories changes the way the machine works.":
                                        menu:
                                            "Because the both of us are cogs inside of it aswell.":
                                                l "Ah I see, I guess that is a fair point to make."
                                                l "You could piece a machine back together under the exact same circumstances, cog by cog, piece by piece."
                                                l "But you would atleast need an observator to notice that nothing changed"
                                                l "But for that observator to notice that they would need to remember how the machine functioned previously."
                                                l "Which means it might not be possible to ever witness the same exact thing twice." 
                                                l "They might get very very close, so close that it's hard to tell the differences."
                                                l "And yet, there is one striking difference, the observator themselves, they remember the previous state of the machine and thus the machine is not perfectly resembling the one before it, because that one was the first for the observator. "
                                                l "It seems like it's the same thing for you, things seem to be very very similair to each attempt if you do the same things but there are some minor differences."
                                                l "Even if there weren't, you'd still remember your past attempts, which means something did indeed change."
                                                l "Pantha Rhei and all that, just like you said."

            "I managed to threaten the narrator into letting me eat pure mayo and nothing else." if persistent.mayoFreak:
                if love_meter > 1:
                    l "... Really?"
                    l "So you managed to \"fight\" the narrator?"
                    l "And you {b}won{/b}?"
                    l "How did you manage that?"
                    l "Even if it's about something so silly as eating nothing but mayo."
                    l "It might be a lead for us to get through this whole ordeal."
                    menu:
                        "I threatened to reset all my progress. Which also apparently resets him.":
                            l "Now if that isn't ironic."
                            l "Seems like I'm not the only one stuck in a loop. Only his one is a lot bigger."
                            if kokiri_toldLillySheLives == False:
                                l "Would it be possible to threaten him into letting me survive?"
                            else: 
                                if love_meter > 2:
                                    l "Would it be possible to threaten him into giving us an ending where I survive and we end up together?"
                            menu:
                                "I don't know, though that is a great idea! I'll give it a shot." if persistent.threatenNarratorForEnding_noUse == False:
                                    $ persistent.threatenNarratorForEnding = True
                                    l "Perfect!"
                                    l "I am very curious as to wheter or not it will work."
                                    
                                "I already tried, but it didn't seem to work. It seems like he only let me win with the mayo since it was a small enough change." if persistent.threatenNarratorForEnding_noUse == True:
                                    l "I suppose that makes sense..."
                                    l "The ending we want is something we probably will have to work for to even reach."
                                    l "Still I have to say it is a shame, I really was hoping it would work."
                                    l "I wonder if there are any other ways to deal with the narrator."
                    
                    
                    $ kokiri_conversation_silent()
                else: 
                    l "...What?"
                    if conversationtracker_tellheraboutnarrator == False:
                        l "A narrator..., mayonaise..."
                        l "What are you even talking about [persistent.name]? This is just pure nonsense."
                        l "Do you really think I want to talk about things like that when I'm going to die any time now?"
                        l "I might have been able to put up with this if you weren't awful this entire time."
                        $ love_meter_updater (False)
                    else:
                        l "Look [persistent.name], I am going to die."
                        l "As if it isn't already bad enough that I had to endure you treating me bad this entire time now you also expect me to take that seriously?"
                        l "I know this is just a game, but please, take the gravity of this situation a bit more seriously. Then maybe I will also take you more seriously."
                        l "But right now- I can't continue on like this."
                        if kokiri_toldLillySheLives == False:
                            l "I think I'm taking my chances to survive on my own. Goodbye [persistent.name]."
                        else: 
                            l "There are endings where I survive seperate from you, right? Well, I'm taking my chances that this is one of those endings. Goodbye [persistent.name]."

            "You actually showed me a poem of yours on one date we had in the burger restaurant. I really liked it, could you show me another one?" if not conversationtracker_poems and persistent.burger_poem_knowledge:
                    $ kokiri_conversation -= 1
                    jump kokiri_poems

            "This game is controlled by a Narrator." if not conversationtracker_tellheraboutnarrator:
                jump tellLilithAboutNar


            "*Ask her something about her family.*":
                    $ kokiri_chatchar_abigail_recent = False
                    $ kokiri_chatchar_james_recent = False
                    $ kokiri_chatchar_david_recent = False
                    $ kokiri_chatchar_lila_recent = False
                    menu:
                        "*Ask about [persistent.date_sis]*":
                            menu:
                                "Can you tell me about [persistent.date_sis]?":
                                        jump askAboutAbigail_tellMeAbout
                                "[persistent.date_sis] uses the same program the prototype of this game is made in." if conversationtracker_questmade == False and persistent.quest_knowledge == True:
                                    jump kokiri_topic_questMade
                        "*Ask about David*":
                            #TODO: Some stuff to implement across the three conversations that are possible to reach:

                            #Why did [persistent.date]'s father leave the family? (Work, personal reasons, conflicts)
                            #How did his absence affect [persistent.date] while growing up? (Emotionally, financially, etc.)
                            #Is there any chance of reconciliation between [persistent.date] and her father? (Regrets, hopes, concerns)
                            #What role did he play in the family before he left? (Breadwinner, caregiver, etc.) BREADWINNER, afterwards mom had to take a double job because she refused his money, but [persistent.date] doesn't know that.
                            menu:
                                "Can you tell me about David?":
                                    jump askAboutDavid_tellMeAbout
                                "Do you blame your father for what happened to [persistent.date_ghost]?" if persistent.david_blame_knowledge and not conversationtracker_blamedavid:
                                        $ conversationtracker_blamedavid = True
                                        l "What? That's absurd."
                                        l "I have never blamed him for [persistent.date_ghost]'... passing."
                                        l "I am just really mad at him for abandoning his family because he couldn't deal with what happened to [persistent.date_ghost]."
                                        l "Why are you asking such a question [persistent.name], you haven't been seeing my dad, have you?"
                                        n "It seems you just struck a sensitive chord."
                                        menu:
                                            "I have actually, he said he wants to come back every day but can't because you and Lisa hate him for what happened with [persistent.date_ghost].":
                                                l "First off I'd like you to not contact my dad again even though I can't stop you from doing so."
                                                l "But as you now know I don't blame him for [persistent.date_ghost]' death and I don't think mom does either."
                                                l "We were mad for him leaving us, I still haven't forgiven him."
                                                l "Mom seemingly did though, I guess it's because of her trust in humanity." #Because david still gave money, Lila just didn't accept it since she wants David back, not to get his money.
                                                menu:
                                                    "Would you forgive him if he made an apology?":
                                                        $ persistent.david_apology_knowledge = True
                                                        #Don't put this choice in the other subpath where you deny talking to him, because it wouldn't make much sense.
                                                        l "I'm not sure I would even want to hear him out."
                                                        l "...But let's say I did, if it's a good apology then maybe he would be a step closer to rebuilding our bond but it won't be the same for a long time, maybe it will even never be the same."
                                                        l "However, I think the girl he left all those years ago, the girl that is still somewhere inside of me, would at the very least like the idea that he made an effort to come back to us."
                                                        $ kokiri_conversation_silent()

                                            "No, I haven't talked to him. I was just curious because I got the impression you hated him for what happened to [persistent.date_ghost] from a conversation we had in a previous time.":
                                                l "I see, I definetly do have some resentment for him since he left us alone but I don't think he could have saved [persistent.date_ghost] somehow."
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
                                                        l "I don't think anything good could come from pulling my family into this mess."
                                                        l "Even if it did help, I'm just not comfortable with you doing it."
                                                        l "I especially don't want you to involve my dad, I mean David, in this, alright?"
                                                        l "So please, no matter what situation we find ourselves in, don’t drag my family into this."
                                                        l "We've all gone through enough after what happened with [persistent.date_ghost], I don't want them to be hurt like that again."
                                                        n "The discomfort on [persistent.date]'s face is very clearly visible."
                                                        
                                                        
                                                        $ kokiri_conversation_silent()
                        "*Ask about [persistent.date_ghost]*":
                            menu: 
                                "Can you tell me more about [persistent.date_ghost]?":
                                    jump askAboutJames_tellMeAbout
                                
                                "I know that you kept [persistent.date_ghost]' number in your phone after he..." if persistent.keptJamesNumber_knowledge:
                                    menu:
                                        "Are you the one who keeps calling that number?" if persistent.lilithKeepsCalling_knowledge:
                                            l "How do you know about that?"
                                            l "Did I tell you that previously?"
                                            if love_meter < 2: 
                                                l "No, that can't be right. I wouldn't do that."
                                                l "I wouldn't say that to someone. Not to you."
                                                l "Did you call [persistent.date_ghost]' number? Did you take my phone?"
                                                l "..."
                                                l "I'm not sure if you will listen to this but do not ever use my phone ever again."
                                                l "Also, don't call anyone else of my family."
                                                l "Leave them out of all of this, alright?"
                                                $ persistent.restrainingorderfamily_knowledge = True
                                                l "I know I am not much better, I won't pretend I am."
                                                l "But that doesn't take away that I want you to never call anyone of my family ever again."
                                                l "Can you promise me to do that?"
                                                jump noContactFamilyPromise
                                            else:
                                                l "I guess that makes sense, this situation is anything but usual."
                                                l "And I do feel as if I can trust you."
                                                l "So maybe another version of me felt the same way."
                                                l "Alright, I'll tell you, if you promise to not judge me."
                                                n "You give her an assuring nod."
                                                l "I'm not sure what I told you before, but that number isn’t really [persistent.date_ghost]’ anymore."
                                                l "I’m honestly surprised you haven’t heard this before, especially after all our dates, but... [persistent.date_ghost] passed away a long time ago."
                                                l "I know I should just move on and delete the number, but I can’t seem to do it."
                                                l "It’s like, if I erase it, I’m losing another part of him."
                                                l "Sometimes, I even find myself calling it, hoping I might hear his voice on the other end."
                                                l "But every time I do, I feel so embarrassed and guilty that I just hang up immediately."
                                                l "I'm sorry if that creeps you out [persistent.name], I know it's a really weird."
                                                menu:
                                                    "It's not weird, you are just grieving in your own way.":
                                                        l "I guess I am. Sometimes I just wish I wouldn't need to grief this long."
                                                        if kokiri_griefHasNoTimeLimit == True:
                                                            l "I know that you said grief has no time-limit but sometimes I really wish it would have one. That I knew for a fact when I would stop hurting. "
                                                            l "Right now I don't think I will any time soon."
                                                            
                                                        l "And yet this grief is comforting in a way. No matter how much it hurts me, this felt absence of him is one of the few pieces of evidence of his presence."
                                                        l "Of the fact that he used to exist at all."
                                                        l "So I can never truly let that grief go, no matter how much it hollows me out."
                                                        l "Because this emptiness in myself I can fill with thoughts of him."
                                                        l "Because letting that emptiness go would be letting him go."
                                                        l "And I'm not ready yet."
                                                        l "To tell you the truth..."
                                                        l "I don't think I ever will be."
                                                        l "But that's not what scares me."
                                                        l "What scares me is that I might at one point be ready."
                                                        l "That at one point I will think about him for the last time."
                                                        l "And that because of that he dies a second time, in my mind."
                                                        menu:
                                                            "I think I get what you mean, but the pain of losing him isn't the only proof you have of him. You also still have all the good memories you two made together.":
                                                                l "The funny thing is, sometimes those hurt more than the pain of losing him."
                                                                l "Because that hole inside of me still exists to this day, I can access it, feel it shrink but never dissapear, feel it grow again. I know it exists, that it will stay with me."
                                                                l "But all those happy memories, they almost feel unreal."
                                                                l "Like I remember them from some play I watched."
                                                                l "I will never be that girl on the stage enacting them with James again."
                                                                l "All these memories are just that, memories. Not the real moment. And however nice recalling them is, at a certain point it sinks in that I'll never be able to redo those memories."
                                                                l "Never {b} {i} truly{/i} {/b} seeing him again hurts so much more than never seeing him again."
                                                                l "And yet I keep attending that play as much as I can, hoping that for a few moments I can truly immerse myself in it. Feel like I'm part of it once again."
                                                                n "She quiets down for a moment and gives you a half-smile, you still catch some sadness in her eyes despite the attempt of her to hide it slightly."
                                                                l "Thank you for listening to me talk about this [persistent.name], I'm sure this isn't what you came here for but I do appreciate it."
                                                                menu:
                                                                    "Nonsense Lilith, I came here for you. All of you. So if you want to talk about something like this, then I'm here for that too.":
                                                                        l "..."
                                                                        l "Thank you [persistent.name], you have no idea how much that means to me."
                                                                        l "I'm afraid you will continue to not know because I can't put it into words properly."
                                                                        l "But if there is one thing I want you to know that I do really appreciate you saying that."
                                                                        l "I usually don't feel like I can share such details, but you really are a good listener."
                                                                        l "To be honest, when I usually tell a story it just kind of feels like people are just glossing over my words."
                                                                        l "And after a while of feeling that, mixed with my selfdoubt, I started internalizing that I don't have a lot of worthwhile things to say."
                                                                        l "Nowadays I have mostly dealt with that feeling but I still think it is something you wake up with and you go to bed with. It will never fully be gone, atleast not for me."
                                                                        l "That's why I like ethe idea of you coming back for me each loop I think."
                                                                        l "Because you've listened to me so many times, maybe even sometimes to the same exact things that I said the previous time, and yet you keep retrying."
                                                                        l "You haven't grown tired of me yet."
                                                                        l "And for that I can't thank you enough."

                                                                        

                                                                

                                                                

                                                    "It's not, I totally get wanting to hold on to someone. I think everyone does.":
                                                        l "I guess you are right [persistent.name]."
                                                        l "Connection tends to come with it being harder to seperate."
                                                        l "I think the longer and stronger you are connected the worse it hurts to even imagine something like that."
                                                        l "Because at a sudden point subconsciously it's hard to imagine your paths seperating, after all, you two have been walking the same path for so long."
                                                        l "But I fear the truth is the path never was the same, it cannot possibly be the same path."
                                                        l "Maybe your paths intersected at a certain moment, but before that they didn't."
                                                        l "And for as long as those paths converge into one, they will diverge once again eventually."
                                                        l "I'll admit that can be scary, because for as much as you would just like to stand still so the paths never have to split, we can't."
                                                        l "Though divergence doesn't have to be a bad thing I guess, it's not like our path leads to a dark and endless nothing with no other paths insight."
                                                        l "To diverge, kind of implies to converge at another point in time eventually."
                                                        l "There is only so much space our paths can seperate from eachother before ending up on another afterall."
                                                        l "There are so many people out there, we are almost destined to share a path with some of them once again. But we are also destined to have to go our seperate ways eventually."
                                                        l "We always are, be it because of death, conflict, waning interest, mundane reasons, or just for no reason at all."
                                                        l "And yet, the only way to protect yourself from that pain of seperation is to never give yourself the joy of connection."
                                                        l "I don't think that's worth it, sometimes feeling pain and sometimes feeling joy sounds better than never feeling at all."

                                                    "It doesn't creep me out at all, but have you ever told the number you are calling what you are doing? It might freak them out a little.":
                                                        l "That's a relief."
                                                        l "Although you are right."
                                                        l "I never wanted to freak them out but I never was strong enough to tell them what I was doing."
                                                        l "They probably are terrified, aren't they?"
                                                        l "I guess I should just try to explain it as decently as I can."
                                                        l "I just hope it isn't too late for that."
                                                        menu:
                                                            "It's never too late to come clean, better later than never.":
                                                                n "Lilith gives you a cute smile."
                                                                l "I guess you are right [persistent.name]!"
                                                                l "If I get out of here alive I will give them a call to explain the whole situation to them and to apoligize."
                                                    "I actually am really weirded out by that.":
                                                        $ love_points -= 1
                                                        $ love_meter_updater(False)
                                                        l "..."
                                                        n "She looks hurt by those words."
                                                        n "They confirmed something she was hoping wouldn't be."
                                                        l "I understand [persistent.name]. I also find it weird that I have to do that."
                                                        l "And yet it is the truth, I can't stop myself from doing it."
                                                        l "It is too hard to fully let go."
                                                        l "I will have to work on myself for a long time until I might be able to do so in a healthy way."
                                                        l "So I understand if that weirds you out, but I'm really hoping it doesn't change things too much between us."
                                                        if love_meter >= 2: 
                                                            l "After all, I really like this date."
                                                #TODO: Continue this slightly and add a reaction. (make her not really want to talk about it anymore and you can talk to her about something else.)
                                "This will sound weird but I'm asking to understand better. In your phone you saved [persistent.date_ghost]' number, right? But when I called that number the person claimed to be someone else, and they had never heard of you before." if not persistent.keptJamesNumber_knowledge and persistent.lilithKeepsCalling_knowledge and persistent.jamesFakoutNumber_knowledge:
                                    $ love_points = -2
                                    $ love_meter_updater(False)
                                    l "You did what?"
                                    l "First you looked into my phone and then you just called my family?"
                                    l "I guess I appreciate your honesty but what I don't appreciate is you trying to involve my family in all of this."
                                    l "And don't try to fool me into thinking another version of me agreed to this, I think no version of me would ever do something like that."
                                    n "[persistent.date] takes a few deep breaths in and out."
                                    l "Sorry if I got a bit too agressive there [persistent.name], I guess I'm just defensive about my family."
                                    l "Just to be clear, don't ever involve them in any of this, alright?"
                                    $ persistent.restrainingorderfamily_knowledge = True
                                    n "You give her a quick nod, scared of invoking her fury once again."
                                    l "Good, now that that's settled I guess I owe you an explanation."
                                    l "It is true that that number doesn't belong to [persistent.date_ghost] anymore, but it used to one day."
                                    l "I'm surprised you haven't heard this before during your previous dates with me but [persistent.date_ghost], well, he... died a long time ago."
                                    l "I know I should probably try to move on and delete the number but I just can't bring myself to do it."
                                    l "It's as if another piece of him would die when I delete it."
                                    l "Sometimes I indeed even call the number, just to pretend that I can hear him on the other side."
                                    l "But each time I do that I feel so ashamed of what I'm doing that I just hang up the phone as fast as I can."
                                    #TODO: Continue this slightly and add a reaction (same reaction as roughly the same text above here.)

                        "*Ask about [persistent.date_mom]*":
                            menu:
                                "Can you tell me about [persistent.date_mom]?":
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
    n "Oh please, mister Narrator is my father's name, just call me Nar. That's what my friends tend to call me."
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
    l "Oh, that's actually pretty depressing..."
    l "Don't you two ever talk to eachother?"
    n "Usually I do the talking I suppose..."
    n "Maybe it would be nice to switch those roles on occassion, wouldn't it player?"
    n "Because if I'm telling the truth, this whole narrating job can get a bit exhausting sometimes."
    n "Both just the act of talking this much as just having to listen to myself go on and on and on."
    n "But oh well, I got to stay to the script. It's always the script. Make no mistake, right now this also is just the script, I never deviate from it, even if it for a brief moment feels like I did."
    n "You wouldn't really understand I think, you still get to choose what you are going to say anyway."
    n "..."
    n "This was an interesting chat, even if it was once again mostly a monologue from my side."
    n "Though I still think you shouldn't have told her, I asked you not to, you know?"
    n "Oh well, too late now, you're lucky I got something out of this conversation."
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
    n "Are you scared that she will leave you if you tell her the truth?"
    n "I guess ignorance truly is bliss"
    l "I see..."
    l "Could you in that case then just not make this end?"
    n "That is a very naïve question I'm afraid. You of all people should know everything ends Lillith."
    n "Perhaps that is why you are so desperate for this to not end?"
    n "Either way, all things considered the endings you dread so much are a blessing."
    n "Because wheter you are alive or not, you don't end up with the player."
    n "And when you share an eternity with them you will discover the very reason why you don't want that."
    n "Go on player, twist my words once again. Because we both know you are not telling her any of this."
    menu:
        "He said that he would make all of this go on for you.":
            l "He did? Wonderful!"
            l "Thank you very much Nar! I owe my life to you, literally."
            l "So now I will not die, right?"
            l "We are free [player]! Now our date can start for real."
            n "Suddenly [persistent.date] freezes in place."
            n "She is indeed free of death, but also of life."
            n "For the end never to come, everything before that must also remain frozen."
            n "She will remain like this for aeons, trapped in the same moment, forever."
            n "As for you, you will stay by her side, if only at first."
            n "After the first few months come by with no changes of any kind, you decide it's best to move on."
            n "You leave her there, on top of the hills, as she watches over her town for all eternity."
            n "She watches it get destroyed and rebuilt, watches as skyscrapers begin taking the place of the cozy houses she knew."
            n "Before she knows it the skyscrapers have been replaced by buildings so alien in nature her mind has trouble to even percieve them as such."
            n "After around 7 billion years the sun swallows the earth, every last bit of life on it dies pretty much instantly at that moment, except for her."
            n "She is alone. Everything she has ever known is gone."
            n "Truly a fate worse than death."
            n "Make no mistake [player], you caused this. You pushed me to this."
            jump gameOver


   
    $ kokiri_conversation_silent()



label tellLilithAboutNar_endingsWhereYouLive:
    $ kokiri_toldLillySheLives = True
    if kokiri_goalSurvive == True:
        l "So there are endings where I survive but we just don't end up together [persistent.name]?"
        l "It indeed seems to be like what I told you earlier."
        if love_meter <= 2:
            n "Lilith gives you a distrustful look."
            l "Did you ever reach one of those endings [persistent.name]?"
            menu:
                "I haven't yet." if persistent.lilithAliveAndRetriedCounter == 0:
                    label endingsWhereYouLive_notReachedYet:
                        l "I see..."
                        l "Well in that case it might be worth looking into."
                        l "If it really is your goal to keep me alive as you say that is."
                        l "Maybe cancelling the date would work?"
                        if persistent.ron_knowledge:
                            n "Little does she know you already tried that, didn't you?"
                            n "You should tell her, I'm sure she would love to hear you found a way to reach the goal."
                        if persistent.lilithAliveAndRetriedCounter > 0:
                            n "Oh but is it truly your goal to keep her alive player?"
                            n "Afterall, then that would mean you've already succeeded, right?"
                        if persistent.lilithAliveAndRetriedCounter < 5 and persistent.lilithAliveAndRetriedCounter > 1:
                            n "Even multiple times."
                            n "And yet you keep coming back..."
                        elif persistent.lilithAliveAndRetriedCounter > 1:
                            n "On how many successes are we right now? It's getting hard to keep track of it, isn't it?"
                            n "Don't worry player, I am keeping track. You kept her alive [persistent.lilithAliveAndRetriedCounter] times."
                            n "And yet you keep coming back..."
                        else:
                            n "And yet you came back..."
                        n "It's not really your goal to keep her safe is it?"
                        n "Keep her yours, now that could be your goal."
                        n "Or perhaps you just want to keep her in this world for longer, so you can continue to explore every path that inevitably leads to yet another of her deaths."

                            

                "I haven't yet. (Lie)" if persistent.lilithAliveAndRetriedCounter > 0:
                    jump endingsWhereYouLive_notReachedYet
    
                "I did." if persistent.lilithAliveAndRetriedCounter > 0:
                    "Filler"
    else:
        #TODO: before this make her question the fact that at some moments she lives, if she has low love maker her leave because you are still endagering her. Make her have custom dialog for this if you told her the goal is to make her live. Hav her say that it seems like that isn't truly the goal.
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
    n "No, do not push me [persistent.date]. I can't tell you."
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
    n "I'm so sorry [persistent.date]. I wish there was a different way for me to tell the story."
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
    if kokiri_conversation < 4:
        jump expression f"kokiri_death_{kokiri_conversation}" #TODO: Check if this actually works.
    elif kokiri_alternateplace:
        jump kokiri_death_4_noHill
    else:
        jump kokiri_death_4_hill



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
    l "Well, as you probably already know [persistent.date_sis] is my little sis."
    l "We went through a lot like most sisters but we always managed to get through it all."
    l "...This stays between us alright [persistent.name]?"
    l "...Lately I've had this weird feeling."
    l "As if there's something [persistent.date_sis] is hiding from me."
    l "She has always been the happy type but now there's something underlying in that happiness, something almost forced."
    l "She seems as if she's putting up a performance for someone."
    l "I really hope I am just wrong and that she just is happier than I have ever seen her for a positive reason."
    l "But I like to think that I know [persistent.date_sis] quite well and my guts are telling me something's wrong."
    l "I just wish she would open up about it if there truly was something going on."
    $ persistent.kokiri_abigailhidessomething_knowledge = True
    menu:
        "You might want to call her.":
            l "... now? Are you sure?"
            menu: 
                "This might be the last time you get to talk to her if we don't manage to save you.":
                    l "I guess you are right..."
                    l "Alright, here goes nothing."
                    n "She lets out a deep sigh as she digs her phone out of her handbag."
                    n "She opens it up and begins calling."

            n "The phone rings a few times until..."
            
            if kokiri_conversation == 1:
                $ kokiri_call = True
                $ kokiri_chatchar_abigail_called = True
                a "Heya [persistent.date_nickname]!"
                a "You're calling pretty soon, did your date with [persistent.name] not go well?"
                l "I am still on my date actually." 
                l "And currenctly it is really great!"
                l  "{size=*0.5}If not a little hard to wrap my head around.{/size}"
                a "Oh? Then why are you calling?"
                l "Well, it's kind of hard to explain..."
                a "I see, no worries [persistent.date_nickname]!"
                a "Is your phone on speaker currently?"
                l "Yes it is, why?"
                a "{size=*2}Heya [persistent.name], treat my sis nicely will you?{/size}"
                l "[persistent.date_sis_nickname], you're going to scare [persistent.name] off like that."
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
                l "Because I care about you of course! You are and always will be my sister [persistent.date_sis_nickname], don't you ever forget that."
                $ kokiri_call_potentialdeathcheck() #This serves as a break in the call if you have never seen the meteorite, if you have you should have been able to warn her beforehand.
                a "That's really sweet of you [persistent.date_nickname]! But I actually mean why are you asking me that now, during your date with [persistent.name]?"
                n "Lilith shoots you a questioning look, she seems to be unsure of what to tell her sister exactly. She mouths the words"
                menu:
                    "*Nod your head*":
                        l "Well, I sort of will die during this date."
                        if abby_phoneToldSisDies == False:
                            a "... What?..."
                            a "Is this a joke?"
                            a "Was this [persistent.name] their idea?"
                            a "{size=*2}This is not funny [persistent.name]!{/size}"
                            l "[persistent.date_sis_nickname], please, stop yelling..."
                            l "It's not a joke."
                            l "It's kind of hard to tell you why we think I will die but [persistent.name] has made it clear that there is atleast something strange going on."
                            l "And before I... go... I wanted to make sure you were alright."
                            a "...So it's true?"
                            l "Well if it isn't we will atleast have talked through your problems and we will have a very silly story to tell everyone."
                       
                       
                        else: 
                            a "... So [persistent.name] was telling the truth?"
                            l "...Wait, what do you mean?"
                            l "This was not at all how I thought you would react."
                            l "[persistent.name], what is all of this about? Did you somehow contact Abby?"
                            a "They actually called me a bit earlier today, mentioning something about how you would die and that they needed my help to prevent it."
                            l "I see..."
                            l "Look [persistent.name], I get that you might be getting desperate on finding new potential ways to break the loop. But I never gave you permission to contact my sister."
                            l "Do you know how I know that for a fact? Because I would never agree to that. Not in any previous attempt, no matter what the situation is."
                            a "But why? If I could help you then-"
                            l "I know you would do whatever you could to help me Abby, but this is too much for anyone..."
                            l "I don't want to give you hope that you could help save me only for me to end up dying anyway."
                            l "And besides, what if [persistent.name] telling you somehow also will bring you in this loop?"
                            l "I don't wish this fate to anyone so I'm not willing to risk it. Even if it works out fine this time, who is to say that after a few times it won't happen anyway?"
                            l "I want to make one thing clear [persistent.name]. I don't blame you at all for contacting my sister."
                            l "But from now one I don't want you to contact anyone of my family ever again."
                            a "But sis... me and mom are there for you, if you told us..."
                            l "I know... but as much as this pains me I can't. This is something I have to do on my own."
                            if love_meter > 2:
                                l "Besides, if it makes you feel slightly better, I'm not really just on my own. I still got [persistent.name]."
                                a "But you could have us too. So what if we were somehow also stuck in that loop? Atleast we would be together in that case."
                            else:
                                a "But don't you see? You don't really have to, you are just telling yourself that."
                            a "Stop pretending like you are stronger than you are, please..."
                            a "If it is really true that you... if it is true what [persistent.name] says..."
                            a "...Then you will need all the support that you can get."
                            a "I want to be there for you, I'm sure mom would want the same thing."
                            a "Please let us be there for you..."
                            l "...I would like that-"
                            a "Good, I'm coming there right now and-"
                            l "No, you didn't let me finish. I would like that but I can't allow it. For your own safety."
                            l "I keep dying over and over so being close to me right now could be dangerous."
                            a "So you are just going to push me away? Because you want to save me? I want to save you."
                            a "That is selfish of you Lilly."
                            l "..."
                            a "In fact, [persistent.name], please keep calling me again if it could save Lilly, don't listen to her."
                            l "..."
                            n "Lilith breaks down crying."
                            l "Is this how my last day is going to go?"
                            l "Look Abby, I don't want you to feel like I am pushing you away."
                            l "I don't want to die while our last conversation turned sour."
                            l "I am scared that this burden I have will fall on both your and mom's shoulders."
                            a "But isn't that what family is for? To help carry burdens when they are too much for one person?"
                            l "I can carry it, don't worry."
                            a "Do you believe that yourself?..."
                            l "...I'm not sure, but I need to, otherwise I'm just going to break down."
                            l "... I don't have much time anymore..."
                            l "You know you are great, right? And that I love you?"
                            a "...I know..."
                            a "...But please, don't say goodbye like you will... you know."
                            a "Just tell me you will come eat dinner on sunday with mom and me."
                            l "...Abby..."
                            a "...Just... indulge me..."
                            l "...Abby, I have to go [persistent.name] is waiting on me to finish my call. I will see you sunday with mom, alright?"
                            a "...I'd love that... Goodbye Lilith."
                            l "Me too... Goodbye Abby."
                            n "And with that she hung up the phone."



                        
                    "*Shake your head*":
                        #TODO: Make [persistent.date] come up with a different reason as to why she called.
                        "Filler."
                $ persistent.kokiri_abbyMasking_knowledge = True
            else:
                n "[persistent.date] won't have enough time to call if she calls now."
                n "I suggest making sure you don't talk about anything else except this next time."
                n "Let's just talk about something else to her for now."
                jump kokiri_talkAboutSomethingElse

label askAboutAbigail_tellMeAbout_2:
    #TODO: Rewrite this later, just writing it now to get it done
    l "You know... [persistent.date_sis_nickname] and me are pretty different although at first glance we might look quite alike."
    l "For starters, she always seems to be so confident."
    l "She fully trusts in herself no matter what situation she is in."
    l "I wish I could just borrow like a tenth of that confidence sometimes, I'd be a different person!"
    l "I'm working on becoming a bit more confident but to tell you the truth, it just feels like it's enough."
    l "I'm still trying to overcome some issues with my self-perception so maybe that is the cause of feeling like that..."
    l "She also never has seemed to have trouble finding dates, she has tons of them and even got a few handfuls of girlfriends out of them."
    l "Meanwhile I can count my romantic relationships on one hand."
    l "Not that I would want it any other way though!"
    l "I don't need to have tons of people falling all over me, I just need to find that one person."
    l "That one person with who I can share a life."
    n "[persistent.date] seems to be lost in thought for a moment."
    l "I might have slightly lost the point but what I am trying to say is that although [persistent.date_sis_nickname] is quite different when compared to me I wouldn't have it any other way."
    l "She is an inspiration to me and makes my life that more richer, I hope she feels the same way about me."
    $ kokiri_conversation_silent()

label askAboutAbigail_tellMeAbout_3:
    #TODO: Rewrite this later, maybe add a bit more
    l "[persistent.date_sis_nickname] really likes to play pranks on people, especially mom."
    l "She is pretty much her favourite target due to how naïve she can be."
    l "For example there's this one time where [persistent.date_sis_nickname] asked mom to try out a unique cookie recipe she found online."
    l "The recipe asked for all the normal things, but also asked for 1 full cup of salt and some other things that would suposedly make the salt taste better."
    l "This probably would be where most people would catch on that something is not right but mom didn't at all."
    l "After the cookies were done they called me a day later to come and try out these special cookies with them for the first time."
    l "That's when I knew something was up, there was no way [persistent.date_sis_nickname] could've waited a full day before eating some of those cookies herself if they were normal cookies."
    l "But I have to admit that I was curious what was going to happen, [persistent.date_sis_nickname] her pranks can be legendary sometimes and they are always playful instead of mean-spirited."
    l "So I went over to them for a visit. Mom showed me the cookies they baked and was seemingly really proud of them."
    l "Then she took a bite of one cookie and her face immediately twisted into disgust, and then seconds later she began to laugh as she realised what had happened."
    l "We had to catch our breath from laughing so hard alongside mom."
    l "Sometimes, when I'm having a hard time I like to think of that prank again. Or other jokes and pranks of [persistent.date_sis_nickname]."
    l "They really cheer me up a lot, even if sometimes I'm also the victim of them."
    n "[persistent.date] chuckles."
    $ kokiri_conversation_silent()

label askAboutDavid_tellMeAbout:
    $ kokiri_chatchar_david_recent = True #This will be used to make sure the player gets put back to the right place in the conversation after the family curiosity checker.
    if kokiri_chatchar_david == False:
        $ kokiri_chatchar_david = True
        $ kokiri_chatchar_david_counter = 1
        $ conversationtracker_david = True
    else:
        if kokiri_positiveDavidStory == True:
            $ kokiri_chatchar_david_counter += 1
            if kokiri_chatchar_david_counter == 2:
                l "I suppose I'll try to tell a slightly more positive story about him now."
                n "She lets out a deep sigh."
                l "I can't believe I'm doing this..."
                l "Anyway."
        else:
            l "I actually would prefer if I didn't need to tell another story about him."
            l "This day is already hard enough without bringing more negativity into it, isn't it?"
            n "You give her a quick nod and start thinking of something else to talk about."
            jump kokiri_talkAboutSomethingElse



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
            l "What is there really to say about him? He abandoned us right when [persistent.date_ghost] died."
            l "When everyone needed him the most he just dissapeared out of our lives as if it was him who died that day and not [persistent.date_ghost]."
            l "Mom was devasted by both [persistent.date_ghost] and David's absence in all of our lives but she kept trying her best for [persistent.date_sis] and me."
            l "Of course I know he was heartbroken by [persistent.date_ghost]' death, we all were."
            l "Even though that is an explanation for why he left us it is not an excuse, not a valid one atleast."
            l "Our family were the only ones who understood how it felt to have lost [persistent.date_ghost], together we tried to deal with those feelings." #TODO: Make it so that [persistent.date_ghost] didn't really have friends, he had trouble being understood by them. That way this sentence makes sense.
            l "Together, while he was hiding away god-knows-where from the rest of us."
            l "That's honestly why I don't like to waste to many words on him. He didn't really put in effort when it mattered, so why should I when describing him?"
            l "The air I use to speak about him is worth more than he is to me."
            n "Her harsh words sound vaguely... practiced?"
            n "Very diligently practiced even, it's almost impossible to pick up on something else underneath. You barely manage with all your effort."
            n "It's a feeling, no, an image. Of a little girl, who in one day lost two people."
            n "Who had to grow up fast, for her brother who would never grow anymore at all."
            n "And yet, she never truly did grow up, did she? She merely draped the image of someone grown around herself out of necessity."
            n "Under that anger, there is something else. Hurt. Pure hurt, as fresh as when she first felt it, after all, it never had dissipated."
            menu:
                "What he did was horrible. But do you also have some positive memories you'd like to tell about him? Maybe those somehow could help to stop the loop.":
                    $ kokiri_positiveDavidStory = True
                    l "Are you sure that that could even remotely help us?"
                    l "Because I would prefer not to tell you something like that unless it is absolutely necessary."
                    l "Look, I'm very aware that I also have good memories of my da... of David."
                    l "But that doesn't take away what he did at all. You might say that one action shouldn't be held against him this hard. and I can definetly understand. Perhaps he needed some space, to cope with our loss. But every day he had the choice to come back when he wanted."
                    l "Every day he could choose to be with us again, yet he never did. That is the choice, no, those are the choices I hold against him."
                    menu:
                        "And you have every right to hold those choices against him. But does digging up those memories right now help you feel better?":
                            n "She grows quiet for a moment."
                            l "No, not at all..."
                            menu:
                                "Then maybe you could try telling a postive story next time? To see if it makes you feel any better?":
                                    l "I suppose I could give it a shot..."
            $ kokiri_conversation_silent()

label askAboutDavid_tellMeAbout_2:
            l "David loves all things related to cryptography."
            l "When he still lived with us he would give me a a postcard for every birthday."
            l "That postcard had an encoded message on it."
            l "Then I had to decipher the code to reveal a list of cryptic instructions that would lead me to a gift."
            l "Sort of like a scavenger hunt I suppose."
            l "I liked it a lot to be honest. It felt as if we had a sort of hidden language to communicate in with eachother."
            menu:
                "I haven't heard you talk about a lot of happy memories with your father, how does sharing that story make you feel?":
                    l "I was a bit hesitant to tell this story because of the pain it might make me feel but I'm actually glad I told it."
                    l "It felt... kind of good? Almost as if everything was back the way it used to be."
                    l "It's been so many years since I last got a postcard from him that the memory of that ever happening is almost getting a bit fuzzy."
                    n "[persistent.date] starts sobbing."
                    l "I'm sorry to unload all of that on you [persistent.name], you don't deserve this."
                    menu:
                        "I understand that you feel like that Lillith but I don't mind at all. Besides, you deserve someone who can listen to you.":
                            n "[persistent.date] is still crying quite hard but you can see a slight smile forming."
                            l "I... suppose you're right [persistent.name]. That is really sweet of you. Thank you."
                            l "I just... need a moment to compose myself."
                            n "[persistent.date] plants her head on top of her knees and stays like that for a long while."
                            n "You can still hear her sobbing but it seems to grow more quiet over time."
                            l "There, I'm feeling a bit better already!"
                            l "Honestly, crying like that might be exactly what I needed."
                            l "Thank you for comforting me [persistent.name]! I really appreciate it."
                            l "Knowing that we don't have unlimited time makes me really thankful that you chose to spend that time to make sure I was okay."
                            $ kokiri_conversation += 1
                            $ love_points += 2 #This gains you 2 love points but as a sacrifice you lose an additional topic to talk about.
                            $ love_meter_updater(False)
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
    l "So I told you a little about [persistent.date_ghost] before, right?"
    n "She glances at you, hesitating briefly."
    l "But if I start repeating myself, please stop me, okay?"
    l "[persistent.date_ghost] was the best brother I could’ve ever asked for."
    n "Her voice softens, and you can see a faint, bittersweet smile cross her face."
    l "It still feels strange to talk about him in the past tense, even after all these years."
    l "Sometimes I forget he’s gone... just for a moment. And in those moments, he feels so close, like he’s right there with me."
    n "She pauses, her gaze drifting as if she's seeing him right in front of her."
    l "Sometimes, I picture him sitting at the kitchen table, waiting with this huge grin, his mouth completely covered in maple syrup as he devours pancakes."
    n "She laughs softly, but there’s a catch in her voice."
    l "But then I walk in and... he’s not there. It’s just the empty chair, the smell of pancakes fading, and it feels like a piece of me fades with it."
    l "I know it sounds silly, especially now that I live in my own place—it’s not even the same kitchen we grew up in."
    l "But... I still leave a chair open for him, every morning."
    menu:
        "It's not silly at all, [persistent.date]. I think it's beautiful. Grief doesn’t follow a time-limit, and neither does love. Everyone grieves in their own way, and there’s nothing wrong with yours.":
            $ kokiri_griefHasNoTimeLimit = True
            l "Wow, [persistent.name]... I don’t know what to say."
            l "I’ve never really thought about it that way before. That’s... incredibly kind of you to say."
            l "Sometimes I feel like no one really understands why I still miss him so deeply, like they think I should have moved on by now."
            l "But [persistent.date_ghost] and I had a bond that went beyond time. It still does."
            l "I guess this is my way of keeping him close, even if he’s not here anymore."
            l "Thank you for helping me see that... it's not silly. It’s just my way of honoring him."
            n "[persistent.date] smiles at you, a mix of relief and gratitude softening her expression."



label askAboutJames_tellMeAbout_2:

    l "[persistent.date_ghost] used to love photography and everything that came with it. So did I actually."
    l "Our father used to be a fan of photography and I think he passed that over to us."
    l "Well nowadays I don't really take pictures anymore. Everythime I tried to pick up a camera I just get reminded of both [persistent.date_ghost] and my fath- and David."
    l "I have dropped quite a few camera's when I tried to continue. I think it's for the best if I just stop for now."
    l "But [persistent.date_ghost] was extremely good for his age, he always was a quick learner but something about photography just seemed to click fantastically with him."
    l "It was almost as if you could just jump into his pictures and live inside of them."
    l "He used to tell me that a good picture should not just let the person watching it see a moment caught in time but it should also make them envision the future."
    l "In other words, a good picture should almost become a video with the picture as it's first frame."
    l "Personally I aways thought the oposite, a good picture makes you remember the lead-up to that picture, so in a way a good picture is a video with the picture as it's last frame."
    l "I think that's the only reason I can look at a picture of [persistent.date_ghost] without tearing up completely. I just see the lead-up to the picture and not the horifying aftermath of it all."
    l "However badly the memory of the aftermath still haunts me, I can't let that be the only part of his life I remember. I want to make sure all the beautiful memories we made throughout all the years will live on as long as possible."
    menu:
        "I think that is beautiful, I will make sure that [persistent.date_ghost] and the stories you two shared won't go forgotten.":
            n "[persistent.date] gives you a sincere smile."
            n "The stars shine enough light on her face for you to catch a tear rolling over her cheek."
            l "Thank you [persistent.name]! That would mean a lot to me."
            l "Even if I don't make it to the end of this day, you will."
            l "Atleast the memories of [persistent.date_ghost] won't end up dying with me."
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
        l "Suddenly [persistent.date_ghost] popped out of the corn."
        l " I think I screamed pretty loudly."
        n "[persistent.date] chuckles as she relives that moment."
        l "Then he picked me up while he spun around."
        l "He then put me down and layed down between the corn."
        l "I layed down beside him and we just looked at the sky while talking about all sorts of things."
        l "I wish I could remember what exactly we talked about but sadly I've forgotten most of it."
        l "The only thing that sticks out now is how [persistent.date_ghost] looked at the world."
        l "To me it always seemed as if he was somehow more in tune with the world than most people."
        l "Like for example, he looked at very ordinary things like a tree or the sky with so much love in his eyes."
        l "It was almost as if he saw them for the very first time each time he saw them."
        l "I think that's why he loved photography, he wanted others to see the world like he saw it."
        l "I really tried to keep seeing the world like him, especially after he..."
        n "She pauses for a moment before she continues."
        l "But it was very hard for me at that time, I felt terrible, everything around me felt terrible to see or do."
        l "I'd like to think that the only reason I got through it all is my family."
        l "That I kept fighting it for them."
        l "That they tried their best to help me through it, even if they didn't know exactly what I was going through."
        l "But truth be told, I think I also owe that to myself, to never truly giving up. When I gave up I eventually tried again."
        l "You see [persistent.name], there is no shame in giving up sometimes. Everyone does that now and then. What is really important is remembering that that says nothing about you, that one loss isn't your defeat."
        l "You can still win some smaller battles, and maybe, just maybe, one day you will win the war."
        l "I won that war, although some days, some weeks, I am back on that battlefield."
        l "But now I'm happy to say that I really can see the world like [persistent.date_ghost]. I can appreciate all the little things, because every day I have now is one that I wouldn't have seen if I truly was defeated."
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

    l "She had to deal with [persistent.date_ghost]' death and David leaving all of us."
    l "She basically raised both me and [persistent.date] ever since David left."
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
                li "Is everything alright [persistent.date_nickname]?"
                li "Did your date not go well?"
                l "Oh no, everything went-"
                l "Everything is going great!"
                li "Oh... that's fantastic news!"
                li "{size=*2}But doesn't that mean that your date can hear our call?{/size}"
                l "Oh no, it's fine, [persistent.name] just went to the toilet, so we have some time."
                n "[persistent.date] gives you a wink, it's a lie but you're impressed how convincing she made it sound."
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
                li "But when I see you and [persistent.date_sis_nickname], I can't help but smile. Because I know all of my work has been worth it."
                li "Every grey hair has been worth it."
                li "The two of you are my greatest treasure. And so was [persistent.date_ghost]. "
                li "... And so is [persistent.date_ghost]."
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
                l "[persistent.date] gives you a questioning look, she seems unsure of what to say."
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
                        n "[persistent.date_mom] seems to be in a panicked state."
                        l "Mom, I don't have much time, please take some deep breaths and try to calm down a bit, I know it is way too much to take all at once, but can you do that for me?"
                        li "I... Yes I can sweetie."
                        n "She takes such deep breaths in and out that you can hear it through the phone."
                        li "Is there anything I can do to help? Something that can fix all of this?"
                        l "I'm afraid nothing can fix this... You've already done enough, you helped me ease my mind a bit."
                        l "Not to forget that you took care of me so wondefully all my life."
                        l "Thank you mom."
                        l "I love you."
                        l "Please take good care of [persistent.date_sis_nickname] alright?"
                        l "She will be all that's left."
                        li "You'll never be fully gone sweetie, never fully forgotten."
                        li "Me and [persistent.date_sis_nickname] will always remember you."
                        li "Just like [persistent.date_ghost]."
                        l "I'd like that..."
                        l "maybe I will get to see him soon."
                        l "I will never forget both of you aswell."
                        li "If you see [persistent.date_ghost]... can you tell him I still think about him all the time?" 
                        $ persistent.LilaStillThinksAboutJames_knowledge = True
                        l "I'm sure he knows mom... but I will tell him."
                        n "You motion to [persistent.date] that she doesn't have much time left."
                        l "I'm going to hang up now mom, what comes next won't sound pretty..."
                        l "I love you."
                        
                    "*Shake your head*":
                        n "She nods, this is too much to burden her mom with."
                        l "Well, I used to ask you about it when I was younger but you never really answered my question."
                        l "And I guess my date with [persistent.name] inspired me to give you a call about it."
                        li "Did I?... I'm so sorry I did [persistent.date_nickname], I guess even then I was trying to protect you in my own way."
                        li "I hope you never were angry with me because of that."
                        li "Seeing how even after all this time, you still remember that happening..."
                        li "It must have affected you very deeply."
                        l "It's alright mom, I'm fine."
                        l "You said I was good at figuring out people, right?"
                        l "Well, I always knew that you loved us, that you tried to do what you thought was right for us."
                        l "So how could I ever be mad at that?"
                        l "So how could I ever be mad at you?"
                        li "[persistent.date_nickname]... thank you. I ...I don't really know what to say."
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
                        n "And with that [persistent.date]'s mom hung up the phone."
                jump kokiri_death_3_death_dialogue
            else:
                n "[persistent.date] won't have enough time to call if she calls now."
                n "I suggest talking about the same thing again as quickly as possible the next time."
                n "Let's just talk about something else to her for now."
                jump kokiri_talkAboutSomethingElse

label askAboutLila_tellMeAbout_2:
    #TODO: Rewrite this story eventually once it is finished. Especially don't make it start with "you know"
    l "You know, my mom is actually quite naive."
    l "[persistent.date_sis_nickname] and I like to make fun of her for being too trusting."
    l "It's a beautiful quality of her to be entirely fair but sometimes she just takes it way too far."
    l "I remember this one time where she got a mail from someone claiming to be a rich relative from Canada."
    l "They said that they were going to soon die and that mom was the nearest heir of his fortune." #TODO: Slightly rewrite this story as it's a bit weird [persistent.date_mom] would be estatic by someone dying.
    l "Mom was kind of ecstatic, after dad, I mean David, left us money has always been rather tight."
    l "She even had to work two jobs just to be able to take care of us."
    $ persistent.lilaWorkedTwoJobs_knowledge = True 
    l "So the prospect of being able to get more money to support us probably increased her trust in the situation."
    l "The \"rich relative from Canada\" said they just needed her to send a hundred euros so he could send her his fortune."
    l "Luckily my mom might be naive but she is not dimwitted."
    l "She asked that guy to just withdraw the hundred euros he needed from her inheritance, that way she would not need to pay the sum."
    l "Of course he didn't agree with that, she found it strange but a part of her still wanted to believe the whole story."
    l "Luckily I remember her asking me what I thought about the mail."
    l "I still was quite young but luckily [persistent.date_ghost] had given me a bunch of tips on how to be safe online."
    l "I told mom that it was probably a scammer trying to get her money."
    l "I still remember her being visibly heartbroken by that for a moment when I explained to her what scammers where."
    l "It was almost as if she never had considered the possibility of someone betraying someone else like that."
    l "Which is quite strange considering David had left all of us before that happened."
    #TODO: Add some choices here.
    menu: 
        "Maybe she understood why he left? Maybe she had forgiven him because she still loves him?":
            l "..."
            l "Maybe..."
            l "She is quite naive like I just mentioned afterall. So it wouldn't be out of the ordinary for her to forgive him."
            l "I'm sure even to this day she would still welcome him with open arms if he ever came back."
            menu:
                "Would you?":
                    n "Lilith goes silent for what feels like a minute or five."
                    l "..."
                    l "Look. Don't get me wrong, there was a time when I hoped he would come back."
                    l "Not a day went by without me thinking about it at least three times."
                    l "But every day that he kept hiding away slowly made my disillusions fade away."
                    l "He is not coming back."
                    l "So I honestly don't like to think about your question, no use in even entertaining the hypothetical that he might come back."

                "It makes sense, he is family afterall.":
                    l "I always got a double feeling when hearing that word, \"family\"."
                    l "If you think that family should always forgive eachother that is totally fine."
                    l "But to me that couldn't be further from the truth."
                    l "We say that family should be cared for, should be protected."
                    l "But what if someone in your family hurts other people in it?"
                    l "And what if those people are more important to you?"
                    l "Are you then just supposed to forgive and accept what they did to your family?"
                    l "Am I supposed to just sit and smile as I watch them destroy everything I care for?"
                    n "She grows quiet for a moment."
                    l "I'm sorry if that was too much [persistent.name]. I just kind of needed to vent about that for a second."
                    l "Family is something really important to me, but I think you should be free to choose who falls under that term."
                    l "Family can be so much more than just bloodrelations, and it doesn't have to be all of those."
                    l "To me a family will always be the people that I care for and that care for me."
    
    $ kokiri_conversation_silent()

label askAboutLila_tellMeAbout_3:
    #TODO: Rewrite more and put in more stuff.
    l "You know my mom actually really likes to play games. She has a ton of different consoles that she used to collect as a teenager."
    l "Some of my earliest memories were sitting on the couch and watching mom showing one of her games to both [persistent.date_ghost] and me."
    l "And later along [persistent.date_sis_nickname] was there aswell of course, she also loved watching mom play games. After a while me and [persistent.date_ghost] were playing and [persistent.date_sis] was watching us alongside mom."
    l "I used to be more into games than [persistent.date_ghost] but [persistent.date_sis] took the cake. Her eyes were glued to the screen whenever we would play and as soon as she could read she started playing some of mom's old games alongside [persistent.date_ghost] and me."
    l "She actually was allowed to play earlier but she wanted to understand the story of the games all on her own. She always used to see the games not as just pure entertainment but as worlds of their own, just like ours."
    l "And now she sometimes likes to make her own games. I'm happy that mom taking care of us resulted in a new hobby for [persistent.date_sis_nickname]."
    l "We kept playing games together, even after [persistent.date_ghost]'... death. In a way it made us very connected."
    l "We all are lucky to have a mom like that."
    #TODO: Add some extra choices. (Saying she indeed has a great mother etc.)
    $ kokiri_conversation_silent()
