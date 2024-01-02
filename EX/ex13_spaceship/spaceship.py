"""Spaceship"""

class Crewmate:
    """
    Crewmate class.

    Not all crewmates are created equal, each has their own color, role and task attributes.
    """
    def __init__(self, color: str, role: str, tasks: int = 10):
        """Initializes the class.

        The color must be capitalized and the role must be inserted in all caps.
        The crewmates will also have a boolean value of protected and their tasks,
        which are at 10 by default."""
        color.capitalize()
        self.color = color

        roles = ("Crewmate", "Sheriff", "Guardian angel", "Altruist")
        role.capitalize()
        if role not in roles:
            self.role = "Crewmate"
        else:
            self.role = role.capitalize()
        self.tasks = tasks
        self.protected = True

    def __repr__(self):
        """Representing the class.

        A nice and clean way to display the information when directly calling the object in this class."""
        return f"{self.color}, role: {self.role}, tasks left: {self.tasks}."

    def complete_task(self):
        """Completing a task.

        Upon finishing a task, remove one integer value from the crewmates tasks attribute."""
        self.tasks -= 1

class Impostor:
    """
    Crewmate class.

    Not all impostors are created equal, each has their own color and kills
    attribute, which starts at one.
    """
    def __init__(self, color):
        """Initialize the impostor class.

        The color must be capitalized, the impostor also has a kills attribute,
        which starts at one by default."""
        color.capitalize()
        self.color = color

        self.kills = 0

    def __repr__(self):
        """Representing the class.

        A nice and clean way to display the information when directly calling the object in this class."""
        return f"Impostor {self.color}, kills: {self.kills}"

class Spaceship:
    def __init__(self, ):
        self.crewmate_list = []
        self.impostor_list = []
        self.player_color_list = []
        self.dead_players = []

    def get_crewmate_list(self):
        return self.crewmate_list

    def get_impostor_list(self):
        return self.impostor_list

    def get_dead_players(self):
        return self.dead_players

    def add_crewmate(self, crewmate: Crewmate):
        self.player_color_list = []
        if crewmate.color not in self.player_color_list:
            self.crewmate_list.append(crewmate)
            self.player_color_list.append(crewmate.color)

    def add_impostor(self, impostor: Impostor):
        self.player_color_list = []
        if impostor.color not in self.player_color_list and isinstance(impostor, Impostor):
            self.impostor_list.append(impostor)
            self.player_color_list.append(impostor.color)

    def kill_impostor(self, sheriff: Crewmate, color: str):
        chosen_impostor = list(filter(lambda impostor: impostor.color == color, self.impostor_list))
        if chosen_impostor:
            self.player_color_list.remove(color)
            self.impostor_list.remove(chosen_impostor[0])
            self.dead_players.append(chosen_impostor)
        else:
            self.crewmate_list.remove(sheriff)
            self.dead_players.append(sheriff)

    def revive_crewmate(self, altruist: Crewmate, dead_crewmate: Crewmate):
        if dead_crewmate in self.dead_players:
            self.dead_players.remove(dead_crewmate)
            self.player_color_list.append(dead_crewmate.color)
            self.crewmate_list.append(dead_crewmate)
            self.crewmate_list.remove(altruist)
            self.player_color_list.remove(altruist.color)
            self.dead_players.append(altruist)

    def protect_crewmate(self, guardian_angel: Crewmate, crewmate_to_protect: Crewmate):
        if guardian_angel in self.dead_players:
            for crewmate in self.crewmate_list:
                crewmate.protected = False
            crewmate_to_protect.protected = True

    def kill_crewmate(self, impostor: Impostor, color):
        chosen_crewmate = list(filter(lambda crewmate: crewmate.color == color, self.crewmate_list))
        if chosen_crewmate:
            if chosen_crewmate[0].protected == False:
                self.crewmate_list.remove(chosen_crewmate[0])
                self.player_color_list.remove(color)
                self.dead_players.append(chosen_crewmate[0])
                impostor.kills += 1
            else:
                chosen_crewmate[0].protected = False

    def sort_crewmates_by_tasks(self):
        sorted_crewmates = sorted(self.crewmate_list, key=lambda crewmate: crewmate.tasks)
        return sorted_crewmates

    def sort_impostors_by_kills(self):
        sorted_impostors = sorted(self.impostor_list, key=lambda impostor: impostor.kills)
        return sorted_impostors

    def get_regular_crewmates(self):
        chosen_crewmate = list(filter(lambda crewmate: crewmate.role == "CREWMATE", self.crewmate_list))
        return chosen_crewmate
    def get_role_of_player(self, color: str):
        if color in self.player_color_list:
            chosen_impostor = list(filter(lambda impostor: impostor.color == color, self.impostor_list))
            chosen_crewmate = list(filter(lambda crewmate: crewmate.color == color, self.crewmate_list))
            if chosen_impostor:
                return chosen_impostor[0].role
            else:
                return chosen_crewmate[0].role

    def get_crewmate_with_most_tasks_done(self):
        sorted_crewmates = sorted(self.crewmate_list, key=lambda crewmate: crewmate.tasks)
        return sorted_crewmates[0]

    def get_impostor_with_most_kills(self):
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
    yellow = Crewmate("Yellow", "Guardian Angel", tasks=5)
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

    for impostor in spaceship.impostor_list:
        if not isinstance(impostor, Impostor):
            raise TypeError("List should only contain Impostor objects.")
