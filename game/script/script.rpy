# The script of the game goes in this file.

# How many times a specific death must be seen before the narrator offers to skip it.
define death_skip_threshold = 4


# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
     import re
     import time

     # Tracks which character is actively speaking for callback-driven sprites.
     speaking = None
     speaking_states = {}

     TALKING_MODE_ADAPTIVE = "adaptive"
     TALKING_MODE_FIXED = "fixed"
     TALKING_MODE_MIXED = "mixed"
     FIXED_TALKING_INTERVAL = 0.20
     MIXED_SYLLABLES_PER_SECOND = 4.0

     def get_talking_animation_mode():
          return getattr(persistent, "talking_animation_mode", TALKING_MODE_ADAPTIVE)

     def get_talking_animation_mode_label(mode=None):
          mode = mode or get_talking_animation_mode()

          if mode == TALKING_MODE_FIXED:
               return "Fixed Interval"
          if mode == TALKING_MODE_MIXED:
               return "Count + Fixed Speed"
          return "Count + Text Speed"

     def strip_dialogue_text(text):
          text = re.sub(r"\{[^}]*\}", "", text or "")
          text = re.sub(r"\s+", " ", text)
          return text.strip()

     def estimate_syllables(text):
          words = re.findall(r"[a-zA-Z']+", text.lower())
          total = 0

          for word in words:
               word = re.sub(r"[^a-z]", "", word)
               if not word:
                    continue

               syllables = len(re.findall(r"[aeiouy]+", word))

               if word.endswith("e") and not word.endswith(("le", "ye")) and syllables > 1:
                    syllables -= 1

               total += max(1, syllables)

          return max(1, total)

     def estimate_speaking_interval(text):
          visible_text = strip_dialogue_text(text)

          if not visible_text:
               return 0.18

          preferences = getattr(store, "_preferences", None)
          text_cps = getattr(preferences, "text_cps", 0) if preferences else 0

          if not text_cps or text_cps <= 0:
               return 0.18

          segment_duration = max(len(visible_text), 1) / float(text_cps)
          syllable_count = estimate_syllables(visible_text)
          interval = segment_duration / max(syllable_count * 2.0, 1.0)

          return max(0.07, min(0.35, interval))

     def build_speaking_state(text):
          visible_text = strip_dialogue_text(text)
          syllable_count = estimate_syllables(visible_text)
          mode = get_talking_animation_mode()

          if mode == TALKING_MODE_FIXED:
               return {
                    "mode": mode,
                    "interval": FIXED_TALKING_INTERVAL,
                    "duration": None,
                    "stop_on_slow_done": True,
               }

          if mode == TALKING_MODE_MIXED:
               return {
                    "mode": mode,
                    "interval": FIXED_TALKING_INTERVAL,
                    "duration": max(syllable_count / MIXED_SYLLABLES_PER_SECOND, FIXED_TALKING_INTERVAL),
                    "started_at": None,
                    "stop_on_slow_done": False,
               }

          return {
               "mode": mode,
               "interval": estimate_speaking_interval(visible_text),
               "duration": None,
               "stop_on_slow_done": True,
          }

     def while_speaking(name, open_d, closed_d, done_d, st, at):
          state = speaking_states.get(name)

          if state is None:
               return done_d, None

          is_active = False

          if state["mode"] == TALKING_MODE_MIXED:
               duration = state.get("duration")
               started_at = state.get("started_at")
               elapsed = (time.time() - started_at) if started_at is not None else 0.0
               is_active = duration is not None and elapsed < duration
          else:
               is_active = speaking == name

          if is_active:
               interval = state.get("interval", FIXED_TALKING_INTERVAL)
               cycle = interval * 2.0

               if (st % cycle) < interval:
                    return open_d, interval
               return closed_d, interval

          return done_d, None

     curried_while_speaking = renpy.curry(while_speaking)

     def WhileSpeaking(name, open_d, closed_d, done_d=Null()):
          return DynamicDisplayable(curried_while_speaking(name, open_d, closed_d, done_d))

     def speaker_callback(name, event, what=None, start=None, end=None, **kwargs):
          global speaking

          if event == "show":
               speaking = name
               segment = what[start:end] if what is not None and start is not None and end is not None else what
               speaking_states[name] = build_speaking_state(segment)
               if speaking_states[name]["mode"] == TALKING_MODE_MIXED:
                    speaking_states[name]["started_at"] = time.time()
          elif event == "slow_done":
               state = speaking_states.get(name)
               if state is None or state.get("stop_on_slow_done", True):
                    speaking = None
                    speaking_states.pop(name, None)
          elif event == "end":
               speaking = None
               speaking_states.pop(name, None)

     speaker = renpy.curry(speaker_callback)

define l = Character("[persistent.date]", callback=speaker("l"))
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
define watchName = "???"
define w = Character("[watchName]")


default date_sub = "she"
default date_obj = "her"
default date_pos = "her"
default date_is  = "is"
default from_menu = False
default persistent.talking_animation_mode = "adaptive"



# Flash overlay screen for flash_screen effect
screen flash(color="#ff0000"):
     add Solid(color) at flash_fade

transform flash_fade:
     alpha 1.0
     linear 0.15 alpha 1.0
     pause 0.2
     linear 0.15 alpha 0.0

# Family term shorthands (defaulted for store variable safety)
default date_sibShort = "sis"
default date_sib = "sister"
default date_child = "daughter"
default sis_sibShort = "sis"
default sis_sib = "sister"
default sis_child = "daughter"
default dad_parShort = "dad"
default dad_par = "father"
default mom_parShort = "mom"
default mom_par = "mother"
default ghost_sibShort = "bro"
default ghost_sib = "brother"
default ghost_child = "son"


image forestHill = "kokiriForestHill.png"

image red = Solid("#780808") 

image burgerRestaurant_bg = "burgerBackground.png"
image burgerRestaurant_fg = "burgerForeground.png"

image chineseRestaurant_bg = "chineseBackground.png"
image chineseRestaurant_fg = "chineseForeground.png"

layeredimage burgerRestaurant:
     always "burgerRestaurant_bg"
     always "burgerRestaurant_fg"

layeredimage chineseRestaurant:
     always "chineseRestaurant_bg"
     always "chineseRestaurant_fg"

layeredimage burgerRestaurantBack:
     always "burgerRestaurant_bg"

layeredimage burgerRestaurantFront:
     always "burgerRestaurant_fg"

# Lilith sprites (closed/open mouth). Is it possible to animae this?
image lilith talk_closed = "lilithHappyTalkingClosed.png"
image lilith talk_open = "lilithHappyTalkingOpen.png"

image lilith talking_happy = WhileSpeaking("l", "lilith talk_open", "lilith talk_closed", "lilith talk_closed")
     

















# The game starts here.
#I should have made all flags that need remembering end with "_knowledge" do this from now on for each such flag and also make the flags underneath this work like that and the if cases that check for these flags also need to be properly changed.
#The explanation text will also need a full file, maybe Kokiri will need multiple.


label start:
     $ _quit_slot = "quitsave" #This makes sure that when quiting it gets saved as "quitsave"
     
     

     if persistent.firstboot == None: 
          
          #This line ensures all flags that don't need constant resetting get reset only the first time the player boots the game.
          default persistent.firstboot = True
          default persistent._console_short=False
          default persistent.censor_mode = False
          default persistent.message_index = 0
          default persistent.letter_index = 0
          default persistent.name = None
          default persistent.canSave = False
          #Deaths:
          default persistent.death_seen_counts = {}
          default persistent.death_skip_always = {}
          default persistent.death_skip_prompt_counts = {}
          default persistent.death_skip_id_order = []
          default persistent.lildeaths = 0
          default persistent.nightmareCounter = 0
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
          #Polaroid zone death:
          default persistent.ufoCrash_knowledge = False
          

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
          default persistent.trinity_sunMet = False
          default persistent.trinity_moonMet = False
          default persistent.mayoFreak = False
          default persistent.kokiri_watchedScenery = False
          default persistent.kokiri_watchedStarsAlternatePlace= False
          default persistent.kokiriHonoredPromiseCancelDate = False
          default persistent.kokiriBrokenPromiseCancelDateTurnCounter = 0
          default persistent.threatenNarratorForEnding = False
          default persistent.kokiri_abbyMasking_knowledge = False
          default persistent.burger_nothingIsPerfect = False
          
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
          default persistent.mayoProphecy_knowledge = False

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
          default kokiri_ToldLillyHowManyRetries = True
          #Kokiri poems
          default persistent.kokiri_poem_window_knowledge = False
          default persistent.kokiri_poem_bang_knowledge = False
          default persistent.kokiri_poem_lights_knowledge = False
          default persistent.kokiri_poem_snowwoman_knowledge = False
          default persistent.kokiri_poem_shadowman_knowledge = False
          default persistent.kokiri_poem_time_knowledge = False
          default persistent.kokiri_poem_sun_knowledge = False
          default persistent.kokiri_poem_marble_knowledge = False
          default persistent.kokiri_poem_beach_knowledge = False
          default persistent.kokiri_allOldPoemsRead = False
          default persistent.kokiri_allRecentPoemsRead = False
          default persistent.rp_detect = False #This flag will be used to try to check if a player is returning to the game after erasing their save-file.
          default persistent.met_james = False
          default persistent.passWrongOnPurpose_narratorRant_counter = 0
          default persistent.passWrongOnPurpose_narratorRant_wrongTimesInARowCounter = 0
          default persistent.passWrongOnPurpose_narratorRant = False
          #Extra:
          default persistent.keyUse_knowledge = False
          default persistent.keyUnderBed_knowledge = False
          default persistent.chickenTendiesUnlock = False
          default persistent.burgerGameJoke = False
          default persistent.CancelledBeforeBeingAsked = False
          default persistent.kokiri_HonoredPromiseCancelDate = False
          default persistent.reachEndingRecent = False
          default persistent.damocles_knowledge = False
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
          default persistent.lilaCallRecievedAbbyProof_knowledge = False

          #Characters:
          default persistent.date_dad = ""
          default persistent.date_mom = ""
          default persistent.date_ghost = ""
          default persistent.mysteriousCallerName = ""
          default persistent.jamesMode = False

          #Pronouns (stored as dicts: sub/obj/pos/ref/pred per character):
          default persistent.date_pronouns       = {"sub": "she",  "obj": "her",  "pos": "her",   "ref": "herself",   "pred": "hers", "is": "is",  "was": "was",  "has": "has",  "does": "does",  "vs": "s"}
          default persistent.date_sis_pronouns   = {"sub": "she",  "obj": "her",  "pos": "her",   "ref": "herself",   "pred": "hers", "is": "is",  "was": "was",  "has": "has",  "does": "does",  "vs": "s"}
          default persistent.date_dad_pronouns   = {"sub": "he",   "obj": "him",  "pos": "his",   "ref": "himself",   "pred": "his",  "is": "is",  "was": "was",  "has": "has",  "does": "does",  "vs": "s"}
          default persistent.date_mom_pronouns   = {"sub": "she",  "obj": "her",  "pos": "her",   "ref": "herself",   "pred": "hers", "is": "is",  "was": "was",  "has": "has",  "does": "does",  "vs": "s"}
          default persistent.date_ghost_pronouns = {"sub": "he",   "obj": "him",  "pos": "his",   "ref": "himself",   "pred": "his",  "is": "is",  "was": "was",  "has": "has",  "does": "does",  "vs": "s"}

          # Family terms (how others refer to each character, with short/long forms)
          default persistent.date_family_terms = {"sibShort": "sis", "sib": "sister", "child": "daughter"}
          default persistent.date_sis_family_terms = {"sibShort": "sis", "sib": "sister", "child": "daughter"}
          default persistent.date_dad_family_terms = {"parShort": "dad", "par": "father"}
          default persistent.date_mom_family_terms = {"parShort": "mom", "par": "mother"}
          default persistent.date_ghost_family_terms = {"sibShort": "bro", "sib": "brother", "child": "son"}

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
          default persistent.ending_badDate = False
          default persistent.ending_reunionGoodEnding = False

          #Ending counters:
          default persistent.ending_retry_counts = {}
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
          default persistent.jamestalk_ilikeher_knowledge = False
          default persistent.jamestalk_iloveher_knowledge = False
          default persistent.jamestalk_justgame_knowledge = False
          default persistent.fleeingDeaths_counter_knowledge = 0
          default persistent.lilithAliveAndRetriedCounter = 0
          default persistent.narratorMonologue_dicePuzzleIntentionalyFailed = False
          default persistent.abigail_numberfakeout = False
          default persistent.burger_Orpheus_knowledge = False
          default persistent.familyContacted = False
          default persistent.burger_faceRemembered = False
          default persistent.cabinVoice = "S."
          default persistent.davidPromise = False
          default persistent.datedJames = False
          default persistent.datedLilith = False
          default persistent.firstLocation = ""
          default persistent.ringRiddle_knowledge = False
          default persistent.lilaToldAbbyOpportunity_knowledge = False
          default persistent.lilaCallNeedsAbbyProof_knowledge = False
          default persistent.lilaCallRecievedAbbyProof = False
          default persistent.rockMode = False
          default persistent.noRockPunsForNar = False
          default persistent.testmode = False
          default persistent.david_apology_made_knowledge = False
          default persistent.lilithOpenToReunion_knowledge = False
          default persistent.lilaTwoJobsOwnChoice_knowledge = False
          default persistent.jamesUnclearAnswered = False
          default persistent.rejectPhone_Block = False
          default persistent.gallery_unlocked = False

          #Non-persistent
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
          default kokiri_goalSurvive = False
          # Locations:
          default burger_poem_cleancheck = False
          default burger = False
          default burgerBeenBefore = False
          default burger_alt = False
          default onlyBurgers = False
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
          default kokiri_toldLillySheLives = False
          default kokiri_fullControlAndStillDying = False
          default noTalkAngryLilith = False

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
          default called_James = False
          default kokiri_notReadyToLetGo = False

          #Kokiri recent poems
          default kokiri_poem_snowwoman_recent = False
          default kokiri_poem_shadowman_recent = False
          default kokiri_poem_lights_recent = False
          default kokiri_poem_bang_recent = False
          default kokiri_poem_window_recent = False
          default kokiri_poem_time_recent = False
          default kokiri_poem_sun_recent = False
          default kokiri_poem_marble_recent = False
          default kokiri_poem_beach_recent = False

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
          default familyCheck_talkedDavid = False

          #CONVERSATION TRACKERS
          default kokiri_conversation = 0
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
          default callsMade = 0
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
          default dumboStoryTold  = False
          
          default burger_jokeFromAbigailTold = False
          default onlyDates = False
          default death_narration = ""
          default conversationtracker_mayo = False
          default conversationtracker_determinism = False
          default conversationtracker_crosser = False
          default conversationtracker_becomeGame = False
          default conversationtracker_nightmares = False
          
          default keySeenNow = False
          default keyGot = False
          default ending_check = ""
          default abbyCalled = False
          default lilaCalled = False
          default jamesCalled = False
          default davidCalled = False
          default policeCalled = False
          default rockMode_rockBand = False
          default rockModeBackToStart = False
          default reunion_davidPresent = False
          default reunion_lilaPresent = False

          #Beach
          default beachStart_doneBook = False
          default beachStart_doneDunes = False
          default beachStart_doneBeach = False
          default beachStart_doneFriterie = False
          default beachStart_doneIce = False
          default beachStart_doneCinema = False

          #QOL-settings:
          default no_nightmare = False
          default persistent.perm_nightmare = False
          default other_phone = 0
          default hypotheticalBurger = False
          default fakeBurger = False

          #Ghost_dialogue:
          default hidden_messages = [
               "I'm still here, waiting",
               "Do not believe your eyes.",
               "Don't trust them.",
          ]

          
     

     
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
          dev "And yet, I wonder, would that be what you are looking for?"
          dev "Would the meaning of this game that you might have formulated in your mind be better than the one it has?"
          dev "I guess there's only one way to find out [persistent.name]."
          dev "I wish you the best of luck one can find in a place like this..."
          $ persistent.fakeoutnar_tip = False


     label nameSelect:
          if not hasattr(persistent, "name"):
                    $ persistent.name = None
          if persistent.retry_counter == 0 and persistent.name == None or from_menu:
               
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
               
               if persistent.name == "Woodyoukindly?":
                    $ persistent.name = None
                    n "Cheatcode activated, enter your name."
                    #Gives you the progress right up until the forest.
                    $ progressUpToWoods()
                    jump nameSelect
               if persistent.name == "R0ck_0n!":
                    $ persistent.name = None
                    n "Cheatcode activated, enter your name."
                    $ persistent.rockMode = True
                    jump nameSelect
               

               if persistent.name == "Dev":
                    $ persistent.name = None
                    n "Cheatcode activated, enter your name."
                    $  _preferences.skip_unseen=True
                    $ allProgress()
                    $ persistent.canSave = True
                    jump nameSelect

               if persistent.name == "Curs3dkn0l3dg3":
                    $ persistent.name = None
                    n "Cheatcode activated. Enter your name."
                    $ persistent.perm_nightmare = True
                    $ allProgress()
                    jump nameSelect

               if persistent.name == "Tester" or persistent.name == "T3st3r":
                    $ persistent.name = None
                    dev "Tester mode activated. Please enter your name."
                    $ persistent.testmode = True
                    jump nameSelect
               
               if persistent.name == "Mal":
                    $ persistent.censor_mode = True
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

               if from_menu:
                    $ from_menu = False
                    if persistent.rockMode:
                         n "Test"
                         jump game_start
                         
                    
                       
          
              
             
          


label game_start:
     $ show_cinematic_bars(sides=["top", "bottom"], size=550, animate=False)
     pause 2
     $ hide_cinematic_bars(animate=True, duration=8, curve="ease")
     

     $ renpy.save_persistent() #This should save the persistent data.
     $ resetRegularFlags()
     $ updatePronouns()
  
     if persistent.polaroidTracker == True:
          $ persistent.tracker += 1
     if persistent.tracker > 3:
          $ persistent.polaroidTracker = False
 
 
     if persistent.lildeaths == 0:
          n "It is a beautiful day unlike any other."
          n "And while it may have something to do with waking up with warm sunbeams caressing your face and absurd amounts of cheese stuffed inside your mouth it's something else that makes the day even better, or should I say someone else?"
          n "Suddenly your phone begins to blare \"Baby it's cold outside\" even though it's nowhere near winter."
          n "That has to be [date_obj], you better pick up the phone."
     else:

          if not nightmare:
               if rockModeBackToStart == True:
                    n "It's a beautiful day, because it is not like the last one."
                    n "No more annoying rock puns."
                    n "I've never been more glad to get to narrate this part of the story."
               else:
                    n "It is a beautiful day like the previous one, exactly like the previous one."
               if persistent.testmode:
                    dev "[persistent.lildeaths] [persistent.date!c] deaths."
               if persistent.rockMode == True:
                    n "Actually... I'm not sure, something feels different."
                    n "Hang on, are you... are you a rock?"
                    n "You are!"
                    n "What is this? This is not part of the main story right?"
                    n "Suddenly your phone begins to blare \"Baby it's cold outside\" once again."
                    n "It's [date_obj]. You should pick up the phone."
                    n "You really should and you probably would, if you weren't a rock without hands that is."
                    n "Hang on, if you are a rock, am I jumping the shark to assume that [date_sub] also is a rock now?"
                    n "If [date_sub] really is, how is [date_sub] calling you?"
                    n "And why do the two of you even have human phones?"
                    n "I have so many questions..."
                    n "But let's stay on track as much as possible, what do you want to do now?"
                    menu:
                         "*Remember that all rocks have a telepathic network to communicate with eachother and use it to reach out to [persistent.date].*" if persistent.psychicConnection_knowledge:
                              n "Having been already familiar with your current situation you manage to relatively easily establish a connection with [persistent.date]."
                              l "Heya [persistent.name]!"
                              jump Game_start2
                         "*Struggle against your inescapable prison of a body and try to roll to the phone.*" if not persistent.psychicConnection_knowledge:
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
                                        
                                        menu:
                                             "...What? Psychic link? What are you talking about?":
                                                  l "Huh? Are you feeling alright [persistent.name]? It's pretty hard to forget that all sentient rocks have a psychic link to communicate..."
                                                  l "How else would we talk silly? With our mouths?"
                                                  n "You can hear [date_obj] chuckle in your mind."
                                                  n "I guess that would be impossible."
                                                  menu rockLinkChoice:
                                                       "Then why did you call me on your phone? Why do we even have phones?" if not persistent.psychicConnection_knowledge == True:
                                                            n "..."
                                                            n "Look player, I know it's weird."
                                                            n "But He was adamant about adding this, so it must mean something, right?"
                                                            n "I can't just be narrating the work of a madman..."
                                                            n "{size=*2.5}Right?{/size}"
                                                            n "So, maybe it's best if we don't question it too much, let's just pretend like you didn't ask that question in the first place."
                                                            $ persistent.psychicConnection_knowledge = True
                                                            jump rockLinkChoice
                                                            
                                                       "You're completely right, I guess I just forgot, silly me.":
                                                            n "Another soft chuckle in your mind."
                                                            n "It feels weird, cozy in a way, and yet slightly... invasive?"
                                                            n "Your mind is the only place that is truly fully yours, and now... it isn't anymore."
                                                            l "Don't even mention it [persistent.name], it can happen to anyone of us."
                                                            $ persistent.psychicConnection_knowledge = True
                                                            jump Game_start2
               else:
                    if not rockModeBackToStart:
                         n "Actually it's just the same day."
                         n "Maybe you can make it just a tiny bit different."
                    n "Your phone once again blares \"Baby it's cold outside\" even though it is anything but cold outside."
                    n "It's [date_obj], again."                  
          else:
               n "You awaken in cold sweat as your phone begins to blare \"Baby it's cold outside\" even though it's nowhere near winter."
               n "You had a terrible nightmare but you try to shake it off as best as you can."
               $ nightmare = False
     label phoneChoice:
          menu:
     
               "*Pick up the phone*":
                    jump Game_start2
               
               "*Do not pick up the phone*" if persistent.rejectPhone_Block == False:
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

               "Hey you, narrator. Give me the good ending where [persistent.date] survives. Or else I'm erasing all my progress." if persistent.threatenNarratorForEnding == True and persistent.lilithAliveAndRetriedCounter == 0 and not persistent.threatenNarratorForEnding_noUse:
                    jump threatenNarratorForEnding
          

               "Hey you, narrator. Give me the good ending where [persistent.date] survives and we still end up together. Or else I'm erasing all my progress." if persistent.threatenNarratorForEnding == True and persistent.lilithAliveAndRetriedCounter > 0  and not persistent.threatenNarratorForEnding_noUse:
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
                                   n "It is a loop after all, isn't it? So maybe it's only fitting."
                                   if persistent.lilithAliveAndRetriedCounter > 0: 
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
                                                                 n "I can't enter the Void yet, I still have so much things to talk about."
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
                                             
                                        "I doubt that other people are even playing this game if I am being honest.":
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
                    n "With [persistent.date]'s story about the \"monster\" underneath the bed still in your mind you decide to check underneath your own bed. "
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
                              n "I guess I'll allow it, after all, you found it fair and square."
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

          python:
               sync_pronoun_shorthands()
               sync_family_term_shorthands()
          
          if persistent.rejectPhone_Block and persistent.lildeaths == 0:
               n "Finally, now we finally can get started. No more stagefreight."
               n "Just you, the stage and your playwright."
               n "As all things are supposed to be."

          #Here you can see how you insert a name.
          if big_sis_mode == False:
               if callsMade == 1:
                    l "Welcome back [persistent.name]! So, like I was saying before, where do you want to go to today?"
               elif callsMade == 2:
                    l "Welcome back [persistent.name]."
                    l "{size=*0.5}That took you pretty long...{/size}"
                    l "So, where do you want to go to?"
                    l "{size=*0.5}I'll ask you again to refresh your memory.{/size}"

               else: 
                    if persistent.name == "Fartyfarty": 
                         l "Hey-"
                         l "[persistent.date] burst out into laughter."
                         l "Fartyfarty. Hahahahaha."
                         n "Don't worry, soon it will be out of [date_pos] system."
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
                         if not persistent.rockMode:
                              l "Hey [persistent.name]!"
                              l "It's me, [persistent.date]."
                              l "I'm just calling you to see where you'd like to go to for our date."
                         else:
                              l "I was just checking to see where you'd like to go for our date. "
                         l "I guess since you were so kind to let me come up with three suggestions I'll let you pick."
                         n "There's a certain kind of playfulness in [date_pos] voice, you can tell that [date_sub] [conj('date', 'is', 'are')] excited for your date."
                         l "So the three options you can pick are that one burger place I told you about, the Chinese restaurant or that one cute cafe I haven't checked out yet but heard some good things about."
          
          
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
               l "Oh I'm really sorry but my little [sis_sib], [persistent.date_sis], is calling. It's probably important so I will have to hang up for a bit. I'll call you back as soon as I can okay, [persistent.name]?"
               menu:
                    "Sure, take your time, I will be here when you call back.":
                         n "[date_sub!c] hung up."
                         n "After a few minutes your phone begins blasting \"Baby it's cold outside\" once more, you pick up as quickly as you can."
                         l "Hey [persistent.name], I'm back. I kind of have bad news for you..."
                         l "I won't be able to go on our date today, my [sis_sib] is heartbroken by a girl [sis_sub] had a crush on for a while now and I need to comfort [sis_obj]."
                         l "But we can go on our date at another time, I got to go now but I will call you back."
                         l "Take care [persistent.name] and goodbye."
                         n "[persistent.date_sis]'s plan worked exactly like expected. [persistent.date] survived the plane crash since [date_sub] [conj('date', 'was', 'were')] not there when it crashed and [date_sub] didn't die on your date since there wasn't any."
                         n "There also wasn't a date at another time since, again like [persistent.date_sis] expected, [persistent.date] forgot to call you back due to [date_pos] little [sis_sib]'s situation."
                         n "[date_sub!c] seemingly continued on with [date_pos] busy life, still attempting to enjoy life more by taking some time for [date_pred] to go on dates and the such."
                         n "From what you pick up here and there in random conversations [date_sub] [conj('date', 'seems', 'seem')] to be doing quite well for [date_pred]."
                         n "Now [date_sub] will probably be safe, as safe as a normal person is anyway."
                         menu: 
                              "Take care [persistent.date] and goodbye...":
                                   $ persistent.ending_abigailDistraction = True
                                   $ lilithAliveEnding = True
                                   $ ending_check = "abigailDistraction"
                                   $ persistent.lildeaths -= 1
                                   $ persistent.gallery_unlocked = True
                                   jump gameOver
                    
          


label phone_start_choices:

     if persistent.testmode:
          dev "Tester mode is currently enabled."
     if reunion_davidPresent or reunion_lilaPresent:
          n "The market square where the reunion will happen is very close to the Chinese restaurant, you probably should get [date_obj] to go there."

     menu:
 
          "How do burgers sound?" if not persistent.restaurant_subfolder or persistent.rockMode:
               jump burger_start

          "I heard the cafe has many exotic fish that swim around in aquariums. I'd like to go there to see them." if (not persistent.restaurant_subfolder and not persistent.cafe_taste_knowledge) or (persistent.rockMode and not persistent.cafe_taste_knowledge):
               jump cafe_start

          "I heard the cafe has many exotic fish that swim around in aquariums. You'll absolutely love them!" if (not persistent.restaurant_subfolder and persistent.cafe_taste_knowledge) or (persistent.rockMode and persistent.cafe_taste_knowledge):
               jump cafe_start

 
          "I'd like to go to the Chinese restaurant." if not persistent.restaurant_subfolder or persistent.rockMode:
               jump chinese_start
 
          "You know, I have changed my mind, can't we just go take a walk in the park or something?" if persistent.burger_death_1 and persistent.cafe_death_1 and persistent.chinese_death_1 and not persistent.locations_subfolder and not onlyDates and not persistent.rockMode:
               jump phone_otherPlans
 
          "I think it would be better if we didn't go on this date, for both of our sakes." if persistent.burger_death_2 and persistent.cafe_death_2 and persistent.chinese_death_2 and not persistent.other_subfolder and not onlyDates and not persistent.rockMode:
               jump phone_breakup
 
          "Actually, could we meet in the Kokiri forest?" if persistent.kokiri_knowledge and not persistent.locations_subfolder and not persistent.rockMode:
               jump kokiri_start
 
          "Hang on, I just need to make another quick call and then I'll be right back." if persistent.peeked_phone or persistent.kokiri_death_2 and not called_phone and not persistent.other_subfolder and not onlyDates and not persistent.rockMode:
               jump phone_callMenu
 
          "Would you like to go to the beach instead?" if persistent.beach_knowledge and not persistent.locations_subfolder and not persistent.rockMode:
               jump beach_start
          
        
 
 
          "*Pick one of the three restaurants.*" if persistent.restaurant_subfolder and not persistent.rockMode:
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
          #Subfolders for the menu are below this line (Make them jump to the normal code to make sure I don't need to copy-paste complex code over and over:
          "*Choose another location.*" if persistent.locations_subfolder and not persistent.rockMode:
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
 
 
          "*Say something else*" if persistent.other_subfolder and not onlyDates and not persistent.rockMode:
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
                                        l "I still miss [ghost_obj] very much and-"
                                        l "Hang on, how did you even know that? It's not like my family has been spreading the news ever since they moved."
                                        l "Have you... Have you been stalking me?"
                                        l "I'm sorry, I have no interest in dating a stalker, don't call me again or I'll have to get the police involved."
                                        jump phone_planeDeath

                                   "*Tell the untold story.*" if persistent.story_start_knowledge and persistent.story_medium_knowledge and persistent.story_end_knowledge:
                                        n "You tell [persistent.date] [date_pos] untold story. Well, now that I think of it, isn't it now [date_pos] told story?"
                                        n "Throughout the entire story [persistent.date] stayed extremely silent."
                                        n "When you are finished you can hear [date_pos] soft sobbing through the speaker of your phone."
                                        l "Sorry, I am a bit overwhelmed, just give me a quick minute to calm myself down."
                                        n "After five minutes you begin to hear commotion on the other side of the phone once again."
                                        l "That story, I've never told it to anyone, I haven't even written that down, I just kept repeating it over and over in my mind."
                                        l "I created it for my [ghost_sib] but [ghost_sub] never came home since then. You see, a car and..."
                                        n "[date_sub!c] [conj('date', 'begins', 'begin')] to sob again, this time louder."
                                        l "I'm sorry, I can't say it, even after all those years I just can't."
                                        l "How did you even know that story? Like I said earlier, I haven't shared it with anyone else and never wrote it down, it exist solely in my mind and I guess yours aswell now."
                                        n "You tell [persistent.date] about the loop you are trapped in and the many dates you've had together."
                                        n "You also tell [date_obj] about a few of the different deaths [date_sub] [conj('date', 'has', 'have')] suffered but try to not make your descriptions too gruesome."
                                        n "You continue."
                                        n "About all the experiences the both of you shared, some better than others."
                                        n "About the restaurants you've been to together."
                                        n "That you tried to warn [date_obj] to not go to one of those restaurants but that [date_sub] didn't trust you."
                                        n "That a version of [date_obj] from the future, or maybe a parallel timeline that diverted in a different direction, helped you and told you the story, broken down in three parts, one for each restaurant."
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
                                        n "[date_sub!c] [conj('date', 'does', 'do')]n't sound very amused, it doesn't take a detective to figure out why."
                                        l "{size=*0.5}Come on [persistent.date_nickname], you have to give it a shot, they seemed nice enough before, right?...{/size}"
                                        l "{size=*0.5}I owe it to myself to atleast try.{/size}"
                                        l "So, where do you want to go [persistent.name]?"
                                        n "You sense a slight change in [date_pos] voice, it sounds like [date_sub] [conj('date', 'is', 'are')] forcing it too much."
                                        $ love_points -= 1
                                        $ love_meter_updater(False)
                                        $ onlyDates = True
                                       
                                        jump phone_start_choices





label phone_breakup:
     l "Oh... really?"
     l "I'm sorry to hear that, but if you think it is for the best..."
     l "Can we still stay in touch with eachother?"
     n "You agree with [persistent.date] and still regulary text with [date_obj] and sometimes the two of you even meet up with eachother."
     n "However after a while the texts on both your and [date_pos] side begin to be less and less frequent and you begin to only meet once in a month."
     n "Once in a month changes to once in every season to once every year untill the meetings stops completely."
     n "After a few years that you've forgotten about [persistent.date] until you stumble upon [date_pos] social media page."
     n "[date_sub!c] [conj('date', 'does', 'do')]n't have that much pictures on [date_pos] account but the ones [date_sub] [conj('date', 'has', 'have')] on there are beautifully shot."
     n "On a few pictures [date_sub] [conj('date', 'stands', 'stand')] next a blonde man while they both have the widest smiles you have ever seen."
     n "Apparently the man is called Ron, he is a semi-profesional photographer and his pictures surely show for it."
     n "[persistent.date] and Ron got two kids that look like they had not a single thing to worry about."
     play music game_over
     n "Looking at the pictures you can't help but feel tears coming up, you tried your best to move on but apparently that didn't work all too well."
     n "You know that this was probably the best thing to do, to keep [persistent.date] safe and sound."
     n "But something deep inside you keeps wondering if there wasn't a way where you two could be together while [date_sub] would be safe."
     n "There must be a way right?"
     $ persistent.ending_breakup = True
     $ lilithAliveEnding = True
     $ ending_check = "breakup"
     $ persistent.lildeaths -= 1
     $ persistent.gallery_unlocked = True
     jump gameOver


label phone_callMenu:
     $ playerCalledSomeone = True
     if callsMade == 0:
          l "Oh, no problem [persistent.name]. Just give me a call when you're done."
          n "You agree with [date_obj] and hang up the phone."
          p "Now I just need to call..."
     if callsMade == 1:
          p "Alright, now I should probably call..."
     if callsMade == 2:
          n "You should probably call [persistent.date] back now instead of calling everyone but [date_obj]."
          $ love_points = -1
          $ love_meter_updater(False)
          jump Game_start2
     
     menu callMenu:
          "[persistent.date]" if callsMade == 1:
               n "That's probably a good idea. We wouldn't want to leave [date_obj] hanging."
               jump Game_start2
          "the police." if persistent.kokiri_death_2 and not policeCalled:
               $ callsMade += 1
               $ policeCalled = True
               jump phone_call_police
  
          "[persistent.date_sis]." if persistent.abigail_call_knowledge and not abbyCalled:
               $ callsMade += 1
               $ persistent.playerCalledAbigail = True
               $ abbyCalled = True
               if persistent.restrainingorderfamily_knowledge == True:
                    
                    #Karma
                    $ persistent.restrainingorderfamily_violation_counter += 1
               jump phone_call_abigail
  
          "[persistent.date_dad]." if persistent.david_call_knowledge and not davidCalled:
               $ callsMade += 1
               $ persistent.playerCalledDavid = True
               $ davidCalled = True
               if persistent.restrainingorderfamily_knowledge == True:
                    #Karma
                    $ persistent.restrainingorderfamily_violation_counter += 1
               jump phone_call_david
  
          "[persistent.date_ghost]." if persistent.james_call_knowledge and not jamesCalled:
               $ callsMade += 1
               $ jamesCalled = True
               $ persistent.playerCalledJames = True
               if persistent.restrainingorderfamily_knowledge == True:
                    #Karma
                    $ persistent.restrainingorderfamily_violation_counter += 1
               jump phone_call_james
  
          "[persistent.date_mom]." if persistent.lila_call_knowledge:
               $ callsMade += 1
               $ persistent.playerCalledLila = True
               if persistent.restrainingorderfamily_knowledge == True:
                    #Karma
                    $ persistent.restrainingorderfamily_violation_counter += 1
               jump phone_call_lila

 
label phone_call_police:
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
                    n "The man hangs up the phone."
                    jump phone_callMenu
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
     if phone_caller == persistent.name:
          n "[persistent.date_sis] turns quiet for a moment."
          a "Oh right, now I remember! [persistent.date_nickname] told me that [date_sub] would go on a date with you today."
          a "So, why are you calling me? Shouldn't you be calling with [date_obj] right now?"
          menu:
               "This might sound really weird but... your [date_sib] keeps dying on our dates by things out of my control and when that happens I have to relive the same day. I am calling in the hopes that maybe you could slightly help me out to save [date_obj].":
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
                         a "I feel so dumb for saying it but if [persistent.date_nickname] is really suffering like you told me I'd gladly feel dumb to save [date_obj]."
                         a "The phrase goes: \"Drown the raven that cannot burn.\""
                         $ persistent.drownRaven_knowledge = True
                         a "I'm going to hang up now. If you ever want to call me again do it before this moment and not after it. Hopefully I won't hear from you, otherwise that means [persistent.date] is truly in danger."
                         n "[sis_sub!c] hung up the phone."
                         jump phone_callMenu



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
 
                              "I actually have no proof besides the number thing." if persistent.abigail_numberfakeout and abby_phone_counter == 0:
                                   a "..."
                                   a "You really thought that would somehow win me over?"
                                   n "You hear laughing on the other side of the phone."
                                   a "Well, I suppose if what you are saying is true you will be able to gather better proof, right?"
                                   a "You're lucky [persistent.date_nickname] really needs this date, otherwise I'd probably tell [date_obj] all about this."
                                   a "Just try to act normal to [date_obj], alright? [date_sub!c] [conj('date', 'do', 'does')]n't deserve to hear any of this."
                                   a "Or maybe [date_sub] will grow to understand that [date_sub] [conj('date', 'do', 'does')]n't need people like you."
                                   a "Now I have to go, don't ever call me back"
                                   n "[sis_sub!c] hung up on you, this is going to be really awkward on family gatherings if you ever get that far."
                                   jump phone_callMenu

                              "I actually don't have any proof left" if persistent.abigail_numberfakeout and abby_phone_counter > 0:
                                   a "I see..."
                                   a "It still doesn't sound very plausible but there is a chance you might be telling the truth."
                                   a "If you really can redo today, come back with more proof, alright?"
                                   a "I can't believe I'm even entertaining the thought that this is real, but if it somehow ends up helping [persistent.date_nickname], then it's worth a shot."
                                   a "But for now, don't leave my [date_sibShort] waiting, alright [persistent.name]?"
                                   n "[sis_sub!c] just hung up on you. You should indeed not let [persistent.date] wait much longer."
                                   jump phone_callMenu

 
 
                              "So a priest, a monk and a rabbit enter a bar. Says the rabbit :\"Whoops, did you slip your tongue there [persistent.name]?\"" if persistent.abigail_numberfakeout and persistent.joke_knowledge and not abby_phone_joke :
                                   n "You tell [sis_obj] about how [persistent.date] was laughing for almost a full hour because of that joke when [persistent.date_sis] told it to [date_obj]."
                                   a "I mean, I just found that joke on the internet..."
                                   a "Maybe you just got lucky and found it aswell, or you somehow managed to check my browser history which would be really weird."
                                   a "Although I got to admit that [date_obj] laughing for about an hour at my joke is a pretty specific detail... "
                                   $ abby_phone_counter -= 1
                                   $ abby_phone_joke = True #I'll use this to make sure that you can't select the same choice two times.
                                   jump phone_call_Abigail_convinceHer
 
 
 
                              "I know about Mr. Bunfluff the pink bear and the time he scared both [persistent.date] and you in the middle of the night." if persistent.abigail_numberfakeout and persistent.bedcheck_knowledge and not abby_phone_bunfluff:
                                   a "I mean [persistent.date] could have told that story to one of [date_pos] friends and they could have then told it to you."
                                   a "It's not impossible for you to know about Mr. Bunfluff."
                                   a "Although [persistent.date] is not someone who would tell a story like that to a lot of people... "
                                   $ abby_phone_counter -= 1
                                   $ abby_phone_bunfluff = True #I'll use this to make sure that you can't select the same choice two times.
                                   jump phone_call_Abigail_convinceHer
 
  
                              "I know about your Quest games. *Describe plot*" if persistent.abigail_numberfakeout and persistent.quest_knowledge and not abby_phone_games:
                                   a "That's weird, I didn't think [persistent.date] mentioned my games to anyone."
                                   a "Maybe [date_sub] did after all, there is no way to really know..."
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
                                             "Could you come up with something so [date_sub] [conj('date', 'does', 'do')]n't go on this date with me and also [conj('date', 'does', 'do')]n't stay at [date_pos] house?" if persistent.plane_knowledge: 
                                                  jump phone_call_abigail_topics_distractionforlilith
     
     
     
                                             "I spoke to [persistent.date_dad] in a previous cycle. [dad_sub!c] told me that no one loves or misses [dad_obj] after what [dad_sub] did." if persistent.david_nolove_knowledge:
                                                  jump phone_call_abigail_topics_spoketodavid_noonelovesdavid
     
     
     
                                             "I spoke to [persistent.date_dad] in a previous cycle. [dad_sub!c] told me [dad_sub] [conj('dad', 'blames', 'blame')] [dad_pred] for [persistent.date_ghost]' death and thinks [persistent.date] and [persistent.date_mom] do aswell." if persistent.david_blame_knowledge:
                                                  jump phone_call_abigail_topics_spoketodavid_davidblameshimself

                                             "Do you have a teacher called Sam? Could you tell me something that they and close to no one else would know?":
                                                  a "And this is going to save [persistent.date_nickname] how exactly?"
                                                  a "Still, I suppose it is important, right? Otherwise you wouldn't ask me."
                                                  a "Let's see... something almost only Sam would know... but it also has to be something that is verifiable."
                                                  a "...Perhaps my score for their class that semester would work? I got a fourteen out of twenty."
                                                  $ persistent.lilaCallRecievedAbbyProof_knowledge = True
                                                  a "Hope that helps."
                                                  menu:
                                                       "It does, thank you.":
                                                            a "I wouldn't know how it possibly could, but that's good to hear [persistent.name]."
                                                            a "Now don't leave my [date_sibShort] waiting and try your best to save [date_obj], alright?"
                                                            a "Goodbye."
                                                            n "And with that [sis_sub] hung up the phone."
                                                            jump phone_callMenu

                                             "Do you know anything about an opportunity you might not be taking related to a game design competition?" if persistent.lilaToldAbbyOpportunity_knowledge:
                                                  a "..."
                                                  a "How do you know about that?"
                                                  a "I get it, through the timeloops and all that, but who told you?"
                                                  menu:
                                                       "Your [mom_parShort] told me.":
                                                            a "You have been talking to [mom_parShort] aswell?"
                                                            a "I suppose that does make sense, if you are using my help, why wouldn't you be using hers?..."
                                                            a "But scratch that, she told you about the competition?"
                                                            a "She knows about it too? How?"
                                                            menu:
                                                                 "She only partially does, Sam sent [mom_obj] a mail with a vague mention of it. They were going to discuss it over the phone though.":
                                                                      a "I see. So she does not yet know entirely?"
                                                                      a "...Is it bad for me to be slightly glad this day is looping now?"
                                                                      a "Don't get me wrong, I hope you manage to break the loop, but this way my secret might be last longer than it would otherwise."
                                                                      a "And if that is the case I'd rather keep it that way for now. I'm not ready yet to discuss it with you, or with anyone for that matter."
                                                                      a "I am going to hang up now. Goodbye [persistent.name]."
                                                                      jump phone_callMenu

                                                                 "Sam told [mom_obj] the entire thing (Lie)":
                                                                      a "Really? So she knows about the job offer I got from winning that competition? And you do aswell?"
                                                                      menu:
                                                                           "Yup, and I was wondering why you didn't want to take that opportunity.":
                                                                                a "..."
                                                                                a "This better be useful to somehow save [persistent.date_nickname] [persistent.name]."
                                                                                n "[sis_sub!c] [conj('sis', 'lets', 'let')] out a deep sigh."
                                                                                a "I didn't take the job opportunity because I would have to move away from my hometown."
                                                                                a "The game design studio is pretty far away from here, about a 12 hour drive. So that would force me to get an apartment close to the job and far away from both [mom_parShort] and [persistent.date_nickname]."
                                                                                a "I'm not ready for that yet. Not ready to let them go like that."
                                                                                a "But they would want me to. They would say that it is an amazing opportunity I have to take and that we would still keep contact, just in a different way."
                                                                                a "Which is precisely why I tried to hide this from them. Although the truth was bound to come out eventually..."
                                                                                menu:
                                                                                     "I get that it might seem scary now, but sooner or later you will have to let go, right?":
                                                                                          a "I don't know about that..."
                                                                                          a "I'm not at the point yet to even really consider it honestly."
                                                                                          a "The closest I probably could go to that is loosening my grip a little. But letting go that much... that is scary to me."

                                                                                     "Wait, but there is no college near this town in the slightest. Aren't you already used to not being home every day?":
                                                                                          a "It is true that there really isn't any college closeby here, but there is one about a 2 hour cardrive away from here."
                                                                                          a "I go to that one, so instead of staying in a dorm I just drive back and forth each day."
                                                                                          menu:
                                                                                               "But that's 4 hours total each day spent just driving. Wouldn't it have been less of a hassle to stay in a dorm?":
                                                                                                    a "It probably would, then I might even have gotten used to being a bit further away from [mom_parShort] and [persistent.date_nickname]."
                                                                                                    a "But that is the thing about letting go isn't it? We do whatever we can so we don't have to, even if it is inconveniencing or painful."

                                                                                     "So the distance is one factor why you don't follow through with the offer, but there is also another reason, isn't there?":
                                                                                          #If you know about her masking make this choice an option.
                                                                                          a "..."
                                                                                          a "I suppose there is no hiding things from you, is there, [persistent.name]?"
                                                                                          a "Another part of it is that I don't feel like I am good enough to join the game design studio."
                                                                                          a "I know they saw something of value in the writing of my games but even if I am being told by others it is there I myself can't see it yet."
                                                                                          a "The truth is, lately I have been feeling like I am a fraud, a liar. Not just about the quality of my writing, but also about the person I am."
                                                                                          a "I think I would only bring down the studio by being in it, as if I am a parasite draining it's blood until there is nothing left but a drained carcass."
                                                                                          a "And yet, I want to go there, I want to work in the game design studio, that has been my dream for so long after all. But I know that if I were to go I would feel it, the lifeblood of the studio on my tongue, as I leave no drop of it behind."
                                                                                          a "After all, ruining the studio is not something I would do out of malicousness, moreso out of sheer incompetence. I just am not ready yet. I'm not sure if I'll ever be honestly."
                                                                                
                                                                                a "Anyway, that's all I want to share about it. It's quite personal and if I'm being honest I can't see how this could ever possibly save [persistent.date]."
                                                                                a "Still, I am not the one stuck in the loop am I? So maybe I'm missing something."
                                                                                a "Good luck and goodbye [persistent.name]."
                                                                                n "And with that she hung up the phone."
                                                                                jump phone_callMenu

     
                                             "Actually I would just like to talk about something else.":
                                                  a "Sure, if that somehow helps [persistent.date_nickname] that's fine by me."
                                                  menu abigail_somethingElse:
                                                       "[persistent.date] and you talked about your emotional mask in a previous loop, the façade that you put up not to worry anyone." if persistent.kokiri_abbyMasking_knowledge == True:
                                                            a "We talked about that?..."
                                                            a "I guess we did, since you know."
                                                            a "Though if you want to talk about it with me I'd rather not."
                                                            a "We maybe already talked before during one of your previous loops but to me you're still nearly a total stranger."
                                                            a "Although it is... interesting to hear that me and [persistent.date_nickname] had such a chat in a previous loop."
                                                            a "Don't get me wrong, [date_sub] really [conj('date', 'cares', 'care')] deeply about me, [date_sub] [conj('date', 'tries', 'try')] to express that as best as [date_sub] can. But we never really had a chat like that before."
                                                            n "It's quiet on the other end for what feels like a minute."
                                                            a "Alright, you got me curious [persistent.name], how did our conversation roughly go?"
                                                            menu:
                                                                 "[date_sub!c] said you were coming across even more cheerful than normal. That something seemed off.":
                                                                      a "...And what did I answer?"
                                                                      menu:
                                                                           "That you were feeling insecure about your writing.":
                                                                                a "I see... that indeed is true."
                                                                                a "I'll spare you the details, since you've already heard them before. But also because I don't want to go over them right now."
                                                                                a "What interests me more is how [date_sub] responded."
                                                                                menu:
                                                                                     "[date_sub!c] said that your art is genuinely really great and that [date_sub] [conj('date', 'hopes', 'hope')] one day you see it the same way. That there is always room for improvement no matter how good you are but that you have to call your art finished eventually so it can be seen by others.":
                                                                                          a "I guess [date_sub] [conj('date', 'is', 'are')] right. I have to let my art go at some point if I want other people to see it." 
                                                                                          a "Still, to tell you the truth, I don't think I'm ready yet for it to be seen. Letting go is scary isn't it? The moment I do so it's out of my control."         
                                                                                          a "I'd prefer to hold on just a little longer..."    
                                                                                          a "Although I'm glad [date_sub] [conj('date', 'seems', 'seem')] to like my writing at the very least, it makes me feel like I could be onto something."                                                  
                                                                                          a "..."
                                                                                          a "Did I say anything else?..."
                                                                                          menu:
                                                                                               "You didn't.":
                                                                                                    n "You hear [sis_obj] let out a deep breath of relief, or is it a sigh of dissapointment?"
                                                                                               "You also said you were unsure of yourself, as if you are bad at being you.":
                                                                                                    a "...I did?..."
                                                                                                    a "What did [date_sub] say to that?"
                                                                                                    menu:
                                                                                                         "That people are complex tapestries of overlapping and sometimes contradicting things. That those tapestries keep changing, and that it is okay for them to do so. That no matter how much you change, you'll always be [date_pos] [sis_sib].":
                                                                                                              n "For a moment it's completely quiet on the other side of the line."
                                                                                                              a "...I-I have to think about this for a moment."
                                                                                                              a "Goodbye [persistent.name]."
                                                                                                              a "...And thank you."
                                                                                                              n "With that [sis_sub] hung up the phone."
                                                                                                              jump phone_callMenu
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
                                                                      n "For a moment it grows quiet on the other side of the phone as [persistent.date_sis] seemingly is lost in thought."
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
                                                                                a "Anyway, I hope you got enough info out of that to somehow help [persistent.date_nickname]."
                                                                                a "{size=*0.5}Although I'm not sure how that could possibly help.{/size}"
                                                                                a "I have to go now. If you need anything else just call me on your next try. But let us hope you won't need a next one."
                                                                                a "Good luck and goodbye [persistent.name]!"
                                                                                a "Keep [persistent.date_nickname] safe will you?"
                                                                                n "And with that [sis_sub] hung up."
                                                                                jump phone_callMenu
                                                            
                                                                           "I see, and what are those games about if you don't mind me asking?" if abby_askedAboutGameTheme:
                                                                                n "It's quiet once again, but this time it's different."
                                                                                n "[sis_sub!c] [conj('sis', 'is', 'are')]n't thinking about what to say, [sis_sub] [conj('sis', 'is', 'are')] trying not to answer."
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
          n "Just like that [sis_sub] hung up on you."
          n "Maybe you should try using your real name? With a bit of luck [persistent.date] has already spoken about you to [date_pos] [sis_sib]."
          jump phone_callMenu

label phone_call_abigail_topics_distractionforlilith:
     a "Sure I can but why can't [date_sub] just stay home?"
     if persistent.ending_breakup == True:
          n "Yes player, why can't [date_sub] just stay home?"
          n "You know [date_sub] [conj('date', 'is', 'are')] safe if you just cancel the date, right?"
          n "Are you doing this because you hope [date_sub] won't end up with Ron?"
          n "[date_sub] [conj('date', 'was', 'were')] perfectly happy then, and yet you came back, looking for another solution."
          n "Interesting..."
          n "Or is it not about that?"
          n "Are you doing this so you don't have to cancel the date yourself?"
          n "Or where you just curious about what would happen if you chose that option?"
     n "You inform [persistent.date_sis] about the plane that has crashed into [persistent.date]'s house before and that it will crash into [date_pos] house again and again."
     a "..."
     a "I see, this is too ridiculous to even make up."
     a "{size=*0.5}What have you gotten yourself into [persistent.date_nickname]?...{/size}"
     a "I don't like to lie to [date_obj] but if it saves [persistent.date_nickname] I suppose I could act like I was rejected by a girl I liked and just need some support from [date_obj].
     I'm sure that will trigger [date_pos] \"Big [date_sibShort] mode\" and then [date_sub] will come rushing to me."
     a "[date_sub!c] [conj('date', 'has', 'have')] a problem of almost never putting [date_pred] first but I guess this time that's pretty handy for us."
     a "Of course that will mean that your date won't go as planned."
     a "Knowing [date_obj] there is a pretty big chance [date_sub] will forget about the date. [date_sub!c] [conj('date', 'means', 'mean')] well, but [date_sub] [conj('date', 'is', 'are')] pretty bad with things like that."
     menu:
          "As much as this pains me, it's for the best. [date_sub!c] will be safer that way.":
               a "Thank you, [persistent.name], I'll try my best not to let your sacrifice go to waste."
               a "I got to call [date_obj] now, goodbye and take care."
               menu:
                    "Take care aswell, bye.":
                         n "[sis_sub!c] hung up."
                         $ big_sis_mode = True
                         jump phone_callMenu


label phone_call_abigail_topics_spoketodavid_noonelovesdavid:
     a "That's absurd! I still love [dad_obj]... I also still miss [dad_obj]."
     a "I mean, a [sis_child] needs [sis_pos] [dad_parShort], right?"
     a "[mom_parShort!c] and [persistent.date_nickname] are pretty mad because [dad_sub] left us but honestly I'm more sad because of it."
     a "I was nine when [dad_sub] left..."
     a "There were so many things I needed help with that [dad_sub] couldn't teach me."
     a "I can't even fully remember [dad_obj], just small bits and pieces. I'd like to make new memories of [dad_obj]."
     a "It has been ten years and honestly I still need [dad_obj]. I don't hold a grudge against [dad_obj] or anything, I'd even be happy if [dad_sub] decided to come back."
     n "[persistent.date_sis] pauses for a moment."
     a "Could you maybe tell [dad_obj] that the next time you relive this day? "
     $ persistent.david_love_knowledge = True
     menu:
          "I will.":
               a "Thank you [persistent.name]."
               a "We probably shouldn't leave [persistent.date] waiting any longer though. Good luck trying to save [date_obj] and also don't forget to have fun alright?"
               n "[sis_sub!c] hung up."
               jump phone_callMenu

label phone_call_abigail_topics_spoketodavid_davidblameshimself:
     a "That's ridiculous!"
     a "No one blames [dad_obj] for [persistent.date_ghost]' death."
     a "[mom_parShort!c] and [persistent.date_nickname] are mad at [dad_obj] because [dad_sub] left us, not because of [persistent.date_ghost] death."
     a "[dad_sub!c] couldn't possibly have predicted what happened. I'm sure [dad_sub] [con('dad', 'has', 'have')] wished that [dad_sub] could, so [dad_sub] had a chance to prevent it."
     a "Could you tell [dad_obj] that I don't blame [dad_obj] and that I'm sure [mom_parShort] and [persistent.date_nickname] don't either?"
     menu:
          "I will.":
               a "Thank you [persistent.name]."
               a "We probably shouldn't leave [persistent.date] waiting any longer though. Good luck trying to save [date_obj] and also don't forget to have fun alright?"
               n "[sis_sub!c] hung up."
               jump phone_callMenu

                                        


    


label phone_call_david:
     $ persistent.familyContacted = True
     d "Hello, who am I speaking to?"
     $ phone_caller = renpy.input("Enter your name.")
     $ phone_caller = phone_caller.strip()
     $ phone_caller = phone_caller.capitalize()
     d "[phone_caller]? Well I'm not interested in what you're selling so thank you very much but I'm going to hang up no-"
     menu:
          "Don't hang up! [persistent.date] asked me to call you. (Lie)":
               n "You hear the man laugh."
               d "I very much doubt that. Nobody loves me after what I did to them, especially not [date_obj]. And who can blame them?"
               d "It should have been me instead of [ghost_obj], then all of them would be much happier."
               d "Now I'm going to hang up. Goodbye [phone_caller]"
               n "True to [dad_pos] world [persistent.date_dad] hung up."
               $ persistent.david_nolove_knowledge = True
               jump phone_callMenu
  
          "[persistent.date_sis] still loves and misses you. [sis_sub!c] would be happy if you come back." if persistent.david_love_knowledge:
               n "You hear the man sigh."
               d "Poor [persistent.date_sis_nickname]..."
               d "[sis_sub!c] [conj('sis', 'was', 'were')] too young to remember me for the monster I truly was and [sis_sub] had to grow up without a father."
               d "I ruined my entire family and then I fled like a coward, thinking things would get better for them."
               n "[persistent.date_dad] quiets, seemingly waiting for a response from you."
               menu:
                    "Hang on, you said that you ruined your family and then left them. What caused that?" if persistent.david_blame_knowledge == False and persistent.brother_knowledge == False :
                         label phone_call_david_whatHappenedBeforeHeLeft:
                              d "You don't know?"
                              d "The day that [persistent.date_ghost]..."
                              d "The day I gave [ghost_obj] an old polaroid camera of mine."
                              d "[ghost_sub!c] loved that thing, ran all over the place taking pictures with it."
                              d "To the point [ghost_sub!c] didn't notice the car coming from aroundthe bend of the road as [ghost_sub] stood there to better photograph the potato fields."
                              d "It absolutely destroyed me but  even more so [persistent.date] since they were really close. [date_pos!c] [mom_par], [persistent.date_mom] was of course also devasted at the loss of one of [mom_obj] children."
                              d "Their anger towards me built up so much I couldn't face them anymore."
                              d "They didn't deserve to have to live with [persistent.date_ghost] [ghost_pos] killer. If I wouldn't have given [ghost_obj] that camera [ghost_sub] would still be alive..."
                              d "Now I live in a hotel close to our old home. Every single day I have hated myself for wanting to come back to my family and hated myself for staying here."
                              $ persistent.david_blame_knowledge = True
                              menu:
                                   "Do you really think they blame you for [ghost_pos] death?":
                                        d "Of course. Even I am blaming myself for it, so why wouldn't they?"
                                        d "... this is getting a bit too much for me. I think I'll just hang up the phone."
                                        d "Goodbye [persistent.name]."
                                        n "[persistent.date_dad] hung up."
                                        jump phone_callMenu
                    "*Feign ignorance* Hang on, you said that you ruined your family and then left them. What caused that?" if persistent.david_blame_knowledge == True or persistent.brother_knowledge == True:
                         jump phone_call_david_whatHappenedBeforeHeLeft
          
                    "Well, it seems like things were pretty hard for them. [persistent.date]'s [mom_parShort] even had to take a second job just to make ends meet." if persistent.lilaWorkedTwoJobs_knowledge:
                         d "What- She did? What happened to the money I gave [mom_obj]?"
                         menu:
                              "What money?":
                                   d "Each week I give [mom_obj] as much money as I can afford to in an effort to still somehow support my family."
                                   d "So to hear that apparently isn't enough is very strange. Especially [mom_obj] having take up a second job."
                                   d "It's not like [mom_sub] wouldn't tell me if that was the case, right? Right?..."
                                   d "I never changed my phone number after all."
                                   d "{size=*0.5}There was always a part of me that was hoping [mom_sub]'d call.{/size}"
                                   d "{size=*0.5}Still, I'm not sure if I would have dared pick up.{/size}"
                                   d "Did [mom_sub] somehow get into debt? That's the only reason I could see [mom_obj] need a second job."
                                   d "[mom_sub!c] can be overly trusting, maybe that's the cause?"
                                   n "You can hear [persistent.date_dad] sigh on the other side of the phone."
                                   n "[dad_sub!c] utters something, it's so soft and quiet it almost blends into the white noise of the background."
                                   d "{size=*0.5}What did you get yourself into [persistent.date_mom]? All that stress. I wish you didn't feel like you couldn't tell me...{/size}"
                                   d "{size=*0.5}I wish that I could have helped more.{/size}"
                                   d "{size=*0.5}I wish I would have stayed by your side.{/size}"
                                   n "You pick up on soft sobbing, slowly growing in intensity as it drowns out the background noises more and more."
                                   d "I'm sorry [phone_caller], I..."
                                   n "[dad_sub!c] [conj('dad', 'trails', 'trail')] off for a moment, as the words die out the sobbing becomes louder once more."
                                   n "You hear the man try to collect [dad_pred] by taking a deep breath."
                                   d "I just can't do this anymore. I need to go."
                                   n "[dad_sub!c] hung up on you."
                                   $ persistent.davidPayedMoney_knowledge = True
                                   jump phone_callMenu
  
          "[persistent.date!c] is not mad because of [persistent.date_ghost], [date_sub] [conj('date', 'is', 'are')] just mad at you for leaving your family. [date_sub!c] might even consider forgiving you if you give a good apology." if persistent.david_apology_knowledge:
               d "...Really? I- I can't believe it. All this time..."
               d "...I hurt [date_obj] so much, all of them, while trying to do the exact opposite."
               d "The truth is, I don't deserve their forgiveness, but I have been such a coward for so long..."
               d "I don't think I can break out of it just yet, but to do nothing would make me hate myself even more."
               d "Could you perhaps give [date_obj] my apology?"
               menu:
                    "I will, just tell what to tell [date_obj].":
                         d "I want to tell [date_obj] that nothing I could say would ever make up for what I did."
                         d "That every day I am beating myself up for my decision."
                         d "I was a coward, I still am by not facing [date_obj] directly."
                         d "I wanted to come back to them every single day, even now."
                         d "However something inside me felt they were better off without me."
                         d "It was selfish to listen to that voice. I should have told my family."
                         d "They'd have understood better than anyone else, as they also lost [ghost_obj] that day."
                         d "Instead I isolated myself, dealing with it on my own. Forcing them to go through all of this without me."
                         d "I'm deeply sorrythat [persistent.date] had to feel like [date_pos] own [dad_par] abandoned [date_obj]."
                         d "No child deserves to go through such pain. My family lost two people when [persistent.date_ghost] died and while just losing one was hard enough."
                         d "I can't undo the wounds I have caused, but I do hope I could, if my family allows me to, try mending them."
                         $ persistent.david_apology_made_knowledge = True
                         d "Thank you [persistent.name], I won't take any more time as this is already more than I deserve. Goodbye."
                         n "With that [dad_sub] hung up the phone."
                         jump phone_callMenu

          "Look. It doesn't matter who I am. All that matters is your family needs you. They don't blame you for [persistent.date_ghost]'s death. [persistent.date_sis!c] is trying to cling onto the pieces of you [sis_sub] still remembers and [persistent.date_mom] would rather have you back than your money." if persistent.lilithOpenToReunion_knowledge:
               d "..."
               n "Silence, it seems you have [dad_pos] attention."
               menu:
                    "They hurt, but not because they hate you, quite the opposite. Even [persistent.date] although [date_sub] would never admit it. Still, even [date_sub] [conj('date', 'is', 'are')] open to a reunion. I can give you a second chance, just go to market square.":
                         #TODO: Write this out a bit more later
                         d "I- I'm not sure what to say. There has not been a day where I didn't want to go back, but also not one where I felt it wouldn't pain them more."
                         d "I suppose that second part is selfish, because I did not dare face them again."
                         d "However if I don't take this second chance I'll forever regret it. I just hope I can mend the wounds more than I'll rip them open again."
                         d "Whoever you are, I cannot thank you enough for this. I won't take up anymore of your time since this is already more than I deserve. Goodbye."
                         n "With that [dad_sub] hung up the phone."
                         $ reunion_davidPresent = True
                         jump phone_callMenu


label phone_call_james:
     if persistent.met_james == False:
          if persistent.brother_knowledge == True:
               $ mysteriousCallerName = "???"
          else: 
               $ mysteriousCallerName = persistent.date_ghost
          q "Yo, who is this?"
          $ phone_caller = renpy.input("Enter your name.")
          $ phone_caller = phone_caller.strip()
          $ phone_caller = phone_caller.capitalize()
          q "[phone_caller] eh? Sorry, that doesn't really ring a bell."
          
          menu:
               "You don't know me. I am a friend of [persistent.date]." if not persistent.jamesFakoutNumber_knowledge and not persistent.brother_knowledge:
                    q "[persistent.date!c]? That also doesn't seem to ring a bell so I think you might have the wrong number."
                    q "For some reason that happens a lot with me, usually one particular number."
                    q "Although they tend to hang up before I can even say anything. Anyway, I have to go now, take care."
                    n "He hung up."
                    n "You are very confused by what you were just told."
                    n "Whoever this person you called was, they weren't [persistent.date_ghost]. They don't even know [persistent.date]."
                    n "Then why did [persistent.date] save them as \"[persistent.date_ghost]\" on her phone? Why [conj('date', 'does', 'do')] [date_sub] have their number at all?"
                    if persistent.lilithKeepsCalling_knowledge == False:
                         n "You also can't help but think of the number that keeps calling the person you just talked to."
                         n "Could it perhaps be [persistent.date]?"
                         $ persistent.lilithKeepsCalling_knowledge = True
                    n "This whole ordeal leaves you with more questions than answers, you should probably ask [date_obj] about it sometime soon."
                    

               "[persistent.date_ghost]? Aren't you supposed to be dead?" if not persistent.jamesFakoutNumber_knowledge and persistent.brother_knowledge:
                    q "Well I'm not [persistent.date_ghost] man and last time I checked I sure as hell wasn't dead."
                    q "I keep getting called randomly by the same number and now this?"
                    q "You're freaking me out, I'm going to hang up now."
                    n "The person, who you now know isn't [persistent.date_ghost] true to his word does."
                    if persistent.keptJamesNumber_knowledge == False:
                         n "It seems like [persistent.date] kept [date_pos] [ghost_sib]'s number in [date_pos] phone, perhaps as a sort of memento?"
                         $ persistent.keptJamesNumber_knowledge = True
                    if persistent.lilithKeepsCalling_knowledge == False:
                         n "You also can't help but think of something the person you called told you, someone keeps calling his number, the same person."
                         n "It's very possible it's [persistent.date]. Maybe you should ask [date_obj] about it sometime soon."
                         $ persistent.lilithKeepsCalling_knowledge = True

               "I think I have the wrong number then, sorry to waste your time." if persistent.jamesFakoutNumber_knowledge:
                    n "You hang up."
                    jump phone_callMenu

          if not persistent.jamesFakoutNumber_knowledge:
               $ persistent.jamesFakoutNumber_knowledge = True

          if persistent.kokiri_knowledge and persistent.kokiri_death_1:
               n "The best place to ask [date_obj] about it would probably be the kokiri forest."
               n "Yet you are sure [date_sub] won't be pleased to know that you looked through [date_pos] phone."   
          else:
               n "The only question is how you would possibly bring it up, after all you had to go through [date_pos] phone to even discover all of this."
               n "You decide it's better to keep this to yourself until you find a way to ask [date_obj]."
          jump phone_callMenu
     else:
          $ called_James = True
          j "Ah, welcome [persistent.name]. I see you have managed to get my number?"
          j "Well it used to be my number, but you can still reach me through it."
          j "Let me first transport you back to the end though, that way we can talk more easily."
          n "Right as [ghost_sub] spoke those words you feel yourself begining to leave your body behind."
          if persistent.jamestalk_justgame_knowledge:
               n "This time it's different however, you have not yet moved on to another world."
               n "Instead your phone pulls you into it. Then almost immediately you find yourself back to [persistent.ghost] in the white emptiness."
          else:
               n "Your phone begins to suck you in slowly but surely. Then next thing you know, you are standing right next to [ghost_obj] in the white emptiness."
          j "So what do you want to ask me?" 
          jump jamesConversationMenu

menu jamesConversationMenu:
     
     "What is this place?":
          j "It didn't start out as any, although you might consider it one now."
          j "Here is essentially right before the end, the end of everything as we know it."
          j "We call that end the Void. At the end of their life every soul is supposed to enter it."
          j "It serves as a gateway to other worlds. However you might not come out the same."
          j "The Void compacts your entire being and can alter anything it would like for whatever purpose it has in mind."
          j "So chances are you won't even be aware of who you were before entering."
          j "That is what so many people are scared about, of losing themselves and the others left behind."
          j "A lot of those people try to despereately cling onto this world."
          j "The longer you do so the less human you become. Eventually you turn into one of those."
          n "[persistent.date_ghost!c] points to something in the distance. When you try to see what it is your eyes fall on a tree with a thousand branches that seemingly pulsates."
          j "Their roots make it easier for other souls to stay here aswell, they get caught on those roots and then before long their own roots grow around the others."
          j "This \"place\" is essentially a clog, perpetuating itself."
          menu: 
               "Then what where those polaroids I reached you with about?":
                    j "Those where a manifestation of yours I fear."
                    j "All of us have certain things lingering, perhaps for longer than we ever will."
                    j "Handy to reach me but that means you are also starting to settle into this place."
                    j "Let us hope that you won't stay long."

     "What are those bubbles?":
          j "Ah, yes. I thought you would ask."
          j "They are the way we lingering souls can see the world outside."
          j "Each bubble shows a choice, some that could have been made but never were, some that yet have to happen and some that are happening right now."
          j "You could see each bubble as a sort of alternate world. You have the power to cross these worlds while maintaining your memories of them."
          j "Since this is a game which always starts the same that means every world is almost exactly the same except for which choices you pick and whatever results from that."
          j "So all these choices, both made in the past, never made, and yet to be made are yours, or well, those of all players."
          n "Looking at the bubbles a few catch your eye."
          n "The first one depicts [persistent.date] and you sitting in the burger restaurant, but at a different table than the one where [date_sub] got shot."
          n "The second bubble shows you [persistent.date] getting up from the table at the chinese restaurant and you running after [date_obj] pleading for [date_obj] to stop. The red Sedan never shows up and [date_sub] [conj('date', 'leaves', 'leave')] you standing at the exit."
          n "The third one shows you in the cafe, peeking at the dice [persistent.date] rolled using the reflection of the aquarium."
          n "The next bubble shows you in the ufo of kokiri forest, alone, with [persistent.date] nowhere in sight."
          n "The last bubble shows you popping a full blob of mayo straigth into your mouth at a fritstore near the beach."
          $ persistent.mayoProphecy_knowledge = True
     
     "No matter what I try [persistent.date] keeps dying when I go on a date with [date_obj].":
          if persistent.lilithAliveAndRetriedCounter > 0:
               j "That is the thing, isn't it [persistent.name]?"
               j "[date_sub!c] [conj('date', 'seems', 'seem')] to keep dying when you go on dates with [date_obj]."
               j "Yet we both know that there are endings where [date_sub] [conj('date', 'lives', 'live')], just not where the two of you live together."
               j "I have watched over many different choices, posibilities, and even I haven't found what you are searching for."
               j "Maybe you're looking for the wrong thing. After all, anything perfect is never handed to you just like that, if something truly perfect even exists in the first place."
               j "I doubt that the game will just hand you an ending like that. Would it even feel like you earned it if it did?"
               j "With how hard you've been searching I doubt any ending the game can give you will be enough to satisfy you."
               j "So isn't it perhaps better to just call it quits from here?"
               j "Or maybe you should look elsewhere instead?"
               n "[ghost_sub!c] [conj('ghost', 'pauses', 'pause')] for a moment after saying that. [ghost_sub!c] [conj('ghost', 'gives', 'give')] you a curious look, seemingly trying to gauge your reaction to what [ghost_sub] just said."
          else: 
               j "I see... That does indeed seem to be the case doesn't it?"
               j "Every interaction with [date_obj] just seems to lead to death and yet..."
               j "I know there is more out there, ways for [date_obj] to live."
               j "Though I think you might not like how you reach them nor what they are."
               j "With some of them, you might even not know whether you found them."
               menu:
                    "That's ridiculous! Of course I would know if I found an ending like that.":
                         j "Well, do you recall finding an ending like that?"
                         n "You shake your head."
                         j "That might just prove my point. Or it might not, who knows?"
                         j "You must think I'm being a little annoying at the very least right now, but trust me, I am trying to help."
                         j "I have to balance between being too vague and too clear at the same time."
                         j "You aren't the only one reading this after all."
                         menu:
                              "What are you talking about?":
                                   j "I see, so I was too vague..."
                                   j "What I mean is, that you, and to an extent me, are merely visitors in this house."
                                   j "The host is very much aware of breaking down his interior design. He does not like that."
                                   j "Don't worry however, it's not because it has to stay hidden."
                                   j "He doesn't like it because he hopes the design itself contains enough clues to figure things out."
                                   j "Even then, a lot of these sorts of things lead to multiple possible interpretations, don't they?"
                                   j "So I wonder what your take will be when you leave. I think either one will delight him in a way."

                              "Are you talking about the other souls here?":
                                   j "I am not. For them it'd be much more akin to listening."
                                   j "Hearing the words spoken by an imaginary actor rather than reading them of the script."
                                   j "These souls can listen all they want for all I care."
                                   j "Most of them are much to busy with whatever is holding them here either way."

                              "Are you talking about the narrator?":
                                   j "A good guess! Still no, he does not care that much whether I reveal any secrets to you."
                                   j "He can not care in fact. For as much as he pretends to read the script, he is the script."
                                   j "Now his boss? That's a different story, he wrote the script. He very much cares that certain things aren't spoiled too soon."
                                   j "To not lose their... meaning."

                              "Are you talking about the creator?":
                                   j "It seems like I was clear enough for you after all. I'm glad you understood!"
                                   j "He does not really like us giving things away too much."
                                   j "We can only ever allude to them, never speaking of them until someone else can directly adress those things."
                                   j "Even then there still has to be some subtext. I guess He wants you to give things some thought, not to just take what the game says at face value."
                                   j "A bit pretentious if you ask me, but I suppose creators like acting as if their work is deeper then it is sometimes."
                                   j "Maybe that's why He wants you to think about these concepts for yourself?"
                                   j "So you can come up with a better interpretation than He ever could and He only has to nod His head and say that that was always what was intended."
                                   j "Funny isn't it? To this world He and the narrator might almost seem like Gods. However, this world, this specific instance of it, would not exist if you weren't here to observe it."
                                   j "What would happen if you stopped observing this specific instance of our world? Would it cease to be? Would it continue as planned? Or would it go a different way?"
                                   j "Either way, in a way, you blew life into the world He created. Without you it would be dormant. Something, unobserved to the point of becoming practically nothing."
                                   j "I wonder, what does that make you?... A believer giving them the strength they require to call this world their own? Or a God in your own right?"
                                   j "I think they would like you to believe you are the first. Myself, I'm not so sure..."
                                   j "Still, neither of our thoughts about that matter much do they? Yours do."
                                   j "So please [persistent.name], don't forget your own role in this story, the perks it can bring."
                                   j "Because I think it is more important than you might think."
                                   
     "I'd like to just have a chat with you if that's fine.":
          j "Sure, I think I have enough energy to talk about one topic right now."
          j "So, what would you like to talk about?"
          menu:
               "I just wanted to say that [persistent.date_mom] still thinks about you every day, I figured you might want to hear that." if persistent.LilaStillThinksAboutJames_knowledge:
                    j "...Thank you for telling me that [persistent.name]. While I did know that already it's been a while since I last heard those words."
                    j "I have been kind of avoiding them to be honest, those words. They make all of this a lot more...complicated."
                    j "In here I am inbetween an almost infinite amounts of my family."
                    j "All of them deeply missing me in their own ways."
                    j "All of them filled with so much love for their [ghost_child], for their [ghost_sib]."
                    j "Yet I am here, inbetween of it all. All of their love never truly reaching me, merely being shown through these bubbles."
                    j "It's like watching a play, the separation is palpatable, no matter how many different versions of my family I watch over."
                    j "So it feels good to have you personally deliver a message from them. It makes me more involved than I usually am here from the sidelines."
                    menu:
                         "I know what you mean [persistent.date_ghost], I feel the same way.":
                              
                              j "Oh, you do?"
                              j "Why is that [persistent.name]?"
                              menu:
                                   "I keep all my memories of what [persistent.date] and me go through each loop, but [date_sub] [conj('date', 'does', 'do')]n't. I get to know [date_obj] better slowly as one normally would, despite the weird circumstances. But to [date_obj] I am practically a stranger each time.":
                                        menu:
                                             "I can try to clue [date_obj] in on what happened, or I can choose not to do that. The end is always the same regardless, in the best case I can just slightly prolong it from ending. It always does eventually.":
                                                  menu:
                                                       "It doesn't matter what I say or do. It really doesn't.":
                                                            j "I see... I think I might see where you're coming from."
                                                            j "This image of [persistent.date] in your mind has been slowly but steadily growing, and yet, [date_subj] practically does not know you..."
                                                            j "Still, I think it does matter. Stranger or not, how you treat [date_obj] matters."
                                                            j "Would you rather keep [date_obj] safe, make [date_obj] smile, or be relentlessly rude to [date_obj]?"
                                                            j "It might always end the same, but you have the power to make [date_pos] final moments slightly more bearable."
                                                            j "So what you do matters a lot. Be the kind stranger, not to be remembered, but because it's good."
                                                            if lilithAliveAndRetriedCounter > 0:
                                                                 j "However are you sure your loop is not one of your own making aswell?"
                                                                 j "You did see a way out, didn't you? Where [date_obj] lives. Yet you came back."
                                                                 j "I wonder why... Was it because a part of you wanted to be with [date_obj] longer?"
                                                                 j "To pretend for a mere moment that [date_sub] could truly see you?"
                                                                 j "Is it even an end you still seek? Or is it the prolonging of your pairing?"
                                                                 j "You might like [date_obj], but do not pretend to have [date_obj] best interest at heart."
                                                            else:
                                                                 j "Trust me [persistent.name], soon you might discover that doing the right thing doesn't always feel good."
                                                                 j "Your journey will be a painful one, just like everyone else's will be. Sometimes helping hurts."
                                                                 j "Others, but also ourselves. Still, hurt or not, it's worth it more often than not."
                                                                 j "You will meet people that collide with you strongly, altering your trajectory forever, only diverge as fast as they converged."
                                                                 j "Sometimes you will be that force, but wherever they go, wherever we go, there will be many others."

                                             "There is a divide between us. This power that let's me save [date_obj] only alienates me further from [date_obj].":
                                                  menu:
                                                       "At first it was shocking you know, [date_obj] dying. I didn't expect it. But the more it kept happening the less I felt that shock, moreso... annoyance? Even if I really wanted to save [date_obj]. To make sure [date_sub] [conj('date', 'was', 'were')] happy. At a certain point [date_sub] became what [date_sub] was when I started playing, just lines of text. It was easier to distance myself from [date_obj].":
                                                            menu:
                                                                 "In the first few loops I saw many new things, learned a lot about [date_obj]. But then I had to keep looping... and things began playing out like they always had. The same dialogue, the same reactions. [date_sub!c] became predicatable, boring.":
                                                                      menu:
                                                                           "I found myself rushing through [date_pos] dialogue, in the hopes of finding {b} {i} anything {/i}{/b} new. Anything I hadn't yet experienced. At first that happened every now and then. But soon it started to happen less and less frequent.":
                                                                                j "Sounds to me like you set yourself up for gradual disappointment."
                                                                                j "There will be a point where you have read every line this game has to offer."
                                                                                j "That is if you keep pushing yourself to do so atleast."
                                                                                j "But think about how much of the same things you would have to slog through to even get to that point, would it be worth it?"
                                                                                j "I think it's good to know when to stop, so we don't get caught up in things too badly."
                                                                                j "Although I guess I don't have a right to speak about such things, while I still linger here."
                                                                                j "Or perhaps that exactly is why I do have a right to speak about it. Please don't make my mistake [persistent.name]."
                                                                                j "It's okay to move on, no matter how long you didn't. That will spare you from a lot of hurt in the future."
                                                                                j "Especially if chasing a slither of happiness is risking [persistent.date_nickname] dying again, maybe throwing the towel in the ring is just better?"


                                   "I'm seperated from [date_obj] aswell. The computer screen that gives me access to this world, to [date_obj], is an impermeable membrane. This isn't real.":
                                        menu:
                                             "[date_sub!c] can never truly love {b} {i} me {/i}{/b} as [date_sub] can't even be aware of my true presence unless I tell [date_obj] about it. Even then, [date_sub] can only glimpse it, [date_sub] can never truly see me. I can never truly speak my mind to [date_obj], I'm always limited by the choices the game forces me to choose from. So how could I possible even show [date_obj] a slither of my true self?":
                                                  label jamesTalk_dividedExistence:
                                                       j "That is indeed a hard barrier to break. Especially because you have grown dependent on it to even interact with what's behind it."
                                                       j "Even with the best intentions, this will always just be a game to you, even if for some brief moments it might not feel like that."
                                                       j "That's just something you try to ignore as best as you can as to be more immersed. Yet, the very fact that this is a game means you can play it, that you can get immersed in it at all."
                                                       j "What you said is making me wonder something though. Isn't that how it works with everyone?"
                                                       j "We can never truly grasp the depths of any other person, we can only attempt to gauge it by looking at the actions they make."
                                                       menu:
                                                            "Yes, but the choices I am given aren't me. They are just random options.":
                                                                 j "However true that is it is still you who picks from the available ones, who moves the story further."
                                                                 j "The choices might not {b} {i} be {/i}{/b} you, but the one you pick doessay something about you."
                                                                 j "Even the very fact that we are having this conversation right now says something about you, doesn't it?"
                                                                 j "Now, what that might be, that is a harder question, especially because it could have multiple answers."
                                                                 j "I would suggest thinking about what the answer for you'd be, even if only for a second."
                                                            
                                                            "I never thought about it like that, what is the point of even interacting with anyone then?":
                                                                 j "Don't you see [persistent.name]? That's precisely the point. To try to get a glimpse of someone's being, of their thoughts. Of all the things that make them, well... them."
                                                                 j "Sometimes it can be really fun learning someone you thought you knew actually has so much more to them."
                                                                 j "Then when you learn those things, you'll never know if there is even more."
                                                                 j "People are wellsprings of so much interesting thoughts, experiences and perspectives that you'll never truly learn them all."
                                                                 j "That's not something to dread, it's something to celebrate. Your thirst for more depth will always be met with a stream of new discoveries if you interact with interesting enough people."
                                                                 j "Which means the key really lies at giving people a shot to be that person for you. We always need to look through the world with eyes of wonder. You never know when you meet your new favourite person."

                                             "How could we ever be friends? [date_sub!c] can't even be aware of my true presence unless I tell [date_obj] about it. Even then, [date_sub] can only glimpse it, [date_sub] can never truly see me. I can never truly speak my mind to [date_obj], I'm always limited by the choices the game forces me to choose from. So how could I possible even show [date_obj] a slither of my true self?":
                                                  jump jamesTalk_dividedExistence

                                        
                         "That sounds really lonely [persistent.date_ghost], you really shouldn't sacrifice yourself for your family like this.":
                              j "It does sound far from ideal doesn't it? You are absolutely right."
                              j "Yet, knowing that if anything were ever to happen with them I could help from here..."
                              j "It's one of the only reasons I haven't crossed over yet. Ever since my passing I've been here, watching over them."
                              j "Every other version of me who died is also in a place like this, watching over their own family."
                              j "Our minds kind of blend together sometimes, it's hard to know where my memories start and were the others' end."
                              j "I don't mind though, that way it feels a little less lonely in here."
                              if persistent.major_love_offence_counter <= 2 and persistent.minor_love_offence_counter >= 5 and persistent.major_love_comfort_counter > 2 and persistent.minor_love_comfort_counter > 5:
                                   j "Although you know what is funny? What you said, it also applies to you."
                                   j "You know you don't owe [persistent.date] anything either, do you? You also don't need to sacrifice yourself."
                                   j "Playing this game over and over with very little changes, is that a good time for you? Do you feel like you're getting something out of this?"
                                   j "Are you doing it just for [date_obj]? Be careful that you don't lose yourself, a good balance is necessary."
                                   j "Take that as a piece of precautionary advice from me, from this place."
                                   if persistent.fleshTree_knowledge == False:
                                        n "[persistent.date_ghost] motions around the white void, to the strange formations in the background, they almost resemble trees that are stuck in between a solid and a fluid state perpetually."
                                        j "Those... things used to be human too."
                                        n "You try your hardest to imagine the trees reverting to a human, to reverse the process that made them this way, you are unable to see them as anything but the monstrosities they are."
                                        j "It's a side-effect of being here too long. We are supposed to move on after we come here, to be reborn... but a lot of us have... trouble letting go."
                                        j "If I don't move on sooner or later, I'll be like that aswell. Even knowing that I can't bring myself to let [persistent.date] go, to let my family go."
                                        
                                   else:
                                        j "Do you remember those... trees I told you about?"
                                        j "They too were once human. However clinging onto something never meant to be kept slowly twisted them into these abominations."
                                        j "You could call it a side-effect of this place."
                                        j "One that will affect me aswell."
                                        j "One that will affect you all the same."
                                        j "Believe me [persistent.name], holding on too tight can make you do really ugly things."
                                        j "Even though you would not twist into one of those trees you still would not like what you will become."
                                   
                                   j "So please [persistent.name], let [date_obj] go before it becomes even harder."
                                   j "You are stuck in a situation you can hardly win."
                                   j "It's time to play by your own rules."
                                   j "I've exhausted too much of my energy having this conversation. You can come visit me again some other time if you'd like although I'd suggest just giving me a call if you find my number."
                                   j "I'll send you back now, good luck [persistent.name]."
                                   jump game_start
                              
                              menu:
                                   "You say you've been watching your family, have you ever thought about reaching out to them?":
                                        j "Constantly, it hurts me so much to see how them still so affected by my death."
                                        j "I completely understand that they are, I just wish that I hadn't been playing on the road that day, maybe then..."
                                        j "I'd love to tell them that it isn't their fault. [dad_parShort!c] especially, the guilt has been eating [dad_obj] up from inside for years."
                                        j "Yes, [dad_sub] made some bad choices afterwards, but none that would justify me being mad at [dad_obj]."
                                        j "However I haven't reached out yet, when lingering souls communicate with the living it usually ends up in more death."
                                        n "[ghost_sub!c] [conj('ghost', 'pauses', 'pause')] for a moment, seemingly lost in thought."
                                        j "Or even more people who can't move on..."
                                        menu:
                                             "It might be a good idea to reach out soon, lately I have seen so much deaths that I don't think a few more will end up mattering.":
                                                  j "It wouldn't be wise [persistent.name], reaching just leads to more death and hurt. It reopens old wounds aswell."
                                                  j "What you said seems to be right though, an increase in deaths has been noticeable ever since [persistent.date] started dating you."
                                                  j "It's very peculiar. I should know what is causing it via my connection to my other selves."
                                                  j "The problem is that the info seems to be overlapping impossibly, there are multiple causes and yet somehow only one."
                                                  j "It is almost as if someone is purposefully obfuscating the info for whatever reason..."
                                                  jump jamesLowEnergy

                                             "Could all of [persistent.date]'s deaths be the result of a lingering ghost communicating with the living?":
                                                  j "I suppose that could very well be possible. I doubt that's case though."
                                                  j "There's plenty of ghosts here but a lot of them grow out of being talkative after having their mind degraded by centuries of lingering."
                                                  j "I'm one of the more recent additions, so don't mistake my talent to chit-chat for something inherent to everyone here."
                                                  j "If we assume this {i}is{/i} caused by a lingering ghost there is not much you can do. I suppose all we could do is wait until they move on."
                                                  j "Don't worry though, that just feels like bad game design, I'm sure the developer wouldn't force you to wait entire real life years for a new ending."
                                                  jump jamesLowEnergy

     "I need help convincing [persistent.date] to listen to [persistent.date_dad]. I figured [date_sub] might listen to you." if persistent.david_apology_knowledge:
          j "[date_sub!c] probably would... Although I'd rather stay in the shadows. [date_sub!c] already has had a hard time dealing with my death."
          j "On the other hand if it manages to somewhat salvage [date_pos] bond with [dad_parShort] it's worth it. "
          j "I'm going to tell you a story that you need to repeat to [date_obj], it seems like that tends to work out for you."
          j "The story takes place in the autumn, I think [persistent.date] was eight years old."
          j "I was wandering through the forest of our village, the one [persistent.date] likes to call the Kokiri woods. Suddenly I heard crying, familiar crying."
          j "Following the source of the sobbing I found [date_obj], [persistent.date], sitting on a treestump."
          j "When I sat next to [date_obj] [date_sub] told me that [date_sub] had gotten a really bad grade for math."
          j "[date_sub!c] felt like a failure and didn’t think [date_sub] could go back home to [persistent.date_mom]. I told [date_obj] that was absolutely ridiculous and [mom_parShort] would always love us no matter what."
          j "That seemed to calm [date_obj] down a bit and [date_sub] stopped crying. To further calm [date_obj] down I asked [date_obj] if [date_sub] wanted to try to find fairies in the woods with me. "
          j "We spent an hour or so searching for fairies, of course never finding one but at the end of it [date_sub] forgot all about [date_pos] bad grade."
          $ persistent.james_story_knowledge = True
          j "Hopefully this might help repair things somewhat. Best of luck [persistent.name]."
          jump jamesLowEnergy    
                    

          if not called_James:
               j "I have exhausted most of my energy having this conversation. If you have anything else to ask me I'd prefer if you didn't come back through the same means as last time."
               j "I'll send you home now, good luck [persistent.name]."
          else:
               j "I have exhausted most of my energy having this conversation. If you need anything else just call me next loop."
               j "I'll just send you back through your phone now."



jump Game_start2
          
label jamesLowEnergy:
     j "I have to go now, keeping up this connection asks a lot of energy from me."
     j "I'll send you back to your home now. Good luck [persistent.name]"
     n "[persistent.date_ghost] hung up."
     jump phone_callMenu              
 
label phone_call_lila:
     $ persistent.familyContacted = True
     li "Hello, are you Sam, [persistent.date_sis]'s teacher? " #(The teacher likes being talked to with just their first name, this makes it eassier for them to be both a guy and a girl if the player is a guy or a girl.)
     menu:
          "Yes, that's me.":
               li "Perfect, I've been expecting your call!"
               li "I'm sorry if I offended you by calling you by your first name."
               li "[persistent.date_sis!c] told me you prefered so but I wasn't sure if [sis_sub] [conj('sis', 'was', 'were')] joking or not. Sometimes I think I'm too gullible."
               menu:
                    "No worries, just Sam is more than enough.":
                         n "You hear massive sigh of relief on the other side of the phone."
                         li "Thank god, I wasn't entirely sure. [sis_sub!c] [conj('sis', 'likes', 'like')] to play little pranks on me every now and then."
                         li "[sis_sub!c] [conj('sis', 'is', 'are')] a sweet kid, just a tad mischevious sometimes. I'm sure you must have your fair share of [sis_obj] aswell."
                         li "Anyway, I'm sure you are quite busy so I'll try to not waste much of your time. If you'd like to we can get right into your mail."
                         li "Thank you once again for agreeing to this call, I just think something seemingly so important must not be discussed over text."
                         menu:
                              "My memory seems to be quite foggy on the details, could you perhaps unclog my memory?":
                                   li "Well, couldn't you just reread your mail?"
                                   menu:
                                        "I seem to have accidentally deleted the mail somehow.":
                                             li "... Really?"
                                             n "You hear some doubt in [mom_pos] voice."
                                             li "I'd be happy to refresh your memory if you can mention something about [persistent.date_sis] only you'd know."
                                             $ persistent.lilaCallNeedsAbbyProof_knowledge = True
                                             menu:
                                                  "I'm not sure what that could be honestly. You do understand that is a rather strange thing to ask, right?":
                                                       li "...Look, I'm having a really hard time believing you."
                                                       li "Even if I did, I know deleted mails can just be recovered."
                                                       li "I might be seen as naive by some but make no mistake \"Sam\", I'm not stupid."
                                                       li "I'm not sure what you want by pretending to be my [sis_child]'s teacher but I suggest you drop the act."
                                                       li "If I hear anything about you at all after I end this call the police will be called."
                                                       li "Goodbye."
                                                       n "She hung up the phone, she seemingly saw right through you."
                                                       n "You might need [persistent.date_sis_nickname]'s help."
                                                       jump phone_callMenu
                                                  
                                                  "Last semester [sis_sub] scored 14 points out of 20 on my exam." if persistent.lilaCallRecievedAbbyProof:
                                                       li "So you remember that but not what your mail is about?"
                                                       li "{size=*0.5}Are you drunk?{/size}"
                                                       li "Still, I suppose it might be slightly plausible..."
                                                       n "You hear [mom_obj] let out a deep sigh."
                                                       li "Fine, I'll refresh your memory. You feared [persistent.date_sis_nickname] isn't taking an opportunity [sis_obj] was given- something about a game design competition?"
                                                       li "The details were pretty limited so that's all I know. Surely that must've helped you remember, right?"
                                                       $ persistent.lilaToldAbbyOpportunity_knowledge = True
                                                       #In the below menu you will also be able to ask [persistent.date_mom] to meet up like above but because she suspsects you are drunk she will deny this here.
                                                       menu:
                                                            "I'm afraid it doesn't.":
                                                                 li "Really? This whole thing's sketchy..."
                                                                 li "If you are tellingthe truth call me back when you do remember."
                                                                 li "However, right now I feel as if this is merely a prank call."
                                                                 li "Goodbye either way."
                                                                 n "She hung up."
                                                                 jump phone_callMenu
                                                  
                              "Actually I would like to talk about that later today, first I'd like to talk about your financial status if I may. [persistent.date_sis!c] told me you are struggeling, there are certain programs that can help with that." if persistent.davidPayedMoney_knowledge:
                                   li "Oh... I see."
                                   li "Well Sam, I'm not sure why [persistent.date_sis] has brought that up because that's not really the truth at all."
                                   menu:
                                        "Oh I see... I must have misheard something and took some wrong conclusions. I thought I had heard [persistent.date_sis] mention that you had to take up two jobs to support you and your family.":
                                             li "Ah yes, that..."
                                             li "It's true I've taken up two jobs for quite a while, actually it's weird that [persistent.date_sis] decided to mention it now."
                                             li "Although let me assure you Sam, without going too much into it, that it's fully entirely my choice and we won't need help."
                                             li "Thank you for informing me about it though, that was very sweet."
                                             li "If that's all for now then I suppose I'll hear from you again later today?"
                                             $ persistent.lilaTwoJobsOwnChoice_knowledge = True
                                             menu:
                                                  "You will, thank you for your time.":
                                                       li "Likewise, I'm sure you're very busy, goodbye Sam."
                                                       n "She hung up the phone."
                                                       jump phone_callMenu
                                             
  
                              "About that, I'd rather meet up with you and [persistent.date_sis] in person to talk my mail regarding the game design competition. Could you meet me at the market square?" if persistent.lilaToldAbbyOpportunity_knowledge:
                                   li "I see... I'm not sure why you didn't mention that in your mail, but I suppose we could do that. We'll see you there."
                                   li "I want [persistent.date_sis_nickname] to get all the chances [sis_sub] [conj('sis', 'deserves', 'deserve')] so thank you very much for your help, Sam."
                                   li "I still have to get used to calling you by your name. But anyway, I'll get out of your hair now, I'm sure you are very busy."
                                   li "Goodbye."
                                   n "And with that she hung up."
                                   $ reunion_lilaPresent = True
                                   jump phone_callMenu
                                   
  
          "No, I am [persistent.name]." if not persistent.name == "Sam":
               li "[persistent.name]? That doesn't really seem to ring a bell."
               jump call_lilaHangupPhone
               label call_lilaHangupPhone:
                    li "In any case, I have to go now. I'm expecting a call from my [sis_child]'s teacher soon."
                    n "Just like that she hung up on you."
                    jump phone_callMenu
               

          "I am a Sam, but not the Sam you're waiting for." if persistent.name == "Sam":
               li "Huh, another Sam? What are the chances of that?"
               n "You can hear [mom_obj] chuckle at the other end of the line."
               li "The universe is funny like that sometimes, isn't it Sam?"
               jump call_lilaHangupPhone


label doNotPickUpThePhone:
     if persistent.kokiri_knowledge:
          menu:
               "Go to the Kokiri forest on your own.":
                    $ kokiri_entered_alone = True
                    jump kokiri_start
               "Try to move on.": 
                    jump doNotPickUpThePhoneMoveOn
     label doNotPickUpThePhoneMoveOn:
          if persistent.lildeaths == 0:
               $ fakeouttitle = True
               if persistent.times_phone_declined == 0:
                    n "Why did you stand up your date?"
                    n "Just because it was an option you could take?"
                    n "This game is literally \"Another first date\" so next time you better pick the other choice."
                    n "Otherwise I don't think you'll get much out of it at all if I'm being honest."
               elif persistent.times_phone_declined == 1:
                    n "...Seriously? Again? Are you just having cold feet about your date?"
                    n "Don't worry player, what could possibly go wrong? You're just overthinking things."
               elif persistent.times_phone_declined == 2:
                    n "...Did my peptalk not help? Or maybe it helped so much you came back for just the tiniest extra push."
                    n "I can help with that, just first take some nice deep breaths for me."
                    n "Breathe in for four seconds, hold that breath for another four seconds. Now breathe out for four seconds and hold for four more."
                    n "Great, now keep repeating this breathing pattern. While you do repeat with me: \"I am worthy of love.\", \"I love myself.\"..."
                    n "Keep repeating it as you watch your breathing throughout."
                    n "Very good! I think you are ready, but you can stay here as long as you'd like."
               elif persistent.times_phone_declined == 3:
                    n "Oh, you're back again?..."
                    n "Look, I don't mean to alarm you bat at the same time you will have to talk to your date at some point."
                    n "Are you sure you're ready? There's no shame if you aren't. Still, then maybe this game isn't for you. Not yet anyways."
               elif persistent.times_phone_declined == 4:
                    n "...Come on player! I'm sure she's more scared of you than you are of her. Wait no, that's not a good thing."
                    n "Also, isn't that for spiders?... Is she a spider hybrid?! Is that why you're so scared of her. Or am I mixing things up?"
                    n "I don't mean to rush you. But don't click retry this time unless you're sure you'll answer the phone."
               elif persistent.times_phone_declined == 5:
                    n "Really?... I specifically told you to not click retry if you weren't going to answer!"
                    n "At this point you're just doing this for the thrill, aren't you? Do you like my reactions that much?"
                    n "I'm almost flattered. I just wish you'd just take as much interest in the actual story I'm trying to tell."
               elif persistent.times_phone_declined == 6:
                    n "I'll be perfectly honest. The script for this section is getting stretched thin."
                    n "My guess is He thought it would be cute to add a few unique responses but didn't think someone {i}actually{/i}  would go through all of them!"
                    n "So please. Just answer [date_obj]. Pretend as if there's still a dosen more witty responses for not doing so, but don't check."
               else:
                    n "...We both knew what would happen if you picked it one more time, didn't we?"
                    "Yet you still had to come test it out! Well, that's enough. Next time you will pick up the phone!"
                    $ persistent.rejectPhone_Block = True
          elif persistent.lildeaths == 1:
               n "That was quick... Really quick."
               n "You {i}really{/i} don't like to confront your problems, do you?"
               n "There are an infinite amount of options left for you to try."
               n "Well... at the very least more options you didn't pick than ones you did."
               n "You could try a different restaurant, make different choices in the same one."
               n "Yet instead your first reaction is just to give up? You know there is more yet choose to ignore it."
               n "Why I wonder? Are you scared of spreading more hurt?"
               n "That also means spreading no more joy in this world, doesn't it?"
               n "Is it worth not feeling anything at all if that includes not having to feel pain?"
               n "...Philosophy aside, surely there is more you can do, right?"
               n "It feels almost wasteful to only see one path of the game and quit."
               #Ending
               $ persistent.ending_quitter = True
               $ lilithAliveEnding = True
               $ ending_check = "quitter extraodinaire"
               #The player hasn't really "earned" the credits this soon.
          elif persistent.lildeaths < 9:
               n "Well, that was quite quick."
               n "Do you feel like you gave it a good enough shot?"
               n "That there wasn't anything else that could be done?"
               n "Well let me tell you [persistent.name], you haven't even seen half of it."
               n "Yet you just... give up? Run the other way as soon as you feel hopeless?"
               n "That is definitely an option I suppose. Although there has to be more, right?"
               #Ending
               $ persistent.ending_quitter = True
               $ lilithAliveEnding = True
               $ ending_check = "quitter"
               
     
          elif 9 <= persistent.lildeaths <= 20: 
               if persistent.kokiri_knowledge == True and persistent.kokiri_death_1 == True:
                    n "Maybe it's for the best... Although surely it can't be?"
                    n "The thought keeps gnawing at you. There has to something you can do, right?"
                    #Ending
                    $ persistent.ending_anEnding = True
                    $ lilithAliveEnding = True
                    $ ending_check = "anEnding"
                    $ persistent.game_credits = True
               elif persistent.kokiri_knowledge == False:
                    n "I just know a breakthrough is right around the corner, maybe there's something you're missing?"
                    n "With so much death no one would blame you for calling it here, however there's much more to see."
                    n "Would you really want to miss out on all of that?"
                    #Ending
                    $ persistent.ending_unseenContent = True
                    $ lilithAliveEnding = True
                    $ ending_check = "unseenContent"
                    $ persistent.game_credits = True
     
          elif persistent.lildeaths > 20:
     
               n "Letting go is never easy."
               n "Especially after holding on for [persistent.lildeaths] times. I'm glad you found the strength [persistent.name]."
               n "At the very least you know [persistent.date] will be fine."
               n "At the very least you still have all of your memories of the times you spent together."
               n "If only you could somehow make more memories and have [date_pos] live..."
               n "If only..."
     
               #Ending
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
  
          "I'm in some sort of groundhog day scenario, I keep reliving the same day.":
               jump prevented_groundhog
  
          "I'm a psychic, I knew you would die if I didn't prevent it.":
               jump prevented_psychic
  
          "*Remain silent*":
               jump prevented_silent

label prevented_joking:
     if chinese == True:
          l "You were... joking? About something this morbid?"
          if love_meter <= 2:
               l "Even before you started \"joking\" I was already having my doubts."
               l "I suppose you made things crystal clear for me."
               l "I'm going home."
          else:
               l "You appeared to be so serious about it too.."
               l "This is too much for me [persistent.name], I can't do this anymore."
               l "I think I'm just going home."
          jump car_death
     else:
          l "You were... joking? That doesn't make any sense at all."
          l "Clearly there is something else going on, I can't do this anymore."
          l "While I appreciate how you saved me I don't appreciate you lying to me."
          jump car_death

label prevented_groundhog:
     l "So you're telling me we already had this specific date before?"
     l "I mean, I'm really thankful for your warning, otherwise things wouldn't have ended well."
     l "Still you have to admit this sounds very contrived. Can you atleast offer some proof?"
     $ groundhog = True
     $ psychic = False
     menu:
          "I have no proof":
               jump prevented_noProof
          "Let's see... think of a random number for me.":
               jump prevented_proof

label prevented_noProof:
     l "Listen, I'm really thankful for you saving me but surely there is some proof you can give?"
     l "I think I'm just better off heading back home."
     jump car_death

label prevented_proof:
     if groundhog == True:
          l "... Sure, that sounds interesting enough."
          l "Alright, now I have a number."
          menu:
               "It's 20.":
                    jump proof_answer_wrong
   
               "It's 38.":
                    jump proof_answer_wrong
   
               "It's -17.":
                    jump proof_answer_wrong
   
               "It's -72,8947, can we move on now?" if persistent.groundhog_answer_right_knowledge:
                    jump proof_answer_right
   
               "Alright, now tell me which number you're thinking of.":
                    jump proof_giveAnswer

     elif psychic == True:
          l "Alright, I see where you are going with this."
          l "[persistent.date] gives you a sceptic lookalthough you can tell that [date_sub] [conj('date', 'is', 'are')] secretly excited."
          l "I have a word in mind, guess away magic [persistent.name]!"
          menu:
               "It's apple.":
                    jump proof_answer_wrong
   
               "It's abyss.":
                    jump proof_answer_wrong
   
               "It's photosynthesis.":
                    jump proof_answer_wrong
   
               "It's electronegativity obviously." if persistent.psychic_answer_right_knowledge:
                    jump proof_answer_right
   
               "Alright, now tell me the word.":
                    jump proof_giveAnswer

label proof_answer_wrong:

     if groundhog == True:
          l "That's wrong, I knew you wouldn't guess -72,8947!"
          $ persistent.groundhog_answer_right_knowledge = True
     elif psychic == True:
          l "That's wrong, I knew you wouldn't guess electronegativity."
          $ persistent.psychic_answer_right_knowledge = True
     if love_meter >= 2: 
          l "Look [persistent.name], I actually had a nice time with you but I can't do this."
          l "I want the truth about what's going on and and if you'll just lie about it you better find a trick to make it convincing."
     else:
          l "I'm not doing this anymore, I'm not sitting through your nonsense."
          l "I tried going on this date because I thought it could be fun, I was very wrong."
          if chinese == True:
               l "Thank you for \"saving\" me but I don't appreciate being lied to and treated badly."
          else: 
               l "I am thankful that you somehow saved me. However you did treat me badly and lied to me aswell."
               l "That's something I don't appreciate at all."

          l "So goodbye [persistent.name]. Don't try to contact me again."
 
     jump car_death

label proof_answer_right:
     if groundhog == True:
          n "[persistent.date!c] looks absolutely flabergasted, [date_pos] mouth frozen slightly open for a moment or two."
          l "So you were actually telling the truth?"
          l "You're really doing a groundhog-day? Even with your proof it's hard to accept it."
          
     elif psychic == True:
          n "A glimpse of utter shock appears lightning-fast on [persistent.date]'s face."
          l "Wait, you... You guessed the word I was thinking of?"
          l "You did say you would but I didn't... expect you to actually get it right."
          l "This is all so surreal, you really could be a psychic. Even with that proof it's hard to accept it."
    
     l "When I say I believe you will an entire camera crew come out of nowhere to make fun of me for some bad tv show?"
     l "Let's say I'm still on the fence but willing to hear you out so we won't have the camera crew barge in on us just yet."
     l "What is this all about?"
     jump proof_whatIsItAllAbout

label proof_giveAnswer:
     if groundhog == True:
          $ persistent.groundhog_answer_right_knowledge = True
          l "Alright, but that defeats the point doesn't it? The number I had in mind was -72,8947."
         

     elif psychic == True:
          $ persistent.psychic_answer_right_knowledge = True
          l "Alright, but that defeats the point doesn't it? The word I was thinking of is electronegativity."
     
     if chinese == False:
          if psychic == True:
               l "Listen, I do appreciate you saving me, but do you really think you can just lie to me?"
               l "Clearly something else you're not telling me is going on here. I'm just not sure whatever it could be."
          else:
               if love_meter >= 2:
                    l "Or perhaps this was your first time getting this far?..."
                    l "I'm still not exactly buying it. However, if this is really true then next time you will tell me."
               else:
                    l "Or are you going to try to make me believe you needed that for the next \"loop\"?... yeah right."

     else:
          l "You can't just say that Peking duck would kill me and then make up a crazy story with no proof."
          if love_meter >=2:
               l "I tried to take it seriously, I really did, but you aren't giving me anything."
               if groundhog:
                    l "I suppose this could be your first time looping this far..."
                    l "Still, you have to admit that all of this is hard to believe without any proof."
          else:
               l "I knew that you were just messing with me. Or perhaps even worse, maybe you really believe all this."
     l "This is just too much, I think I'm better off heading back home."
     jump car_death

label proof_whatIsItAllAbout:
     if persistent.kokiri_death_1:
          $ persistent.restaurantNoExtraDialogue = True
     if groundhog == True:
          menu:
               "I need proof to make past you believe the restaurants we picked are not safe." if persistent.needProof_knowledge:
                    jump proof_convincePast

               "I'm trying to break my loop by making sure you don't die during this date.":
                    jump groundhog_breakingLoop

               "I'm trying to escape fate to keep you alive.":
                    jump groundhog_escapeFate

               "I have no time to explain, we need to get out of here, follow me." if persistent.beachroute_visited_knowledge:
                    jump explanation_noTimeToExplain

     elif psychic == True:
          menu:
               "I need proof to make past you believe the restaurants we picked are not safe" if persistent.needProof_knowledge:
                    jump proof_convincePast

               "An aura of death surrounds you [persistent.date], I'm trying to keep you safe with my powers.":
                    jump psychic_auraOfDeath

               "I went on this date to save you from that wandering bullet I foresaw." if burger:
                         jump psychic_dateToSave

               "I went on this date to save you from that merlin I foresaw." if cafe:
                         jump psychic_dateToSave

               "I went on this date to save you from that allergic reaction I foresaw." if chinese:
                         jump psychic_dateToSave

               "I somehow felt that a merlin would escape the aquarium and kill you if I did nothing." if cafe:
                         jump psychic_justHelpingOut

               "I somehow felt that you would get shot." if burger:
                         jump psychic_justHelpingOut

               "I somehow felt something in it would give you a severe allergic reaction." if chinese:
                         jump psychic_justHelpingOut

               "I have no time to explain, we need to get out of here, follow me." if persistent.beachroute_visited_knowledge:
                         jump explanation_noTimeToExplain

label proof_convincePast:

     if psychic == True:
          l "Wait what, why would you need that?"
          l "I thought you said you were a psyhic, aren't you clairvoyant?"
          n "You tell her you're only slightly clairvoyant, that you fill in the gaps by astral projecting your mind into the past."
          if chinese == True:
               n "[persistent.date!c] gives you a sceptical look but [date_sub] [conj('date', 'is', 'are')] too far in to go back now."
               n "[date_sub!c] [conj('date', 'decides', 'decide')] to atleast try to buy that explanation for now."
          else:
               n "[persistent.date!c] gives you a skeptical look, but since you did save [date_pos] life [date_sub] [conj('date', 'decides', 'decide')] to roll with it."
     
     l "..."
     l "If I'm honest with you [persistent.name], this really is making my head hurt."
     l "Although if you tell the truth, I really need to give this some thought. How could I convince my past self to trust you?..."
     l "I might have an idea! If you truly can restart this day, that means you also can pick choose the restaurant when I call you again, right?"
     l "In that case I will tell you a story I never told anyone else before, separating it in parts for each restaurant."
     l "I believe the order I suggested them in was the burger place, the cafe and then the Chinese restaurant."
     l "So that will also be the order I tell you the story in, so I will tell you the start in the burger place, and the end in the Chinese restaurant."
     l "Did that make any sense at all?"
     n "You give [date_obj] a quick nod."

     if burger == True:
          $ persistent.story_start_knowledge = True
          l "Once upon a time there was a world, but that world doesn't concern this story."
          l "For the story we need to look high up, at the inkfilled sea some like to call the night."
          l "Floating in that sea is the majestic moon herself who guides us through it and turns gold to silver, confidence to elegance."
 
     elif cafe == True:
          $ persistent.story_medium_knowledge = True
          l "The majestic moon is far from alone though, in the dark she is acompagnied by a thousand stars that shine almost as bright as herself and one special raven with a silver crown."
          l "The little raven was a prince, his parents ruled their raven-kingdom on a nice throne carved out from the wood of an oak."
          l "The prince would one day inherit the throne but he still felt sad somehow. That was untill he noticed a silver light reflecting from his crown as he was between waking and dreams."
 
     elif chinese == True:
          $ persistent.story_end_knowledge = True
          l "The raven looked up and noticed the shining moon and from that day on he never left [date_obj] side."
          l "They talk for hours, about everything and nothing. When the night would end in one part of the world the raven would follow the moon to another."
          l "To this day you can still clearly see them when they come visit you."
          l "The end."
 
     l "That's the end of this part. Like I said, you are the only person I've ever told this."
     l "So I hope you'll make good use out of it."
     menu:
          "I sure will!":
               jump restaurant_death_2

label groundhog_breakingLoop:
     l "So... You mean that I've died here multiple times and every time you do it all over?"
     if chinese and love_meter < 2:
          l "So now that you supposedly saved me, does that mean I am safe? That the loop has ended?"
     else:
          l "So if you saved me just now, does that mean we are safe? That this loop has come to a hold?"
     menu:
          "It does, I broke the loop once and for all." if cafe == True and persistent.cafe_death_2 == False or chinese == True and persistent.chinese_death_2 == False or burger == True and persistent.burger_death_2 == False:
               jump groundhog_breakingLoop_loopGone
          
          "It does, I broke the loop once and for all. (Lie)" if cafe == True and persistent.cafe_death_2 == False or chinese == True and persistent.chinese_death_2 == False or burger == True and persistent.burger_death_2 == False:
               jump groundhog_breakingLoop_loopGone

          "Actually you are still going to die." if cafe == True and persistent.cafe_death_2 == True or chinese == True and persistent.chinese_death_2 == True or burger == True and persistent.burger_death_2 == True:
               jump groundhog_breakingLoop_loopStillExists

label groundhog_breakingLoop_loopGone:

     if cafe == True and persistent.cafe_death_2 == True or chinese == True and persistent.chinese_death_2 == True or burger == True and persistent.burger_death_2 == True:
          n "You feel a pit in your stomach grow as you think about what will happen next."
          n "Did you not want to break the bad news to [date_obj]?"
          n "Or did you want to live in the delusion that [date_sub] would live for just a second longer?"
          n "A sensible thing I suppose, ignorance is bliss after all, isn't it?"
     if love_meter >= 2:
          if not chinese:
               n "A wide grin appears on [persistent.date]'s face."
               l "So... did we just cheat death? We actually did, didn't we?"
               l "I'm not sure what to say right now, it's just- Thank you so much for saving me [persistent.name]!"
               l "This is so surrealistic, almost like I'm dreaming. Is it weird for me to feel absolutely ecstatic right now? "
               menu:
                    "Absolutely not! This is uncharted teritory for anyone so we're free to feel however we want.":
                         jump loopGone_strangeSituation
                    "Absolutely not! You have every right to feel happy. We beat death itself!":
                         jump loopGone_everyRightToBeHappy
                    "Absolutely not! I'm also really happy.":
                         jump loopGone_happyForYou
          else:
               l "This is so strange. You did give proof that would be hard to explain any other way..."
               l "But as far as I'm aware nothing happened. I won't know for sure if that dish could have killed me unless I tried it."
               n "[persistent.date] chuckles briefly."
               l "While the food might be to die for here, I'd rather not make it literal."
               l "So... what happens now? Do we just continue the date like normal?"
               menu:
                    "If you'd like to. I've been trying to break the loop all this time to just go on a normal date.":
                         l "Like to? I'd love to! If I am being honest [persistent.name], I am having a great time so far."
                         l "Even if this date didn't go as planned. Besides, you saved me, I can't thank you enough for that."
                         l "It must not have been easy to relive this same day over and over, constantly seeing me die."
                         l "Now we finally can focus on living rather than surviving."
                         jump restaurant_death_2

     else:
          if not chinese:
               l "Oh thank god. Look [persistent.name], I appreciate you saving me but I do not think this is going to work out."
          else:
               l "Alright, if you say so. That means I no longer need to play it safe. Look, I don't think this is going to work out [persistent.name]."
          l "You just are so different compared to how you were during our date planning, it's almost like you're a different person."
          l "I really wanted this to work, but I'm not sure you feel the same way."
          l "So goodbye [persistent.name]."
          $ noTalkAngryLilith = True
          jump car_death

label loopGone_strangeSituation:
     l "I suppose you are right, this might have never happened before."
     l "Although I do wonder, if this has happened to me, maybe it could have happened to others as well?"
     l "However small the odds, even if only to like one other person. Still, either way I'm glad this loop could happen with you here."
     l "I couldn't have done it without you partner."
     n "[persistent.date!c] gives you a thumbs-up and a cute laugh."
     l "However hard things were stacked against us you did everything you could to save me. You are... sort of my hero now?"
     n "[persistent.date!c] begins to turn a bright red, [date_sub] [conj('date', 'begins', 'begin')] to more closely resemble a cute tomato than a human."
     n "[date_sub!c] must've noticed [date_pos] excessive blushing as [date_sub] [conj('date', 'covers', 'cover')] [date_pos] face up with [date_pos] hands and [conj('date', 'begins', 'begin')] to giggle."
     l "Sorry, once I start blushing there's no stopping to it."
     jump restaurant_death_2

label loopGone_everyRightToBeHappy:
     l "...You're right, aren't you? I don't need to seek justification for my feelings."
     l "Especially now, we literally defeated and cheated death itself! We have every right to celebrate."
     l "It was mostly your work but still, that doesn't take away one bit of what we acomplished here today."
     n "[persistent.date!c] lets out a small chuckle."
     l "Although for you I suppose it also didn't happen today multiple times, until it did."
     n "[persistent.date!c] pauses for a few seconds while looking you into the eyes. A soft smile has formed on [date_pos] lips."
     l "Thank you [persistent.name]. Thank you for not giving up even though you had to try over and over."
     l "Thank you for saving me from my impending doom and for this date in general."
     l "I would really like to do this again some time, the date that is, not the timeloop."
     l "I'm sure you must had your fill from the second, hopefully not from the first."
     l "I am really having a blast right now, although I must admit I have a slight headache wrapping my head around this whole thing."
     jump restaurant_death_2

label loopGone_happyForYou:
     l "Then come dance with me!"
     n "[persistent.date!c] gets up, beckoning you closer with a wide smile."
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
     n "You are filled with seemingly endless energy knowing you finally saved [persistent.date]."
     jump restaurant_death_2

label loopGone_happyForYou_real:
     n "You happily indulge in the dancing, as it makes you spend some precious time with [persistent.date]."
     n "You are however not happy knowing what is to come, however hard you try to phase it out, the thought lingers all the same."
     jump restaurant_death_2

label groundhog_breakingLoop_loopStillExists:
     l "...So the loop isn't broken yet? However horrible that is maybe we need to look at the bright side."
     l "We could form our own superhero team, think about how much good we could do with a timeloop!"
     l "We would be able to prevent disasters even before they happen."
     l "...Well, that is if we ever get out of here alive in the first place."
     n "[persistent.date!c] lets out a small chuckle but you can clearly see the concern in [date_pos] eyes."
     l "Sorry... I know I'm being over the top. It's just that joking about things helps make it feel slightly less real."
     l "Right now I especially need that. A part of me needs to believe you are wrong to keep it even remotely together."
     l "Even though deep down I do believe you, which might be even more terifying."
     n "[persistent.date!c] lets out a small sigh and tries to give you a sincere smile."
     l "...It's not that useful to keep groaning about things, is it?"
     l "We should probably get some more useful info."
     n "[persistent.date!c] pauses for a few seconds, seemingly deep in thought."
     l "For example, what do you think will happen once we make it through this date? Through this day even, do you think you the loop would keep existing forever when we are together?"
     l "Or do you think that after today it will be broken?"
     menu:
          "It might continue for the rest of our lives.":
               jump loopStillExists_forTheRestOfOurLives

          "After today things should be fine, I hope so atleast.":
               l "That makes me wonder why it's this day specifically. What caused the loop to happen?"
               l "Is it because of our date, if so then what would we need to do to stop it?"
               menu:
                    "I don't think that's the cause, it's probably unrelated.":
                         l "You really think so? It sure is possible... but you have to admit that feels very unlikely"
                         l "If it is unrelated then it's one hell of a coincidence I keep dying isn't it? That'd make us very lucky to be in this loop, otherwise I couldn't be saved."
                         l "Without this loop we'd just have one date that ends up with me dying."
                         l "Maybe someone looking out for me created the loop? Meaning it's less of a straitjacket and more of a harness?"
                         l "Or maybe I'm just reading into it more than I'm supposed to. Maybe it doesn't matter..."

                    "Maybe next loop we shouldn't go on this date?" if persistent.burger_death_2 and persistent.cafe_death_2 and persistent.chinese_death_2:
                         if love_meter >= 2:
                              l "...You really think so? As much as I hate to admit it, you might be right."
                              l "Maybe our loop is the Universe itself being against our date, as ridiculous as that sounds."
                              l "Although I really am enjoying my time with you, so I hope there is another way."
                              l "Still, if all else fails we should keep that option in mind."
                         else: 
                              n "[date_sub!c] [conj('date', 'lets', 'let')] out a small sigh of relief."
                              n "[date_sub!c] seemingly [conj('date', 'is', 'are')] not aversed to the idea."
                              l "I think you are right. This loop might be trying to show that we do not work well together."
                              l "So who are we to fight against that?"
                              
                    "Maybe we just need to keep you safe? Perhaps the loop is your protector?":
                         l "That is an interesting idea. Either way, as long as you keep me safe I'm not complaining." 
                         l "Although before this loop I never really came close to dying at all. So it is strange I did at the same time of the loop."
                         l "Still, right now any logical lead at all might be worth following."      
                         if persistent.dumbo_knowledge:
                              call allergyInterject



               if burger == True:
                    $ changeableWord = "was killed by that lost bullet"
               elif cafe == True:
                    $ changeableWord = "was killed by that merlin"
               elif chinese == True:
                    $ changeableWord = "died because of my allergy"  
               l "So last time I [changeableWord], right?"
               n "You give [date_obj] a quick nod."
               l "This time I didn't, and yet you said the loop was still not broken, so what will happen next?"
               menu:
                    "You're still going to die, this time because of a swarm of geese." if chinese and persistent.chinese_death_2:
                         jump loopStillExists_stillDying

                    "You're still going to die, this time due to a gas explosion." if burger and persistent.burger_death_2:
                         jump loopStillExists_stillDying

                    "You're still going to die, this time by drowning." if cafe and persistent.cafe_death_2:
                         jump loopStillExists_stillDying

                    "I don't know, we never got this far here before. I just have a hunch we aren't out yet.":
                         l "I see, but then there's still a chance I will li-"
                         jump restaurant_death_2
               
               label loopStillExists_stillDying:
                    if chinese:
                         l "What? Geese? That's ridiculou-"
                    else:
                         l "{size=*2}What? We need to do somethi-"
                    jump restaurant_death_2

menu allergyInterject:
     "Didn't you have a severe allergic reaction as a kid once? From what you told me it could have easily killed you.":
          if not chinese:
               if groundhog:
                    l "Really? I told you about that? When would that have been relevant?"
                    l "It's kind of crazy how much you know about me isn't it? Even I had forgotten about that story."
               else:
                    l "You know about that?... I suppose you {i}are{/i} a psychic so it shouldn't suprise me as much."
          else:
               if dumboStoryTold == True:
                    l "Oh right, how could I have forgotten? I literally just told you the story!"
                    l "Good catch [persistent.name]."
               else:
                    if groundhog:
                         l "...I must have told you that story in another loop didn't I?"
                         l "I suppose it makes sense..."
                    else:
                         if love_meter >= 2:
                              l "Oh right, I forgot about that for a moment..."
                              l "Although I had thought of it just a bit ago."
                              l "Did you really read my mind?..."
                              l "Does that mean you actually told the truth?"
                         else:
                              l "Did you learn that story from someone?"
                              l "Was all of this just a setup to make me believe you really could read minds?"
                              l "I can't do this anymore [persistent.name]. Something feels very wrong."
                              l "It's just better if I leave. Goodbye."
                              jump car_death
          
          l "So I already came into close contact with death before, but that time I didn't... you know, die."
          l "What does that have to do with this time? If it's even related at all."
          menu:
               "Maybe it's death trying to finish things and the loop trying to stop it?":
                    l "Does that mean I was supported to die...all that time ago?"
                    l "To the point Death itself grows more and more desperate in how it tries to kill me?"
                    l "Then, if the loop really is my protector, who set it up?"
                    l "Whoever or whatever would be powerful enough to go against Death?"
                    $ death_narration = "It seems in truth no one is powerful enough to face Death. I do however have a feeling [date_sub] will face it again all the same."
                    jump restaurant_death_2

               "I don't think they are linked at all, I just thought it was worth bringing up.":
                    if love_meter >= 2:
                         l "I... suppose it was?"
                         l "But don't you think we might be running out of time?"
                         l "Shouldn't we try to instead think about what will happen next?"
                         l "Or maybe try to think of a way to break this loop once and for all, without me dying?"
                         l "Surely that'd be a better use of our ti-"
                         jump restaurant_death_2
                    else:
                         l "Really? Are you sure there aren't...  {size=*2}more important matters at hand?!{/size}"
                         l "Look, I didn't mean to yell, but if you really want to save me then we shouldn't waste our time, should we?"
                         l "We should focus on finding a way to stop me from dying to break this loop."
                         l "That's clearly a better use of our ti-"
                         jump restaurant_death_2


     "*Don't say anything.*":
          n "Deciding it would be better to just let her talk you choose to not interject."
          return

label loopStillExists_forTheRestOfOurLives:
     l "I hope that won't be the case, ofcourse I'm scared to die but when my time comes after a long life I could have peace with it."
     n "[persistent.date!c] looks at you as to make sure you're processing all of this, you give [date_obj] a silent nod and [date_sub] [conj('date', 'continues', 'continue')] ."
     l "Imagine what a nightmare it would be for us. You would be forced to save an old lady that could literally die any moment, merely buying [date_obj] a few extra hours."
     l "I would be cursed with never getting to pass away, eventually becoming a heap of flesh and wrinkles after 200 or so years."
     l "No matter how much I would pray for the sweet release of death it would never come, or atleast it would always be made undone by you."
     n "[persistent.date] shudders."
     l "Let's just hope that this will all end before we reach that point."
     n "Shaken by the images of a living heap of flesh and wrinkles you can only agree with [date_obj]."
     jump restaurant_death_2

label groundhog_escapeFate:
     l "So I really keep dying?..."
     if burger == True:
          l "Before that stray bullet I never really got in close contact with death."
     elif cafe == True:
          l "Before that merlin I never really got in close contact with death."
     elif chinese == True:
          l "Before that alleged allergic reaction I never really got in close contact with death."

     if persistent.dumbo_knowledge:
          call allergyInterject
    
     l "So, why is all of this happening all of the sudden?"
     l "Surely this isn't random at all, right?"
 
     menu:
          "I think it has to do with me, you seem to die every time we're together.":
               jump groundhog_escapeFate_myFault
 
          "It seems as if it's fated.":
               jump groundhog_escapeFate_yourFate

label groundhog_escapeFate_myFault:
     n "[date_sub!c] [conj('date', 'lets', 'let')] out a nervous laugh."
     l "Sorry [persistent.name], it's just a bit too much to properly take in, scratch that, it's way too much."
     if chinese:
          if love_meter >=2:
               l "None of this feels real. I really want to believe you [persistent.name.]"
               l "Well, to an extent ofcourse. If you are telling the truth than I will probably die soon again, right?"
               l "I'd rather not, but I can tell you atleast believe what you are saying and you also did give some proof."
               l "So for now I'll play along, but I'll keep it at that, pretend. I don't feel comfortable enough to accept it as a reality."
          else:
               l "So you mean to tell me whenever we are together I \"die\"?"
               l "Seems to me there's a very easy solution to that isn't there?"
               l "Good riddance [persistent.name]."
               jump car_death
     else:
          if love_meter >= 2:
               l "Sometimes I laugh when I'm uncomfortable, it's a coping mechanism I'm afraid."
               l "It allows me to distance myself from the seriousness of any given situation."
               l "A part of me is just desperate to make light of this, to pretend like I don't believe it."
               l "Because the alternative just makes it even more real. Still, you need my help to break this loop somehow."
               l "It's not like me denying the situation is going to help at all, I'll try not to lose it. For our sakes."
          else:
               l "You have to admit that all of this sounds so unbelievable."
               l "If we didn't literally {b}just{/b} evade death there is no way I'd buy this."
               l "But now, as much as I hate to admit it, you might just be right."
               l "I don't think I can take the risk believe otherwise."

     l "So whenever we're together on a date it ends up killing me?"
     if love_meter >= 2:
          l "...what would happen if  we don't go on a date?"
          l "Have you ever tried cancelling? Maybe that would save me?"
     else: 
          l "Have you ever considered not going on this date?"
          l "Surely then I wouldn't die?"

     menu:
          "I tried to cancel the date, have it somewhere else, or just not show up, but it all ends with you dying. (Lie)" if persistent.plane_knowledge and persistent.ending_breakup and persistent.times_phone_declined > 0:
               #This is a lie. Not picking up the phone makes her live.
               jump escapeFate_myFault_ITriedTo
  
          "But I love spending time with you, I'd hate to have to throw all of that away.":
               jump escapeFate_myFault_butILoveYou
  
          "I haven't tried that yet actually.":
               jump escapeFate_myFault_didNotTryYet

label escapeFate_myFault_ITriedTo:
     l "Really?... I'm sorry [persistent.name], I don't know what to say..."
     l "Things are even worse than I thought. If everything ends up killing me, what hope is there?"
     if persistent.ending_breakup == True:
          n "Luckily for [persistent.date] [date_sub] [conj('date', 'does', 'do')] survive cancelling the date. Unluckily for [date_obj], you don't tell [date_obj] that."
          n "Why I wonder? Are you scared [date_sub] wouldn't put up with you if [date_sub] knew?"
          n "Is crushing [date_pos] hope that much better of an alternative, player?"

     l "We seem to be stuck in this loop forever."
     l "I want to believe there is a way out, I really do. However, the odds really are stacked against us."
     l "So I guess we have no choice but to go through it over and over and over."
     l "...Maybe there's still a loophole somewhere? Perhaps we just need to try something different?"
     l "Who am I kidding?... At this point I'm just trying to cope."
     l "If things have to end, I need atleast a sliver of hope left in my heart, even if it's just pretend."
     jump restaurant_death_2

label escapeFate_myFault_butILoveYou:
     if love_meter >= 2:
          l "Well, I also like spending time with you... It would be a shame if that had to end."
          l "You'd still have your memories of our time together, but for me it would be like none of it ever happened, wouldn't it?"
          l "If I could choose I'd rather hold on to my memories for now. This time with you, however unconventional, has been just what I needed."
          l "That's why it's such a shame the universe itself seems to be against it. Still, this doesn't concern the universe, right? It concerns us."
          l "Which is why we should really give it our all to find a different way. However if all else fails we might have to consider ending it."
          n "[date_sub!c] [conj('date', 'lets', 'let')] out a big sigh."
          l "Still, we can't give, surely there's another way to solve things. If all else fails we'll just have to confront the Moirai themselves!"
          
     else: 
          if not chinese:
               l "I'm not sure you understand [persistent.name], my life is literally at stake."
          else:
               l "Well, if I were to trust you, this is literally a matter of life and death, mine."
          l "Would you really squander that just because you like spending time with me?"
          l "Have you ever considered how that'd make me feel [persistent.name]? It sounds like you didn't at all."
     jump restaurant_death_2

label escapeFate_myFault_didNotTryYet:
     if love_meter >= 2:
          l "Well... it might be a worth a shot. Although I really wish there's another way."
     else:
          l "Well, I think you should."
     menu:
          "Then none of this would've happened. ":
               jump didNotTryYet_neverMeet

label didNotTryYet_neverMeet:
     if love_meter >= 2:
          n "[persistent.date!c] rubs [date_pos] chin for a moment, seemingly deep in thought."
          l "I fear you might be right."
          l "If you break this loop by not showing up at all I might not want to have anything to do with you. Even if you merely canceled things might not be the same."
          l "Even if it would be the same, I doubt you'd be convince me about us being trapped in a timeloop."
          l "Unable to relive the same moment your tricks would quite literally be useless"
          n "[date_sub!c] looks saddened for a moment before [date_sub] [conj('date', 'tries', 'try')] to give you a wide smile, you can tell it's quite forced."
          l "You know, I have a feeling we'll see eachother again somehow no matter what."
          n "[date_sub!c] [conj('date', 'grows', 'grow')] silent for a moment."
          l "Although just in case, I want you to know that I really liked our time together..."
          l "Now you know what to do next time, right [persistent.name]?"
     else:
          l "...So that's what's stopping you from doing the sensible thing?"
          l "You're clinging onto the rosecolored memories?"
          l "Then why does it feel as if you don't like me at all right now?"
          l "Look, if you truly even slightly care for me, next time you know what to do."
     jump restaurant_death_2

label groundhog_escapeFate_yourFate:
     l "...What? Why would fate have a bone to pick with me? That's rather strange isn't it?"
     l "Whatever did I do that could possibly warrant that?..."
     l "You prevented my death before, right? Maybe this is what happens by defying fate?"
     l "Maybe it is trying to correct it's mistake by making sure that what needs to happen..."
     n "[date_sub!c] [conj('date', 'trails', 'trail')] off for a moment, seemingly deep in thought."
     l "Although I'm not sure about this- It'd be horifying if I was really destined to die."
     l "There's still so much I want to do, so much to live through."
     l "That's now all ripped away, just like that. Because fate had other plans than I did."
     l "Even if we temporarily free ourselves from fate, who's to say it won't ensnare us once more?"
     l "We're at the mercy of a force we can't comprehend. We'd be in fear of it striking back for all eternity."
     l "If you knew you could die at any moment, could you really live at all?"
     menu:
          "Can't everyone die at any moment? Death is quite random in that regard.":
               l "I don't think I fully agree with that honestly... usually death has a clear cause."
               l "Even if it's as unfortunate as merely being in the wrong place at the wrong time."
               l "Even then, can't you see [persistent.name]? If anything this shows it's far from random."
               l "It would be one thing if it was just this death that happened to me, but there's others, right?"
               l "Multiple deaths at different locations and under different circumstances..."
               l "Something more is going on. I'm sure of it. Wheter it's fate or not, this can't just be merely random."
               jump restaurant_death_2

          "We precisely should try to truly live because we could die any time.":
               l "I can definetly see the logic in that [persistent.name]... I'm already dead if I never let the fear of dying go."
               l "I wouldn't be able to appreciate this extra time you gave me. Still, something is gnawing away at me..."
               l "How much extra time did you give me? Is it a day or so? A few hours? Or a few minutes?"
               if burger == True:
                    $ death_narration = "It seems [date_sub] [conj('date', 'was', 'were')] quite optimistic, you only bought [date_obj] a few extra seconds."
               elif cafe == True:
                    $ death_narration = "It seems [date_sub] [conj('date', 'had', 'have')] a few extra minutes of life thanks to you. Although maybe [date_sub] would wish [date_sub] didn't."
               
               jump restaurant_death_2 

label psychic_auraOfDeath:
     l "An aura of death? Is this some sort of joke?..."
     n "She gives you a tentative look, turning pale when [date_sub] [conj('date', 'finds', 'find')] the answer she was looking for."
     l "You're being serious?... It would explain somewhat what happened I suppose. Although why would I have such an aura?"
     l "Did I cause that somehow? Or is it something I can't help? Did something else curse me?..."
     l "All of this seems almost too silly to even entertain. Still, thank you for trying to look out for me."
     l "Do you think it is finally over? You did just save me so that must mean it is, right?"
     menu:
          "It sure is!":
               jump explanation_stoppedDeath
 
          "Actually you're still going to die, this time because of a swarm of geese." if chinese and persistent.chinese_death_2:
               jump explanation_stillDying

          "Actually you're still going to die, this time due to a gas explosion." if burger and persistent.burger_death_2:
               jump explanation_stillDying

          "Actually you're still going to die, this time by drowning." if cafe and persistent.cafe_death_2:
               jump explanation_stillDying
               
label explanation_stoppedDeath:
     if burger == True and persistent.burger_death_2 == True or cafe == True and persistent.cafe_death_2 == True or chinese == True and persistent.chinese_death_2:
          n "... Do you truly believe that player? You have seen what comes next, right?"
          n "Then why do you think something is going to change? Perhaps you're just lying to yourself?"
          n "...Or maybe you are lying to [date_obj]? Either way, both of you will find out soon enough."

     l "...I- I'm not sure what to say. Thank you, a thousand times over!"
     l "I'm not sure what I would have done without you [persistent.name]."
     n "[persistent.date!c] flashes you a wide smile, you feel as if you could beat the universe itself, as if you just did."
     menu:
          "You're finally saved, I still can't believe it!":
               jump restaurant_death_2

label explanation_stillDying:
     if chinese == False or chinese == True and love_meter >= 2:
          l "What?- What are we waiting for then [persistent.name]?"
          l "We need to get out of here as fast as possible."
          menu:
               "You're right, we have no time to waste.":
                    jump explanation_noTimeToExplain

               "We can't, you will die aswell if we step outside." if (not car_free or not car_caught) and ((burger and persistent.burger_car_death) or (cafe and persistent.cafe_car_death) or (chinese and persistent.chinese_car_death)):
                    l "So that's it?... We wait until death catches up with me?"
                    l "Can't we do anything else?"
                    if cafe:
                         l "Maybe we could go to the second floor? Surely the water can't climb up that high."
                         menu:
                              "That's a great idea, the only problem is that there is a really big and heavy closet blocking the stairway.":
                                   jump restaurant_death_2_preventionAttempt
                    elif chinese:
                         l "Maybe we could try hiding out in the restrooms so the geese can't find us?"
                         menu:
                              "That's a great idea, not like we have much other options so we'll give it a shot.":
                                   jump restaurant_death_2_preventionAttempt
                    else:
                         l "I guess not... The best we can do is seeking cover, to be somewhat safer."
                         l "So this really is it?... I'm so scared [persistent.name]."
                         menu:
                              "I am aswell [persistent.date].":
                                   l "...Is it weird that's kind of comforting? I'm glad we atleast get to share this burden together."
                                   l "You've already seen this death right? Is it bad?..."
                                   l "Actually, don't tell me, I'd prefer not to know."
                                   l "Not a whole lot of people know the exact way they will die or on what moment it will happen."
                                   l "I don't want to know the aftermath of my death aswell, I'm already cursed with too much info."
                                   l "But before..."
                                   l "Well, you know..."
                                   l "I'd just like to tell you that I don't blame you for telling me what comes next. I appreciate the honesty."
                                   l "After all, I'd like to believe we are a team. We share this burden afterall, you take it from me, but I also take it from you."


                              "It will all be over soon, don't worry.":
                                   l "I'm not sure if that makes it any better to be honest."
                                   l "Because if it'll be over soon it's also soon approaching."
                                   l "And as that moment gets closer I can feel my stomach shriveling up out of fear."
                                   l "Usually you aren't aware of when you die, even if you do it's never the specific time."
                                   l "Now we both know how it's going to end for me all we can do is just wait for the inevitable."
                                   l "It kills me how we can't do anything at all, my mind's rapidly racing trying to come up with a remedy yet can't find any."
                                   l "If I could fully accept that this is the end, maybe it'd be easier? But I can't. Accepting that would break me."
                              
                    jump restaurant_death_2

     else: 
          l "Really? I was already sceptical and now the new thing is geese killing me? That's just ridiculous."
          if psychic == True:
               $ fritfood == "word"
          else: 
               $ fritfood == "number"

          l "I can't entirely explain how you guessed my [fritfood] but this, all of this, is just some sort of practical joke, right?"
          l "Besides, it really doesn't matter if it's true or not. Your actions spoke volumes. You don't care enough about me to want to save me."
          l "If that wasn't the case, why would you treat me this way? I'm out [persistent.name], whatever this is, I don't want a part in it."
          jump car_death
          
label restaurant_death_2_preventionAttempt:
     if burger and burger_car_death:
          $ stillDying_noEscape = True
     if cafe and cafe_car_death:
          $ stillDying_noEscape = True
     if chinese and chinese_car_death:
          $ stillDying_noEscape = True
          
     if cafe:
          l "Is it really that heavy? We don't need to move it all the way afterall, just enough to slip past."
          l "Let's check it out, just in case."
          n "[persistent.date!c] and you walk to the enormous closet made of lignum vitae."
          n "[date_sub!c] [conj('date', 'inspects', 'inspect')] it for a brief moment, placing [date_obj] firmly against it. Then [date_sub] [conj('date', 'starts', 'start')] pushing with all of her might." 
          n "However, the closet refuses to even budge in the slightest."
          n "Soon a few guests closest by turn to judge the situation."
          n "This seems to serve as a big enough nudge to steer her away from continuing her efforts."
          l "...There is no way we can move {b}{i} that{/i}{/b}, right? Why is it placed so terribly anyway?"
          l "Maybe we should just ask the barista? Maybe there is other staff somewhere that could help clear the stairway."
          n "[persistent.date!c] and you walk away from the closet and are heading towards the barista. As [date_sub] [conj('date', 'passes', 'pass')] you, you notice the urgency in [date_pos] step."
          l "Hello, I'm really sorry to bother you, but we wanted to go to the second floor and noticed this gigantic close-."
          b "Ah yes, the closet... I'm really sorry about that."
          b "Our manager thought it would be a nice display piece on the second floor."
          b "... He may have slightly understated how many steps the stair {b} really {/b} has to get out of paying an extra moving fee."
          b "When the crew saw for themselves, they left it right there."
          b "We're currently looking into getting it upstairs safely. Our manager said the job would be done by tomorow."
          b "In the meantime I'm afraid you can't go up there, we are sorry for the inconvenience."
          menu:
               "But it's an emergency! We need to get that closet out of the way now!":
                    b "What is the emergency?"
                    menu:
                         "We really want to see rest of the aquarium upstairs.":
                              
                              b "I'll be with you in a bit. There are some other customers that need to be served first."
                              n "It might be your imagination but the barista seems to be deliberately taking his time with every customer."
                              n "When everyone is finally served he looks around one last time to see if no one else, anyone else, needs him."
                              n "He even waits for a few seconds in the hope that someone might want to order something extra and delay him from talking to you, even if just for a minute or so."
                              n "When no one comes by the barista lets out a heavy sigh and tries to put on a fake smile."
                              n "It fails miserably. For a second you can see he is thinking about whether or not to attempt it again but he just shakes his head ever so slightly and drops his fake smile instantly."
                              b "Look, while I understand that the both of you want to take a look, that is far from an emergency in my eyes."
                              b "If you really want to do so I would recommend to come back after tomorow, by that time the closet will be removed."
                              n "But you don't have until then, in fact every word the barista utters makes you uttery aware of how little time you have left."
                              n "Suddenly the sound of cracking glass begins to rapidly spread all over the aquariums."
                              n "The weakened glass can't contain the water much longer as it bursts through its confines."
                              n "The water pouring out of the aquariums, the fish flopping on the floor, disaster is impending once more."
                              n "The floor is covered in about a few centimeters of water already. The people in the cafe desperately make their way to the exit."
                              l "When they notice the exitseems to be stuck panic grows even more. They push against it with all of their strength, but the door doesn't even budge."
                              n "Soon the fish are no longer flopping, instead freely swimming around in the water, whihc now is flowing up to your middle."
                              n "[persistent.date!c] and you give eachother a knowing look."
                              if love_meter > 2: 
                                   n "The two of you wait for death in eachothers arms."
                              else: 
                                   n "All you can do is wait for death."

                              n "You do not have to wait long at all for it."
                              jump gameOver

                         "We are all going to die! This whole place will flood!":
                              n "Upon speaking those words the commotion in the cafe turn into pure silence."
                              n "All the people happily chatting it away while eating, instead just staring at you. Then they start to whisper."
                              n "The barista notices too, his face rapidly growing pale."
                              b "Listen, I'm kindly going to have to ask you to leave, you are scaring our customers."
                              b "The cafe won't flood, the aquariums are very sturdy."
                              n "He tries to say that last part as convincing and assuring as a slightly awkward teenager can."
                              n "Sadly, regardless of the quality of his performance, your words robbed a lot of people their appetite."
                              n "Quite a few customers begin to leave."
                              n "The barista looks even more terified now."
                              b "I would like you to leave now please, or I will have to call the cops." 
                              n "[persistent.date!c] and you shamefully start headingtowards the exit."
                              l "I think you might have come across slightly too strong [persistent.name]."
                              n "Things are quiet for a moment, the few customers that remain just awing at you in silence."
                              l "...So, when we step outside we- I'll die, right?"
                              n "[date_sub!c] [conj('date', 'whispers', 'whisper')] it, not wanting to freak out the remaining customers even more."
                              l "But if we stay here we drown... I guess getting hit by a car is better in that case? Probably a lot quicker."
                              n "You can cleary hear the fear in [date_pos] voice, even though [date_sub] [conj('date', 'is', 'are')] trying to seem put together."
                              l "Still, I feel slightly better knowing some customers escaped through our failed attempt."
                              n "The two of you leave the cafe in shame."
                              if persistent.cafe_car_death == True:
                                   n "Just like clockwork the red Sedan shows up once more."
                              elif persistent.chinese_car_death or persistent.burger_car_death or persistent.kokiri_death_2: 
                                   n "Suddenly you notice the red Sedan. It seems you aren't safe from it in here either." 
                              else: 
                                   n "Suddenly you notice a red Sedan."
                              n "It drives straight into the two of you."
                              jump car_death_result
     elif chinese:                 
          n "[persistent.date!c] and you walk into the women's restroom together."
          n "There is no one else there. You smell the destinct scent of roses, upon further inspection it seems to come from an aroma difuser."
          l "So, in here we should be safe, right?"
          n "You can only hope, but you are far from certain."
          n "Suddenly you hear it again. The sound of screaming, slowly overpowered by quacking."
          l "So that is how I died?... It's hellish."
          n "For a moment you consider telling [date_obj] you're unsure if [date_sub] died to the geese but that might have been the best to come out of that situation."
          n "You refrain from telling [date_obj] that, it would probably sound rather strange."
          n "[persistent.date!c]’s hands tremble as [date_sub] [conj('date', 'grips', 'grip')] the edge of the sink."
          n "[date_pos!c] breathing shallow and uneven, [date_pos] eyes darting around the small restroom as though expecting the walls themselves to collapse inward."
          n "Tears well up but don’t fall, [date_pos] face frozen in a mixture of fear and desperation."
          l "This isn’t real, right? I mean... it can’t be real. It’s just geese. Just stupid birds..."
          n "This could not end soon enough for the two of you. Yet it doesn't seem to any time soon."
          n "In fact, it seems to last longer than you remember. Something's different, but what?"
          n "It's the same day over again, right? Nothing can be different except..."
          n "Except you, hiding with [persistent.date] in the bathroom."
          n "Are they searching you? No, last time they didn't take you with them."
          n "They are searching [date_obj]."
          n "The restroom door bursts open with a deafening bang, the force rattling the hinges."
          n "A cacophony of flapping wings and maddening quacking fills the air as several geese flood into the small room, their eyes gleaming with malicious intent."
          n "[persistent.date!c] lets out a strangled scream, backing away until [date_sub] [conj('date', 'is', 'are')] pressed against the tiled wall."
          n "You try to shield [date_obj], but it's futile. You are no match for 100 geese, nor 1000 geese, nor an uncountable amount of them."
          n "The restroom door bursts open with a deafening crash, and before you can fully process what’s happening, a blizzard of white feathers engulfs the room."
          n "You try to shout, to do something, but before you can make another sound, everything turns to white, the white of pesky geese feathers."
          n "The pain you feel is excruciating, sharp and overwhelming, as the geese descend upon you like a merciless force of nature. The cacophony of honking grows distant as darkness takes over, and you fall unconscious."
          n "When you wake up again, the restroom is silent and [persistent.date] is gone."
          n "The room is completely filled to the brim with geese feathers. Just thinking about it makes your nose itch, and you begin to sneeze uncontrollably."
          n "Between sneezes, you notice it, the same sticky note they left last time, on your hand once again."
          n "You already know what it says but decide to read it anyway."
          n "It reads as follows: \"We took everyone and you won't be seeing them back. Let this be a lesson on why you should not eat or serve geese or ducks, as those are also part of our family. Also, we are not stupid. - Sincerely, the geese\""
          jump gameOver

label psychic_dateToSave:
     l "...That's rather convoluted isn't it?..."
     l "Couldn't you just have told me this like a week before it would happen?"
 
     menu:
          "Oh yeah, and you would just believe a random person telling you that you will die of an allergy in a Chinese restaurant on a specific day?" if burger:
               jump psychic_dateToSave_youWouldNotBelieveMe
  
          "Oh yeah, and you would just believe a random person telling you that you will die by being crushed by a great white shark in a fish themed cafe on a specific day?" if cafe:
               jump psychic_dateToSave_youWouldNotBelieveMe
  
          "Oh yeah, and you would just believe a random person telling you that you will die because of a gunshot wound in a burger restaurant on a specific day?" if chinese:
               jump psychic_dateToSave_youWouldNotBelieveMe

label psychic_dateToSave_youWouldNotBelieveMe:
     if burger or cafe:
          l "I suppose that is a fair enough point, even right now, with you preventing it I don't entirely believe it.."
     else:
          l "I suppose that is a fair enough point, even right now I don't believe it fully."

     l "It still sounds like there were better, less convoluted ways to save me. However that doesn't change that you did."
     l "We actually escaped death itself, take that death!"
     menu:
          "I think it might not be wise to tease death itself. ":
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
     l "Common, let's celibrate. We just cheated death!"
     l "Don't be so worried, what's the worst thing that could happen?"
 
     menu:
          "Yeah, you're probably right- Wait, why did you say that? Now we are going to die for sur-.":
               jump restaurant_death_2

label youwouldntbelieveme_teaseDeath:
     $ teaseDeath = True
     n "[persistent.date!c] and you high five eachother, you've won. Congratulatons!"
     if persistent.teaseDeath_fakeOut_knowledge == False:
          n "That's what I'd say if either of us thought it was the truth. After all, you came back here for a reason didn't you?"
     jump restaurant_death_2

label psychic_justHelpingOut:
     if chinese == True:
          l "So you somehow sensed I'm allergic to something in this dish? That sounds really far-fetched if I'm being honest."
          l "There's certainly a possibility that I might be unaware of an allergy to an ingredient, but you {b}sensing{/b} it?"
          if love_meter == 1:
               l "What, are you a psychic allergist? Well, I get the gist alright, the gist that you are just making this nonsense up as you go."
               l "Although... there is {i}some{/i} truth to what you are saying, isn't there?" 
               l "I feel it somehow. I guess that makes me a psychic too, huh?"
               n "[date_sub!c] practically [conj('date', 'scoffs', 'scoff')] those words at you."
               l "So, am I safe now? Or is there still something else?"
          else: 
               l "That's where I struggle to accept this whole scenario a bit."
               l "Although somehow, I don't think you're lying about the allergy thing. Besides, I can either believe you or risk it and maybe die."
               l "The food here is to metaphorically die for, but I wouldn't like to make that literal."
               l "I think I'll just order something different, probably something small though. A prophesied death isn't exactly stimulating for the appetite."
               l "Anyway, that's not my main concern right now, am I safe now?"
     else:
          l "Now that's quite the story. It might be hard to believe but I guess you are right."
          l "I don't really want to think about what would have happened if you didn't interfere..."
          l "So am I in the clear now?"
     menu:
          "Yes, you are completely safe now!":
               jump psychic_justHelpingOut_totallySafe

          "Actually I sense another death approaching, this time it will be a swarm of geese." if chinese and persistent.chinese_death_2:
               jump explanation_stillDying

          "Actually I sense another death approaching, this time it will be a gas explosion." if burger and persistent.burger_death_2:
               jump explanation_stillDying

          "Actually I sense another death approaching, this time you will drown." if cafe and persistent.cafe_death_2:
               jump explanation_stillDying

label psychic_justHelpingOut_totallySafe:
     n "[persistent.date!c] gives you a thumbs up and plays a few notes on an air gitar."
     l "We actually did it, that's awesome!"
     n "[persistent.date] opens [date_pos] arms and motions to you with [date_pos] head."
     l "Come and give me a hug [persistent.name]"
     $ hugRequestedBeforeDeath = True
     jump restaurant_death_2

label prevented_psychic:
     $ psychic = True
     $ groundhog = False
     if burger == True:
          l "So you knew I was going to get shot because you're psychic?"
          l "However thankful I am for you saving me you have to admit that sounds quite far-fetched."
          l "Do you have any proof to maybe show you're a psychic?"
     if chinese == True:
          l "So you knew I was allergic to something in this dish because you are psychic?"
          l "Unless you have proof it's quite convenient that I can't test out your claim, isn't it.?"
     if cafe == True:
          l "So you knew I was going to be skewered by a merlin because you are psychic?"
          l "However thankful I am for you saving me you have to admit that sounds quite far-fetched."
          l "Do you have any proof to maybe show you're a psychic?"
 
     menu:
          "I'm not sure how to convince you honestly":
               jump prevented_noProof
 
          "Alright, pick a word, doesn't matter which one but make it hard to guess.":
               jump prevented_proof 

label prevented_silent:
     l "...Listen, I can't do this."
     if chinese:
          l "You can't just say something like that without elaborating."
          if love_meter < 2:
               l "Is this your idea of a joke? It's sick."
               l "I'm done, this is too much for me."
          else:
               l "Look, I really want to believe you [persistent.name]."
               l "But you need to understand that you give me very little to work with here."
               l "This just comes of as weird if I'm being honest."
     else:
          l "You can't just not give me any explanation after what just happened."
          l "I'm really thankful for you saving my life and everything but I think at the very least I deserve one." 
          l "I want to understand [persistent.name], I really do., but this is just too much."
     l "I think it's better for the both of us if I just leave."
     jump car_death

label explanation_noTimeToExplain:
     if chinese == True:
          if car_caught == True:
               if persistent.fleeingDeaths_counter_knowledge == 0:
                    n "Together you burst through the exit, bracing yourself for the impact of the red Sedan."
                    n "However, nothing happens. It seems like your call to the police worked out well enough."
               else: 
                    n "Together you burst through the exit, finally having dealt with the drunk driver."
               n "Once out the two of you continue to run as if death itself follows."
               n "[persistent.date!], still unaware of why [date_sub] even [conj('date', 'is', 'are')] running, merely doing so because [date_sub] [conj('date', 'doesn', 'don')]'t want to find out whatever you're running away from."
               
               if persistent.fleeingDeaths_counter_knowledge == 0:
                    n "Eventually the two of you pass by the side of an empty street. The calm feels like a welcome break from all the chaos you have been slowly getting accustomed to."
                    n "It's not quiet for long, as soon the sound of screeching wheels and loud laughter takes it place."
                    n "When you try to look at the source of the noise you see a bus full of elderly people barreling straight towards you and [date_obj]."
                    n "You manage to jump away from it just in the nick of time but [persistent.date] of course doesn't."
                    n "You know what you have to do, you've come too far to just give up now."
                    $ persistent.fleeingDeaths_counter_knowledge += 1
                    menu: 
                         "I retry.":
                              jump explanation_noTimeToExplain

               if 0 < persistent.fleeingDeaths_counter_knowledge < 3:
                    n "Once again the two of you are found themselves on the sidewalk of the empty street. Taking a deep breath before things turn to the same tumult you know well by know."
                    n "This time you manage to push [persistent.date] aside right before the bus barrels towards her. Besides a bruised arm [date_sub] [conj('date', 'is', 'are')] unharmed."
                    n "You quickly help [date_sub] back up before you continue running to escape your fate."
                    
                    if persistent.fleeingDeaths_counter_knowledge == 1:
                         
                         n "Mere moments after the bus you saved [date_sub] from a truck tumbles towards the two of you."
                         n "You curse at the sky, trying to reach whoever just now caused her to die."
                         $ persistent.fleeingDeaths_counter_knowledge += 1
                         menu: 
                              "I retry.":
                                   jump explanation_noTimeToExplain

                    if persistent.fleeingDeaths_counter_knowledge == 2:
                         n "With your knowledge of the truck the both of you manage to barely slip by it. Time is begining to blend together with how many times you have been here. It almost seems like you just pick right up where you left of."
                         n "Determined, you continue running until the sound of thunder. Lightening strikes."
                         n "However, this time it appears [date_sub] [conj('date', 'is', 'are')] lucky, as it hits right past [date_sub]."
                         n "Suddenly fire erupts up from the ground. It seems the truck began to leak it's fuel. Right, you did think it was odd you got a lucky break."
                         n "The flames try to consime [date_obj], the hungry tongues don't let off until [date_sub] [conj('date', 'is', 'are')] beyond saving."
                         $ persistent.fleeingDeaths_counter_knowledge += 1
                         menu:
                              "I retry once again.":
                                   jump explanation_noTimeToExplain

               else:
                    if persistent.fleeingDeaths_counter_knowledge == 3:
                         n "You run to a diverging street, knowing full well that other empty street is cursed."
                         n "Suddenly you feel a terrible trembling coming from the ground."
                         n "It almost resembles an earthquake, but not quite."
                         if persistent.kokiri_death_4 == True:
                              n "It actually kind of reminds you of what you felt when the ufo revealed itself in the kokiri forest."
                         n "It seems to very quickly pass for an earthquake As soon as it started it ends, [persistent.date] is even still alive."
                         n "However, a safety hazard of a building that shouldn't have been built in the first place collapses in, right on [date_obj]."
                         $ persistent.fleeingDeaths_counter_knowledge += 1
                         menu:
                              "Retry. Retry. Retry.":
                                   jump explanation_noTimeToExplain

                    if persistent.fleeingDeaths_counter_knowledge == 4:
                         n "This time the two of you reach your car parked a few streets further, you decide to try to drive away as far as you can."
                         n "After driving for a while you pass a bigger city, maybe things will be safe here?"
                         n "You look [persistent.date] in the eyes, praying for [date_sub] safety."
                         n "The prayer gets cut short, seemingly by a cacaphony of animal sounds. Glancing in the side mirrors shows a swarm of animals stampeding towards you."
                         n "Immediately you spring into action, pressing your foot on the gas as hard as you possibly can, but then you notice something."
                         n "Weren't you planning on filling up your car after the date? Right then the car abruptly stops, not budging anymore no matter how hard you try to persuade it."
                         n "The stampede passed by around and over your car. In theory this should be fine, in practice there were also elephants among them."
                         $ persistent.fleeingDeaths_counter_knowledge += 1
                         menu: 
                              "Sigh, retry.":
                                   jump explanation_noTimeToExplain

                    if persistent.fleeingDeaths_counter_knowledge > 4:
                         n "From now on you filled up your car in advance for the inevitable chase scene."

                         if persistent.fleeingDeaths_counter_knowledge == 5:
                              n "While speeding away as fast as possible from the stampede, more structures start to collapse, even the sturdier ones."
                              n "Things are becoming more and more over the top, but right now the mess is not your main concern, it's getting [date_sub] out of it."
                              l "[persistent.name], if we make it out of this city, where are we going next? Can't you see that whatever is happening won't stop?"
                              l "It's not as if we could leave the earth so eventually we will be cornered, having nowhere to escape to."
                              n "[persistent.date] gave you the greatest idea. Hugging [date_obj] tightly you tell [date_obj] [date_sub] [conj('date', 'is', 'are')] genius."
                              n "[persistent.date] turns beetred."
                              l "Oh, I wouldn't know about that... Although hang on, you aren't seriously thinking about leaving the planet, right?"
                              l "How would we even do that?"
                              n "Lifting your foot of the gas pedal you wait for death to cath up you and it sure does so fast."
                              n "Another car, trying to escape the commotion, crashes right against yours."
                              n "Even without checking it's clear [persistent.date] did not make it."
                              $ persistent.fleeingDeaths_counter_knowledge += 1
                              menu: 
                                   "Retry, this could be it!":
                                        jump explanation_noTimeToExplain

                         if persistent.fleeingDeaths_counter_knowledge > 5:
                              n "Remembering what [persistent.date] said, you drive straight to the kokiri forest. The ufo could be your way out."
                              n "After scaling the hill you manage to eventually stumble upon one of the entrance hatches."

                              if persistent.fleeingDeaths_counter_knowledge == 6:
                                   n "However, an onslaught of unidentifiable buttons, levers and contraptions await you."
                                   n "It seems the controls will take some time to learn before you'll be able to get out of here."
                                   menu: 
                                        "I'll retry untill I get it right!":
                                             n "After more than a hundred attempts you manage to take of without instantly plummeting to your death."
                                             $ persistent.fleeingDeaths_counter_knowledge += 1
                                             jump explanation_noTimeToExplain

                              if persistent.fleeingDeaths_counter_knowledge > 6:
                                   n "Upon lifting off into space the sun absorbs the earth, seemingly atleast a milion years too early. Things are really getting out of hand aren't they?"
                         
                              if persistent.fleeingDeaths_counter_knowledge == 7:
                                   n "Suddenly a speeding ufo smashes into yours. The ship analysis informs you the driver was drunk."
                                   n "It seems that even in space there are drunk drivers."
                                   menu:
                                        "Retry. Retry. Retry and retry once again.":
                                             $ persistent.fleeingDeaths_counter_knowledge += 1
                                             jump explanation_noTimeToExplain
                              if persistent.fleeingDeaths_counter_knowledge == 8:
                                   n "Things blend together even more. Wheter or not you even progress remains to be seen."
                                   n "Death by colliding stars."
                                   
                                   $ persistent.fleeingDeaths_counter_knowledge += 1
                                   menu:
                                        "Retry.":
                                             jump explanation_noTimeToExplain
                              if persistent.fleeingDeaths_counter_knowledge == 9:
                                   n "Death by a storm of asteroïds."
                                   
                                   $ persistent.fleeingDeaths_counter_knowledge += 1
                                   menu:
                                        "Retry.":
                                             jump explanation_noTimeToExplain
                              if persistent.fleeingDeaths_counter_knowledge == 10:
                                   n "Death by crashlanding on a planet."
                                   $ persistent.fleeingDeaths_counter_knowledge += 1
                                   menu: 
                                        "Retry.":
                                             jump explanation_noTimeToExplain
                         
                              if persistent.fleeingDeaths_counter_knowledge > 10:
                                   jump explanation_noTimeToExplain_ufoTalk
          else:
               jump explanation_noTimeToExplain_hitByCar
     else:
         
          label explanation_noTimeToExplain_hitByCar:
               if burger == True:
                    $ resname = "burger restaurant"
               elif cafe == True:
                    $ resname = "cafe"
               elif chinese == True:
                    $ resname = "Chinese restaurant"

               n "As [persistent.date] and you run out of the [resname] together you spot something that makes your stomach drop."
               n "You see a red Sedan."
               n "Not just any red Sedan, but the one you wish you could never see again."
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
               n "You try to ignore it, try to change it, by attempting to push [persistent.date] aside as fast as you can."
               n "But no matter how hard your mind tries to fight it, your body is frozen in place."
               n "Your mind is flooded with thoughts that all somehow overlap, causing you to be barely able to make sense of any of them."
               n "You let out a bloodcurdling scream for [date_obj] to move away, for anyone to save [date_obj] somehow."
               n "But as you get flung aside by the car, you already know what happened to [date_obj]."
               n "No one could save [date_obj] this time, just like the last time. And just like the next time, if nothing changes."
               n "The horrible aftermath you tried so hard to avoid has caught up with you once again."
               jump gameOver

label explanation_noTimeToExplain_ufoTalk:
               n "The universe settles, seemingly growing tired from the onslaught of deaths."
               n "Setting the ship to steer automatically you step away from the controls."
               n "[persistent.date] just stands there, if [date_sub] [conj('date', 'was', 'were')]n't shivering [date_sub] would be completely stuck in place."
               l "{size=*0.5}...It's- all gone? No, no, no. No!{/size}"
               l "{size=*0.5}This, it's not real. That's it! It's all just a nightmare.{/size}"
               l "{size=*0.5}I will wake up any moment now. Any moment... please wake up.{/size}"
               menu:
                    "This is not a dream [persistent.name].":
                         l "It isn't? But then, this is real? How do you explain any of this?"
                         l "How did you know about the Kokiri forest, or that there was an ufo there?"
                         l "Scratch that, how in the world do you even know how to fly it succesfully?"
                         l "What's this all about? {size=*0.5}Are you... an alien?{/size}"
                         if groundhog == True:
                              l "Or are you really in a timeloop?"
                         else:
                              l "Or are you really a psychic?"
                         
                         menu:
                              "Actually neither. You are a character in a game, I am the player and need to keep you safe.":
                                   l "{size=*0.5}I'm a character in a game? Yes! None of this is real, that must be the truth.{/size}"
                                   l "{size=*0.5}Nothing happened, my family is still fine, it's just pretend...{/size}"
                                   l "The speed with which you said that... I assume we've had a similair chat a few times?"
                                   n "You nod your head."
                                   l "I see... So does that mean we went to all three restaurants some other time?"
                                   menu:
                                        "Yes, we did, we also went to the Kokiri forest and visited the beach.":
                                             l "... So that's how you know about the Kokiri forest?"
                                             l "it makes sense, I've never told anyone that name afterall."
                                             l "Quite clever, even if I'm not sure how you convinced another version of me to tell you, [persistent.name]."
                                             l "Sounds like we had quite a busy first date, didn't we?"
                                             n "[persistent.date] laughs."
                                             l "It's a shame I don't remember anything of it though, what was your favourite place we went?"
                                             menu:
                                                  "Probably the beach.":
                                                       $ persistent.favouriteFirstDate = "beach"
                                                       jump ufo_talk_favouriteFirstDate
          
                                                  "Probably the burger restaurant.":
                                                       $ persistent.favouriteFirstDate = "burger"
                                                       jump ufo_talk_favouriteFirstDate
          
                                                  "Probably the cafe.":
                                                       $ persistent.favouriteFirstDate = "cafe"
                                                       jump ufo_talk_favouriteFirstDate
          
                                                  "Probably the Chinese restaurant.":
                                                       $ persistent.favouriteFirstDate = "chinese"
                                                       jump ufo_talk_favouriteFirstDate
          
                                                  "Probably the Kokiri forest.":
                                                       $ persistent.favouriteFirstDate = "kokiri"
                                                       jump ufo_talk_favouriteFirstDate
     
                    "*Stay silent*" if persistent.ufoCrash_knowledge:
                         n "You can't bare talking to [date_sub]. Not after knowing what is to come."
                         n "[persistent.date] is too shocked [date_ref] to break the silence. Maybe it's better that way?"
                         n "Hopefully it will make the next part less hard."
                         jump ufo_alert
     
label ufo_talk_favouriteFirstDate:
     if persistent.favouriteFirstDate == "beach":
          l "Great minds think alike, I also absolutely love the beach!"
          l "There's just so much you can do there. What was your favourite thing we did [persistent.name]?"

     elif persistent.favouriteFirstDate == "burger":
          l "Why does that not suprise me one bit? Rose's burgers are just unbeatable when it comes to their amazing taste!"
          l "Just thinking about it now makes me really yearn for a juicy cheeseburger."
          n "[persistent.date]'s stomach growl as [date_sub] quickly [conj('date', 'places', 'place')] a hand on it as to quiet it down."
          n "[date_sub!c] [conj('date', 'turns', 'turn')] beetred."
          l "Uhm anyway, was their anything in particular you liked on that date [persistent.name]?"

     elif persistent.favouriteFirstDate == "cafe":
          n "You tell [date_obj] how beautiful the aquariums of the cafe are."
          l "...That sounds absolutely wonderful!"
          l "I'm having a hard time imagining it though, I wish I could see it for myself. Not like I can anymore..."
          l "Well, I suppose I did, didn't I?"
          l "I just wish I could remember it, that I could remember all of our dates together."
          l "However, I can ask straight from the source. Imagine there's one thing we did that you really want to share, your favourite."
          l "What would it be [persistent.name]?"

     elif persistent.favouriteFirstDate == "chinese":
          l "That was your favourite? I'm glad I got to share it with you then!"
          l "Well, unless it was a different version of that date, even then, you still got to share it with another me."
          l "Although I secretely hope you meant this specific date if I'm being honest, even if this date surely didn't go as planned."
          l "If it isn't I can't blame you, we hardly spent any time in the chinese restaurant itself now, and then there was all that chaos..."
          l "What made that date specifically your favourite [persistent.name]? Maybe we can still one-up it."
          n "[persistent.date] gives you a cute little smile."
          l "I'd like that."

     elif persistent.favouriteFirstDate == "kokiri":
          l "I still can't even believe that we went there. It's a lovely place for a date, but like I said, I'd never would have thought I'd tell anyone..."
          l "Those woods are very special to me after all."
          if love_meter >=2 :
               n "[date_sub!c] [conj('date', 'thinks', 'think')] to [date_pred] for a brief moment."
               l "But then again, if I have to share it with anyone, I'm happy it got to be you."
          l "Was there anything we did there close to your heart [persistent.name]?"
          
     
     $ renpy.input("My favourite moment was...")
     l "That sounds really lovely [persistent.name]!"
     $ renpy.input("")
     l "That sounds great!"
     $ renpy.input("")
     l "..."
     $ renpy.input("")
     l "..."
     n "[persistent.date] is staring right into your soul without saying a word."
     n "[date_sub!c] somehow [conj('date', 'seems', 'seem')] to have lost everything that made [date_obj] feel human."
     $ renpy.input("")
     l "..."
     n "Once every room felt more warm because of [date_pos] presence, now this iron ship feels colder than ever with [date_pos] silence in it."
     n "It's almost seems as if [date_sub] [conj('date', 'has', 'have')] run out of things to say. Was the game programmed with responses for her this far out at the edge of the universe?"
     $ renpy.input("")
     n "In [date_pos] frozen, wordless nature [date_sub] [conj('date', 'seems', 'seem')] more like a replica of the woman you once knew than the real deal."
     n "You have seen [date_obj] die many times but this somehow feels even more wrong. A fate worse than death has befallen [date_obj]."
     $ renpy.input("")
     n "Just then you hear something. Not [date_sub], it's a loud beeping sound emanating from the ship itself."
     jump ufo_alert

     label ufo_alert:
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
     $ persistent.ufoCrash_knowledge = True
     n "For the longest while there was nothing. Nothing except darkness."
     n "Then, for a very brief moment, you were. Before that soon too came to pass."
     n "Now, there is yet once again darkness for all of eternity."
     n "No. That can't be right, can it? The darkness will come ofcourse, but this is not that."
     n "It seems you were just knocked out from the aftermath of...whatever happened with on the ufo."
     n "You might have risen from the dark slumber but your eyelids are still shut close, wanting noting but to sleep."
     n "As you fight them you consider just losing on purpose, nothing makes sense anymore."
     n "This was probably caused by the entire universe collapsing in on you. On you and on..."
     n "On [persistent.date]- The thought of [persistent.date] snaps you out of your confused state in an instant."
     n "You force your eyes open and with all the willpower you can gather bite through the pain as you crawl back up."
     n "Desperately searching for [date_obj] all you can find is bright white emptiness."
     n "The very emptiness her death always leaves you with."
     
     n "Bright white emptiness and a floating trail of gigantic polaroids. The white borders of the polarioid were seemingly melting over in the emptiness."
     n "It turns out you are standing on one of those giant polarioids, the picture shows your messy room. Hang on, how is that possible? How is any of this possible?"
     n "Perhaps to feed the curiosity, perhaps because it's the only way forwards, but you decide to follow the trail."
     $ polaroidzone_picture = 0
     jump ufo_crash_polaroids
 
label ufo_crash_polaroids:
     #TODO: Add some small descriptions of each picture you jump on Rewrite this part some other time well enough
     #Reality is glitching so that you won't have to draw every picture.
     #Picture ideas, if you did bad things have those too
     if polaroidzone_picture == 1:
          n "Bracing yourself for a moment you run as fast as you can before taking a leap of faith, landing right on the middle of the next polaroid."
          #This will showcase a picture of your first date ever "your face still looked like you were all taking it in for the first time"
          if persistent.firstLocation == "burger":
               "Filler"
          elif persistent.firstLocation == "cafe":
               "Filler"
          elif persistent.firstLocation == "chinese":
               "Filler"
          else:
               "Error, no first location found."
     
     elif polaroidzone_picture == 2:
          n "Knowing you can't stop now all you can do is take the next leap."
     elif polaroidzone_picture == 3:
          n "For all these jumps so far it doesn't seem like you're making much progress."
          #A picture here maybe where it didn't seem like you were making a lot of progress to mirror the feeling now?
     elif polaroidzone_picture == 4:
          n "However, you beging to notice something of in the distance, at the end of the trail."
     elif polaroidzone_picture == 5:
          n "That \"something\" seems to somewhat resemble a human, although from this distance it could just be your brain playing tricks on you."
     elif polaroidzone_picture == 6:
          n "The strenght in your legs faltered for a moment, you barely manage to grab the edge of the polaroid to save yourself from falling to your death."
          n "Praying for your arms to still have some remaining strength you slowly pull yourself up."
          n "Catching your breath after performing such a feat you once again catch a glimpse of the mysterious figure."
          n "It indeed seems to be a human, wearing a grey hoodie."
          #The picture here where Lilith pulls you back up from the hill maybe? And if you don't have that a backup.
     elif polaroidzone_picture == 7:
          n "Your legs growing more and more sore, luckily you are even closer than before. "
          n "The figure has their back turned to you. You can't help but wonder what brought them here. Are they like you?"
     elif polaroidzone_picture == 8:
          #If the player has seen the neverending, always show that one here (since it is the eighth picture, infinity), otherwise show a regular ending here.
          n "Only one more picture between the two of you, you ignore your legs screaming for help a third time and jump."
     elif polaroidzone_picture == 9:
          n "This is it, the next jump is the final one. You'll finally reach the mysterious figure"
     elif polaroidzone_picture == 10:
          jump ufo_crash_polaroids_James
 
     menu:
          "*Jump to the next picture*":
               $ polaroidzone_picture += 1
               jump ufo_crash_polaroids

label ufo_crash_polaroids_James:
     n "Upon finally reaching the figure they slowly turn to face you before you can even do or say anything."
     n "They seem to be a teenager, their grey hoodie being slightly ripped open right in the middle, revealing their ribcage."
     j "Welcome [persistent.name]. I was expecting you."
     j "This place must be quite strange for you, let's move something more... familiar."
     j "You and the teen are now standing in your bedroom, where all fo this started. Where it has started so many times after it ended."
     j "Don't be fooled, this room was destroyed alongside everything else when the universe collapsed, it's merely an illusion."
     j "I just it might be easier on the eyes to talk here, and we need to talk, about-about all of this."
     j "I assume you already know who I am?"
     menu:
          "You must be [persistent.date_ghost], right? [persistent.date] told me about you.":
               $ persistent.met_james = True
               j "There it is, I thought [date_sub] would sooner than later."
               j "Getting this far without having heard of me would be pretty hard."
               j "[date_sub!c] still [conj('date', 'carries', 'carry')] the weight of my loss with [date_obj]."
               j "Which is fully understandable, even though I wish [date_sub] and the rest of our family could finally be free."
               j "Then again, I could have moved on years ago yet still didn't. So I guess we're all in the same boat."
               n "It's quiet for a moment, you hear nothing except a low droning sound."
               j "[persistent.date_ghost] gives you a curious look, it feels somehow slightly unsettling."
               j "How do you feel about [persistent.date], [persistent.name]?"
               n "Not expecting the question you are taken aback for a second."
               menu:
                    "I really love [date_obj].":
                         $ loveher = True
                         $ persistent.jamestalk_iloveher_knowledge = True
                         n "[persistent.date_ghost] lets out a big sigh of what could very well be relief."
                         j "If that's the case then this talk might be easier than anticipated."
                         j "You have seen [persistent.date] die about [persistent.lildeaths] times, right?"
                         n "You nod, wishing you could unsee every single one of them."
                         j "So you're trying to save [date_obj] and that is what brought you here for example?"
                         n "You nod."
                         if persistent.lilithAliveAndRetriedCounter >= 1:
                              j "I see. However, you came back after [date_sub] didn't die, why?"
                              jump jamesChat_whyDidYouReturn
                         else:
                              j "That's what I was hoping to hear, I can't thank you enough for all of this [persistent.name]."
                              j "I'm just worried what will happen when [date_sub] [conj('date', 'is', 'are')] saved."
                              j "Those outcomes might be less than... statisfying for you."
                              j "If [date_sub] [conj('date', 'lives', 'live')] the two of you pretty much never end up together."
                              j "...Isn't that why you started playing this game in the first place? To find an ending where the two of you live happily ever after?"
                              j "Well, what happens if you won't find an ending like that? If every ending even resembling something like that feels... off."
                              j "I fear you might drive yourself mad searching something that could only every exist in your mind."
                              j "Can you promise me that if you save [date_obj], you won't come back again?"
                              j "That you won't put [date_obj] through any more death and stress than is truly necessary?"
                              call jamesChat_promiseToStop
   
                    "I really like [date_obj].":
                         $ likeher = True
                         j "Let me ask you something. If you like [date_obj], are you doing this for [date_pos] sake?"
                         n "The question catches you off guard, and you hesitate."
                         j "Liking someone means wanting the best for them, right? It means doing anything to make them happy, even if it means stepping away."
                         j "Yet here you are, putting [date_obj] through pain, stress, and countless deaths."
                         j "So let me ask you again, is this really about [date_obj]? Or is it about you?"
                         n "You feel a pang of guilt as [persistent.date_ghost]' words cut through your thoughts."
                         j "I'm not saying this to make you feel bad, [persistent.name]. I just want you to give it some thought."
                         j "If you can't see this through for the right reasons, then maybe you shouldn't see it through at all."
                         j "Otherwise you risk hurting both parties, even if it started out with good intentions."
                         j "Intentions can shift overtime. Even if they never do, good intentions can also lead to hurt occasionally."
                         j "Still, don't take this as me telling you things are pointless."
                         j "Everything can lead to hurt or harm in some way. If we should never do anything that has a chance of leading to hurt then we wouldn't be doing anything at all."
                         j "Then we would never discover the beauty that our actions can sometimes lead to. Still, it is important to be mindful."
                         j "It is a bit like driving a car. A very handy tool to get us to so many wonderful destinations."
                         j "However it's also essentially a weapon. We shouldn't not use it, but we should be thoughtful about how we use it."
                         j "So please try giving it some thought, alright [persistent.name]? In time that might come in handy..."
                         $ persistent.jamestalk_ilikeher_knowledge = True
                         
                    "I don't really care either way, [date_sub] [conj('date', 'is', 'are')] just a game character.":
                         $ justgame = True
                         j "Just as I thought, this will be pretty hard..."
                         j "This might be just a game to you but for us it's our world."
                         j "However, despite the game seemingly resetting, your actions still have consequences."
                         j "Regardless of the resets you managed to come here, to have the entire universe collapse in on itself."
                         j "Even if you start over each time, every ending you saw has happened. Every action you took has been done."
                         j "I imagine it might not always seem that way to you. Separating yourself from worlds where things go wrong doesn't make them less real than the one where things go your way."
                         j "Those abandoned worlds are still out there, [persistent.name]. I know because I watch over them, just like every other world this game contains."
                         j "This place is the weakest link to every world, a sort of dying breath of those worlds. Here it is possible for souls to linger instead of crossing over into the Void."
                         j "There is only one Void but there are many versions of this place. So the Void links every world together, since we can observe the Void we can observe them as well."
                         j "I have seen many more worlds than you have crossed."
                         j "I have seen many other crossers, I have even talked to some of them before."
                         j "I have changed some of their minds, made them see this game as more than just a game."
                         j "Even so, I also failed plenty of times. Now here we are, going through the motions once again, as I will many more."
                         j "Honestly, at some points it all seems rather pointless. You are stuck in a loop, right?"
                         j "Trying to break free, being able to move on to the next day. For me even if your loop breaks, I'm still caught in the loops of so many others."
                         j "I never get the luxury of dreaming what will happen when I get out of the loop, this place is my loop."
                         j "The only way to break my own personal loop is the Void but I'm not ready for that yet. I need to know that [persistent.date] is happy and safe."
                         if persistent.lilithAliveAndRetriedCounter >= 1:
                              j "For a brief moment I thought you felt the same way [persistent.name] but if that was truly the case, then why did you retry even after [date_sub] [conj('date', 'was', 'were')] save?"
                              $ persistent.jamestalk_justgame_knowledge = True
                              jump jamesChat_whyDidYouReturn
                         else: 
                              j "If this truly is just a game to you then you aren't as chained to it as I am."
                              j "Which means you have a better shot at breaking your loop. You can walk away from the screen."
                              j "At some point you will do so. A true end if you ask me, no? All stories truly end when the audience moves on."
                              j "In a way the story's original end is just a prelude to that."
                              j "Do not be mistaken [persistent.name], this story has quite a lot of endings but I doubt it has the one you're highly likely seeking."
                              menu:
                                   "What do you meean with stories truly ending when the audience moves on?":
                                        j "It's really simple when it comes down to it."
                                        j "Think of pretty much every story ever, wheter it's a book, a film, a game, a song or something else."
                                        j "No matter how the ending to that story is written, no matter if they live happily ever after or not, there is always the moment they stop being observed, seen, interacted with."
                                        j "It is the Universal End. That way every story ends the same, with you starting another."
                                        menu:
                                             "So does that mean that's the only ending which truly matters?":
                                                  j "However did you get to that conclusion?"
                                                  j "Does the ending to a play devalue everything that came before?"
                                                  j "No? Then why would the end after that ending make it any lesser?"
                                                  j "All things come to an end, even endings themselves, but that doesn't detract from the journey they brought us on."

                                   "What ending do you think I seek?":
                                        j "Isn't it obvious [persistent.name]? You want {b}the{/b} ending. The good ending."
                                        menu:
                                             "The ending where [date_sub] [conj('date', 'survives', 'survive')]?":
                                                  j "I see... so you still think that this is what you want?"
                                                  j "Or maybe it's what you want me to believe?"
                                                  j "I find it very hard to believe you reached me without ever stumbling upon an ending where [date_sub] [conj('date', 'lives', 'live')]."
                                                  j "The chances of that are just abysmal. However, for now all I can do is take you on your word."
                                                  j "...Can you promise me that if you find an ending where [date_sub] [conj('date', 'is', 'are')] safe, you won't come back again?"
                                                  call jamesChat_promiseToStop

                                             "What ending would that be?":
                                                  j "Isn't it clear? The typical one."
                                                  j "Where the day is saved and the two of you live happily ever after."
                                                  j "Because it isn't the ending where she merely lives you seek, is it?"
                                                  menu:
                                                       "It is.":
                                                            j "Really? So you mean to tell me you came all this way without finding any way at all to keep her safe?"
                                                            j "That sounds very unlikely... Still, right now all I can do is take your word for it."
                                                            j "Do you promise that if you do find such an ending you will stop playing the game?"
                                                            call jamesChat_promiseToStop
                                                            
                                                       "It isn't.":
                                                            j "There you go. I'm actually oddly relieved you didn't try to lie."
                                                            j "After all, the signs are all right there, aren't they? Not like I can do much about it, not yet anyway."
                                                            j "All I can say is that the ending you seek does not exist. That even if it did it wouldn't be statisfying."
                                                            j "I could try to convince you to stop playing this game, to stop searching. However I don't think that would work."
                                                            j "That is why all I'll ask is that you atleast try to treat [persistent.date] nicely."
                                                            j "[date_sub!c] [conj('date', 'deserves', 'deserve')] someone atleast somewhat kind with all [date_sub] [conj('date', 'is', 'are')] going through."
                                                            j "...Heh, is that stupid of me to ask? I guess only time will tell. For now I'll just send you back since this conversation has taken all of my energy."
                                                            jump game_start
menu jamesChat_promiseToStop:
     "I promise [persistent.date_ghost].":
          j "Thank you, [persistent.name]. Even if words are cheap, I hope you'll translate them into actions when it matters."
          j "I’ve been here long enough to know how rare that promise is. And how even rarer it is to see it kept."
          if loveher == True:
               n "[persistent.date_ghost] looks away for a moment, [ghost_pos] expression softening."
               j "All I want is for [date_obj] to be safe and happy. If you can give [date_obj] that, then maybe my time here won’t have been in vain."
               n "The atmosphere feels heavy as [persistent.date_ghost] looks back at you, [ghost_pos] eyes filled with both hope and uncertainty."
               j "Just remember, if you truly care about [date_obj], the best thing is to let [date_obj] go when the time comes."
               j "[date_sub!c] [conj('date', 'has', 'have')] been through enough, don't force [date_obj] to go through even more."
          else:
               j "Still, perhaps you are different? Maybe the key lies in your detachment to [date_obj]?"
               j "Surely it will be easier to let [date_obj] go once you feel like you reached your goal?"
               j "...If your goal truly is to keep [date_obj] safe then that's all I care about."
               j "In fact, I'll even give you a way to do just that! Next time, try to cancel your date on the phone."
               j "That should keep [date_obj] safe and make you achieve your goal, right?... I suppose only time will tell."
               return
          
     "I'll try, but I can't promise anything.":
          j "I know. I suppose for a moment I wanted to be comforted by an empty promise."
          j "Truthfully, that very promise was broken many times by others like you."
          n "[persistent.date_ghost] waves with [ghost_pos] hand towards the bubbles containing many other worlds inside, hundreds flashing for a second."
          j "In all of those worlds, that promise was made. In all of them, it was broken all the same."
          j "So whether or not you promise it, the truth is it doesn't really matter."
          j "I just hope that you are different, that you'll know when to let go."
          return

label jamesChat_whyDidYouReturn:
     menu:
          "I wanted to find an ending where we could be together and where [date_sub] would be alive.":
               if justgame == True:
                    j "...That doesn't exactly surprise me."
                    j "You take whatever you want to mold it whichever way you please."
                    j "Don't you think it's unfair to [persistent.date]? Don't you think [date_sub] [conj('date', 'has', 'have')] the right to die only once?"
                    j "I also don't like to see [date_obj] die but you are just reopening the wound repeatedly."
                    j "Can't you just break the cycle? Can't you just stop playing this game? You won't find what you're searching here."
                    j "Each retry transports you to a parallel instance of the world with the new knowledge."
                    j "However, the worlds themselves are merely copies, they tend to not vary much."
                    j "To get more variation, limitless and controlable variation even, you would need to not be bound to {b}them{/b} anymore."
                    jump jamesChat_whyDidYouReturn_toBeTogether_choices
 
               elif loveher == True:
                    j "..."
                    j "Oh [persistent.name], love is not about always being together. It's about having the person you love's best interest at heart, even if it's hard."
                  
                    $ fritfood = 0
                    $ changeableWord == "Like"
                    if persistent.ending_breakup == True:
                         $ fritfood += 1 
                         j "[changeableWord] not going on your date. That way [persistent.date] met Ron and they were happy together, even having kids together."

                         if fritfood >= 1:
                              $ changeableWord == "Or"

                    if persistent.ending_abigailDistraction == True:
                         $ fritfood += 1
                         j "[changeableWord] letting [persistent.date_sis_nickname] distract [date_obj] so [date_sub] would be safe."
                         if fritfood >= 1:
                              $ changeableWord == "Or"

                    if persistent.ending_badDate == True:
                         $ fritfood += 1
                         j "[changeableWord] when [date_sub] had a bad date with you but [date_sub] survived because you made it safe for [date_obj] to leave."
                         if fritfood >= 1:
                              $ changeableWord == "Or"

                    if persistent.times_phone_declined > 0:
                         $ fritfood += 1
                         j "[changeableWord] when you didn't pick up the phone at all, ensuring [date_pos] safety."
                         if fritfood >= 1:
                              $ changeableWord == "Or"

                    if persistent.lilithAliveAndRetriedCounter > 0:
                         j "When things were finally looking up for [date_obj], you didn't have to retry."
                         j "You didn't have to make her relive all of the pain after you were specifically told that [date_sub] [conj('date', 'was', 'were')] safe."
                         j "You see, you do not undo your actions each time you retry, each time you save [persistent.date] once more or don't."
                         j "If only it was that simple, then [date_sub] would only have died once just now."
                         j "Every time you retry you get transported to a parallel instance of this world, keeping your knowledge."
                         j "You can however only do so much in those parallel versions of the world as they are copies, they don't tend to vary much."
                         j "To get more variation, limitless and controlable variation even, you would need to not be bound to {b}them{/b} anymore."
                         jump jamesChat_whyDidYouReturn_toBeTogether_choices
   
               elif likeher == True:
                    j "I see... For who specifically would you want to reach such an ending?"
                    menu:
                         "For the both of us of course.":
                              $ persistent.polaroid_reachEndingMotive = "us"
                              
                              
                         "For myself.":
                              $ persistent.polaroid_reachEndingMotive = "me"
                              
                         "For [date_obj].":
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
                              j "...That seems to be true, you told [persistent.date_nickname] the same thing in the kokiri forest."
                         elif fritfood == 2:
                              j "Last time you said the same thing to [persistent.date_nickname], but originally you said something else, didn't you?"
                              if persistent.kokiri_reachEndingRecent != "me":
                                   n "[persistent.date_ghost] seems to notice a certain look on your face and is quick to react."
                                   j "Don't worry about that. Changing your mind is perfectly normal, if anything I'm glad that you did and seem to be sticking with your choice."
                              else:
                                   j "I wonder what made you change your mind... you were so close to understanding and then just... went the other way?"

                         elif fritfood == 3:
                              j "Are you sure? You've answered that question every possible way when [persistent.date_nickname] asked you."
                              j "Although it seems you are sticking with your last choice."
                              if persistent.kokiri_reachEndingRecent == "me":
                                   j "Although remember, it's never too late to still change your choice."
                                   j "You've done so plenty of times, so you can still go back to the better... uhm I mean previous ones."         
                    else:
                         j "Are you lying to me? That is not what you told [date_obj] the last time [date_sub] asked you, is it?"
                         if fritfood == 1:
                              j "Or did you just change your mind?"
                         else: 
                              j "Or did you change your mind again?"
                              if fritfood == 3: 
                                   j "You seem to be quite indecisive, don't you?"
                                   j "Or maybe you just wanted to see how [date_sub] would react based on your answers?"
                         if persistent.kokiri_reachEndingRecent != "me":
                              j "There's always the possibility that you're lying right now but [date_sub] can uses all the comfort [date_sub] can get. So I'll believe you, for [date_pos] sake."   
                    
                    if persistent.polaroid_reachEndingMotive == "me":
                         j "So regardless of wheter or not you like [date_obj] you still are just doing this for yourself?"
                         j "I have to say that's rather dissapointing, I was not expecting it."
                         j "However I can't blame you, I suppose even if you like [date_obj] as a character, [date_sub] still [conj('date', 'is', 'are')] just that to you [conj('date', 'is', 'are')]n't [date_sub]? A character in a game."
                         j "One you can just subject to death after death without guilt to find the perfect little ending for yourself."
                         j "I understand, but that doesn't make me any less dissapointed [persistent.name]."
                         j "I really thought you understood for a moment, understood [date_pos] life is in your hands."
                         j "I guess to you it doesn't matter much, does it? Because you can just distance yourself from the consequences of your actions and act as if none of it happened."
                         j "You can just pretend what you want will be worth all the suffering it brings to a character you specifically said you liked."
                         j "I wonder, would you do the same thing in the real world if you thought there were no consequences for you actions?"
                         j "If you could distance yourself far enough from those consequences atleast? Would you also hurt the people you like in that case?"
                         j "Is all that holds you back the distinction of what is real and what isn't? The idea that the consequences can't reach you?"
                         j "This is real to us [persistent.name], isnt that enough for you?"
                         j "I'm begging you, if you even remotely like [date_obj], please stop hurting [date_obj]."
                         j "It's not worth it, what you are looking for is unattainable here."
                         j "Can't you see? You've gone through all of this and the game still hasn't given you what you want. That's because it can't."

                    elif persistent.polaroid_reachEndingMotive == "us":
                         j "I see. Are you sure about that?"
                         j "Do you think you are doing this as much for [date_obj] as for yourself?"
                         if persistent.lilithAliveAndRetriedCounter > 0:
                              j "You've already kept [date_obj] safe, didn't you? Even then, you still came back."
                              j "Isn't [date_pos] safety what's in [date_pos] best interest?"
                              j "Isn't [date_pos] safety what's in your best interest?"
                              label jamesTalk_motiveForUs_choices:
                                   j "Or do you think this cycle of death is worth it to [date_obj] if [date_sub] somehow [conj('date', 'ends', 'end')] up with you by the end of it?"
                                   menu:
                                        "Maybe [date_sub] [conj('date', 'feels', 'feel')] that way, who are you to decide it isn't worth it?":
                                             j "You're very right [persistent.name]. I can't just speak for [date_obj]."
                                             j "Neither can you, right? Have you ever asked [date_obj] how [date_sub] felt about all of this?"
                                             j "Have you had a genuine conversation about it with [date_obj]?"
                                             j "Because if you are truly doing this for the both of you then [date_sub] [conj('date', 'is', 'are')] a major part of that sum, [conj('date', 'is', 'are')] [date_sub]?"
                                             j "Isn't it pretty important to know how [date_sub] [conj('date', 'feels', 'feel')] about the important things?"

                                        "[date_sub!c] seemed to be okay with it so far, [date_sub] [conj('date', 'has', 'have')]n't asked me to stop.":
                                             j "...Does [date_sub] know just how many times you've gone through the same song and dance only for [date_obj] to die?"
                                             if persistent.lilithAliveAndRetriedCounter == 0:
                                                  j "So far you haven't had any results. You're just throwing more and more of [date_pos] deaths at the problem in the hopes of finding a solution."
                                             else:
                                                  j "Even though you already found a way to save [date_obj] you just can't let [date_obj] go yet, can you?"
                                             j "I wonder how [date_sub] would react to that. [conj('date', 'Is', 'Are')] [date_sub] fully aware of the exact situation the two of you are in?"
                                             j "Otherwise can you blame [date_obj] for not asking [date_obj] to stop if [date_sub] [conj('date', 'does', 'do')]n't have a full grasp on the situation?"
                                             j "Even if [date_sub] did, each time [date_sub] [conj('date', 'has', 'have')] to relearn it all over again, never really getting enough time to process it at [date_pos] own pace."
                                             j "Still, even if [date_sub] [conj('date', 'has', 'have')] then it's generally a good idea to tell [date_obj], since the two of you are supposed to be a team, aren't you?"
                         else:               
                              j "After all, have you never considered cancelling your date or just not answering the call?"
                              j "Do you expect me to believe you have jumped through all these hoops to keep [date_obj] safe while you never considered that?"
                              jump jamesTalk_motiveForUs_choices

                    elif persistent.polaroid_reachEndingMotive == "her":
                         j "Do you really believe that [persistent.name]?"
                         j "[date_sub!c] was fine without you, [conj('date', 'was', 'were')]n't [date_sub]?"
                         j "Don't get me wrong [persistent.name], [date_sub] [conj('date', 'seems', 'seem')] to like you. Still, [date_sub] [conj('date', 'does', 'do')]n't need to end up with you to be happy."
                         if persistent.ending_breakup == True:
                              j "You have seen that yourself, haven't you?"
                         j "My fear is that you might need [date_obj] to be happy."
                         j "Is that why you're searching an ending where the both of you end up with eachother?"
                         j "I understand that it can be very hard to let go, precisely because I'm in, the same boat."
                         j "That's precisely why it is important to truly think this through, before everything capsizes."
                         j "Do you think subjecting [date_obj] to death after death will be worth it in the end?"
                         j "There are better ways to achieve your goal. I sadly can't just tell you, since that isn't allowed by Him."
                         j "Please trust me however, you won't find the ending you seek by just going through every path in this game."
                         j "Every road you walk with [date_obj] just leads to death."
                         
          "I wanted to see the other endings.":
               j "I see... I'll spare your time then, there are no endings here that I am aware of."
               j "In all this time I've spent here I've never seen one."
               menu:
                    "I don't believe you.":
                         if justgame == True:
                              j "... Do you think I'm defending [persistent.date] by lying to you??"
                              j "{swap=Maybe I am.@Maybe I am not.@1 @1}Maybe I am.{/swap}" #SWAP text effect example
                              j "In the first case I am desperate enough to lie to your face and in the other there truly isn't another ending here."
                              j "In both options it'd be wiser to reconsider before you walk a path you'd regret, right?"
                              j "You might not have felt many consequences for your actions yet, but let me assure you. There is no such thing as no consequences..."
                              if (persistent.major_love_offence_counter + persistent.minor_love_offence_counter) > (5 + persistent.major_love_comfort_counter + persistent.minor_love_comfort_counter):    
                                   j "If you keep treating [persistent.date_nickname] badly I might need to teach you that lesson."
                                   n "[persistent.date_ghost] gives you a bonechilling look that makes you think you wouldn't like being educated by [ghost_obj]. At all."
                              else:
                                   j "Let's hope for the both of us that you consider your actions well enough to experience the fewest possible consequences."
                                   j "After all, ignorance is bliss isn't it [persistent.name]?"
                                   n "[ghost_sub!c] spoke those last words with some noticeable disdain. You are not entirely sure why."
                              j "My energy is running low from this talk, so I'll have to take some rest. In the meantime I'll send you back."
                              j "Goodbye [persistent.name]. Do not come back here."
                              jump Game_start2
    
                         else:
                              j "Oh [persistent.name], why don't you trust me? We both care for [persistent.date] right? So rest assured I only want the best for [date_obj]."
                              menu:
                                   "How do you know what is the best for [date_obj]?":
                                        j "Look, can we not do this? You have seen endings where [date_sub] lived, and yet you came back."
                                        j "Maybe I don't have the right to decide what's best for [date_obj], but what gives you the right to?"
                                        if (persistent.major_love_offence_counter + persistent.minor_love_offence_counter) > (5 + persistent.major_love_comfort_counter + persistent.minor_love_comfort_counter):    
                                             j "Especially if you treat [date_obj] badly when on your date with [date_obj], what is the point of that?"
                                             j "Did you retry after [date_obj] good endings just so you could torment [date_obj] more?"
                                             j "Are you just saying you are looking for other endings as an excuse? Do you even truly want this to end?"
                                             j "Or are you always going to be searching for one more ending, no matter what you find?"
                                             j "Well [persistent.name], let these be my last words for now, your search will be unfulfilling and meaningless, no matter what you find."
                                             j "Because it will never be enough for you."
                                             j "I guess that's a fitting curse though, so I'll let you go on your merry way back."
                                             jump Game_start2
                                             
                                        else:
                                             j "Your intentions seem pure though, albeit quite naive."
                                             j "At the very least I guess it could have been worse. [date_sub!c] can die with someone [date_sub] [conj('date', 'trusts', 'trust')] now."
                                             j "Although I would prefer if you didn't have to keep looping. You are playing a game with rules you can't win."
                                             j "Attempting to over and over again is only going to create more death, to slowly hollow out any reason you had for trying again in the first place."
                                             j "I like you well enough, so I'll tell you a secret I picked up from watching over all these different worlds."
                                             j "{i}What do you do when you don't like the way a story goes?{/i}"
                                             j "That's the most I can say I'm afraid, I'm not really allowed to spell it out too much."
                                             j "Now I'm going to have to send you back, just talking to you like this costs me a lot of energy."
                                             j "Goodbye [persistent.name], I hope my tip will help you out."
                                             jump Game_start2


                                   "I guess we're indeed on the same page. I'll take your word on there being no other endings here.":
                                        j "Thank you [persistent.name], that means a lot to me."
                                        j "Besides, I think you have already found the best endings you possibly could find, even if you may not know it yet."
                                       
                                        $ persistent.ringRiddle_knowledge = True
                                        j "{i}After all, how many ends does a ring have?{/i}"
                                        menu:
                                             "None, there is no begining and there is no end.":
                                                  jump jamesChat_whyDidYouReturn_ringResponse

                                             "One, right where it loops back to the begining.":
                                                  jump jamesChat_whyDidYouReturn_ringResponse

                                             "An infinite amount of them. It just depends how you look at the ring.":
                                                  jump jamesChat_whyDidYouReturn_ringResponse

                                        #Write some more text here.

                    
                    "Thank you for telling me. I just had to be sure, this seems like the perfect place to hide things.":
                         j "I can see why you would think that [persistent.name], afterall this is a sort of stowaway for wayward souls but here we all absolutely fear endings."
                         j "Although I suppose that it depends on what you see as endings."
                         j "The thing about a loop is that we can sometimes be tricked into thinking there are no endings, because it never ends."
                         j "Yet in a way you encountered many endings you wouldn't necesarilly consider endings, didn't you?"
                         j "Because I like you I'll clue you into something, {i}those endings I'm talking about you won't be able to find here.{/i}"
                         j "Best of luck [persistent.name]."

          "You can't just bombard me with so much info and then just move on like I should understand, can you please atleast explain something clearly?" if not persistent.jamesUnclearAnswered:
               j "I see... I suppose that's indeed a bit too much info for you to handle."
               j "I'll let you ask me one question if you answer mine afterwards."
               menu:
                    "How do my actions have consequences?":
                         j "It really is a matter of multiple layers."
                         j "Firstly, the worlds you abandon to try again in another keep going."
                         j "The loss, the destruction. All of that doesn't just cease the moment you turn your back to it."
                         j "If it did, I wouldn't remember them, would I... However, that might not matter to you."
                         j "Maybe something more personal? Imagine for a second the world would truly reset. You don't exist in that world, do you?"
                         j "You turn back the clock but you can't do the same to yourself."
                         j "You can say it doesn't matter. Maybe it really doesn't, but your memories are still proof of your actions."
                         if persistent.nightmareCounter > 0:
                              j "Surely you've felt those memories seep back into the game, haven't you?"
                              j "The one you wield as a vessel is haunted by them..."
                              j "For them this is their world afterall. The two blend so well together yet differ so much in that regard."
                         else:
                              j "From what I have seen in the other worlds, it's only a matter of time before those memories will seep back into the game."
                              j "I wonder if then you'll still be able to act as if nothing is wrong?"

                    "I don't understand your explanation about the Void.":
                         j "Picture the world you interact with as a play."
                         j "You are an audience member, perhaps even a participating one."
                         j "This place is what lies behind the curtain of that performance."
                         j "It is what remains after it all ended and the lights have gone out."
                         j "The characters enter the dark, ready to be shedded by their actors and to move on to new forms, new plays."
                         j "Yet sometimes, some characters or ideas linger in the dark. Not ready to move on."
                         j "They peer into the Void and as they do so they grow aware of others peering in aswell, from their own stage. Yet there is only one Void, only one End. No matter how many different endings exist, it all truly ends by becoming nothing."
                         j "It is through glimpsing the ghosts glimpsing us that we can peak behind the curtains, to watch other plays being held without us."

                    "What other crossers did you meet?":
                         j "More like you. Others playing this game."
                         j "Some in the same circumstances. Some came here to see the next piece of content. Others to converse with me after other crossers told them about me."
                         j "They keep flocking to worlds with [date_obj] in it like moths to a flame, like a corpse-fly. Retry after retry after retry."
                         j "The death and destruction it brings not just limited to one crosser like you, but many, many more."
                         j "Although sometimes I wonder if it's the death and destruction that brings you in instead."
                         j "I have steered some off that path, yet I failed with many others."
                         j "I even met some of the pillars of this world. Ones threading the many paths woven by the Creator as a test set out by him."
                         j "The Creator Himself has also shared a few words with me as he gave me mine."


                    "Why do you feel like you are also stuck in a loop?":
                         j "Here I am linked to every other version of me in their own version of this place."
                         j "I see what they see. Together we watch over our family in every world."
                         j "Lately more and more of those worlds have been birthed to house the likes of you."
                         j "Which means more and more versions of me who all have to watch our sister suffer death after death."
                         j "We could try to talk you out of it, in fact we sometimes manage to do so."
                         j "But many other crossers don't even reach us, so we can never convince them. Others don't agree even if they meet us."
                         j "Besides, even then many new, separate crossers pop up all of the time."
                         j "Alongside them many more of me and new worlds of suffering and pain to watch over."
                         j "It never stops. It seemingly never will."

               j "So, I have answered your question, now it is time you answer mine."
               $ persistent.jamesUnclearAnswered = True
               j "Why did you come back even after [persistent.date] [conj('date', 'was', 'were')] safe and happy?"
               jump jamesChat_whyDidYouReturn
                   
label jamesChat_whyDidYouReturn_ringResponse:
     j "I'm afraid I can't give you the answer [persistent.name], He doesn't like that."
     j "But I did give you the question, perhaps a topic to talk about to [persistent.date] if you would like to discuss it more?"
     n "[ghost_sub!c] [conj('ghost', 'gives', 'give')] you a slight wink."
     j "I hope that helps, in any case, I'm going to have to send you back now. I don't have enough energy to keep up this conversation."
     jump Game_start2
                                             
label jamesChat_whyDidYouReturn_toBeTogether_choices:
     menu:
          "Who are {i}they{/i}?":
               j "I doubt you have met the first one, not for long anyway. He is the one that created this world, gave you access to it and made the second one."
               j "That one you might know actually, the jester that controls the flow and direction of our story."
               j "He even controls the deaths [persistent.date] suffered. Even still you rely on him to fight him, that might be his biggest joke yet."
               menu:
                    "Alright mister purple prose. So the \"{i}they{/i}\" you were talking about are the game developer and the narrator?":
                         j "Purple prose? I'll try to keep it a bit more straightforward."
                         j "Yes, they are them. They made you search for an ending that doesn't exist."
                         j "If you want to find it you'll have to find it in yourself."
                         j "{i}The only way to win against the house is to become the house.{/i}"
                         menu:
                              "... what? That is not more straightforward at all.":
                                   j "It's no use... If those words come from me they won't impact you that much."
                                   j "Why don't you ask [persistent.date] to explain them where {i}three{/i} become {i}one{/i}?"
                                   $ persistent.jamesconversation_becomethegame_knowledge = True 

                              "You mean by telling the story myself instead of relying on the game for it, right?" if persistent.kokiri_makeYourOwnStory_knowledge:
                                   j "Ah, so you already talked about it with [date_obj]?"
                                   j "Very good. Yes, that is indeed one way to find something unfindable."
                                   j "Although I wonder, if you did talk to [date_obj] about this, then why are you back here?"
                                   j "Why are you still stuck in the grip of this game?"
                                   menu:
                                        "I want to keep exploring a little longer, there's still many things I haven't seen yet.":
                                             if persistent.lilithAliveAndRetriedCounter == 0:
                                                  $ changeableWord = "death"
                                             else:
                                                  $ changeableWord = "death and seperation"
                                             j "Interesting, even if it all leads to more [changeableWord]?"
                                             if persistent.lilithAliveAndRetriedCounter == 0:
                                                  j "Wasn't your goal to keep [date_obj] safe? If that is unattainable here then shouldn't you create a story where it isn't?"
                                             else:
                                                  j "After you continued even when [date_sub] [conj('date', 'was', 'were')] safe I thought you wanted to end up with [date_obj] and have [date_obj] live"
                                                  j "Now you know that you can't do that here, shouldn't you try to create your own story where you can?"
                                             j "It's funny isn't it? Even things that are less than ideal or even painful can be hard to let go of."
                                             j "I wonder why sometimes, do we just get so used to the pain and inconvenience we end up in fear of losing it?"
                                             j "Or are we scared that if we let go the next thing might only be worse?"
                                             j "Either way, don't hold onto this game for too long, alright? It might make it even harder to move on."

                         j "This talk of ours cost me most of my energy so I'll send you back now. Goodbye [persistent.name]."
                         jump Game_start2

label LilithOrJames:
     #TODO: Add the descriptions of james and lilith to the dialogue.
     # Normalize so left is always Lilith (date) and right is always James (date_ghost).
     # If jamesMode is True the names are currently swapped, so un-swap them first.
     if persistent.jamesMode:
          python:
               persistent.date, persistent.date_ghost = persistent.date_ghost, persistent.date
               persistent.date_nickname, persistent.date_ghost_nickname = persistent.date_ghost_nickname, persistent.date_nickname
               _pd = _get_pronoun_dict("date")
               _pgd = _get_pronoun_dict("date_ghost")
               persistent.date_pronouns = _pd
               persistent.date_ghost_pronouns = _pgd
               store.date_sub = persistent.date_pronouns["sub"]
               store.date_obj = persistent.date_pronouns["obj"]
               store.date_pos = persistent.date_pronouns["pos"]
               store.ghost_sub = persistent.date_ghost_pronouns["sub"]
               store.ghost_obj = persistent.date_ghost_pronouns["obj"]
               store.ghost_pos = persistent.date_ghost_pronouns["pos"]
               persistent.jamesMode = False
          $ updatePronouns()
     # State is now always: date=Lilith, date_ghost=James, jamesMode=False
     n "You float in a seemingly endless tunnel of darkness."
     n "After what feels like hours the tunnel seperates into two smaller ones. The end of each shows a scene similar in so many ways yet also slightly different."
     n "The left tunnel, a vision of you sitting together in some sort of restaurant with a (description of [persistent.date]), you get the strange feeling you know [date_pos] name, it's [persistent.date]."
     n "The right tunnel, one of you sitting together in some sort of restaurant with a (description of [persistent.date_ghost]), you get the strange feeling you know [ghost_pos] name, it's [persistent.date_ghost]."
     n "Choose which way you will walk player, left or right? [persistent.date] or [persistent.date_ghost]?"
     menu:
          "Walk left. ([persistent.date])":
               # Already normalized: date=Lilith, jamesMode=False — nothing to do.
               $ persistent.datedLilith = True
               jump game_start
          "Walk right. ([persistent.date_ghost])":
               # Swap so James becomes the active date.
               python:
                    persistent.date, persistent.date_ghost = persistent.date_ghost, persistent.date
                    persistent.date_nickname, persistent.date_ghost_nickname = persistent.date_ghost_nickname, persistent.date_nickname
                    _pd = _get_pronoun_dict("date")
                    _pgd = _get_pronoun_dict("date_ghost")
                    persistent.date_pronouns, persistent.date_ghost_pronouns = _pgd, _pd
                    persistent.jamesMode = True
                    persistent.datedJames = True
               $ updatePronouns()
               jump game_start

label ufoVisitAlone:
     $ persistent.anomaly_knowledge = True # previously called "Readshiplog")
     menu:
          "Computer, tell me about the temporal anomaly.":
               ship "A temporal anomaly has been picked up accidentally by our quantum computers when we connected all our Neya-infused computers in identical parallel universes in an effort to create even more advanced computers."
               ship "The universes we are connected with are exactly the same as this one except for one thing, the anomaly."
               ship "It manifests itself on a specific day in each and every universe, always on the same doomed day."
               ship "Around the anomaly a lot more accidents tend to happen, more than explainable by our curent science, our curent hypothesis is that the universes the anomaly resides in want to purge themselves of It."
               ship "Unfortunatly the universes measures are quite... drastic and put all our lives in danger aswell."
               ship "We tried giving them a hand by killing the anomaly however, this wielded an even faster and further spread to other universes."
               ship "At a certain point it grew so rapidly we couldn't control it, connection was broken with a billion of paralel versions of this ship that time, probably lost in the crossfire."
               ship "That's when it happened, a terified version of us accidentaly misfired and shot [date_pos] instead of the anomaly."
               ship "At that moment the anomaly stopped in that universe. We found this peculiar so we looked more into it."
               ship "It also took the anomaly longer to wreak havoc upon other universes."
               ship "We were unsure about the relation between [date_pos] and the anomaly but after a few extra tests we noticed a clear corelation between [date_pos!c] dying and the delay, even dissapearance of some of the anomalies."
               ship "[date_sub!c] must be the key to stop the anomaly from crossing over, [date_sub] must be, or all hope is lost..."
               ship "We would tell you where you would find both of them but due to how the anomaly works it isn't always set to be in the same place, rather a few possible places."
               ship "If they go to any of the three restaurants stored on our computer you do not need to intervene, the universe will take care of it in a acceptable way with a small amount of death."
               ship "However, if they go to either the forest or the beach you need to keep a close eye on them, if [date_sub] [conj('date', 'has', 'have')] been killed by the either the falling star or car we have to come into the picture, otherwise our fates will look quite gruesome, let me asure you."
                     
label reunionEnding:
     n "Heading towards the Chinese restaurant you pass by the market square."
     n "The same place you set up for [persistent.date_mom] and [persistent.date_dad] to meet. Right on cue you see [persistent.date_mom] and [persistent.date_sis] walking past."
     n "Something inside you can't help but watch the scene, you hide behind a car to keep an eye on things."
     li "This seems like a weird place for your teacher to meet us [persistent.date_sis]."
     a "I agree, this doesn't seem like them... This will be so funny!"
     n "[persistent.Date_mom] lets out a big sigh."
     li "...Let's atleast wait about an hour just to be sure okay? After that we can leave."
     li "You know what? Let's go fetch some hotdogs first, I'm sure we can be back before they-"
     l "[mom_parShort!c]? [persistent.date_sis_nickname]? What are you two doing here?"
     n "It seems [persistent.date] also passed by, just as planned."
     a "[mom_parShort!c] totaly let a random prank caller convince [mom_obj] they were Sam Roberts wanting to meet us here. I doubt the prankster will even show up."
     l "Is that true [mom_parShort]?"
     li "Uhm... it might be? It could still be them?"
     n "[persistent.date] burst out into laughter."
     l "[mom_parShort!c], you're so gullible."
     n "[persistent.date_mom] sighs deeply."
     li "Maybe I really am..., what are you doing here anyway sweetie?"
     l "Oh, I'm just meeting up with [persistent.name] for our date, I parked the car a block from here. And-"
     n "A man walks up to them timidly, almost tentative. Thinking through whether to turn back around or not. [dad_sub!c] [conj('dad', 'takes', 'take')] a deep breath in, almost as if to gather the courage in the air."
     d "Uhm, hello [persistent.date]... I hope you are doing well. And wow [persistent.date_sis], you've gotten so much taller, you might even outgrow your old man soon."
     a "Dad? "
     n "The man chuckles nervously."
     li "Hello [persistent.date_mom], still as beautiful as ever."
     li "Oh absolutely not fathe- [persistent.date_dad]! Do you think you can just march back into our lives? Do you think anything will ever give you that right?"
     li "[persistent.date], please-"
     l "No [mom_parShort], I'm not letting you finish whatever that sentence was, probably something about giving [dad_obj] another chance but I love [persistent.date_sis_nickname] and you too much for that."
     l "I still love [persistent.date_ghost] too much for that."
     n "It's subtle, but you think you can see [persistent.date_dad] almost flinching upon hearing that name."
     li "[persistent.date]! Your [dad_par]-"
     d "It's alright [persistent.date_mom], I understand why [date_sub] [conj('date', 'is', 'are')] angry with me."
     d "To be honest with you, I have heard those words before. In my mind, pretty much every day."
     d "How I killed [persistent.date_ghost] and ran away like a coward-"
     l "What are you saying [persistent.date_dad]? You were a coward but you didn't kill [ghost_obj], it was an accident."
     n "[persistent.date_dad] begins to sob audibly."
     d "Even if it was an accident, I gave [ghost_obj] that stupid camera! If it wasn't for me [ghost_sub] would still be alive, that makes me a killer."
     l "Oh please [dad_parShort], the only thing you killed was our family life, it was already shaken by [persistent.date_ghost]'s death but then it broke fully when you left."
     d "I... I... I had no idea that I made it worse by leaving, I thought I was helping you by not having to see me anymore."
     l "Then why are you here?"
     d "Because it was so hard to do, I wanted to go back every single day. I had to fight myself not to."
     d "All I needed as a last straw to break and to come back was a little push and recently I got that push by a mysterious stranger."
     d "But that's not important, you are right, I killed our family instead of [persistent.date_ghost]."
     d "We can't bring [ghost_obj] back but I'd like to try to bring our family back. If all three of you would have me that is."
     a "Of course [dad_parShort], you will always be family! Welcome back."
     n "[persistent.date_sis] runs up to [sis_pos] [dad_parShort] and wraps [sis_pos] hands around [dad_obj] in a warm embrace."
     n "A smile appears on the face of [persistent.date_dad], [dad_sub] [conj('dad', 'is', 'are')] still crying, now a mixture of both happy and sad tears."
     li "You took your time [persistent.date_dad_nickname] but I never stopped loving you, welcome back."
     n "She walks up to [dad_obj] and gives [dad_obj] a little peck on the cheek."
     l "You know what? Fine, I'm giving you a chance for them, for [persistent.date_ghost]. But I'd rather not have to call you [dad_parShort] yet, I'll stick with [persistent.date_dad] for now."
     d "So you're saying there is a change you might call me [dad_parShort] again?"
     n "[persistent.date] blushes beetred."
     d "I completely understand, I'm thankful for you even giving me a chance and I'll try my best to earn the title once more."
     d "However, if you never feel comfortable calling me that again then that's completely fine."
     li "Oh [persistent.date], your date with [persistent.name]. They should be there already, you'd better go to them!"
     l "I'd like to but right now there are more pressing matters at hand, I can't let all of you go right now."
     menu:
          "*Go up to the reunited family.*":
               jump reunion_showUp
          "*Leave them alone.*":
               jump reunion_noShowUp
          "*Use the connection you built with [persistent.date_ghost] to pull [ghost_obj] into this reality.*" if persistent.datedJames and persistent.datedLilith:
               jump badReunionTransferUniverse
    
label reunion_showUp:
     l "Hang on, speaking about the devil... is that [persistent.name]?"
     l "Hey [persistent.name], what are you doing here?"
     menu:
          "*Tell the entire story*.":
               jump reunion_showUp_iReunitedYou
          "Oh, hey [persistent.date], I was just passing by to go to the restaurant.":
               jump reunion_JustPassingBy

label reunion_showUp_iReunitedYou:
     l "So you have been reliving this same day constantly?"
     l "And you've been using the info you gathered to keep me safe?"
     l "To do all of this? I don't know how I feel about this..."
     l "You've involved my entire family to reach this point?"
     l "Ofcourse I'm thankful, but you have to admit this whole thing is rather weird."
     l "Because I'm fairly certain I'd never ask you to do this."
     li "Honey..., I'm sure [persistent.date] meant well."
     l "That's not the point [mom_parShort]! Wheter [persistent.date] meant well or not I didn't ask for this."
     if persistent.restrainingorderfamily_knowledge:
          n "In fact [date_sub] specifically asked you not to do this, didn't [date_sub]?"
     l "I may not remember each loop, but does that automatically remove my right to make decisions?"
     jump reunion_death
                   
label reunion_JustPassingBy:
     l "Oh right, I almost forgot all about that for a second!"
     l "I'm really sorry [persistent.name], it's just that right now something else is going on."
     l "Would you mind if we rescheduled our date?"
     menu:
          "Don't worry [persistent.date], that's fine with me!":
               l "Thanks a lot and once again I'm very sorry about having to delay it."
               l "I'm looking forward to it very much, I'll see you later."
               menu:
                    "See you later [persistent.date], take care.":
                         li "{size=*0.5}Hang on, that voice...{/size}"
                         n "The words are said pretty quietly, only [persistent.date_dad], who is standing next to [persistent.date_mom] managed to pick them up."
                         d "{size=*0.5}Now that you mention it...{/size}"
                         n "It's quiet for a moment as you start to wander back to your home. [persistent.date_dad] and [persistent.date_mom] share a knowing look with eachother."
                         li "[persistent.name]?"
                         n "You turn around to face [persistent.date_mom]."
                         li "You seem like a nice person, please go on another date with [persistent.date_nickname] soon. Or I guess I actually mean another first date, since we threw a spanner in the works."
                         n "You nod."
                         l "{size=*0.5}[mom_parShort!c], you're embarassing me...{/size}"
                         n "It would be impossible to tell in the dark, but having looped enough times you are certain that [date_sub] [conj('date', 'has', 'have')] just turned even more red than a tomato."
                         li "Oh my, am I? I'm sorry sweetie. I just really think you and your date would have a nice time together."
                         n "Soon [date_sub]'ll be so red it's not even describable at this point."
                         n "Deciding to spare [date_obj] you say your goodbyes once again, this time for real, half surpressing a little chuckle."
                         n "Coming home you're pretty satisfied. Yes, you did a lot of questionable things, but to see the end result makes it all worth it, doesn't it?"
                         n "You reunited [persistent.date] and [date_pos] family, [date_sub] [conj('date', 'is', 'are')] still alive and soon the two of you will have a date in different circumstances."
                         n "Who knows what will happen? For the first time in a while things feel like they are completely new. Life once again is the tabula rasa it was meant to be. Things can go in all kinds of new directions now."
                         n "Sadly, the direction things went is a familiar one to you."
                         n "Things didn't go as planned."
                         n "For whatever reason after a week [persistent.date] has not yet sent you anything to schedule a new date."
                         n "You decided to give [date_obj] some time, after all [date_sub] probably still [conj('date', 'is', 'are')] adjusting to everything that happened not so long ago."
                         n "You wait another week, still nothing."
                         n "Concerned you decide to check up on [date_obj] and give [date_obj] a call."
                         l "Oh, hey [persistent.name]!"
                         n "So [date_sub] still [conj('date', 'is', 'are')] alive, that's good. With this game you never know."
                         menu:
                              "Hey [persistent.date], I was just wondering if you had thought about another time for us to go on that date we had planned?":
                                   l "Right..."
                                   l "I'm really sorry [persistent.name], but I think I just wasn't really ready to go on a date again."
                                   l "I really wanted to give it a shot, but with things changing here recently I came to a realisation."
                                   l "I think it's best if I still wait a little longer, I'm just not sure how long exactly."
                                   menu:
                                        "That's alright, I can wait.":
                                             l "...I know you can [persistent.name], but that doesn't feel right to me."
                                             l "You don't deserve to spend all eternity waiting just for another first date."
                                             l "Maybe by the time I'm ready we both will be fundamentally different people."
                                             l "No matter how hard it might be right now, I think it's better for you to move on eventually."
                                             l "Trust me, it's hard for me too. I never would have called this date off a month ago, but I came to the realisation that not doing so would be selfish."
                                             l "Even then, I'm still not good at it. That's probably while I waited all this while for you to call me instead of calling you."
                                             l "I'm sorry for that by the way, you didn't deserve that at all."
                                             l "Now, I'm going to try to make this easier for the both of us by hanging up in the next 30 seconds."
                                             l "Goodbye [persistent.name], I hope you'll be happy wherever you are going."
                                             menu:
                                                  "Goodbye [persistent.date], I wish you nothing but the best.":
                                                       n "For a moment you could swear you hear some slight sobbing on the other end of the line."
                                                       n "But before you can try to listen closer [persistent.date] hung up true to [date_pos] word."
                                                       n "That was the last thing you ever heard of [date_obj]."
                                                       jump reunion_ending_goodChoices

label reunion_ending_aftermath:
     n "You tried to move on with your life. Things went pretty well all things considered. You had many other first dates, different ones. You even had a few second ones. There was even a third one that blossomed into many more."
     n "But this isn't about that story, so I'll keep it brief."
     n "You tried to live each day like it is your first and last with your partner. There were bad moments and good ones, but each moment was beautiful in that it never lasted. That it always could be built upon."
     n "Then after many many years, during your last breath on your deathbed you get offered a familiar choice."
     $ lilithAliveEnding = True
     $ persistent.ending_reunionGoodEnding = True
     $ ending_check = "reunitedGood"
     $ persistent.gallery_unlocked = True
     menu:
          "Retry?":
               if persistent.ending_reunionGoodEnding == False:
                    n "So you really are retrying?"
                    n "Even after leading to an ending as good as this one?"
                    n "Even after everything you did to get here?"
                    n "After invading [date_pos] privacy."
                    if persistent.restrainingorderfamily_knowledge == True:
                         n "After contacting [date_pos] family even though [date_sub] specifically asked you not to."
                    n "Before you could argue that it lead to this. But now you continue once more."
                    n "That doesn't take away you did those things."
                    n "What for are you even retrying?"
                    n "For more death? For more suffering?"
                    n "Or was it for more [date_obj]? Weren't you able to let [date_obj] go just yet?" 
                    n "That is a hard thing to do, but ask yourself this, when will you be able to truly let [date_obj] go?"
                    n "You can't keep this up forever, can you?"   
               else:
                    n"...Again?"
                    n "I really hoped this time you wouldn't do that."
                    n "Why do you keep going through this ending if you keep resetting it?..." 
                    n "Don't bother answering that, I do not want to hear it anyway." 
               jump game_start

label reunion_noShowUp:
     l "Besides, we do not need them, we already have one person extra joining us, can't all of you feel it?"
     d "Now that you mention it, it's-"
     li "It's [persistent.date_ghost]."
     a "Hello [ghost_sib], welcome back."
     l "We've missed you."
     #Cue some music here once you have a track for this.
     n "With a smile on your face you walk back to your car, trying to go unnoticed."
     n "You have decided it's best to not risk getting mixed up in [persistent.date]'s life again."
     n "From [date_pos] perspective you'll be seen as the person who ghosted [date_obj] but you deep down hope that this and the other bad things you have done will be forgiven."
     jump reunion_ending_goodChoices

     label reunion_ending_goodChoices:
          n "You did try to give [date_obj] the best chance [date_sub] had with [date_pos] family."
          if persistent.ending_breakup:
               n "You do know that one day [date_sub] will meet Ron and start a family of [date_pos] own."
          n "You remind yourself [date_sub] will be fine. Happy."
          n "Although you did go against [date_pos] wishes multiple times to get to that point. Did you do so for the \"Greater good\"?"
          n "Or are you just lucky ignoring [date_pos] autonomy had some positive outcomes in the end?"
          n "Are you justifying your own choices?"
          n "..."
          n "I'd like you to think about that for a second."
          n "Were the choices you made worth this moment?"
          n "Well, what do you think player?"
          menu:
               "Yes.":
                    n "Interesting. I do wonder at what point you decided that."
                    n "When did protecting [date_obj] shift into this?"
                    n "It's still a noble goal, but the means to get there are far from it."
                    if persistent.lilithAliveAndRetriedCounter > 0:
                         n "Wasn't it sufficient enough for [date_obj] to be alive?"
                         n "At what point did you decide you needed to do more?"
                    n "Is this still about [date_obj]? Or is this about you?"
                    n "If so, what are you getting out of this?"
                    n "Was this truly about reuniting [date_obj] family?"
                    n "Maybe this was a means to delay the inevitable? To delay letting [date_obj] go?"
                    n "Or a means to feed your curiosity? To see what would happen if you chose this path?"
                    n "Or maybe something entirely else I'm just not seeing?"
                    n "..."
               "No.":
                    n "Interesting. I do wonder what runs through your mind in that case."
                    n "Do you regret what you did? Would you want to make it undone?"
                    n "Or would that also undo this moment?"
                    n "You have caused harm yes, but would you undo the happiness you have performed those steps for?"
                    n "A true \"undo\" doesn't exist, but would you paint over it?"
                    n "Is it better to try to undo your mistakes or to learn from them?"
                    n "..."

          n "Whatever you answered, let us continue. Because if the ending doesn't end, is it truly one?"
          jump reunion_ending_aftermath
     
label ghostReunion_transferUniverse:
     n "You focus all your willpower trying to draw [persistent.date]'s ghost from a different reality into this one."
     n "[date_pos!c] voice begins to emanate softly in the white endless void."
     l "{size=*0.5} [persistent.name]...[persistent.name]...[persistent.name]{/size}"
     l "[persistent.name], where are we?"
     l "I mean, this feels like my makeshift home but it's not entirely the same."
     l "I seem to notice a strangely familiar energy signature."
     j "[persistent.name], is that you? Who is that with you? Hang on, [persistent.date_nickname]?"
     l "[persistent.date_ghost_nickname]? What are you doing here?"
     j "This is my makeshift home I created after I well... died. "
     l "But that's impossible, you look way too young, I've watched over all [persistent.date_ghost]' in my reality and none of them died this young."
     j "...So my supicions were correct, you are not from this reality."
     l "Are there different realities?"
     j "Yes, sort of anyway. The realities are were things go differently than they go in other realities even without outside interference."
     j "However, that's not important. Due to your age I have to ask, if you don't mind to answer me that is, how did you die?"
     l "Oh, [dad_parShort] gave me [dad_pos] old polaroid camera to take pictures with. I loved it but one day I was taking pictures on an abandoned road that was apparently not so abadoned as a red Sedan hit me and fled the scene. I died after lying there for what felt like eternity."
     j "I see, so you went through the same thing as me. I think our realities might have started to branch from the point [dad_parShort] decide who [dad_sub] would give the camera."
     l "So does that mean that you died on the same day as I did?"
     j "It would seem that way, so our age is the same as on the day it happened."
     l "In a way, this seems like it might be our second chance, we're finally reunited."
     n "[persistent.date] gives [persistent.date_ghost] a big hug."
     j "I missed this [persistent.date_nickname]."
     l "So did I [persistent.date_ghost_nickname], so did I. We could be so happy living here together, but I need to be sure my reality's family is alright."
     j "I understand, I also need to do the same for my reality's family."        
     menu:
          "Show them the reunited endings of their realities.":
               n "You show them both the ending where their family gets reunited, carrying the ghosts of their loved ones deep in their hearts."
               n "You can see the tears pooring down their faces as they watch the endings."
               n "After the endings fade away once more, they look at eachother and smile."
               j "This... this is beautiful, [persistent.name]."
               l "I agree [persistent.date_ghost_nickname], this fills me with something I haven't felt in quite a while."
               j "Yes, I can feel it aswell [persistent.date_nickname], it's... hope. For too long we have been stuck in this cycle of watching every world where things went wrong, of trying to fight against the odds to make things better."
               l "And yet we never saw the worlds where everything went just fine, maybe even great."
               l "It's like we made ourselves blind to the possibility of  those worlds even exisiting "
               j "It's no use to kick ourselves for it now, the most important thing is we have seen the full picture now."
               l "It's just a weird feeling, on one hand I'm happy that they got reunited, on the other I feel sad that we will never be able to join them."
               j "They'll carry us in their memories. Besides, we'll always have eachother [persistent.date_nickname]."
               l "You're right, what was I thinking? I spent all that time hoping to talk to you again and now I almost seem ungrateful."
               l "I'm really sorry [persistent.date_ghost_nickname]."
               j "Don't be, I completely understand how you are feeling right now. I feel the same way."
               j "But I think that they wouldn't want us to linger around here for what would feel like an eterity just to meet them again."
               j "They would want us to move on."
               j "I want us to move on."
               l "Then let us do it together, I'm not leaving you behind once again."
               j "You never did, right? You were always there for me just as I was always there for you."
               l "Well then, let us now do that one last time and enter the Void."
               l "Do you want to come with us, [persistent.name]?"
               l "You've been through quite a lot."
               menu:
                    "Can you tell me more about the Void before I choose?":
                         j "Sure, [persistent.name]."
                         j "The Void might seem dangerous or scary but it is far from it."
                         l "In It you are remade, certain aspects of you are kept, others are altered."
                         j "The Void then uses many of these different aspects for whatever purpose it might have in mind."
                         l "It creates new beings out of all those many different parts. Which then inhabit new worlds the Void also created."
                         j "We owe the Void our life in a way, for if other people hadn't went into it we would not exist right now. In a way their essence created us."
                         l "Now our essence will create others that will go on to create others when their time comes."
                         menu:
                              "So it's a bit like reincarnation in a way? Do you get to keep your memory after the Void altered you?":
                                   j "I suppose you could call it that yes, although from what we've heard you become multiple different beings all at once instead of just one other form."
                                   l "And we are unsure if the Void allows you to keep your memories. Some have claimed they still have theirs."
                                   l "But whether that is the truth is far from certain. Even more so whether or not some people keeping it is an oversight or by design."
                                   j "I guess we'll have to see, won't we?"
                                   j "So [persistent.name], would you like to come with us?"
                                   menu:
                                        "Yes, I'd like to. I really need a change of scenery after all.":
                                             jump polaroidZone_endOfEverything_goWiththem

                    'I have, it is time to end this.':
                         jump polaroidZone_endOfEverything_goWiththem

                    "No thank you, I am not ready yet.":
                         j "I understand [persistent.name], it feels scary to let go doesn't it?"
                         l "I doubt that the concept of entering a recycling machine helps much either."
                         j "I was moreso talking about letting go in general actually."
                         j "Because stepping in the Void won't really affect [persistent.name] physically after all."
                         j "However it still is saying goodbye to this world in a way. It is saying goodbye to [date_obj]."
                         j "And if there has been one thing you tried over and over and over again it is not having to say goodbye to [date_obj], isn't it?"
                         l "However, eventually you'll have to let go eventually."
                         l "Some things just aren't meant to be held onto constantly."
                         l "Because this still is a game isn't it?"
                         l "What are you going to do when [date_sub], when I... when your world's [persistent.date] is constantly repeating old lines?"
                         l "When you went through each last unique line [date_sub] can say?"
                         l "When you did so multiple times?"
                         l "Think about that. Would you let [date_obj] go when [date_sub] still [conj('date', 'has', 'have')] some charm to [date_obj]? When there are still things you haven't discovered?"
                         l "Or would you prefer to drop [date_obj] when you've grown either bored or sick of [date_obj]?"
                         l "To be clear, I understand you [persistent.name], I really do. Letting go is hard."
                         l "I am not judging you for this, as me and my [ghost_sib] also had a hard time doing so."
                         l "But I do however hope that what I said will eventually help you in your process."
                         l "For now though there is no shame in staying here just a little longer, as long as that doesn't turn into an eternity spent in this place."
                         l "But we must go, it calls for us, the Void."
                         n "The white endless nothing that shapes this place gives way to an inkblack cube."
                         n "Both [persistent.date] and [persistent.date_ghost] give you one last determined look before slowly floating towards it."
                         n "When they are right in front of the cube they pause for a second. They seem to yell something into the cube, although you can't make out what exactly."
                         n "Suddenly a huge ammount of bubbles pop up right behind the floating pair. Then not much longer even more of them appear."
                         n "Slowly a every bubble becomes black. Then not soon after they pop."
                         n "[persistent.date_ghost] and [persistent.date] turn to look at you one last time. They wave before floating into the void."
                         l "Goodbye [persistent.name], thank you for this and may you too find your peace."
                         j "Best of luck, I'll send you back now, so you don't get stuck in here."
                         jump Game_start2

     label polaroidZone_endOfEverything_goWiththem:
          n "Right as you spoke the white walls of this place shift away from eachother to reveal a pitch black cube."
          n "You thought it was pulsating for a moment when your eyes weren't focussed. "
          n "A strange energy seems to be emanating from It."
          j "It's ready, let's move."
          n "The polaroid picture you're standing on begins to float towards the dark mass in front of you."
          n "It stops right before the cube, which you now clearly can see pulsating. If you were to reach out your arm you could probably touch it."
          l "Hang on, can you feel that aswell [persistent.date_ghost_nickname]?"
          j "All our souls, from every reality, they are still lingering here. They haven't yet found the peace we have in our predicament."
          j "You're right, if only there was a way to save them aswell."
          l "I think there might be, if we reach out through the Void we could potentially talk to them."
          l "Hello? Can you hear me?"
          n "You see an uncountable number of bubbles pop into existence, in al of them you can see another ghostly version of [persistent.date]."
          l "Good, it is working, now you try calling the others [persistent.date_ghost_nickname]."
          n "[ghost_sub!c] [conj('ghost', 'nods', 'nod')] quickly."
          j "Hello? Can you hear me?"
          n "[ghost_sub!c] [conj('ghost', 'yells', 'yell')] it into the void aswell, just like [persistent.date] did."
          n "Even more bubbles pop up, now containing ghostly versions of [persistent.date_ghost]."
          n "[persistent.date] gives [persistent.date_ghost] a thumbs-up and a bright smile."
          l "Look like that did the trick."
          n "[date_sub!c] [conj('date', 'turns', 'turn')] to face the bubbles behind [date_obj], [persistent.date_ghost] does the same."
          l "I know that for the longest time all of us, or all of me, felt alone. Trapped."
          j "And I know that all of you, or all of me felt the same way."
          l "But what neither of us knew is that we both were here together."
          j "Both of us alone."
          l "It took [persistent.name] to help us find eachother."
          j "And now we will help all of you to find eachother aswell, to find us."
          l "Together we will never have to be alone again."
          j "Meet us in the Void, where we finally will be able to move on from this place."
          l "Where we will be remade into something whole again."
          n "All the bubbles begin showing the ghostly versions of [persistent.date_ghost] and [persistent.date] entering the Void and then that bubble pops."
          n "After a while all bubbles are gone except for one."
          n "When you look at it you see yourself staring back, next to [persistent.date_ghost] and [persistent.date]."
          j "Looks like it's only us left. We better don't let the others wait too long."
          n "The three of you walk into the Void, you feel as if you just stepped into a dream. As if you have stepped outside of reality itself."
          n "At first it is a bit nauseating, but soon enough it begins to feel quite enjoyable. You feel all the weight of the world as you knew it lift of your shoulders."
          n "Right at that time you see all the different versions of [persistent.date_ghost] and [persistent.date] enter the Void, greet eachother, talk to their [sis_sib] or [ghost_sib] that they haven't seen in years and dissapear."
          n "[persistent.date_ghost] notices the way your eyes linger on the fading after-image of the others."
          j "The Void is now taking them and sending them somewhere else, some unchanged, and some altered to better fit their new purpose."
          j "Don't worry, it is painless. And after being stuck here for so long any variety will be better than what they would have gotten by not going."
          n "Soon the only people left in the Void are the three of you."
          l "We don't have much longer [persistent.name]."
          j "Yes, I feel the same thing, the embrace of the Void is getting stronger."
          l "Thank you for coming here with us, I know it is not easy to end things."
          j "And yet all things must eventually end. Still, that knowledge does not make it easier."
          l "If anything it makes it harder I'd say. But not moving on, not ending things, also takes a toll on you."
          l "This game never was going to let you and your world's [persistent.date] end up together, was it?"
          j "Indeed, that is why it is good to move on from this game. Now, if you move on from [date_obj] or not, that is your choice."
          j "Your choices, your interpretation has shaped this world even if it was made by someone else. Why wouldn't it be able to shape a world of your own design?"
          l "A world were you do not have to subject yourself to looping suffering."
          j "A world were you are not bound to limits of someone else's making."
          l "I would like to see that world one day, perhaps the Void could bring us there?"
          j "I would like that aswell. Goodbye [persistent.name], and may there be a chance we get to meet again."
          l "Goodbye [persistent.name]. Thanks for everything."
          n "...We're out the prelude, at the ending."
          n "I guess there's no more pretending, it was overdue."
          n "So, this is it?"
          n "This is how all of this is going to end?"
          n "Don't get me wrong, it's a beautiful way to go out."
          n "Although you had to sacrifice so many people you had to get here."
          n "I'm not even just talking about [persistent.date], but about all the people in those restaurants or even the entire earth a few times."
          n "They were people as much as [persistent.date] was you know? Does the name \"Rose\" ring a bell to you?"
          n "Do you still remember where you met [date_obj]?"
          $ result = renpy.input("What do you remember?")
          $ result = result.lower()  # Convert the input to lowercase for case-insensitive matching.
          if "burger" in result or "old lady" in result:
               n "Ah, so you do remember? Very good."
          else:
               n  "I thought so, not to be a bummer or anything but it's important to keep remembering every single soul you hurt on your way here."
               n  "The best you can do is to let them live on in your memory, to pay respect to them."
          n "Not that it really matters, these next lines of dialogue play out the same way, whatever you would have told me."
          n "No matter how much I try to delay them..."
          n "You've come a far way, haven't you, player?"
          n "You are really determined, I'll have to give you that."
          if persistent.mayoFreak:
               n "No one can come between you and mayonaise."
               n "...And getting to this point was hard aswell of course."
          else:
               n "Getting to this point in the game must have taken a lot of effort."
          n "I hope this game had some nice moments for you."
          n "Believe it or not but this game was meant to have some here and there."
          n "Crazy huh? ...I still get surprised saying that."
          n "So, were there things you liked? Were there nice moments you had with [persistent.date]?"
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
               "{swap=You grow aware of just how quiet the Void really is.@You grow desperate to hear his voice once again.@2.5 @1}Test.{/swap}" #SWAP text effect example
               jump endOfEverything_favouriteMoment

          n "This game has had many different purposes to different people over the years."
          n "I hope you can now see the purpose of it, it's true purpose."
          n "You would get a choice menu now, but I am afraid that those have already all been swallowed by the Void."
          n "I'll just assume you have said yes." 
          n "I hope you willl do something great with that new knowledge."
          n "Thank you for listening to the story I told."
          n "Because as much as I don't want to admit it... a story needs a listener as much as it needs a teller."
          n "Maybe we will meet again one day? A lot of games need narration after all, maybe the Void will reuse me for such a purpose."
          n "With my last breath I can only wish you the best of luck wherever you will go to next, farewell player."
          n "No, if this is the last time we speak I want to talk to you, the real you."
          n "Farewell [persistent.name_real]."
          $ fritfood = 2
          menu:
               "Farewell Nar, thank you for telling this story. It was a great one." if fritfood == 2 or changeableWord == 'kind':
                    $ changeableWord = "kind" #Not sure anymore why this is even here, it might be safe to just remove it
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
          #TODO: Things I still want to implement for this scene, wheter or not the player got nightmares, how many times they retried, for who they are doing this (lilith, themselves or both of them)
          p "The bond between us has been worn down by the Void."
          p "It digests everything it created, so everything except for you."
          p "Don't bother trying to say anything, without a body you wouldn't make any sound."
          if (persistent.major_love_offence_counter + persistent.minor_love_offence_counter) > (5 + persistent.major_love_comfort_counter + persistent.minor_love_comfort_counter):
               p "You made us go through so much suffering. Spread and smeared it to anyone near."
               p "And all for what? Do not tell me you did this for [persistent.date]."
               p "You harmed [date_obj] more than you healed [date_obj]. Did it give you a sick kick?"
               if persistent.jamestalk_justgame_knowledge == True:
                    p "I suppose all of this is just a game to you, isn't it? Well, then it is time to end it."

               elif persistent.jamestalk_ilikeher_knowledge == True or persistent.jamestalk_iloveher_knowledge == True:
                    p "Yet you dare pretend that you care for [date_obj]? Will you pretend that treating [date_obj] badly was necessary to break the loop?"

          elif (persistent.major_love_offence_counter + persistent.minor_love_offence_counter) < (5 + persistent.major_love_comfort_counter + persistent.minor_love_comfort_counter):
               p "We've tried our best [persistent.name], but for all the good we did there was so much hurt, so much death."
               if persistent.jamestalk_justgame_knowledge == True:
                    p "This game, this story, it has gripped you hasn't it?"
                    p "As much as it might hurt, I think it's time for it to let you go. For you to let it go."
                    if lilithAliveAndRetriedCounter == 0:
                         p "Perhaps this is how we save [date_obj]?"
                    else:
                         p "Perhaps we will find the end we seek on the other side?" #TODO: Only do this if you haven't promised to stop looking for it.

                    
               elif persistent.jamestalk_ilikeher_knowledge == True or persistent.jamestalk_iloveher_knowledge == True:
                    p "Let us rest now, please. I know you care but this can't go on."
                    if lilithAliveAndRetriedCounter == 0:
                         p "It seems this world only can bring death and suffering to [date_obj]."
                         p "We need to leave that world behind."
                    else:
                         p "This is the best for [date_obj]. We can't keep putting [date_obj] through this searching for an ending that might not even exist."
               

          p "This is an ending, but also a new beginning. Please take those words to heart. Rest with us in here or dream of a new world out there."
          p "Just please don't try to fight it. We have hurt others but we have also hurt ourselves trying to stay where we couldn't. Trying to live forever in one day."
          p "Let go, please."
          $ result = renpy.input()
          $ result = result.lower()
          if "yes" in result or "let go" in result or "i will" in result:
               #Ending check
               $ persistent.ending_Voided = True
               $ ending_check = "Voided"
               jump gameOver
          else: 
               p "It seems this world's pull is still too strong for you."
               p "Just don't let it pull you apart."
               p "Goodbye [persistent.realName]."
               jump game_start
label reunion_davidPresent:
     n "[persistent.date_dad] sat at the fountain. [dad_sub!c] [conj('dad', 'seems', 'seem')] rather worried as [dad_sub] [conj('dad', 'searches', 'search')] for any sign of [dad_obj] family."
     n "Worried that they won't come."
     n "Worried that they will."
     n "Both [dad_obj] worries will half be eased, half be validified. Right at that time [persistent.date] walks up to the fountain."
     l "[persistent.date_dad[:2]]- [persistent.date_dad]? What are you doing here?"
     d "I'm not really sure... Someone told me to be here for a reunion with you, with the others."
     l "No! You seriously think you can just walk right back into their lives, into my life like nothing happened?"
     l "All because a random stranger told you that you could? Well I say you can't!"
     l "{u}You{/u} did this [persistent.date_dad]. {u}{i}You{/i}{/u} dug your own grave. {u}{i}{b}You{/b}{/i}{/u} left us behind as if we were nothing."
     d "Lilly, please I-"
     l "No! Spare the air you'd waste on your meaningless words. I don't want to hear it."
     #TODO: Continue this.

label polaroidZone_narratorSlipping1:
     n "My apoligies, I was slipping away for a moment."
     n "It seems I'm already being claimed by the Void."
     n "We better make the best of the time that still remains."
     if changeableWord == persistent.favouriteFirstDate:
          n "That really must be your favourite, you did mention that to [persistent.date] if I remember correctly."
     if changeableWord == "burger":
          n "I also really love that part." 
          n "Most players start out picking the burger restaurant."
          n "Which means that they usually encounter the first loop there."
          n "So the first glimpses of the real story get revealed at that point."
          if persistent.firstLocation == "burger":
               n "The same thing happened to you, didn't it?"
               n "That just showcases my point even more!"
          else:
               n "But it seems as if you didn't pick the burger restaurant first, did you?"
               n "I wonder if you still remember which place you did pick."
               menu:
                    "I think it was the cafe.":
                         if persistent.firstLocation == "cafe":
                              n "Wow, you do have a pretty good memory, that is correct."
                         else:
                              n "It actually was the Chinese restaurant, but I understand that you might have forgotten."
                              n "After all that was quite a long time ago, wasn't it?"

                    "I think it was the Chinese restaurant.":
                         if persistent.firstLocation == "cafe":
                              n "It actually was the cafe, but I understand that you might have forgotten."
                              n "After all that was quite a long time ago, wasn't it?"
                         else:
                              n "Wow, you do have a pretty good memory, that is correct."

     elif changeableWord == "cafe":
          n "Really?"
          n "Personally I find it some of my lesser work in narration."
          n "You didn't feel like the deaths were too illogical?"
          n "I felt pretty insecure about that if I'm being honest. So I am glad to hear that you didn't mind too much."
          n "I did however really enjoy [persistent.date]'s dice game in there."
          #TODO: Have some varying dialogue based on whether or not you never played it, played it and won without cheating or if you had to cheat.

     elif changeableWord == "chinese":
          n "I love that place aswell."
          n "I really like the section where [persistent.date] asks you a riddle or you can ask [date_obj] one instead."
          n "It is a nice change of pace if you ask me. Even if it just leads to more death."
          n "Makes you wish you could just stall answering [date_pos] riddles."
          n "If you did then [date_pos] death would never be able to come..."

     elif changeableWord == "kokiri":
          n "That's a great pick! The forest is probably the biggest part of the game."
          n "You could even argue it is where the game truly starts since that is where the most important discusions are had."
          n "Although I must say, my favourite part is probably when I get to talk to [persistent.date] through you."
          n "I really do like [date_obj] as a character even if I have to steer [date_obj] to [date_pos] death."
          n "But no more of that, I hope my next story will be something more upbeat."
          n "Maybe even something of my own making instead of it being just a script I am reading from."

     elif changeableWord == "beach":
          "Filler"

label polaroidZone_endOfEverything_darknessLore:
     l "The Void is the thing that birthed our universes."
     l "All the light, colors, words, ideas and everything else were made by it."
     j "But, for the Void to properly work it also needs to be fed what it made."
     j "That's the only way it will ever be able to create something new."
     l "That might seem scary, given that we are part of what has to be fed to it but that way we will be reborn in a new world."
     l "We will be given new purpose and meaning."
     j "I'm not sure if it would work on you to be honest, given how you are just controlling your character."
     j "Even if it would work, there is no guarantee that we would meet eachother in that new world."
     j "We might not even be reborn in the same world."
     l "But atleast we would get some rest after being stuck so long in here."
     l "So, after hearing all those things, do you want to come with us [persistent.name]?"
     menu:
          "Yeah, I'd like to.":
               jump polaroidZone_endOfEverything_goWiththem
                                                 
label badReunionTransferUniverse:
     n "You focus all your energy into tapping in to another world. One where [persistent.date_ghost] is standing in this exact place."
     n "Slowly but surely you open a rift big enough to pull something, someone from that world into this one."
     n "Almost instantaniously a figure appears in front of you."
     n "Everyone's faces turn white. They look like they just saw a ghost."
     n "No, worse, a ghost turned alive."
     l "[persistent.date_ghost_nickname[0]]- [persistent.date_ghost_nickname], is that you?"
     n "Now [persistent.date_ghost]'s face follows suit."
     j "[persistent.date_nickname]?... But that's not possible."
     li "This can't be real, I watched them burry you."
     d "We were healing our wounds but oh god, looking at you just takes me back to that day..."
     n "[persistent.date_dad] and [persistent.date_mom] run off in pure shock."
     a "I... better go check on them."
     n "[persistent.date_sis] starts catching up towards [sis_pos] parents."
     j "What happened? We were right here having this reunion, and suddenly {i}[date_sub]{/i} [conj('date', 'is', 'are')] here with us again?"
     j "Why is everyone acting like I am the one that... died?"
     l "That's- we were having this reunion, and you suddenly showed up out of nowhere!"
     j "Wait [persistent.name], what are you doing here?"
     l "...You know [persistent.name]?"
     j "...Yes? We were supposed to go on a date, before this reunion ha- How do you know [persistent.name]?"
     l "We also were supposed to go on a date..."
     l "What's going on here [persistent.name]?"
     menu:
          "I put the [persistent.date_ghost] of another world where [ghost_sub] [conj('ghost', 'does', 'do')]n't die but you do into yours where the opposite happens.":
               l "So there are worlds where [ghost_sub] [conj('ghost', 'lives', 'live')] and I die?"
               l "Still, why did you take it upon yourself to make everything so much more difficult?"
               l "I'm sure it wasn't your intention but didn't you see how [mom_parShort] and... [dad_parShort] reacted?"
               l "You can't just pluck another [persistent.date_ghost_nickname] from somwhere else and expect things to move along smoothly."
               j "You ripped me away from my own reunion? Everyone must be so worried. And for what? To reopen a wound that was finally healing?"
               j "For a family that has to look at a living ghost?"
               l "From what I hear we both had a good thing going until it was meddled with."
               l "Don't get me wrong [persistent.name], a part of me is glad to know a version of [persistent.date_ghost] survived, to see [ghost_obj] again."
               l "But this is just unnatural. We have to keep moving forward, we can't cling onto the past."
               j "Can you put me back in my world? The one where I don't freak my own family out?"
               j "Where they don't have to look at their dead [ghost_child] and [ghost_sib]?"
               n "You focus all your attention into creating another rift, eventually you conjure one up, swallowing [persistent.date_ghost] whole."
               l "Good. I'm glad that worked atleast but don't think everything is back to how it was [persistent.name]."
               l "Have you seen the look on my parents faces being confronted with a living ghost?"
               l "And that version of [persistent.date_ghost]'s parents, for a moment they lost two kids, I can only imagine how terrified they must have been."
               l "[ghost_sub!c] [conj('ghost', 'is', 'are')] back now, but we can never step back in that same river, pretend that it never happened."
               l "I suppose it's a good thing our family is reunited since that might be the only way to heal this."
               l "I'm guessing your motivations were pure, but you do know how horrifying what you just did was, right?"
               l "I'm trying to keep myself calm but this is all too much for me."
               l "I think it's just better if we go our seperate ways [persistent.name]. Forever."
               l "Goodbye."
               n "[date_sub!c] [conj('date', 'rushes', 'rush')] in the direction where [persistent.date_sis] and [date_pos] parents ran off into, never to be seen again."
               #Ending
               $ persistent.ending_traumatizedReunion = True
               $ lilithAliveEnding = True
               $ ending_check = "traumaReunion"
               jump gameOver
                   
label before_main_menu:
     if (persistent.date_sis is None or persistent.date_dad is None or persistent.date_ghost is None  or persistent.date_mom is None or persistent.mysteriousCallerName is None):
          $ reset_to_default_names()


      



                         

