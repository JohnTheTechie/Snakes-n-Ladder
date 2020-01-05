from bs4 import BeautifulSoup


class ConfigReader:
    """
    Parse and read out the configuration values for the game
    """

    def __init__(self):
        """
        create and initialize the soup
        """
        self.soup = None

    def parse(self, file="../configurations/test_game_config.xml"):
        """
        open and parse the xml config file
        :param file: location of the config file
        :return: None
        """
        with open(file) as xml:
            self.soup = BeautifulSoup(xml, "lxml-xml")

    def get_dice_type(self):
        """
        read out the dice type to be used
        :return: dice type: string
        """
        return self.soup.dice.type.text

    def get_dice_count(self):
        """
        read out number dice to be used

        :return: dice count: int
        """
        return int(self.soup.dice.count.text)

    def get_link_list(self):
        """
        read out the branching links

        :return: list of link pairs (from, to)
        """
        tag_list = self.soup.circuit.branching.find_all("link")
        link_list = []
        for item in tag_list:
            (fro, to) = int(item["from"]), int(item["to"])
            link_list.append((fro, to))
        self._process_link_validity(link_list)
        return link_list

    def _process_link_validity(self, links):
        """
        checks if the link map is forming loops

        raises an exception if so

        :param links: list of link pairs
        :return: None
        """
        for n in range(0, len(links)-1):
            (fro_x, to_x) = links[n]
            for y in range(n+1, len(links)):
                (fro_y, to_y) = links[y]
                # print((fro_x, to_x), (fro_y, to_y))
                if fro_x == to_y or fro_y == to_x:
                    raise Exception("circular linking")
