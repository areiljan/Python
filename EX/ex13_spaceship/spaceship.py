"""Spaceship"""

class Crewmate:
    """
    Crewmate class.

    Not all crewmates are created equal, each has their own color, role and task attributes.
    """
    def __init__(self, color: str, role: str, tasks: int = 10):
        """Initialize the class.

        The color must be capitalized and the role must be inserted in all caps.
        The crewmates will also have a boolean value of protected and their tasks,
        which are at 10 by default."""
        self.color = color.capitalize()

        roles = ("Crewmate", "Sheriff", "Guardian Angel", "Altruist")
        role = role.title()
        if role not in roles:
            self.role = "Crewmate"
        else:
            self.role = role.title()
        self.tasks = tasks
        self.protected = False

    def __repr__(self):
        """Represent the class.

        A nice and clean way to display the information when directly calling the object in this class.
        """
        return f"{self.color}, role: {self.role}, tasks left: {self.tasks}."

    def complete_task(self):
        """Complete a task.

        Upon finishing a task, remove one integer value from the crewmates tasks attribute.
        """
        if self.tasks > 0:
            self.tasks -= 1

class Impostor:
    """
    Impostor class.

    Not all impostors are created equal, each has their own color and kills
    attribute, which starts at one.
    """
    def __init__(self, color):
        """Initialize the impostor class.

        The color must be capitalized, the impostor also has a kills attribute,
        which starts at one by default."""
        self.color = color.capitalize()

        self.kills = 0

    def __repr__(self):
        """Represent the class.

        A nice and clean way to display the information when directly calling the object in this class.
        """
        return f"Impostor {self.color}, kills: {self.kills}."

class Spaceship:
    """Spaceship class

    This is the class, where the game takes place, this class holds all the action functions,
    lists of players in different stages of the game and filtering systems, to keep an eye on
    the progress of each player.
    """
    def __init__(self, ):
        """Initialize the class.

        Adding the crewmate list, which will only hold living crewmates, the impostor list,
        which will only hold living impostors. The player color list, which makes it easier to
        keep track of the in-game player colors. And lastly the dead players list, which will hold
        both dead impostors and crewmates.
        """
        self.crewmate_list = []
        self.impostor_list = []
        self.player_color_list = []
        self.dead_players = []

    def get_crewmate_list(self):
        """Call the crewmate list.

        Returns a representation of crewmates.
        """
        return self.crewmate_list

    def get_impostor_list(self):
        """Call the impostor list.

        Returns a representation of impostors.
        """
        return self.impostor_list

    def get_dead_players(self):
        """Call the dead.

        Returns a list of the dead.
        """
        return self.dead_players

    def add_crewmate(self, crewmate: Crewmate):
        """Add a crewmate.

        Adds a crewmate to the spaceship. Makes sure, that no duplicate colors are added.
        """
        color = crewmate.color.capitalize()
        if crewmate.color not in self.player_color_list and isinstance(crewmate, Crewmate):
            self.crewmate_list.append(crewmate)
            self.player_color_list.append(color)

    def add_impostor(self, impostor: Impostor):
        """Add an impostor.

        Adds an impostor to the spaceship. Makes sure, that no duplicates are added and that the
        impostor count does not exceed 3.
        """
        color = impostor.color.capitalize()
        if impostor.color not in self.player_color_list and isinstance(impostor, Impostor)\
        and len(self.impostor_list) < 3:
            self.impostor_list.append(impostor)
            self.player_color_list.append(color)
        else:
            print(f"{impostor.color} cannot be an impostor.")

    def kill_impostor(self, sheriff: Crewmate, color: str):
        """Kill an impostor.

        The Sheriff can kill an impostor if he chooses right, if he does not choose right , he himself
        will die.
        """
        if sheriff in self.crewmate_list and sheriff.role == "Sheriff":
            color = color.capitalize()
            chosen_impostor = list(filter(lambda impostor: impostor.color == color, self.impostor_list))
            if chosen_impostor:
                self.player_color_list.remove(color)
                self.impostor_list.remove(chosen_impostor[0])
                self.dead_players.append(chosen_impostor[0])
            else:
                self.crewmate_list.remove(sheriff)
                self.dead_players.append(sheriff)

    def revive_crewmate(self, altruist: Crewmate, dead_crewmate: Crewmate):
        """Revive a crewmate.

        The altruist can sacrifice his/her own life to bring a crewmate back from the dead.
        """
        if dead_crewmate in self.dead_players and altruist.role == "Altruist" \
            and altruist in self.crewmate_list:
            self.dead_players.remove(dead_crewmate)
            self.player_color_list.append(dead_crewmate.color)
            self.crewmate_list.append(dead_crewmate)
            self.crewmate_list.remove(altruist)
            self.player_color_list.remove(altruist.color)
            self.dead_players.append(altruist)

    def protect_crewmate(self, guardian_angel: Crewmate, crewmate_to_protect: Crewmate):
        """Protect a crewmate.

        The guardian angel can choose which one player he chooses to cast a protection spell upon.
        All other players will be toggled unprotected.
        """
        if guardian_angel in self.dead_players and guardian_angel.role == "Guardian Angel"\
                and crewmate_to_protect in self.crewmate_list:
            is_value_present = any(crewmate.protected == True for crewmate in self.crewmate_list)
            if is_value_present:
                for crewmate in self.crewmate_list:
                    crewmate.protected = False
                crewmate_to_protect.protected = True

    def kill_crewmate(self, impostor: Impostor, color):
        """Kill a crewmate.

        The impostors can kill crewmates. The impostor kill statistic will be upped by one.
        """
        if impostor in self.impostor_list:
            color = color.capitalize()
            chosen_crewmate = list(filter(lambda crewmate: crewmate.color == color, self.crewmate_list))
            if chosen_crewmate:
                if not chosen_crewmate[0].protected:
                    self.crewmate_list.remove(chosen_crewmate[0])
                    self.player_color_list.remove(color)
                    self.dead_players.append(chosen_crewmate[0])
                    impostor.kills += 1
                else:
                    chosen_crewmate[0].protected = False

    def sort_crewmates_by_tasks(self):
        """Sort crewmates by tasks.

        Sort the remaining crewmates by the amount of tasks they have left.
        """
        sorted_crewmates = sorted(self.crewmate_list, key=lambda crewmate: crewmate.tasks)
        return sorted_crewmates

    def sort_impostors_by_kills(self):
        """Sort impostors by kills.

        Sort the remaining impostors by the amount of kills they have.
        """
        sorted_impostors = sorted(self.impostor_list, key=lambda impostor: impostor.kills, reverse=True)
        return sorted_impostors

    def get_regular_crewmates(self):
        """Get a list of the remaining regular crewmates.

        Filters out a list of crewmates without a special role attribute.
        """
        chosen_crewmate = list(filter(lambda crewmate: crewmate.role == "Crewmate", self.crewmate_list))
        return chosen_crewmate

    def get_role_of_player(self, color: str):
        """Get the player role.

        Get the player role with the speciifed color. The roles are: Crewmate, Impostor, Guardian
        Angel, Sheriff, Altruist.
        """
        color = color.capitalize()
        if color in self.player_color_list:
            chosen_impostor = list(filter(lambda impostor: impostor.color == color, self.impostor_list))
            chosen_crewmate = list(filter(lambda crewmate: crewmate.color == color, self.crewmate_list))
            if chosen_impostor:
                return "Impostor"
            elif chosen_crewmate:
                return chosen_crewmate[0].role
            else:
                return None

    def get_crewmate_with_most_tasks_done(self):
        """Get crewmate with least tasks left.

        Returns the crewmate with the most actions done during this game.
        """
        sorted_crewmates = sorted(self.crewmate_list, key=lambda crewmate: crewmate.tasks)
        return sorted_crewmates[0]

    def get_impostor_with_most_kills(self):
        """Get the deadliest impostor.

        Returns the impostor with the biggest amount of kills.
        """
        sorted_impostors = sorted(self.impostor_list, key=lambda impostor: impostor.kills, reverse=True)
        return sorted_impostors[0]



if __name__ == "__main__":
    print("Spaceship.")

    spaceship = Spaceship()
    print(spaceship.get_dead_players())  # -> []
    print()

    print("Let's add some crewmates.")
    red = Crewmate("Red", "Crewmate")
    white = Crewmate("White", "Impostor")
    yellow = Crewmate("Yellow", "Guardian angel", tasks=5)
    green = Crewmate("green", "Altruist")
    blue = Crewmate("BLUE", "Sheriff", tasks=0)

    print(red)  # -> Red, role: Crewmate, tasks left: 10.
    print(white)  # -> White, role: Crewmate, tasks left: 10.
    print(yellow)  # -> Yellow, role: Guardian Angel, tasks left: 5.
    print(blue)  # -> Blue, role: Sheriff, tasks left: 0.
    print()

    print("Let's make Yellow complete a task.")
    yellow.complete_task()
    print(yellow)  # ->  Yellow, role: Guardian Angel, tasks left: 4.
    print()

    print("Adding crewmates to Spaceship:")
    spaceship.add_crewmate(red)
    spaceship.add_crewmate(white)
    spaceship.add_crewmate(yellow)
    spaceship.add_crewmate(green)
    print(spaceship.get_crewmate_list())  # -> [Red, role: Crewmate, tasks left: 10., White, role: Crewmate, tasks left: 10., Yellow, role: Guardian Angel, tasks left: 4., Green, role: Altruist, tasks left: 10.]

    spaceship.add_impostor(blue)  # Blue cannot be an Impostor.
    print(spaceship.get_impostor_list())  # -> []
    spaceship.add_crewmate(blue)
    print()

    print("Now let's add impostors.")
    orange = Impostor("orANge")
    black = Impostor("black")
    purple = Impostor("Purple")
    spaceship.add_impostor(orange)
    spaceship.add_impostor(black)

    spaceship.add_impostor(Impostor("Blue"))  # Blue player already exists in Spaceship.
    spaceship.add_impostor(purple)
    spaceship.add_impostor(Impostor("Pink"))  # No more than three impostors can be on Spaceship.
    print(spaceship.get_impostor_list())  # -> Orange, Black and Purple
    print()

    print("The game has begun! Orange goes for the kill.")
    spaceship.kill_crewmate(orange, "yellow")
    print(orange)  # -> Impostor Orange, kills: 1.
    spaceship.kill_crewmate(black, "purple")  # You can't kill another Impostor, silly!
    print(spaceship.get_dead_players())  # -> Yellow
    print()

    print("Yellow is a Guardian angel, and can protect their allies when dead.")
    spaceship.protect_crewmate(yellow, green)
    print(green.protected)  # -> True
    spaceship.kill_crewmate(orange, "green")
    print(green in spaceship.dead_players)  # -> False
    print(green.protected)  # -> False
    print()

    print("Green revives their ally.")
    spaceship.kill_crewmate(purple, "RED")
    spaceship.revive_crewmate(green, red)
    print(red in spaceship.dead_players)  # -> False
    print()

    print("Let's check if the sorting and filtering works correctly.")

    red.complete_task()
    print(spaceship.get_role_of_player("Blue"))  # -> Sheriff
    spaceship.kill_crewmate(purple, "blue")
    print(spaceship.sort_crewmates_by_tasks())  # -> Red, White
    print(spaceship.sort_impostors_by_kills())  # -> Purple, Orange, Black
    print(spaceship.get_regular_crewmates())  # -> White, Red

