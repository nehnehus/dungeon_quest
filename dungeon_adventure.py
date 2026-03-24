import random

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        # TODO: Ask the user for their name using input()
        username = input("What is your name?: ")
        # TODO: Initialize a dictionary with keys: "name", "health", and "inventory"
        user_dict = {"name":username, "health":10,"inventory":[]}
        # TODO: Return the dictionary
        return user_dict

    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        # TODO: Create a dictionary of treasure names and integer values
        treasures= {
             "Gold Coin": 10,
             "Silver Coin": 50,
             "Ruby neclace": 100,
             "Diamond Ring": 1500,
             "Green emerald": 5000,
                    }
        # TODO: Return the dictionary
        return treasures


    def display_options(room_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        # TODO: Print the room number and the 4 menu options listed above
        print(f"""
                You are in room {room_number}.
                What would you like to do?
                1. Search for treasure
                2. Move to next room
                3. Check health and inventory
                4. Quit the game
                """)

    def search_room(player, treasures):
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        outcome = random.choice(['treasure', 'trap'])
        # TODO: Write an if/else to handle treasure vs trap outcomes
        if outcome == 'treasure':
        # TODO: Update player dictionary accordingly
            new_treasure = random.choice(list(treasures.keys()))
            player['inventory'].append(new_treasure)
        # TODO: Print messages describing what happened
            print(f"Success!! You have found a {new_treasure}, worth {treasures[new_treasure]} gold!")
        else:
        # TODO: Update player dictionary accordingly
            player['health'] -= 2
        # TODO: Print messages describing what happened
            print(f'Oh no! You fell into a trap and lost 2 health points. Your current health is {player['health']}')


    def check_status(player):
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        # TODO: Print player health
        print(f'Your current health is {player['health']}')
        # TODO: If the inventory list is not empty, print items joined by commas
        if player['inventory']:
             print(f'You have: {", ".join(player['inventory'])} in your inventory!')
        # TODO: Otherwise print “You have no items yet.”
        else:
             print("You have no items in your inventory.")

    def end_game(player, treasures):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        # TODO: Calculate total score by summing the value of collected treasures
        total_score = sum(treasures[item]for item in player['inventory'])
        # TODO: Print final health, items, and total value
        print(f'Final health : {player['health']} \n Items collected: {', ' .join(set(player['inventory']))} \n Total Score in Gold: {total_score}')
        # TODO: End with a message like "Game Over! Thanks for playing."
        print(f'Thanks for playing, {player['name']}!!!')

    def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # TODO: Loop through 5 rooms (1–5)
        for room in range(1,6):
        # TODO: Inside each room, prompt player choice using input()
            while True:
                display_options(room)
                choice = int(input("Enter your choice (1-4):  "))
              
        # TODO: Use if/elif to handle each choice (1–4)
                if choice == 1:
                    search_room(player, treasures)
                    if player['health'] < 1:
                        print('You Died, better luck next time!')               
                        end_game(player, treasures)
                        return
                elif choice == 2:
                    if room < 5:
                        print(f'You are moving on to the next room...time to explore room {room +1}')
                    break
                elif choice == 3:
                    check_status(player)
                elif choice == 4:
                    print('You are a quitter!!! Try again!')
                    end_game(player, treasures)
                    return
                else:
                    print('Invalid choice! Try again! Must choose a number 1-4.')
                

        # TODO: Break or return appropriately when player quits or dies


        # TODO: Call end_game() after all rooms are explored
        end_game(player, treasures)

  

    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)


if __name__ == "__main__":
    main()
