# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Define custom dissolve transitions
define slow_dissolve = Dissolve(1.5)
define quick_dissolve = Dissolve(0.5)
    
# Vulnerability menu tracking variables
default chose_given_up = False
default chose_too_much = False
default chose_scared = False

# The game starts here.

label start:

    scene black
    with fade

    play music bgm_ancient_memories fadein 1.0

    # Centered dramatic opening - no textbox, text appears in center
    show text "{color=#FFF}{size=40}Time is a cruel concept wouldn't you agree?{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve
    
    show text "{color=#FFF}{size=40}So many humans would give up anything just for more time{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve
    
    show text "{color=#FFF}{size=40}After all{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve
    
    show text "{color=#FFF}{size=40}Time's endless march creates many regrets{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve
    
    show text "{color=#FFF}{size=40}...{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve
    
    show text "{color=#FFF}{size=40}Perhaps we started off on the wrong foot when we first met.{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve
    
    show text "{color=#FFF}{size=40}Perhaps I'll try a different approach.{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve

    # Scene Description: A girl awakens in the fragmented memory space Cycle No. Unknown... (FADE IN)
    # Assuming a background for the fragmented memory space is available, e.g., 'bg fragmented_space'
    # scene bg fragmented_space with fadeIn

    show sera close_eyes:
        xalign 0 yalign 0.5
    with dissolve
    "The girl on the floor stares at Time itself with a blank expression..."

    show sera neutral:
        xalign 0 yalign 0.5
    "She has been here before..." 
    "More times than she could remember..."
    t "So we meet again..."

    show curator glitching:
        xalign 1.0 yalign 0.5 xzoom -1.0
    with slow_dissolve
    t "Don't look at me like that."
    t "By now, you of all people should already know the consequences of your actions"
    q "..."
    t "Silent treatment, again?"
    t "{i}s i g h . . . {/i}"
    t "Don't worry, we have all the time in the world here..."

    #####################################################################################
    # Scene Description: The Rift of Time - A void where time stands still (FADE IN)
    #####################################################################################

    scene rift_time_bg with flash_white
    show sera sad:
        xalign 0 yalign 0.5
    show curator neutral:
        xalign 1.0 yalign 0.5 xzoom -1.0
    with dissolve

    "A short haired girl stands up and turns her back on time."

    t "You know it's futile to change events."
    t "It's not like I'm the one that's stopping you from your \"happy ending\"."
    t "After all, I'm just a \"curator\" who records the history of the world."
    c "And you..."

    # CHANGE THE CHARACTER SPRITE
    show curator neutral:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "You are tampering with the natural flow and course of time in the num-"

    #####################################################################################
    # Scene Art Play 1: The Rift of Time - A void where time stands still (Flash)
    #####################################################################################

    stop music fadeout 1.0 
    play music bgm_quiet_sea fadein 3.5

    scene scene1 with flash_white

    hide sera 
    hide curator

    q "Numerous times I've tried to save my friends!"
    c "Then..."
    c "Why won't you let the world move forward?"
    q "..."
    q "I-"
    q "I just need to save them."

    scene rift_time_bg 

    show sera neutral:
        xalign 0 yalign 0.5
    show curator neutral:
        xalign 1.0 yalign 0.5 xzoom -1.0
    with slow_dissolve
    c "I see..."

    show sera sad:
        xalign 0 yalign 0.5
    show curator sad:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "Before you attempt to break reality again, I implore you to walk with me."

    menu:
        "Walk with her":
            jump walk_with_her
        "Leave":
            jump leave


label walk_with_her:

    show curator happy:
        xalign 1.0 yalign 0.5 xzoom -1.0
    "This choice seems to make the woman happy. As if waiting for this moment, the curator takes the chance to explain something she's been wanting to tell for a long time."

    c "This place is more than just a void."
    show curator smile:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "This is the river of time where I keep all of which has transpired."

    show sera neutral:
        xalign 0 yalign 0.5
    show curator neutral:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "Your endless cycles created an endpoint in the river which is not supposed to exist."
    c "After all, this is supposed to be an infinite void."
    c "I remember your computer nerd friend had a similar term for this."

    show curator sad:
        xalign 1.0 yalign 0.5 xzoom -1.0
    "The Curator directs her gaze downward as if she was deep in thought."

    c "What the world just experienced was a memory overflow."

    #####################################################################################
    # Scene Art Play 2: The Rift of Time - A void where time stands still (Flash)
    #####################################################################################

    scene scene3 with flash_white
    "The Curator dramatically unveils the vast fragments of memories and worlds coalesced into one spot as if an invisible wall is preventing the world from moving forward. Sera stands shocked at the vast accumulation of crystals before her. This was her many attempts in giving her friends a true ending."
        
    show sera neutral:
        xalign 0 yalign 0.5
    show curator neutral:
        xalign 1.0 yalign 0.5 xzoom -1.0
    with dissolve
    c "Since you won't let the world move forward, it just collapsed on itself."
    c "If you go back to the beginning of the week, who knows how much faster the world will break."
    c "After all, most of the shards here belong to you, the worlds you made, and your memories, Sera."
    s "Then what do you suggest, I do"

    show curator happy:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "NO WAY! YOU'RE ACTUALLY COOPERATING!?"

    show curator neutral:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "{i}Ahem {/i}"
    "The curator clears her throat and straightens her dress to appear more dignified."

    scene rift_time_bg with flash_white

    show sera neutral:
        xalign 0 yalign 0.5
    show curator smile:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "I'll be honest, you REALLY need to return my pocket watch or whatever that old geezer turned my authority into."

    show sera angry: 
        xalign 0.0 yalign 0.5
    s "But what about my friends?"

    show curator neutral:
        xalign 1.0 yalign 0.5 xzoom -1.0
    s "Without the things I did, they'd be forced to walk paths they never wanted to tread."
    s "I won't allow their dreams to fade away like it's nothing."
    s "I can't think of living in a world where we can't be all together again."
    s "I can't just go back knowing I could have done something for them."

    show curator sad:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "Sera, this entire conundrum we are in is the result of your own memories!"
    c "There won't be any friends or a world to return to if you remember everything..."

    show curator angry:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "You repeated the same week for who knows how long to the point your very memories have clogged the flow of time!"

    scene scene2 with quick_dissolve
    hide curator
    hide sera

    s "And then what!? I go back to the beginning without a single memory of any loop?"
    s "I can't bear to witness my friend disappear like that!"

    "Time observes the girl lost in her own conundrum with little to no regard of the perilous fate she placed reality in."

    c "Honestly, if that {b}{i}local deity{/i}{/b} of yours never played with my realm's authority we wouldn't be here in the first place."
    c "I've observed you for across so many cycles Sera. I never could quite understand why you people act the way you do."

    scene rift_time_bg 

    show sera neutral:
        xalign 0 yalign 0.5
    show curator neutral:
        xalign 1.0 yalign 0.5 xzoom -1.0
    with quick_dissolve
    c "Tell me..."

    # The Curator's Interrogation
    label curator_interrogation:
        menu:
            "Do you know who you are?":
                jump who_are_you
            "Are you truly special?":
                jump are_you_special

label who_are_you:
    show sera happy: 
        xalign 0.0 yalign 0.5 
    s "Who I am?"

    show curator smile:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "You heard that right."

    show sera neutral: 
        xalign 0.0 yalign 0.5 
    s "Who I am?"
    s "Of course I do."

    show curator happy:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "Mhmm. You say that and yet from my observations you are a confusing one."
    c "During your times away from this void, I've observed some of your history."

    show curator smile:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "You humbly brag in front of others to put up a confident front- hoping to appear mightier than the rest."
    
    show curator sad:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "People may not notice it, but you like to push others away through excuses of being busy and all, just to be alone with yourself."

    show curator smile:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "Despite this, you even go out of your way to help others- be it at your own detriment."
    c "I never considered you the sociable type despite the way you present yourself to others."

    show curator happy:
        xalign 1.0 yalign 0.5 xzoom -1.0
        
    c "You withdraw from yourself from situations you find difficult."
    show curator smile:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "You crave praise from other people yet not those close to you."
    c "Sometimes I truly wonder If you even live for yourself and what you want."

    show curator happy:
        xalign 1.0 yalign 0.5 xzoom -1.0
    s "Then I think my answer is, no."
    jump after_interrogation_dialogue

label are_you_special:
    show curator happy:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "\"Woe is life\" isn't that right, Sera?"

    show sera sad:
        xalign 0.0 yalign 0.5
    s "What do you want?"

    show curator smile:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "Sorry, sorry, I'm merely trying to break the ice between us"

    show curator happy:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "I just want to say that you considering yourself as unique is a misconception."

    show sera neutral:
        xalign 0.0 yalign 0.5
    c "You're delusional to think you are grandiose or special. These fantastical reveries you have in your mind are devastating to your future."

    show curator neutral:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "It hurts when what you imagine life could be doesn't match up with reality, right?"
    s "..."
    c "You think your experiences, failures, and inadequacies are solely unique to you?"

    show curator happy:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "You do everything by yourself because you believe no one can understand or relate to you. You refuse help just to preserve your golden image."

    show curator neutral:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "Look at you now."

    show sera happy:
        xalign 0.0 yalign 0.5
    s "Of all the people to say that to me, I think you're the least qualified to lecture me on this."
    show curator happy:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "Hmm. Maybe."
    c "But, as an observer, I say that you can keep dreaming about being a hero in a grand adventure, or a protagonist of some story."

    show curator smile:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "However, if you don't take a step forward. Those will only remain fantasies forever."
    s "Well, too late for me now I guess."
    jump after_interrogation_dialogue

label after_interrogation_dialogue:
    show curator happy:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "I don't want to stop you, Sera."
    c "There must be more as to why your local deity made such a drastic decision.  A mortal, with my power? Preposterous!"
    s "I know, I know. Just let me think for a second."

    stop music fadeout 1.0
    play music bgm_echoes_lost fadein 1.0

    show curator angry:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "WE don't have seconds, Everything is collapsing and I am on my wit's end."
    c "I don't meddle with mortal affairs because it is safer that way."
    c "But right now, if we want to have a tomorrow, then I need that object in your hands."

    show sera neutral:
        xalign 0.0 yalign 0.5
    c "Can you at least tell me why you desperately want to change things."

    s "..."
    show curator neutral:
        xalign 1.0 yalign 0.5 xzoom -1.0
    s "This is the only thing I can cling towards."

    # Reset tracking variables for vulnerability choices
    $ chose_given_up = False
    $ chose_too_much = False
    $ chose_scared = False

label vulnerability_menu:
    menu:
        "I've already given up." if not chose_given_up:
            $ chose_given_up = True
            jump given_up
        "It's too much." if not chose_too_much:
            $ chose_too_much = True
            jump too_much
        "I'm scared." if not chose_scared:
            $ chose_scared = True
            jump scared

label given_up:
    show sera sad:
        xalign 0 yalign 0.5
    s "My life is utterly worthless."
    s "I don't exactly see any point in continuing forward."
    s "So, it's as you've said, I've just been waiting in my room, waiting for the days to go by."

    show sera depressed:
        xalign 0 yalign 0.5
    s "In the grand scheme of things, I don't really matter much."
    s "After all, in this world, there's a million others just like me doing the same thing."
    s "In fact, we do the same thing and yet they are still better than me in every single way no matter how much work I put into my work."
    s "I'm not special."
    
    # Check if all options have been selected
    if chose_given_up and chose_too_much and chose_scared:
        jump after_vulnerability_dialogue
    else:
        jump vulnerability_menu

label too_much:
    show sera happy:
        xalign 0.0 yalign 0.5
    s "You know..."
    s "I once excelled in a lot of things."
    s "I once believed I was the best in everything."
    s "Somewhere down the line, everyone started relying on me."
    s "Everyone kept telling me how great I was."

    show sera sad:
        xalign 0.0 yalign 0.5
    s "I don't want to disappoint those people."
    s "I started doing things not because I wanted to, but because it was expected of me."
    s "If I can't match those expectations, then doesn't that mean my abilities are lacking."
    s "When everyone went their separate ways so many things nagged me."

    show sera depressed:
        xalign 0.0 yalign 0.5
    s "\"Why am I not good enough\""
    s "\"Why can't you do something this simple\""
    s "I'm not worthy of anyone's praise."
    
    # Check if all options have been selected
    if chose_given_up and chose_too_much and chose_scared:
        jump after_vulnerability_dialogue
    else:
        jump vulnerability_menu

label scared:
    show sera sad:
        xalign 0.0 yalign 0.5
    s "I fear that I'll never measure up to my old self."
    show sera happy:
        xalign 0.0 yalign 0.5
    s "I keep looking back at my old works and find it \"better\" than the professional stuff I make these days."
    show sera sad:
        xalign 0.0 yalign 0.5
    s "Sometimes I feel like it was a mistake to fall in love with art"
    s "Everytime I finish a piece, I'd be stuck wondering for a while if I can even make something new."
    s "I see all these other people in different spaces enjoying their craft."
    show sera happy: 
        xalign 0 yalign 0.5
    s "Yet, here I am." 
    s "Indifferent." 
    s "Mediocre."
    s "Perhaps it would've been much safer to choose a \"normal\" job than what I'm doing right now."

    show sera sad:
        xalign 0.0 yalign 0.5
    s "I'm so far behind compared to my friends." 
    s "I don't know what to do other than keep doing what I'm already doing."
    s "It's so painful to create sometimes." 
    s "I feel so disconnected to my original goal."
    s "At times, I just find myself lost in making new things."
    
    show sera depressed:
        xalign 0 yalign 0.5
    s "But, I'm afraid I'll one day run out of ideas."
    s "Maybe even stop and be forgotten entirely."
    
    # Check if all options have been selected
    if chose_given_up and chose_too_much and chose_scared:
        jump after_vulnerability_dialogue
    else:
        jump vulnerability_menu

label after_vulnerability_dialogue:

    show curator happy:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "But, it feels wonderful to create a masterpiece. Wouldn't you agree?"
    s "Yeah... It's a feeling that will never go away."

    s "If I am given the option to do everything over and over again. I would keep choosing to be an artist."
    s "Art makes me feel alive."

    show curator neutral:
        xalign 1.0 yalign 0.5 xzoom -1.0
    "The curator fixes their gaze upon Sera that's lost in her own thoughts."

    show curator sad:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "Your sense of self is warped, Sera."
    c "But, if you yourself believe you don't deserve anything..."
    c "Then how can you expect others to help you?"
    
    show curator sad:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "You keep wanting people to validate the idea of you being meaningless."
    show curator neutral:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "Sera, the truth is- people care."
    c "You never showed any reason for them not to want you."
    c "You think so little of yourself and thought nobody cared about you."

    show curator sad:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "However in those many cycles you experienced, you failed to pick up on anything at all."

    show curator neutral:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "I know that giving up doesn't seem so bad when it feels like the entire world is against you."    
    c "Thinking that nobody could possibly understand what you're going through is cruelty onto yourself."

    show curator sad:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "You are only suffocating yourself by isolating yourself."
    c "Sera, you can't avoid people or activities just because you don't want to disappoint them."
    c "There's no shame in being helped by others, it will never ever be a weakness."
    c "You don't have to carry everything by yourself, it's fine to open up."
    c "There are just problems that are too big to handle for one person."
    c "Throughout the course of time, I've seen many like you."
    c "Don't ever think no one cares about you."

    "The curator tried to offer words of encouragement to Sera but they had one specifically important thing to say."

    show curator neutral:
        xalign 1.0 yalign 0.5 xzoom -1.0
    c "You keep trying to create the perfect ending for your group, but did you ever include yourself?"
    c "If you ever find yourself lost, those people are more than willing to share the pain that you carry."

    "Those words caught Sera off guard. Consequently, a thought struck Sera."


    s "Hey-"
    s "I'm willing to do anything to get together with my friends again..."
    s "If I get the chance, I won't run away from anything."
    s "I- If- I give this back, you can fix everything right?"
    c "!"
    c "Of course."
    c "However, you know I'll be deleting everything, right?"
    c "Your memories- your experiences- your decisions... everything you ever did in those cycles."
    s "I know... but why do you sound so hesitant? Weren't you always forcing me to return your power when we first met each other? Isn't this what you always wanted?"
    c "I'm taking a different approach this time, for your information."
    c "Clearly this method produced me desirable results."

    "Sera clutches a pocket watch in her hands. She seemed hesitant to let it go. Despite this, Sera knew this was the only option left. Time has run out. So, Sera loosens her grip of the pocket watch and extends her hand towards the curator."

    "After thorough reflection and talk with the curator, Sera decides to return their authority."

    "Time's Curator gently receives the pocket watch from Sera and it transforms the small mechanical device into a brush in their hands. The curator's lips curl into a soft smile while their eyes carry a sense of sorrow."

    c "I can't exactly empathize that much with you Sera."
    c "Outside of gods, deities, and the other governing concepts you're one of the only few humans I've interacted with."
    c "You're right that you won't remember a single thing once I restore the world."
    c "However, I'll pull a few strings here and there for you this one time only."
    s "Wait, what are you going to do?"
    c "It's nothing that     you need to be concerned with."
    c "If you're lucky, all of this would have just felt like a dream."
    c "If you remember this dream-"
    c "Would you consider making an offering to a shrine outside of your town?"
    s "I- outside of town?"
    c "Hehe. Nothing to be concerned about for now."
    c "Your experiences are like a story. That's why I'm rooting for you as a protagonist."

    # The curator fixes the fragments of memories and time in the infinite void with a wave of their brush.
    # Dramatic centered text for the final message
    
    hide sera
    hide curator
    window hide
    
    scene black with slow_dissolve
    
    show text "{color=#FFF}{size=40}From here on out, your decision or indecision will determine your future.{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve
    
    show text "{color=#FFF}{size=40}If I were to comment on anything about your story, Sera.{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve
    
    show text "{color=#FFF}{size=40}I want you to know that sometimes there's so many unnecessary things{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve
    
    show text "{color=#FFF}{size=40}that humans have in their minds stopping them from moving forward.{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve
    
    show text "{color=#FFF}{size=40}Your choices change up your tomorrow.{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve
    
    show text "{color=#FFF}{size=40}Soon your actions will play a great part in a story.{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve
    
    show text "{color=#FFF}{size=40}Don't let the past weigh you down nor let the future stop you.{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve
    
    show text "{color=#FFF}{size=40}Don't let time pass you by!{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve

    # fade to white
    scene white with fade

    # This ends the game.
    return

