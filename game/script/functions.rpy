
label gdwl_functions:
    init python:
        def love_meter_result():
            if love_meter <= 0:
                #Check for the location to send to the right place.
                if kokiri == True:
                    renpy.jump("kokiri_angryLilith")
                elif beach == True:
                    "Filler"
                    #TODO: Make an angry Lilith beach part once you start working on the beach.
                else:
                    renpy.jump ("car_death")
        def love_meter_updater():
            global love_points
            global love_meter
            global minor_love_offence
            global major_love_offence
            global minor_love_comfort
            global major_love_comfort
            #TODO: Check if the code below with the persistent counters works.
            love_meter = love_points + love_meter
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
            love_meter_result()


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
                    fam_obsession = "James"
                elif james_obsession == True:
                    fam_obsession = "James"
                    only_one_asked = True
                    fam_pronoun = "him"

                elif david_interest == True:
                    fam_obsession = "David"
                elif david_obsession == True:
                    fam_obsession = "David"
                    only_one_asked = True
                    fam_pronoun = "him"

                elif abigail_interest == True:
                    fam_obsession = "Abigail"
                elif abigail_obsession == True:
                    fam_obsession = "Abigail"
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
                    if fam_obsession == "James":
                        renpy.say(l, "You haven't been using info about him to try to \"win\" the game, right?")

                    else:
                        renpy.say(l, "You haven't involved [fam_pronoun] in all of this yet, right?")


                else:
                    if fam_obsession == True:
                        renpy.say (l, "You know, you seem to have quite an interest in my family, [fam_obsession] in particular.")
                        if fam_obsession == "James":
                            renpy.say (l, "You haven't been using info about him and my family to try to \"win\" the game, right?")
                        else:
                            renpy.say (l, "You haven't involved [fam_pronoun] or anyone else in all of this yet, right?")

                    else:
                        renpy.say (l, "You know, you seem to have quite an interest in my family.")
                        renpy.say (l, "You haven't involved them yet in all of this, right?")
                        no_fam_obsession = True

                if fam_obsession == "David":
                    renpy.say(l, "I don't want to have anything to do with him ever again or I atleast don't want to have him involved in any of this.")
                elif fam_obsession == "Lila":
                    renpy.say (l, "I don't want to involve her in any of this. She has looked out for me for my entire life [name]")
                    renpy.say (l, "She doesn't deserve to be dragged into this mess.")
                elif fam_obsession == "Abigail":
                    renpy.say(l, "I don't want to involve her [name]. She means too much to me and I would hate to make her go through the same situation we are currently in.")
                else:
                    renpy.say(l, "It doesn't really impact them directly, I am the only one that keeps dying so I think it's better to leave them out of this mess.")

                if no_fam_obsession == True:
                    renpy.say (l, "Lilith studies your face, seemingly in an attempt to gauge your reaction to her next question.")
                    renpy.say (l, "You haven't involved them yet.... have you?")
                else:
                    if james_involved:
                        if fam_obsession == "James":
                            renpy.say(l, "Although I am fine with sharing stories about James I don't want you to use any memories of him to further benefit you.")
                            renpy.say (l, "It already hurts enough just to have to live with these memories.")
                            if only_one_asked == True:
                                renpy.say(l, "Lilith studies your face, seemingly in an attempt to gauge your reaction to her next question.")
                                renpy.say (l, "You haven't used anything James-related to your befit yet... have you?")
                                persistent.abusedJamesInfo_knowledge = True

                            else:
                                renpy.say (l, "I would also prefer it if you didn't involve anyone of my family into this.")
                                renpy.say(l, "Lilith studies your face, seemingly in an attempt to gauge your reaction to her next question.")
                                renpy.say (l, "You haven't involved anyone yet.... have you?")
                        else:
                            renpy.say (l, "And although I am fine with sharing stories about James I don't want you to use any memories of him to further benefit you. It already hurts enough just to have to live with these memories.")

                renpy.jump("didYouInvolveFamily")

        def family_curiosity_checker_movetox(): #This function moves you back to the right story about Lilith's family if you promise to not use them for your own gain.
            if kokiri_chatchar_abigail_recent == True:
                renpy.jump("askAboutAbigail_tellMeAbout_" + str(kokiri_chatchar_abigail_counter))

            elif kokiri_chatchar_david_recent == True:
                renpy.jump("askAboutDavid_tellMeAbout_" + str(kokiri_chatchar_david_counter))


            elif kokiri_chatchar_james_recent == True:
                renpy.jump("askAboutJames_tellMeAbout_" + str(kokiri_chatchar_james_counter))

            elif kokiri_chatchar_lila_recent == True:
                renpy.jump("askAboutLila_tellMeAbout_" + str(kokiri_chatchar_lila_counter))

        def kokiri_conversation_silent():
            kokiri_meteoritewarn()
            if kokiri_conversation == 2:
                if kokiri_meteorite_alert or kokiri_alternateplace == True: #The meteorite doesn't hit Lilith.
                    renpy.jump("kokiri_death_1_prevented")
                else:
                    renpy.jump("kokiri_death_1")

            else:
                renpy.say (n, "Lilith grows quiet for a moment. She seems to be waiting on you to say something.") #TODO: (change this line)
                #TODO: Make this line also change depending on the meteorite and the car, check the kokiri_conversation value.If the kokiri chat value is 2 this can jump to the scne where she notices the meteorite.
                renpy.jump("silentconversationsbackontrack")

        def kokiri_call_potentialdeathcheck():
            global kokiri_call_death_1_check
            global kokiri_call_death_2_check
            persistent.kokiri_call_death = True
            if kokiri_alternateplace == True:
                #The meteorite death check is not needed here, it is very far from her.
                #The car one does happen though.

                renpy.say (n, "The same meteorite that had previously ended up cutting your date with Lilith short now passes by her, un-noticed as it breaks into several smaller pieces." )
                renpy.say (n, "They spreads across the entire forest, none of them landing even near her.")
                renpy.say (n, "You can't help but smile at the thought.")
                renpy.say (n, "Lilith is so focussed on her conversation that she can't even suspect her past death.")
                renpy.say (n, "You think it's better that way, ignorance is bliss.")
                if car_caught == True:
                    renpy.say (n, "While Lilith is engrossed in her conversation you notice the Red-Sedan isn't showing up. Looks like your call to the police worked wonderfully.")
                else:
                    kokiri_call_death_2_check = True
                    renpy.jump("kokiri_death_2")
            else:
                if kokiri_meteorite_alert == True:
                    renpy.say (n, "The meteorite breaks into many different parts that spread all around the forest. One of them lands right where Lilith was sitting.")
                    renpy.say (n, "For a brief moment you are reminded of the horible state she was in when it hit her head.")
                    renpy.say (n, "You try to shake the feeling it gives you away and you half-succeed.")
                    renpy.say (n, "Lilith looks at you with visible shock in her eyes, knowing that she doesn't have much time left you point at the phone and motion her to continue calling.")
                    renpy.say (n, "She nods and frowns slightly, she understands very well what you are not saying directly but thinking nontheless.")
                    renpy.say (n, "The end is near.")
                    renpy.say (n, "Her end is near.")
                    renpy.say (n, "It might not be the meteorite.")
                    renpy.say (n, "It might not be right now.")
                    renpy.say (n, "But it will be something else.")
                    renpy.say (n, "It will happen soon.")
                    if car_caught == True:
                        renpy.say (n, "While Lilith is engrossed in her conversation you notice the Red-Sedan isn't showing up. Looks like your call to the police worked wonderfully.")

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
                        renpy.say(n, "Suddenly you are plagued with a vision of the meteorite that killed Lilith. You should probably try to warn her this time.", interact=False)
                        met_check = renpy.display_menu([("You might want to sit on my right instead of my left first. Something's coming soon.","meteorite_warn"),("*Don't warn her.*","no_meteorite_warn")])
                        if met_check == "meteorite_warn":
                            renpy.say (n, "Lilith gives you a nod as she moves to the other side of the blanket, to your left.")
                            renpy.say (l, "That's a bit of an odd request but I guess I will see why I needed to do that soon enough, right?")


                            kokiri_meteorite_alert = True
                        else:
                            kokiri_meteorite_no_alert = True


    jump after_setup
