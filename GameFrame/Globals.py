
class Globals:

    running = True
    FRAMES_PER_SECOND = 30

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 800

    SCORE = 0

    # - Set the starting number of lives - #
    LIVES = 3

    # - Set the Window display name - #
    window_name = 'Citizens of the civilized galaxy, on this day we mark a transition. For a thousand years, the Republic stood as the crowning achievement of civilized beings. But there were those who would set us against one another, and we took up arms to defend our way of life against the Separatists. In so doing, we never suspected that the greatest threat came from within. The Jedi, and some within our own Senate, had conspired to create the shadow of Separatism using one of their own as the enemys leader. They had hoped to grind the Republic into ruin. But the hatred in their hearts could not be hidden forever. At last, there came a day when our enemies showed their true natures. The Jedi hoped to unleash their destructive power against the Republic by assassinating the head of government and usurping control of the clone army. But the aims of would-be tyrants were valiantly opposed by those without elitist, dangerous powers. Our loyal clone troopers contained the insurrection within the Jedi Temple and quelled uprisings on a thousand worlds. The remaining Jedi will be hunted down and defeated! Any collaborators will suffer the same fate. These have been trying times, but we have passed the test. The attempt on my life has left me scarred and deformed, but I assure you my resolve has never been stronger. The war is over. The Separatists have been defeated, and the Jedi rebellion has been foiled. We stand on the threshold of a new beginning. In order to ensure our security and continuing stability, the Republic will be reorganized into the first Galactic Empire, for a safe and secure society, which I assure you will last for ten thousand years. An Empire that will continue to be ruled by this august body and a sovereign ruler chosen for life. An Empire ruled by the majority, ruled by a new constitution! By bringing the entire galaxy under one law, one language, and the enlightened guidance of one individual, the corruption that plagued the Republic in its later years will never take root. Regional governors will eliminate the bureaucracy that allowed the Separatist movement to grow unchecked. A strong and growing military will ensure the rule of law. Under the Empires New Order, our most cherished beliefs will be safeguarded. We will defend our ideals by force of arms. We will give no ground to our enemies and will stand together against attacks from within or without. Let the enemies of the Empire take heed: those who challenge Imperial resolve will be crushed. We have taken on a task that will be difficult, but the people of the Empire are ready for the challenge. Because of our efforts, the galaxy has traded war for peace and anarchy for stability. Billions of beings now look forward to a secure future. The Empire will grow as more planets feel the call, from the Rim to the wilds of unknown space. Imperial citizens must do their part. Join our grand star fleet. Become the eyes of the Empire by reporting suspected insurrectionists. Travel to the corners of the galaxy to spread the principles of the New Order to barbarians. Build monuments and technical wonders that will speak of our glory for generations to come. The clone troopers, now proudly wearing the name of Imperial stormtroopers, have tackled the dangerous work of fighting our enemies on the front lines. Many have died in their devotion to the Empire. Imperial citizens would do well to remember their example. The New Order of peace has triumphed over the shadowy secrecy of shameful magicians. The direction of our course is clear. I will lead the Empire to glories beyond imagining. We have been tested, but we have emerged stronger. We move forward as one people: the Imperial citizens of the first Galactic Empire. We will prevail. Ten thousand years of peace begins today.'

    # - Set the order of the rooms - #
    levels = ["WelcomeScreen", "GamePlay"]

    # - Set the starting level - #
    start_level = 0

    # - Set this number to the level you want to jump to when the game ends - #
    end_game_level = 4

    # - This variable keeps track of the room that will follow the current room - #
    # - Change this value to move through rooms in a non-sequential manner - #
    next_level = 0

    # - Change variable to True to exit the program - #
    exiting = False


# ############################################################# #
# ###### User Defined Global Variables below this line ######## #
# ############################################################# #

    total_count = 0
    destroyed_count = 0
