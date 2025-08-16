
label gdwl_functions:
    init python:
        def love_meter_result(alwaysJump):
            if love_meter <= 0 or alwaysJump == True:
                #Check for the location to send to the right place.
                if kokiri == True:
                    renpy.jump("angryLilith")
                elif beach == True:
                    "Filler"
                    #TODO: Make an angry [persistent.date] beach part once you start working on the beach.
                else:
                    renpy.jump ("car_death")
        def love_meter_updater(alwaysJump):
            global love_points
            global love_meter
            global minor_love_offence
            global major_love_offence
            global minor_love_comfort
            global major_love_comfort
            love_points = 2
            love_meter += love_points
            if love_points == -1:
                minor_love_offence += 1
                persistent.minor_love_offence_counter += 1
            elif love_points <= -2:
                major_love_offence += 1
                persistent.major_love_offence_counter += 1

            if love_points == 1:
                minor_love_comfort += 1
                persistent.minor_love_comfort_counter += 1
            elif love_points >= 2:
                major_love_comfort += 1
                persistent.major_love_comfort_counter += 1
            love_points = 0
            if alwaysJump == True:
                love_meter_result(True)
            else:
                love_meter_result(False)


        def family_curiosity_checker():
            global family_ask
            global james_interest
            global james_obsession
            global david_interest
            global david_obsession
            global lila_interest
            global lila_obsession
            global abigail_interest
            global abigail_obsession
            global fam_obsession
            global fam_pronoun
            global no_fam_obsession
            global james_involved
            family_ask += 1
            if family_ask == 3:
                family_ask = 0
                if kokiri_chatchar_abigail == True:
                    if kokiri_chatchar_abigail_counter == 2:
                        abigail_interest = True

                    elif kokiri_chatchar_abigail_counter == 3:
                        abigail_obsession = True
                elif kokiri_chatchar_david == True:
                    if kokiri_chatchar_david_counter == 2:
                        david_interest = True

                    elif kokiri_chatchar_david_counter == 3:
                        david_obsession = True
                elif kokiri_chatchar_james == True:
                    if kokiri_chatchar_james_counter == 2:
                        james_interest = True

                    elif kokiri_chatchar_james_counter == 3:
                        james_obsession = True
                elif kokiri_chatchar_lila == True:
                    if kokiri_chatchar_lila_counter == 2:
                        lila_interest = True

                    elif kokiri_chatchar_lila_counter == 3:
                        lila_obsession = True





                if james_interest == True:
                    fam_obsession = "[persistent.date_ghost]"
                elif james_obsession == True:
                    fam_obsession = "[persistent.date_ghost]"
                    only_one_asked = True
                    fam_pronoun = "him"

                elif david_interest == True:
                    fam_obsession = "David"
                elif david_obsession == True:
                    fam_obsession = "David"
                    only_one_asked = True
                    fam_pronoun = "him"

                elif abigail_interest == True:
                    fam_obsession = "[persistent.date_sis]"
                elif abigail_obsession == True:
                    fam_obsession = "[persistent.date_sis]"
                    only_one_asked = True
                    fam_pronoun = "her"

                elif lila_interest == True:
                    fam_obsession = "mom"
                elif lila_obsession == True:
                    fam_obsession = "mom"
                    only_one_asked = True
                    fam_pronoun = "her"

                if only_one_asked == True:

                    renpy.say(l, "You know, you seem to have quite an interest in [fam_obsession].")
                    if fam_obsession == "[persistent.date_ghost]":
                        renpy.say(l, "You haven't been using info about him to try to \"win\" the game, right?")

                    else:
                        renpy.say(l, "You haven't involved [fam_pronoun] in all of this yet, right?")


                else:
                    if fam_obsession == True:
                        renpy.say (l, "You know, you seem to have quite an interest in my family, [fam_obsession] in particular.")
                        if fam_obsession == "[persistent.date_ghost]":
                            renpy.say (l, "You haven't been using info about him and my family to try to \"win\" the game, right?")
                        else:
                            renpy.say (l, "You haven't involved [fam_pronoun] or anyone else in all of this yet, right?")

                    else:
                        renpy.say (l, "You know, you seem to have quite an interest in my family.")
                        renpy.say (l, "You haven't involved them yet in all of this, right?")
                        no_fam_obsession = True

                if fam_obsession == "David":
                    renpy.say(l, "I don't want to have anything to do with him ever again or I atleast don't want to have him involved in any of this.")
                elif fam_obsession == "[persistent.date_mom]":
                    renpy.say (l, "I don't want to involve her in any of this. She has looked out for me for my entire life [persistent.name]")
                    renpy.say (l, "She doesn't deserve to be dragged into this mess.")
                elif fam_obsession == "[persistent.date_sis]":
                    renpy.say(l, "I don't want to involve her [persistent.name]. She means too much to me and I would hate to make her go through the same situation we are currently in.")
                else:
                    renpy.say(l, "It doesn't really impact them directly, I am the only one that keeps dying so I think it's better to leave them out of this mess.")

                if no_fam_obsession == True:
                    renpy.say (l, "[persistent.date] studies your face, seemingly in an attempt to gauge your reaction to her next question.")
                    renpy.say (l, "You haven't involved them yet.... have you?")
                else:
                    if james_involved:
                        if fam_obsession == "[persistent.date_ghost]":
                            renpy.say(l, "Although I am fine with sharing stories about [persistent.date_ghost] I don't want you to use any memories of him to further benefit you.")
                            renpy.say (l, "It already hurts enough just to have to live with these memories.")
                            if only_one_asked == True:
                                renpy.say(l, "[persistent.date] studies your face, seemingly in an attempt to gauge your reaction to her next question.")
                                renpy.say (l, "You haven't used anything [persistent.date_ghost]-related to your befit yet... have you?")
                                persistent.abusedJamesInfo_knowledge = True

                            else:
                                renpy.say (l, "I would also prefer it if you didn't involve anyone of my family into this.")
                                renpy.say(l, "[persistent.date] studies your face, seemingly in an attempt to gauge your reaction to her next question.")
                                renpy.say (l, "You haven't involved anyone yet.... have you?")
                        else:
                            renpy.say (l, "And although I am fine with sharing stories about [persistent.date_ghost] I don't want you to use any memories of him to further benefit you. It already hurts enough just to have to live with these memories.")

                renpy.jump("didYouInvolveFamily")

        def family_curiosity_checker_movetox(): #This function moves you back to the right story about [persistent.date]'s family if you promise to not use them for your own gain.
            if familyCheck_talkedDavid == True:
                renpy.say (l, "Now that that is cleared up, what would you like to talk about [persistent.name]?")
                renpy.jump("talkKokiri")
            if kokiri_chatchar_abigail_recent == True:
                renpy.jump("askAboutAbigail_tellMeAbout_" + str(kokiri_chatchar_abigail_counter))

            elif kokiri_chatchar_david_recent == True:
                renpy.jump("askAboutDavid_tellMeAbout_" + str(kokiri_chatchar_david_counter))


            elif kokiri_chatchar_james_recent == True:
                renpy.jump("askAboutJames_tellMeAbout_" + str(kokiri_chatchar_james_counter))

            elif kokiri_chatchar_lila_recent == True:
                renpy.jump("askAboutLila_tellMeAbout_" + str(kokiri_chatchar_lila_counter))

        def kokiri_conversation_silent():
            kokiri_silentMoment = True
            kokiri_meteoritewarn()
            if kokiri_conversation == 2:
                if kokiri_meteorite_alert or kokiri_alternateplace == True: #The meteorite doesn't hit [persistent.date].
                    renpy.jump("kokiri_death_1_prevented")
                else:
                    renpy.jump("kokiri_death_1")

            else:
                renpy.say (n, "[persistent.date] grows quiet for a moment. She gives you an expecting look, as if she's waiting for you to say something.")
                renpy.jump("silentconversationsbackontrack")

        def kokiri_call_potentialdeathcheck():
            global kokiri_call_death_1_check
            global kokiri_call_death_2_check
            persistent.kokiri_call_death = True
            if kokiri_alternateplace == True:
                #The meteorite death check is not needed here, it is very far from her.
                #The car one does happen though.

                renpy.say (n, "The same meteorite that had previously ended up cutting your date with [persistent.date] short now passes by her, un-noticed as it breaks into several smaller pieces." )
                renpy.say (n, "They spreads across the entire forest, none of them landing even near her.")
                renpy.say (n, "You can't help but smile at the thought.")
                renpy.say (n, "[persistent.date] is so focussed on her conversation that she can't even suspect her past death.")
                renpy.say (n, "You think it's better that way, ignorance is bliss.")
                if car_caught == True:
                    renpy.say (n, "While [persistent.date] is engrossed in her conversation you notice the Red-Sedan isn't showing up. Looks like your call to the police worked wonderfully.")
                else:
                    kokiri_call_death_2_check = True
                    renpy.jump("kokiri_death_2")
            else:
                if kokiri_meteorite_alert == True:
                    renpy.say (n, "The meteorite breaks into many different parts that spread all around the forest. One of them lands right where [persistent.date] was sitting.")
                    renpy.say (n, "For a brief moment you are reminded of the horible state she was in when it hit her head.")
                    renpy.say (n, "You try to shake the feeling it gives you away and you half-succeed.")
                    renpy.say (n, "[persistent.date] looks at you with visible shock in her eyes, knowing that she doesn't have much time left you point at the phone and motion her to continue calling.")
                    renpy.say (n, "She nods and frowns slightly, she understands very well what you are not saying directly but thinking nonetheless.")
                    renpy.say (n, "The end is near.")
                    renpy.say (n, "Her end is near.")
                    renpy.say (n, "It might not be the meteorite.")
                    renpy.say (n, "It might not be right now.")
                    renpy.say (n, "But it will be something else.")
                    renpy.say (n, "It will happen soon.")
                    if car_caught == True:
                        renpy.say (n, "While [persistent.date] is engrossed in her conversation you notice the Red-Sedan isn't showing up. Looks like your call to the police worked wonderfully.")

                    else:
                        kokiri_call_death_2_check = True
                        renpy.jump("kokiri_death_2")
                else:
                    kokiri_call_death_1_check = True
                    renpy.jump("kokiri_death_1")


        def kokiri_meteoritewarn():
            #Put this function at the front of the continue talking
            global met_check
            global kokiri_meteorite_alert
            global kokiri_meteorite_no_alert
            global kokiri_conversation

            if kokiri_conversation == 2:
                if persistent.kokiri_death_1 == True:
                    if kokiri_alternateplace == False:
                        renpy.say(n, "Suddenly you are plagued with a vision of the meteorite that killed [persistent.date]. You should probably try to warn her this time.", interact=False)
                        met_check = renpy.display_menu([("You might want to sit on my right instead of my left first. Something's coming soon.","meteorite_warn"),("*Don't warn her.*","no_meteorite_warn")])
                        if met_check == "meteorite_warn":
                            renpy.say (n, "[persistent.date] gives you a nod as she moves to the other side of the blanket, to your left.")
                            renpy.say (l, "That's a bit of an odd request but I guess I will see why I needed to do that soon enough, right?")


                            kokiri_meteorite_alert = True
                        else:
                            kokiri_meteorite_no_alert = True

        def resetRegularFlags():


            # Set variables that need other default values
            globals()["love_meter"] = 3
            globals()["carDescription"] = ""
            globals()["changeableWord"] = ""
            globals()["dicenumber"] = 0
            globals()["dicenumber2"] = 0
            globals()["rw1"] = 0
            globals()["rw2"] = 0
            globals()["rw3"] = 0
            globals()["rw_total"] = 0
            globals()["family_ask"] = 0
            globals()["riddleAnswersTold"] = 0
            globals()["chinese_lilithBreakupTrigger"] = 0
            
            
            globals()["met_check"] = ""
            globals()["tracker"] = 0
            globals()["questmade"] = 0
            globals()["love_points"] = 0
            globals()["eastername"] = ""
            globals()["minor_love_comfort"] = 0
            globals()["minor_love_offence"] = 0
            globals()["major_love_comfort"] = 0
            globals()["major_love_offence"] = 0
            globals()["other_phone"] = 0


            global_vars = [
                "called_phone",
                "burger",
                "cafe",
                "chinese",
                
                "nightmare",
                "kokiri_cherishAllDates",
                "burgerBeforeLie",
                "abby_phoneToldSisDies",
                "kokiri_griefHasNoTimeLimit",
                "kokiri_groundhog_lie",
                "kokiri_psychic_lie",

                "car_caught",
                "car_free",
                "groundhog",
                "psychic", 
                "hugRequestedBeforeDeath", 
            
                # Locations:
                "burger_poem_cleancheck", 
                "burger", 
                "burgerBeenBefore", 
                "burger_alt", 
                "cafe", 
                "kokiri", 
                "beach", 
                "brotherasked", 
                "burger_nightmare",
                "kokiri_jamesTalkBlock",
                
                "cafedicecheat", 
                "cafe_badLove_lowbar", 
                "cafe_badLove_justafeeling", 
                "chinese", 
                "peking", 
                "orange", 
                
                "riddle_loop", 
                "kokiri", 
                "kokiri_groundhog_lie", 
                "kokiri_psychic_lie", 
                
                "poem_conversation", 
                "teaseDeath", 
                "angryLilith", 
                "kokiri_poemBad", 
                "kokiri_promiseCancelDate", 
                "abby_phoneToldSisDies", 

                "kokiri_poems_rated_once", 
                "kokiri_poems_rateblock", 
                "kokiri_alternateplace", 
                "kokiri_holdhand", 
                "kokiri_scenery_headhurt", 
                "kokiri_scenery_breakfrombreakingyourhead", 
                "kokiri_scenery_gamegoal", 
                "kokiri_meteorite_alert", 
                "kokiri_meteorite_no_alert", 
                "kokiri_finalTalk", 
                "kokiri_call_death_2_check", 
                "kokiri_call_death_1_check", 
                "kokiri_death_4_playerResponse", 
                "damoclesAsked", 
                "big_sis_mode", 
                "lilithAliveEnding", 
                "playerCalledSomeone", 
                "kokiri_positiveDavidStory",
                "kokiri_familyContacted",
                "kokiri_ToldLillyHowManyRetries,"
                
                
                "peeked_phone_temp",
                "kokiriStarGazed", #Check if you have watched the stars with [persistent.date] at a certain part of the game this run.
                "kokiriSceneryWatched", #Check if you have watched the scenery with [persistent.date] this run.
                "kokiri_scenery_shutUpLackOfSelfEsteem", 
            
                "kokiri_griefHasNoTimeLimit", 
                "kokiri_silentMoment", 
                #Kokiri recent poems
                "kokiri_poem_snowwoman_recent", 
                "kokiri_poem_shadowman_recent", 
                "kokiri_poem_lights_recent", 
                "kokiri_poem_bang_recent", 
                "kokiri_poem_window_recent", 
                #Booleans to see who you ask about the most at familyask in kokiri
                

                "kokiri_chatchar_abigail", 
                "kokiri_chatchar_james", 
                "kokiri_chatchar_lila", 
                "kokiri_chatchar_david", 
                "kokiri_call", 
                "james_interest", 
                "abigail_interest", 
                "david_interest", 
                "lila_interest", 
                "james_obsession", 
                "abigail_obsession", 
                "david_obsession", 
                "lila_obsession", 
                "no_fam_obsession", 
                "james_involved", 
                "kokiri_chatchar_abigail_recent",
                "kokiri_chatchar_james_recent", 
                "kokiri_chatchar_david_recent", 
                "kokiri_chatchar_lila_recent", 
                "familyCheck_talkedDavid",
                #CONVERSATION TRACKERS
                "conversationtracker_poems", 
                "conversationtracker_tellheraboutnarrator", 
                "conversationtracker_questmade", 
                
                "conversationtracker_abigail", 
                "conversationtracker_david", 
                "conversationtracker_james", 
                "conversationtracker_lila", 
                "conversationtracker_blamedavid", 
                "conversationtracker_poem_window", 
                "conversationtracker_poem_snowwoman", 
                "conversationtracker_poem_window", 
                "conversationtracker_poem_shadowman", 
                "conversationtracker_poem_lights", 
                "conversationtracker_poem_bang", 



                #Other flags
                "abby_askedAboutGameTheme", 
                "nmDetect", 
                "mDetect", 
                "hard_rude", 
                "easy_rude", 
                
                "demetrius", 
                "adriel", 
                "currentcar", 
                
                "booklovertalked", 
                "musiclovertalked", 
                "phone_wrongPassword_graceSystem", 
                "lilithAliveEnding", 
                "burger_explosion_outside", 
                "called_phone", 
            
                "rockMode", 
                "burger_jokeFromAbigailTold", 
                "onlyDates", 
                "kokiri_cherishAllDates", 
                "davidPromise", 

                #Beach
                "beachStart_doneBook", 
                "beachStart_doneDunes", 
                "beachStart_doneBeach", 
                "beachStart_doneFriterie", 
                "beachStart_doneIce", 
                "beachStart_doneCinema", 

                
            
                #QOL-settings:
                "no_nightmare", 
                "perm_nightmare", 
            ]

            for var in global_vars:
                globals()[var] = False

            

             
            
        
           
            
            
      
           
           
          
            
          
            
           
        
            
           
            
            
    jump after_setup

                


