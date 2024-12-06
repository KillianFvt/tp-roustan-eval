class Disk:
    __total = -1
    __used = -1

    def __init__(self, total, used):
        self.__total = total
        self.__used = used

    @property
    def free(self):
        return self.__total - self.__used

    @property
    def used_perc(self):
        return self.__used / self.__total

    def __str__(self):
        return f"Disk[total: {self.__total} Gb, used: {self.__used} Gb]"

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.used_perc < other.used_perc