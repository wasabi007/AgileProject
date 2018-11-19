from normal_user import User


class BaseClass(User):

    def user_type(self):
        selection = input("Enter admin, user or mod")
        return selection

    def delete_comment(self, comment_id):
        usertype = self.user_type()
        if usertype.role == 'mod' or usertype.role == 'admin':
            self.comments.remove(comment_id)
        else:
            print('not allowed')

    def delete_user(self, user_id):
        usertype = self.user_type()
        if usertype.role == 'admin':
            self.users.remove(user_id)
        else:
            print('not allowed')

    def edit_comments(self, comment_id):
        new = input('enter new content')
        self.comments[comment_id].content = new

