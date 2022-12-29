import game.main_menu as menu
import game.character as char
import game.achievement_display as achiev
import game.room as rm
import game.options as opt
import game.end as end

from opts import ROOMS


def main():
    """
    Main game loop
    """
    # Shows main menu
    selection = menu.display()

    # If achievements is selected
    if selection == menu.ACHIEVEMENTS:
        # Displays achievements menu and when the user leaves returns to the main menu
        achiev.display()
        return main()

    # If newgame is selected
    else:
        # Creates the character
        character = char.select()
        # If character creation is cancelled returns to main menu
        if character == None:
            return main()

        # Displays starting text (lore)
        menu.display_lore()

        # Displays inital Room & character
        char.display(character)
        rm.display(character['room'], character)

        while character['remaining'] > 0:
            opt.display(ROOMS[character['room']['id']]['special_options'], character)
        
        end.write_achivement()
            

        # TODO: Continue...


main()
