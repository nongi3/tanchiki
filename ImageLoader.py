from pygame import image, Rect


class ImageLoader:
    """
    Класс для загрузки спрайтов сразу для всех объектов
    _______________________
    Атрибуты
    sprites : объект image из pygame, в который загружаются все картинки для игры
    _______________________
    Методы
    get_sub_image : возвращает часть общего спрайта - спрайт конкретного объекта
    """
    def __init__(self):
        self.sprites = image.load("sprites.png")

    def get_sub_image(self, left_cor, right_cor):
        """
        возвращает часть общего спрайта - спрайт конкретного объекта
        :param left_cor: координаты левого верхнего угла необходимого изображения на общей картинке
        :param right_cor: координаты правого нижнего угла необходимого изображения на общей картинке
        :return: определенный необходимый спрайт
        """
        width = right_cor[0] - left_cor[0]
        height = right_cor[1] - left_cor[1]
        return self.sprites.subsurface(Rect(left_cor, (width, height)))

    def get_player_images(self):
        player_left_cor = (0, 0)
        player_right_cor = (35, 38)
        return [self.get_sub_image(player_left_cor, player_right_cor)]
