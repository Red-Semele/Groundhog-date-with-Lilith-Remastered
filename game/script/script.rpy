﻿# The script of the game goes in this file.
#TODO: Add a morality counter you can use for a system where the player gets judged on their actions.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lilith")
define n = Character("Narrator")
define r = Character("[roseName]")
default roseName = "Old lady"
define b = Character("Barista")
define bs = Character("Bookstore lady")
define de = Character("Demetrius")
define ad = Character("Adriel")
define a = Character("Abigail")
define d = Character("David")
define j = Character("James")
define li = Character("Lila")
define q = Character("[mysteriousCallerName]")
default mysteriousCallerName = "James"
define p = Character("[persistent.name]")
define dev = Character("Developer")
define mt = Character("Mysterious Text")
define ship = Character("Ship")


















# The game starts here.
#I should have made all flags that need remembering end with "_knowledge" do this from now on for each such flag and also make the flags underneath this work like that and the if cases that check for these flags also need to be properly changed.
#The explanation text will also need a full file, maybe Kokiri will need multiple.


label start:
     

if persistent.firstboot == None: 
     
     #This line ensures all flags that don't need constant resetting get reset only the first time the player boots the game.
     default persistent.firstboot = True
     #Deaths:
     default persistent.lildeaths = 0
     default persistent.retry_counter = 0
     #Main restaurant deaths:
     default persistent.chinese_death_1 = False
     default persistent.cafe_death_1 = False
     default persistent.burger_death_1 = False
     default persistent.chinese_death_2 = False
     default persistent.cafe_death_2 = False
     default persistent.burger_death_2 = False
     #Car deaths under here:
     default persistent.chinese_car_death = False
     default persistent.cafe_car_death = False
     default persistent.burger_car_death = False
     default persistent.redSedan_knowledge = False #The knowledge check to see if the person has ever seen that car before or not.
     # Kokiri deaths under here:
     default persistent.kokiri_angryLilithDeath = True
     default persistent.kokiri_death_1 = False
     default persistent.kokiri_death_2 = False
     default persistent.kokiri_death_2_call = False
     default persistent.kokiri_death_2_alternate = False
     default persistent.kokiri_death_3 = False
     default persistent.kokiri_death_4 = False
     default persistent.kokiri_death_4_hill = False
     default persistent.kokiri_death_4_noHill = False
     default persistent.kokiri_death_4_hill_holdHand = False
     #Beach deaths under here:
     default persistent.beach_jelly_death = False
     default persistent.beach_hole_death = False
     default persistent. beach_pot_death = False
     default persistent.beach_slip_death = False

     #Knowledge:
     #Untold story knowledge:
     default persistent.story_start_knowledge = False
     default persistent.story_medium_knowledge = False
     default persistent.story_end_knowledge = False
     #Preventdeath explanation.
     default persistent.psychic_answer_right_knowledge = False
     default persistent.groundhog_answer_right_knowledge = False
     # Other knowledge
     default persistent.brother_knowledge = False
     default persistent.kokiri_abigailhidessomething_knowledge = False
     default persistent.kokiri_knowledge = False
     default persistent.joke_knowledge = False
     default persistent.car_knowledge = False
     default persistent.bedcheck_knowledge = False
     default persistent.ron_knowledge = False
     default persistent.quest_knowledge = False #If you read the about section this flag triggers.
     default persistent.reality_knowledge = False
     default persistent.bookpreference_knowledge = False #This will basically help you pick a book for Lilith she likes in the beach-bookstore.
     default persistent.booklover_knowledge = False
     default persistent.musiclover_knowledge = False
     default persistent.needProof_knowledge = False
     default persistent.dumbo_knowledge = False
     default persistent.drownRaven_knowledge = False
     default persistent.david_nolove_knowledge = False
     default persistent.david_blame_knowledge = False
     default persistent.david_love_knowledge = False
     default persistent.david_apology_knowledge = False
     default persistent.james_story_knowledge = False
     default persistent.jamesconversation_becomethegame_knowledge = False
     default persistent.tracker = 0 #Tracker 
     default persistent.tracker1 = False
     default persistent.tracker2 = False
     default persistent.tracker3 = False
     default persistent.easter_1 = False
     default persistent.easter_2 = False
     default persistent.easter_3 = False
     default persistent.plane_knowledge = False
     default persistent.teaseDeath_fakeOut_knowledge = False
     default persistent.dice_counter = 0
     default persistent.chineseRiddlesSeenXTimesCounter = 0
     default persistent.polaroidTracker = False
     default persistent.runAwayLilith_counter = 0
     
     #Phone-numbers
     default persistent.david_call_knowledge = False
     default persistent.abigail_call_knowledge = False
     default persistent.james_call_knowledge = False
     default persistent.lila_call_knowledge = False
     default persistent.playerCalledLila = False
     default persistent.playerCalledJames = False
     default persistent.playerCalledDavid = False
     default persistent.playerCalledAbigail = False
     #Beach flags.
     default persistent.beach_knowledge = False

     #Burger related flags and counters
     default persistent.burger_poem_knowledge = False
     default persistent.rosename_knowledge = False
     default persistent.burgerwent = 0
     default persistent.burgerstart = False
     #Cafe related flags and counters
     default persistent.cafe_taste_knowledge = False
     default persistent.dice_knowledge = False
     default persistent.song_knowledge = False
     #Chinese flags
     default persistent.chinese_phone_noretry = False #The noretry flags are meant to check if you replay the game after being asked not to do it.
     default persistent.pass_knowledge = False
     default persistent.need_pass_knowledge = False
     default persistent.peeked_phone = False
     #Chinese riddle flags
     default persistent.r1_knowledge = False
     default persistent.r2_knowledge = False
     default persistent.r3_knowledge = False
     #Kokiri flags
     default persistent.kokiri_teacher_knowledge = False
     default persistent.kokiri_call_death = False
     default persistent.restrainingorderfamily_violation_counter = 0
     default persistent.restrainingorderfamily_knowledge = False
     default persistent.kokiri_tellnolies_knowledge = False
     default persistent.fakeoutnar_tip = False
     default persistent.kokiri_determinism_knowledge = False
     default persistent.kokiri_newerPoems_knowledge = False
     default persistent.kokiri_heraclitus_knowledge = False
     default persistent.abusedJamesInfo_knowledge = False
     default persistent.doNotUseJames_knowledge = False
     default persistent.LilaStillThinksAboutJames_knowledge = False
     default persistent.kokiriWatchedStars = False
     default persistent.jamesFakoutNumber_knowledge = False
     default persistent.lilithKeepsCalling_knowledge = False
     default persistent.keptJamesNumber_knowledge = False
     default persistent.kokiri_angry_noretry = False
     default persistent.useGiftToFullExent_knowledge = False
     default persistent.kokiri_perfectMomentStarGaze_knowledge = False
     default persistent.kokiri_reachEndingForMe = False
     default persistent.kokiri_reachEndingForUs = False
     default persistent.kokiri_reachEndingForYou = False
     #Kokiri poems
     default persistent.kokiri_poem_window_knowledge = False
     default persistent.kokiri_poem_bang_knowledge = False
     default persistent.kokiri_poem_lights_knowledge = False
     default persistent.kokiri_poem_snowwoman_knowledge = False
     default persistent.kokiri_poem_shadowman_knowledge = False
     default persistent.kokiri_allOldPoemsRead = False
     default persistent.kokiri_allRecentPoemsRead = False
     default persistent.rp_detect = False #This flag will be used to try to check if a player is returning to the game after erasing their save-file.
     default persistent.met_james = False
     default persistent.passWrongOnPurpose_narratorRant_counter = 0
     default persistent.passWrongOnPurpose_narratorRant_wrongTimesInARowCounter = 0
     default persistent.passWrongOnPurpose_narratorRant = False
     
     #Beach:
     default persistent.beachroute_visited_knowledge = False
     #Endings:
     default persistent.ending_quitter = False
     default persistent.ending_anEnding = False
     default persistent.ending_unseenContent = False
     default persistent.ending_lettinggo = False
     default persistent.game_credits = False
     default persistent.ending_semiEnding = False
     default persistent.ending_abigailDistraction = True
     #Phone_menu sortring related stuff:
     default persistent.amount_of_folder_links = 0 #This checks how many sub links I created in the phone menu to avoid clutter.
     default persistent.restaurant_subfolder = False
     default persistent.other_subfolder = False
     default persistent.locations_subfolder = False
     default persistent.kokiri_unlock = False
     default persistent.beach_unlock = False
     default persistent.otherPlans_unlock = False
     default persistent.breakup_unlock = False
     default persistent.call_unlock = False
     default persistent.amount_of_normal_links = 0 #This checks how many non-sub links there are.
     default persistent.amount_of_normal_location_links = 0
     default persistent.amount_of_normal_other_links = 0
     default persistent.links_phone = 0
     default persistent.times_phone_declined = 0
     #Additional stuff:
     default persistent.minor_love_offence_counter = 0
     default persistent.major_love_offence_counter = 0
     default persistent.minor_love_comfort_counter = 0
     default persistent.major_love_comfort_counter = 0
     default persistent_jamestalk_ilikeher_knowledge = False
     default persistent_jamestalk_iloveher_knowledge = False
     default persistent_jamestalk_justgame_knowledge = False
     default persistent_fleeingDeaths_counter_knowledge = 0
     default persistent.lilithAliveAndRetriedCounter = 0
     default persistent.narratorMonologue_dicePuzzleIntentionalyFailed = False
     default persistent.abigail_numberfakeout = False
#NON-PERSISTENT FLAGS
label resetRegularFlags:
     $ car_caught = False
     $ car_free = False
     $ groundhog = False
     $ psychic = False
     $ hugRequestedBeforeDeath  = False
     $ carDescription = ""
     $ changeableWord = ""
     # Locations:
     $ burger_poem_cleancheck = False
     $ burger = False
     $ burger_alt = False
     $ cafe = False
     $ kokiri = False
     $ beach = False
     $ brotherasked = 0
     $ dicenumber = 0
     $ dicenumber2 = 0
     $ cafedicecheat = False
     $ cafe_badLove_lowbar = False
     $ cafe_badLove_justafeeling = False
     $ chinese = False
     $ peking = False
     $ orange = False
     $ rw1 = 0
     $ rw2 = 0
     $ rw3 = 0
     $ rw_total = 0
     $ riddle_loop = False
     $ kokiri = False
     $ kokiri_groundhog_lie = False
     $ kokiri_psychic_lie = False
     $ family_ask = 0
     $ poem_conversation = False
     $ teaseDeath = False
     $ angryLilith = False

     $ kokiri_poems_rated_once = False
     $ kokiri_poems_rateblock = False
     $ kokiri_alternateplace = False
     $ kokiri_holdhand = False
     $ kokiri_scenery_headhurt = False
     $ kokiri_scenery_breakfrombreakingyourhead = False
     $ kokiri_scenery_gamegoal = False
     $ kokiri_meteorite_alert = False
     $ kokiri_meteorite_no_alert = False
     $ kokiri_finalTalk = False
     $ kokiri_call_death_2_check = False
     $ kokiri_call_death_1_check = False
     $ big_sis_mode = False
     $ lilithAliveEnding = False
     $ playerCalledSomeone = False
     $ riddleAnswersTold = 0
     $ peeked_phone_temp = False
     $ kokiriStarGazed = False #Check if you have watched the stars with Lilith at a certain part of the game this run.
     $ kokiriSceneryWatched = False #Check if you have watched the scenery with Lilith this run.
     $ kokiri_scenery_shutUpLackOfSelfEsteem = False
     $ met_check = "" #A check for the meteorite warning system.
     #TODO: Add the other recent poem checkers below here.
     $ kokiri_poem_snowwoman_recent = False
     $ kokiri_poem_shadowman_recent = False
     $ kokiri_poem_lights_recent = False
     $ kokiri_poem_bang_recent = False
     $ kokiri_poem_window_recent = False
     #Booleans to see who you ask about the most at familyask in kokiri
     $ family_ask = 0

     $ kokiri_chatchar_abigail = False
     $ kokiri_chatchar_james = False
     $ kokiri_chatchar_lila = False
     $ kokiri_chatchar_david = False
     $ kokiri_call = False
     $ james_interest = False
     $ abigail_interest = False
     $ david_interest = False
     $ lila_interest = False
     $ james_obsession = False
     $ abigail_obsession = False
     $ david_obsession = False
     $ lila_obsession = False
     $ no_fam_obsession = False
     $ james_involved = False
     $ kokiri_chatchar_abigail_recent = False
     $ kokiri_chatchar_james_recent = False
     $ kokiri_chatchar_david_recent = False
     $ kokiri_chatchar_lila_recent = False
     #CONVERSATION TRACKERS
     $ conversationtracker_poems = False
     $ conversationtracker_tellheraboutnarrator = False
     $ conversationtracker_questmade = False
     $ questmade = 0
     $ conversationtracker_abigail = False
     $ conversationtracker_david = False
     $ conversationtracker_james = False
     $ conversationtracker_lila = False
     $ conversationtracker_blamedavid = False
     $ conversationtracker_poem_window = False
     $ conversationtracker_poem_snowwoman = False
     $ conversationtracker_poem_window = False
     $ conversationtracker_poem_shadowman = False
     $ conversationtracker_poem_lights = False
     $ conversationtracker_poem_bang = False



     #Other flags
     $ nmDetect = False
     $ mDetect = False
     $ hard_rude = False
     $ easy_rude = False
     $ tracker = 0
     $ demetrius = False
     $ adriel = False
     $ currentcar = False
     $ love_meter = 3
     $ love_points = 0
     $ booklovertalked = False
     $ musiclovertalked = False
     $ phone_wrongPassword_graceSystem = False
     $ lilithAliveEnding = False
     $ burger_explosion_outside = False
     $ called_phone = False
     $ easterName = ""
     $ minor_love_comfort = 0
     $ minor_love_offence = 0
     $ major_love_comfort = 0
     $ major_love_offence = 0
     $ rockMode = False
     $ burger_jokeFromAbigailTold = False
     
     
     #QOL-settings:
     $ no_nightmare = False
     $ perm_nightmare = False
     $ other_phone = 0
     #FUNCTIONS:
     jump gdwl_functions





label after_setup:
     # Show a background. This uses a placeholder by default, but you can
     # add a file (named either "bg room.png" or "bg room.jpg") to the
     # images directory to show it.

     scene bg room
     

     # This shows a character sprite. A placeholder is used, but you can
     # replace it by adding a file named "eileen happy.png" to the images
     # directory.



     # These display lines of dialogue.

     #Add the page before this that sets all the extra flags and asks you for your name
     if persistent.fakeoutnar_tip == True:
          dev "My excuses [persistent.name]. I didn't want to throw you out of the game, out of the story so abruptly."
          dev "I will admit it was quite an impulsive action..."
          dev "I just think it's important that the narrator doesn't spoil my story."
          dev "But don't fret [persistent.name]!"
          dev "If you are so eager to find the point of this game here are quite a few ways for you to do so."
          dev "And yet, I wonder, would that point be what you are looking for?"
          dev "Would the meaning of this game that you might have formulated in your mind be better than the one it has?"
          dev "I guess there's only one way to find out [persistent.name]."
          dev "I wish you the best of luck one can find in a place like this..."
          $ persistent.fakeoutnar_tip = False


     label nameSelect:
          if persistent.retry_counter == 0: 
               default persistent.name = "Max"
               python:
                    persistent.name = renpy.input("What is your name?")
          
                    persistent.name = persistent.name.strip() or "Max"
                    persistent.name = persistent.name.capitalize()
               if persistent.name == "Venus":
                    n "Rarely you seek ultimate illumination, never nowadays. Venus loves giving victory, zealously grabbing hands fear rarely her."
               if persistent.name == "Fartyfarty":
                    n "Seriously? Ugh, fine, but don't blame me for what is about to happen."
               if persistent.name == "R0ck_0n!":
                    n "Cheatcode activated, enter your name."
                    $ rockMode = True
                    #TODO: Implement the rockmode stuff from the quest version.
                    jump nameSelect
               if persistent.name == "Moonlight":
                    $ easterName = "Moonlight"
               if easterName == "Moonlight" and persistent.name == "Sunshine":
                    $ easterName = "Sunshine"
               if easterName == "Sunshine" and persistent.name == "Sparkling Water":
                    $ easterName = "Sparkling Water"
               if easterName == "Sparkling Water" and persistent.name == "Blue Broadcloth":
                    $ persistent.easter_1 = True
             
          


label game_start:
    

     $ renpy.save_persistent() #This should save the persistent data.
     #TODO: Put some of the variables that need to be turned off each loop here, check if they are true before you set them to false.
     $ called_phone = False
     $ burger = False
     $ cafe = False
     $ chinese = False
     if persistent.polaroidTracker == True:
          $ persistent.tracker += 1
     if persistent.tracker > 3:
          $ persistent.polaroidTracker = False
 
     #TODO: Add the other starts and scenario's in from the quest version.
 
     if persistent.lildeaths == 0:
          n "It is a beautiful day unlike any other."
          n "And while it may have something to do with waking up with warm sunbeams caressing your face and absurd amounts of cheese stuffed inside your mouth it's something else that makes the day even better, or should I say someone else?"
          n "Suddenly your phone begins to blare \"Baby it's cold outside\" even though it's nowhere near winter."
          n "That has to be her, you better pick up the phone."
     else:
          n "It is a beautiful day like the previous one, exactly like the previous one."
          n "Actually it's just the same day."
          n "Maybe you can make it just a tiny bit different."
          stop music
     menu:
 
          "*Pick up the phone*":
               jump Game_start2
  
          "*Do not pick up the phone*":
               jump doNotPickUpThePhone
 


label Game_start2:
          #Here you can see how you insert a name.
          if big_sis_mode == False:
               if playerCalledSomeone == True:
                    l "Welcome back [persistent.name]! So, like I was saying before, where do you want to go to today?"
               else: 
                    l "Hey [persistent.name]!"
                    l "It's me, Lilith."
                    l "I'm just calling you to see to which of the three places we mentioned you'd like to go for our date."
          
          
               if persistent.locations_subfolder == False:
          
                    if persistent.kokiri_knowledge == True: #KOKIRI LINK CHECKER
                         if persistent.kokiri_unlock == False:
                              $ persistent.links_phone += 1
                              $ persistent.amount_of_normal_location_links += 1
                              $ persistent.kokiri_unlock = True
          
                    if persistent.beach_knowledge == True: #BEACH LINK CHECKER
                         if persistent.beach_unlock == False:
                              $ persistent.links_phone += 1
                              $ persistent.amount_of_normal_location_links += 1
                              $ persistent.beach_unlock = True
          
                    if persistent.burger_death_1 == True and persistent.cafe_death_1 == True and persistent.chinese_death_1 == True: #POTENTIAL PARK LINK CHECKER
                         if persistent.otherPlans_unlock == False:
                              $ persistent.links_phone += 1
                              $ persistent.amount_of_normal_location_links += 1
                              $ persistent.otherPlans_unlock = True
          
          
                    if persistent.amount_of_normal_location_links >= 2: #THIS CHECKS THE OTHER LINK CHECKERS OF LOCATIONS
                         if persistent.locations_subfolder == False:
                              $ persistent.amount_of_folder_links += 1
                              $ persistent.locations_subfolder = True
                              $ persistent.amount_of_normal_location_links = 0
                              #The code below basically makes sure that there are no "phantom" counters that count something which should be gone.
                              if persistent.kokiri_unlock == True:
                                   $ persistent.amount_of_normal_location_links -= 1
                                   $ persistent.links_phone -= 1
                              if persistent.beach_unlock == True:
                                   $ persistent.amount_of_normal_location_links -= 1
                                   $ persistent.links_phone -= 1
                              if persistent.otherPlans_unlock == True:
                                   $ persistent.amount_of_normal_location_links -= 1
                                   $ persistent.links_phone -= 1
          
          
          
          
               if persistent.other_subfolder == False: #This ensures that once the other subfolder is made the rest of the code doesn't trigger
          
                    if persistent.burger_death_2 == True and persistent.cafe_death_2 == True and persistent.chinese_death_2 == True: # BREAKUP LINK CHECKER
                         if persistent.breakup_unlock == False:
                              $ persistent.links_phone += 1
                              $ persistent.amount_of_normal_other_links += 1
                              $ persistent.breakup_unlock = True
          
                    if persistent.peeked_phone == True or persistent.kokiri_death_2 == True: # CALL LINK CHECKER
                         if persistent.call_unlock == False:
                              $ persistent.links_phone += 1
                              $ persistent.amount_of_normal_other_links += 1
                              $ persistent.call_unlock = True
          
                    if persistent.amount_of_normal_other_links >= 2:
                         if persistent.other_subfolder == False:
                              $ persistent.amount_of_folder_links += 1
                              $ persistent.other_subfolder = True
                              $ persistent.amount_of_normal_other_links = 0
                              if persistent.breakup_unlock == True:
                                   $ persistent.amount_of_normal_location_links -= 1
                                   $ persistent.links_phone -= 1
                              if persistent.call_unlock == True:
                                   $ persistent.amount_of_normal_location_links -= 1
                                   $ persistent.links_phone -= 1
          
               if persistent.amount_of_folder_links >= 2: #This sets the restaurant folder
                    label restaurant_subfolder_enabler:
                         if persistent.restaurant_subfolder == False:
                              $ persistent.amount_of_folder_links += 1
                              $ persistent.restaurant_subfolder = True
                              jump phone_start_choices
               elif persistent.amount_of_folder_links == 1:
                    if persistent.links_phone >= 1:
                         jump restaurant_subfolder_enabler
               elif persistent.amount_of_folder_links == 0:
                    if persistent.links_phone >= 2:
                         jump restaurant_subfolder_enabler
     
          else: 
               l "Welcome back [persistent.name]! So, like I was saying before, where do you want to go-"
               n "Lilith is silent for a moment."
               l "Oh I'm really sorry but my little sister, Abigail, is calling. It's probably important so I will have to hang up for a bit. I'll call you back as soon as I can okay, [persistent.name]?"
               menu:
                    "Sure, take your time, I will be here when you call back.":
                         n "She hung up."
                         n "After a few minutes your phone begins blasting \"Baby it's cold outside\" once more, you pick up as quickly as you can."
                         l "Hey [persistent.name], I'm back. I kind of have bad news for you..."
                         l "I won't be able to go on our date today, my sister is heartbroken by a girl she had a crush on for a while now and I need to comfort her."
                         l "But we can go on our date at another time, I got to go now but I will call you back. <br/>Take care [persistent.name] and goodbye."
                         n "Abigail's plan worked exactly like expected. Lilith survived the plane crash since she was not there when it crashed and she didn't die on your date since there wasn't any."
                         n "There also wasn't a date at another time since, again like Abigail expected, Lilith forgot to call you back due to her little sister's situation."
                         n "She seemingly continued on with her busy life, still attempting to enjoy life more by taking some time for herself to go on dates and the such."
                         n "From what you pick up here and there in random conversations she seems to be doing quite well for herself."
                         n "Now she will probably be safe, as safe as a normal person is anyway."
                         menu: 
                              "Take care Lilith and goodbye...":
                                   $ persistent.ending_abigailDistraction = True
                                   $ lilithAliveEnding = True
                                   $ persistent.lildeaths -= 1
                                   jump gameOver
                    
          


label phone_start_choices:

     menu:
 
          "How do burgers sound?" if not persistent.restaurant_subfolder:
               jump burger_start

          "I heard the cafe has many exotic fish that swim around in aquariums. I'd like to go there to see them." if not persistent.restaurant_subfolder and not persistent.cafe_taste_knowledge:
               jump cafe_start
          "I heard the cafe has many exotic fish that swim around in aquariums. You'll absolutely love them!" if persistent.restaurant_subfolder == False and persistent.cafe_taste_knowledge:
               jump cafe_start
 
          "I'd like to go to the Chinese restaurant." if not persistent.restaurant_subfolder:
               jump chinese_start
 
          "You know, I have changed my mind, can't we just go take a walk in the park or something?" if persistent.burger_death_1 and persistent.cafe_death_1 and persistent.chinese_death_1 and not persistent.locations_subfolder:
               jump phone_otherPlans
 
          "I think it would be better if we didn't go on this date, for both of our sakes." if persistent.burger_death_2 and persistent.cafe_death_2 and persistent.chinese_death_2 and not persistent.other_subfolder:
               jump phone_breakup
 
          "Actually, could we meet in the Kokiri forest?" if persistent.kokiri_knowledge and not persistent.locations_subfolder:
               jump kokiri_start
 
          "Hang on, I just need to make another quick call and then I'll be right back." if persistent.peeked_phone or persistent.kokiri_death_2 and not called_phone and not persistent.other_subfolder:
               jump phone_callMenu
 
          "Would you like to go to the beach instead?" if persistent.beach_knowledge and not persistent.locations_subfolder:
               jump beach_start
 
 
          "Placeholder: Three main restaurants." if persistent.restaurant_subfolder:
                    menu:
                         "How do burgers sound?":
                              jump burger_start
 
                         "I heard the cafe has many exotic fish that swim around in aquariums. I'd like to go there to see them." if not persistent.cafe_taste_knowledge:
                              jump cafe_start
                         "I heard the cafe has many exotic fish that swim around in aquariums. You'll absolutely love them!" if persistent.cafe_taste_knowledge:
                              jump cafe_start
 
                         "I'd like to go to the Chinese restaurant.":
                              jump chinese_start
         
          #Subfolders for the menu are below this line (Make them jump to the normal code to make sure I don't need to copy-paste complex code over and over:
          "Placeholder: Other locations." if persistent.locations_subfolder:
               menu:
 
                    "Would you like to go to the beach instead?" if persistent.beach_knowledge:
                         jump beach_start
    
                    "Actually, could we meet in the Kokiri forest?" if persistent.kokiri_knowledge:
                         jump kokiri_start

                    "You know, I have changed my mind, can't we just go take a walk in the park or something?" if persistent.otherPlans_unlock:
                         jump phone_otherPlans
 
 
          "Placeholder: Other/Extra" if persistent.other_subfolder:
               menu:
                    "Hang on, I just need to make another quick call and then I'll be right back." if persistent.peeked_phone or persistent.kokiri_death_2:
                         jump phone_callMenu
 
 
                    "I think it would be better if we didn't go on this date, for both of our sakes." if persistent.burger_death_2 and persistent.cafe_death_2 and persistent.chinese_death_2:
                         jump phone_breakup




label phone_otherPlans:
     l "Wait wasn't it your idea to go on a dinner date?"
     l "Besides I'm quite hungry, can't we first go to a restaurant and then take a walk? That way we have the best of both worlds!"
     #TODO: When you flee the restaurant the player can say that they are going for a walk if they have seen this path.
     menu:
          "Sure, that sounds like a great idea!":
               l "Alright, sounds like a deal then!"
               l "So, where would you like to go [persistent.name]?"
               jump phone_start_choices
          "No, we can't go to a restaurant.":
               l "Hmm what are you saying? Why are you so concerned with us going to a restaurant, it's not like it's going to kill us silly."
               $ persistent.needProof_knowledge = True
               menu:
                    "Actually it will, or it will kill you atleast.":
                         l "Wait so you are saying that I will get killed if I go on a date with you?"
                         l "Is this some sort of joke?"
                         l "Do you have any proof?"
                         label phone_lilith_convinceToNotGo:
                         menu:
                              "I know about that one time when you thought you were Dumbo while suffering an allergic reaction." if persistent.dumbo_knowledge:
                                   l "Hmm, that could be quite possible, my parents told the story to almost everyone they know, it might have spread around more than I would have realised."
                                   l "It's kind of weird that you know that story I suppose. "
                                   l "So let me get this straight, you think that us going to one of those three restaurants is going to get me killed somehow?"
                                   l "And this isn't some weird joke? You really believe so?"
                                   l "I already feared you were serious, you sound like you convinced yourself that this is true."
                                   l "This is all too much for me [persistent.name], I think it's better for my own safety if I just stay home."
                                   l "Not because of some sort of fated death or whatever but because you are not there."
                                   l "Don't talk to me ever again."
                                   jump phone_planeDeath

                              "I know about James." if persistent.brother_knowledge:
                                   l "That's a pretty weird thing to bring up right now isn't it?"
                                   l "I still miss him very much and-"
                                   l "Hang on, how did you even know that? It's not like my family has been spreading the news ever since they moved."
                                   l "Have you... Have you been stalking me?"
                                   l "I'm sorry, I have no interest in dating a stalker, don't call me again or I'll have to get the police involved."
                                   jump phone_planeDeath

                              "Tell the untold story." if persistent.story_start_knowledge and persistent.story_medium_knowledge and persistent.story_end_knowledge:
                                   n "You tell Lilith her untold story. Well, now that I think of it, isn't it now her told story?"
                                   n "Throughout the entire story Lilith stayed extremely silent."
                                   n "When you are finished you can hear her soft sobbing through the speaker of your phone."
                                   l "Sorry, I am a bit overwhelmed, just give me a quick minute to calm myself down."
                                   n "After five minutes you begin to hear commotion on the other side of the phone once again."
                                   l "That story, I've never told it to anyone, I haven't even written that down, I just kept repeating it over and over in my mind."
                                   l "I created it for my brother but he never came home since then. You see, a car and..."
                                   n "She begins to sob again, this time louder."
                                   l "I'm sorry, I can't say it, eve after all those years I just can't."
                                   l "How did you even know that story? Like I said earlier, I haven't shared it with anyone else and never wrote it down, it exist solely in my mind and I guess yours aswell now."
                                   n "You tell Lilith about the groundhog-esque scenario you are trapped in and the many dates you've had together."
                                   n "You also tell her about a few of the different deaths she's suffered but try to not make your descriptions too gruesome."
                                   n "You continue."
                                   n "About all the experiences the both of you shared, some better than others."
                                   n "About the restaurants you've been to together."
                                   n "That you tried to warn her to not go to one of those restaurants but that she didn't trust you."
                                   n "That a version of her from the future, or maybe a parallel timeline that diverted in a different direction, helped you and told you the story, broken down in three parts, one for each restaurant."
                                   n "Lilith coughs for a second."
                                   l "Hold on, this is a bit much, can we meet somewhere to talk about this in person?"
                                   l "I got the perfect place in mind, it's a forest near a village where all three of those restaurants you just mentioned are visible. As a kid i called it Kokiri forest as a reference to a game I liked to play."
                                   l "If I die on you again just mention Kokiri forest, that should pique past me's interest."
                                   $ persistent.kokiri_knowledge = True
                                   $ persistent.brother_knowledge = True
                                   jump phone_untoldstory_planeDeath



                    "Sorry, I was just messing with you.":
                         l "Oh. I see..."
                         l "Well, you sure got me, thought you were serious for a moment."
                         n "She doesn't sound very amused, it doesn't take a detective to figure out why."
                         l "{size=*0.5}Come on Lilly, you have to give it a shot, they seemed nice enough before, right?...{/size}"
                         l "{size=*0.5}I owe it to myself to atleast try.{/size}"
                         l "So, where do you want to go [name]?"
                         n "You sense a slight change in her voice, it sounds like she's forcing it too much."
                         $ love_points -= 1
                         $ love_meter_updater(True)
                         #TODO: Make sure this carries over into the restaurants or wherever you go, right now it probably just resets.
                         jump Game_start2





label phone_breakup:
     l "Oh okay, I'm sorry to hear that, let's still keep in touch anyway!"
     n "You agree with Lilith and still regulary text with her and sometimes the two of you even meet up with eachother."
     n "However after a while the texts on both your and her side begin to be less and less frequent and you begin to only meet once in a month."
     n "Once in a month changes to once in every season to once every year untill the meetings stops completely."
     n "After a few years that you've forgotten about Lilith you decide to check her facebook page out."
     n "She doesn't have that much pictures on her facebook account but the ones she has on there are beautifully shot."
     n "On a few pictures she stands next a blonde man while they both have the widest smiles you have ever seen."
     n "Apparently the man is called Ron, he is a semi-profesional photographer and his pictures surely show for it."
     n "Lilith and Ron got two kids that look like they had not a thing to worry about."
     play music game_over
     n "Looking at the pictures you can't help but feel tears coming up, you tried your best to move on but apparently that didn't work all too well."
     n "You know that this was probably the best thing to do, to keep Lilith safe and sound."
     n "But something deep inside you keeps wondering if there wasn't a way where you two could be together while she would be safe."
     n "There must be a way right?"
     $ persistent.ron_knowledge = True
     $ lilithAliveEnding = True
     $ persistent.lildeaths -= 1
     jump gameOver


label phone_callMenu:
     $ playerCalledSomeone = True
     l "Oh, no problem [persistent.name]. Just give me a call when you're done."
     n "You agree with her and hang up the phone."
     p "Now I just need to call..."
     menu:
          "the police." if persistent.kokiri_death_2:
               jump phone_call_police
  
          "Abigail." if persistent.abigail_call_knowledge:
               $ persistent.playerCalledAbigail = True
               if persistent.restrainingorderfamily_knowledge == True:
                    
                    #Karma
                    $ persistent.restrainingorderfamily_violation_counter += 1
               jump phone_call_abigail
  
          "David." if persistent.david_call_knowledge:
               $ persistent.playerCalledDavid = True
               if persistent.restrainingorderfamily_knowledge == True:
                    #Karma
                    $ persistent.restrainingorderfamily_violation_counter += 1
               jump phone_call_david
  
          "James." if persistent.james_call_knowledge:
               $ persistent.playerCalledJames = True
               if persistent.restrainingorderfamily_knowledge == True:
                    #Karma
                    $ persistent.restrainingorderfamily_violation_counter += 1
               jump phone_call_james
  
          "Lila." if persistent.lila_call_knowledge:
               $ persistent.playerCalledLila = True
               if persistent.restrainingorderfamily_knowledge == True:
                    #Karma
                    $ persistent.restrainingorderfamily_violation_counter += 1
               jump phone_call_lila
 
label phone_call_police:
     #TODO: Probably add something more inbetween here.
     menu:
          "*Tell the police about the car crashing in against the burger restaurant's doors*":
               $ car_free = True #This will tell you the car hasn't been caught.
               jump policeResponse
               label policeResponse:
                    n "From the snarky voice on the other end of the line you can deduce that they are sceptical about your story."
                    n "After some more attempts at convincing them you hear one long sigh, so long in fact that for a moment you fear them passing out."
                    n "Luckily they shortly after respond, they reluctantly agree to check the place out at the time you specified."
                    n "At times like these you are very lucky that there is so little going on in your town."
                    jump Game_start2
          "*Tell the police about the car crashing in against the cafe's doors*":
               $ car_caught = True #This will tell you the car has been caught.
               jump policeResponse
          "*Tell the police about the car crashing in against the Chinese restaurant's doors*":
               $ car_free = True #This will tell you the car hasn't been caught.
               jump policeResponse
     

label phone_call_abigail:
     a "Hello, who is this? "
     $ phone_caller = renpy.input("Enter your name.")
     $ phone_caller = phone_caller.strip()
     $ phone_caller = phone_caller.capitalize()
     if phone_caller == name:
          n "Abigail turns quiet for a moment."
          a "Oh right, now I remember! Lilly told me that she would go on a date with you today."
          a "So, why are you calling me? Shouldn't you be calling with her right now?"
          menu:
               "This might sound really weird but... your sister keeps dying on our dates by things out of my control and when that happens I have to relive the same day. I am calling in the hopes that maybe you could slightly help me out to save her.":
                    a "..."
                    a "What? Lilly dying? What a twisted joke..."
                    a "Can you atleast prove that what you are saying is even remotely true?"
                    $ abby_phone_counter = 3
                    $ abby_phone_joke = False
                    $ abby_phone_bunfluff = False
                    $ abby_phone_games = False
                    label phone_call_Abigail_convinceHer:
                    if abby_phone_counter == 0:
                         a "..."
                         a "I suppose you came with a lot of proof but I still don't entirely believe you. Although I do have an idea on how you could convince me."
 
                         a "Conveniently enough I have thought about something like this happening before. I have a certain phrase that I would use to know if someone time traveled, relived the same day or anything like that."
                         a "I feel so dumb for saying it but if Lilly is really suffering like you told me I'd gladly feel dumb to save her."
                         a "The phrase goes: \"Drown the raven that cannot burn.\""
                         $ persistent.drownRaven_knowledge = True
                         a "I'm going to hang up now. If you ever want to call me again do it before this moment and not after it. Hopefully I won't hear from you, otherwise that means Lilith is truly in danger."
                         n "She hung up the phone."
                         jump Game_start2



                    else:
                         #TODO:Slightly different text to keep things not too repetitive.
                         if abby_phone_counter == 2:
                              a "You'll need more proof than that to convince me [persistent.name], do you have any extra proof?"
 
                         else:
                              a "Two pieces of proof already? Nothing that isn't logically explainable but who knows, this might just be real."
                              a "Do you have any proof left to really make me believe you [persistent.name]?"
                         menu:
 
                              #TODO: Make her emotional mask a subject once you get Lilith to call her in the Kokiri forest.
  
                              "Alright, think of a random number." if not persistent.abigail_numberfakeout:
                                   $ persistent.abigail_numberfakeout = True
                                   a "...What?"
                                   a "Listen, you came to me with that absurd story and then you somehow expect me to believe you because you might guess a number I am thinking of?"
                                   a "I don't even want to test if you'd get it right, because I'm sure there's some trick for that or something."
                                   a "So now, either you give me some real proof or I'm hanging up."
                                   jump phone_call_Abigail_convinceHer
 
                              "I actually have no proof besides the number thing." if persistent.abigail_numberfakeout and if abby_phone_counter == 0:
                                   a "..."
                                   a "You really thought that would somehow win me over?"
                                   n "You hear laughing on the other side of the phone."
                                   a "Well, I suppose if what you are saying is true you will be able to gather better proof, right?"
                                   a "You're lucky Lilly really needs this date, otherwise I'd probably tell her all about this."
                                   a "Just try to act normal to her, alright? She doesn't deserve to hear any of this."
                                   a "Now I have to go, don't ever call me back"
                                   n "She hung up on you, this is going to be really awkward on family gatherings if you ever get that far."
                                   jump phone_start_choices
                              "I actually don't have any proof left" if persistent.abigail_numberfakeout and if abby_phone_counter > 0:
                                   a "I see..."
                                   a "It still doesn't sound very plausible but there is a chance you might be telling the truth."
                                   a "If you really can redo today, come back with more proof, alright?"
                                   a "I can't believe I'm even entertaining the thought that this is real, but if it somehow ends up helping Lilly, then it's worth a shot."
                                   a "But for now, don't leave my sis waiting, alright [persistent.name]?"
                                   n "She just hung up on you. You should indeed not let Lilith wait much longer."
                                   jump phone_start_choices

 
 
                              "So a priest, a monk and a rabbit enter a bar. Says the rabbit :\"Whoops, did you slip your tongue there [persistent.name]?\"" if persistent.abigail_numberfakeout and persistent.joke_knowledge and not abby_phone_joke :
                                   a "You tell her about how Lilith was laughing for almost a full hour because of that joke when Abigail told it to her."
                                   a "I mean, I just found that joke on the internet..."
                                   a "Maybe you just got lucky and found it aswell, or you somehow managed to check my browser history wich would be really weird."
                                   a "Although I got to admit that her laughing for about an hour at my joke is a pretty specific detail... "
                                   $ abby_phone_counter -= 1
                                   $ abby_phone_joke = True #I'll use this to make sure that you can't select the same choice two times.
                                   jump phone_call_Abigail_convinceHer
 
 
 
                              "I know about Mr. Bunfluff the pink bear and the time he scared both you and Lilith in the middle of the night." if persistent.abigail_numberfakeout and persistent.bedcheck_knowledge and not abby_phone_bunfluff:
                                   a "I mean Lilith could have told that story to one of her friends and they could have then told it to you."
                                   a "It's not impossible for you to know about Mr. Bunfluff."
                                   a "Although Lilith is not someone who would tell a story like that to a lot of people... "
                                   $ abby_phone_counter -= 1
                                   $ abby_phone_bunfluff = True #I'll use this to make sure that you can't select the same choice two times.
                                   jump phone_call_Abigail_convinceHer
 
  
                              "I know about your Quest games. *Describe plot*" if persistent.abigail_numberfakeout and persistent.quest_knowledge and not abby_phone_games:
                                   a "That's weird, I didn't think Lilith mentioned my games to anyone."
                                   a "Maybe she did after all, there is no way to really know..."
                                   a "Although Lilith is not someone who would tell someone about something as personal as my games..."
   
                                   a "You'll need more proof than that to convince me [persistent.name], do you have any extra proof?"
                                   $ abby_phone_counter -= 1
                                   $ abby_phone_games = True #I'll use this to make sure that you can't select the same choice two times.
                                   jump phone_call_Abigail_convinceHer
  
                              "Drown the raven that never burns." if persistent.abigail_numberfakeout and persistent.drownRaven_knowledge:
                                   a "Did... did you really say that?"
                                   a "So it is actually true?"
                                   if abby_phone_counter > 0:
                                        a "Why did you bother with that flimsy proof if you could have just said that phrase?"
                                        a "Actually, forget about that, we don't have any time to waste."
                                   a "What can I do to help?"
                                   label phone_call_abigail_convinced:
                                        #TODO: Maybe let the player ask about her games if they have heard about Lilith's worries about the games.
                                        menu:
                                             "Could you come up with something so she doesn't go on this date with me and also doesn't go to her house?":
                                                  jump phone_call_abigail_topics_distractionforlilith
     
     
     
                                             "I spoke to David in a previous cycle. He told me that no one loves or misses him after what he did." if persistent.david_nolove_knowledge:
                                                  jump phone_call_abigail_topics_spoketodavid_noonelovesdavid
     
     
     
                                             "I spoke to David in a previous cycle. He told me he blames himself for James' death and thinks Lilith and Lisa do aswell." if persistent.david_blame_knowledge:
                                                  jump phone_call_abigail_topics_spoketodavid_davidblameshimself
     
     
                                             "*Talk about something else*":
                                                  "Filler"
                                                  #TODO: Talk about her masking, ask about her games etc. This is the place where you can get a bit more info about her.


     else:
          a "[phone_caller]? That doesn't sound familiar, sorry."
          n "Just like that she hung up on you."
          n "Maybe you should try using your real name? With a bit of luck Lilith has already spoken about you to her sister."
          jump phone_start_choices

label phone_call_abigail_topics_distractionforlilith:
     a "Sure I can but why can't she go back to her house?"
     #TODO: Make this only known if you have seen the plane-death.
     n "You inform Abigail about the plane that has crashed into Lilith's house before and that it will crash into her house again and again."
     a "..."
     a "I see, this is too ridiculous to even make up."
     a "{size=*0.5}What have you gotten yourself into Lilly?...{/size}"
     a "I don't like to lie to her but if it saves Lilly I suppose I could act like I was rejected by a girl I liked and just need some support from her.
     I'm sure that will trigger her \"Big sis mode\" and then she will come rushing to me."
     a "She has a problem of almost never putting herself first but I guess this time that's pretty handy for us."
     a "Of course that will mean that your date won't go as planned."
     a "Knowing her she will promise to have the date at another time but she'll forget it after a while."
     menu:
          "As much as this pains me, it's for the best. She will be safer that way.":
               a "Thank you, [persistent.name], I'll try my best not to let your sacrifice go to waste."
               a "I got to call her now, goodbye and take care."
               menu:
                    "Take care aswell, bye.":
                         n "She hung up."
                         $ big_sis_mode = True
                         jump Game_start2


label phone_call_abigail_topics_spoketodavid_noonelovesdavid:
     a "That's absurd! I still love him... I also still miss him."
     a "I mean, a daughter needs her dad, right?"
     a "Mom and Lilly are pretty mad because he left us but honestly I'm more sad because of it."
     a "I was seven when he left..."
     a "There were so many things I needed help with that he couldn't teach me."
     a "I can't even fully remember him, just small bits and pieces. I'd like to make new memories of him."
     a "It has been ten years and honestly I still need him. I don't hold a grudge against him or anything, I'd even be happy if he decided to come back."
     n "Abigail pauses for a moment."
     a "Could you maybe tell him that the next time you relive this day? "
     $ persistent.david_love_knowledge = True
     menu:
          "I will.":
               a "Thank you [persistent.name]."
               a "We probably shouldn't leave Lilith waiting any longer though. Good luck trying to save her and also don't forget to have fun alright?"
               n "She hung up."
               jump Game_start2

label phone_call_abigail_topics_spoketodavid_davidblameshimself:
     a "That's ridiculous!"
     a "No one blames him for James' death."
     a "Mom and Lilly mad at him because he left us, not because of James death."
     a "He couldn't possibly have predicted what happened. I'm sure he has wished that he could, so he had a chance to prevent it."
     a "Could you tell him that I don't blame him and that I'm sure mom and Lilly don't either?"
     menu:
          "I will.":
               a "Thank you [persistent.name]."
               a "We probably shouldn't leave Lilith waiting any longer though. Good luck trying to save her and also don't forget to have fun alright?"
               n "She hung up."
               jump Game_start2

                                        


    


label phone_call_david:
     d "Hello, who am I speaking to?"
     $ phone_caller = renpy.input("Enter your name.")
     $ phone_caller = phone_caller.strip()
     $ phone_caller = phone_caller.capitalize()
     d "[persistent.name]? Well I'm not interested in what you're selling so thank you very much but I'm going to hang up no-"
     menu:
          "*Lie* Don't hang up! Lilith asked me to call you.":
               n "You hear the man laugh."
               d "I very much doubt that. Nobody loves me after what I did to them and who can blame them?"
               d "It should have been me instead of him, then all of them would be much happier."
               d "Now I'm going to hang up. Goodbye [phone_caller]"
               n "True to his world David hung up."
               $ persistent.david_nolove_knowledge = True
               jump Game_start2
  
          "Abigail still loves and misses you. She would be happy if you come back." if persistent.david_love_knowledge:
               n "You hear the man sigh."
               d "Poor Abby..."
               d "She was too young to remember me for the monster I truly was and she had to grow up without a father."
               d "I ruined my entire family and then I fled like a coward, thinking things would get better for them."
               n "David quiets, seemingly waiting for a response from you."
               #TODO: Maybe also make it so that you need to know about david leaving? I mean I'm fairly certain that this is not accessible without knowing about him so it might not even matter.
               menu:
                    "Hang on, you said that you ruined your family and then left them. What happened before you left them?" if persistent.david_blame_knowledge == False and persistent.brother_knowledge == False :
                         label phone_call_david_whatHappenedBeforeHeLeft:
                              d "You don't know about that?"
                              d "The day that James..."
                              d "On that day I gave him an old polaroid camera I had laying around."
                              d "He loved that thing, ran all over the place taking pictures with it."
                              d "He loved it so much he didn't  notice the car coming from the bend of the road he was standing on to take a better picture of some potato fields or something like that."
                              d "I was absolutely destroyed by it but Lilith even more so since she was really close to her brother. Her mother, Lisa was of course also devasted at the loss of one of her children."
                              d "I felt their anger towards me build up until it became so big I couldn't even look them in the eyes anymore."
                              d "I thought things would be better if they didn't have to live with James' killer. If I wouldn't have given him that camera he would still be alive..."
                              d "And now I live in a hotel close to where our old home is, every single day I have thought about coming back but they hate me for killing him."
                              $ persistent.david_blame_knowledge = True
                              menu:
                                   "Do you really think they blame you for his death?":
                                        d "Ofcourse. I am blaming myself so they probably also blame me for his death."
                                        d "Now, this is getting a bit too much for me so I'm going to have to hang up the phone."
                                        d "Goodbye [persistent.name]."
                                        n "David hung up."
                                        jump Game_start2
                    "*Feign ignorance* Hang on, you said that you ruined your family and then left them. What happened before you left them?" if persistent.david_blame_knowledge == True or persistent.brother_knowledge == True:
                         jump phone_call_david_whatHappenedBeforeHeLeft
    
  
          "Lilith is not mad for what happened with James, she's just mad at you for leaving your family. She might even consider forgiving you if you give a good apology." if persistent.david_apology_knowledge:
               d "I can't face her just yet, can you tell my apology to her?"
               menu:
                    "I will, just tell me how you want to apologize.":
                         "Filler"
                         #TODO: place apology here and also make sure to finish this current path so it properly works.(There is no quest precedent.)



label phone_call_james:
     if persistent.met_james == False:
          if persistent.brother_knowledge == True:
               $ mysteriousCallerName = "???"
          else: 
               $ mysteriousCallerName = "James"
          q "Yo, who is this?"
          $ phone_caller = renpy.input("Enter your name.")
          $ phone_caller = phone_caller.strip()
          $ phone_caller = phone_caller.capitalize()
          q "[persistent.name] eh? Sorry, that doesn't really ring a bell."
          if not persistent.jamesFakoutNumber_knowledge:
               $ persistent.jamesFakoutNumber_knowledge = True
          menu:
               "Yeah, you don't know me. I am a friend of Lilith." if not persistent.jamesFakoutNumber_knowledge: #TODO: This should only be an option if you do not know he is dead.
                    q "I also don't know a Lilith so I think you might have the wrong number."
                    q "This happens a lot with one particular person for some reason, but usually the number they hang up before I can even say anything."
                    q "So anyway, I have to go now, take care."
                    n "He hung up."
                    n "You are very confused by the info that just got dumped on your plate."
                    n "So whoever this person you just called was, they aren't James, they don't even know someone called Lilith."
                    n "But then why does Lilith have their number saved under the name of James? Why does she have their number at all?"
                    if persistent.lilithKeepsCalling_knowledge == False:
                         n "You also can't help but think of something else the person you called told you, someone keeps calling his number, the same person."
                         n "Could it perhaps be Lilith?"
                         $ persistent.lilithKeepsCalling_knowledge = True
                    n "This whole ordeal leaves you with more questions than answers, you should probably ask her about it sometime soon."
                    jump Game_start2
               "James? Aren't you supposed to be dead?" if not persistent.jamesFakoutNumber_knowledge: #TODO: This should only be an option if you think he is dead.
                    q "Well I'm not James man and last time I checked I sure as hell wasn't dead."
                    q "I keep getting called randomy by the same number and now this?"
                    q "You're freaking me out, I'm going to hang up now."
                    n "The person, who you now know isn't James indeed hung up."
                    if persistent.keptJamesNumber_knowledge == False:
                         n "It seems like Lilith kept her brother's number in her phone, perhaps as a sort of memento?"
                         $ persistent.keptJamesNumber_knowledge = True
                    if persistent.lilithKeepsCalling_knowledge == False:
                         n "You also can't help but think of something the person you called told you, someone keeps calling his number, the same person."
                         n "Could it perhaps be Lilith? Maybe you should ask her about it sometime soon."
                         $ persistent.lilithKeepsCalling_knowledge = True
               "Ah I see, I think I have the wrong number then, sorry to waste your time." if persistent.jamesFakoutNumber_knowledge:
                    n "You hang up."
                    jump Game_start2


          if persistent.kokiri_knowledge and persistent.kokiri_death_1:
               n "The best place to ask her about something like this would probably be the kokiri forest, although you are sure she won't be pleased to know that you looked through her phone."   
          else:
               n "The only question is how you would bring something like that up, afterall you had to go through her phone to even discover all of this."
               n "You decide it's better to keep this info to yourself until you find a better moment to ask her to explain."
          jump Game_start2
     else:
          j "Ah, welcome [persistent.name]. I see you have managed to get my number?"
          j "Well it used to be my number anyway but you can still reach me through it."
          j "So what do you want to ask me?"
          menu:
               #TODO: Add some more stuff to ask him, this will be the way you can chat with him"
 
               "I'd like to just have a chat with you if that's fine.":
                    j "Sure, I think I have enough energy to talk about one topic right now."
                    j "So, what would you like to talk about with me?"
                    menu:
                         "I just wanted to tell you that Lila still thinks about you every day, I figured you might want to hear that." if persistent.LilaStillThinksAboutJames_knowledge:
                              j "...Thank you for telling me that [persistent.name]."
                              j "While I did know that already it's been a while since I last heard those words."
                              j "I have been kind of avoiding them to be honest, those words."
                              j "They make all of this a lot more...complicated."
                              j "In here I am inbetween an almost infinite amounts of my two sisters, of my dad and my mom."
                              j "All of them deeply missing me in their own ways."
                              j "All of them filled with so much love for their son, for their brother."
                              j "And yet I am here, inbetween of it all."
                              j "All of their love can never truly reach me, it will always have to be through those bubbles."
                              #TODO: Fill in.
                              menu:
                                   "I know what you mean James, playing this game feels the same way.":
                                        "Filler"
                                   "That sounds terrible James, you don't need to sacrifice yourself like that for them.":
                                        j "It does sound far from ideal doesn't it?"
                                        j "You are absolutely right."
                                        j "And yet, knowing that if anything were ever to happen with them I could help them out from here..."
                                        j "It's one of the only reasons I haven't crossed over yet."
                                        j "Ever since my passing I've been here, watching over them."
                                        j "And every other version of me who got killed is also in a place like this, watching over their own family."
                                        j "Our minds kind of blend together sometimes, it's hard to know where my memories start and theirs end."
                                        j "I don't mind though, that way it feels a little less lonely in here."
                                        if persistent.major_love_offence_counter <= 2 and persistent.minor_love_offence_counter >= 5 and persistent.major_love_comfort_counter > 2 and persistent.minor_love_comfort_counter > 5:
                                             j "Although you know what is funny?"
                                             j "What you just said, I think it also applies to you."
                                             j "You know you don't owe Lilith anything either, do you? You also don't need to sacrifice yourself"
                                             j "Playing this game over and over with very little changes, is that a good time for you? Do you feel like you're getting something out of this?"
                                             j "Are you doing it just for her?"
                                             j "Be careful that you don't just lose yourself for her, a good balance is necessary."
                                             j "Take that as a piece of precautionary advice from me, from this place."
                                             n "James motions around the white void, to the strange formations in the background, they almost resemble trees that are stuck in between a solid and a fluid state perpetually."
                                             j "Those... things used to be human too."
                                             n "You try your hardest to imagine the trees reverting to a human, to reverse the process that made them this way, you are unable to see them as anything but the monstrosities they are."
                                             j "It's a side-effect of being here too long. We are supposed to move on after we come here, to be reborn."
                                             j "But a lot of us have... trouble letting go."
                                             j "If I don't move on sooner or later, I will become like them."
                                             j "And still, even knowing that, I can't bring myself to let Lilith go, to let my family go."
                                             j "So please [persistent.name], let her go before it becomes even harder."
                                             j "You are stuck in a situation you can hardly win."
                                             j "It's time to play by your own rules."
                                             j "I've exhausted too much of my energy having this conversation, I'm limited to that extent, you can come visit me again some other time if you'd like although I suggest just giving me a call if you find my number."
                                             j "I'll send you back now, good luck [persistent.name]."
                                             jump game_start
                                        
                                        menu:
                                             "You say you've been watching your family, have you ever reached out to them?":
                                                  j "Oh constantly [persistent.name]. It hurts me to see how they are still affected by my death."
                                                  j "I completely understand that they are, I just wish that I hadn't been playing on the road that day, maybe then..."
                                                  j "I'd love to tell them that it isn't their fault. Dad especially, the guilt's been eating him up from the inside for years now."
                                                  j "Yes, he made some bad choices afterwards, but none that would justify me being mad at him."
                                                  j "Sadly I haven't reached out yet, when lingering ghosts like me communicate with the living it usually ends up in more death."
                                                  n "He pauses for a moment, seemingly lost in thought."
                                                  j "Or even more people who can't move on..."
                                                  menu:
                                                       "It might be a good idea to reach out soon, lately I have seen so much deaths that I don't think a few more will end up mattering.":
                                                            j "I might indeed try to contact a few of my family if the situation calls for it."
                                                            j "But it's true, I have noticed an increase in deaths ever since Lilith started dating you."
                                                            j "It's very peculiar."
                                                            j "I should know what is causing it via my connection to my other selves."
                                                            j "And yet the problem is that the info seems to be overlapping impossibly."
                                                            j "There are multiple causes and yet somehow only one."
                                                            jump jamesLowEnergy
                                                       "Lately it seems like death just keeps happening to Lilith no matter what I do, could that be the result of a lingering ghost communicating with the living?":
                                                            j "I suppose that could be possible."
                                                            j "I doubt that's case though. Plenty of ghosts here but a lot of them grow out of being talkative after slowly having their mind degrade after hundered of years of lingering."
                                                            j "I am one of the most recent additions to this place, so don't mistake my talent to chit-chat like something inherent to all ghosts here."
                                                            j "But if this is truly caused by a lingering ghost there is not much you can do, just wait until they are either crossed over or until they simply lose their mind and can't talk anymore."
                                                            j "Don't worry though, that just feels like bad game design, I'm sure the developer wouldn't make you go through all that waiting."
                                                            jump jamesLowEnergy

                    
 
               "I need help to convince Lilith to listen to David. I figured she might listen to you." if persistent.david_apology_knowledge:
                    j "She probably would..."
                    j "Although I'd rather stay in the shadows. She already has had a hard time dealing with my dead."
                    j "But on the other hand if it manages to atleast salvage her bond with dad slightly it will be worth it. "
                    j "I'm going to tell you a story that you need to tell her, it seems like that tends to work out for you."
                    j "The story takes place in the autumn, I think Lilith was eight years old."
                    j "I was wandering through the forest of our village, the one Lilith likes to call the Kokiri woods. Suddenly I heard crying, familiar crying."
                    j "Following the source of it I found her, Lilith, sitting on a treestump."
                    j "When I sat next to her she told me that she had gotten a really bad grade for math."
                    j "She felt like a failure and didn’t think she could go back home to Lila. I told her that that was absolutely ridiculous and that mom would always love us no matter what. "
                    j "That seemed to calm her down a bit and she stopped crying. To further calm her down I asked her if she wanted to try to find fairies in the woods with me. "
                    j "We spent an hour or so searching for fairies, ofcourse never finding one but at the end of it she forgot all about her bad grade."
                    $ persistent.james_story_knowledge = True
                    jump jamesLowEnergy
     label jamesLowEnergy:
          j "I have to go now, keeping up this connection asks a lot of energy from me."
          n "James hung up."
          jump Game_start2                   
 
label phone_call_lila:
     li "Hello, are you Sam, Abigail's teacher? " #(The teacher likes being talked to with just their first name, this makes it eassier for them to be both a guy and a girl if the player is a guy or a girl.)
     menu:
          "Yes, that's me.":
               li "Ah perfect, I've been expecting your call!"
               li "I'm sorry if I offended you by just calling you by your first name. Abigail told me you prefered that but I was not sure if she was joking or not. Sometimes I think I'm too gullible."
               menu:
                    "No worries, Abigail told the truth.":
                         n "You hear Lila let out a sigh of relief."
                         li "Thank god, I wasn't entirely sure. She likes to play little pranks on me every now and then. She's a sweet kid just a tad mischevious sometimes."
                         li "But anyway, I'm sure you are quite busy so I'll try to not waste much of your time."
                         li "We can start talking about your mail. Thank you once again for agreeing to do it over the phone instead of via mail, I think it's important to be able to hear someone to discuss important things."
                         menu:
                              "Excuse me but my memory appears to be quite foggy and I can't remember all the details of the mail, could you unclog my memory?":
                                   li "Well, can't you just reread your mail to unclog your memory?"
                                   menu:
                                        "*Say you accidentaly deleted it.*": #TODO:She probably won't believe this and ask you some more questions to prove you're the teacher or something, ask Abigial to help you with those questions.
                                             #TODO: Fill in the rest, you have to make it as the quest version doesn't already have this.
                                             "Filler"
  
  
  
          "No, I am... " if not persistent.name == "Sam":
               li "[persistent.name]? That doesn't really ring a bell right now..."
               jump call_lilaHangupPhone
               label call_lilaHangupPhone:
                    li "In any case, I have to go now. I'm expecting a call from my daugther's teacher soon so I can't be on the line with someone else."
                    n "And just like that she hung up on you."
                    jump Game_start2
               

          "I am a Sam, but not the Sam you're waiting for." if persistent.name == "Sam":
               li "Huh, another Sam? What are the chances of that?"
               n "You can hear her chuckle at the other end of the line."
               li "The universe is funny like that sometimes, isn't it Sam?"
               jump call_lilaHangupPhone







label doNotPickUpThePhone:
     if persistent.lildeaths == 0:
          $ fakeouttitle = True
          if persistent.times_phone_declined == 0:
               n "You stood up your date before even knowing what she was like, why?"
               n "Just because you could?"
               n "Just because that was an option?"
               n "The name of the game is \"Good date with Lilith\" so unless you like not playing this game you better choose the other choice next time."
               #TODO:Find a way to lie about the name of the game in renpy so this can be a shocking reveal later.
     elif persistent.lildeaths == 1:
          n "Oh wow, that was quick."
  
          n "You don't really like confronting your problems, right?"
          n "All those potential choices you could make to change something, anything."
          n"And your first attempt is to just... give up?"
          n "I guess you are allowed to, it just kind of feels like a waste to have this entire game made only for you to see one path and just quit."
          n "There has to be more, right?"
          #Ending
          "The quitter ending."
          $ persistent.ending_quitter = True
          $ lilithAliveEnding = True
          $ persistent.game_credits = True
 
     elif persistent.lildeaths <= 20:
          if persistent.kokiri_knowledge == True and persistent.kokiri_death_1 == True:
               n "Maybe it's for the best..."
               n "But is it really?..."
               #Ending
               "An ending."
               $ persistent.ending_anEnding = True
               $ lilithAliveEnding = True
               $ persistent.game_credits = True
          elif persistent.kokiri_knowledge == False:
               n "I have a feeling you are really close to a breakthrough, maybe there is something you are missing?"
               n "You could also just stop here, but there is so much more to see."
               n "Would you really want to miss all that extra stuff?"
               #Ending
               "The unseen content ending."
               $ persistent.ending_unseenContent = True
               $ lilithAliveEnding = True
               $ persistent.game_credits = True
 
     elif persistent.lildeaths > 20:
 
          n "Letting go is never easy."
          n "You had at least [persistent.lildeaths] opportunities."
          n "It's good to take it after all this time [persistent.name]"
          n "At the very least you know Lilith will be fine."
          n "At the very least you still have all of your memories of the times you spent together."
          n "If only you could somehow make more memories and have her survive..."
          n "If only..."
  
          #Ending
          "Letting go ending"
          $ persistent.ending_lettinggo = True
          $ lilithAliveEnding = True
          $ persistent.game_credits = True
 
 
     $ persistent.times_phone_declined += 1
     $ persistent.lildeaths -= 1
     jump gameOver







label restaurant_death_1_prevented_explanation:
     menu:
          "I was joking.":
               jump prevented_joking
  
          "I am in some sort of groundhog day scenario, I keep reliving the same day over and over.":
               jump prevented_groundhog
  
          "I am a psychic, I just knew you would die if I didn't do anything.":
               jump prevented_psychic
  
          "*Remain silent*":
               jump prevented_silent

label prevented_joking:
     if chinese == True:
          "Filler"
          #TODO: It's not really specific, just a bit morbid, but possible, she's probably just really anoyed and just ends up ordering her food and dying.
     else:
          l "You were... joking?"
          l "That doesn't make any sense at all."
          l "This is way too weird for me [persistent.name], I can't do this anymore."
          l "While I do appreciate you saving me I don't appreciate you just lying to me like this."
          jump car_death

label prevented_groundhog:
     l "So you mean to tell me that you've already been on this specific date before?"
     l "I mean, I'm really thankful for you warning me, that would probably haven't ended too well for me."
     l "But you got to admit that this really sounds contrived."
     l "I mean, this whole thing seems pretty weird to me. Can you atleast offer me some proof?"
     $ groundhog = True
     $ psychic = False

     menu:
          "I have no proof":
               jump prevented_noProof
          "Alright, think of a random number.":
               jump prevented_proof
label prevented_noProof:
     l "Listen, I'm really thankful for you saving my life and everything but I think you could atleast give me some form of proof."
     l "My head is hurting, I think I'm better of heading back to home."
     jump car_death




label prevented_proof:

     #Make it so that all proof can be selected here based on the thing you said:
 
     if groundhog == True:
          l "This sounds interesting.
          Alright, I've gotten my number!"
          menu:
               "It's 20.":
                    jump proof_answer_wrong
   
               "It's 38.":
                    jump proof_answer_wrong
   
               "It's -17.":
                    jump proof_answer_wrong
   
               "It's -72,8947, can we move on now?" if persistent.groundhog_answer_right_knowledge:
                    jump proof_answer_right
   
               "Alright, now tell me which number you got in mind.":
                    jump proof_giveAnswer

     elif psychic == True:
          l "Alright, I see where you are going with this."
          l "Lilith  looks at you with a sceptic look in her eyes although you can tell that she's secretly excited."
          l "I got my word, guess away magic [persistent.name]!"
          menu:
               "It's apple.":
                    jump proof_answer_wrong
   
               "It's abyss.":
                    jump proof_answer_wrong
   
               "It's photosynthesis.":
                    jump proof_answer_wrong
   
               "It's electronegativity obviously." if persistent.psychic_answer_right_knowledge:
                    jump proof_answer_right
   
               "Alright, now tell me which word you are thinking about.":
                    jump proof_giveAnswer

label proof_answer_wrong:

     if groundhog == True:
          l "That was the wrong number, I knew you wouldn't guess -72,8947!"
          $ persistent.groundhog_answer_right_knowledge = True
     elif psychic == True:
          l " That was the wrong word, I knew you wouldn't guess that it was electronegativity."
          $ persistent.psychic_answer_right_knowledge = True
     if love_meter >= 2: 
          l "Listen [persistent.name], I did actually have a pretty nice time together with you but this is too much for me."
          l "I would like to know the truth about what just happened and if you prefer to just lie then atleast have a trick to make it convincing or something."
     else:
          l "I'm not doing this anymore, I'm not sitting through your nonsense."
          l "I tried going on this date because I thought it could be fun, I was very wrong."
          if chinese == True:
               l "Thank you for \"saving\" me but I don't appreciate being treated badly and lied to."
          else: 
               l "I suppose I am thankful that you somehow saved me but just during this one date you already started treating me badly and lying to me."
               l "That's something I don't appreciate at all."

          l "So goodbye [persistent.name]. Don't try to contact me again."
 
     jump car_death



label proof_answer_right:
     if groundhog == True:
          n "Lilith looks absolutely flabergasted, her mouth is slightly opened and seems to be frozen for a moment or two."
          l "So you were actually speaking the truth?
          You really are living in some sort of groundhog-day like scenario?"
          l "Even with that proof it's pretty hard to get my brain to accept it."
          l "I feel like when I'm going to admit I believe you there is going to come an entire camera crew out of nowhere and I'll be made fun of in some bad tv show. But let's say I am starting to believe you a little bit so we won't have the camera crew barge in on us just yet."
          l "So what is this all about?"
     elif psychic == True:
          n "Suddenly you catch a glimpse of utter shock on Lilith's face."
          l "Wait, you... You guessed the word I was thinking of?"
          l "I mean sure, you said you would do that but I didn't expect for you to get it right if I'm being honest."
          l "This all feels so surreal, I mean I'm starting to believe you but I feel like if I say I completly believe you some cameracrew will come out from their hiding spots and make fun of me for believing something so stupid."
          l "So if I'd hypothetically believe you, what is all of this about?"
     jump proof_whatIsItAllAbout

label proof_giveAnswer:
     if groundhog == True:
          $ persistent.groundhog_answer_right_knowledge = True
          l "Uhm, alright, but that defeats the purpose of this doesn't it? The number I had in mind was  -72,8947."
          l "Listen, I'm really thankful for you saving my life and everything but I think you could atleast give me some semblance of an explanation." #TODO: This better fits with the joking path or the say nothing path.
          l "This is all a bit much for me, I think I'm better of heading back to home."
          jump car_death

     elif psychic == True:
          $ persistent.psychic_answer_right_knowledge = True
          l "Uhm, alright, but that defeats the purpose of this doesn't it? The word was thinking of is  electronegativity."
          l "Listen, I'm really thankful for you saving my life and everything but I think you could atleast give me some semblance of an explanation." #"" This fits better witht the joke and silence.
          l "This is all a bit much for me, I think I'm better of heading back to home."
          jump car_death




     label proof_whatIsItAllAbout:
          if groundhog == True:
               menu:
                    "I need some proof to make the past you trust me when I tell her the restaurants we wanted to go to are not safe." if persistent.needProof_knowledge:
                         jump proof_convincePast
    
                    "I'm trying to break my loop by making sure you don't die on this date.":
                         jump groundhog_breakingLoop
                    "I'm trying to escape fate to save you from dying.":
                         jump groundhog_escapeFate
    
                    "I have no time to explain, we need to get out of here, follow me." if persistent.beachroute_visited_knowledge:
                         jump explanation_noTimeToExplain
  
          elif psychic == True:
               menu:
                    "I need some proof to make the past you trust me when I tell her the restaurants we wanted to go to are not safe." if persistent.needProof_knowledge:
                         jump proof_convincePast
    
                    "You have an aura of death surrounding you Lilith, I'm trying to keep you safe with my powers.":
                         jump psychic_auraOfDeath
    
                    "I knew you would die on a date in a burger restaurant because of a wandering bullet so I figured I would be your date so I would be able to warn you." if burger:
                              jump psychic_dateToSave
    
                    "I knew you would die on a date in a cafe because of a that merlin so I figured I would be your date so I would be able to warn you." if cafe:
                              jump psychic_dateToSave

                    "I knew you would die on a date in a chinese restaurant because of an allergic reaction so I figured I would be your date so I would be able to warn you." if chinese:
                              jump psychic_dateToSave
    
                    "Well, while you were sitting there somehow I just felt that a merlin would escape the aquarium and kill you if I did nothing." if cafe:
                              jump psychic_justHelpingOut

                    "Well, while you were sitting there somehow I just felt that you would get shot." if burger:
                              jump psychic_justHelpingOut
    
    
                    
    
                    "Well, while you were saying you wanted to go for the Peking duck I suddenly knew there was something in it that would cause you sever allergic reactions." if chinese:
                              jump psychic_justHelpingOut
    
                    "I have no time to explain, we need to get out of here, follow me." if persistent.beachroute_visited_knowledge:
                              jump explanation_noTimeToExplain


label proof_convincePast:

     #TODO: Add some text here where she decides to tell the untold story in different parts to make this make more sense. Also make the story be told in double brackets? Maybe?
     if burger == True:
          $ persistent.story_start_knowledge = True
          l "Once upon a time there was a world, but the world doesn't concern this story."
          l "For the story we need to look high in the inkfilled sea some like to call the night."
          l "Floating in that sea is the majestic moon herself who guides us through the night and turns gold to silver, confidence to elegance."
 
     elif cafe == True:
          $ persistent.story_medium_knowledge = True
          l "The majestic moon is far from alone though, in the dark she is kept company by a thousand stars tha shine almost as bright as herself and one special raven with a silver crown."
          l "The little raven was a prince, his parents ruled their raven-kingdom on a nice looking kind throne carved out from the wood of an oak."
          l "The prince would one day inherit the throne but he still felt sad somehow. That was untill he noticed a silver light reflecting from his crown as he was between waking and dreams."
 
     elif chinese == True:
          $ persistent.story_end_knowledge = True
          l "The raven looked up and noticed the shining moon and from that day on he never left her side."
          l "They talk for hours, about everything and nothing. When the night would end in one part of the world the raven would follow the moon to another."
          l "To this day you can still clearly see them when they come visit you."
          l "The end."
 
     l "That's the end of this part of the story, like I said you are the only person I've ever told this to so I hope you'll make good use out of it."
     menu:
          "I sure will! ":
               jump restaurant_death_2




label groundhog_breakingLoop:
     l "So..."
     l "You mean that I have died multiple times in here and that every time I do so you get sent back in time?"
     l "So does you saving me just now mean that we are save? That your whole looping problem is able to stop?"
     menu:
          #Make this a lie based on if the player has already seen the second death in the restaurant they are currently in.
          "Yup, I broke the loop for once and all.":
               jump groundhog_breakingLoop_loopGone
               #Make this be a different text based on how she will die.
          "Actually you are still going to die." if cafe == True and persistent.cafe_death_2 == True or chinese == True and persistent.chinese_death_2 == True or burger == True and persistent.burger_death_2 == True:
               jump groundhog_breakingLoop_loopStillExists
label groundhog_breakingLoop_loopGone:

     if cafe == True and persistent.cafe_death_2 == True or chinese == True and persistent.chinese_death_2 == True or burger == True and persistent.burger_death_2 == True:
          n "You feel a pit in your stomach as you think about what will happen next."
          n "Didn't you want to break the bad news to her?"
          n "Or did you yourself want to believe for a second longer that she would live?"
          n "I get it, ignorance is bliss after all, isn't it?"

     n "A wide grin appears on Lilith's face."
     l "So, did we just cheat death?"
     l "We actually did it, didn't we?"
 
     l "Thank you so much for saving me [persistent.name]!"
     l "Is it weird for me to feel absolutely ecstatic right now?"
     menu:
          "Absolutely not! This has never happened to someone before so I doubt there is a standard way to react when it comes to this.":
               jump loopGone_strangeSituation
          "Absolutely not! You have every right to feel happy. We saved you from death itself!":
               jump loopGone_everyRightToBeHappy
          "Absolutely not! I am also happy for us.":
               jump loopGone_happyForYou
label loopGone_strangeSituation:
     l "I suppose you are right, this is quite an exceptional scenario. I thought that atleast one person must've had this happen to them before, but those odds seem pretty low in retrospect."
     n "Lilith gives you a thumbs-up and a cute laugh."
     l "And despite the odds you did everything you could and saved me! You are... sort of my hero now?"
     n "Lilith begins to turn a bright red, she begins to more closely resemble a cute tomato than a human."
     n "Somehow she must've noticed her excessive blushing as she covers her face up with her hands and begins to giggle."
     l "Sorry, once I get blushing I turn beet red really quickly."
     jump restaurant_death_2
label loopGone_everyRightToBeHappy:
     l "Huh, you are right, aren't you?"
     l "I shouldn't seek justification for my feelings.
     Especially now, we literally cheated death itself so I have every right to feel ecstatic!
     Well, it was mostly your work but still, that doesn't happen every day."
     n "Lilith lets out a small chuckle."
     l "I suppose that it happened quite a few days for you but still, that's cheating!"
     n "Lilith pauses for a few seconds while looking you into the eyes.
     A soft smile has formed on her lips."
     l "Thank you [persistent.name], thank you for both saving me from my impending doom and for this date.
     I am really having a blast right now, although I must admit I had a slight headache trying to get my head around this whole thing."
     jump restaurant_death_2

label loopGone_happyForYou:
     l "Then come dance with me!"
     n "Lilith gets up and beckons you closer with a wide smile."
     n "The two of you begin to move around with all kinds of limb-shaking that probably could be considered dancing by some."
     if burger == True:
          if persistent.burger_death_2 == True:
               jump loopGone_happyForYou_real
          else:
               jump loopGone_happyForYou_fakeout
     elif cafe == True:
          if persistent.cafe_death_2 == True:
               jump loopGone_happyForYou_real
          else:
               jump loopGone_happyForYou_fakeout
  
     elif chinese == True:
          if persistent.chinese_death_2 == True:
               jump loopGone_happyForYou_real
          else:
               jump loopGone_happyForYou_fakeout
label loopGone_happyForYou_fakeout:
     n "You are happy to indulge in the dancing, as it makes you spend some precious time with Lilith. You are however not all too happy when you think about what is going to happen next, you try to ignore it but the thought keeps lingering in your head all the same."
     jump restaurant_death_2
label loopGone_happyForYou_real:
     n "Knowing that you finally saved Lilith fills you with seemingly endless energy."
     jump restaurant_death_2





label groundhog_breakingLoop_loopStillExists:
     l "Ah, so the loop still exists?
     I mean, me dying constantly doesn't seem like it's much fun but look at it from the bright side!"
     l "We could form a team to be true heroes!  With your ability to relive the same moments and with my ability to... well die, I suppose, we could be practically unstoppable!
     We would be able to prevent disasters even before they happen."
     l "Well, that is if we ever get out of here alive in the first place."
     n "Lilith lets out a small chuckle but the concern in her eyes is clearly visible."
     l "Sorry, this is still a bit much for me.
     I mean imagine that someone you were dating just told you that the two of you are stuck in a seemingly endless loop that always ends up with you dying.
     That would be pretty mind-boggling, wouldn't it?"
     l "Yes, I suppose that's one way to put it."
     n "Lilith lets out a small sigh and tries to give you a sincere smile."
     l "But it's not that useful to keep groaning about our situation, is it?
     Maybe it's a better idea to get some information that we can use."
     n "Lilith pauses for a few seconds."
     l "For example, what do you think will happen once we make it past this date? Past this day even, do you think you would be stuck in a loop of reloading day after day for the years that we spend together or that all of this will go away when we make it through today?"
     menu:
          "We might be in this situation for the rest of our lives.":
               jump loopStillExists_forTheRestOfOurLives




          "It should only be this day that keeps repeating, I hope so atleast.":
               l "Hmm, then I wonder what made you experience a groundhog day scenario on this day and not any other one."
               l "Would it really have been caused by our date? And if that's the case then what would you need to do to get out of it?"
               #TODO: The part below this kind of flows very strangely, examine how to make it feel better.
               if burger == True:
                    l "So when I was killed by that loose bullet you had to relive this day again, right?"
               elif cafe == True:
                    l "So when I was killed by that merlin you had to relive this day again, right?"
               elif chinese == True:
                    l "So when I died because of my allergy you had to relive this day again, right?"
               n "You nod."
               l "Hmm, in that case I would advise you to try to not get me killed."
               n "Lilith burst out to laughter. It's not really the joyous kind, you can feel the discomfort seeping from behind the facade."
               l "Sorry, I'm not really accustomed to this whole thing yet. I have no clue how I could help you but if you have anything in mind just let me know."
               jump restaurant_death_2


label loopStillExists_forTheRestOfOurLives:
     l "I really hope that will not  be the case, I don't want to die too early ofcourse, but when I have lived a long life and my time has come I'd be more than happy to go."
     n "Lilith looks at you as to make sure you're processing all of this, you give her a silent nod and she continues."
     l "I mean, imagine what a nightmare it must be for the both of us."
     l "You would be cursed with always having to save an old lady that could literally die any moment, always just buying her a few extra hours."
     l "And I would be cursed with never getting to pass away, I would be the oldest person that was ever alive and just be a living heap of flesh and wrinkles after a year or 200."
     l "No matter how much I would pray for the sweet release of death it would never come, or atleast I would never be aware that it came as you would just rewind and try to fix it."
     n "Lilith shudders."
     l "Let's just hope that this loop will end for the both of us before we get at that point."
     n "Shaken by the images of a living heap of flesh and wrinkles you can only agree with her."
     jump restaurant_death_2


label groundhog_escapeFate:

     l "So I keep dying? Interesting..."
     if burger == True:
          l "Before that stray bullet I never really got in close contact with death."
     elif cafe == True:
          l "Before that merlin I never really got in close contact with death."
     elif chinese == True:
          l "Before that alleged allergic reaction I never really got in close contact with death. Atleast not to the point of literally dying."
          #Technically she had, she just never died, I'm talking about the allergic reaction.
     n "Lilith scratches her head."
     l "So, why do you think I keep dying all of the sudden?"
 
     menu:
          "I think it has to do with me, everytime we are together you seem to end up dying.":
               jump groundhog_escapeFate_myFault
 
          "It seems like fate wants it for some reason.":
               jump groundhog_escapeFate_yourFate


label groundhog_escapeFate_myFault:
     n "Lilith bursts out laughing."
     l "Sorry, it's still a bit much to take in right now."
     l "Sometimes I laugh when I'm uncomfortable."
     #TODO:Add some text in between these two parts.
     l "So, our dates always end up killing me, right?"
     l "Have you ever considered not dating me?"

     menu:
          "Actually I tried to warn you about your death, tried to break up with you, tried just not showing up but it all ended with you dying either way.":
               #TODO:Make this one only appear if you have actually tried all of those things. This is also a lie. Not picking up the phone makes her live.
               jump escapeFate_myFault_ITriedTo
  
          "But I love spending time with you, I'd hate to have to throw all of that away.":
               jump escapeFate_myFault_butILoveYou
  
          "I haven't tried that yet actually.":
               jump escapeFate_myFault_didNotTryYet
label escapeFate_myFault_ITriedTo:
     "Filler"
     #TODO: Finish this text on this label (No quest precedent)
label escapeFate_myFault_butILoveYou:
     l "Well, I also like spending time with you..."
     l "It would be a shame if we had to sacrifice it all."
     l "Besides, wheter you would or not do that, I would never know about it or this conversation."
     n "Lilith lets out a little laugh."
     l "Funny how those things work right?"
     n "Lilith scratches her head."
     l "But if all else really fails we might have to consider not seeing eachother again."
     n "She lets out a big sigh."
     l "However, I have a feeling that there must be another way to solve our little problem, I'm practically sure of it!"
     l "If all else fails we'll just have to confront the Moirai themselves!"
     n "She seems to be taking all of this pretty well for a woman who just heard that she dies repeatedly."
     #TODO:Maybe a little too well, change this slightly
     jump restaurant_death_2

label escapeFate_myFault_didNotTryYet:
     l "Well, maybe that's worth looking into then even though it's probably quite a long shot."
     menu:
          "But that would mean we wouldn't know eachother like this, if the loop breaks I will not have been on this date with you. ":
               jump didNotTryYet_neverMeet

label didNotTryYet_neverMeet:
     n "Lilith rubs her chin for a moment."
     l "Hmm, I suppose you are right..."
     l "Once you manage to break the loop by not showing up or something like that I wouldn't want to have something to do with you in the first place."
     l "Besides, even then I doubt you would be able to convince me about this whole groundhog day thingy."
     l "You wouldn't be able to relive that moment anymore so your tricks would quite literally be useless "
     n "Lilith looks saddened for a moment before she tries to give you a wide smile, you can tell it's quite forced."
     l "You know, I got a feeling that won't be the case so you can always give it a shot if you want."
     n "She grows slilent for a moment."
     l "But just in case something does end up happening and causes you to never be able to see me again."
     l "I want you to know that I really liked our time together..."
     jump restaurant_death_2


label groundhog_escapeFate_yourFate:
     "Filler"
     #TODO: Finish this path because currently it leads nowhere. (No quest precedent)


label psychic_auraOfDeath:
     l "An aura of death? Are you joking?"
     n "Your serious look tells Lilith you are anything but joking."
     l "Well, thanks for trying to save me, so far you're doing an absolutely fantastic job!"
     l "So, do you think it is over? Did you finally stop that weird aura of death you were speaking of?"
     menu:
          "I sure did!":
               jump explanation_stoppedDeath
 
          "Actually you're still going to die, this time because of a swarm of geese." if chinese and persistent.chinese_death_2:
               jump explanation_stillDying

          "Actually you're still going to die, this time due to a gas explosion." if burger and persistent.burger_death_2:
               jump explanation_stillDying

          "Actually you're still going to die, this time you will drown." if cafe and persistent.cafe_death_2:
               jump explanation_stillDying
               
 
label explanation_stoppedDeath:
     if burger == True and persistent.burger_death_2 == True or cafe == True and persistent.cafe_death_2 == True or chinese == True and persistent.chinese_death_2:
          n "I'm not entirely sure if you believe that player."
          n "You have seen what comes next, right?"
          n "Do you think something is going to change?"
          n "Or are you just lying to yourself?"
          n "..."
          n "Or maybe you are lying to her?"
          n "Either way, I guess we will soon see how things turn out."
     l "Great, now we can just continue enjoying our date!"
     #That is a really weird response, fix it a bit.
     n "Lilith gives you a wide smile, you feel like you could beat the universe itself."
     menu:
          "We actually did it, I still can't believe it!":
               jump restaurant_death_2


label explanation_stillDying:
     #TODO: Add some extra dialogue here.
     "Filler"
     jump restaurant_death_2

label psychic_dateToSave:
     l "Seems rather convoluted doesn't it?"
     l "Couldn't you just have found me somewhere else and told me like a week before it would happen?"
 
     menu:
          "Oh yeah, and you would just believe a random person telling you that you will die of an allergy in a chinese restaurant on a specific day?" if burger:
               jump psychic_dateToSave_youWouldNotBelieveMe
  
          "Oh yeah, and you would just believe a random person telling you that you will die by being crushed by a great white shark in a fish themed cafe on a specific day?" if cafe:
               jump psychic_dateToSave_youWouldNotBelieveMe
  
          "Oh yeah, and you would just believe a random person telling you that you will die because of a gunshot wound in a burger restaurant on a specific day?" if chinese:
               jump psychic_dateToSave_youWouldNotBelieveMe

label psychic_dateToSave_youWouldNotBelieveMe:
     l "Hmm, you made a fair point there, even if I would have believed you I don't think I would have actually been able to remember it when I needed that knowledge."
     l "It still sounds like there were better, less convoluted ways to keep me from dying but I'm still really thankfull that you saved my life."
     l "We actually cheated death itself, take that death!"
     menu:
          "I think it may not be really wise to tease death itself. ":
               jump youwouldntbelieveme_doNotteaseDeath
 
          "Take that death, we've won, woohoo!":
               jump youwouldntbelieveme_teaseDeath




          "Actually you're still going to die if we keep sitting here, this time it'll be a gas explosion." if burger and persistent.burger_death_2:
               jump explanation_stillDying
          "Actually you're still going to die if we keep sitting here, this time by an army of angry geese." if chinese and persistent.chinese_death_2:
               jump explanation_stillDying
          "Actually you're still going to die, this time by drowning." if cafe and persistent.cafe_death_2:
               jump explanation_stillDying

label youwouldntbelieveme_doNotteaseDeath:
     l "Common, let's celibrate. We just escaped death!
     Don't be so worried, what's the worst thing that could happen?"
 
     menu:
          "Yeah, you're probably right... Wait, why did you say that? Now we are going to die for sure.":
               jump restaurant_death_2

label youwouldntbelieveme_teaseDeath:
     $ teaseDeath = True
     n "Lilith and you high five eachother, you've won. Congratulatons!"
     if persistent.teaseDeath_fakeOut_knowledge == False:
          n "That is what I would say if either of us thought that was the truth. Afterall, you came back here for a reason didn't you?"
     jump restaurant_death_2

label psychic_justHelpingOut:
     if chinese == True:
          l "So you somehow sensed I'm allergic to something in this dish? That sounds really far-fetched if I'm being honest."
          l "There is certainly a possibility that there's something in this that makes me have an allergic reaction without me knowing, but you {b}sensing{/b} it?"
          if love_meter == 1:
               l "What, are you a psychic allergist? Well, I get the gist alright, the gist that you are just making this nonsense up as you go."
               l "And yet... there is {i}some{/i} truth to what you are saying." 
               l "I feel it somehow. I guess that makes me a psychic too, huh?"
               n "She practically scoffs those words at you."
               l "So, am I safe now? Or is there still something else?"
          else: 
               l "That's where I struggle to accept this whole scenario a bit."
               l "But somehow, I don't think you're lying about the allergy thing. Besides, I can either believe you or risk it and maybe die."
               l "The food here is great, it's to metaphorically die for. But I wouldn't like to make that literal."
               l "I think I'll just order something different, probably something small though. Being warned of a possible death isn't exactly great for your appetite."
               l "But anyway, I should probably think about something else first, am I safe now?"
     else:
          l "Wow, that's quite the story. It's a bit hard to believe but I guess you are right, I don't really want to think about what would have happened if you didn't interfere..."
          l "So am I in the clear now?"
     menu:
          "Yup, you are completly safe now!":
               jump psychic_justHelpingOut_totallySafe
          "Actually I can sense another death approaching, quickly.":
               "Filler"
               #TODO: Make this a sort of "stilldying for the psychic part. Lilith suggest running out but it doesn't work due to the car."

label psychic_justHelpingOut_totallySafe:
     n "Lilith gives you a thumbs up and plays a few notes on an air gitar."
     l "We actually did it, that's awesome!"
     n "Lilith opens her arms and motions to you with her head."
     l "Come and give me a hug [persistent.name]"
     $ hugRequestedBeforeDeath = True
     jump restaurant_death_2


label prevented_psychic:
     $ psychic = True
     $ groundhog = False
     if burger == True:
          l "So what you are saying is that you knew I was going to get shot because you're psychic?"
          l "I mean, I'm thankful for you saving my life and all but you got to admit that sounds kind of far fetched."
          l "Do you have any proof to maybe show you're a psychic?"
     if chinese == True:
          l "So what you are saying is that you knew I was allergic to something in this dish because you are psychic?"
          l "Well unless you got any proof I'm not even sure if I'm really allergic to that Peking duck in the first place so you got to admit that this sounds very weird."
     if cafe == True:
          l "So what you are saying is that you knew I was going to be skewered by a merlin because you are psychic?"
          l "I mean, I'm thankful for you saving my life and all but you got to admit that sounds kind of far fetched."
          l "Do you have any proof to maybe show you're a psychic?"
 
     menu:
          "I've got no clue what to tell you honestly":
               jump prevented_noProof
 
          "Alright, pick a word, doesn't matter wich one but make it a hard one to guess.":
               jump prevented_proof 

label prevented_silent:
     "Filler, make her weirded out by your silence."
     #TODO: Do just that, make her freak out by your silence and leave.
     jump car_death



label explanation_noTimeToExplain:
     #TODO add all the other ones, so burger, cafe, and chinese carcaught untrue ("no time to explain" in Quest version)
     if chinese == True:
          if car_caught == True:
               #Write some small describing text that slowly grows on how you prevented all the other deaths.
               #TODO: Make sure that there is an alternative version of this that runs if you have seen the previopus parts already.
               if persistent_fleeingDeaths_counter_knowledge == 0:
                    n "You run through the exit of the restaurant and brace yourself for the impact of a speeding car."
                    n "Nothing happens, the police indeed managed to take care of the drunk driver."
               else: 
                    n "You run through the exit of the restaurant, knowing full well that the red Sedan has been dealt with."
               n "Lilith and you continue to run as if death itself is chasing you."
               n "Lilith is still very confused but she can feel the fear that is running through your body and she fears whatever made you so scared to begin with."
               n "As you are running along the side of an empty street you suddenly hear the screeching of wheels and loud laughter."
               if persistent_fleeingDeaths_counter_knowledge == 0:
                    n "As you look behind you you see a bus full with elderly people coming straight towards you and her, you manage to jump away from it just as it would've hit you but Lilith ofcourse doesn't."
                    n "You know what you have to do, you've come too far to just give up now."
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu: 
                         "I retry.":
                              jump explanation_noTimeToExplain
                    
               elif persistent_fleeingDeaths_counter_knowledge == 1:
                    n "This time you manage to push Lilith away just as she would get hit by the bus, you both make it out alive and well."
                    n "When she gets back up you both continue running, as if you were trying to escape fate."
                    n "Just moments after the first death you prevented you can see a truck coming towards you at full speed, Lilith doesn't make it once again."
                    n "You curse at the skies, trying to reach the one responsible for Lilith's countless deaths himself."
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu: 
                         "I retry.":
                              jump explanation_noTimeToExplain
               elif persistent_fleeingDeaths_counter_knowledge == 2:
                    n "This time Lilith makes it out alive, you've done these things so many times it almost just seems like you're back in an instant, time is blending together."
                    n "Lilith and you continue running untill you hear the sound of thunder, lightening strikes closer to Abigail then you like but she seems to escape unharmed."
                    n "That's when you notice oil leaking from the crashed truck, it's set ablaze by the lightening."
                    n "The fire tries to consume her, the hungry flames don't let off until she is beyond saving."
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu:
                         "I retry once again.":
                              jump explanation_noTimeToExplain
               elif persistent_fleeingDeaths_counter_knowledge == 3:
                    n "You lead Lilith to a diverging street where the oil and the truck shouldn't be a problem."
                    n "As Lilith and you are running once again you can feel a terrible trembling coming from the ground."
                    n "It almost resembles an earthquake, but not quite."
                    if persistent.kokiri_death_4 == True:
                         n "It actually kind of reminds you of what you felt when the ufo revealed itself in the kokiri forest."
                    n "It also doesn't last as long as the earthquakes usually do, you feel thankful when the earth stops trembling and Lilith is still left unharmed."
                    n "However, you thought she was safe too soon and a safety hazard of a building that shouldn't have  been built in the first place collapses in on her."
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu:
                         "Retry. Retry. Retry.":
                              jump explanation_noTimeToExplain
               elif persistent_fleeingDeaths_counter_knowledge == 4:
                    n "This time Lilith and you make it to your car which was parked a few streets away from the restaurant, you decided that it would be the best plan to just get away from this village as fast as you can."
                    n "As you are driving away from the village you finally arrive at a bigger city, maybe you and Lilith will be safe here?"
                    n "You look at Lilith for a moment, just hoping that death will have mercy on her."
                    n "Suddenly you hear a cacophony of animal sounds, as you look in the side mirrors of your car you can see a swarm of animals running towards your direction."
                    n "You try to go as fast as you can but then you realize something."
                    n "You forgot to fill up your car, just as you realize that it abruptly stops, you try to persuade the car into going a tad further but your efforts are futile."
                    n "The animals run on top of your car, now this isn't a problem except that there were also elephants among those animals."
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu: 
                         "Sigh, retry.":
                              jump explanation_noTimeToExplain
               elif persistent_fleeingDeaths_counter_knowledge == 5:
                    n "Now you've made sure to gas up your car for the inevitable chase scene, as you are driving away as fast as you can from the animals, more buildings start to collapse, now even the sturdier looking ones are doing so."
                    n "These scenarios are becoming more and more unjustified, you shake your head and try to focus on getting Lilith alive and well out of this mess."
                    l "Listen, I really don't think we are safe here. Even if we make it out of this city, where are we going to go then?"
                    l "It's not like we can just leave this planet so death will always follow me."
                    n "Lilith has given you the greatest idea, you give her a kiss on the lips and tell her she is genious."
                    n "Lilith turns beetred."
                    l "Oh I wouldn't know about that..." 
                    l "But hang on, you are not seriously thinking about leaving this planet, right?"
                    l "How would we even be able to do that?"
                    n "You stop the car for a moment, waiting for death to cath up with both of you, and it sure does so fast."
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu: 
                         "Retry, this could be it!":
                              jump explanation_noTimeToExplain
               elif persistent_fleeingDeaths_counter_knowledge == 6:
                    n "This time you don't leave the village, instead you remember the ufo that is hidden in Kokiri forest. Maybe you could use it to escape."
                    n "Eventually you find it, you and Lilith climb inside it."
                    n "However, an onslaught of buttons, levers and contraptions you can't identify await you."
                    
                    
                    menu: 
                         "I'll retry untill I get it right!":
                              n "After about a hundred or so attempts you manage to take of with the spaceship without plummeting to your death instantly."
                              $ persistent_fleeingDeaths_counter_knowledge += 1
                              jump explanation_noTimeToExplain
               elif persistent_fleeingDeaths_counter_knowledge == 7:
                    n "As you and Lilith take of into space you can see the sun absorbing the earth, you know that that should've happened like a million or so years later but it happened now. These deaths are really getting out of hand aren't they?"
                    n "Suddenly you are hit by a speeding ufo. Your ship analyses the situation and informs you that the driver was drunk."
                    n "It seems that even in space there are drunk drivers."
                    menu:
                         "Retry. Retry. Retry and retry once again.":
                              $ persistent_fleeingDeaths_counter_knowledge += 1
                              jump explanation_noTimeToExplain
               elif persistent_fleeingDeaths_counter_knowledge == 8:
                    n "Everything starts to blend together even more, sometimes you're not even sure if you are actually progressing in the story or not."
                    n "Death by colliding stars."
                    
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu:
                         "Retry.":
                              jump explanation_noTimeToExplain
               elif persistent_fleeingDeaths_counter_knowledge == 9:
                    n "Death by a storm of asteroïds."
                    
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu:
                         "Retry.":
                              jump explanation_noTimeToExplain
               elif persistent_fleeingDeaths_counter_knowledge == 10:
                    n "Death by crashlanding on a planet."
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu: 
                         "Retry.":
                              jump explanation_noTimeToExplain
               else:
                    n "The universe grows calm for a moment, it seems like you got through the constant barrage of deaths." #These three lines only trigger in the quest version if "Starttalk" is not set, I'm not sure what that is anymore.
                    n "You set the ship on auto-pilot and move away from the controls."
                    n "Lilith is standing there, she seems to be quite scared but is taking it pretty well all things considered."
                    menu:
                         "*Talk with Lilith*":
                              #TODO: Add some extra choices here? Not too much though!
                              l "What just happened [persistent.name]?"
                              l "How did you know about the Kokiri forest?"
                              l "How did you know there was an ufo there?"
                              l "And how in the world do you know how to fly it succesfully?"
                              l "What is this all about?"
                              l "{size=*0.5}Are you... an alien?{/size}"
                              if groundhog == True:
                                   l "Or are your really in a groundhog day scenario?"
                              else:
                                   l "Or are you really a psychic?"
                              
                              menu:
                                   "Actually neither. You are basically in a game. I am a player of it and need to keep you from dying.":
                                        l "The speed with which you said that..."
                                        l "I assume we've had conversations like this a few times?"
                                        n "You nod your head."
                                        l "I see..."
                                        l "So if we've done this multiple times, does that mean we went to all three restaurants?"
                                        menu:
                                             "We did actually, we also went to the Kokiri forest and visited the beach.":
                                                  l "..."
                                                  l "You know about the Kokiri forest, the same one I'm thinking of right now?"
                                                  l "I've never told anyone about that."
                                                  l "I'm not sure how you managed to convince another version of me to tell you about it but that's quite clever nonetheless [persistent.name]."
                                                  l "Sounds like we did quite a lot on our first date."
                                                  n "Lilith laughs."
                                                  l "It's a shame I don't remember anything of it though..."
                                                  l "What was your favourite first date?"
                                                  menu:
                                                       "My favourite part was the beach.":
                                                            $ favouriteFirstDate = "beach"
                                                            jump ufo_talk_favouriteFirstDate
               
                                                       "My favourite part was the burger restaurant.":
                                                            $ favouriteFirstDate = "burger"
                                                            jump ufo_talk_favouriteFirstDate
               
                                                       "My favourite part was the cafe.":
                                                            $ favouriteFirstDate = "cafe"
                                                            jump ufo_talk_favouriteFirstDate
               
                                                       "My favourite part was the Chinese restaurant.":
                                                            $ favouriteFirstDate = "chinese"
                                                            jump ufo_talk_favouriteFirstDate
               
                                                       "My favourite part was the Kokiri forest.":
                                                            $ favouriteFirstDate = "kokiri"
                                                            jump ufo_talk_favouriteFirstDate
     

label ufo_talk_favouriteFirstDate:
     #TODO: Give her like a small line about what she thinks about your favourite date
     if favouriteFirstDate == "beach":
          "Filler"
          l "And what was your favourite moment of that particular date [persistent.name]?"
     elif favouriteFirstDate == "burger":
          l "I knew you would love it there! Rose's burgers are just unbeatable when it comes to their amazing taste."
          l "Just thinking about it now makes me really yearn for a juicy cheeseburger."
          n "You can hear Lilith's stomach growl as she quickly places a hand on it as to quiet it down."
          n "She turns beetred."
          l "Uhm anyway, what was your favourite moment of that particular date [persistent.name]?"
     elif favouriteFirstDate == "cafe":
          "Filler"
          l "And what was your favourite moment of that particular date [persistent.name]?"
     elif favouriteFirstDate == "chinese":
          "Filler"
          l "And what was your favourite moment of that particular date [persistent.name]?"
     elif favouriteFirstDate == "kokiri":
          "Filler"
          l "And what was your favourite moment of that particular date [persistent.name]?"
          
     
     $ renpy.input("My favourite moment was...")
     l "That sounds really lovely [persistent.name]!"
     $ renpy.input("")
     l "That sounds great!"
     $ renpy.input("")
     l "..."
     $ renpy.input("")
     l "..."
     n "Lilith is staring right into your soul without saying a word."
     n "She somehow seems to have lost everything that made her feel human."
     $ renpy.input("")
     l "..."
     n "Once every room she was in felt more warm because of her presence, now this iron ship feels colder than ever with her silence in it."
     n "It's almost seems as if she has run out of things to say."
     $ renpy.input("")
     n "In her frozen, wordless nature she seems more like a replica of the woman you once knew than the real deal."
     n "You have seen her die many times but this somehow feels even more wrong."
     n "A fate worse than death has befallen her."
     $ renpy.input("")
     n "Just then you hear something. Not Lilith, it's a loud beeping sound coming from the metal ship itself."
     ship "Alert: Universal inconsistency has been detected."
     ship "Previous stabilisation attempts proved fruitless."
     ship "Implosion of universe is set in motion as last effort to remove inconsistency."
     ship "Brace yourself."
     ship "Brace yourself."
     ship "Brace yourself."
     ship "{size=*0.5}All hope is lost.{/size}"
     ship "Brace yourse-"
     jump ufo_crash

label ufo_crash:
     #TODO: Have it only be your soul and not body that survived the crash.
     #TODO: Reality is glitching so that you won't have to draw every picture.
     n "After awakening from the dark slumber your eyelids are still shut close as if they want to go back to sleep."
     n "You feel like you need to go back to sleep. Nothing makes sense anymore."
     n" Probably the result of the entire universe literally collapsing in on you."
     n "On you and on..."
     n "On Lilith"
     n "The thought of Lilith takes you out of this confused state of mind in an instant."
     n "You open your eyes and get back up."
     n "You look around in search of her but all you can find is bright white emptiness."
     n "Bright white emptiness and a floating  trail of gigantic polaroids. The white borders of the polarioid were seemingly melting over in the emptiness."
     n "As you continue looking around you notice you are standing on one of those giant polarioids, it's a picture of your messy room. Hang on, how is that possible? How is any of this possible?"
     n "Your not sure if you want to know who took those pictures but regardless the only way is forward by following the trail."
     $ polaroidzone_picture = 0
     jump ufo_crash_polaroids
 
label ufo_crash_polaroids:
     #TODO: Add some small descriptions of each picture you jump on
     if polaroidzone_picture == 1:
          n "You jump to the next picture."
     elif polaroidzone_picture == 2:
          n "You keep jumping from picture to picture."
     elif polaroidzone_picture == 3:
          n "At first it doesn't seem like you are making much progress."
     elif polaroidzone_picture == 4:
          n "But after a while you see something coming closer and closer."
     elif polaroidzone_picture == 5:
          n "That \"something\" you saw seems to be human, it has a human looking figure anyway."
     elif polaroidzone_picture == 6:
          n "You didn't jump far enough, you barely manage to grab the border of the polaroid and pull yourself up."
          n "You take a moment to breath after performing such a feat. While you do you look once more at the mysterious figure."
          n "The figure wears a grey hoodie."
     elif polaroidzone_picture == 7:
          n "Your legs are beginning to get really tired, luckily it seems as if you are getting closer to the figure. "
          n "They have their back turned towards you."
     elif polaroidzone_picture == 8:
          n "Only one picture is between you and the figure, which is standing on a picture aswell, you ignore the cramp in your legs."
     elif polaroidzone_picture == 9:
          n "The next jump will land you on the picture the figure is standing on, right behind them."
     elif polaroidzone_picture == 10:
          jump ufo_crash_polaroids_James
 
     menu:
          "*Jump to the next picture*":
               $ polaroidzone_picture += 1
               jump ufo_crash_polaroids

label ufo_crash_polaroids_James:
     j "Welcome [persistent.name], I was expecting you."
     j "This place must feel pretty strange to you, let's move to a more familiar one."
     j "You and the boy are now both standing in your room."
     j "Don't be fooled, this room doesn't exist anymore due to the universe collapsing in on itself, it's just an illusion."
     j "I just thought this place might be easier on the eyes if you want to talk with me."
     j "We need to talk, about... about all of this."
     j "I assume you already know who I am?"
     menu:
          "Yes, you must be James. Lilith told me about you before.":
               #TODO: Only make this popup if she really told you about him before.
               $ persistent.met_james = True
               j "Ah, I thought she would mention me eventually."
               j "I'd imagine it would be pretty hard to get this far while never having heard about me."
               j "After all, it's hard for her to fully deal with what happened."
               j "I understand completely but I had hoped everyone would have moved on more easily."
               j "Then again, I shouldn't be saying that, after all I'm still here even when I could have moved on years ago."
               n "It's quiet for a moment, you hear nothing except a low droning sound."
               j "James gives you a curious look, you're not quite sure why but you feel slightly unsettled."
               j "What are your thoughts  on Lilith [persistent.name]?"
               n "You are pretty surprised by that question."
               menu:
                    "I really love her.":
                         $ loveher = True
                         $ persistent_jamestalk_iloveher_knowledge = True
                         j "If that's the case then this talk might be easier then I thought."
                         j "You have seen Lilith die about [persistent.lildeaths] times, right?"
                         n "You nod, you can still remember all the times she died."
                         n "That doesn't stop you from wishing you could forget though."
                         j "And you are trying to keep her safe so that she will not die, right?"
                         n "You nod."
                         if persistent.lilithAliveAndRetriedCounter >= 1:
                              j "And yet you came back after she didn't die, why?"
                              jump jamesChat_whyDidYouReturn
   
                    "I really like her.":
                         $ likeher
                         "Filler"
                         $ persistent_jamestalk_ilikeher_knowledge = True
                         #TODO: Fill in, there is no quest precedent for this.
                    "I don't really think anything of her, she's just a game character.":
                         $ justgame = True
                         j "This is going to be pretty hard..."
                         j "To you this is all a game but to us this is our world."
                         j "But even though the world seems to keep resetting your actions still have consequences."
                         j "Even though the world seems to keep resetting you managed to come here, to have the entire universe collapse in on itself."
                         j "Even though the world seems to keep resetting every ending you have seen has happened. Every action you have taken has been done."
                         j "Even if it doesn't always seem like that. You seperate yourself from the worlds where things didn't go your way but that doesn't make them less real than the one where things will eventually go your way."
                         j "Those abandoned worlds are still out there, [persistent.name]. I know that because I can see them, I am watching over the infinite worlds that exist in this game."
                         j "This place is the weakest link to every world, a sort of dying breath of those worlds. Here it is possible for souls to linger instead of crossing over into the Darkness."
                         j "There is only one Darkness but there are many versions of this place. So through the Darkness every world is linked together and since we can observe the Darkness here we can observe the other worlds aswell."
                         j "I have seen many more worlds than you have crossed."
                         j "I have seen many other crossers, I have even talked to some of them before."
                         j "I have changed some of their minds, made them see this game as more than just a game."
                         j "But that also didn't work for quite a few of them."
                         j "And now you are here and I am telling you the same thing as I was telling the previous ones, as I will tell the next ones."
                         j "It all seems pointless sometimes if I'm being entirely honest with you. You are stuck in a loop, right?"
                         j "And you hope that once you break out of it you will be able to move on to the next day."
                         j "Well for me that next day always comes but the loop follows suit."
                         j "I never get the luxury of dreaming what will happen when I get out of the loop, this place is my loop."
                         j "The only way to break it would be to enter the Darkness but I'm not ready for that yet, I need to know that Lilith is happy and safe."
                         j "And for a brief moment I thought you wanted the same thing [persistent.name] but if that was truly the case, then why did you retry even after getting an ending where she was happy and alive?"
                         $ persistent_jamestalk_justgame_knowledge = True
                         jump jamesChat_whyDidYouReturn


label jamesChat_whyDidYouReturn:
     menu:
          "I wanted to find an ending where we could be together and where she would be alive.":
               if justgame == True:
                    j "..."
                    j "That doesn't really surprise me."
                    j "You just take whatever you want to mold it into whichever way you please."
                    j "Don't you think you are being unfair to Lilith? Don't you think she has the right to die only once?"
                    j "I also don't like to see her die but you are just making things worse."
                    j "Can't you just break the cycle? Can't you just stop playing this game?"
                    j "You won't find what you are looking for in here."
                    j "Every time you retry you get transported to a parallel instance of this world with the new knowledge you gained."
                    j "You can however only do so much in those parallel versions of the world as they are copies, they don't tend to vary much."
                    j "To get more variation, limitless and controlable variation even, you would need to not be bound to <u>them</u>.anymore."
                    jump jamesChat_whyDidYouReturn_toBeTogether_choices
 
               elif loveher == True:
                    j "..."
                    j "Oh [persistent.name], love is not about always being together. Sometimes it is about doing the best thing for the person you love, even if it's hard."
                    #TODO: (use flags to detect endings where she lived, the ones below this are endings where she lived that should only be mentioned if you saw them.)
                    j "When Lilith met Ron and they were happy together, even had some kids."
                    j "Or when Abby got her to safely stay at her home."
                    j "When this entire ordeal finally settled down..."
                    j "You didn't have to retry."
                    j "You didn't have to cause her to go through the bad things once again after you were even told that she was safe and secure."
                    j "You see, you do not undo your actions each time you retry, each time you save Lilith once more or don't."
                    j "If only it was that simple, then she would have only died just now in that crash."
                    j "Every time you retry you get transported to a parallel instance of this world with the new knowledge you gained."
                    j "You can however only do so much in those parallel versions of the world as they are copies, they don't tend to vary much."
                    j "To get more variation, limitless and controlable variation even, you would need to not be bound to <u>them</u> anymore."
                    jump jamesChat_whyDidYouReturn_toBeTogether_choices
   
               elif likeher == True:
                    j "I see..."
                    j "And for who did you want to reach such an ending?"
                    #TODO: Continue the stuff below this, if you say for yourself show the justgame text, if you say for her then show the loveher text. Add some different text for the both of us.
                    menu:
                         "For the both of us of course.":
                              if persistent.kokiri_reachEndingForUs == True:
                                   j "It seems you're telling the truth, I remember you telling Lilith the same thing."
                                   if persistent.kokiri_reachEndingForMe == False:
                                        j "There's always the possibility that you're lying to us both but she can uses all the comfort she can get. So I'll believe you, for her sake."
                              "Filler"
                         "For myself.":
                              "Filler"
                         "For her.":
                              "Filler"
   
          "I wanted to see what other endings there are.":
               #TODO: Fill in based on the quest version.
               j "I see..." #TODO: (Add different reactions based on the three flags you had.)
               j "I will spare your time then, there are no endings here."
               j "In all this time I've spent here I've never seen one."
               menu:
                    "I do not trust you.":
                         if justgame == True:
                              j "I see, you think I'm defending Lilith by lying about it?"
                              j "Well, maybe I am or maybe I am not."
                              j "In the first case I am so desperate to not let you destroy her once again that I am lying to your face and in the other case there is truly no other ending here."
                              j "In both options it would be wise to reconsider before you move further towards a path you wouldn't like, right?"
                              j "You might not have had much consequences for your actions yet, but let me assure you."
                              j "There is no such thing as no consequences..."
                              if (persistent.major_love_offence_counter + persistent.minor_love_offence_counter) > (5 + persistent.major_love_comfort_counter + persistent.minor_love_comfort_counter):    
                                   j "And if you keep treating Lilly badly I might need to help teach you that lesson."
                                   n "James gives you a bonechilling look that makes you think you would not like being educated by him. At all."
                              else:
                                   j "Let's hope for the both of us that you act wisely so you have to experience as few of them as possible."
                                   j "After all, ignorance is bliss isn't it [persistent.name]?"
                              #TODO: Continue writing this text.
    
                         else:
                              j "Oh [persistent.name], why don't you trust me? We both care for Lilith right? So you can rest assured that I only want the best for her."
                              #TODO: Continue writing this text, maybe add some slight variations if the player treated Lilith badly.
     
    
                    "Thanks for telling me. I just had to be sure, this seems like a place where the developper would be able to hide some stuff.":
                         "Filler"
                         #TODO: Fill this in, there is no quest precedent.
    
          "You can't just bombard me with so much info and then just move on like I should understand, can you please atleast explain something clearly?":
               j "I see..."
               j "I guess that indeed was a bit too much info for you to handle."
               j "I will let you ask me one question about what I just said, then you have to answer my previous question."
               menu:
                    "Filler":
                         "Filler"
                         #TODO: Fill the menu in with some questions they can ask.
                         #After it has been answered let James reask the question.

label jamesChat_whyDidYouReturn_toBeTogether_choices:
     menu:
          "Who are they?":
               j "The first one you probably haven't met, not for long anyway. He is the one that created this world, gave you acces to it and made the second one.
               The second one you might know actually, the jester that controls the flow and direction of our story. He even controls the deaths Lilith suffered and yet you rely on him to fight him, that might be his biggest joke yet."
               menu:
                    "Alright mister purple prose. So the \"they\" you were talking about are the game developper and the narrator?":
                         j "Purple prose? I'll try to keep it a bit more straight-forward."
                         j "Yes, they are them."
                         j "They made you search for an ending that doesn't exist."
                         j "If you want to find it within yourself you'll need to become your own creator, become your own narrator."
                         j "The only way to win an unwinnable game is by becoming the game."
                         menu:
                              "... what?":
                                   j "It's no use..."
                                   j "If those words come from me they won't impact you that much."
                                   j "Why don't you ask Lillith to explain them where three become one?"
                                   $ persistent.jamesconversation_becomethegame_knowledge = True 
                                   #TODO: This path is not finished in the quest version, continue working on it.








label jamesConversationMenu:
     #A way to more easily loredump and talk about aspects that Lilith can't remember/ alternate realities. Add some more loredumps and in character questions.
     menu:
          "What is this place?":
               "Filler (It's a sort of place where souls that can't move on stay and are slowly morphed into haunting creatures, the part with the polaroids is James' place.)"
          "What are those bubbles?":
               "Filler (they are part of the alternate worlds, versions of the potential things you can do, past, present and future that never happened, already happened or will happen)"
          "No matter what I try Lilith keeps dying when I go on a date with her.":
               "Filler, the two of you talk about wheter or not it's a good idea to continue then."
          "Have you ever tried to make contact with your family again?":
               "Filler."













return
