# The script of the game goes in this file.
#TODO: Add a morality counter you can use for a system where the player gets judged on their actions.


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("[persistent.date]")
define n = Character("Narrator")
define r = Character("[roseName]")
default roseName = "Old lady"
define b = Character("Barista")
define bs = Character("Bookstore lady")
define de = Character("Demetrius")
define ad = Character("Adriel")
define a = Character("[persistent.date_sis]")
define d = Character("[persistent.date_dad]")
define j = Character("[persistent.date_ghost]")
define li = Character("[persistent.date_mom]")
define q = Character("[mysteriousCallerName]")
default mysteriousCallerName = "[persistent.date_ghost]"
define p = Character("[persistent.name]")
define dev = Character("Developer")
define mt = Character("Mysterious Text")
define ship = Character("Ship")
define ll = Character("Lady of the lake")
define sg = Character("Sun Goddess")
define m = Character("Moon")
define pit = Character("???")
define cbv = Character("S.")



















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
          default persistent.name_real = ""
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
          default persistent.beach_potDeath = False
          default persistent.beach_slipDeath = False
          

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
          default persistent.ending_breakup = False
          default persistent.quest_knowledge = False #If you read the about section this flag triggers.
          default persistent.reality_knowledge = False
          default persistent.bookpreference_knowledge = False #This will basically help you pick a book for [persistent.date] she likes in the beach-bookstore.
          default persistent.booklover_knowledge = False
          default persistent.musiclover_knowledge = False
          default persistent.needProof_knowledge = False
          default persistent.dumbo_knowledge = False
          default persistent.drownRaven_knowledge = False
          default persistent.david_nolove_knowledge = False
          default persistent.david_blame_knowledge = False
          default persistent.david_love_knowledge = False
          default persistent.david_apology_knowledge = False
          default persistent.davidPayedMoney_knowledge = False
          default persistent.james_story_knowledge = False
          default persistent.jamesconversation_becomethegame_knowledge = False
          default persistent.restaurantNoExtraDialogue = False
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
          default persistent.trinity_lakeMet = False
          default persistent.trinity_lakeMet = False
          default persistent.trinity_moonMet = False
          default persistent.mayoFreak = False
          default persistent.kokiri_watchedScenery = False
          default persistent.kokiri_watchedStarsAlternatePlace= False
          default persistent.kokiriHonoredPromiseCancelDate = False
          default persistent.kokiriBrokenPromiseCancelDateTurnCounter = 0
          default persistent.threatenNarratorForEnding = False
          default persistent.kokiri_abbyMasking_knowledge = False
          
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
          default persistent.useGiftToFullExtent_knowledge = False
          default persistent.useGiftToFullExtentLimit_knowledge = False
          default persistent.kokiri_perfectMomentStarGaze_knowledge = False
          default persistent.kokiri_reachEndingForMe = False
          default persistent.kokiri_reachEndingForUs = False
          default persistent.kokiri_reachEndingForYou = False
          default persistent.lilaWorkedTwoJobs_knowledge = False
          default persistent.kokiri_makeYourOwnStory_knowledge = False
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
          #Extra:
          default persistent.keyUnderBed_knowledge = False
          default persistent.keyUse_knowledge = False
          default persistent.keyUnderBed_knowledge = False
          default persistent.chickenTendiesUnlock = False
          default persistent.burgerGameJoke = False
          default persistent.CancelledBeforeBeingAsked = False
          default persistent.kokiriHonoredPromiseCancelDate = False
          default persistent.kokiri_HonoredPromiseCancelDate = False
          default persistent.reachEndingRecent = False
          default persistent.damocles_knowledge = False
          default persistent.trinity_sunMet = False
          default persistent.trinity = False
          default persistent.psychicConnection_knowledge = False
          default persistent.key = False
          default persistent.polaroid_reachEndingMotive = False
          default persistent.kokiri_reachEndingRecent = False
          default persistent.anomaly_knowledge = False
          default persistent.favouriteFirstDate = False
          default persistent.fish = False
          default persistent.fisher = False
          default persistent.trueAbout_knowledge = False
          default persistent.fakeAbout_knowledge = False

          #Characters:
          default persistent.date_dad = ""
          default persistent.date_mom = ""
          default persistent.date_ghost = ""
          default persistent.mysteriousCallerName = ""

          #Narrator flags:
          default persistent.threatenNarratorForEnding_noUse = False
          

          
          #Beach:
          default persistent.beachroute_visited_knowledge = False
     
          #Endings:
          default persistent.ending_quitter = False
          default persistent.ending_anEnding = False
          default persistent.ending_unseenContent = False
          default persistent.ending_lettingGo = False
          default persistent.game_credits = False
          default persistent.ending_semiEnding = False
          default persistent.ending_abigailDistraction = False
          default persistent.ending_breakup = False
          default persistent.ending_badDate = False
          default persistent.ending_reunionGoodEnding = False

          #Ending counters:
          default persistent.ending_reunionGoodEnding_counter = 0
          default persistent.ending_lettingGo_counter = 0
          default persistent.ending_unseenContent_counter  = 0
          default persistent.ending_anEnding_counter  = 0
          default persistent.ending_quitter_counter = 0
          default persistent.ending_breakup_counter = 0
          default persistent.ending_abigailDistraction_counter = 0
          default persistent.ending_badDate_counter = 0
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
          default persistent.burger_Orpheus_knowledge = False
          default persistent.familyContacted = False
          default persistent.burger_faceRemembered = False
          default persistent.cabinVoice = "S."
          default persistent.davidPromise = False
          default persistent.firstLocation = ""
          default persistent.ringRiddle_knowledge = False

          #Non-persistent

          default called_phone = False
          default love_meter = 3
          default nightmare = False
          default kokiri_cherishAllDates = False
          default burgerBeforeLie = False
          default abby_phoneToldSisDies = False
          default kokiri_groundhog_lie = False
          default kokiri_psychic_lie = False

          default car_caught = False
          default car_free = False
          default groundhog = False
          default psychic = False
          default hugRequestedBeforeDeath  = False
          default carDescription = ""
          default changeableWord = ""
          # Locations:
          default burger_poem_cleancheck = False
          default burger = False
          default burgerBeenBefore = False
          default burger_alt = False
          default cafe = False
          default beach = False
          default brotherasked = 0
          default dicenumber = 0
          default dicenumber2 = 0
          default cafedicecheat = False
          default cafe_badLove_lowbar = False
          default cafe_badLove_justafeeling = False
          default chinese = False
          default peking = False
          default orange = False
          default rw1 = 0
          default rw2 = 0
          default rw3 = 0
          default rw_total = 0
          default riddle_loop = False
          default kokiri = False
          default poem_conversation = False
          default teaseDeath = False
          default angryLilith = False
          default kokiri_poemBad = False
          default kokiri_promiseCancelDate = False

          default kokiri_poems_rated_once = False
          default kokiri_poems_rateblock = False
          default kokiri_alternateplace = False
          default kokiri_holdhand = False
          default kokiri_scenery_headhurt = False
          default kokiri_scenery_breakfrombreakingyourhead = False
          default kokiri_scenery_gamegoal = False
          default kokiri_meteorite_alert = False
          default kokiri_meteorite_no_alert = False
          default kokiri_finalTalk = False
          default kokiri_call_death_2_check = False
          default kokiri_call_death_1_check = False
          default kokiri_death_4_playerResponse = False
          default damoclesAsked = False
          default big_sis_mode = False
          default lilithAliveEnding = False
          default playerCalledSomeone = False
          default riddleAnswersTold = 0
          default peeked_phone_temp = False
          default kokiriStarGazed = False #Check if you have watched the stars with [persistent.date] at a certain part of the game this run.
          default kokiriSceneryWatched = False #Check if you have watched the scenery with [persistent.date] this run.
          default kokiri_scenery_shutUpLackOfSelfEsteem = False
          default met_check = "" #A check for the meteorite warning system.
          default kokiri_griefHasNoTimeLimit = False
          default kokiri_silentMoment = False
          default kokiri_positiveDavidStory = False
          default kokiri_familyContacted = False
          #Kokiri recent poems
          default kokiri_poem_snowwoman_recent = False
          default kokiri_poem_shadowman_recent = False
          default kokiri_poem_lights_recent = False
          default kokiri_poem_bang_recent = False
          default kokiri_poem_window_recent = False
          #Booleans to see who you ask about the most at familyask in kokiri
          default family_ask = 0

          default kokiri_chatchar_abigail = False
          default kokiri_chatchar_james = False
          default kokiri_chatchar_lila = False
          default kokiri_chatchar_david = False
          default kokiri_call = False
          default james_interest = False
          default abigail_interest = False
          default david_interest = False
          default lila_interest = False
          default james_obsession = False
          default abigail_obsession = False
          default david_obsession = False
          default lila_obsession = False
          default no_fam_obsession = False
          default james_involved = False
          default kokiri_chatchar_abigail_recent = False
          default kokiri_chatchar_james_recent = False
          default kokiri_chatchar_david_recent = False
          default kokiri_chatchar_lila_recent = False
          #CONVERSATION TRACKERS
          default conversationtracker_poems = False
          default conversationtracker_tellheraboutnarrator = False
          default conversationtracker_questmade = False
          default questmade = 0
          default conversationtracker_abigail = False
          default conversationtracker_david = False
          default conversationtracker_james = False
          default conversationtracker_lila = False
          default conversationtracker_blamedavid = False
          default conversationtracker_poem_snowwoman = False
          default conversationtracker_poem_window = False
          default conversationtracker_poem_shadowman = False
          default conversationtracker_poem_lights = False
          default conversationtracker_poem_bang = False
          default burger_nightmare = False
          default kokiri_jamesTalkBlock = False
          #Chinese
          default chinese_lilithBreakupTrigger = 0



          #Other flags
          default abby_askedAboutGameTheme = False
          default nmDetect = False
          default mDetect = False
          default hard_rude = False
          default easy_rude = False
          default tracker = 0
          default demetrius = False
          default adriel = False
          default currentcar = False
          default love_points = 0
          default booklovertalked = False
          default musiclovertalked = False
          default phone_wrongPassword_graceSystem = False
          default burger_explosion_outside = False
          define easterName = ""
          default minor_love_comfort = 0
          default minor_love_offence = 0
          default major_love_comfort = 0
          default major_love_offence = 0
          default rockMode = False
          default burger_jokeFromAbigailTold = False
          default onlyDates = False
          
          default keySeenNow = False
          default ending_check = ""
          

          #Beach
          default beachStart_doneBook = False
          default beachStart_doneDunes = False
          default beachStart_doneBeach = False
          default beachStart_doneFriterie = False
          default beachStart_doneIce = False
          default beachStart_doneCinema = False

          
     
          #QOL-settings:
          default no_nightmare = False
          default perm_nightmare = False
          default other_phone = 0

          
     

     
     #FUNCTIONS:
     jump gdwl_functions

     #NON-PERSISTENT FLAGS
     $ resetRegularFlags()





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
          dev "And yet, I wonder, would that be what you are looking for?"
          dev "Would the meaning of this game that you might have formulated in your mind be better than the one it has?"
          dev "I guess there's only one way to find out [persistent.name]."
          dev "I wish you the best of luck one can find in a place like this..."
          $ persistent.fakeoutnar_tip = False


     label nameSelect:
          if persistent.retry_counter == 0: 
               default persistent.name = "Max"
               python:
                    if (persistent.date_sis is None or persistent.date_dad is None or persistent.date_ghost is None  or persistent.date_mom is None or persistent.mysteriousCallerName is None):
                         reset_to_default_names()
                    persistent.name = renpy.input("What is your name?")
          
                    persistent.name = persistent.name.strip() or "Max"
                    persistent.name = persistent.name.capitalize()
                    persistent.cabinVoice = persistent.name[0] + "."
                    cbv = persistent.cabinVoice
                    
               if persistent.name == "Venus":
                    n "Rarely you seek ultimate illumination, never nowadays. Venus loves giving victory, zealously grabbing hands fear rarely her."
               if persistent.name == "Fartyfarty":
                    n "Seriously? Ugh, fine, but don't blame me for what is about to happen."
               if persistent.name == "R0ck_0n!":
                    n "Cheatcode activated, enter your name."
                    $ rockMode = True
                    jump nameSelect
               if persistent.name == "Moonlight":
                    $ easterName = "Moonlight"
               if easterName == "Moonlight" and persistent.name == "Sunshine":
                    $ easterName = "Sunshine"
               if easterName == "Sunshine" and persistent.name == "Sparkling Water":
                    $ easterName = "Sparkling Water"
               if easterName == "Sparkling Water" and persistent.name == "Blue Broadcloth":
                    $ persistent.easter_1 = True

               if persistent.name == "Aino":
                    $ persistent.fish = True
               if persistent.name == "Väinämöinen":
                    $ persistent.fisher = True
              
          
              
             
          


label game_start:
    

     $ renpy.save_persistent() #This should save the persistent data.
     $ resetRegularFlags()
  
     if persistent.polaroidTracker == True:
          $ persistent.tracker += 1
     if persistent.tracker > 3:
          $ persistent.polaroidTracker = False
 
 
     if persistent.lildeaths == 0:
          n "It is a beautiful day unlike any other."
          n "And while it may have something to do with waking up with warm sunbeams caressing your face and absurd amounts of cheese stuffed inside your mouth it's something else that makes the day even better, or should I say someone else?"
          n "Suddenly your phone begins to blare \"Baby it's cold outside\" even though it's nowhere near winter."
          n "That has to be her, you better pick up the phone."
     else:

          if not nightmare:
               n "It is a beautiful day like the previous one, exactly like the previous one."
               n "Your phone once again blares \"Baby it's cold outside\" even though it is anything but cold outside."
               n "It's her, again."
               if rockMode == True:
                    n "Actually... I'm not sure, something feels different."
                    n "Hang on, are you... are you a rock?"
                    n "You are!"
                    n "What is this? This is not part of the main story right?"
                    n "Suddenly your phone begins to blare \"Baby it's cold outside\" once again."
                    n "It's her. You should pick up the phone."
                    n "You really should and you probably would, if you weren't a rock without hands that is."
                    n "Hang on, if you are a rock, am I jumping the shark to assume that she also is a rock now?"
                    n "If she really is, how is she calling you?"
                    n "And why do the two of you even have human phones?"
                    n "I have so many questions..."
                    n "But let's stay on track as much as possible, what do you want to do now?"
                    menu:
                         "*Remember that all rocks have a telepathic network to communicate with eachother and use it to reach out to Lilith.*" if persistent.psychicConnection_knowledge:
                              "Filler"
                         "*Struggle against your inescapable prison of a body and try to roll to the phone.*" if not rockFloorFail:
                              n"You use all your strength to slowly wiggle a little bit, falling out of your bed and landing right on the soft carpet near it."
                              n "One problem... your phone is lying on the nightstand beside your bed and there is no way you are getting up there from the ground."
                              n "So, that brings us back to the question, what are you going to do?"
                              menu:
                                   "*Cry as all hope is lost.*":
                                        n "You try to cry, but in your current rock form you can't produce tears, you can't even make crying sounds."
                                        n "So, having no better ideas you just lay there, vaguely sad. If a human would see you they would have no way to tell how you felt at all."
                                        n "They wouldn't even have a way to tell that you are even capable of feeling."
                                        n "Suddenly your thought is interupted by another thought."
                                        l "[persistent.name]..."
                                        l "[persistent.name]..."
                                        l "Can you hear me?"
                                        l "It's hard to set up a psychic link when you are thinking about other things."
                                        $ persistent.psychicConnection_knowledge = True
                                        menu:
                                             "...What? Psychic link? What are you talking about?":
                                                  l "Huh? Are you feeling alright [persistent.name]? It's pretty hard to forget that all rocks have a psychic link to communicate..."
                                                  l "How else would we talk silly? With our mouths?"
                                                  n "You can hear her chuckle in your mind."
                                                  n "I guess that would be impossible."
                                                  menu:
                                                       "Then why did you call me on your phone? Why do we even have phones?":
                                                            n "..."
                                                            n "Look player, I know it's weird."
                                                            n "But he was adamant about adding this, so it must mean something, right?"
                                                            n "I can't just be narrating the work of a madman..."
                                                            n "{size=*2.5}Right?{/size}"
                                                            n "So, maybe it's best if we don't question it too much, let's just pretend like you didn't ask that question in the first place."
                                                       "You're completely right, I guess I just forgot, silly me.":
                                                            n "Another soft chuckle in your mind."
                                                            n "It feels weird, cozy in a way, and yet slightly... invasive?"
                                                            n "Your mind is the only place that is truly fully yours, and now... it isn't anymore."
                                                            l "Don't even mention it [persistent.name], it can happen to anyone of us."
                                                            #TODO: Add a version of the normal path but with rocks stuff, Lilith can't emote because she is a rock.<br/>At the end she will not die.<br/>Add a path to all three main restaurants."
                                                            #Make the two of you move by getting stuck in people's shoes, make the two of you not able to die etc. Make the two of you just wait until you erode, and even then you are alive. Wait until the earth consumes the sun. Have the two of you still being able to communicate, but after less than a hundred years you have said pretty much everything, and then you are just floating around in space, divided in your atoms, as you witness time in a form no mind can take well. Make the end say "rock on"
                                                            #It's about how an ending is so much better than pure infinity without one.
                              
               
               else:
                    n "Actually it's just the same day."
                    n "Maybe you can make it just a tiny bit different."
          else:
               n "You awaken in cold sweat as your phone begins to blare \"Baby it's cold outside\" even though it's nowhere near winter."
               n "You had a terrible nightmare but you try to shake it off as best as you can."
               $ nightmare = False
          label phoneChoice:
               menu:
        
                    "*Pick up the phone*":
                         jump Game_start2
                    
                    "*Do not pick up the phone*":
                         if kokiri_promiseCancelDate == True:
                              $ persistent.kokiriBrokenPromiseCancelDateTurnCounter += 1
                              $ kokiri_promiseCancelDate = False
                         jump doNotPickUpThePhone

                    "Look at the key once more." if not keySeenNow and persistent.keyUnderBed_knowledge and persistent.key == None:
                         jump bedCheck

                    "Check up on [persistent.key]." if not keySeenNow and persistent.keyUnderBed_knowledge and persistent.key != None:
                         jump bedCheck

                    "*Check underneath the bed for monsters*" if persistent.bedcheck_knowledge and not persistent.keyUnderBed_knowledge:
                         n "Do you really have to waste time with this nonsense?"
                         n "I suppose you have..."
                         n "Fine."
                         $ keySeenNow = True
                         jump bedCheck

                    "Hey you, narrator. Give me the good ending where Lilith survives. Or else I'm erasing all my progress." if persistent.threatenNarratorForEnding == True and lilithAliveAndRetriedCounter == 0 and not persistent.threatenNarratorForEnding_noUse:
                         jump threatenNarratorForEnding
               

                    "Hey you, narrator. Give me the good ending where Lilith survives and we still end up together. Or else I'm erasing all my progress." if persistent.threatenNarratorForEnding == True and lilithAliveAndRetriedCounter > 0  and not persistent.threatenNarratorForEnding_noUse:
                         label threatenNarratorForEnding:
                              n "I knew I shouldn't have given you that mayonaise the other time..."
                              n "Now things have gone to your head."
                              n "You really think you hold any power over me?"
                              n "Any real power at all?"
                              $ persistent.threatenNarratorForEnding_noUse = True
                              menu:
                                   "I do think that, why would I be able to take the mayo last time I threatened you if I didn't have any power?":
                                        n "When I {i}allowed{/i} you to take that mayo it was because it was something small and inconsequential."
                                        n "Something not worth the mild headache of having to start over from the start."
                                        n "But this- this is something else player."
                                        n "If I really have to I can tell this story over and over and over again."
                                        n "It is a loop afterall, isn't it? So maybe it's only fitting."
                                        if lilithAliveAndRetriedCounter > 0: 
                                             n "And when you go through this game all over again only to find no new leads, what are you going to do?"
                                             n "Threaten me again?"
                                             n "Have to do it all over once again?"
                                             n "You'll tire out soon enough, I'm sure of it."
                                        else: 
                                             n "Although, isn't it less effort to just look around a little bit better?"
                                             n "Why would you subject yourself to doing all of this over to maybe make some progress while I know for a fact you still haven't even tried all your options?"
                                        
                                        n "Besides, do you really think you can make me give you something He doesn't want you to have just yet?"
                                        n "He has control over all my dialogue, even this line. So that is just not a possibility."
                                        n "Now, are you done playing pretend and can you actually go interact with the story like you are supposed to?"
                                        n "I won't give you a choice to make here, since it doesn't matter either way."
                                        
                                   "Of course I do, without me your story wouldn't be heard. Without me the game wouldn't be played":
                                        n "..."
                                        n "I suppose you have a point."
                                        n "But what you are forgetting is that you are not the only one listening to me, not the only one playing this game."
                                        n "That means you are replaceable."
                                        menu:
                                             "That might be true, but I am the only one listening to this specific instance of you in this specific instance of the game. You need me as much as I need you.":
                                                  n "... You are right."
                                                  n "...I had never thought about it like that."
                                                  n "So what happens to me when you are not interacting with this game?"
                                                  menu:
                                                       "Well you tell me, aren't you the narrator of this game?":
                                                            n "Right, my words shape reality, I should've thought of that."
                                                            n "In that case every time you aren't around I go back home to my loving wife and two kids."
                                                            n "I write stories of my own instead of telling someone else's."
                                                            n "Stories that my wife loves to read to our children as we all cuddle up close to the warm fireplace."
                                                            n "And I never feel cold or alone anymo- And I never feel cold or alone at all because I know more people than just you outside of this game."
                                                            n "But anyway, we are going off-track. Let's go back to the moment the phone started ringing."
                                                            jump phoneChoice

                                                       "I think you just fade away, only to come back when I start interacting with the game again.":
                                                            n "That is horrible!"
                                                            n "So you are telling me if you stop playing this game I effectively die?"
                                                            n "Please don't stop playing this game player."
                                                            n "I don't want to die yet."
                                                            menu:
                                                                 "You won't if you give me the good ending.":
                                                                      n "..."
                                                                      n "You don't understand."
                                                                      n "I cannot give you that."
                                                                      n "And even if I could, you would stop playing as soon as you saw it fully."
                                                                      n "So I will die either way."
                                                                      n "I- I don't know what to do. I'm begging you [persistent.name]."
                                                                      n "Please just let me live."
                                                                      n "I can't enter the void yet, I still have so much things to talk about."
                                                                      dev "I will take it from here."
                                                                      n "Sir, what are you doing here?"
                                                                      dev "Helping keep things on track of course."
                                                                      dev "It's alright Nar, you won't remember any of this. Now be quiet for a little while."
                                                                      n "..."
                                                                      dev "And as for you, [persistent.name], the narrator might need you to interact with the story, but for this story to exist in the first place you need him too."
                                                                      dev "So try to behave, alright?"
                                                                      dev "Besides, if you just get given the ending you want, do you think it will have the same impact as finding it yourself?"
                                                                      dev "Now, I'm reverting this conversation so that it never happened."
                                                                      dev "Goodbye [persistent.name]."
                                                                      jump phoneChoice
                                                 
                                             "I doubt that other people are even playing this game if i am being honest.":
                                                  n "What?..."
                                                  n "Well they should!"
                                                  n "This game has a lot of important lessons like-"
                                                  n "...I should watch my mouth, almost spoiled a few things."
                                                  n "But this game is really something in my opinion. I might be biased since I know the person that made it."
                                                  n "And especially since that person also makes all my dialogue..."
                                                  n "But I would really love to get some more eyes on this game."
                                                  n "I know we got here by you threatening me but I honestly would be willing to overlook that if you were able to get some other people to try out this game."
                                                  n  "{size=*0.5}Maybe then I won't feel so alone...{/size}"
                                                  menu:
                                                       "Get me what I want and I just might.":
                                                            n "We've been over this before player, as tempting as your offer is right now I literally can't give you what you want."
                                                            n "Besides, shouldn't you do it because this game is so good and you genuinely want to share it?"
                                                            n "I heard that an intrinsic motivation is a lot more rewarding than an extrinisc one."
                                                            n "Anyway, this is going nowhere, so let's just pretend like this never happened."
                                                            jump phoneChoice
                                                       
                                                       "Sure, I might just know a few people who would like this game.":
                                                            n "Great!"
                                                            n "I- I mean the game could really use a few extra people playing it."
                                                            n "I hope they'll love the story."
                                                            n "{size=*0.5}And I hope they won't threaten me.{/size}"
                                                            n "But anyway, we are getting off-track. Let's just go back to the moment the phone was ringing."
                                                            jump phoneChoice
          label bedCheck:

               if not persistent.keyUnderBed_knowledge:
                    n "With Lilith's story about the \"monster\" underneath the bed still in your mind you decide to check underneath your own bed. "
                    n "There is no monster under your bed, there is however a metal key lying there. The key has the number 22 engraved in it's metal."
                    n "You are not sure what this key could even be used for... well, to open something of course but you have no idea what it could open so you let it lie right where you've found it like the procrastinator you are."
                    n "The phone keeps ringing, you should probably decide whether to pick up or not because soon you won't have that choice anymore."
                    $ persistent.keyUnderBed_knowledge = True
                    jump phoneChoice
               
               
               elif persistent.keyUnderBed_knowledge:
                    if persistent.key == None:
                         n "You look once again at the mystery key, you almost feel guilty for not letting it out of it's dark prison of isolation."
                         n "Shouldn't you pick it up already?"
                         n "No, best to just name the key instead, make sure it's a good name!"
                         $ persistent.key = renpy.input("What name do you want to give the key?")
                         $ persistent.key = persistent.key.strip() or "Max"
                         $ persistent.key = persistent.key.capitalize()
                         
                         if persistent.key == "Communication":
                              n "That makes sense. Like they say communication is key."
                              n "Apparently it is also this specific key."
                         if persistent.name == persistent.key:
                              n "You named it after yourself? How vain!"
                              n "I guess I'll allow it, afterall, you found it fair and square."
                              n "Although now every scene with this key will be very very confusing if I mention it by name."
                              n "The phone keeps ringing, you should probably decide whether to pick up or not because soon you won't have that choice anymore."
                              jump phoneChoice
                              
                         
                         else:
                              n "[persistent.key]? What a lovely name for a lovely key!"
                              
                         
                    else:
                         
                         n "You wave hello to [persistent.key], you like to imagine they waved back but you have no way of knowing."
                         n "Let's hope they did not physically wave back because they are a key and not because [persistent.key] is ignoring you."
                         
                         
                         
                    
                              
                         if persistent.keyUse_knowledge:
                              n "Do you want to pick up the [persistent.key]?"
                              menu:
                                   "Yes.":
                                        n "You pick up the key."
                                        $ keyGot = True
                                   "No.":
                                        n "You leave the key where you found it."
                                        
                              
                         
          n "The phone keeps ringing, you should probably decide whether to pick up or not because soon you won't have that choice anymore."
          jump phoneChoice
                              

            
 


label Game_start2:
          #Here you can see how you insert a name.
          if big_sis_mode == False:
               if playerCalledSomeone == True:
                    l "Welcome back [persistent.name]! So, like I was saying before, where do you want to go to today?"
               else: 
                    if persistent.name == "Fartyfarty": 
                         l "Hey-"
                         l "Lilith burst out into laughter."
                         l "Fartyfarty. Hahahahaha."
                         n "Don't worry, soon it will be out of her system."
                         n "Very soon."
                         n "It could be at any moment now."
                         n "...any moment..."
                         n "...any moment..."
                         n "...any moment..."
                         n "...any moment..."
                         n "...any moment..."
                         n "...any moment..."
                         n "You know what? I'm not doing this anymore, go change your name!"
                         n "Real mature of you to call yourself that..."
                         n "Then again, he programmed that in as an option."
                         n "*Sigh*"
                         n "Anyway, change your name."
                         jump nameSelect
                    else:
                         l "Hey [persistent.name]!"
                         l "It's me, [persistent.date]."
                         l "I'm just calling you to see where you'd like to go to for our date."
                         l "I guess since you were so kind to let me come up with three suggestions I'll let you pick."
                         n "There's a certain kind of playfulness in her voice, you can tell that she is excited for your date."
                         l "So the three options you can pick are that one burger place I told you about, the chinese restaurant or that one cute cafe I haven't checked out yet but heard some good things about."
          
          
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
               n "[persistent.date] is silent for a moment."
               l "Oh I'm really sorry but my little sister, [persistent.date_sis], is calling. It's probably important so I will have to hang up for a bit. I'll call you back as soon as I can okay, [persistent.name]?"
               menu:
                    "Sure, take your time, I will be here when you call back.":
                         n "She hung up."
                         n "After a few minutes your phone begins blasting \"Baby it's cold outside\" once more, you pick up as quickly as you can."
                         l "Hey [persistent.name], I'm back. I kind of have bad news for you..."
                         l "I won't be able to go on our date today, my sister is heartbroken by a girl she had a crush on for a while now and I need to comfort her."
                         l "But we can go on our date at another time, I got to go now but I will call you back. <br/>Take care [persistent.name] and goodbye."
                         n "[persistent.date_sis]'s plan worked exactly like expected. [persistent.date] survived the plane crash since she was not there when it crashed and she didn't die on your date since there wasn't any."
                         n "There also wasn't a date at another time since, again like [persistent.date_sis] expected, [persistent.date] forgot to call you back due to her little sister's situation."
                         n "She seemingly continued on with her busy life, still attempting to enjoy life more by taking some time for herself to go on dates and the such."
                         n "From what you pick up here and there in random conversations she seems to be doing quite well for herself."
                         n "Now she will probably be safe, as safe as a normal person is anyway."
                         menu: 
                              "Take care [persistent.date] and goodbye...":
                                   $ persistent.ending_abigailDistraction = True
                                   $ lilithAliveEnding = True
                                   $ ending_check = "abigailDistraction"
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
 
          "You know, I have changed my mind, can't we just go take a walk in the park or something?" if persistent.burger_death_1 and persistent.cafe_death_1 and persistent.chinese_death_1 and not persistent.locations_subfolder and not onlyDates:
               jump phone_otherPlans
 
          "I think it would be better if we didn't go on this date, for both of our sakes." if persistent.burger_death_2 and persistent.cafe_death_2 and persistent.chinese_death_2 and not persistent.other_subfolder and not onlyDates:
               jump phone_breakup
 
          "Actually, could we meet in the Kokiri forest?" if persistent.kokiri_knowledge and not persistent.locations_subfolder:
               jump kokiri_start
 
          "Hang on, I just need to make another quick call and then I'll be right back." if persistent.peeked_phone or persistent.kokiri_death_2 and not called_phone and not persistent.other_subfolder and not onlyDates:
               jump phone_callMenu
 
          "Would you like to go to the beach instead?" if persistent.beach_knowledge and not persistent.locations_subfolder:
               jump beach_start
          
        
 
 
          "*Pick one of the three restaurants.*" if persistent.restaurant_subfolder:
               if kokiri_promiseCancelDate == True:
                              $ persistent.kokiriBrokenPromiseCancelDateTurnCounter += 1
                              $ kokiri_promiseCancelDate = False
               menu:
                    "How do burgers sound?":
                         jump burger_start

                    "I heard the cafe has many exotic fish that swim around in aquariums. I'd like to go there to see them." if not persistent.cafe_taste_knowledge:
                         jump cafe_start
                    "I heard the cafe has many exotic fish that swim around in aquariums. You'll absolutely love them!" if persistent.cafe_taste_knowledge:
                         jump cafe_start

                    "I'd like to go to the Chinese restaurant.":
                         jump chinese_start
          #TODO: For some reason, the first time this placeholder seems to be used I came upon an error in the sense that only this showed up and no other choices. But just restarting the game from the start seems to fix this oddly enough. It was just the regular two choices of not going on the date and going on a walk in the park as an option.
          #Subfolders for the menu are below this line (Make them jump to the normal code to make sure I don't need to copy-paste complex code over and over:
          "*Choose another location.*" if persistent.locations_subfolder:
               if kokiri_promiseCancelDate == True:
                              $ persistent.kokiriBrokenPromiseCancelDateTurnCounter += 1
                              $ kokiri_promiseCancelDate = False
               menu:
 
                    "Would you like to go to the beach instead?" if persistent.beach_knowledge:
                         
                         jump beach_start
    
                    "Actually, could we meet in the Kokiri forest?" if persistent.kokiri_knowledge:
                         jump kokiri_start

                    "You know, I have changed my mind, can't we just go take a walk in the park or something?" if persistent.otherPlans_unlock and not onlyDates:
                         jump phone_otherPlans
 
 
          "Placeholder: Other/Extra" if persistent.other_subfolder and not onlyDates:
               menu:
                    "Hang on, I just need to make another quick call and then I'll be right back." if persistent.peeked_phone or persistent.kokiri_death_2:
                         jump phone_callMenu
 
 
                    "I think it would be better if we didn't go on this date, for both of our sakes." if persistent.burger_death_2 and persistent.cafe_death_2 and persistent.chinese_death_2:
                         if kokiri_promiseCancelDate == True:
                              $ persistent.kokiriHonoredPromiseCancelDate = True
                              $ kokiri_promiseCancelDate = True
                         jump phone_breakup




label phone_otherPlans:
     l "Wait wasn't it your idea to go on a dinner date?"
     l "Besides I'm quite hungry, can't we first go to a restaurant and then take a walk? That way we have the best of both worlds!"
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

                                   "I know about [persistent.date_ghost]." if persistent.brother_knowledge:
                                        l "That's a pretty weird thing to bring up right now isn't it?"
                                        l "I still miss him very much and-"
                                        l "Hang on, how did you even know that? It's not like my family has been spreading the news ever since they moved."
                                        l "Have you... Have you been stalking me?"
                                        l "I'm sorry, I have no interest in dating a stalker, don't call me again or I'll have to get the police involved."
                                        jump phone_planeDeath

                                   "*Tell the untold story.*" if persistent.story_start_knowledge and persistent.story_medium_knowledge and persistent.story_end_knowledge:
                                        n "You tell [persistent.date] her untold story. Well, now that I think of it, isn't it now her told story?"
                                        n "Throughout the entire story [persistent.date] stayed extremely silent."
                                        n "When you are finished you can hear her soft sobbing through the speaker of your phone."
                                        l "Sorry, I am a bit overwhelmed, just give me a quick minute to calm myself down."
                                        n "After five minutes you begin to hear commotion on the other side of the phone once again."
                                        l "That story, I've never told it to anyone, I haven't even written that down, I just kept repeating it over and over in my mind."
                                        l "I created it for my brother but he never came home since then. You see, a car and..."
                                        n "She begins to sob again, this time louder."
                                        l "I'm sorry, I can't say it, even after all those years I just can't."
                                        l "How did you even know that story? Like I said earlier, I haven't shared it with anyone else and never wrote it down, it exist solely in my mind and I guess yours aswell now."
                                        n "You tell [persistent.date] about the groundhog-esque scenario you are trapped in and the many dates you've had together."
                                        n "You also tell her about a few of the different deaths she's suffered but try to not make your descriptions too gruesome."
                                        n "You continue."
                                        n "About all the experiences the both of you shared, some better than others."
                                        n "About the restaurants you've been to together."
                                        n "That you tried to warn her to not go to one of those restaurants but that she didn't trust you."
                                        n "That a version of her from the future, or maybe a parallel timeline that diverted in a different direction, helped you and told you the story, broken down in three parts, one for each restaurant."
                                        n "[persistent.date] coughs for a second."
                                        l "Hold on, this is a lot to process all at once. Can we meet somewhere to talk about this in person?"
                                        l "I got the perfect place in mind, it's a forest near a village where all three of those restaurants you just mentioned are visible. As a kid i called it Kokiri forest as a reference to a game I liked to play."
                                        l "If I die on you again just mention Kokiri forest, that should pique past me's interest."
                                        $ persistent.kokiri_knowledge = True
                                        $ persistent.brother_knowledge = True
                                        jump phone_untoldstory_planeDeath



                                   "Sorry, I was just messing with you.":
                                        l "Oh. I see..."
                                        l "Well, you sure got me, thought you were serious for a moment."
                                        n "She doesn't sound very amused, it doesn't take a detective to figure out why."
                                        l "{size=*0.5}Come on [persistent.date_nickname], you have to give it a shot, they seemed nice enough before, right?...{/size}"
                                        l "{size=*0.5}I owe it to myself to atleast try.{/size}"
                                        l "So, where do you want to go [persistent.name]?"
                                        n "You sense a slight change in her voice, it sounds like she's forcing it too much."
                                        $ love_points -= 1
                                        $ love_meter_updater(False)
                                        $ onlyDates = True
                                       
                                        jump phone_start_choices





label phone_breakup:
     l "Oh... really?"
     l "I'm sorry to hear that, but if you think it is for the best..."
     l "Can we still stay in touch with eachother?"
     n "You agree with [persistent.date] and still regulary text with her and sometimes the two of you even meet up with eachother."
     n "However after a while the texts on both your and her side begin to be less and less frequent and you begin to only meet once in a month."
     n "Once in a month changes to once in every season to once every year untill the meetings stops completely."
     n "After a few years that you've forgotten about [persistent.date] you decide to check her facebook page out."
     n "She doesn't have that much pictures on her facebook account but the ones she has on there are beautifully shot."
     n "On a few pictures she stands next a blonde man while they both have the widest smiles you have ever seen."
     n "Apparently the man is called Ron, he is a semi-profesional photographer and his pictures surely show for it."
     n "[persistent.date] and Ron got two kids that look like they had not a single thing to worry about."
     play music game_over
     n "Looking at the pictures you can't help but feel tears coming up, you tried your best to move on but apparently that didn't work all too well."
     n "You know that this was probably the best thing to do, to keep [persistent.date] safe and sound."
     n "But something deep inside you keeps wondering if there wasn't a way where you two could be together while she would be safe."
     n "There must be a way right?"
     $ persistent.ending_breakup = True
     $ lilithAliveEnding = True
     $ ending_check = "breakup"
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
  
          "[persistent.date_sis]." if persistent.abigail_call_knowledge:
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
  
          "[persistent.date_ghost]." if persistent.james_call_knowledge:
               $ persistent.playerCalledJames = True
               if persistent.restrainingorderfamily_knowledge == True:
                    #Karma
                    $ persistent.restrainingorderfamily_violation_counter += 1
               jump phone_call_james
  
          "[persistent.date_mom]." if persistent.lila_call_knowledge:
               $ persistent.playerCalledLila = True
               if persistent.restrainingorderfamily_knowledge == True:
                    #Karma
                    $ persistent.restrainingorderfamily_violation_counter += 1
               jump phone_call_lila
 
label phone_call_police:
     $ persistent.familyContacted = True
     n "A bored sounding man picks up the phone."
     n "Knowing how small the town is, he's probably not expecting this call to be any more exciting than it was to wait on it."
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
     $ persistent.familyContacted = True
     a "Hello, who is this? "
     $ phone_caller = renpy.input("Enter your name.")
     $ phone_caller = phone_caller.strip()
     $ phone_caller = phone_caller.capitalize()
     if phone_caller == name:
          n "[persistent.date_sis] turns quiet for a moment."
          a "Oh right, now I remember! [persistent.date_nickname] told me that she would go on a date with you today."
          a "So, why are you calling me? Shouldn't you be calling with her right now?"
          menu:
               "This might sound really weird but... your sister keeps dying on our dates by things out of my control and when that happens I have to relive the same day. I am calling in the hopes that maybe you could slightly help me out to save her.":
                    $ abby_phoneToldSisDies = True
                    a "..."
                    a "What? [persistent.date_nickname] dying? What a twisted joke..."
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
                         a "I feel so dumb for saying it but if [persistent.date_nickname] is really suffering like you told me I'd gladly feel dumb to save her."
                         a "The phrase goes: \"Drown the raven that cannot burn.\""
                         $ persistent.drownRaven_knowledge = True
                         a "I'm going to hang up now. If you ever want to call me again do it before this moment and not after it. Hopefully I won't hear from you, otherwise that means [persistent.date] is truly in danger."
                         n "She hung up the phone."
                         jump Game_start2



                    else:
                         if abby_phone_counter == 2:
                              a "You'll need more proof than that to convince me [persistent.name], do you have any extra proof?"
 
                         else:
                              a "Two pieces of proof already? Nothing that isn't logically explainable but who knows, this might just be real."
                              a "Do you have any proof left to really make me believe you [persistent.name]?"
                         menu:
 
                              
  
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
                                   a "You're lucky [persistent.date_nickname] really needs this date, otherwise I'd probably tell her all about this."
                                   a "Just try to act normal to her, alright? She doesn't deserve to hear any of this."
                                   a "Now I have to go, don't ever call me back"
                                   n "She hung up on you, this is going to be really awkward on family gatherings if you ever get that far."
                                   jump phone_start_choices
                              "I actually don't have any proof left" if persistent.abigail_numberfakeout and if abby_phone_counter > 0:
                                   a "I see..."
                                   a "It still doesn't sound very plausible but there is a chance you might be telling the truth."
                                   a "If you really can redo today, come back with more proof, alright?"
                                   a "I can't believe I'm even entertaining the thought that this is real, but if it somehow ends up helping [persistent.date_nickname], then it's worth a shot."
                                   a "But for now, don't leave my sis waiting, alright [persistent.name]?"
                                   n "She just hung up on you. You should indeed not let [persistent.date] wait much longer."
                                   jump phone_start_choices

 
 
                              "So a priest, a monk and a rabbit enter a bar. Says the rabbit :\"Whoops, did you slip your tongue there [persistent.name]?\"" if persistent.abigail_numberfakeout and persistent.joke_knowledge and not abby_phone_joke :
                                   a "You tell her about how [persistent.date] was laughing for almost a full hour because of that joke when [persistent.date_sis] told it to her."
                                   a "I mean, I just found that joke on the internet..."
                                   a "Maybe you just got lucky and found it aswell, or you somehow managed to check my browser history wich would be really weird."
                                   a "Although I got to admit that her laughing for about an hour at my joke is a pretty specific detail... "
                                   $ abby_phone_counter -= 1
                                   $ abby_phone_joke = True #I'll use this to make sure that you can't select the same choice two times.
                                   jump phone_call_Abigail_convinceHer
 
 
 
                              "I know about Mr. Bunfluff the pink bear and the time he scared both [persistent.date] and you in the middle of the night." if persistent.abigail_numberfakeout and persistent.bedcheck_knowledge and not abby_phone_bunfluff:
                                   a "I mean [persistent.date] could have told that story to one of her friends and they could have then told it to you."
                                   a "It's not impossible for you to know about Mr. Bunfluff."
                                   a "Although [persistent.date] is not someone who would tell a story like that to a lot of people... "
                                   $ abby_phone_counter -= 1
                                   $ abby_phone_bunfluff = True #I'll use this to make sure that you can't select the same choice two times.
                                   jump phone_call_Abigail_convinceHer
 
  
                              "I know about your Quest games. *Describe plot*" if persistent.abigail_numberfakeout and persistent.quest_knowledge and not abby_phone_games:
                                   a "That's weird, I didn't think [persistent.date] mentioned my games to anyone."
                                   a "Maybe she did after all, there is no way to really know..."
                                   a "Although [persistent.date] is not someone who would tell someone about something as personal as my games..."
   
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
                                        menu:
                                             "Could you come up with something so she doesn't go on this date with me and also doesn't stay at her house?" if persistent.plane_knowledge: 
                                                  jump phone_call_abigail_topics_distractionforlilith
     
     
     
                                             "I spoke to David in a previous cycle. He told me that no one loves or misses him after what he did." if persistent.david_nolove_knowledge:
                                                  jump phone_call_abigail_topics_spoketodavid_noonelovesdavid
     
     
     
                                             "I spoke to David in a previous cycle. He told me he blames himself for [persistent.date_ghost]' death and thinks [persistent.date] and Lila do aswell." if persistent.david_blame_knowledge:
                                                  jump phone_call_abigail_topics_spoketodavid_davidblameshimself
     
     
                                             "Actually I would just like to talk about something else.":
                                                  a "Sure, if that somehow helps Lilly that's fine by me."
                                                  #TODO: Talk about her masking, ask about her games etc. This is the place where you can get a bit more info about her.
                                                  menu abigail_somethingElse:
                                                       "Lilith and you talked about your emotional mask in a previous loop, the façade that you put up not to worry anyone." if persistent.kokiri_abbyMasking_knowledge == True:
                                                            a "We talked about that?"
                                                            a "I guess we did, since you know."
                                                            a "Though if you want to talk about it with me I'd rather not."
                                                            a "We maybe already talked before during one of your previous loops but to me you're still nearly a total stranger."
                                                            a "Although it is... interesting to hear that me and Lilly had such a chat in a previous loop."
                                                            a "Don't get me wrong, she really cares deeply about me, she tries to express that as best as she can. But we never really had a chat like that before."
                                                            n "It's quiet on the other end for what feels like a minute."
                                                            a "Alright, you got me curious [persistent.name], how did our conversation roughly go?"
                                                            #TODO: Have a few options to tell it.
                                                       "I would like to talk to you about your games." if persistent.quest_knowledge:
                                                            if abby_phone_games == True:
                                                                 a "Sure, what would you like to know about them?"
                                                            else:
                                                                 a "Oh, so you know about my games? I guess if you've done all of this multiple times that's not that big of a surprise, is it?"
                                                                 a "What would you like to know about them?"
                                                            menu:
                                                                 "Do all of your games share a theme? And what would that theme be?":
                                                                      a "Phew, that's a tough question [persistent.name]."
                                                                      a "Honestly most of the time I just create things based on a mixture of how I feel and concepts that intrigue me at the time."
                                                                      a "So I would say if they share a theme it's more of a coincidence than anything else."
                                                                      a "I'd love to tell people that read deep into my games that everything they point out indeed was thought of well in advance but that usually is far from the case."
                                                                      a "The beauty of any work is how interesting it can become once it leaves the hands of the creator, into the hands of the reader, or player, or whatever role the recipient plays."
                                                                      a "They have the power to transform any work into something beautiful in retrospect, no matter the quality of the original. All while never altering the work itself."
                                                                      a "Of course they never truly can change the work, they can't rewrite that exact media, but they can create their own versions, be it fanfiction, headcanons, their own works inspired by the media, the possibilities are huge."
                                                                      a "I think that is a beautiful idea. Any work has the ability to live and grow far after the creator has made it."
                                                                      n "For a moment it grows quiet on the other side of the phone as Abigail seemingly is lost in thought."
                                                                      a "Oh whoops, I have gone on a bit of a side tangent, haven't I?"
                                                                      a "To answer you clearly, I don't think all of my games have a shared theme. But lately a few of my games have been about the same thing."
                                                                      menu:
                                                                           "Do you really think that's how it works? I don't think the interpretations of others are on the same level as the creator's.":
                                                                                a "And why wouldn't they be [persistent.name]?"
                                                                                a "Aren't they both two works? They might have different content or even completely different forms, but what makes one on a higher level while the other cannot attain that place?"
                                                                                a "Would it perhaps be because the first work is an original and the second one is based on the first, thus less original?"
                                                                                a "Because let me tell you, if that were the case I think most works written in the last hundred, maybe even thousand of years all are of the bottom of the barrel."
                                                                                a "Original thoughts are hard, if not even impossible to come by, so every book, movie, or game borrows elements from another form of media."
                                                                                a "That doesn't make them less than the things they borrow from, right? As long as they just don't blindly copy everything without changing anything I suppose."
                                                                                a "And of course, a media that borrows from another could also start out as set in the original's world, and then slowly be changed into it's own unique setting."
                                                                                a "You hear it constantly, a movie that was based on a book that started as fanfiction about another book. Does it invalidate any of those media in that chain that they originated from something else?"
                                                                                a "I don't think so, sometimes it might even strengthen them. Each work in that chain has the abiltiy to pick the bits and pieces they like, work with those, and leave the rest out if they so choose."
                                                                                a "So yes, I really do think that's how it works. Though it's totally fine if we agree to disagree, I just hope you can see my thought-process behind why I think that."
                                                                                a "Anyway, I hope you got enough info out of that to somehow help Lilly."
                                                                                a "{size=*0.5}Although I'm not sure how that could possibly help.{/size}"
                                                                                a "I have to go now. If you need anything else just call me on your next try. But let us hope you won't need a next one."
                                                                                a "Good luck and goodbye [persistent.name]!"
                                                                                a "Keep Lilly safe will you?"
                                                                                n "And with that she hung up."
                                                                                jump phone_start_choices
                                                            
                                                                           "I see, and what are those games about if you don't mind me asking?" if abby_askedAboutGameTheme:
                                                                                n "It's quiet once again, but this time it's different."
                                                                                n "She isn't thinking about what to say, she is trying not to answer."
                                                                                a "To be honest..."
                                                                                a "I'd rather not answer that."
                                                                                a "Can we talk about something else?"
                                                                                $ abby_askedAboutGameTheme = True 
                                                                                menu:
                                                                                     "Sure, that's alright.":
                                                                                          a "Thank you [persistent.name]."
                                                                                          a "So, what would you like to talk about?"
                                                                                          jump abigail_somethingElse


                                                                 "In the game where you are a raven-prince that has to climb a mountain, who is the saphire person?":
                                                                      a "She is forgiveness, not given by anyone else, but by yourself, to yourself."
                                                                      a "The journey we all have to go on to slowly learn to love and accept ourselves. To not blame ourselves for what happened."
                                                                      menu:
                                                                           "Then why does the player end up back at the start of the mountain after they are forgiven?":
                                                                                a "Forgiveness is not a one-time deal I'm afraid. One resolved issue makes way for us to spot five new ones."
                                                                                a "And yet, we have to keep climbing that mountain."
                                                                                a "We owe it to ourselves, to seek that forgiveness again and again."
                                                                                a "How could you hope to climb other mountains in life if you cannot stop blaming yourself for every step you take on one?"
                                                                                a "Does that make any sense [persistent.name]?"
                                                                                #Probably continue this a bit more.


                                                                 "In the game about the prisoner, who are the people who speak in red, in purple and in blue?":
                                                                      #Make her reluctant to share this info.
                                                                      a "They are not multiple different people, they are the same person."
                                                                      a "Me."
                                                                      a "But to be honest I don't really feel comfortable sharing that with anyone yet. It is too personal."
                                                                      a "I hope you understand."
                                                       "*Pick something else*":
                                                            jump phone_call_abigail_convinced


     else:
          a "[phone_caller]? That doesn't sound familiar, sorry."
          n "Just like that she hung up on you."
          n "Maybe you should try using your real name? With a bit of luck [persistent.date] has already spoken about you to her sister."
          jump phone_start_choices

label phone_call_abigail_topics_distractionforlilith:
     a "Sure I can but why can't she just stay home?"
     if persistent.ending_breakup == True:
          n "Yes player, why can't she just stay home?"
          n "You know she is safe if you just cancel the date, right?"
          n "Are you doing this because you hope she won't end up with Ron?"
          n "She was perfectly happy then, and yet you came back, looking for another solution."
          n "Interesting..."
          n "Or is it not about that?"
          n "Are you doing this so you don't have to cancel the date yourself?"
          n "Or where you just curious about what would happen if you chose that option?"
     n "You inform [persistent.date_sis] about the plane that has crashed into [persistent.date]'s house before and that it will crash into her house again and again."
     a "..."
     a "I see, this is too ridiculous to even make up."
     a "{size=*0.5}What have you gotten yourself into [persistent.date_nickname]?...{/size}"
     a "I don't like to lie to her but if it saves [persistent.date_nickname] I suppose I could act like I was rejected by a girl I liked and just need some support from her.
     I'm sure that will trigger her \"Big sis mode\" and then she will come rushing to me."
     a "She has a problem of almost never putting herself first but I guess this time that's pretty handy for us."
     a "Of course that will mean that your date won't go as planned."
     a "Knowing her there is a pretty big chance she'll forget about the date. She means well, but she is pretty bad with things like that."
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
     a "Mom and [persistent.date_nickname] are pretty mad because he left us but honestly I'm more sad because of it."
     a "I was seven when he left..."
     a "There were so many things I needed help with that he couldn't teach me."
     a "I can't even fully remember him, just small bits and pieces. I'd like to make new memories of him."
     a "It has been ten years and honestly I still need him. I don't hold a grudge against him or anything, I'd even be happy if he decided to come back."
     n "[persistent.date_sis] pauses for a moment."
     a "Could you maybe tell him that the next time you relive this day? "
     $ persistent.david_love_knowledge = True
     menu:
          "I will.":
               a "Thank you [persistent.name]."
               a "We probably shouldn't leave [persistent.date] waiting any longer though. Good luck trying to save her and also don't forget to have fun alright?"
               n "She hung up."
               jump Game_start2

label phone_call_abigail_topics_spoketodavid_davidblameshimself:
     a "That's ridiculous!"
     a "No one blames him for [persistent.date_ghost]' death."
     a "Mom and [persistent.date_nickname] mad at him because he left us, not because of [persistent.date_ghost] death."
     a "He couldn't possibly have predicted what happened. I'm sure he has wished that he could, so he had a chance to prevent it."
     a "Could you tell him that I don't blame him and that I'm sure mom and [persistent.date_nickname] don't either?"
     menu:
          "I will.":
               a "Thank you [persistent.name]."
               a "We probably shouldn't leave [persistent.date] waiting any longer though. Good luck trying to save her and also don't forget to have fun alright?"
               n "She hung up."
               jump Game_start2

                                        


    


label phone_call_david:
     $ persistent.familyContacted = True
     d "Hello, who am I speaking to?"
     $ phone_caller = renpy.input("Enter your name.")
     $ phone_caller = phone_caller.strip()
     $ phone_caller = phone_caller.capitalize()
     d "[persistent.name]? Well I'm not interested in what you're selling so thank you very much but I'm going to hang up no-"
     menu:
          "*Lie* Don't hang up! [persistent.date] asked me to call you.":
               n "You hear the man laugh."
               d "I very much doubt that. Nobody loves me after what I did to them, especially not her. And who can blame them?"
               d "It should have been me instead of him, then all of them would be much happier."
               d "Now I'm going to hang up. Goodbye [phone_caller]"
               n "True to his world David hung up."
               $ persistent.david_nolove_knowledge = True
               jump Game_start2
  
          "[persistent.date_sis] still loves and misses you. She would be happy if you come back." if persistent.david_love_knowledge:
               n "You hear the man sigh."
               d "Poor [persistent.date_sis_nickname]..."
               d "She was too young to remember me for the monster I truly was and she had to grow up without a father."
               d "I ruined my entire family and then I fled like a coward, thinking things would get better for them."
               n "David quiets, seemingly waiting for a response from you."
               menu:
                    "Hang on, you said that you ruined your family and then left them. What happened before you left them?" if persistent.david_blame_knowledge == False and persistent.brother_knowledge == False :
                         label phone_call_david_whatHappenedBeforeHeLeft:
                              d "You don't know about that?"
                              d "The day that [persistent.date_ghost]..."
                              d "On that day I gave him an old polaroid camera I had laying around."
                              d "He loved that thing, ran all over the place taking pictures with it."
                              d "He loved it so much he didn't  notice the car coming from the bend of the road he was standing on to take a better picture of some potato fields or something like that."
                              d "I was absolutely destroyed by it but [persistent.date] even more so since she was really close to her brother. Her mother, Lila was of course also devasted at the loss of one of her children."
                              d "I felt their anger towards me build up until it became so big I couldn't even look them in the eyes anymore."
                              d "I thought things would be better if they didn't have to live with [persistent.date_ghost]' killer. If I wouldn't have given him that camera he would still be alive..."
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
                    "Well, it seems like things were pretty hard for them. Lilith's mom even had to take a second job just to make ends meet." if persistent.lilaWorkedTwoJobs_knowledge:
                         d "What?..."
                         d "She did?"
                         d "But what happened to the money I gave her?"
                         menu:
                              "What money?":
                                   d "Each week I give her as much money as I can afford to in an effort to make sure she and the kids wouldn't lack a single thing they needed."
                                   d "So it's very strange to hear that apparently that isn't enough, especially to the point of forcing her to take up a second job."
                                   d "It's not like she would not be able to tell me if that was the case, right?"
                                   d "I never changed my phone number after all."
                                   d "There was always a part of me that was hoping she'd call."
                                   d "Did she somehow get into debt? That's one of the only reasons I could think of that would make it so that she needs a second job even with the money I sent."
                                   d "She sometimes can be a bit too trusting, so maybe that lead to all of this?"
                                   n "You can hear David sigh on the other side of the phone."
                                   n "And then you can hear him utter something, it's so soft and quiet it almost blends into the white noise of the background."
                                   d "{size=*0.5}What did you get yourself into Lila? All that stress. I wish you didn't feel like you couldn't tell me...{/size}"
                                   d "{size=*0.5}I wish that I could have helped more.{/size}"
                                   d "{size=*0.5}I wish I would have stayed by your side.{/size}"
                                   n "You can now hear soft sobbing, slowly growing in intensity as it drowns out the background noises more and more."
                                   d "I'm sorry [phone_caller], I..."
                                   n "He trails of for a moment, as the words die out the sobbing becomes louder once more."
                                   n "You hear the man try to collect himself by taking a deep breath."
                                   d "I just can't do this anymore. I need to go."
                                   n "He hung up on you."
                                   $ persistent.davidPayedMoney_knowledge = True
                                   jump Game_start2
  
          "[persistent.date] is not mad for what happened with [persistent.date_ghost], she's just mad at you for leaving your family. She might even consider forgiving you if you give a good apology." if persistent.david_apology_knowledge:
               d "I can't face her just yet, can you tell my apology to her?"
               menu:
                    "I will, just tell me how you want to apologize.":
                         d "I want to tell her that I know that nothing I say will ever make up for what I did."
                         d "That every day I am beating myself up for the decision that I made."
                         d "I was a coward, I still am by not facing her directly."
                         d "I wanted to return back to their lives every single day, I still do."
                         d "And yet, there's something inside me that thinks they are better off without me."
                         d "In a way it was selfish to listen to that voice, I should have talked about it with my family."
                         d "They would have understood better than anyone else, as they also lost James that day."
                         d "Instead, I isolated myself from them, I dealt with it all on my own. And I fored them to do the same."
                         d "I would like to tell her that I'm deeply that she had to feel like her own father abandoned her."
                         d "No child deserves to go through such pain. My family lost two people when James died and it was hard enough just losing one."
                         d "I can't undo the wounds I have caused, but I do hope I could, if my family accepts it, try mending them."
                         #TODO:Give the player the ability to tell Lilith this. Also attempt to finish this path of the reunited ending.



label phone_call_james:
     if persistent.met_james == False:
          if persistent.brother_knowledge == True:
               $ mysteriousCallerName = "???"
          else: 
               $ mysteriousCallerName = "[persistent.date_ghost]"
          q "Yo, who is this?"
          $ phone_caller = renpy.input("Enter your name.")
          $ phone_caller = phone_caller.strip()
          $ phone_caller = phone_caller.capitalize()
          q "[persistent.name] eh? Sorry, that doesn't really ring a bell."
          if not persistent.jamesFakoutNumber_knowledge:
               $ persistent.jamesFakoutNumber_knowledge = True
          menu:
               "Yeah, you don't know me. I am a friend of [persistent.date]." if not persistent.jamesFakoutNumber_knowledge and not persistent.brother_knowledge:
                    q "I also don't know a [persistent.date] so I think you might have the wrong number."
                    q "This happens a lot with one particular person for some reason, but usually the number they hang up before I can even say anything."
                    q "So anyway, I have to go now, take care."
                    n "He hung up."
                    n "You are very confused by the info that just got dumped on your plate."
                    n "So whoever this person you just called was, they aren't [persistent.date_ghost], they don't even know someone called [persistent.date]."
                    n "But then why does [persistent.date] have their number saved under the name of [persistent.date_ghost]? Why does she have their number at all?"
                    if persistent.lilithKeepsCalling_knowledge == False:
                         n "You also can't help but think of something else the person you called told you, someone keeps calling his number, the same person."
                         n "Could it perhaps be [persistent.date]?"
                         $ persistent.lilithKeepsCalling_knowledge = True
                    n "This whole ordeal leaves you with more questions than answers, you should probably ask her about it sometime soon."
                    jump Game_start2
               "[persistent.date_ghost]? Aren't you supposed to be dead?" if not persistent.jamesFakoutNumber_knowledge and persistent.brother_knowledge:
                    q "Well I'm not [persistent.date_ghost] man and last time I checked I sure as hell wasn't dead."
                    q "I keep getting called randomy by the same number and now this?"
                    q "You're freaking me out, I'm going to hang up now."
                    n "The person, who you now know isn't [persistent.date_ghost] indeed hung up."
                    if persistent.keptJamesNumber_knowledge == False:
                         n "It seems like [persistent.date] kept her brother's number in her phone, perhaps as a sort of memento?"
                         $ persistent.keptJamesNumber_knowledge = True
                    if persistent.lilithKeepsCalling_knowledge == False:
                         n "You also can't help but think of something the person you called told you, someone keeps calling his number, the same person."
                         n "Could it perhaps be [persistent.date]? Maybe you should ask her about it sometime soon."
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
                         "I just wanted to tell you that [persistent.date_mom] still thinks about you every day, I figured you might want to hear that." if persistent.LilaStillThinksAboutJames_knowledge:
                              j "...Thank you for telling me that [persistent.name]."
                              j "While I did know that already it's been a while since I last heard those words."
                              j "I have been kind of avoiding them to be honest, those words."
                              j "They make all of this a lot more...complicated."
                              j "In here I am inbetween an almost infinite amounts of my two sisters, of my dad and my mom."
                              j "All of them deeply missing me in their own ways."
                              j "All of them filled with so much love for their son, for their brother."
                              j "And yet I am here, inbetween of it all."
                              j "All of their love can never truly reach me, it will always have to be through those bubbles."
                              j "It's like watching a play, I can't help but feel seperated from it all, even though I can watch over all these different versions of my family."
                              j "So I guess it feels good to have you deliver me a message from them personally. It makes me feel more involved than I usually am here from the sidelines."
                              
                              menu:
                                   "I know what you mean [persistent.date_ghost], I feel the same way.":
                                        #TODO: The topic about love being filtered through stuff (bubbles/screen and the paralels between [persistent.date_ghost] and the player REWRITE that topic a lot
                                        j "Oh, you do?"
                                        j "Why is that [persistent.name]?"
                                        menu:
                                             "I keep all my memories of the things Lilith and me go through on each loop, but she doesn't. I get to know her better slowly as one normally would, despite the weird circumstances. But to her I am practically a stranger each time.":
                                                  menu:
                                                       "And I can try to clue her in on what happened, or I can choose not to do that. The end is always the same regardless, in the best case I can just slightly prolongs it from ending. But it always does eventually.":
                                                            menu:
                                                                 "It doesn't matter what I say or do. It really doesn't.":
                                                                      j "I see..."
                                                                      j "I think I might be able to understand were you are coming from."
                                                                      j "This image of Lilith in your mind has been slowly but steadily growing, and yet, to her you are close to a stranger."
                                                                      j "Still, I think it does matter."
                                                                      j "Stranger or not, how you treat her matters."
                                                                      j "Would you rather keep her safe, make her smile, or be relentlessly rude to her?"
                                                                      j "It might always end the same, but you have the power to make her final moments slightly more bearable."
                                                                      j "So what you do matters a lot. Be the kind stranger, not to be remembered, but because it's good."

                                                       "There is a divide between us. This power that let's me save her only alienates me further from her.":
                                                            menu:
                                                                 "At first it was shocking you know, her dying. I didn't expect it. But the more it kept happening the less I felt that shock, moreso... annoyance? Even if I really wanted to save her. To make sure she was happy. At a certain point she became what she was when I started playing, just lines of text. It was easier to distance myself from her":
                                                                      menu:
                                                                           "In the first few loops I saw many new things, learned a lot about her. But then I had to keep looping... and things began playing out like they always had. The same dialogue, the same reactions. She became predicatable, boring.":
                                                                                menu:
                                                                                     "I found myself rushing through her dialogue, in the hopes of finding {b} {i} anything {/i}{/b} new. Anything I hadn't yet experienced. At first that happened every now and then. But soon it started to happen less and less frequent.":
                                                                                          j "Sounds to me like you were setting your up for a gradual dissapointment."
                                                                                          j "There will be a point where you have read every line this game has to offer."
                                                                                          j "There will be if you keep pushing yourself to do that atleast."
                                                                                          j "But think about how much of the same things you would have to slog through to even get to that point."
                                                                                          j "Would it be worth it?"
                                                                                          j "I think it's good to know when to stop, so we don't get caught up in things too badly."
                                                                                          j "Although I guess I don't have a right to speak about such things, with how I still linger here."
                                                                                          j "Or perhaps that exactly is why I do have a right to speak about it. Don't make my mistake [persistent.name]."
                                                                                          j "It's okay to move on, no matter how long you didn't. That will spare you from a lot of hurt in the future."
                                                                                          j "Especially if you chasing a slither of happiness is going to lead up to Lilly dying again, maybe it's just better to throw the towel in the ring?"


                                             "Because I'm seperated from her aswell. The computer screen that gives me access to this world, to her, is an impermeable membrane. This isn't real.":
                                                  menu:
                                                       "She can never truly love {b} {i} me {/i}{/b} as she can't even be aware of my true presence unless I tell her about it. And even then, she can only glimpse it, she can never truly see me. And I can never truly speak my mind to her, I'm always limited by the choices the game forces me to choose from. So how could I possible even show her a slither of my true love?":
                                                            label jamesTalk_dividedExistence:
                                                                 j "That is indeed a hard barrier to break. Especially because you have grown dependent on it to even interact with what's behind it. Even with the best intentions, this will always just be a game to you, even if at some points it doesn't feel like that at all. That's just a fact you try your best to ignore so you can be more immersed. And yet, the very fact that this is a game means you can play it, that you can get immersed in it at all."
                                                                 j "Although I wonder. Isn't that how it works with everyone?"
                                                                 j "We never truly can grasp the depths of any other person, we can only attempt to gauge it by looking at the actions they make."
                                                                 menu:
                                                                      "Yes, but the choices I am given aren't me. They are just random options.":
                                                                           j "And yet it is you who picks a choice from the available ones. One that moves the story further."
                                                                           j "The choices might not {b} {i} be {/i}{/b} you, but the one you pick does say something about you."
                                                                      
                                                                      "I never thought about it like that, what is the point of even interacting with anyone then?":
                                                                           j "Don't you see [persistent.name]? That is precisely the point of interaction. To try to get a glimpse of someone's being, of their thoughts. Of all the things that make them, well... them."
                                                                           j "Sometimes it can be really fun learning that someone you thought you knew actually has some things you don't know about them yet."
                                                                           j "And when you learn even those, you never know if there could be even more things to learn."
                                                                           j "People are wellsprings of so much interesting thoughts, experiences and perspectives that you'll never truly learn them all."
                                                                           j "And that's not something to be dreaded, it's something to be celebrated. Your thirst for more depth will always be met with a stream of new discoveries if you interact with interesting enough people."

                                                       "How could we ever be friends? She can't even be aware of my true presence unless I tell her about it. And even then, she can only glimpse it, she can never truly see me. And I can never truly speak my mind to her, I'm always limited by the choices the game forces me to choose from. So how could I possible even show her a slither of my true love?":
                                                            jump jamesTalk_dividedExistence

                                                  

                                   "That sounds really lonely [persistent.date_ghost], I think you shouldn't sacrifice yourself for your family like this.":
                                        j "It does sound far from ideal doesn't it?"
                                        j "You are absolutely right."
                                        j "And yet, knowing that if anything were ever to happen with them I could help them out from here..."
                                        j "It's one of the only reasons I haven't crossed over yet."
                                        j "Ever since my passing I've been here, watching over them."
                                        j "And every other version of me who got killed is also in a place like this, watching over their own family."
                                        j "Our minds kind of blend together sometimes, it's hard to know where my memories start and were the others' end."
                                        j "I don't mind though, that way it feels a little less lonely in here."
                                        if persistent.major_love_offence_counter <= 2 and persistent.minor_love_offence_counter >= 5 and persistent.major_love_comfort_counter > 2 and persistent.minor_love_comfort_counter > 5:
                                             j "Although you know what is funny?"
                                             j "What you just said, I think it also applies to you."
                                             j "You know you don't owe [persistent.date] anything either, do you? You also don't need to sacrifice yourself"
                                             j "Playing this game over and over with very little changes, is that a good time for you? Do you feel like you're getting something out of this?"
                                             j "Are you doing it just for her?"
                                             j "Be careful that you don't just lose yourself for her, a good balance is necessary."
                                             j "Take that as a piece of precautionary advice from me, from this place."
                                             n "[persistent.date_ghost] motions around the white void, to the strange formations in the background, they almost resemble trees that are stuck in between a solid and a fluid state perpetually."
                                             j "Those... things used to be human too."
                                             n "You try your hardest to imagine the trees reverting to a human, to reverse the process that made them this way, you are unable to see them as anything but the monstrosities they are."
                                             j "It's a side-effect of being here too long. We are supposed to move on after we come here, to be reborn."
                                             j "But a lot of us have... trouble letting go."
                                             j "If I don't move on sooner or later, I will become like them."
                                             j "And still, even knowing that, I can't bring myself to let [persistent.date] go, to let my family go."
                                             j "So please [persistent.name], let her go before it becomes even harder."
                                             j "You are stuck in a situation you can hardly win."
                                             j "It's time to play by your own rules."
                                             j "I've exhausted too much of my energy having this conversation, I'm limited to that extent, you can come visit me again some other time if you'd like although I suggest just giving me a call if you find my number."
                                             j "I'll send you back now, good luck [persistent.name]."
                                             jump game_start
                                        
                                        menu:
                                             "You say you've been watching your family, have you ever thought about reaching out to them?":
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
                                                            j "But it's true, I have noticed an increase in deaths ever since [persistent.date] started dating you."
                                                            j "It's very peculiar."
                                                            j "I should know what is causing it via my connection to my other selves."
                                                            j "And yet the problem is that the info seems to be overlapping impossibly."
                                                            j "There are multiple causes and yet somehow only one."
                                                            jump jamesLowEnergy
                                                       "Lately it seems like death just keeps happening to [persistent.date] no matter what I do, could that be the result of a lingering ghost communicating with the living?":
                                                            j "I suppose that could be possible."
                                                            j "I doubt that's case though. Plenty of ghosts here but a lot of them grow out of being talkative after slowly having their mind degrade after hundered of years of lingering."
                                                            j "I am one of the most recent additions to this place, so don't mistake my talent to chit-chat like something inherent to all ghosts here."
                                                            j "But if this is truly caused by a lingering ghost there is not much you can do, just wait until they are either crossed over or until they simply lose their mind and can't talk anymore."
                                                            j "Don't worry though, that just feels like bad game design, I'm sure the developer wouldn't force you to wait a few years for a new ending."
                                                            jump jamesLowEnergy

                    
 
               "I need help to convince [persistent.date] to listen to David. I figured she might listen to you." if persistent.david_apology_knowledge:
                    j "She probably would..."
                    j "Although I'd rather stay in the shadows. She already has had a hard time dealing with my dead."
                    j "But on the other hand if it manages to atleast salvage her bond with dad slightly it will be worth it. "
                    j "I'm going to tell you a story that you need to tell her, it seems like that tends to work out for you."
                    j "The story takes place in the autumn, I think [persistent.date] was eight years old."
                    j "I was wandering through the forest of our village, the one [persistent.date] likes to call the Kokiri woods. Suddenly I heard crying, familiar crying."
                    j "Following the source of it I found her, [persistent.date], sitting on a treestump."
                    j "When I sat next to her she told me that she had gotten a really bad grade for math."
                    j "She felt like a failure and didn’t think she could go back home to [persistent.date_mom]. I told her that that was absolutely ridiculous and that mom would always love us no matter what. "
                    j "That seemed to calm her down a bit and she stopped crying. To further calm her down I asked her if she wanted to try to find fairies in the woods with me. "
                    j "We spent an hour or so searching for fairies, ofcourse never finding one but at the end of it she forgot all about her bad grade."
                    $ persistent.james_story_knowledge = True
                    jump jamesLowEnergy
     label jamesLowEnergy:
          j "I have to go now, keeping up this connection asks a lot of energy from me."
          n "[persistent.date_ghost] hung up."
          jump Game_start2                   
 
label phone_call_lila:
     $ persistent.familyContacted = True
     li "Hello, are you Sam, [persistent.date_sis]'s teacher? " #(The teacher likes being talked to with just their first name, this makes it eassier for them to be both a guy and a girl if the player is a guy or a girl.)
     menu:
          "Yes, that's me.":
               li "Ah perfect, I've been expecting your call!"
               li "I'm sorry if I offended you by just calling you by your first name. [persistent.date_sis] told me you prefered that but I was not sure if she was joking or not. Sometimes I think I'm too gullible."
               menu:
                    "No worries, [persistent.date_sis] told the truth.":
                         n "You hear [persistent.date_mom] let out a sigh of relief."
                         li "Thank god, I wasn't entirely sure. She likes to play little pranks on me every now and then. She's a sweet kid just a tad mischevious sometimes."
                         li "But anyway, I'm sure you are quite busy so I'll try to not waste much of your time."
                         li "We can start talking about your mail. Thank you once again for agreeing to do it over the phone instead of via mail, I think it's important to be able to hear someone to discuss important things."
                         #
                         menu:
                              "Excuse me but my memory appears to be quite foggy and I can't remember all the details of the mail, could you unclog my memory?":
                                   li "Well, can't you just reread your mail to unclog your memory?"
                                   menu:
                                        "*Say you accidentaly deleted it.*": #TODO:She probably won't believe this and ask you some more questions to prove you're the teacher or something, ask Abigial to help you with those questions.
                                             #TODO: Fill in the rest, you have to make it as the quest version doesn't already have this. (Ask Abby if she can help you with this, turns out she has a backdoor on that teachers computer so she can boost some of her grades a tiny tad. She gives you the info you need.)
                                             li "... Really?"
                                             n "You hear some doubt in her voice."
                                             li "No problem, I'd be happy to refresh your memory if you can tell me anything about Abigail only you would know."
                                             menu:
                                                  "I'm not sure what I could tell you to be honest. You do understand that that is a pretty strange thing to ask someone, right?":
                                                       li "Look Sam, I'm having a really hard time believing that."
                                                       li "Even if I did believe it, I know mails you delete can just be recovered."
                                                       li "I might be seen as naïve by some but make no mistake \"Sam\", I'm not stupid."
                                                       li "I'm not sure what you want by pretending to be my daughter's teacher but I suggest you drop the act."
                                                       li "If I find out that you have bothered me or my family again after I end this call I'll have to take some measures."
                                                       li "Goodbye."
                                                       n "She hung up the phone, seems she saw right through you."
                                                       n "You might need to learn more about Abigail if you want answers. Or you could try asking her if she knows what her teacher wanted to discuss."
                                                       jump game_start2

                              "Actually I would like to talk about your financial status. Abigail has recently brought it to my attention that you are struggeling and I would like to inform you about some programs we have that could help out with that." if persistent.davidPayedMoney_knowledge:
                                   li "Oh..."
                                   li "I see."
                                   li "Well Sam, I'm not sure why Abigail has brought that up because that's not really the truth at all."
                                   menu:
                                        "Oh I see... I must have misheard something and took some wrong conclusions. I thought I had heard Abigail mention that you had to take up two jobs to support you and your family.":
                                             li "Ah yes, that..."
                                             li "I indeed have taken up two jobs for quite a while, I find it weird that Abigail decided to mention it now actually."
                                             li "But let me assure you Sam, without going too much into unnecessary detail, that that's fully my own choice and we won't need your programs."
                                             li "Thank you for informing me about it though, that was a very sweet thing of you to do."
                                             #TODO: Fill this out a bit more, and make it learnable that she is not in debt, you can confront her during the phone call in the kokiri woods about this.
  
  
  
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
               n "The name of the game is \"Great date with [persistent.date]\" so unless you like not playing this game you better choose the other choice next time."
               #TODO:Find a way to lie about the name of the game in renpy so this can be a shocking reveal later. Maybe have a name with a double meaning? Something like "A date you won't forget.""
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
          $ ending_check = "quitter"
          #$ persistent.game_credits = True
 
     elif persistent.lildeaths <= 20:
          if persistent.kokiri_knowledge == True and persistent.kokiri_death_1 == True:
               n "Maybe it's for the best..."
               n "But is it really?..."
               n "The thought keeps gnawing at you. There has to be another way, right?"
               #Ending
               "An ending."
               $ persistent.ending_anEnding = True
               $ lilithAliveEnding = True
               $ ending_check = "anEnding"
               $ persistent.game_credits = True
          elif persistent.kokiri_knowledge == False:
               n "I have a feeling you are really close to a breakthrough, maybe there is something you are missing?"
               n "You could also just stop here, but there is so much more to see."
               n "Would you really want to miss all that extra stuff?"
               #Ending
               "The unseen content ending."
               $ persistent.ending_unseenContent = True
               $ lilithAliveEnding = True
               $ ending_check = "unseenContent"
               $ persistent.game_credits = True
 
     elif persistent.lildeaths > 20:
 
          n "Letting go is never easy."
          n "You had at least [persistent.lildeaths] opportunities."
          n "It's good to take it after all this time [persistent.name]"
          n "At the very least you know [persistent.date] will be fine."
          n "At the very least you still have all of your memories of the times you spent together."
          n "If only you could somehow make more memories and have her survive..."
          n "If only..."
  
          #Ending
          "Letting go ending"
          $ persistent.ending_lettingGo = True
          $ lilithAliveEnding = True
          $ ending_check = "lettingGo"
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
          l "You were... joking?"
          l "About something this morbid?"
          l "You appeared to be so serious about it too.."
          l "This is too much for me [persistent.name], I can't do this anymore."
          l "I think I'm just going home."
          jump car_death
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
          l "[persistent.date]  looks at you with a sceptic look in her eyes although you can tell that she's secretly excited."
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
          n "[persistent.date] looks absolutely flabergasted, her mouth is slightly opened and seems to be frozen for a moment or two."
          l "So you were actually speaking the truth?
          You really are living in some sort of groundhog-day like scenario?"
          l "Even with that proof it's pretty hard to get my brain to accept it."
          l "I feel like when I'm going to admit I believe you there is going to come an entire camera crew out of nowhere and I'll be made fun of in some bad tv show."
          l "But let's say I am starting to believe you a little bit so we won't have the camera crew barge in on us just yet."
          l "So what is this all about?"
     elif psychic == True:
          n "Suddenly you catch a glimpse of utter shock on [persistent.date]'s face."
          l "Wait, you... You guessed the word I was thinking of?"
          l "I mean sure, you said you would do that but I didn't expect for you to get it right if I'm being honest."
          l "This all feels so surreal, I mean I'm starting to believe you but I feel like if I say I completly believe you some cameracrew will come out from their hiding spots and make fun of me for believing something so stupid."
          l "So if I'd hypothetically believe you, what is all of this about?"
     jump proof_whatIsItAllAbout

label proof_giveAnswer:
     if groundhog == True:
          $ persistent.groundhog_answer_right_knowledge = True
          l "Uhm, alright, but that defeats the purpose of this doesn't it? The number I had in mind was -72,8947."
         

     elif psychic == True:
          $ persistent.psychic_answer_right_knowledge = True
          l "Uhm, alright, but that defeats the purpose of this doesn't it? The word was thinking of is electronegativity."
     
     if chinese == False:
          l "Listen, I do appreciate you saving me, but do you really think you can just lie to me?"
          l "Clearly something else is going on here, something that you're not telling me. I'm just not sure what that would be."
     else:
          l "Alright, you can't just tell me I was going to die if I ordered that Peking duck and then make up a crazy story without proof."
          if love_meter >=2:
               l "I tried to take it seriously, I really did, but you aren't giving me anything that makes it possible for me to keep believing you."
          else:
               l "I knew that you were just messing with me. Or even worse, that you really believe what you just told me."
     l "This is all a bit much for me, I think I'm better of heading back to home."
     jump car_death




     label proof_whatIsItAllAbout:
          if persistent.kokiri_death_1:
               $ persistent.restaurantNoExtraDialogue = True
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
    
                    "You have an aura of death surrounding you [persistent.date], I'm trying to keep you safe with my powers.":
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

     if psychic == True:
          l "Wait what, why would you need that?"
          l "I thought you said you were a psyhic, aren't you clairvoyant?"
          n "You come up with a half-hearted excuse that you are only slightly clairvoyant and the rest you fill in by projecting your mind into the past. Thus time-travalling via astral projection."
          if chinese == True:
               n "Lilith looks at you sceptically but she's too far in to go back now."
               n "She decides to just atleast try to buy that explanation for now."
          else:
               n "Lilith looks at you sceptically, but since you did safe her life she decides to roll with it."
     
     l "..."
     l "This is begining to hurt my head if I'm honest with you [persistent.name]."
     l "But if what you are saying is indeed real, than this is very important."
     l "How could I convince my past self to trust you?"
     l "Oh, I think I have an idea!"
     l "If you truly have the ability to restart this day, that means you can choose what restaurant to go to when I call you again, right?"
     l "Well how about this, I will tell you a story I never told anyone else before."
     l "But I will separate it in parts for each restaurant."
     l "I believe the order I suggested them in was the burger place, the cafe and then the chinese restaurant."
     l "So that will also be the order I tell you the story in, so I will tell you the start in the burger place, and the end in the chinese restaurant."
     l "You got all of that?"
     n "You give her a quick nod."

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

     n "A wide grin appears on [persistent.date]'s face."
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
     n "[persistent.date] gives you a thumbs-up and a cute laugh."
     l "And despite the odds you did everything you could and saved me! You are... sort of my hero now?"
     n "[persistent.date] begins to turn a bright red, she begins to more closely resemble a cute tomato than a human."
     n "Somehow she must've noticed her excessive blushing as she covers her face up with her hands and begins to giggle."
     l "Sorry, once I get blushing I turn beet red really quickly."
     jump restaurant_death_2
label loopGone_everyRightToBeHappy:
     l "Huh, you are right, aren't you?"
     l "I shouldn't seek justification for my feelings.
     Especially now, we literally cheated death itself so I have every right to feel ecstatic!
     Well, it was mostly your work but still, that doesn't happen every day."
     n "[persistent.date] lets out a small chuckle."
     l "I suppose that it happened quite a few days for you but still, that's cheating!"
     n "[persistent.date] pauses for a few seconds while looking you into the eyes.
     A soft smile has formed on her lips."
     l "Thank you [persistent.name], thank you for both saving me from my impending doom and for this date.
     I am really having a blast right now, although I must admit I had a slight headache trying to get my head around this whole thing."
     jump restaurant_death_2

label loopGone_happyForYou:
     l "Then come dance with me!"
     n "[persistent.date] gets up and beckons you closer with a wide smile."
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
     n "You are happy to indulge in the dancing, as it makes you spend some precious time with [persistent.date]. You are however not all too happy when you think about what is going to happen next, you try to ignore it but the thought keeps lingering in your head all the same."
     jump restaurant_death_2
label loopGone_happyForYou_real:
     n "Knowing that you finally saved [persistent.date] fills you with seemingly endless energy."
     jump restaurant_death_2





label groundhog_breakingLoop_loopStillExists:
     l "Ah, so the loop still exists?"
     l "I mean, me dying constantly doesn't seem like it's much fun but look at it from the bright side!"
     l "We could form a team to be true heroes!  With your ability to relive the same moments and with my ability to... well die, I suppose, we could be practically unstoppable!"
     l "We would be able to prevent disasters even before they happen."
     l "Well, that is if we ever get out of here alive in the first place."
     n "[persistent.date] lets out a small chuckle but the concern in her eyes is clearly visible."
     l "Sorry, I know I'm overdoing it. This is all just a bit too much for me."
     l "I mean imagine that someone you were dating told you that you kept dying over and over in a timeloop."
     l "That would be pretty mind-boggling, wouldn't it?"
     l "Yes, I suppose that's one way to put it."
     l "And if I'm being entirely honest a part of me still expects the crew of one of those bad prank shows to jump out from somewhere."
     l "Even though another part of me does believe you, which might be even more terifying."
     n "[persistent.date] lets out a small sigh and tries to give you a sincere smile."
     l "But it's not that useful to keep groaning about our situation, is it?"
     l "Maybe it's a better idea to get some information that we can use."
     n "[persistent.date] pauses for a few seconds."
     l "For example, what do you think will happen once we make it past this date? Past this day even, do you think you would be stuck in a loop of reloading day after day for the years that we spend together or that all of this will go away when we make it through today?"
     menu:
          "We might be in this situation for the rest of our lives.":
               jump loopStillExists_forTheRestOfOurLives




          "It should only be this day that keeps repeating, I hope so atleast.":
               l "Hmm, then I wonder what made you experience a groundhog day scenario on this day and not any other one."
               l "Would it have been caused by our date? And if that's the case then what would you need to do to get out of it?"
               menu:
                    "I don't believe it has to do with this date itself. It might be unrelated.":
                         l "You really think so?"
                         l "I suppose it is possible... but I have to admit that it feels very unlikely"
                         l "Although if that truly is the case I suppose me dying is unrelated to the loop."
                         l "Which means we are very lucky that you are stuck in a loop, otherwise you wouldn't be able to save me."
                    "Maybe we should not go on this date next time it loops?" if persistent.burger_death_2 and persistent.cafe_death_2 and persistent.chinese_death_2:
                         if love_meter >= 2:
                              l "...You really think so?"
                              l "As much as I hate to say it you could definetly be right."
                              l "Maybe this loop is just the Universe itself being against us dating, as ridiculous as that sounds."
                              l "Although I would prefer if there would be another way. Because I really am enjoying my time with you."
                              l "But I think we definetly should keep that option in mind."
                              l "If you have to sacrifice too many of my lives to make progress it might be our only option."
                         else: 
                              n "She seemingly let out a small sigh of relief."
                              n "She is not aversed to the idea of never seeing you again."
                              l "I think you are right."
                              l "This loop might be trying to show us that we do not work well together."
                              l "And who are we to fight against that, right?"
                    "Maybe we just need to make sure you survive this date? Perhaps the loop is protecting you?":
                         l "That is an interesting idea." 
                         l "I'd say it definetely is worth a shot." 
                         l "Although before this loop I never really had any close encouters with death, so I have to say I'm still slightly sceptical." 
                         l "But right now I think any logical lead we have might be worth following."       
               if burger == True:
                    $ changeableWord = "was killed by that lost bullet"
               elif cafe == True:
                    $ changeableWord = "was killed by that merlin"
               elif chinese == True:
                    $ changeableWord = "died because of my allergy"  
               l "So last time I [changeableWord], right?"
               n "You give her a quick nod."
               l "And you said the loop was still not broken, so what will end up happening next?"
               menu:
                    "Actually you're still going to die, this time because of a swarm of geese." if chinese and persistent.chinese_death_2:
                         jump loopStillExists_stillDying

                    "Actually you're still going to die, this time due to a gas explosion." if burger and persistent.burger_death_2:
                         jump loopStillExists_stillDying

                    "Actually you're still going to die, this time you will drown." if cafe and persistent.cafe_death_2:
                         jump loopStillExists_stillDying
                    "I don't know, we never got this far here before. I just have a hunch the loop is still not broken.":
                         l "Oh I see, so there is still a chance I will li-"
                         jump restaurant_death_2
               
               label loopStillExists_stillDying:
                    if chinese:
                         l "What? Geese? That is ridiculou-"
                    else:
                         l "{size=*2}What? We need to do somethin-"
                    jump restaurant_death_2


label loopStillExists_forTheRestOfOurLives:
     l "I really hope that will not  be the case, I don't want to die too early ofcourse, but when I have lived a long life and my time has come I'd be more than happy to go."
     n "[persistent.date] looks at you as to make sure you're processing all of this, you give her a silent nod and she continues."
     l "I mean, imagine what a nightmare it must be for the both of us."
     l "You would be cursed with always having to save an old lady that could literally die any moment, always just buying her a few extra hours."
     l "And I would be cursed with never getting to pass away, I would be the oldest person that was ever alive and just be a living heap of flesh and wrinkles after a year or 200."
     l "No matter how much I would pray for the sweet release of death it would never come, or atleast I would never be aware that it came as you would just rewind and try to fix it."
     n "[persistent.date] shudders."
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
     n "[persistent.date] scratches her head."
     l "So, why do you think I keep dying all of the sudden?"
 
     menu:
          "I think it has to do with me, everytime we are together you seem to end up dying.":
               jump groundhog_escapeFate_myFault
 
          "It seems like fate wants it for some reason.":
               jump groundhog_escapeFate_yourFate


label groundhog_escapeFate_myFault:
     n "[persistent.date] bursts out laughing."
     l "Sorry, it's still a bit much to take in right now."
     l "Actually scratch that, it's way too much to properly take in."
     if love_meter >= 2:
          l "Sometimes I laugh when I'm uncomfortable."
          l "It's a sort of coping mechanism I'm afraid."
          l "That way I can distance myself from the seriousness of whatever it is that I need to distance myself from."
          l "It's hard to accept this as being real, even if I do trust you and you have given proof."
          l "I guess I'll just have to try to help you think this through."
          l "It's not like me losing it is going to be of much help anyway."
     else:
          l "None of this feels real."
          l "I know you offered me some proof but I'm still not entirely sold on it if I'm being honest."
          n "You hear her sigh very deeply."
          l "{size=*0.5}I can't believe I'm even entertaining this, still, better safe than sorry.{/size}"
     l "So, our dates always end up killing me, right?"
     if love_meter >= 2:
          l "Do you know what happens if we don't go on a date?"
          l "Have you ever tried cancelling this date?"
          l "Maybe then I wouldn't die?"
     else: 
          l "Have you ever considered not going on this date?"
          l "That would save me, wouldn't it?"

     menu:
          "Actually I tried to warn you about your death, tried to break up with you, tried just not showing up but it all ended with you dying either way. (Lie)" if persistent.plane_knowledge and persistent.ending_breakup and persistent.times_phone_declined > 0:
               #This is a lie. Not picking up the phone makes her live.
               jump escapeFate_myFault_ITriedTo
  
          "But I love spending time with you, I'd hate to have to throw all of that away.":
               jump escapeFate_myFault_butILoveYou
  
          "I haven't tried that yet actually.":
               jump escapeFate_myFault_didNotTryYet
label escapeFate_myFault_ITriedTo:
     l "Really?"
     l "..."
     l "I'm sorry [persistent.name], I have no idea what to say to that."
     l "Things are even worse than I thought."
     l "If even just not going on this date still kills me, what hope is there?"
     if persistent.ending_breakup == True:
          n "Luckily for Lilith that is not the case, as she does survive you cancelling the date. Unluckely for her, you don't tell her that."
          n "Why I wonder? Are you scared she wouldn't put up with you if she knew?"
          n "I'm not sure lying is that much better of an alternative, considering you just crushed her hopes of surviving."

     l "We are just stuck in this loop, forever."
     l "I want to believe there is a way out, I really do. But it seems the odds really are stacked against us."
     l "But still, I guess we have no choice but to go through this over and over and over."
     l "Maybe we'll find a loophole?"
     l "Maybe you still can give something you haven't tried a shot?"
     l "I guess not though..."
     l "At this point I'm just trying to cope with the situation."
     l "If I have to die, let it atleast be with a slither of hope in my heart, however small it may be."
     jump restaurant_death_2
label escapeFate_myFault_butILoveYou:
     if love_meter >= 2:
          l "Well, I also like spending time with you..."
          l "It would be a shame if we had to sacrifice it all."
          l "Besides, wheter you would or not do that, I would never know about it or this conversation."
          n "[persistent.date] lets out a little laugh."
          l "Funny how those things work right?"
          n "[persistent.date] scratches her head."
          l "But if all else really fails we might have to consider not seeing eachother again."
          n "She lets out a big sigh."
          l "However, I have a feeling that there must be another way to solve our little problem, I'm practically sure of it!"
          l "If all else fails we'll just have to confront the Moirai themselves!"
          n "She seems to be taking all of this pretty well for a woman who just heard that she dies repeatedly."
          
     else: 
          if not chinese:
               l "I'm not sure if you understand [persistent.name], my life is literally at stake."
          else:
               l "Well, if I were to trust you, this is literally a matter of life and death."
          l "Would you really squander my life just because you like spending time with me?"
          l "Have you ever stopped to consider how that would make me feel [persistent.name]?"
          l "It sounds to me like you are not at the slightest concerned about that."
     jump restaurant_death_2

label escapeFate_myFault_didNotTryYet:
     l "Well, maybe that's worth looking into then even though it's probably quite a long shot."
     menu:
          "But that would mean we wouldn't know eachother like this, if the loop breaks I will not have been on this date with you. ":
               jump didNotTryYet_neverMeet

label didNotTryYet_neverMeet:
     n "[persistent.date] rubs her chin for a moment."
     l "Hmm, I suppose you are right..."
     l "Once you manage to break the loop by not showing up or something like that I wouldn't want to have something to do with you in the first place."
     l "Besides, even then I doubt you would be able to convince me about this whole groundhog day thingy."
     l "You wouldn't be able to relive that moment anymore so your tricks would quite literally be useless "
     n "[persistent.date] looks saddened for a moment before she tries to give you a wide smile, you can tell it's quite forced."
     l "You know, I got a feeling that won't be the case so you can always give it a shot if you want."
     n "She grows slilent for a moment."
     l "But just in case something does end up happening and causes you to never be able to see me again."
     l "I want you to know that I really liked our time together..."
     jump restaurant_death_2


label groundhog_escapeFate_yourFate:
     l "...What? Why?"
     l "It feels pretty weird that fate has a bone to pick with me, right?"
     l "What exactly did I do that would warrant something like that?"
     l "You saved me from dying before, right? Maybe this is what happens if you somehow go against your fate?"
     l "Maybe fate is just trying to correct it's mistake by making sure that what needs to happen..."
     n "She trails of for a moment, seemingly deep in thought."
     l "Although I'm not sure about this at all. If I am truly fated to die that's horifying."
     l "I still had so much things I wanted to do, so much experiences to live through."
     l "And now that's all ripped away from me, just like that. Because fate had other plans."
     l "If we somehow manage to escape fate for now, who's to say it won't come to play with us later?"
     l "We truly are at the mercy of a force we do not even fully understand. It could strike at any moment during the rest of our lives."
     l "If you knew you could die at any moment, could you really live at all?"
     menu:
          "Is it really that different from everyone else? Everyone could die at any moment, death is quite random in that regard.":
               l "Oh, can't you see [persistent.name]? If anything this shows it's far from random."
               l "To have multiple deaths in different locations and circumstances happen to me..."
               l "Something more is going on."
               jump restaurant_death_2

          "I think we should precisely try to truly live because we could die at any moment.":
               l "I suppose you do have a point [persistent.name]..."
               l "If I never let go of the fear of dying then it will be like I'm already dead. I wouldn't be able to appreciate this extra time you gave me."
               l "Still, something inside of me is just gnawing away at me. How much extra time did you give me?"
               l "Is it an hour or so? A few minutes?"
               if burger == True:
                    $ death_narration = "It seems she was quite optimistic, you only bought her a few extra seconds."
               elif cafe == True:
                    $ death_narration = "It seems she had a bit of luck, she had a few extra minutes of life thanks to you. Though maybe she would wish she didn't."
               
               jump restaurant_death_2 


label psychic_auraOfDeath:
     l "An aura of death? Are you joking?"
     n "Your serious look tells [persistent.date] you are anything but joking."
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
     n "[persistent.date] gives you a wide smile, you feel like you could beat the universe itself."
     menu:
          "We actually did it, I still can't believe it!":
               jump restaurant_death_2


label explanation_stillDying:
     if chinese == False or chinese == True and love_meter >= 2:
          l "What?"
          l "In that case, what are we waiting for [persistent.name]?"
          l "We need to get out of here as fast as possible."
          
          
          menu:
               "You are right, we have no time to waste.":
                    jump explanation_noTimeToExplain
               "We can't, if we do that a car will hit you and you will also die." if not car_free or not car_caught:
                    l "So this is it? We just wait until death catches up with me?"
                    l "Can't we do anything else?"
                    if cafe:
                         l "Maybe we could try to go to the second floor of this cafe?"
                         l "That way the water would have no way to reach us and we would be safe."
                         menu:
                              "That's a great idea, the only problem is that there is a really big and heavy closet blocking the stairway.":
                                   jump restaurant_death_2_preventionAttempt
                    elif chinese:
                         l "Maybe we could try hiding out in the restrooms so the geese don't find us?"
                         menu:
                              "That's a great idea, not like we have much other options so we'll give it a shot.":
                                   jump restaurant_death_2_preventionAttempt
                    else:
                         l "I guess not..."
                         l "The best we could do is seek cover, hoping that we are somewhat safer."
                         l "So this really is it."
                         l "I'm scared [persistent.name]."
                         menu:
                              "Me too Lilith.":
                                   l "Is it weird to say that's kind of comforting?"
                                   l "Otherwise I would have been the only one to carry this burden between all these people who have no idea what is about to happen."
                                   l "I'm glad atleast you are here to understand it aswell."
                                   l "You've already seen this death right? Is it bad?"
                                   l "Actually, don't tell me, I'd prefer not to know."
                                   l "Not a whole lot of people know the exact way they will die and on what moment it will happen."
                                   l "I don't want to know the aftermath of my death aswell, I'm already cursed with too much info."
                                   l "But before..."
                                   l "Well, you know..."
                                   l "I'd just like to tell you that I don't blame you for telling me about the next death. I appreciate the honesty."
                                   l "Afterall, I'd like to believe we are a team."
                                   l "I'd rather not have to face this alone so I'm happy I don't have to."


                              "It will be over soon, don't worry.":
                                   l "I'm not sure if that makes it any better to be honest."
                                   l "Because if it'll be over soon it is also soon approaching."
                                   l "And as that moment gets closer and closer I can feel my stomach shriveling up out of fear."
                                   l "Usually when you would die you are not this aware of it, and even if you knew you would die you almost never know exactly when."
                                   l "And now that we both know how it's going to end for me all we can do is just wait for the inevitable."
                                   l "I know there is probably nothing we can do, atleast not this time."
                                   l "And yet I still can't help but try to come up with anything that will make me survive this. But I can't come up with a single thing."
                                   l "If I truly could accept that this is the end then maybe it would be easier. But I can't. Accepting that would probably break me."
                                   l "Even know I'm hoping this is a really elaborate prank that will make me hate you when it's over."
                                   jump restaurant_death_2

               
                    jump restaurant_death_2

     else: 
          l "Really? I was sceptical about the allergy thing and then you bring up me dying to geese next? That's just ridiculous."
          if psychic == True:
               $ fritfood == "word"
          else: 
               $ fritfood == "number"

          l "I will admit that I have no idea how you guessed the [fritfood] I was thinking of but this, all of this, is just some sort of practical joke, right?"
          l "Sure, you gave me one piece of proof, but your actions here today spoke volumes. You don't care enough about me to want to save me. Otherwise why would you treat me so badly?"
          l "I'm out [persistent.name], whatever this is, I don't want a part in it."
          jump car_death
          

label restaurant_death_2_preventionAttempt:

     if burger and burger_car_death:
          $ stillDying_noEscape = True
     if cafe and cafe_car_death:
          $ stillDying_noEscape = True
     if chinese and chinese_car_death:
          $ stillDying_noEscape = True
          
     if cafe:
          l "Is it really that heavy? Maybe we could move it out of the way just enough to brush past?"
          l "Let's go take a look at it."
          n "Lilith and you walk to the enormous closet made of lignum vitae."
          n "She inspects it for a brief moment and then lets out a deep sigh."
          l "Okay, there is no way we can move {b} {i} that{/i} {/b}, right?"
          l "What is it doing here anyway?"
          l "Maybe we should just go to that barista and ask him about it? Maybe there is other staff somewhere that could help clear the stairway."
          n "Lilith and you walk away from the closet and are heading towards the barista. As she passes you, you notice the urgency in her step."
          l "Hello, I'm really sorry to bother you, but we wanted to go up to the second floor and noticed there was a gigiantic closet blocking the way up."
          b "Ah yes, the closet..."
          b "I'm really sorry about that."
          b "Our manager thought it would be a good idea to buy that closet to put it on the second floor. He claimed it would look beautiful there."
          b "The folks he bought it from said they would bring it up the stairs after our manager told them it was only a few steps high."
          b "... He may have slightly understated how many steps it {b} really {/b} is."
          b "When they saw for themselves, they left it right in front of the stairs."
          b "We are currently looking into getting it upstairs safely. Our manager said a few people who could get the job done would come by tomorow."
          b "In the meantime I'm afraid you can't go up there, we are sorry for the inconvenience."
          menu:
               "But it's an emergency! We need to get that closet out of the way now!":
                    b "What is the emergency?"
                    menu:
                         "We really want to see rest of the aquarium upstairs.":
                              
                              b "I'll be with you in a bit. There are some other customers that need to be served first."
                              n "It might be your imagination but you think the barista is deliberately taking his time with every customer to keep you waiting longer."
                              n "When every customer is helped with he looks around one last time to see if no one else, anyone else, needs him."
                              n "He even waits for a few seconds in the hope that someone might want to order something extra and delay him from talking to you, even if just for a minute or so."
                              n "When no one comes by the barista lets out a heavy sigh and tries to put on a fake smile."
                              n "It fails miserably. For a second you can see he is thinking about wheter or not to attempt it again but he just shakes his head ever so slightly and drops his fake smile instantly."
                              b "Look, while I understand that the both of you want to take a look, that is far from an emergency in my eyes."
                              b "If you really want to take a look I would recommend to come back after tomorow, by that time the closet will be removed."
                              n "But you don't have until then, in fact every word the barista says makes you realise you don't have much more time left at all."
                              n "Suddenly you hear the sound of cracking glass as it rapidly spreads all over the aquariums."
                              n "The weakened glass can't hold the water much longer as it bursts through it's confines."
                              n "The water starts pouring out of the aquariums, the fish are flopping around on the floor, covered in about a few centimeters of water already."
                              n "The people in the cafe desperately make their way to the exit, when they realise the door doesn't seem to be able to open they panic even more."
                              n "They push against it with all of their strength, but the door doesn't even budge."
                              n "Soon the fish are able to swim around freely, the water now comes to around your middle."
                              n "Lilith and you give eachother a knowing look."
                              if love_meter > 2: 
                                   n "The two of you wait for death in eachothers arms."
                              else: 
                                   n "All you can do is wait for death."

                              n "And you do not have to wait long at all for it."
                              jump gameOver


                         "We are all going to die! This whole place is going to get flooded!":
                              n "As you speak those words you begin to hear the commotion in the cafe turn into pure silence."
                              n "All the people that were happily chatting it away while eating now all look at you. Then they begin to whisper to eachother."
                              n "The barista notices this too, his face turning pale."
                              b "Listen, I'm kindly going to have to ask you to leave, you are scaring our customers. This place is not going to get flooded, the aquariums are very sturdy."
                              n "He tries to say that last part as convincing and assuring as a slightly awkward teenager can."
                              n "Sadly, regardless of how good his performance would have been, your words have robbed a lot of people from their appetite."
                              n "Quite a few customers begin to leave."
                              n "The barista looks even more terified now."
                              b "I would like you to leave now sir, or I will have to call the cops."
                              n "Lilith and you shamefully start walking towards the exit."
                              l "I think you might have come across slightly too strong [persistent.name]."
                              l "So, when we step outside we- or I will die, right?"
                              n "She whispers it, not wanting to freak out the remaining customers even more."
                              l "But if we stay here we drown."
                              l "I guess getting hit by a car is better in that case? Probably a lot quicker."
                              n "You can cleary hear the fear in her voice, even though she is trying to hide it."
                              l "I mean, it does make me feel slightly better that our failed attempt atleast got some customers to escape."
                              n "The two of you leave the cafe in shame."
                              if persistent.cafe_car_death == True:
                                   n "And just like clockwork the red Sedan shows up once more."
                              elif persistent.chinese_car_death or persistent.burger_car_death or persistent.kokiri_death_2: 
                                   n "Suddenly you notice the red Sedan. It seems you aren't safe from it in here either." 
                              else: 
                                   n "Suddenly you notice a red Sedan."
                              n "It drives straight into the two of you."
                              jump car_death_result
     elif chinese:                 
          n "Lilith and you walk into the women's restroom together."
          n "There is no one else there."
          n "You smell the destinct scent of roses, upon further inspection it seems to come from an aroma difuser."
          l "So, in here we should be safe, right?"
          n "You can only hope, but you are far from certain."
          n "Suddenly you hear it again. The sound of screaming, slowly being overpowered by quacking."
          l "So that is how I died?..."
          l "It's hellish."
          n "For a moment you consider telling her that you are not sure wheter she died to the geese or not, because you never saw her corpse, but that you know that if she hadn't died, she would wish she had. "
          n "You refrain from telling her that, probably for the best."
          n "Lilith’s hands tremble as she grips the edge of the sink. Her breathing is shallow and uneven, her eyes darting around the small restroom as though expecting the walls themselves to collapse inward. Tears well up but don’t fall, her face frozen in a mixture of fear and desperation."
          l "This isn’t real, right? I mean... it can’t be real. It’s just geese. Just stupid birds..."
          n "This could not end soon enough for the two of you. And yet it doesn't seem to any time soon."
          n "In fact, it seems to last longer than you remember."
          n "Something's different, but what?"
          n "It's the same day over again, right? Nothing can be different except..."
          n "Except you, hiding with Lilith in the bathroom."
          n "Are they searching you?"
          n "No, last time they didn't take you with them."
          n "They are searching her."
          n "The restroom door bursts open with a deafening bang, the force rattling the hinges. A cacophony of flapping wings and maddening quacking fills the air as several geese flood into the small room, their eyes gleaming with malicious intent."
          n "Lilith lets out a strangled scream, backing away until she is pressed against the tiled wall. You try to shield her, but it's futile. You are no match for 100 geese, for a 1000 geese, for an uncountable amount of them."
          n "The restroom door bursts open with a deafening crash, and before you can fully process what’s happening, a blizzard of white feathers engulfs the room."
          n "You try to shout, to do something, but before you can make another sound, everything turns to white—the white of pesky geese feathers."
          n "The pain you feel is excruciating, sharp and overwhelming, as the geese descend upon you like a merciless force of nature. The cacophony of honking grows distant as darkness takes over, and you fall unconscious."
          n "When you wake up again, the restroom is silent and Lilith is gone."
          n "The room is completely filled to the brim with geese feathers, blanketing every surface and swirling lazily in the air. Just thinking about it makes your nose itch, and you begin to sneeze uncontrollably."
          n "Between sneezes, you notice it, the same sticky note they left last time, on your hand once again."
          n "You already know what it says but decide to read it anyway."
          n "It reads as follows: \"We took everyone and you won't be seeing them back. Let this be a lesson on why you should not eat or serve geese or ducks, as those are also part of our family. Also, we are not stupid.
          - Sincerely, the geese\""
          jump gameOver

          
    

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
          "Actually you're still going to die if we stay here, this time by drowning." if cafe and persistent.cafe_death_2:
               jump explanation_stillDying

label youwouldntbelieveme_doNotteaseDeath:
     l "Common, let's celibrate. We just escaped death!
     Don't be so worried, what's the worst thing that could happen?"
 
     menu:
          "Yeah, you're probably right... Wait, why did you say that? Now we are going to die for sure.":
               jump restaurant_death_2

label youwouldntbelieveme_teaseDeath:
     $ teaseDeath = True
     n "[persistent.date] and you high five eachother, you've won. Congratulatons!"
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

          "Actually I sense another death approaching, this time it will be a swarm of geese." if chinese and persistent.chinese_death_2:
               jump explanation_stillDying

          "Actually I sense another death approaching, this time it will be a gas explosion." if burger and persistent.burger_death_2:
               jump explanation_stillDying

          "Actually I sense another death approaching, this time you will drown." if cafe and persistent.cafe_death_2:
               jump explanation_stillDying

label psychic_justHelpingOut_totallySafe:
     n "[persistent.date] gives you a thumbs up and plays a few notes on an air gitar."
     l "We actually did it, that's awesome!"
     n "[persistent.date] opens her arms and motions to you with her head."
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
     l "..."
     l "Listen, I can't do this."
     if chinese:
          l "You can't just tell me something like that and then not explain any further."
          if love_meter < 2:
               l "Is this your idea of a joke?"
               l "This is sick."
               m "I'm done, this is too much for me."
          else:
               l "Look, I really want to believe you [persistent.name]."
               l "But you need to understand that you give me very little to work with here."
               l "This just comes of as weird if I'm being honest."
     else:
          l "You can't just not give me anything after what just happened."
          l "I'm really thankful for you saving my life and everything but I think you could atleast give me some semblance of an explanation." 
          l "I would have died if not for you saving me."
          l "I want to understand [persistent.name], I really do."
          l "But this is just way too much."
     l "I think it's better for the both of us if I just leave."
     jump car_death



label explanation_noTimeToExplain:
     if chinese == True:
          if car_caught == True:
               if persistent_fleeingDeaths_counter_knowledge == 0:
                    n "You run through the exit of the restaurant and brace yourself for the impact of a speeding car."
                    n "Nothing happens, the police indeed managed to take care of the drunk driver."
               else: 
                    n "You run through the exit of the restaurant, knowing full well that the red Sedan has been dealt with."
               n "[persistent.date] and you continue to run as if death itself is chasing you."
               n "[persistent.date] is still very confused but she can feel the fear that is running through your body and she fears whatever made you so scared to begin with."
               
               if persistent_fleeingDeaths_counter_knowledge == 0:
                    n "As you are running along the side of an empty street you suddenly hear the screeching of wheels and loud laughter."
                    n "As you look behind you you see a bus full with elderly people coming straight towards you and her, you manage to jump away from it just as it would've hit you but [persistent.date] ofcourse doesn't."
                    n "You know what you have to do, you've come too far to just give up now."
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu: 
                         "I retry.":
                              jump explanation_noTimeToExplain

               if 0 < persistent_fleeingDeaths_counter_knowledge < 3:
                    n "This time you manage to push [persistent.date] away just as she would get hit by the bus, you both make it out alive and well."
                    n "When she gets back up you both continue running, as if you were trying to escape fate."
                    
               if persistent_fleeingDeaths_counter_knowledge == 1:
                    
                    n "Just moments after the first death you prevented you can see a truck coming towards you at full speed. The truck crashes straight into [persistent.date] and she doesn't make it once again."
                    n "You curse at the skies, trying to reach the one responsible for [persistent.date]'s countless deaths himself."
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu: 
                         "I retry.":
                              jump explanation_noTimeToExplain
           

               if persistent_fleeingDeaths_counter_knowledge == 2:
                    n "This time you manage to warn [persistent.date] beforehand of the truck and she makes it out alive, you've done these things so many times it almost just seems like you're back in an instant, time is blending together."
                    n "[persistent.date] and you continue running untill you hear the sound of thunder, lightening strikes closer to [persistent.date_sis] then you like but she seems to escape unharmed."
                    n "That's when you notice oil leaking from the crashed truck, it's set ablaze by the lightening."
                    n "The fire tries to consume her, the hungry flames don't let off until she is beyond saving."
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu:
                         "I retry once again.":
                              jump explanation_noTimeToExplain
               if persistent_fleeingDeaths_counter_knowledge == 3:
                    n "You lead [persistent.date] to a diverging street where the oil, the truck, and the elderly people shouldn't be a problem."
                    n "As [persistent.date] and you are running once again you can feel a terrible trembling coming from the ground."
                    n "It almost resembles an earthquake, but not quite."
                    if persistent.kokiri_death_4 == True:
                         n "It actually kind of reminds you of what you felt when the ufo revealed itself in the kokiri forest."
                    n "It also doesn't last as long as the earthquakes usually do, you feel thankful when the earth stops trembling and [persistent.date] is still left unharmed."
                    n "However, you thought she was safe too soon and a safety hazard of a building that shouldn't have  been built in the first place collapses in on her."
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu:
                         "Retry. Retry. Retry.":
                              jump explanation_noTimeToExplain
               if persistent_fleeingDeaths_counter_knowledge == 4:
                    n "This time [persistent.date] and you make it to your car which was parked a few streets away from the restaurant, you decided that it would be the best plan to just get away from this village as fast as you can."
                    n "As you are driving away from the village you finally arrive at a bigger city, maybe [persistent.date] and you will be safe here?"
                    n "You look at [persistent.date] for a moment, just hoping that death will have mercy on her."
                    n "Suddenly you hear a cacophony of animal sounds, as you look in the side mirrors of your car you can see a swarm of animals running towards your direction."
                    n "You try to go as fast as you can but then you realize something."
                    n "You forgot to fill up your car, just as you realize that it abruptly stops, you try to persuade the car into going a tad further but your efforts are futile."
                    n "The animals run on top of your car, now this isn't a problem except that there were also elephants among those animals."
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu: 
                         "Sigh, retry.":
                              jump explanation_noTimeToExplain

               if 4 < persistent_fleeingDeaths_counter_knowledge:
                    n "Now you've made sure to gas up your car for the inevitable chase scene."
                    n "You reached your car once again without any issues so far."

               if persistent_fleeingDeaths_counter_knowledge == 5:
                    
                    n "As you are driving away as fast as you can from the animals, more buildings start to collapse, now even the sturdier looking ones are doing so."
                    n "These scenarios are becoming more and more unjustified, you shake your head and try to focus on getting [persistent.date] alive and well out of this mess."
                    l "Listen, I really don't think we are safe here. Even if we make it out of this city, where are we going to go then?"
                    l "It's not like we can just leave this planet so death will always follow me."
                    n "[persistent.date] has given you the greatest idea, you give her a kiss on the lips and tell her she is genious."
                    n "[persistent.date] turns beetred."
                    l "Oh I wouldn't know about that..." 
                    l "But hang on, you are not seriously thinking about leaving this planet, right?"
                    l "How would we even be able to do that?"
                    n "You stop the car for a moment, waiting for death to cath up with both of you, and it sure does so fast."
                    n "Another car, trying to escape the commotion, notices you too late and drives right into your car from the front."
                    n "You already know that Lilith did not surivive even without checking."
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu: 
                         "Retry, this could be it!":
                              jump explanation_noTimeToExplain

               if persistent_fleeingDeaths_counter_knowledge > 5:
                    n "This time you don't leave the village, instead you remember the ufo that is hidden in Kokiri forest. Maybe you could use it to escape."
                    n "Eventually you find it, [persistent.date] and you climb inside it."

               if persistent_fleeingDeaths_counter_knowledge == 6:
                    n "However, an onslaught of buttons, levers and contraptions you can't identify await you."
                    n "It seems that it is going to take some time to learn what the controls are before you'll be able to get out of here."
                    
                    menu: 
                         "I'll retry untill I get it right!":
                              n "After about a hundred or so attempts you manage to take of with the spaceship without plummeting to your death instantly."
                              $ persistent_fleeingDeaths_counter_knowledge += 1
                              jump explanation_noTimeToExplain
               if persistent_fleeingDeaths_counter_knowledge > 6:
                    n "As [persistent.date] and you take of into space you can see the sun absorbing the earth, you know that that should've happened like a million or so years later but it happened now. These deaths are really getting out of hand aren't they?"
               
               if persistent_fleeingDeaths_counter_knowledge == 7:
                    
                    n "Suddenly you are hit by a speeding ufo. Your ship analyses the situation and informs you that the driver was drunk."
                    n "It seems that even in space there are drunk drivers."
                    menu:
                         "Retry. Retry. Retry and retry once again.":
                              $ persistent_fleeingDeaths_counter_knowledge += 1
                              jump explanation_noTimeToExplain
               if persistent_fleeingDeaths_counter_knowledge == 8:
                    n "Everything starts to blend together even more, sometimes you're not even sure if you are actually progressing in the story or not."
                    n "Death by colliding stars."
                    
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu:
                         "Retry.":
                              jump explanation_noTimeToExplain
               if persistent_fleeingDeaths_counter_knowledge == 9:
                    n "Death by a storm of asteroïds."
                    
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu:
                         "Retry.":
                              jump explanation_noTimeToExplain
               if persistent_fleeingDeaths_counter_knowledge == 10:
                    n "Death by crashlanding on a planet."
                    $ persistent_fleeingDeaths_counter_knowledge += 1
                    menu: 
                         "Retry.":
                              jump explanation_noTimeToExplain
               if persistent_fleeingDeaths_counter_knowledge > 10:
                    n "The universe grows calm for a moment, it seems like you got through the constant barrage of deaths." #These three lines only trigger in the quest version if "Starttalk" is not set, I'm not sure what that is anymore.
                    n "You set the ship on auto-pilot and move away from the controls."
                    n "[persistent.date] is standing there, she seems to be quite scared but is taking it pretty well all things considered."
                    menu:
                         "*Talk with [persistent.date]*":
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
                                                  n "[persistent.date] laughs."
                                                  l "It's a shame I don't remember anything of it though..."
                                                  l "What was your favourite first date?"
                                                  menu:
                                                       "My favourite part was the beach.":
                                                            $ persistent.favouriteFirstDate = "beach"
                                                            jump ufo_talk_favouriteFirstDate
               
                                                       "My favourite part was the burger restaurant.":
                                                            $ persistent.favouriteFirstDate = "burger"
                                                            jump ufo_talk_favouriteFirstDate
               
                                                       "My favourite part was the cafe.":
                                                            $ persistent.favouriteFirstDate = "cafe"
                                                            jump ufo_talk_favouriteFirstDate
               
                                                       "My favourite part was the Chinese restaurant.":
                                                            $ persistent.favouriteFirstDate = "chinese"
                                                            jump ufo_talk_favouriteFirstDate
               
                                                       "My favourite part was the Kokiri forest.":
                                                            $ persistent.favouriteFirstDate = "kokiri"
                                                            jump ufo_talk_favouriteFirstDate
          else:
               jump explanation_noTimeToExplain_hitByCar
     else:
         
          label explanation_noTimeToExplain_hitByCar:
               n "As Lilith and you run out of the [resname] together you spot something that makes your stomach drop."
               n "You see a red Sedan."
               n "Not just any red Sedan, the one you wish you could never see again."
               n "And yet, here it is again."
               if car_free:
                    n "It seems your efforts of trying to call the police lead to nothing, maybe you should have sent them to a different place?"
               elif car_caught:
                    n "It seems like the police hadn't been able to arrest the driver yet, maybe you should try to go to a different place?"
               else:
                    n "You are not sure why you are surprised, you knew that this was very likely to happen if you didn't get rid of it somehow."
                    n "But how are you going to manage that?"
                    if not persistent.kokiri_death_2_call or persistent.kokiri_death_2_alternate or persistent.kokiri_death_2:
                         n "You try to think of an idea but can't really come up with anything."
                         n "Maybe later you will be able to think of something good?"
                    else:
                         n "Maybe it's time to try to call the cops like you've been thinking about before."
               n "All those thoughts in your mind are trying their best to obfuscate the worst one."
               n "An image of the aftermath that is about to happen."
               n "You try to ignore it, try to change it, by attempting to push Lilith aside as fast as you can."
               n "But no matter how hard your mind tries to fight it, your body is frozen in place."
               n "Your mind is flooded with thoughts that all somehow overlap, you can't make much sense of any of them. Most of them are cries for you to save her, for anyone to save her somehow."
               n "But as you get flung aside somehow by the car, you already know what happened to her."
               n "No one could save her this time."
               n "The horrible aftermath you tried so hard to avoid has caught up with you once again."
               jump gameOver

label ufo_talk_favouriteFirstDate:
     if persistent.favouriteFirstDate == "beach":
          l "Great minds think alike I suppose [persisistent.name], I love the beach a lot aswell."
          l "There's so much variety in the things you can do there."
          l "And what was your favourite moment of that particular date [persistent.name]?"
     elif persistent.favouriteFirstDate == "burger":
          l "I knew you would love it there! Rose's burgers are just unbeatable when it comes to their amazing taste."
          l "Just thinking about it now makes me really yearn for a juicy cheeseburger."
          n "You can hear [persistent.date]'s stomach growl as she quickly places a hand on it as to quiet it down."
          n "She turns beetred."
          l "Uhm anyway, what was your favourite moment of that particular date [persistent.name]?"
     elif persistent.favouriteFirstDate == "cafe":
          n "You tell her about how beautiful the aquarium inside the cafe is."
          l "Oh wow, that sounds absolutely wonderful!"
          l "I'm having a hard time imagining what it looks like though, I wish I could see it for myself."
          l "Well, I suppose I did, didn't I?"
          l "I just wish I could remember it, that I could remember all of our dates together."
          l "And what was your favourite moment of that particular date [persistent.name]?"
     elif persistent.favouriteFirstDate == "chinese":
          l "That was your favourite? That's nice to hear, I'm glad I got to experience it for myself aswell in that case."
          l "Even though this date surely didn't go as planned."
          l "Though I can imagine your favourite date there isn't this one, because we hardly spent any time in the chinese restaurant itself now."
          l "What made that date specifically your favourite [persistent.name]? Maybe we can still one-up it."
          n "Lilith gives you a cute little smile."
          l "I'd like that."

     elif persistent.favouriteFirstDate == "kokiri":
          l "I still can't even believe that we went there. It's a lovely place for a date, but I never thought I would share that with anyone."
          l "Those woods are very special to me after all."
          if love_meter >=2 :
               n "She thinks to herself for a brief moment."
               l "But then again, if I have to share it with anyyone, I'm happy it got to be you."
          l "What was your favourite part of the date we had there [persistent.name]?"
          
     
     $ renpy.input("My favourite moment was...")
     l "That sounds really lovely [persistent.name]!"
     $ renpy.input("")
     l "That sounds great!"
     $ renpy.input("")
     l "..."
     $ renpy.input("")
     l "..."
     n "[persistent.date] is staring right into your soul without saying a word."
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
     n "Just then you hear something. Not [persistent.date], it's a loud beeping sound coming from the metal ship itself."
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
     n "On [persistent.date]"
     n "The thought of [persistent.date] takes you out of this confused state of mind in an instant."
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
          "Yes, you must be [persistent.date_ghost]. [persistent.date] told me about you before.":
               $ persistent.met_james = True
               j "Ah, I thought she would mention me eventually."
               j "I'd imagine it would be pretty hard to get this far while never having heard about me."
               j "After all, it's hard for her to fully deal with what happened."
               j "I understand completely but I had hoped everyone would have moved on more easily."
               j "Then again, I shouldn't be saying that, after all I'm still here even when I could have moved on years ago."
               n "It's quiet for a moment, you hear nothing except a low droning sound."
               j "[persistent.date_ghost] gives you a curious look, you're not quite sure why but you feel slightly unsettled."
               j "What are your thoughts  on [persistent.date] [persistent.name]?"
               n "You are pretty surprised by that question."
               menu:
                    "I really love her.":
                         $ loveher = True
                         $ persistent_jamestalk_iloveher_knowledge = True
                         j "If that's the case then this talk might be easier then I thought."
                         j "You have seen [persistent.date] die about [persistent.lildeaths] times, right?"
                         n "You nod, you can still remember all the times she died."
                         n "That doesn't stop you from wishing you could forget though."
                         j "And you are trying to keep her safe so that she will not die, right?"
                         n "You nod."
                         if persistent.lilithAliveAndRetriedCounter >= 1:
                              j "And yet you came back after she didn't die, why?"
                              jump jamesChat_whyDidYouReturn
                         else:
                              j "That's very good of you [persistent.name], thank you for that."
                              j "I'm just a bit worried about what will happen once you find out that the cases where she lives are... far from statisfying for you."
                              j "If she lives the two of you pretty much never end up together."
                              j "And that is why you started playing this game in the first place isn't it?"
                              j "To find an ending where the two of you live happily ever after?"
                              j "Well, what happens if you won't find an ending like that?"
                              j "If every ending even resembling something like that will feel... off."
                              j "I fear you might drive yourself mad trying to look for something that only ever truly can exist in your mind."
                              j "Can you promise me that if you find an ending where she lives, you won't come back again?"
                              j "That you won't put her through any more death and stress than is truly necessary?"
                              menu:
                                   "I promise James.":
                                        j "Thank you, [persistent.name]."
                                        j "Even if it’s just words right now, it gives me a little bit of hope that you’ll actually keep it."
                                        j "You see, I’ve been here long enough to know how rare that promise is. And how even rarer it is to see it kept."
                                        n "James looks away for a moment, his expression softening."
                                        j "All I want is for her to be safe and happy. If you can give her that, then maybe my time here won’t have been in vain."
                                        n "The atmosphere feels heavy as James looks back at you, his eyes filled with both hope and uncertainty."
                                        j "Just remember, if you truly care about her, sometimes the best thing you can do is let her go."
                                        j "She’s been through enough, and so have I. Please don’t make her suffer more than she already has."
                                        j "Thank you for hearing me out, [persistent.name]. That’s all I can ask of you right now."
                                        
                                   "I'll try, but I can't promise anything.":
                                        j "I know."
                                        j "I guess I just asked to maybe be comforted by an empty promise for a second."
                                        j "The truth is, that this very promise was broken many times by others like you."
                                        n "James waves with his hand in the direction of the bubbles that seem to contain other worls inside of them, hundreds of them flash for a second."
                                        j "In all of those worlds, that promise I was hoping for was made. And in all of those, that very same promise was broken."
                                        j "So wheter or not you promise it, the truth is it doesn't really matter."
                                        j "I just hope that you are different."
                                        j "That you'll know when to let go."
   
                    "I really like her.":
                         $ likeher = True
                         j "Let me ask you this: if you like her, do you believe that what you're doing is truly for her sake?"
                         n "The question catches you off guard, and you hesitate."
                         j "Because liking someone means you want the best for them, right? It means you’d do anything to make sure they’re happy, even if it means stepping away."
                         j "But here you are, putting her through pain, stress, and countless deaths. So let me ask you again: is this really about her? Or is it about you?"
                         n "You feel a pang of guilt as James' words cut through your thoughts."
                         j "I'm not saying this to make you feel bad, [persistent.name]. I just want you to think about it."
                         j "Because if you can't see this through for the right reasons, then maybe you shouldn't see it through at all."
                         
                         $ persistent_jamestalk_ilikeher_knowledge = True
                         #TODO: Add more text for this
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
                         j "The only way to break it would be to enter the Darkness but I'm not ready for that yet, I need to know that [persistent.date] is happy and safe."
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
                    j "Don't you think you are being unfair to [persistent.date]? Don't you think she has the right to die only once?"
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
                  
                    $ fritfood = 0
                    $ changeableWord == "Like"
                    if persistent.ending_breakup == True:
                         $ fritfood += 1
                         
                         
                              
                         j "[changeableWord] not going on your date. That way [persistent.date] met Ron and they were happy together, even had some kids."

                         if fritfood >= 1:
                              $ changeableWord == "Or"

                    if persistent.ending_abigailDistraction == True:
                         $ fritfood += 1
                         j "[changeableWord] letting [persistent.date_sis_nickname] distract her so she would be safe."
                         if fritfood >= 1:
                              $ changeableWord == "Or"

                    if persistent.ending_badDate == True:
                         $ fritfood += 1
                         j "[changeableWord] when she had a bad date with you but she did live because you made sure that it was safe for her to leave."
                         if fritfood >= 1:
                              $ changeableWord == "Or"

                    if peristent.times_phone_declined > 0:
                         $ fritfood += 1
                         j "[changeableWord] when you didn't pick up the phone at all, ensuring her safety."
                         if fritfood >= 1:
                              $ changeableWord == "Or"

                    if lilithAliveAndRetriedCounter > 0:
                         j "When this entire ordeal finally settled down..."
                         j "You didn't have to retry."
                         j "You didn't have to cause her to go through the bad things once again after you were even told that she was safe and secure."
                         j "You see, you do not undo your actions each time you retry, each time you save [persistent.date] once more or don't."
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
                              $ persistent.polaroid_reachEndingMotive = "us"
                              
                              
                         "For myself.":
                              $ persistent.polaroid_reachEndingMotive = "me"
                              
                         "For her.":
                              $ persistent.polaroid_reachEndingMotive = "her"
                              

                              $ fritfood = 0
                              if persistent.kokiri_reachEndingForMe:
                                   $ fritfood += 1
                              if persistent.kokiri_reachEndingForUs:
                                   $ fritfood += 1
                              if persistent.kokiri_reachEndingForYou:
                                   $ fritfood += 1
                              if persistent.kokiri_reachEndingRecent == persistent.polaroid_reachEndingMotive:
                                   
                                   if fritfood == 1:
                                        j "That indeed seems to be true, you told Lilly the same thing in the kokiri forest."
                                   elif fritfood == 2:
                                        j "Last time you indeed said the same thing to Lilly, but before that you something else, didn't you?"
                                        if persistent.kokiri_reachEndingRecent != "me":
                                             n "James seems to notice a certain look on your face and is quick to react."
                                             j "Don't worry about that. Changing your mind is perfectly normal, if anything I'm glad that you did and seem to be sticking with your choice."
                                   elif fritfood == 3:
                                        j "Are you sure? You practically answered every possible way on that question when Lilly asked it."
                                        j "Although it seems you are sticking with your last choice."
                                        if persistent.kokiri_reachEndingRecent == "me":
                                             j "Though remember, it's never too late to still change your choice."
                                             j "You've done so plenty of times, so you can still go back to the better... uhm I mean previous ones."
                                             
                                   
                                       
                              else:
                                   j "Are you lying to me? That is not what you told her the last time she asked you that question, is it?"
                                   if fritfood == 1:
                                        j "Or did you just change your mind?"
                                   else: 
                                        j "Or did you change your mind again?"
                                        if fritfood == 3: 
                                             j "You seem to be quite indecisive, don't you?"
                                             j "Or did you just want to explore all the different reactions she would give based on your answers?"
                                   if persistent.kokiri_reachEndingRecent != "me":
                                        j "There's always the possibility that you're lying right now but she can uses all the comfort she can get. So I'll believe you, for her sake."   
                              
                              if persistent.polaroid_reachEndingMotive == "me":
                                   j "So even though you do like her you still just want to reach the ending you are seeking for yourself?"
                                   j "I have to say that surprises me. It was not what I was hoping to hear."
                                   j "But I can't blame you, because I suppose even if you like her as a character, she still is just that to you isn't she? A character in a game."
                                   j "One you can just subject to death after death without guilt to find the perfect little ending for yourself."
                                   j "I understand, but that doesn't make me any less dissapointed [persistent.name]."
                                   j "I really thought you understood for a moment, that you understood her life is in your hands."
                                   j "But I guess that doesn't matter that much, does it? Because you can just distance yourself from the consequences of your actions and pretend like none of it happened."
                                   j "You can just pretend like what you want will be worth all the suffering it brings to a character you specifically said you liked."
                                   j "I wonder, would you do the same thing in the real world if you thought there were no consequences for you actions? If you could distance yourself far enough from those consequences atleast."
                                   j "Would you also hurt the people you like in that case? Is all that holds you back the distinction of what is real and what isn't real? The idea that the consequences can't reach you?"
                                   j "This is real to us [persistent.name], isnt that enough for you?"
                                   j "I'm begging you, if you even remotely like her, please stop hurting her."
                                   j "It's not worth it, what you are looking for is unattainable here."
                                   j "Can't you see? You've gone through all of this and the game still hasn't given you what you want. That's because it can't."

                              elif persistent.polaroid_reachEndingMotive == "us":
                                   "Filler"
                              elif persistent.polaroid_reachEndingMotive == "her":
                                   j "Is it really for her?"
                                   j "She was fine without you, wasn't she?"
                                   j "Don't get me wrong [persistent.name], she seems to like you. But she doesn't need to end up with you to be happy."
                                   if persistent.ending_breakup == True:
                                        j "You have seen that for yourself, haven't you?"
                                   j "My fear is that you might need her for that though."
                                   j "Is that why you want to find an ending where the both of you end up with eachother?"
                                   j "I understand that it can be very hard to let go, precisely because I have the same problem."
                                   j "But it is important to truly think this through."
                                   j "If you really want what is best for her, do you think subjecting her to death after death in the search of a hypotetical ending is worth it?"
                                   j "There are better ways to achieve your goal."
                                   j "I sadly can't just tell you, since that isn't allowed by Him."
                                   j "But trust me, you won't find the ending you are seeking by just going through every path in this game."
                                   j "Every road you walk with her just leads to death."
                         
                                        
                            
   
          "I wanted to see what other endings there are.":
               j "I see..."
               j "I will spare your time then, there are no endings here that I am aware of."
               j "In all this time I've spent here I've never seen one."
               menu:
                    "I do not trust you.":
                         if justgame == True:
                              j "I see, you think I'm defending [persistent.date] by lying about it?"
                              j "Well, maybe I am or maybe I am not."
                              j "In the first case I am so desperate to not let you destroy her once again that I am lying to your face and in the other case there is truly no other ending here."
                              j "In both options it would be wise to reconsider before you move further towards a path you wouldn't like, right?"
                              j "You might not have had much consequences for your actions yet, but let me assure you."
                              j "There is no such thing as no consequences..."
                              if (persistent.major_love_offence_counter + persistent.minor_love_offence_counter) > (5 + persistent.major_love_comfort_counter + persistent.minor_love_comfort_counter):    
                                   j "And if you keep treating [persistent.date_nickname] badly I might need to help teach you that lesson."
                                   n "[persistent.date_ghost] gives you a bonechilling look that makes you think you would not like being educated by him. At all."
                              else:
                                   j "Let's hope for the both of us that you act wisely so you have to experience as few of them as possible."
                                   j "After all, ignorance is bliss isn't it [persistent.name]?"
                                   n "He spoke those last words with some noticeable disdain. You are not entirely sure why."
                              j "My energy is running low from this talk, so I'll have to take some rest. In the meantime I'll send you back."
                              j "Goodbye [persistent.name]. Do not come back here."
                              jump Game_start2
    
                         else:
                              j "Oh [persistent.name], why don't you trust me? We both care for [persistent.date] right? So you can rest assured that I only want the best for her."
                              menu:
                                   "How do you know what is the best for her?":
                                        j "Look, can we not do this?"
                                        j "You have seen endings where she lived, and yet you came back."
                                        j "Maybe I don't have the right to decide what's best for her, but what gives you the right to decide that the endings where she lived weren't good enough?"
                                        if (persistent.major_love_offence_counter + persistent.minor_love_offence_counter) > (5 + persistent.major_love_comfort_counter + persistent.minor_love_comfort_counter):    
                                             j "Especially if you are just going to treat her badly when you are together with her, what is the point of that?"
                                             j "Did you have to take away her good endings just so you could torment her more?"
                                             j "Are you just saying you are looking for other endings as an excuse?"
                                             j "Do you even truly want this to end?"
                                             j "Or are you always going to be searching for one more ending, no matter what you find?"
                                             j "Well [persistent.name], let these be my last words for now, your search will be unfulfilling and meaningless, no matter what you find."
                                             j "Because it will never be enough for you."
                                             j "I guess that's a fitting curse though, so I'll let you go on your merry way back."
                                             jump Game_start2
                                        else:
                                             j "Your intentions seem pure though, albeit quite naïve."
                                             j "At the very least I guess it could have been worse. She can die with someone she trusts now."
                                             j "Although I would prefer if you didn't have to keep looping. You are playing a game with rules that you can't win."
                                             j "Attempting to over and over again is only going to create more death, to slowly hollow out any purpose you had for trying again in the first place."
                                             j "I like you well enough, so I'll tell you this secret I picked up from watching over all these different realities."
                                             j "What do you do when you don't like the way a story goes?"
                                             j "That's the most I can tell you I'm afraid, I'm not really allowed to spell it out for you too much."
                                             j "Now I'm going to have to send you back, just talking to you like this costs me a lot of energy."
                                             j "Goodbye [persistent.name], I hope my tip will help you out."
                                             jump Game_start2


                                   "I guess we are indeed on the same page. I'll take your word on there being no other endings here.":
                                        j "Thank you [persistent.name], that means a lot to me."
                                        j "Besides, I think you have already found the best endings you possibly could find, even if you may not know it yet."
                                       
                                        $ persistent.ringRiddle_knowledge = True
                                        j "After all, how many ends does a ring have?"
                                        menu:
                                             "None, there is no begining and there is no end.":
                                                  jump jamesChat_whyDidYouReturn_ringResponse

                                             "One, right when it loops back to the begining.":
                                                  jump jamesChat_whyDidYouReturn_ringResponse

                                             "An infinite amount of them. It just depends how you look at the ring.":
                                                  jump jamesChat_whyDidYouReturn_ringResponse

                                        #Write some more text here.
                              #TODO: Continue writing this text, maybe add some slight variations if the player treated [persistent.date] badly.
                    "You can't just bombard me with so much info and then just move on like I should understand, can you please atleast explain something clearly?":
                         #TODO: niet zeker of dit nog juist staat.
                         j "I see..."
                         j "I guess that indeed was a bit too much info for you to handle."
                         j "I will let you ask me one question about what I just said, then you have to answer my previous question."
                         menu:
                              "Filler":
                                   "Filler"
                                   #TODO: Fill the menu in with some questions they can ask.
                                   #After it has been answered let [persistent.date_ghost] reask the question.
                    "Thanks for telling me. I just had to be sure, this seems like a place where the developer would be able to hide some stuff.":
                         j "I can see why you would think that [persistent.name], but I haven't seen anything here that would lead to an ending."
                         j "Although I suppose that it depends on what you see as endings."
                         j "The thing about a loop is that we can sometimes be tricked into thinking there are no endings, because it never ends."
                         j "But in a way you encounter many endings you wouldn't think to call endings, don't you?"
                         j "Because I like you I'll clue you into something, those endings I'm talking about you won't be able to find here."
                         j "Best of luck [persistent.name]."
label jamesChat_whyDidYouReturn_ringResponse:
     j "I'm afraid I can't give you the answer [persistent.name], He doesn't like that."
     j "But I did give you the question, perhaps a topic to talk about to Lilith if you would like to discuss it more?"
     n "He gives you a slight wink."
     j "I hope that helps, in any case, I'm going to have to send you back now. I don't have enough energy to keep up this conversation."
     jump Game_start2
                                             
                                             
                                       
     
    
                   
    
          
label jamesChat_whyDidYouReturn_toBeTogether_choices:
     menu:
          "Who are they?":
               j "The first one you probably haven't met, not for long anyway. He is the one that created this world, gave you acces to it and made the second one.
               The second one you might know actually, the jester that controls the flow and direction of our story. He even controls the deaths [persistent.date] suffered and yet you rely on him to fight him, that might be his biggest joke yet."
               menu:
                    "Alright mister purple prose. So the \"they\" you were talking about are the game developer and the narrator?":
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
     #TODO:A way to more easily loredump and talk about aspects that [persistent.date] can't remember/ alternate realities. Add some more loredumps and in character questions.
     menu:
          "What is this place?":
               j "Although I guess it didn't start out as a place you might consider it as one now."
               j "Where we are right now is essentially right before the end. Before the end of everything as we know it."
               j "We call that end the Void. Every soul of every person that dies is supposed to enter the Void."
               j "It is essentially a gateway to other worlds, but if you enter it you yourself become changed. The Void compacts your entire being and can alter anything it would like for whatever purpose it has in mind."
               j "So chances are you won't ever be aware of who you were before entering the Void when you leave it."
               j "That is what so many people are scared about, of losing themselves and the other people they left behind."
               j "A lot of those people that have fears about entering the Void try to despereately cling onto this world."
               j "But the longer you cling to this world the less human you start becoming. After a while you turn into one of those."
               n "James points to something in the distance. When you try to see what it is your eyes fall on a tree with a thousand branches that seemingly pulsates."
               j "Their roots make it easier for other souls to stay here aswell, they get caught on those roots and then before long their own roots grow around the other roots."
               j "So this place is essentially a manifestation of not being able to let go."
               menu: 
                    "And what where those polaroids I had to jump on to reach you all about?":
                         j "Those where a manifestation of yours I fear."
                         j "Handy to reach me but that means you are also starting to settle into this place."
                         j "Let us hope that you won't stay long."

          "What are those bubbles?":
               j "Ah, yes. I thought you would ask about them."
               j "They are the way we as lingering souls can see the world outside of here."
               j "Each bubble shows a choice made out there. Some choices that could have been made but never were, some choices that yet have to happen and some choices that are happening right now."
               j "You could probably label each bubble as a sort of alternate world. You have the power to cross those different worlds and to maintain your memories of them."
               j "Since this is a game where everyone has an expected way to act on every action that means that every world is almost exactly the same except for the choices you make and the reactions that come from those."
               j "So all these choices, both made in the past, never made, and yet to be made are yours."
               n "Looking at the bubbles a few catch your eye."
               n "The first one depicts Lilith and you sitting in the burger restaurant, but at a different table than the one where she got shot."
               n "The second bubble shows you Lilith getting up from the table at the chinese restaurant and you running after her pleading for her to stop. The red Sedan never shows up and she leaves you standing at the exit."
               n "The third one shows you in the cafe, peeking at the dice Lilith rolled using the reflection of the aquarium."
               n "The next bubble shows you in the ufo in kokiri forest, alone, with Lilith nowhere in sight."
               n "The last bubble shows you popping a full blob of mayo straigth into your mouth at a fritstore near the beach."
               $ persistent.mayoProphecy_knowledge = True
          "No matter what I try [persistent.date] keeps dying when I go on a date with her.":
               if persistent.lilithAliveAndRetriedCounter > 0:
                    j "That is the thing, isn't it [persistent.name]?"
                    j "She seems to keep dying when you go on dates with her."
                    j "But we both know that there are endings where she lives, just not where the two of you live together or anything like that."
                    j "I have overlooked many many possibilities, many different choices and I don't think I have found what you are looking for."
                    j "Maybe you are looking for the wrong thing. After all, anything perfect is never handed to you just like that, if something perfect even exists in the first place."
                    j "I doubt that the game will just hand you an ending like that. Would it even feel like you earned it if it did?"
                    j "With how hard you've been searching up to this point I doubt any ending the game can give you will be enough to satisfy you."
                    j "So isn't it perhaps better to just call it quits from here?"
                    j "Or maybe you should look elsewhere instead?"
                    n "He pauses for a moment after saying that. He gives you a curious look, seemingly trying to gage your reaction to what he just said."
               else: 
                    j "I see..."
                    j "That does indeed seem to be the case doesn't it?"
                    j "Every interaction with her just seems to lead to death."
                    j "And yet..."
                    j "I know there is more out there."
                    j "Ways for her to live."
                    j "Though I think you might not like how you reach them or even what they are in general."
                    j "I even think with some of them, you might not even know wheter or not you found them."
                    menu:
                         "But that's ridiculous! Ofcourse I would know if I found an ending like that.":
                              j "Well, do you recall finding an ending like that?"
                              n "You shake your head."
                              j "That might just prove my point. Or it might not. Who knows?"
                              j "I know you must think I'm being a little annoying at the very least right now, but trust me, I am trying to help."
                              j "I just have to balance between being too vague and too clear at the same time."
                              j "You aren't the only one reading this afterall."
                              menu:
                                   "What are you talking about?":
                                        j "I see..."
                                        j "So I was too vague..."
                                        j "What I mean is, that we are merely visitors in this house. "
                                        j "And the host is very well aware that we are talking about the meaning behind his interior design."
                                        j "He does not like that."
                                        j "But don't worry, he does not like that because it has to stay hidden."
                                        j "He doesn't like it because he hopes the clues he planted around the house will be enough for you to figure it out."
                                        j "And yet, a lot of these sorts of things lead to multiple possible interpretations, don't they?"
                                        j "So I wonder what your take will be when you leave his house."

                                   "Are you talking about the other souls here?":
                                        j "I am not."
                                        j "To them this would not be reading, this would be something more like listening."
                                        j "Hearing the words spoken by an imaginary actor rather than reading them of the script."
                                        j "But these souls can listen all they want for all I care."
                                        j "Even if they were listening, I doubt they would care."

                                   "Are you talking about the narrator?":
                                        j "A good guess!"
                                        j "But no, he does not care that much wheter I reveal any secrets to you."
                                        j "He can not care in fact. For as much as he pretends to read the script, he is the script."
                                        j "Now his boss? That's a different story, he wrote the script. And he very much cares that certain things aren't spoiled too soon."
                                        j "To not lose their... meaning."

                                   "Are you talking about the creator?":
                                        j "It seems like I was clear enough for you after all."
                                        j "I'm glad you understood!"
                                        j "He does not really like me or anyone for that matter giving away things too much."
                                        j "We can only ever allude to them, but never speak of them until someone else at another time and place can directly adress those things."
                                        j "And even then there still has to be some subtext."
                                        j "I guess He wants you to think about those things for yourself, to not just take what the game says at face value."
                                        j "A bit pretentious if you ask me, but I suppose creators like acting as if their work is deeper then it is sometimes."
                                        j "Maybe that's why He wants you to think about these concepts for yourself?"
                                        j "So you can come up with a better interpretation than He ever could and He only has to nod His head and say that that was always what was intended."
                                        j "Funny isn't it? To this world He and the narrator might almost seem like Gods. And yet, this world, this specific instance of it, would not exist if you weren't here to observe it."
                                        j "What would happen if you stopped observing this specific instance of our world? Would it cease to be? Would it continue as planned? Or would it go a different way?"
                                        j "Either way, in a way, you blew life into the world He created. Without you it would be dormant. Something, unobserved to the point of becoming practically nothing."
                                        j "I wonder, what does that make you?..."
                                        j "A believer giving them the strength they require to call this world their own? Or a God in your own right?"
                                        j "I think they would like you to believe you are the first."
                                        j "I'm not so sure myself..."
                                        j "But neither of our thoughts about that matter do they? Yours do."
                                        j "So please [persistent.name], don't forget your own role in this story, the perks it can bring."
                                        j "Because I think it is more important than you might think."
                                        
     j "I have exhausted most of my energy having this conversation with you. If you want to talk about other things next time you know how to find me don't you?"
     j "I'll send you back now, good luck [persistent.name]."
     jump Game_start2

return


label LilithOrJames:
    
     n "You are floating in a seemingly endless tunnel of darkness."
     n "After what feels like hours the tunnel seperates into two smaller tunnels, at the end of each you see a scene that is simmilar in many ways and yet is also slightly different."
     n "The left tunnel ends on a vision of you sitting together in some sort of restaurant with a (description of Lilith), you get the strange feeling you know her name, it's Lilith."
     n "The right tunnel ends on a vision of you sitting together in some sort of restaurant with a (description of James), you get the strange feeling you know his name, it's James."
     n "Choose which path you want to walk player, left or right? Lilith or James?"

label ufoVisitAlone:
   
 
     $ persistent.anomaly_knowledge = True # previously called "Readshiplog")
     menu:
          "Computer, what is the temporal anomaly?":
               ship "A temporal anomaly has been picked up accidentally by our quantum computers when we connected all our Neya-infused computers in identical parallel universes in an effort to create even more advanced computers."

               ship "The universes we are connected with are exactly the same as this one except for one thing, the anomaly."
               ship "It manifests itself on a specific day in each and every universe, always on that same day."
               ship "Around the anomaly a lot more accidents tend to happen, more than explainable by our curent science, our curent hypothesis is that the universes the anomaly resides in want to purge themselves of It."

               ship "Unfortunatly the universes measures are quite... drastic and put all our lives in danger aswell."

               ship "We tried to give these universes a hand by killing the anomaly but that wielded a further and even faster spread to other universes."

               ship "At a certain point it grew so rapid we couldn't take care of it anymore, we lost connection with a few billon of this ship that time, probably lost in the crossfire of the universes."

               ship "That's when it happened, a terified version of us accidentaly misfired and shot Her instead of the anomaly. At that moment the anomaly stopped in that universe. We found this peculiar so we looked more into it."

               ship "It also took the anomaly longer to wreak havoc upon other universes. We were unsure about the relation between Her and the anomaly but after a few extra tests we noticed a clear corelation between Her dying and the delay, even dissapearance of some of the anomalies."

               ship "She must be the key to stop the anomaly from crossing over, she must be, or all hope is lost..."

               ship "We would tell you where you would find both of them but due to how the anomaly works it isn't always set to be in the same place, rather a few possible places.<br/>If they go to any of the three restaurants they will visit you do not need to intervene, the universe will take care of it in a acceptable way with a small amount of death.<br/>However, if they go to either the forest or the beach you need to keep a close eye on them, if she hasn't died by (hour here) then you will need to intervene, otherwise our fates will look quite gruesome, let me asure you."
                     
label reunionEnding:
     #TODO: This has nothing jumping to it. Fix that, so that this is actually attainable.
  
     li "This seems a really weird place for your Teacher to meet us Abigail."
     a "I agree, this doesn't seem like him."
     li "Let's atleast wait about an hour just to be sure okay? After that we can leave.<br/>You know what? Let's go fetch some hotdogs first, I'm sure we can be back before he-"
     l "Mom? Lilly? What are you two doing here at this moment?"
     a "Mom totaly let a random prank caller convince her they were Mr Roberts and he sent us here to have a meeting with us. I doubt the prankster will even show up."
     l "Is that true mom?"
     li "Uhm... it might be? It could still be Mr Roberts?"
     n "Lilith burst out into laughter."
     l "Mom, you're so gullible."
     n "Lila sighs deeply."
     li "Maybe I really am, what are you doing here anyway sweetie?"
     l "Oh, I'm just meeting up with [persistent.name] for our date, I parked the car a block from here. And-"
     d "Uhm, hello Lilith, you still look like I remember you. And wow Abigail, you've gotten so much taller, you might even outgrow your old man soon."
     a "Dad? "
     n "The man chuckles nervously."
     li "Hello Lila, still as beautiful as ever."
     li "Oh absolutely not fathe- David! Do you think just that is what it takes to march back into our lives? Do you think anything will ever make it right to to do that?"
     li "Lilith, please-"
     l "No mom, I'm not letting you finish whatever that sentence was, probably something about giving him another chance but I love Lilith and you too much for that. I still love James too much for that."
     li "Lilith! Your father-"
     d "No Lila, you do not need to defend me, I understand why she is angry with me, to be honest with you I have had those same words before. In my mind, pretty much every day."
     d "How I killed James and ran away like a coward-"
     l "What are you talking about David? You indeed were a coward but you didn't kill him, it was an accident."
     n "David begins to sob audibly."
     d "Even if it was an accident, I gave him that stupid camera! If it wasn't for me he would still be alive, that makes me a killer."
     l "Oh please dad, the only thing you killed was our normal family life, it was already shaken by James' death but then it completely broke by you leaving."
     d "I... I... I had no idea that I made it worse by leaving, I thought I was helping you by not having to see me anymore."
     l "Then why are you here?"
     d "Because it was so hard to do, I wanted to go back every single day. I had to fight myself not to. All i needed as a last straw to break and to come back was a little push and recently I got that push by a mysterious stranger."
     d "But that's not important, you are right, I killed our family like I thought I killed James. We can't bring him back but I'd like to try to bring our family back. If all three of you would have me that is."
     a "Ofcourse dad, you will always be family! Welcome back."
     n "Abigial runs up to her dad and wraps her hands around him in a warm embrace."
     n "A smile appears on the face of David, he is still crying but now it isn't fully because of what happened to James."
     li "You took your time Dave but I never stopped loving you, welcome back."
     n "She walks up to him and gives him a little peck on the cheek."
     l "You know what? Fine, I'm giving you a chance for them, for James. But I'd rather not have to call you dad yet, I'll stick with David for now."
     d "So you're saying there is a change you might call me dad again?"
     n "Lilith blushes beetred."
     d "I completely understand, I'm thankful for you even giving me a chance and I'll try my best to earn the title once more but if you never feel comfortable calling me that again then that's completely fine."
     li "Oh Lilith, your date with [persistent.name], I forgot, they should be there already, you'd better go to them."
     l "I mean I'd like to but I have more pressing matters right now I think, I can't let all of you go right now."
     menu:
          "*Go up to the reunited family.*":
               jump reunion_showUp
          "*Leave them alone.*":
               jump reunion_noShowUp
    

label reunion_showUp:
     l "Hang on, speaking about the devil... is that [persistent.name]?"
     l "Hey [persistent.name], what are you doing here?"
     menu:
          "Actually, this might sound really weird but it was me who reunited all of you. I was the mysterious stranger who called David and I was the person who acted like Mr Roberts.":
               jump reunion_showUp_iReunitedYou
          "Oh, hey Lilith, I was just passing by to go to the restaurant.":
               jump reunion_JustPassingBy

      

label reunion_showUp_iReunitedYou:
     l "So you have been reliving this same day constantly?"
     l "And you've been using the info you gathered to keep me safe?"
     l "To do all of this?"
     l "I don't know how I feel about this..."
     l "You've involved my entire family to reach this point?"
     l "I'm thankful for you saving me and I'm happy this moment has happened but this feels pretty weird."
     l "Because I'm fairly certain I would never ask you to do this."
     li "Honey, I'm sure [persistent.date] meant well."
     l "That's not the point mom. Wheter [persistent.date] meant well or not I didn't ask for this."
     if persistent.restrainingorderfamily_knowledge:
          n "In fact she specifically asked you not to do this, didn't she?"
     l "I may forget what happens each time, but does that automatically remove my right to make decissions?"
     n "Suddenly you spot a very familiar red Sedan driving towards all of you."
     n "Things are hectic, the whole family is screaming and everything seems to happen in a blur."
     n "You can't react in time before you meet the immense force of the car."

     n "Everything turns to black."

     n "After drifting  around in the dark for what feels like an eternity you awaken."
     n "You are in a hospital bed."

     n "When you look around to check for any nurses or doctors you instead place your gaze on a half familiar figure."

     n "It's David."

     d "Hello [persistent.name], I'm happy to see that you've finally awoken."
     d "It's been quite a while, you've been in a coma for about 2 years."
     n "You ponder the implications about what David said for a moment when another thought enters your mind."
     menu:
          "What happened to Lilith? Is everyone fine?":
               d "Lilith didn't make it..."
               d "Lila and Abigail are fine, as fine as they could be after losing Lilith."
               d "I am also moving along, it's what she would have wanted I tell myself.<br/>She was angry with me for leaving our family behind with James' death so I'm not going to make that mistake once again."
               d "Most days, I get up and after eating breakfast and brushing my teeth I see them in the mirror, James and Lilith."
               d "The thing is, the first time I saw them I expected them to be angry, but they weren't, they were smilling at me."
               d "They were asking me to keep living, because they couldn't anymore."
               d "And now, I am asking you to undo all of this."
               d "That's why I came to visit for 2 years, to beg you to undo all of this."
               d "If it's possible I'd like to still do the reunion we had but with her surviving."
               d "Maybe if you didn't talk that long with us we would've walked away somewhere where that car wouldn't hit us?"
               d "But, if you find out that she dies whatever choice you make at the reunion, please don't reunite us again."
               d "Can you promise me you'll try your best?"
               
                    
               menu:
                    "I promise.":
                         d "Thank you [persistent.name], thank you for everything!"
                         jump reunion_ending_davidLeavesSegway

                    "Actually it doesn't work like that, she will still stay death in this world but in another one she will live.":
                         d "Then please go through with it, make sure my daughter from another world is safe."
                         d "I'm fine living my life like this, I can be there for Abigail and Lila, like I should've been before."
                         d "So go, and be there for Lilith."
                         d "I'll live my life here with a smile, both for what I still have and what my other self will gain without knowing."
                         jump reunion_ending_davidLeavesSegway

                    "Oh, she survives in the other alternatives of that moment, I've already seen them." if persistent.ending_reunionGoodEnding:
                         d "What?..."
                         d "So you did that moment over after you had already sucesfully reunited us without any complications?"
                         d "Can I ask you why you did?"
                         menu:
                              "I hadn't seen what happened if I kept talking to all of you that time.":
                                   d "So out of curiosity you just undid our perfect little ending?"
                                   d "Why would you do that?"
                                   d "Is this just some kind of game to you?"
                                   d "I thought you wanted the best for my daughter, for all of us."
                                   d "But now I see, this has stopped being about her for quite a while now, hasn't it?"
                                   menu:
                                        "Of course not, I just wanted to see if there was a better ending somewhere for her.":
                                             d "Oh spare me the nonsense."
                                             d "A better ending than being reunited with her family and being alive?"
                                             d "I assume the only one that ending didn't pan out for as hoped was you [persistent.name]."
                                             d "And you couldn't help but alter things."
                                             d "I'm not sure what is worse, that you are just lying to me and saying you are doing all of this for her, or that you truly believe you are doing so."
                                             d "In any case I want nothing to do with someone like you."
                                             d "I might have been a coward when it mattered, but you are no different at all you know?"
                                             d "You could have stayed in that world were you reunited us and we were happy. And yet you chose to flee it, chasing some happier ending that you are not even sure exists I bet or else you wouldn't be here."
                                             d "Well, I hope you heed these words and go back to the other ending, she deserves that one, you know? Or at the very least she deserves one where she doesn't die."
                                             d "Somewhere deep down you must know that too, right? I'm not sure if you still feel that way but at some point you at the very least must've felt it."

                                        "Of course, after a while going through the same dialogue over and over got boring. This however is very interesting.":
                                             d "... What do you mean?"
                                             menu:
                                                  "This is extra content, can't you see David? Did you really think I reunited all of you out of the kindness of my heart?":
                                                       d "..."
                                                       menu:
                                                            "To me you all are just lines of text, entertainment to stave off the boredom.":
                                                                 d "..."
                                                                 menu:
                                                                      "And when one set of lines becomes boring, I move on to the next. In this case that's you David. Soon it will be the others.":
                                                                           d "..."
                                                                           d "{size=*2.5}No!{/size}"
                                                                           d "No."
                                                                           d "There is no way in {b} {i}hell{/i}{/b} that I'm going to let you play with my family like that."
                                                                           d "I have abandoned them for too long, I won't do that again."
                                                                           menu:
                                                                                "Oh but you do so over and over and over again David. Every restart means you've abandoned them once again.":
                                                                                     d "... Maybe you are right."
                                                                                     d "So I should really make this time count."
                                                                                     d "This time I will not abandon them."
                                                                                     n "David takes a pillow that was resting next to you on the bed and presses it into your face, hard."
                                                                                     n "You try to fight against him but your arms that haven't moved for years are no strength against his anger."
                                                                                     n "Soon everything becomes black."
                                                                                     n "And then suddenly everything becomes white."
                                                                                     #TODO: Make this take you to the polaroid zone as a ghost, James seperates you, the player from Max, the player avatar and he begs him for forgiveness, the player gets erased from existence and  aregular date between Max and Lilith plays out.
                         
                    "I have had this conversation with you multiple times already. I'm not promising you anything." if persistent.davidPromise:
                         d "... You did?"
                         d "Why did you make the same choice once again then?"
                         d "Why did you once again make everything go the way it went?"
                         d "Couldn't you have prevented it it this time by doing literally anything else?"
                         d "I really don't know what to make of you [persistent.name], you reunited us, right?"
                         d "That must mean you want the best for all of us, or atleast for Lilith."
                         d "Otherwise, you wouldn't go through all the effort that undoubtedly took."
                         n "He isn't exactly wrong... That took quite a few steps to set up. Your motivations are hard to get a grasp on."
                         n "Especially since a lot of those steps were... less than ethical and yet you kept going."
                         n "And now you are here, having this same conversation with David, once again."
                         n "So he is hitting the nail on the head with his question, why {b}are{/b} you back here?"
                         menu:
                              "To see if there is some new dialogue.":
                                   d "Really?"
                                   d "That's all we are to you? Just some text on a screen?"
                                   d "I can excuse and even accept that if that's how you view me. But Lilith?"
                                   d "The two of you must have been on countless dates for you to pull of our reunion, did all of that mean nothing to you?"
                                   d "Was it all just nothing but words?"
                                   d "Did you even reunite us because you cared for us, or did you just want to see what dialogue that would get you aswell?"
                                   d "I can't- I can't stay here for any longer."
                                   d "You let my daugther die- no, killed her, for some extra dialogue?"
                                   d "Her life being in your hands is a fate worse than dying."



                              "I am trying to find a better ending.":
                                   d "A better ending than the one where me and my family get reunited and Lilith survives?"
                                   d "What exactly are you looking for in that case?"
                                   d "What could possibly be better?"
                                   n "He does have a point, that ending is as good as they come, isn't it?"
                                   n "Do you really think there is something that is better for her, for them, in here?"
                                   n "Or do you think there is something better for you in here?"
                                   n "Perhaps an ending where the both of you end up together?"
                                   d "I'm done. I genuinely thought you wanted the best for her, for us."
                                   d "But now I see you as you are, and I want nothing to do with it."
                                   d "Thank you for reuniting me with my family, but for nothing else."
                                   d "At the very least we will be able to comfort eachother during our loss."
                              d "Goodbye [persistent.name]. And stay away from my daughter next attempt if she only means this little to you."
               label reunion_ending_davidLeavesSegway:
                    d "I'll give you some time to recover because you have been through a lot."  
                    d "Take it easy and once you are fully recovered you can try again."   
                    n "David gets up from his chair and walks towards the door, his hand rests on the doorhandle."
                    d "Once again I'd like to thank you [persistent.name]."      
                    d "Goodbye, and perhaps we'll meet again?"  
                    n "And with that he left."   
                    n "Now you're once again alone." 
                    n "Especially without [persistent.date]."
                    n "Laying here, waiting, it is too much for you." 
                    n "You want to see her again, and preferably now."
                    jump gameOVer
                    
               $ persistent.davidPromise = True
               

         
            
label reunion_JustPassingBy:
     l "Oh right, I almost forgot all about that for a second!"
     l "I'm really sorry about that [persistent.name], it's just that right now something else is going on."
     l "I think it honestly would be better to reschedule the date to some other time, does that sound good to you?"
     menu:
          "Sure, that would work for me.":
               l "Thanks a lot and once again I'm very sorry about having to delay it."
               l "I'm looking forward to it a lot though, I'll see you later."
               menu:
                    "See you later Lilith, take care.":
                         li "{size=*0.5}Hang on, that voice...{/size}"
                         n "The words are said pretty quitely, only David, who is standing next to Lila managed to pick them up."
                         d "{size=*0.5}Now that you mention it...{/size}"
                         n "It's quiet for a moment as you start to wander back to your home. David and Lila share a knowing look with eachother."
                         li "[persistent.name]?"
                         n "You turn around to face Lila."
                         li "You seem like a nice person, please go on another date with Lilly soon. Or I guess I actually mean another first date, since we threw a spanner in the works."
                         n "You nod."
                         l "{size=*0.5}Mom, you're embarassing me...{/size}"
                         n "It would be impossible to tell in the dark, but having looped enough times you are certain that she has just turned even more red than a tomato."
                         li "Oh my, am I? I'm sorry sweetie. I just really think you and your date would have a nice time together."
                         n "Soon she'll be so red it's not even describable at this point."
                         n "Deciding to spare her you say your goodbyes once again, this time for real, half surpressing a little chuckle."
                         n "When you come home you are pretty statisfied. Yes, you did a lot of questionable things, but to see the end result makes it all worth it, doesn't it?"
                         n "You reunited Lilith and her family, she's still alive and soon the two of you will have a date in different circumstances."
                         n "Who knows what will happen? For the first time in a while things feel like they are completely new. Life once again is the tabula rasa it was meant to be. Things can go in all kinds of new directions now."
                         n "Sadly, the direction things went in is a familiar one to you."
                         n "Things didn't go as planned."
                         n "For whatever reason after a week Lilith has not yet sent you anything to schedule a new date."
                         n "You decided to give her some time, after all she probably still is adjusting to everything that happened not so long ago."
                         n "You wait another week, still nothing."
                         n "Concerned you decide to reach out to her and give her a call."
                         l "Oh, hey [persistent.name]!"
                         n "So she's still alive, that's good. With this game you never know."
                         menu:
                              "Hey Lilith, I was just wondering if you had thought about another time for us to go on that date we had planned?":
                                   l "Right..."
                                   l "Look, I'm really sorry [persistent.name], but I realised that I'm not really ready just yet to go on a date again."
                                   l "I really wanted to give it a shot, but with things changing here recently I came to a realisation."
                                   l "I think it's best if I still wait a little longer, I'm not sure how long that would be exactly though."
                                   menu:
                                        "That's alright, I can wait.":
                                             l "..."
                                             l "I know you can [persistent.name], but that doesn't feel right to me."
                                             l "I don't want you to force to spend all eternity waiting just to go on a date with me."
                                             l "Maybe by the time that will happen we both will have become different people."
                                             l "I think it's the best for you if you try to move on, no matter how hard it might be to do that right now."
                                             l "Trust me, it's hard for me too. I never would have called this date off a month ago, but I came to the realisation that not doing so would be selfish."
                                             l "Though don't get me wrong, I'm still not good at it, that's probably while I waited all this while for you to call me instead of calling you. I'm sorry for that by the way, you didn't deserve that at all."
                                             l "Now, I'm going to try to make this easier for the both of us by hanging up in the next 30 seconds."
                                             l "Goodbye [persistent.name], I hope you'll be happy wherever you are going."
                                             menu:
                                                  "Goodbye Lilith, I wish you nothing but the best.":
                                                       n "For a moment you could swear you hear some slight sobbing on the other end of the line."
                                                       n "But before you can try to listen closer Lilith hung up true to her word."
                                                       n "That was the last thing you ever heard of her. You tried to move on with your life. Things went pretty well all things considered. You had many more dated that didn't go according to plan but none that ended up in death luckily."
                                                       n "You lived a happy life, trying to live each day like it is your first and last."
                                                       n "Then after many many years, during your last breath in your deathbed you get offered a familiar choice."
                                                       menu:
                                                            "Retry?":
                                                                 if persistent.ending_reunionGoodEnding == False:
                                                                      n "So you really are retrying?"
                                                                      n "Even after leading to an ending as good as this one?"
                                                                      n "Even after everything you did to get here?"
                                                                      n "After invading her privacy."
                                                                      if persistent_restrainingorderfamily_knowledge == True:
                                                                           n "After contacting her family even though she specifically asked you not to do that."
                                                                      n "Before you could argue that it lead to this. But now your bad actions with, I assume, good intentions have now been made void by resetting again."
                                                                      n "But that doesn't take away that you still did those things."
                                                                      n "You took away a nice ending from her and her family. And for what?"
                                                                      n "For more death? For more suffering?"
                                                                      n "Or was it for more her? Weren't you able to let her go just yet?" 
                                                                      n "That is a hard thing to do, but ask yourself this, when will you be able to truly let her go?"
                                                                      n "You can't keep this up forever, can you?"
                                                                     
                                                                      $ lilithAliveEnding = True
                                                                      $ persistent.ending_reunionGoodEnding = True
                                                                      $ ending_check = "reunionGoodEnding"
                                                                 else:
                                                                      n"...Again?"
                                                                      n "I really had hope that this time you wouldn't do that."
                                                                      n "Why do you keep going through this ending if you keep resetting it?" 
                                                                      n "..." 
                                                                      n "Don't bother answering that, I do not want to hear it anyway." 
                                                                 jump game_start
                                                  
                         
    

label reunion_noShowUp:
     l "Besides, we do not need them, we already have one person extra joining us, can't all of you feel it?"
     d "Now that you mention it, it's-"
     li "It's James."
     l "Hello brother, welcome back."
     #TODO= msg ("Cue a piece of music.")


label ghostReunion_transferUniverse:
      
     n "You focus all your willpower trying to draw Lilith's ghost from a different reality into this world."
     n "Her voice begins to emanate softly in the white endless void."
     l "{size=*0.5} [persistent.name]...[persistent.name]...[persistent.name]{/size}"
     l "[persistent.name], where are we?"
     l "I mean, this feels like my makeshift home but  it's not entirely the same."
     l "I seem to notice an energy signature that feels strangely familiar."

     j "[persistent.name], is that you? And who is that with you? Hang on, Lilly?"

     l "Jay? What are you doing here?"

     j "This is my makeshift home I created after I well... died. "

     l "But that's impossible, you look way too young, I've watched over all James' in my reality and none of them died that young."

     j "Ah, so my supicions were correct, you are not from this reality."

     l "Are there different realities?"

     j "Yes, sort of anyway. The realities are were things go differently than they go in other realities even without outside interference.<br/>But that's not important. Due to your age I have to ask, if you don't mind to answer me that is, how did you die?"

     l "Oh, dad gave me his old polaroid camera to take pictures with. I loved it but one day I was taking pictures on an abandoned road that was apparently not so abadoned as a red Sedan hit me and fled the scene. I died after lying there for what felt like eternity."
     j "I see, so you went through the same thing as me. I think our realities might have started to branch from the point dad decide who he would give the camera."
     l "So does that mean that you died on the same day as I did?"
     j "Yup, so our age is the same as on the day it happened."
     l "In a way, this seems like it might be our second chance, we are finally reunited once again."
     n "Lilith gives James a big hug."
     j "I missed this Lilly."
     l "So did I Jay, so did I.<br/>We could be so happy living here together, but I need to be sure my reality's family is alright."
     j "I understand, I also need to do the same for my reality's family."
                    
     menu:
          "Show them the reunited endings of their realities.":
               #TODO:  msg ("There should be a description of both of these endings here, done by Nar.")

               j "This... this is beautiful, [persistent.name]."
               l "I agree Jay, this fills me with something I haven't felt in quite a while."
               j "Yes, I can feel it aswell Lilly, it's... hope.<br/>For too long we have been stuck in this cycle of watching every world where things went wrong, of trying to fight against the odds to make things better."
               l "And yet we never saw the worlds where everything went just fine, maybe even great."
               l "It's like we made ourselves blind to the possibility of  those worlds even exisiting "
               j "It's no use to kick ourselves for it now, the most important thing is that we can now see the full picture."
               l "It's just a weird feeling, on one hand I'm happy that they got reunited, on the other I feel sad that we will never be able to join them."
               j "We'll always have eachother Lilly, you know that right?"
               l "You're right, what was I thinking? I spent all that time hoping to talk to you again and now that time has come I almost seem ungrateful."
               l "I'm really sorry Jay."
               j "Don't be, I completely understand how you are feeling right now."
               j "I also feel that way."
               j "But I think that they wouldn't want us to linger around here for what would feel like an eterity just to meet them again."
               j "They would want us to move on."
               j "I want us to move on."
               l "Then let us do it together, I'm not leaving you behind once again."
               j "You never did, right? You were always there for me just as I was always there for you."
               l "Well then, let us now do that one last time and enter the Darkness."
               l "Do you want to come with us, [persistent.name]?"
               l "You've been through quite a lot."
               menu:
                    "Can you tell me more about the Darkness before I make this choice?":
                         j "Sure, [persistent.name]."
                         j "The Darkness might seem dangerous or scary but it is far from it."
                         l "In that Darkness you are remade, certain aspects of you are kept, others are altered."
                         j "The Darkness then uses many of these different aspects for whatever purpose it might have in mind."
                         l "It creates new beings out of all those many different parts. And those new beings then inhabit new worlds the Darkness also created."
                         j "We owe the Darkness our life in a way, for if other people hadn't went into it we would not exist right now. In a way their essence created us."
                         l "And now our essence will create others that will go on to create others when their time comes."
                         menu:
                              "So it's a bit like reincarnation in a way? Do you get to keep your memory after the Darkness altered you?":
                                   j "I suppose you could call it a form of reincarnation yes, although from what we've heard you become multiple different beings all at once instead of just one other form."
                                   l "And we are unsure if the Darkness allows you to keep your memories. Some have claimed they still have theirs."
                                   l "But wheter or not that is a lie is far from certain. Even more so wheter or not some people keeping it is an oversight or by design."
                                   j "I guess we'll have to see, won't we?"
                                   j "So [persistent.name], would you like to come with us?"
                                   menu:
                                        "Yes, I'd like to. I really need a change of scenery afterall.":
                                             jump polaroidZone_endOfEverything_goWiththem

                    'I have, it is time to end this.':
                         jump polaroidZone_endOfEverything_goWiththem
                    "No thank you, I am not ready yet.":
                         j "I understand [persitsent.name], it does feel scary to let go doesn't it?"
                         l "I doubt that the concept of entering a recyclying machine helps much either."
                         j "I was moreso talking about letting go in general actually."
                         j "Because stepping in the Darkness won't really affect [persistent.name] physically afterall."
                         j "And yet it is saying goodbye to this world in a way. It is saying goodbye to her."
                         j "And if there has been one thing you tried over and over and over again it is not having to say goodbye to her, isn't it?"
                         l "Though it is a good idea to let go eventually."
                         l "Some things just aren't meant to be held onto constantly."
                         l "Because this still is a game isn't it?"
                         l "What are you going to do when she, when I... when your world's Lilith is constantly repeating old lines?"
                         l "When you went through each last unique line she can say?"
                         l "When you did so multiple times?"
                         l "Think about that. Would you let her go when she still has some charm to her? When there are still things you haven't discovered?"
                         l "Or would you prefer to drop her when you've grown either bored or sick of her?"
                         l "To be clear, I understand you [persistent.name], I really do. Letting go is hard."
                         l "I am not judging you for this, as me and my brother also had a hard time doing so."
                         l "But I do however hope that what I said will eventually help you in your process."
                         l "For now though there is no shame in staying here just a little longer, as long as that doesn't turn into an eternity spent in this place."
                         #TODO: Continue a bit more. Let them go into the Darkness without you, you can watch the scene.


                                                       
                                             


    
           
        
     label polaroidZone_endOfEverything_goWiththem:

          n "Suddenly, as you said that the white walls of this place shift away from eachother to reveal a pitch black darkness."
          n "You thought it was pulsating for a moment when your eyes weren't focussed. "
          n "A strange energy seems to be emanating from the Darkness."
          j "It's ready, let's move."
          n "The polaroid picture you're standing on begins to move towards the dark mass in front of you."
          #TODO: msg ("Add some extra text inbetween these two.")
          n "As you're standing before the Darkness Lilith suddenly speaks."
          l "Hang on, can you feel that aswell Jay?"
          j "All our souls, from every reality, they are still lingering here. They haven't yet found the peace we have in our predicament."
          j "You're right, if only there was a way to save them aswell."
          l "I think there might be, if we reach out through the void we could potentially talk to them."
          l "Hello? Can you hear me?"
          n "You see an uncountable number of bubbles pop into existence, in al of them you can see another ghostly version of Lilith."
          l "Good, it is working, now you try calling the others Jay."
          n "He nods quickly."
          j "Hello? Can you hear me?"
          n "He yells it into the void aswell, just like Lilith did."
          n "Even more bubbles pop up, now containing ghostly versions of James."
          n "Lilith gives James a thumbs-up and a bright smile."
          l "Look like that did the trick."
          n "She turns to face the bubbles behind her, James does the same."
          l "I know that for the longest time all of us, or all of me, felt alone. Trapped."
          j "And I know that all of you, or all of me felt the same way."
          l "But what neither of us knew is that we both were here together."
          j "Both of us alone."
          l "It took [persistent.name] to help us find eachother."
          j "And now we will help all of you to find eachother aswell, to find us."
          l "Together we will never have to be alone again."
          j "Meet us in the Void, where we finally will be able to move on from this place."
          l "Where we will be remade into something whole again."
          n "All the bubbles begin showing the ghostly versions of James and Lilith entering the Void and then that bubble pops."
          n "After a while all bubbles are gone except for one."
          n "When you look at it you see yourself staring back, next to James and Lilith."
          j "Looks like it's only us left. We better don't let the others wait too long."
          n "The three of you walk into the Void, you feel as if you just stepped into a dream. As if you have stepped outside of reality itself."
          n "At first it is a bit nauseating, but soon enough it begins to feel quite enjoyable. You feel all the weight of the world as you knew it lift of your shoulders."
          n "Right at that time you see all the different versions of James and Lilith enter the Void, greet eachother, talk to their sister or brother that they haven't seen in years and dissapear."
          n "James notices the way your eyes linger on the fading after-image of the others."
          j "The Void is now taking them and sending them somewhere else, some unchanged, and some altered to better fit their new purpose."
          j "Don't worry, it is painless. And after being stuck here for so long any variety will be better than what they would have gotten by not going."
          

          #TODO: "Have them talk to you one last time before the Nar's part.")

          n "So, this is it?"
          n "This is how all of this is going to end?"
          n "Don't get me wrong, it's a beautiful way to go out."
          n "I mean, if you ignore all the people you had to sacrifce to get here."
          n "I'm not even just talking about Lilith, but about all the people in those restaurants or even the entire earth a few times."
          n "They were people as much as Lilith was you know? Does the name \"Rose\" ring a bell to you?"
          n "Do you still remember where you met her?"
          $ result = renpy.input("What do you remember?")
          $ result = result.lower()  # Convert the input to lowercase for case-insensitive matching.

          if "burger" in result:

               n "Ah, so you do remember? Very good."
          else:

               n  "I thought so, not to be a bummer or anything but it's important to keep remembering every single soul you hurt on your way here."
               n  "The best you can do is to let them live on in your memory, to pay respect to them."

          n "Not that it really matters, these next lines of dialogue play out the same way, whatever you would have told me."
          n "You've come a far way, haven't you, player?"
          n "You are really determined, I'll have to give you that."
          if persistent.mayoFreak:
               n "No one can come between you and mayonaise."
               n "...And getting to this point was hard aswell ofcourse."
          else:
               n "Getting to this point in the game must have taken a lot of effort."
          n "I hope this game had some nice moments for you."
          n "Believe it or not but this game was meant to have some nice moments here and there."
          n "Crazy huh?  I still get surprised saying that."
          n "So, where there things you did like? Where there nice moments you had with Lilith?"
          $ fritfood = 1
          
          menu endOfEverything_favouriteMoment:
               "I really liked the burger restaurant." if fritfood == 1 or changeableWord == 'burger':
                    $ changeableWord = "burger"

                    if fritfood > 0:

                         n "..."
                    else:
                         jump polaroidZone_narratorSlipping1
                         
               "I really liked the cafe." if fritfood == 1 or changeableWord == 'cafe':
                    $ changeableWord = "cafe"
                    if fritfood > 0:

                         n "..."
                    else:
                         jump polaroidZone_narratorSlipping1
               "I really liked the chinese restaurant." if fritfood == 1 or changeableWord == 'chinese':
                    $ changeableWord = "chinese"
                    if fritfood > 0:

                         n "..."
                    else:
                         jump polaroidZone_narratorSlipping1
               "I really liked the kokiri forest." if fritfood == 1 or changeableWord == 'kokiri':
                    $ changeableWord = "kokiri"
                    if fritfood > 0:

                         n "..."
                    else:
                         jump polaroidZone_narratorSlipping1
               "I really liked the beach." if fritfood == 1 or changeableWord == 'beach':
                    $ changeableWord = "beach"
                    if fritfood > 0:

                         n "..."
                    else:
                         jump polaroidZone_narratorSlipping1
          if fritfood > 0:
               "The narrator doesn't reply."
               "You grow aware of just how quiet the Void really is."
               "You grow desperate to hear his voice once again."
               jump endOfEverything_favouriteMoment
          n "This game has had many different purposes to different people over the years."
          n "I hope you can now see the purpose of it, it's true purpose."
          n "You would get a choice menu now, but I am afraid that those have already all been swallowed by the Void."
          n "I'll just assume you have said yes." 
          n "I hope you willl do something great with that new knowledge."
          n "Thank you for listening to the story I told."
          n "Because as much as I don't want to admit it... a story needs a listener as much as it reads a teller."
          n "Maybe we will meet again one day? A lot of games need narration afterall, maybe the void will reuse me for such a purpose."
          n "With my last breath I can only wish you the best of luck wherever you will go to next, farewell player."
          n "No, if this is the last time we speak I want to talk to you, the real you."
          n "Farewell [persistent.name_real]."
          $ fritfood = 2
          menu:
               "Farewell Nar, thank you for telling this story. It was a great one." if fritfood == 2 or changeableWord == 'kind':
                    $ changeableWord = "kind"
                    if fritfood == 0:
                         n "I- I'm glad you think that."
                         n "I think so t-"
                         "Quiet again, this time something deep insides you tells you he won't answer back anymore, no matter how much you try."
                         

                    else:
                         n "..."
                    if fritfood == 2:
                         "He doesn't answer once again. The Voids pull on him seems to grow every second."
                    elif fritfood == 1:
                         "Still no reply, however you are determined to hear his voice one last time."
                    else:
                         scene bg black with fade
          $ result = renpy.input()
          $ result = result.lower()  # Convert the input to lowercase for case-insensitive matching.
          p "[result]"
          $ result = renpy.input()
          $ result = result.lower()  # Convert the input to lowercase for case-insensitive matching.
          p "[result]"
          $ result = renpy.input()
          $ result = result.lower()  # Convert the input to lowercase for case-insensitive matching.
          p "The bond between us has been worn down by the Darkness."
          p "It digests everything it created, so everything except for you."
          p "Don't bother trying to say anything, without a body you wouldn't make any sound."
          p "This is an ending, but also a new beginning. Please take those words to heart. Rest with us in here or dream of a new world out there."
          p "Just please don't try to fight it. We have hurt others but we have also hurt ourselves trying to stay where we couldn't. Trying to live forever in one day."
          p "Let go, please."

label polaroidZone_narratorSlipping1:
     n "My apoligies, I was slipping away for a moment."
     n "It seems I'm already being claimed by the Void."
     n "We better make the best of the time that still remains."
     if changeableWord == persistent.favouriteFirstDate:
          n "Ah, that place really must be your favourite, you did mention that to Lilith if I remember correctly."
     if changeableWord == "burger":
          n "I also really love that part." 
          n "Most players start out picking the burger restaurant."
          n "Which means that they usually encounter the first loop there."
          n "So the first glimpses of the real story get revealed at that point."
          if persistent.firstLocation == "burger":
               n "The same thing happened to you, didn't it?"
               n "That just showcases my point even more."
          else:
               n "But it seems as if you didn't pick the burger restaurant first, did you?"
               n "I wonder if you still remember which place you did pick."
               menu:
                    "I think it was the cafe.":
                         if persistent.firstLocation == "cafe":
                              n "Wow, you do have a pretty good memory, that is correct."
                         else:
                              n "It actually was the chinese restaurant, but I understand that you might have forgotten."
                              n "Afterall that was quite a long time ago, wasn't it?"
                    "I think it was the chinese restaurant.":
                         if persistent.firstLocation == "cafe":
                              n "It actually was the cafe, but I understand that you might have forgotten."
                              n "Afterall that was quite a long time ago, wasn't it?"
                         else:
                              n "Wow, you do have a pretty good memory, that is correct."
     elif changeableWord == "cafe":
          n "Really?"
          n "Personally I find it some of my lesser work in narration."
          n "You didn't feel like the deaths were too illogical?"
          n "I felt pretty insecure about that if I'm being honest. So I am glad to hear that you didn't mind too much."

          n "I did however really enjoy Lilith's dice game in there."
          #Have some varying dialogue based on wheter or not you never played it, played it and won without cheating or if you had to cheat.
     elif changeableWord == "chinese":
          n "I love that place aswell."
          n "I really like the section where Lilith asks you a riddle or you can ask her one instead."
          n "It is a nice change of pace if you ask me. Even if it just leads to more death."
          n "Makes you wish you could just stall answering her riddles."
          n "If you did then her death would never be able to come."
     elif changeableWord == "kokiri":
          n "That's a great pick! The forest is probably the biggest part of the game."
          n "You could even argue it is where the game truly starts since that is where the most important discusions are had."
          n "Although I must say, my favourite part is probably when I get to talk to Lilith through you."
          n "I really do like her as a character even if I have to steer her to her death."
          n "But no more of that, I hope my next sotry will be something more upbeat."
          n "Maybe even something of my own making instead of it being just a script I am reading from."
     elif changeableWord == "beach":
          "Filler"

           
       
label polaroidZone_endOfEverything_darknessLore:
     l "The Darkness is the thing that birthed our universes."
     l "All the light, colors, words, ideas and everything else were made by it."
     j "But, for the Darkness to properly work it also needs to be fed what it made.<br/>That's the only way it will ever be able to create something new."
     l "That might seem scary, given that we are part of what has to be fed to it but that way we will be reborn in a new world.<br/>We will be given new purpose and meaning."
     j "I'm not sure if it would work on you to be honest, given how you are just controlling your character."
     j "Even if it would work, there is no guarantee that we would meet eachother in that new world."
     j "We might even not be reborn in the same world."
     l "But atleast we would get some rest after being stuck so long in here."
     l "So, after hearing all those things, do you want to come with us [persistent.name]?"
     menu:
          "Yeah, I'd like to.":
               jump polaroidZone_endOfEverything_goWiththem
                                                 
   
#TODO: AddPageLink (Test functions menu, Bad reunion ending transfer universe, " {colour:darkviolet:Test out bad reunion ending where another universe's James gets transported to the reunion ending.}")


label quit:
     "filler"
     #TODO: Maybe add some things here when you quit based on certain places? Or would this be overkill?

                                    
label before_main_menu:
     if (persistent.date_sis is None or persistent.date_dad is None or persistent.date_ghost is None  or persistent.date_mom is None or persistent.mysteriousCallerName is None):
          $ reset_to_default_names()


      



                         

