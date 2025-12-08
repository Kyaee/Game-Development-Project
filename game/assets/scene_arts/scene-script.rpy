# ============================================================================
# SCENE ARTS - CG/Event Image Definitions
# ============================================================================
# This file contains all scene art (CG) definitions for special event images.
# Place image files in: game/assets/scene_arts/
#
# Image dimensions: 1920 x 1080 (full screen)
# ============================================================================

# ----------------------------------------------------------------------------
# SCENE ART DEFINITIONS
# ----------------------------------------------------------------------------
# Define your scene art/CG images here
# Naming convention: cg_[scene_name] or scene_[description]

# Example scene art (rename "image.png" to something descriptive)
image cg_example = "assets/scene_arts/image.png"

# Placeholder definitions for future scene arts
# Uncomment and update the path when you add the actual images:

# image cg_farewell = "assets/scene_arts/cg_farewell.png"
# image cg_pocket_watch = "assets/scene_arts/cg_pocket_watch.png"
# image cg_time_restoration = "assets/scene_arts/cg_time_restoration.png"
# image cg_memory_fragments = "assets/scene_arts/cg_memory_fragments.png"
# image cg_sera_memories = "assets/scene_arts/cg_sera_memories.png"

# ----------------------------------------------------------------------------
# SCENE ART WITH EFFECTS
# ----------------------------------------------------------------------------
# Scene arts with built-in transforms or effects

# Example: Scene art that slowly zooms in
image cg_dramatic_zoom:
    "assets/scene_arts/image.png"
    zoom 1.0
    linear 10.0 zoom 1.1

# Example: Scene art with a slight pan
image cg_pan_scene:
    "assets/scene_arts/image.png"
    xalign 0.0
    linear 5.0 xalign 1.0

# ----------------------------------------------------------------------------
# TRANSFORMS FOR SCENE ARTS
# ----------------------------------------------------------------------------
# Custom transforms specifically for CG/scene art presentation

# Flash in - dramatic reveal
transform cg_flash_in:
    alpha 0.0
    linear 0.1 alpha 1.0

# Slow fade in for emotional scenes
transform cg_slow_fade:
    alpha 0.0
    linear 2.0 alpha 1.0

# Ken Burns effect - slow zoom
transform cg_ken_burns:
    zoom 1.0
    linear 15.0 zoom 1.15

# Shake effect for impact moments
transform cg_shake:
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 0


# ----------------------------------------------------------------------------
# TRANSITIONS FOR SCENE ARTS
# ----------------------------------------------------------------------------
# Special transitions for showing/hiding scene arts

define flash_white = Fade(0.4, 0.5, 1.0, color="#FFFFFF")
#                         ↑    ↑    ↑
#                         │    │    └── fade IN duration
#                         │    └─────── hold duration (at solid color)
#                         └──────────── fade OUT duration
define flash_black = Fade(0.1, 0.3, 0.3, color="#000000")
define cg_dissolve = Dissolve(1.5)
define cg_fade = Fade(0.5, 0.5, 0.5)


# ----------------------------------------------------------------------------
# USAGE EXAMPLES (in script.rpy)
# ----------------------------------------------------------------------------
# 
# # Show a scene art with dissolve
# scene cg_farewell with cg_dissolve
#
# # Show scene art with flash
# scene cg_pocket_watch with flash_white
#
# # Show scene art with slow fade and ken burns effect
# scene cg_memory_fragments at cg_ken_burns with cg_slow_fade
#
# # Return to normal scene after CG
# scene rift_time_bg with dissolve
# show sera neutral
# ----------------------------------------------------------------------------
