# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Theodore", color="#4b7200")
define t = Character("[taylor_name]", color="#a87533")
define g = Character("Robin", color="#830e0e")
define o = Character("Oracle Sapphire", color="#efa0fd")
define r = Character("Rhyme", color="#ffaf24")
define n = Character(" ")
define q = Character("???", color="#ffffff")
define d = Character("???", color="#a87533")
define g1 = Character("Guard Red", color="#ff4b4b")
define g2 = Character("Guard Blue", color="#00a8ff")
define g3 = Character("Guards Red and Blue", color="#623abc")
define e = Character("Eliot", color="#e4e4d5")
define e1 = Character("Silver", color="#98948e")
define e2 = Character("Elise", color="#f3e972")
define tr = Character("[taylor_name] and Rhyme")
define rb = Character("Rhyme and Theodore")


image taylor angry flip = im.Flip("taylor angry.png", horizontal=True)
image taylor cat hat flip = im.Flip("taylor cat hat.png", horizontal=True)
image taylor irritated flip = im.Flip("taylor irritated.png", horizontal=True)
image taylor neutral hat flip = im.Flip("taylor neutral hat.png", horizontal=True)
image taylor neutral scarf flip = im.Flip("taylor neutral scarf.png", horizontal=True)
image taylor think scarf flip = im.Flip("taylor think scarf.png", horizontal=True)
image taylor think flip = im.Flip("taylor think.png", horizontal=True)
image taylor neutral flip = im.Flip("taylor neutral.png", horizontal=True)
image taylor startled flip = im.Flip("taylor startled.png", horizontal=True)
image taylor glow1 flip = im.Flip("taylor glow1.png", horizontal=True)
image taylor glow2 flip = im.Flip("taylor glow2.png", horizontal=True)
image elise angry flip = im.Flip("elise angry.png", horizontal=True)
image elise happy flip = im.Flip("elise happy.png", horizontal=True)


default north1 = False
default south1 = False
default east1 = False



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.



    show bg prologue
    with dissolve
    play music "<loop 16.977>music/theodore theme.ogg"

    d "I heard your mentor died recently."

    b "Yes."

    d "Do you wonder when you'll be next?"

    b "...I'll admit.....I've been uneasy since Stanley died.  This is part of the reason I wanted to talk to you. Do you know the other part?"

    d "There's only one other reason why a Keeper would want to talk to me."

    stop music fadeout 2.0

    d "... My grandfather said nothing about the treasure he stole from humans."

    b "Did he leave anything behind?"

    d "We found a letter soon after his death.  It's addressed to me, but I haven't read it yet."

    play music "<loop 32.406>music/taylor theme grand.ogg" fadein 2.0

    b "I know that I should be the one to recover the artifact, Pandora’s Box, but can I ask you to reclaim it in my stead?"

    d "Why can't you do it yourself?"

    b "I have more important duties that only I can fulfil, and I have the feeling that only you can regain it."

    d "I will gladly assist you."

    b "By the way, you never told me your name."

    python:
        taylor_name = renpy.input("(My name...)")
        taylot_name = taylor_name.strip()
        if not taylor_name:
            taylor_name = "Taylor"
    b "[taylor_name]... So you're the feline beast who lives among humans."


    t "Will that be a problem?"

    b "No. If anything, it will make your task easier."

    t "I wish you luck on your quest."

    b "And I wish you luck on your task, [taylor_name]."

    stop music fadeout 5.0
    show bg black
    with fade

    n "SilverCraft presents:"
    n "The Keys of Chaos"

    n "Gale Town"

    n "Later that day...."

    show taylor neutral at right
    show bg home
    with dissolve

    t "(Sigh) Time to read that letter."

    play music "<loop 32.869>music/taylor theme e.ogg" fadein 2.0
    hide taylor neutral flip
    show bg robin
    with dissolve

    g "Little Kitten, not so little anymore I hope...."

    show taylor angry at right
    stop music

    t "......Grandpa......!!!!! You old fart.....!!!"
    hide taylor angry
    show taylor what at right
    t "......Not that you can hear me.....I hope....."

    play music "<loop 32.869>music/taylor theme e.ogg" fadein 2.0
    hide taylor what
    with dissolve

    g "Remember those stories I told you about my epic adventures..."

    g ".....stealing that treasure from those stinky humans?"
    g "Hahaha, anyway, there were four keys that could open an artifact I like to call the Pandora’s Box."
    g "I only stole the box though, which was the most important part.  Quite smart of me if I say so myself."
    g "(Sigh) If only they didn’t try to go after my head.  Ahhh, those days running and thieving.....I miss them."

    g "Back to the point, I never did manage to steal the keys, but I did meet an Oracle......."

    g "Good luck!!"
    g "- Robin Wolf"

    show bg home
    show taylor neutral at right
    with dissolve
    t "Oh Grandpa, you never change.  Always the same ol’ cat....."
    t "I guess the first step would be......to find that Oracle."

    t "It would be best to head out tomorrow."

    hide taylor neutral at right
    show bg chapter1
    with fade
    stop music fadeout 2.0
    show bg black
    with fade
    n "The next morning....."
    show bg home
    show taylor neutral flip at left
    with fade

    t "Well, time to head out."

    hide taylor neutral flip
    hide bg home
    with dissolve
    show bg lake
    show taylor neutral hat flip at left
    with dissolve

    t "(This looks like a good place to stop for water.)"

    hide taylor neutral hat flip
    show taylor startled flip at left

    n "Crash!"
    n "RAARGH!"
    t "What was that?!"

    hide taylor startled flip
    show bg rhymian
    with dissolve
    q "raargh..."
    show taylor irritated flip at left
    with dissolve
    t "(That dragon must have been burnt.  I should help it.)"
    hide taylor ittitated flip
    show taylor neutral hat flip at left
    with fade
    t "(I've done all I can.  I should stay the night and check on the dragon in the morning.)"

    hide taylor neutral hat flip
    show bg lake
    show rhyme happy at right
    with fade

    n "Whoosh"

    show taylor irritated flip at left

    t "(What's with the sound of breathing?)"

    show taylor startled flip at left

    t "Waa!"

    hide taylor startled flip
    n "Thud"

    q "Are you okay?"

    show taylor neutral hat flip at left
    with dissolve

    t "Y-yes.  Who are you?"

    play music "<loop 2.373>music/rhyme theme.ogg" fadein 1.0
    show rhyme excited at right
    r "Oh! My name is Rhymian, but you can just call me Rhyme."
    r "Thank you for helping me!"
    hide rhyme excited
    show rhyme happy at right
    menu:

        r "Anything I can do in return?"

        "Yes":
            jump agree
        "No":
            jump disagree
label agree:
    show taylor think flip at left
    t "My name is [taylor_name], and I need to find someone."
    r "Someone?  Wait...."

    menu:
        r "Does your journey.....have anything to do with the Keepers??!!"

        "Yes":
            jump agree1

        "No":
            jump disagree1

    label agree1:
        show taylor neutral hat flip at left
        t "Eh? How did you know?"
        show rhyme excited at right
        r "Oh! I just knew it!!  Tell me, tell me, what kind of mission are you doing?  Don’t be cheap, tell me!!  Come on, I’ll keep it a secret!!"
        t "Well..."
        hide rhyme excited at right
        hide taylor neutral hat flip at left
        show rhyme happy at right
        show taylor neutral hat flip at left
        with fade
        r "I see, I see.... Let me help you!!"
        hide rhyme happy
        hide taylor neutral hat flip
        show bg flight
        with fade
        jump flight1
    label disagree1:
        show taylor think flip at left
        t "No...."
        hide rhyme happy
        show rhyme sad at right
        r "What do you mean, no?"
        hide rhyme sad
        show rhyme happy at right
        r "...Wait a minute.  I see where this is going."
        hide rhyme happy
        show rhyme excited at right
        r "This is a secret mission, isn’t it?!"
        hide taylor think flip
        show taylor irritated flip at left
        t "It’s-"
        hide rhyme excited
        show rhyme happy at right
        r "No need to elaborate, I understand, just tell me where to go!!"
        hide taylor irritated
        show taylor neutral hat flip at left
        t "I need to find an Oracle."
        hide rhyme happy
        show rhyme excited at right
        r "Oracle?  Yes!!  I know where she is!!!!!!  Just hop on my back, I’ll take you to her."
        hide rhyme excited
        hide taylor neutral hat flip
        show bg flight
        with fade
        jump flight1
label disagree:
    show taylor neutral hat flip at left
    t "Nah, I just wanted to make sure you were okay."
    show rhyme happy at right
    r "I see...."
    show taylor think flip at left
    t "(mumbles) But I do need to find that Oracle."
    show rhyme excited at right
    r "Did you say Oracle??!! "
    r "You did, didn’t you!!"
    r "I know where she is!!!!!!"
    r "Hop on my back, let’s go find her now!!!!"
    hide rhyme excited
    hide taylor think flip
    show bg flight
    with fade
    jump flight1

label flight1:
    t "So, Rhyme, how did you get hurt?"
    r "I was testing out a new fire move and it backfired."
    t "Ouch."
    r "Yeah, but thanks to you, I got help in time."
    t "..."
    r "Anyway, I can't believe I'm helping the Keepers right now!!!"
    t "Why?"
    r "I'm related to Aragon the dragon, the first Keeper."
    r "I've always wanted to be as cool as him!"
    r "I can tell you the story!"
    t "(Oh boy, here we go.)"
    stop music fadeout 3.0

label crystalCaverns:
    show bg black
    with fade

    r "We’re here!!!"

    show bg caverns
    play music "<loop 9.651>music/crystal caverns.ogg"
    show taylor neutral hat flip at left
    with fade

    t "So this is it..."
    t "(What a pretty place.....)"

    r "I can’t go in, it’s too small for me."
    r "I’ll wait outside......Good luck!!"

    t "Okay."

    show bg caverns
    with fade

    t "(This place is beautiful.....)"

    hide taylor neutral hat flip
    show taylor startled flip at left

    q "Who goes there?!"

    t "Wahhh!!!!  Who is it?  What do you want?  I’m not tasty!!"

    q "I’m not going to eat you."

    t "How am I supposed to know that?!"

    q "....."

    hide taylor startled flip
    show taylor irritated flip at left

    t "Reveal yourself then.  Maybe I won’t be as sca- surprised!"

    q "(Sigh) Okay...."

    show oracle at right

    t "Wow, you’re really shiny..."

    hide taylor irritated flip
    show taylor cat hat flip at left

    t "......."

    hide oracle
    show oracle worried at right

    q "Wh-What are you doing?!"

    hide taylor cat hat flip
    show taylor irritated flip at left

    t "E-Eh?  Ah! S-Sorry!  I’m almost got carried away...."


    hide oracle worried
    show oracle at right

    q "It’s okay.  I know how cats are around objects like these sparkles."
    q "...By the way, who are you?"

    t "Before asking someone for their name, shouldn’t you introduce yourself first?"

    o "Ah, my bad.  I’m the Oracle Sapphire."

    hide taylor irritated flip
    show taylor neutral hat flip at left

    t "Oh, so you’re the Oracle!  I’ve been looking for you.  My name is [taylor_name]."

    o "Nice to meet you, [taylor_name]."
    o "Wait, [taylor_name]?  Your name is [taylor_name]?!"

    t "Yes, why?"

    o "So you’re the one foretold of by the prophecy!"
    o "......I thought you’d be human......."

    hide taylor neutral hat flip
    show taylor irritated flip at left

    t "Is there a problem with me being a cat?"

    o "No, no, no. No problem.  If you’re here, you must have gotten Robin’s letter."

    t "Yes, I got Grandpa’s letter.  I was supposed to look for you for....something."

    o "Hahaha, he must have left something out of the letter.  The thing he wanted you to look for are the keys, right?"

    hide taylor irritated flip
    show taylor neutral hat flip at left

    t "Yes."

    o "I have one, the Time Key.  There are four in all:"
    o "The Key of Time,"
    o "The Key of Creation,"
    o "The Key of Destruction,"
    o "and the Key of the Mind."

    hide taylor neutral hat flip
    hide oracle
    show bg white
    with dissolve
    show taylor neutral hat flip at left
    show oracle at right
    show bg caverns
    with dissolve

    t "You’re giving it to me just like that?"

    o "Of course not!"
    o "If it hadn’t been for the fact that Robin saved me, I wouldn’t have given it to you!!"

    t "Saved you?"

    o "That key has been both a blessing and a curse."
    o "Because of the allure of its power, I had to run and hide in so many different places."
    o "Using the power of the key, I managed to escape.  However, one day, I was caught off guard and cornered."
    o "Just when I thought I was going to die, Robin saved me."

    hide taylor neutral hat flip
    show taylor irritated flip at left

    t "I see."

    o "Take care of it."

    hide taylor irritated flip
    show taylor neutral hat flip at left

    t "I will."

    o "This key will guide you to the others."

    o "I wish you well on your journey."

    t "Thank you."

    hide oracle
    hide taylor neutral hat flip at left
    stop music fadeout 2.0
    show bg chapter2
    with fade
    show bg lake
    show taylor neutral hat flip at left
    show rhyme excited at right
    with fade
    play music "<loop 2.373>music/rhyme theme.ogg"

    r "You're back!"

    t "The Oracle told me that this key will point us towards the others."

    hide rhyme excited
    show rhyme happy at right

    r "Cool!  How does it do that?"

    t "It's easy!"

label compass:

    menu:
        t "You just need to ..."

        "Point it towards the sky.":
            jump keyblade
        "Sense its magical powers.":
            jump supernatural
        "Put it in a water dish.":
            jump needle
label keyblade:
    stop music fadeout 3.0
    hide rhyme happy
    hide taylor neutral hat flip
    show bg white
    with dissolve
    t "With the powers vested in me as a feline beast......."
    t "I command you to show me the locations of the other keys!"
    t "........."
    show bg lake
    show taylor irritated flip at left
    show rhyme sad at right
    with dissolve
    play music "<loop 2.373>music/rhyme theme.ogg" fadein 2.0
    r "Well, that didn't work."
    t "I guess that isn't how I'm supposed to use the key."
    hide rhyme sad
    hide taylor irritated flip
    show rhyme happy at right
    show taylor neutral hat flip at left
    r "So if that didn't work, what else can we do?"
    hide taylor neutral hat flip
    show taylor neutral hat flip at left
    t "Hmmmm......"
    jump compass

label supernatural:
    stop music fadeout 3.0
    hide rhyme happy
    hide taylor neutral hat flip
    show bg black
    with dissolve
    r "......."
    t "......."
    r "Do you sense anything?"
    t "Nothing."
    play music "<loop 2.373>music/rhyme theme.ogg" fadein 2.0
    show bg lake
    show taylor irritated flip at left
    show rhyme sad at right
    with dissolve
    r "Well, that didn't work."
    t "I guess that isn't how I'm supposed to use the key."
    hide rhyme sad
    hide taylor irritated flip
    show rhyme happy at right
    show taylor neutral hat flip at left
    r "So if that didn't work, what else can we do?"
    hide taylor neutral hat flip
    show taylor neutral hat flip at left
    t "Hmmmm......."
    jump compass

label needle:
    t "You know the compass trick, right?"
    r "Yeah, you magnetize a needle and make it float on water."
    r "Why would that help?"
    t "Look."
    hide rhyme happy
    hide taylor neutral hat flip
    show bg compass
    with dissolve
    r "The key floats?!"
    t "On top of that, it points in the same direction regardless of how I turn it."
    r "All right, let's go!"
    show bg flight
    with fade
    jump flight

label flight:
    if north1 and east1 and south1:
        jump chapter3
    r "Where does the compass point?"
    menu:

        t "The compass points......."

        "...North.":
            if north1:
                r "We already got the Key of Creation."
                jump flight
            else:
                jump north
        "...East.":
            if east1:
                r "We already got the Key of Destruction."
                jump flight
            else:
                jump east
        "...South.":
            if south1:
                r "We already got the Key of the Mind."
                jump flight
            else:
                jump south
label north:
    r "Key in the North, here we come!"
    t "Okay!"
    show bg lava
    show rhyme happy at right
    show taylor neutral hat flip at left
    with fade
    play music "<loop 10.837>music/city music.ogg" fadeout 2.0
    t "Why did we stop here?"
    r "Look there.  There are humans there.  I'm a dragon, and humans would definitely be suspicious."
    t "......."
    t "Woah!"
    hide rhyme happy
    hide taylor neutral hat flip
    with dissolve
    t "(This looks like a land of destruction...)"
    r "Amazing, right?"
    t "Yeah, this is both beautiful and dangerous."
    show rhyme happy at right
    show taylor neutral hat flip at left
    show bg lava
    with dissolve
    r "I'll wait around here.  You go on ahead."
    t "Okay."
    hide rhyme happy at right
    with dissolve
    t "(I should pull my scarf up.)"
    hide taylor neutral hat flip
    show bg fire city
    show taylor neutral scarf flip at left
    show guards at right
    with fade
    g1 "Halt!"
    g2 "State your name and buisness"
    t "My name is [taylor_name] Wolf."
    t "I'm here on business for the Keeper."
    g1 "The Keeper?"
    g2 "(I heard a legend about the Keepers.)"
    g2 "(They were magical creatures, so I thought they were all myth)"
    g2 "(This strange visitor seems to suggest that they may have existed)"
    g1 "(You really think the Keepers are still alive?)"
    g2 "(Seems so.  If my hunch is correct, this visitor might be able to help this city!)"
    g1 "Very well, then."
    g3 "You may enter!!"
    t "Thank you."
    hide guards
    with fade
    t "(The key here must have changed this land. I wonder what kind of power the key here has.)"
    t "(It's getting late, though.  Perhaps I should rest at an inn.)"
    hide taylor neutral scarf flip at left
    show bg black
    with fade
    stop music fadeout 1.0
    n "The next morning....."
    hide bg black
    play music "<loop 10.837>music/city music.ogg"
    show taylor neutral scarf flip at left
    show bg fire city
    with fade
    t "(What a good night's rest!!  Now time to look for the key.)"
    t "(If I take away the key, will there be any reprecussions?)"
    t "(No.  The damage has been done.)"
    t "(If there's one thing I know about magic, it's that it can never be undone.)"
    hide taylor neutral scarf flip
    show taylor glow1 flip at left
    with fade
    t "(The key is glowing!)"
    t "(...And people are starting to look at me.)"
    t "(I need to retreat somewhere......)"
    t "(Mmm?)"
    hide taylor glow1
    show taylor glow2 flip at left
    t "(The key is glowing even brighter!)"
    t "(This must mean........a key is nearby!!)"
    t "(My intuition tells me that I should go to the topmost floor.)"
    show bg home
    with fade
    show eliot happy at right
    with dissolve
    q "Who are you?"
    t "I'm [taylor_name].  Who are you?"
    show eliot happy at right
    q "Haha, I'm a person with a cursed fate."
    t "Huh?"
    e "My name is Eliot.  I'm assuming you're here for this key of Creation?"
    t "Yes.  Could you give it to me?"
    e "Of course!"
    t "Why?"
    hide eliot happy
    show eliot sad at right
    e "Why?  Because I thought I could help people with this key. "
    e "Not knowing that, in fact, I was just hurting them."
    hide eliot sad
    show eliot happy at right
    e "It's ironic how I brought destruction upon this land when I was trying to create soemthing."
    hide taylor glow2
    show taylor think scarf flip at left
    t "I see...."
    e "No need to feel sorry.  I brought this upon myself."
    e "When you return from your quest, please tell the Keeper that I'm sorry."
    hide taylor think scarf flip
    show taylor neutral scarf flip at left
    t "What?  You know about the Keeper?"
    e "I do.  The Keeper must have sent you here.  I also know that you're a feline."
    e "Anyway, I really wish, when you take the key from this land, everything will return to normal."
    t "..."
    t "(The land will be forever scarred, but......that doesn't mean it can't heal.)"
    hide taylor neutral scarf flip
    hide eliot happy
    show bg lava
    show rhyme happy at right
    show taylor neutral hat flip at left
    with fade
    r "Are you ready to leave?"
    t "Yes."
    play music "<loop 2.373>music/rhyme theme.ogg" fadeout 2.0 fadein 2.0
    hide rhyme happy
    hide taylor neutral hat flip
    show bg flight
    with fade
    $ north1 = True
    jump flight

label east:
    r "All right!  Let's head East!"
    play music "<loop 4.010>music/forest.ogg" fadeout 2.0 fadein 2.0
    show bg forest
    show taylor neutral hat flip at left
    show rhyme sad at right
    with fade
    r "Oh, the compass was pointing us towards this forest."
    t "What forest?  This forest?"
    r "It's called the Forest of No Return."
    hide taylor neutral hat flip
    show taylor think flip at left
    t "Why is it called that?"
    hide rhyme sad
    show rhyme happy at right
    r "Because no one returns, of course!!"
    t "Okay...."
    r "Fine, fine.  Lightning tends to strike unsuspecting victims."
    hide rhyme happy
    hide taylor think flip
    show rhyme sad at right
    show taylor startled flip at left
    n "Rumble"
    hide rhyme sad
    hide taylor startled flip
    show bg white
    n "Crash"
    show bg forest
    show taylor startled flip at left
    show rhyme sad at right
    with dissolve
    t ".....Oh."
    hide taylor startled flip
    show taylor irritated flip at left
    r "Yeah.  That's why this time.....I don't want to come in!!  Lightning is scary!!"
    hide rhyme sad
    with dissolve
    r "Good luck, [taylor_name]!"
    show taylor think flip at left
    t "(Sigh)"
    t "See you later, Rhyme!"
    show taylor neutral scarf flip at left
    with fade
    t "(Rhyme thought I would be struck by lightning...)"
    t "(but I neither heard nor saw any since the bolt that scared Rhyme off.)"
    t "(This forest is beautiful...)"
    t "(I wonder what power the key here might hold.....)"
    hide taylor neutral scarf flip
    show bg village
    show taylor glow1 flip at left
    with fade
    t "(The key here must be nearby.)"
    q "Please, this way."
    t "Why should I go with you?"
    show eli glow at right
    with dissolve
    t "I see..."
    show bg home
    with fade
    q "I assume you too are here for the key?"
    t "There have been others?"
    q "Yes.  I don't mean no harm, but I can't give you this key."
    q "It brought prosperity and peace upon my people, and I don't wish for that to end."
    t "Unfortunately, I have a duty as well and in order to complete it, I must have that key in your hand."
    e1 "......My name is Silver.  Nice to meet you."
    e1 "What's your name?"
    t "My name is [taylor_name]."
    play music "<loop 32.869>music/taylor theme e.ogg" fadeout 2.0 fadein 2.0

label tryAgain:
    e1 "If you answer these two questions correctly, I'll give you this key."
    t ".....Very well."
    e1 "A rooster is sitting at the egde of a barn.  The barn is tilted so that one side is at 60 degrees and the other is at 30 degrees."
    e1 "If the rooster laid an egg, what side would it fall on?"
    t "Hmmm...."
    menu:
        "The egg would always fall on the 30 degree side.":
            jump incorrect
        "The egg would always fall on the 60 degree side.":
            jump incorrect
        "Think about it some more.":
            jump thinkMore
label incorrect:
    e1 "Wrong!!!"
    menu:
        "Try again?":
            jump tryAgain
label thinkMore:
    t "(Why does this question not sit well with me?)"
    menu:
        "There is not enough information.":
            jump incorrect
        "The rooster would sit on the egg, so the egg won't fall.":
            jump incorrect
        "Roosters can't lay eggs.":
            jump correct
label correct:
    e1 "Correct.  There is one more question."

label tryAgain1:
    e1 "Three men go to book a hotel room for three.  They each give the clerk $10 for a total of $30 and go to their room."
    e1 "The manager then tells the clerk that there is a five dollar discount.  The clerk is lost on how to equally give the money back."
    e1 "He then decides to pocket two dollars and gives each of the men three dollars."
    e1 "Since the clerk gave the men three dollars back, each only paid $9 total."
    e1 "But 9 x 3 = 27 plus the $2 the clerk pocketed for a total of $29."
    e1 "Here's the question: Where did the the $1 go?"
    t "Hmmmm....."
    menu:
        "I'm confused":
            jump incorrect1
        "There is no $1.":
            jump correct1
        "The manager has it.":
            jump incorrect1
label incorrect1:
    e1 "Wrong!!"
    menu:
        "Try Again":
            jump tryAgain1
label correct1:
    play music "<loop 4.010>music/forest.ogg" fadeout 2.0 fadein 2.0
    e1 "You got it!  I'll give you the key."
    t "Really?"
    e1 "Yes.  I don't like fighting.  I'd rather you leave peacefully.  Besides, I've done everything I wanted to do with this key."
    hide taylor glow1 flip
    hide eli glow
    show bg white
    with dissolve
    show taylor glow1 flip at left
    show eli happy at right
    show bg home
    with dissolve
    t "What key is it?"
    e1 "The Key of Destruction."
    t "The Key of Destruction?!  How do you create this kind of peace with that power?!"
    e1 "Hahaha, it's quite simple, actually. "
    e1 "Nothing can be created without something being detsroyed."
    t "Interesting."
    e1 "Well, anyway, be on your way, feline."
    hide taylor glow1 flip
    show taylor think scarf flip at left
    t "??!!"
    e1 "Don't be too surprised.  I'm a cat lover.  I can see by how you act and look."
    e1 "Your tail was a big give away though.  I could see it poking through you coat."
    hide taylor think scarf flip
    show taylor neutral scarf flip at left
    t "Is that why you wanted to give me the key so easily?"
    e1 "Of course!  I love cats!!  Any and all types and personalities."
    t "....I....see....."
    e1 "........Will you let me pet you?"
    t "No."
    e1 "Alright, you ought to continue your quest."
    hide eli glow
    show bg forest
    show taylor neutral hat flip at left
    show rhyme excited at right
    with fade
    r "You're alive!!"
    hide taylor neutral hat flip
    show taylor think flip at left
    t "(I'll ignore that comment.)"
    hide rhyme excited
    show rhyme happy at right
    hide taylor think flip at left
    show taylor neutral hat flip at left
    r "Err...You're back!"
    r "Ready to head out?"
    t "Yes."
    play music "<loop 2.373>music/rhyme theme.ogg" fadeout 2.0 fadein 2.0
    hide taylor neutral hat flip
    hide rhyme happy
    show bg flight
    with fade
    $ east1 = True
    jump flight

label south:
    r "South?  Okay."
    show bg flight
    with fade
    r "Oh... this place."
    t "You recognize it?"
    r "Yes."
    r "(Hopefully she let go of the key...)"
    t "Anything wrong?"
    r "No, just be careful."
    show bg islands
    with fade
    t "The land here is beautiful!"
    r "Yup.  The only things that live here are plants."
    t "So then what's that square grid down there?"
    r "Oh yeah, humans also live here, but most of them prefer living in that grid they call a city."
    t "You seem to know a lot about this place."
    r "Of course!  It was my home!"
    stop music fadeout 1.0
    t "Was?"
    play music "<loop 2.849>music/elise.ogg"
    show bg orange
    with dissolve
    n "BOOOM"
    show bg islands
    with dissolve
    t "What was that??!!"
    show bg orange
    with dissolve
    n "BOOM"
    show bg islands
    with dissolve
    t "Rhyme, do you know what's going on?!"
    r "....."
    r "It's the one with the Key of the Mind, Elise."
    t "Eh? How do you know?"
    r "Remember when I told you why I was injured?"
    t "Yes."
    r "She's the one who injured me."
    t "That's cruel."
    r "She's not herself, not since that day..."

label fireAttack:
    t "Another one's coming!!"
    menu:
        "(Which way will you dodge?)"
        "Left":
            show bg orange
            with dissolve
            n "BOOM"
            show bg islands
            with dissolve
            r "That was too close!"
            jump dodge
        "Right":
            show bg orange
            with dissolve
            n "BOOM"
            r "RAARGH!"
            t "AAAHHH!"
            show bg black
            with fade
            t "No...we failed..."
            show bg islands
            with fade
            jump fireAttack
label dodge:
    t "(The key is glowing...)"
    t "Rhyme!  The key!  It's glowing!"
    r "Of course it is!  Didn't you hear me earlier?"
    q "Rhymian, why won't you fight?"
    t "Who are you?!"
    r "That voice is.....Elise!!!!"
    t "Why are you attacking us?!"
    e2 "Rhymian is my enemy.  You are with him.  That means....you too are an enemy."
    r "She's throwing more fire at us!"
    menu:
        n "(What will you do?)"
        "Nothing.":
            show bg orange
            with dissolve
            n "BOOM"
            r "RAARGH!"
            t "AAAHH!"
            show bg black
            with fade
            t "No...we failed..."
            show bg islands
            with fade
            jump fireAttack
        "Dodge left":
            show bg orange
            with dissolve
            n "BOOM"
            show bg islands
            with dissolve
            t "Look!  There's a cave there!"
            r "Right!"
            show bg orange
            with dissolve
            n "BOOM"
            hide bg islands
            hide bg orange
            jump cave
label cave:
    stop music fadeout 3.0
    show bg cave
    show taylor irritated flip at left
    show rhyme sad at right
    with fade
    t "Rhyme, tell me about the relationship between you and Elise."
    r "Well...."
    r "She and I met about a year ago.  We were best buddies and partners."
    r "We traveled all over the area, looking for treasures."
    r "Eventually, she suggested that we look for the magic that keeps the Floating Islands afloat."
    r "I agreed, and we found the source of the magic:"
    r "The Key of the Mind."
    r "I wanted to give the key to the Keeper for safeguarding and she agreed....at first."
    t "At first?"
    r "Yes.  She then discovered the powers of the key."
    r "She wanted to use its power to change all the parts of the world she felt were bad."
    r "I told her we shouldn't play with magic we don't understand, but she refused."
    r "...Elise told me that she wished we weren't friends, and then she started attacking me."
    r "That's why I got hurt.  It wasn't me trying to prove how cool I was."
    r "My friend wanted to hurt me."
    t "Why didn't you fight back?"
    r "I didn't want to hurt a friend.  I still don't.  That's why I refuse to fight back."
    hide taylor irritated flip
    show taylor think flip at left
    t "Hmmm, I actually have an idea....."
    hide rhyme sad
    show rhyme happy at right
    r "What is it?"
    t "Well....."
    hide taylor think flip
    hide rhyme happy
    show bg forest
    show rhyme excited at right
    with fade
    r "Oh, Eliiiiseeee!!!!!  Elise, Elise, ELise, Elise, El-"
    show elise angry flip at left
    with dissolve
    e2 "WHAT?"
    hide rhyme excited
    with dissolve
    r "Tag!!!  You're it!!!!!"
    play music "<loop 2.849>music/elise.ogg"
    e2 "You....you....you.....!!!"
    e2 "This is no time for games!!"
    hide elise angry flip
    with dissolve
    show rhyme happy at right
    with dissolve
    r "Oh yeah?  Then why are you playing?"
    hide rhyme happy
    with dissolve
    show elise angry flip at left
    with dissolve
    e2 "Because I have to catch you!"
    hide elise angry flip
    with dissolve
    show rhyme happy at right
    with dissolve
    r "Isn't that the point of the game?"
    hide rhyme happy
    with dissolve
    show elise angry flip at left
    with dissolve
    e2 "Aargh!"
    hide elise angry flip
    with dissolve
    show rhyme happy at right
    with dissolve
    r "Ha ha!"
    hide rhyme happy
    with dissolve
    show elise angry flip at left
    with dissolve
    e2 "Hmph!"
    hide elise angry flip
    with dissolve
    show rhyme happy at right
    with dissolve
    r "Wooo!"
    hide rhyme happy
    with dissolve
    show elise happy flip at left
    with dissolve
    e2 "Heh!"
    hide elise happy flip
    with dissolve
    show rhyme happy at right
    with dissolve
    r "Yippee-"
    show elise happy flip at left
    with dissolve
    e2 "Gotcha!"
    stop music fadeout 2.0
    e2 "(Panting)"
    r "(Panting)"
    r "That...was...so...much...fun."
    e2 "I...agree."
    e2 "...Rhyme?"
    r "Yes?"
    e2 "I'm...so sorry for what I did to you."
    r "That's all right.  I've been worried about you this whole time."
    e2 "Can we... be friends again?"
    r "Are you kidding me?"
    hide rhyme happy
    show rhyme excited at right
    play music "<loop 2.373>music/rhyme theme.ogg"
    r "Of course I want to be friends with you!"
    e2 "Tch... (always quick to forgive)..."
    hide rhyme excited
    show rhyme happy at right
    e2 "Oh! Before I forget, you should take the key, Rhyme."
    r "Really?"
    e2 "Yes.  You should give it to the Keeper for safeguarding."
    e2 "After all, isn't that what you wanted to do with it?"
    r "Elise, I will make sure that this key makes it to the Keeper."
    e2 "Okay... I will see you afterwards."
    hide elise happy flip
    with dissolve
    show taylor neutral hat flip at left
    with dissolve
    t "I see you got the key."
    r "Yup! And Elise and I are friends again!"
    r "So... Let's head out!"
    hide taylor neutral hat flip
    hide rhyme happy
    show bg flight
    with fade
    $ south1 = True
    jump flight

label chapter3:
    r "We have all the keys!  Where to next?"
    t "Let's stop for a moment to figure out where we need to go next."
    r "Okay!"
    stop music fadeout 3.0
    show bg chapter3
    with fade
    show bg lake
    show rhyme happy at right
    show taylor neutral hat flip at left
    r "So, what's the plan?"
    t "Take a look at these keys."
    play music "<loop 32.869>music/taylor theme e.ogg" fadein 3.0
    hide taylor neutral hat flip
    hide rhyme happy
    show bg keys
    with dissolve
    r "The metal work makes sense for each key, but the glass in the center is strange."

label keys:
    t "The keys must combine somehow..."
    menu:

        r "How do you think we should do that?"

        "Fuse them together magically.":
            t "The keys aren't reacting to each other's presence."
            jump keys

        "Make a key pinwheel by lining up the glass circles":
            t "I fail to see how this helps us."
            jump keys

        "Stack the keys on top of each other by lining up the shafts and the glass":
            t "Hmmm..."
            jump glasses
label glasses:
    show bg chaos
    with dissolve
    t "(An image was hidden in the glass.)"
    r "Hmmmm..."
    t "(This must be what Pandora's Box looks like.)"
    r "This looks familiar...."
    t "(I wonder if the keys were separated to conceal the box.)"
    r "......"
    stop music fadeout 5.0
    r ".....?"
    r "Hmmmm?!"
    r "OH!!"
    show taylor neutral hat flip at left
    show rhyme happy at right
    with dissolve
    t "What is it, Rhyme?!"
    r "I know where it is....."
    t "Where what is?"
    r "Pandora's Box."
    t "You do?!"
    r "Mmmm."
    play music "<loop 2.373>music/rhyme theme.ogg"
    r "I remember a feline beast gave it to me when I was little.  He didn't tell me what it was though."
    r "He only said it was a pretty box that can't be opened."
    r "It was really shiny and pretty, so I kept it in my lair with my other treasures."
    r "Looking back on it, I think the beast was your grandpa.  He looked very similar to you."
    hide taylor neutral hat flip
    show taylor irritated flip at left
    stop music
    t "......GRANDPA!!!"
    t "Why must you do this to me???!!!"
    r "Hahahaha!!"
    t "Grrr....."
    t "Rhyme, lead the way."
    r "Hahaha......got it."
    play music "<loop 2.373>music/rhyme theme.ogg"
    hide taylor irritated flip
    hide rhyme happy
    show bg flight
    with fade
    t "Rhyme, what do you remember from when Grandpa gave you the box?"
    r "Not a lot.  I was somewhere dark the whole time."
    r "What story did your grandpa tell you?"
    t "Humans were trying to catch him, so the box was the bait for a trap."
    t "Grandpa couldn't resist, so he went anyway."
    t "The box was on the fifth floor of a building."
    t "As soon as he swiped the box, he heard footsteps approaching him quickly."
    t "He spotted a window, and he scrambled down the side of the building."
    t "He looked back to see the bewildered humans staring at him from the open window..."
    t "So he laughed at them!"
    t "As it turned out, the humans never knew that the thief they were chasing was a feline beast."
    r "Hahahaha!"
    r "Anyway, we're almost at my cave."
    r "Get ready to land!"
    show bg lair
    show taylor neutral hat flip at left
    show rhyme happy at right
    with fade
    t "So much treasure..."
    hide taylor neutral hat flip
    show taylor cat hat flip at left
    r "Impressive, right?!"
    t "Yeah....."
    r "Well, anyway, let's find the box!"
    stop music
    n "Rustle"
    hide taylor cat hat flip
    hide rhyme happy
    show taylor irritated flip at left
    show rhyme sad at right
    t "Hmmm?"
    r "There are intruders!! How dare they enter my lair without my permission!!"
    hide taylor irritated
    show taylor neutral hat flip at left
    with None
    hide rhyme sad
    with dissolve
    r "Go on, shoo! Shoo!"
    r "Don't make me use my fire!"
    r "Yes, yes, run off, and don't ever come here again!"
    show rhyme happy at right
    play music "<loop 2.373>music/rhyme theme.ogg"
    r "Okay, now that they're gone, what are we doing again?"
    t "We're looking for Pandora's box."
    r "Oh, right! One moment."
    hide rhyme happy
    with dissolve

label treasure:
    t "(I wonder how long it will really take...)"
    hide taylor neutral hat flip
    with fade
    n "A few minutes later...."
    r "Found it?"
    t "No. You?"
    r "Nope."
    show bg lair
    with fade
    n "A few hours later...."
    stop music
    r "Found it!"
    t "Finally!!"
    show bg box
    with dissolve
    t "So this is it..."
    show taylor neutral hat flip at left
    show rhyme happy at right
    with dissolve
    t "..."
    r "What?"
    t "You won't get angry if I take away some of your treasure without your permision, right?"
    r "Well, that's only IF you take it without my permission."
    t "(In other words, never take Rhyme's treasure without permission.)"
    hide rhyme happy
    show rhyme sad at right
    with None
    show bg lair
    with dissolve
    r "......."
    r "Now that you have the box, what are you going to do?"
    play music "<loop 32.869>music/taylor theme e.ogg" fadein 2.0
    t "The Keeper, Theodore, asked me to recover the box and its keys."
    t "Now that I have them all, I should wait for him at Gale."
    t "It's where he wanted to meet me when we first talked, so odds are I'll see him there eventually."
    r "Okay. I'll take you there, but after that..."
    t "It's goodbye."
    r "Yeah..."
    r "I'll miss traveling with you."
    t "Me too."
    stop music fadeout 3.0
    hide taylor neutral hat flip
    hide rhyme sad
    show bg black
    with fade
    r "Bye!"
    r "And make sure you come and visit!"
    play music "<loop 32.869>music/taylor theme e.ogg" fadein 2.0
    show bg credits characters
    with fade
    pause
    show bg bcredits
    with fade
    pause
    show bg mcredits
    with fade
    pause
    show bg credits write
    with fade
    pause
    show bg credits edit
    with fade
    pause
    show bg credits thanks
    with fade
    pause
    show bg credits rpy
    with fade
    pause
    stop music fadeout 3.0
    jump extraCredits

label extraCredits:
    play music "<loop 32.406>music/taylor theme grand.ogg"
    show bg prologue
    with fade
    t "Here is Pandora's box."
    b "Thank you."
    t "I suggest keeping the keys separated."
    b "I suppose that would be wise."
    b "Their power combined nearly destroyed the world once."
    t "By the way..."
    t "I've seen what a single powerful artifact can do in the wrong hands."
    t "The Keeper has access to every artifact that previous Keepers recovered."
    t "That makes you the most powerful, and perhaps the most dangerous creature in the world."
    stop music fadeout 1.0
    t "So I must ask: What stops you from using the power that you have?"
    show bg end 1
    b "........"
    play music "<loop 16.977>music/theodore theme.ogg"
    b "You're not the only one who has seen the destruction magic can bring."
    b "After all, my mentor wasn't the only person I lost to magic......"
    show bg end 2
    b "And magic can bring neither of them back to life."
    t "I must ask another question."
    t "The apprentice who will succeed you: What will stop that apprentice from using that power?"
    show bg end 4
    b "If I do my job right, then the answer is simple."
    b "The apprentice will hate to betray my trust."
    t "........"
    t "Your mentor taught you well.  You already sound like a Keeper."
    b "You really think so?"
    t "Of course!"
    b "........."
    show bg end 3
    b "Thank you, [taylor_name]......"
    b "For everything."
    stop music fadeout 3.0
    show bg black
    n "The End"
    with fade


    # This ends the game.

    return
