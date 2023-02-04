from models import Category

cat = Category.get(2)
# # print(cat.name)
# print(cat.__dict__)

# categories = ('Food', 'Clothes')
# for category in categories:
#     category = Category(name=category)
#     category.save()

# print([elem.values() for elem in Category.all()])
# for res in Category.all():
#     print(res.values())
# print(Category.all())
# with Category._Session() as session:
#     session: Session
    # cat = Category(name='Drinks')
    # session.add(cat)
    # session.commit()
    # session.refresh(cat)
    #     print(cat.id)
    #     print(cat.name)
    #     print(cat.is_published)
    # query = session.scalars(
    #     select(Category)
    #     .order_by('name')
    #     .filter_by(id=2, is_published=True)
    #     # .where(or_(Category.id > 0, Category.is_published == True))
    # )
    # for category in query.all():
    #     category.is_published = False
    #     session.add(category)
    #     session.commit()

    # category = session.get(Category, 1)
    # print(category.name)
    # session.delete(category)
    # session.commit()

    # session.execute(delete(Category).where(Category.is_published == True))
    # session.commit()
    # session.execute(
    #     select(Category, Product)
    #     .join(Product, Product.category_id)
    # )