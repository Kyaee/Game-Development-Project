label leave:

    window hide 
    # Fade to black

    scene black with fade
    
    # Dramatic narrator text - centered, no textbox
    show text "{color=#FFF}{size=40}The girl leaves and pays no heed to the woman talking.{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve
    
    show text "{color=#FFF}{size=40}She pulls out a pocket watch and winds its clock.{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve
    
    # Flash white for the blinding light
    scene rift_time_bg with flash_white
    
    show text "{color=#000}{size=40}This action wraps the girl around in blinding light and vanishes from the realm.{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve
    
    # Fade back to black for the empty void
    scene black with Fade(1.0, 1.0, 1.0)
    
    show text "{color=#FFF}{size=40}In the empty void, one person remains once again.{/size}{/color}" at truecenter with slow_dissolve
    pause
    hide text with quick_dissolve
    
    # Long pause for emotional impact
    pause 1.5
    
    # Set flag to remove the "leave" option from future playthroughs
    # $ persistent.leave_chosen = True
    
    # Return to start
    scene black with Fade(1.0, 1.0, 1.0)
    pause 1.0
    
    return