from task_12_1 import Role, User, Category, Topic, Comment

# roles = ('User', 'Super', 'Admin', 'Editor')
#
# for role in roles:
#     role = Role(name=role)
#     role.save()

# users = [
#     {'user': 'johny',
#      'email': 'johny@gmail.com',
#      'role': 1},
#     {'user': 'harry_12',
#      'email': 'harry_12@gmail.com',
#      'role': 2},
#     {'user': 'markymark',
#      'email': 'markymark@gmail.com',
#      'role': 4},
#     {'user': 'user123',
#      'email': 'user123@gmail.com',
#      'role': 1},
#     {'user': 'oper',
#      'email': 'oper@gmail.com',
#      'role': 3}
# ]
#
# for user in users:
#     user = User(username=user.get('user'), email=user.get('email'), role_id=user.get('role'))
#     user.save()

# categories = ('Science', 'Military', 'Music', 'Entertainment')
#
# for category in categories:
#     category = Category(name=category)
#     category.save()


# topics = [
#     {'author_id': 1,
#      'category_id': 1},
#     {'author_id': 4,
#      'category_id': 3},
#     {'author_id': 3,
#      'category_id': 2},
#     {'author_id': 1,
#      'category_id': 4},
# ]
#
# for topic in topics:
#     topic = Topic(author_id=topic.get('author_id'), category_id=topic.get('category_id'))
#     topic.save()

# comments = [
#     {'user_id': 1,
#      'topic_id': 1,
#      'parent_id': 1},
#     {'user_id': 2,
#      'topic_id': 2,
#      'parent_id': 1}
# ]
#
# for comment in comments:
#     comment = Comment(user_id=comment.get('user_id'), topic_id=comment.get('topic_id'), parent_id=comment.get('parent_id'))
#     comment.save()

# print(User.get(1).username)
print(User.all(limit=1))