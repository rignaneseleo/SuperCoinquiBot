# SuperCoinquiBot is an Open Source bot developed by Leonardo Rignanese <dev.rignanese@gmail.com>
# GNU General Public License v3.0
# GITHUB: https://github.com/rignaneseleo/SuperCoinquiBot

class Flatmate:
    nickname = ""

    def __init__(self, nickname):
        self.nickname = nickname

    def get_nickname(self):
        return self.nickname
