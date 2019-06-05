# coding=utf-8


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group.users:
        return user in group.users
    else:
        for g in group.groups:
            return is_user_in_group(user, g)

    return False  # no users in group


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Expected result of the test: True
print("Parent: " + str(is_user_in_group(sub_child_user, parent)))

# Expected result of the test: True
print("Child: " + str(is_user_in_group(sub_child_user, child)))

# Expected result of the test: True
print("Sub-Child: " + str(is_user_in_group(sub_child_user, sub_child)))


false_parent = Group("false_parent")
false_child = Group("false_child")

false_parent.add_group(false_child)

# Expected result of the test: False
print("False Parent: " + str(is_user_in_group(sub_child_user, false_parent)))

# # Expected result of the test: False
print("False Child: " + str(is_user_in_group(sub_child_user, false_child)))
