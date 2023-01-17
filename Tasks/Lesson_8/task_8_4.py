class Category:
    # cat_dict = dict()
    categories: list[{}] = []

    @classmethod
    def add(cls, cat_name: str, is_published: bool) -> int:
        if all(False if x.get("name") == cat_name else True for x in cls.categories):
            cat_dict = dict()
            cat_dict["name"] = cat_name
            cat_dict["is_published"] = is_published
            cls.categories.append(cat_dict)
            return len(cls.categories) - 1
        else:
            raise ValueError('argument `category` is not unique')

    @classmethod
    def get(cls, i: int) -> dict:
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
    def update(cls, i: int, category: str, is_published: bool) -> None:
        if i not in range(len(cls.categories)):
            cls.add(category, is_published)
        elif all(False if x.get("name") == category else True for x in cls.categories):
            cls.categories[i]["name"] = category
        else:
            raise ValueError('argument `category` is not unique')

    @classmethod
    def make_published(cls, i: int) -> None:
        try:
            cls.categories[i]["is_published"] = True
        except IndexError as ex:
            raise IndexError('wrong category index')
    @classmethod
    def make_unpublished(cls, i: int) -> None:
        try:
            cls.categories[i]["is_published"] = False
        except IndexError as ex:
            raise IndexError('wrong category index')



obj = Category
obj.add("First", False)
obj.add("Second", False)
obj.update(0, "Third", False)
obj.make_published(2)

# obj.delete(0)
print(obj.categories)
