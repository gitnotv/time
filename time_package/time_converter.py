


class timify():
    """[_convert : converts your time in s|m|h|d|w|m|y to seconds then returns the result]"""

    def _convert(self, query : str):
        without_unit = query[:-1]
        raw_unit = query[-1:]
        if without_unit.isnumeric():
            unit_dict = {"s" : 1, "h" : 3600, "m" : 60, "d" : 3600 * 24, "w" : 3600 * 24 * 7, "m" : 3600 * 24 * 7 * 4, "y" : 3600 * 24 * 7 * 4 * 12}
            try:
                converter = unit_dict[raw_unit]
            except KeyError:
                raise KeyError("Recieved invalid time format.")
            else:
                result = int(converter) * int(without_unit)
                return result
        raise ValueError("Recieved characters instead of an integer.")







# t_i var
time_instance = timify()
