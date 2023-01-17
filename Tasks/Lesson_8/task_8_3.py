class Category:
    categories: list[str] = []

    @classmethod
    def add(cls, cat_name: str) -> int:
        if cat_name not in cls.categories:
            cls.categories.append(cat_name)
            return cls.categories.index(cat_name)
        else:
            raise ValueError('argument `category` is not unique')

    @classmethod
    def get(cls, i: int) -> str:
        try:
            return cls.categories[i]
        except IndexError as ex:
            raise ValueError(ex)

    @classmethod
    def delete(cls, i: int) -> None:
        try:
            del cls.categories[i]
        except IndexError:
            pass

    @classmethod
    def update(cls, i: int, category: str) -> None:
        if i not in range(len(cls.categories)):
            cls.add(category)
        elif category not in cls.categories:
            cls.categories[i] = category
        else:
            raise ValueError('argument `category` is not unique')


