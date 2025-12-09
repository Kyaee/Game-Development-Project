# ============================================================================
# SERA - Character Definition Sheet
# ============================================================================
# This file contains all character definitions, images, and transforms
# for the Sera character.
# ============================================================================

# ----------------------------------------------------------------------------
# CHARACTER DEFINITION
# ----------------------------------------------------------------------------
# Define the character with name, color, and text styling

define sera = Character(
    "Sera",
    # Name tag color (shown above dialogue)
    who_color="#89c6ff",
    # Dialogue text color (optional)
    # what_color="#ffffff",
    # Voice tag for auto voice (optional)
    # voice_tag="sera",
    # Image tag for automatic side images (links to image definitions below)
    image="sera",
)

# Alternative short alias for convenience in scripts
define s = sera

# Define ??? as an alias for Sera, but with a different name
define q = Character("{i}Short Haired Girl{/i}", who_color="#f1e2ff", image="sera")


# ----------------------------------------------------------------------------
# IMAGE DEFINITIONS - Basic Sprites
# ----------------------------------------------------------------------------
# Define character sprites and expressions
# Place image files in: game/assets/character_sheets/sera_model/
#
# Naming convention: sera_[outfit]_[expression].png
# Example files:
#   - sera_default_neutral.png
#   - sera_default_happy.png
#   - sera_default_sad.png
#   - sera_default_angry.png
#   - sera_default_surprised.png

# Base/Neutral expressions
# Image files are 1578x2110 pixels, scaled down to fit screen (targeting ~1080 height)
# Available expressions: neutral, happy, sad, angry

image sera neutral:
    "assets/character_sheets/sera_model/sera-neutral.png"
    zoom 0.5 yalign 0.5

image sera happy:
    "assets/character_sheets/sera_model/sera-happy.png"
    zoom 0.5

image sera sad:
    "assets/character_sheets/sera_model/sera-sad.png"
    zoom 0.5

image sera angry:
    "assets/character_sheets/sera_model/sera-angry.png"
    zoom 0.5

image sera close_eyes:
    "assets/character_sheets/sera_model/sera-close-eyes.png"
    zoom 0.5

image sera depressed:
    "assets/character_sheets/sera_model/sera-depressed.png"
    zoom 0.5

# ----------------------------------------------------------------------------
# LAYERED IMAGE DEFINITION (Advanced - for composite sprites)
# ----------------------------------------------------------------------------
# Use this if you have separate layers for base, outfit, expression, etc.
# Uncomment and customize as needed.

# layeredimage sera:
#     # Always shown - the base body
#     always:
#         "assets/character_sheets/sera_model/base.png"
#
#     # Outfit group - only one shown at a time
#     group outfit:
#         attribute default default:
#             "assets/character_sheets/sera_model/outfit_default.png"
#         attribute formal:
#             "assets/character_sheets/sera_model/outfit_formal.png"
#         attribute casual:
#             "assets/character_sheets/sera_model/outfit_casual.png"
#
#     # Expression group - only one shown at a time
#     group expression:
#         attribute neutral default:
#             "assets/character_sheets/sera_model/expression_neutral.png"
#         attribute happy:
#             "assets/character_sheets/sera_model/expression_happy.png"
#         attribute sad:
#             "assets/character_sheets/sera_model/expression_sad.png"
#         attribute angry:
#             "assets/character_sheets/sera_model/expression_angry.png"
#         attribute surprised:
#             "assets/character_sheets/sera_model/expression_surprised.png"
#
#     # Optional accessories (can be shown/hidden independently)
#     group accessories:
#         attribute none default:
#             Null()
#         attribute hairpin:
#             "assets/character_sheets/sera_model/accessory_hairpin.png"


# ----------------------------------------------------------------------------
# SIDE IMAGE (for dialogue box portraits)
# ----------------------------------------------------------------------------
# Small portrait shown next to dialogue text
# Place file at: game/assets/character_sheets/sera_model/side/

# Commented out until actual side images are added:
# image side sera neutral = "assets/character_sheets/sera_model/side/sera_neutral.png"
# image side sera happy = "assets/character_sheets/sera_model/side/sera_happy.png"
# image side sera sad = "assets/character_sheets/sera_model/side/sera_sad.png"


# ----------------------------------------------------------------------------
# TRANSFORMS - Positioning & Animation
# ----------------------------------------------------------------------------
# Custom transforms for this character's positioning and animations

transform sera_entrance:
    # Start off-screen to the right
    xalign 1.0
    alpha 0.0
    # Slide in and fade in
    ease 0.5 xalign 0.75 alpha 1.0

transform sera_exit:
    # Current position
    xalign 0.75
    alpha 1.0
    # Slide out and fade out
    ease 0.5 xalign 1.0 alpha 0.0

transform sera_shake:
    # Quick shake animation for emphasis
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 xoffset 0

transform sera_bounce:
    # Bouncy entrance
    yoffset -20
    ease 0.2 yoffset 0
    ease 0.1 yoffset -10
    ease 0.1 yoffset 0


# ----------------------------------------------------------------------------
# CHARACTER VARIABLES (for tracking character state)
# ----------------------------------------------------------------------------
# Use these to track relationship, mood, or story flags

default sera_affection = 0
default sera_trust = 0
default sera_met = False
default sera_route_unlocked = False


# ----------------------------------------------------------------------------
# CHARACTER-SPECIFIC LABELS (optional scenes/events)
# ----------------------------------------------------------------------------
# Reusable dialogue or event labels specific to this character

label sera_introduction:
    # Character introduction scene
    show sera neutral at center with dissolve
    sera "Oh, hi there!"
    sera "I'm Sera. Nice to meet you!"
    return

label sera_greeting:
    # Generic greeting based on relationship
    if sera_affection >= 50:
        show sera happy
        sera "Hey! I was hoping I'd see you today!"
    elif sera_met:
        show sera neutral
        sera "Oh, hey again!"
    else:
        $ sera_met = True
        show sera happy
        sera "Hi! I don't think we've met before. I'm Sera!"
    return


# ----------------------------------------------------------------------------
# AUDIO DEFINITIONS (character-specific sounds)
# ----------------------------------------------------------------------------
# Voice clips or character-specific sound effects
# Place audio files in: game/assets/sounds/sfx/

# define audio.sera_laugh = "assets/sounds/sfx/sera_laugh.ogg"
# define audio.sera_giggle = "assets/sounds/sfx/sera_giggle.ogg"
