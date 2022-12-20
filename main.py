import pyproj


class Transform:
    """
    :param system1: Первая система счисления (должна соответствовать ключам из словаря epsg_codes)
    :param system2: Вторая система счисления (должна соответствовать ключам из словаря epsg_codes)
    :param lat: Широта
    :param lon: Долгота

    """
    _EPSG_CODES = {
        'WGS-84': 4326,
        'ГСК-2011': 7683,
        'ПЗ-90.11': 4740,
        'СК-95': 7680,
        'СК-42': 4284
    }

    __slots__ = ('__system1', '__system2', '__lat', '__lon')

    def __init__(self, system1, system2, lat, lon):
        self.__verify_system(system1)
        self.__verify_system(system2)

        self.__verify_coord(lat)
        self.__verify_coord(lon)

        self.__system1 = system1
        self.__system2 = system2
        self.__lat = lat
        self.__lon = lon

    # Checking for wrong input data
    @classmethod
    def __verify_system(cls, value):
        if value not in cls._epsg_codes.keys():
            raise TypeError('Вы ввели недопустимую систему координат')

    @classmethod
    def __verify_coord(cls, coord):
        if not isinstance(coord, (float, int)):
            raise TypeError('Координаты должны быть числами')

    def transform(self):
        transformer = pyproj.Transformer.from_crs(self._epsg_codes[self.__system1], self._epsg_codes[self.__system2])
        return transformer.transform(self.__lat, self.__lon)


if __name__ == '__main__':
    trans = Transform('WGS-84', 'СК-42', 52, 33)
    print(trans.transform())
