# SuperCoinquiBot is an Open Source bot developed by Leonardo Rignanese <dev.rignanese@gmail.com>
# GNU General Public License v3.0
# GITHUB: https://github.com/rignaneseleo/SuperCoinquiBot

from .flatmate import Flatmate


class Flat:
    name = ""
    flatmates_list = {}  # coinquilini
    cleaning_turns = []  # turni
    expenses_list = []  # lista spese

    def __init__(self, name):
        self.name = name

    def add_flatmate(self, nickname):
        # Check if it already exists
        if nickname.strip(',.').lower() not in self.flatmates_list:
            self.flatmates_list[nickname.strip(',.').lower()] = (Flatmate(nickname))
            return True
        else:
            return False

    def remove_flatmate(self, nickname):
        # Check if it exists
        if nickname.strip(',.').lower() in self.flatmates_list:
            del self.flatmates_list[nickname.strip(',.').lower()]
            return True
        else:
            return False

    def get_flatmates_names(self):
        flatmates_names = ""
        for nickname, flatmate in self.flatmates_list.items():
            flatmates_names += " " + flatmate.get_nickname()
        return flatmates_names
