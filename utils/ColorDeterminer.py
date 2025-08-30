

class ColorDeterminer:

    @staticmethod
    def is_red(color):

        r = color[0]
        g = color[1]
        b = color[2]

        if r > 120 and g < 50 and b < 50:
            return True

        return False

    @staticmethod
    def is_yellow(color):

        r = color[0]
        g = color[1]
        b = color[2]

        if r > 120 and g > 120 and b < 90:
            return True

        return False

    @staticmethod
    def is_green(color):

        r = color[0]
        g = color[1]
        b = color[2]

        if g > r + 15 and g > b + 20:
            return True

        return False

    @staticmethod
    def is_blue(color):

        r = color[0]
        g = color[1]
        b = color[2]

        if b > r + 20 and b > g + 20:
            return True

        return False
