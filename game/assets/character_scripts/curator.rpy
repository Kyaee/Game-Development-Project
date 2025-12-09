# ============================================================================
# CURATOR - Character Definition Sheet
# ============================================================================
# This file contains all character definitions, images, and transforms
# for the Curator character.
# ============================================================================

# ----------------------------------------------------------------------------
# CHARACTER DEFINITION
# ----------------------------------------------------------------------------
# Define the character with name, color, and text styling

define curator = Character(
    "The Curator",
    # Name tag color (shown above dialogue)
    who_color="#c8a2c8",
    # Dialogue text color (optional)
    # what_color="#ffffff",
    # Voice tag for auto voice (optional)
    # voice_tag="curator",
    # Image tag for automatic side images (links to image definitions below)
    image="curator",
)

# Alternative short alias for convenience in scripts
define c = curator
define t = Character("???", who_color="#c8a2c8", image="curator")



# ----------------------------------------------------------------------------
# IMAGE DEFINITIONS - Basic Sprites
# ----------------------------------------------------------------------------
# Define character sprites and expressions
# Place image files in: game/assets/character_sheets/curator/
#
# Naming convention: curator_[outfit]_[expression].png
# Example files:
#   - curator_default_neutral.png
#   - curator_default_happy.png
#   - curator_default_sad.png
#   - curator_default_angry.png
#   - curator_default_surprised.png

# Base/Neutral expressions
# Image files are 1578x2110 pixels, scaled down to fit screen (targeting ~1080 height)
# Available expressions: neutral, happy, sad, angry

image curator neutral:
    "assets/character_sheets/curator/curator-neutral.png"
    zoom 0.5

image curator happy:
    "assets/character_sheets/curator/curator-happy.png"
    zoom 0.5

image curator sad:
    "assets/character_sheets/curator/curator-sad.png"
    zoom 0.5

image curator angry:
    "assets/character_sheets/curator/curator-angry.png"
    zoom 0.5

image curator smile:
    "assets/character_sheets/curator/curator-smile.png"
    zoom 0.5

# Static glitch expression
image curator glitch:
    "assets/character_sheets/curator/curator-glitch.png"
    zoom 0.5

# Animated glitch effect (cycles through glitch frames)
image curator glitching:
    zoom 0.5
    "assets/character_sheets/curator/glitch/5.png"
    0.25
    "assets/character_sheets/curator/glitch/4.png"
    0.25
    "assets/character_sheets/curator/glitch/3.png"
    0.25
    repeat

# Single glitch flash effect (plays once)
image curator glitch_flash:
    zoom 0.5
    "assets/character_sheets/curator/glitch/1.png"
    0.05
    "assets/character_sheets/curator/glitch/2.png"
    0.05
    "assets/character_sheets/curator/glitch/3.png"
    0.05
    "assets/character_sheets/curator/glitch/4.png"
    0.05
    "assets/character_sheets/curator/glitch/5.png"
    0.05
    "assets/character_sheets/curator/curator-neutral.png"


# ----------------------------------------------------------------------------
# LAYERED IMAGE DEFINITION (Advanced - for composite sprites)
# ----------------------------------------------------------------------------
# Use this if you have separate layers for base, outfit, expression, etc.
# Uncomment and customize as needed.

# layeredimage curator:
#     # Always shown - the base body
#     always:
#         "assets/character_sheets/curator/base.png"
#
#     # Outfit group - only one shown at a time
#     group outfit:
#         attribute default default:
#             "assets/character_sheets/curator/outfit_default.png"
#         attribute formal:
#             "assets/character_sheets/curator/outfit_formal.png"
#         attribute casual:
#             "assets/character_sheets/curator/outfit_casual.png"
#
#     # Expression group - only one shown at a time
#     group expression:
#         attribute neutral default:
#             "assets/character_sheets/curator/expression_neutral.png"
#         attribute happy:
#             "assets/character_sheets/curator/expression_happy.png"
#         attribute sad:
#             "assets/character_sheets/curator/expression_sad.png"
#         attribute angry:
#             "assets/character_sheets/curator/expression_angry.png"
#         attribute surprised:
#             "assets/character_sheets/curator/expression_surprised.png"
#
#     # Optional accessories (can be shown/hidden independently)
#     group accessories:
#         attribute none default:
#             Null()
#         attribute glasses:
#             "assets/character_sheets/curator/accessory_glasses.png"


# ----------------------------------------------------------------------------
# SIDE IMAGE (for dialogue box portraits)
# ----------------------------------------------------------------------------
# Small portrait shown next to dialogue text
# Place file at: game/assets/character_sheets/curator/side/

# Commented out until actual side images are added:
# image side curator neutral = "assets/character_sheets/curator/side/curator_neutral.png"
# image side curator happy = "assets/character_sheets/curator/side/curator_happy.png"
# image side curator sad = "assets/character_sheets/curator/side/curator_sad.png"


# ----------------------------------------------------------------------------
# TRANSFORMS - Positioning & Animation
# ----------------------------------------------------------------------------
# Custom transforms for this character's positioning and animations

transform curator_entrance:
    # Start off-screen to the left
    xalign 0.0
    alpha 0.0
    # Slide in and fade in
    ease 0.5 xalign 0.25 alpha 1.0

transform curator_exit:
    # Current position
    xalign 0.25
    alpha 1.0
    # Slide out and fade out
    ease 0.5 xalign 0.0 alpha 0.0

transform curator_shake:
    # Quick shake animation for emphasis
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 xoffset 0

transform curator_bounce:
    # Bouncy entrance
    yoffset -20
    ease 0.2 yoffset 0
    ease 0.1 yoffset -10
    ease 0.1 yoffset 0


# ----------------------------------------------------------------------------
# CHARACTER VARIABLES (for tracking character state)
# ----------------------------------------------------------------------------
# Use these to track relationship, mood, or story flags

default curator_affection = 0
default curator_trust = 0
default curator_met = False
default curator_route_unlocked = False


# ----------------------------------------------------------------------------
# CHARACTER-SPECIFIC LABELS (optional scenes/events)
# ----------------------------------------------------------------------------
# Reusable dialogue or event labels specific to this character

label curator_introduction:
    # Character introduction scene
    show curator neutral at center with dissolve
    curator "Hello, welcome to the gallery."
    curator "I am the Curator. I oversee all the exhibits here."
    return

label curator_greeting:
    # Generic greeting based on relationship
    if curator_affection >= 50:
        show curator happy
        curator "Ah, it's wonderful to see you again!"
    elif curator_met:
        show curator neutral
        curator "Welcome back."
    else:
        $ curator_met = True
        show curator neutral
        curator "I don't believe we've met. I'm the Curator."
    return


# ----------------------------------------------------------------------------
# AUDIO DEFINITIONS (character-specific sounds)
# ----------------------------------------------------------------------------
# Voice clips or character-specific sound effects
# Place audio files in: game/assets/sounds/sfx/

# define audio.curator_laugh = "assets/sounds/sfx/curator_laugh.ogg"
# define audio.curator_hmm = "assets/sounds/sfx/curator_hmm.ogg"
