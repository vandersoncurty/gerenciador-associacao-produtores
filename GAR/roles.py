from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {
        'view_user': True,
        'edit_user': True,
        'delete_user': True,
    }

class Member(AbstractUserRole):
    available_permissions = {
        'view_user': True,
        'edit_user': False,
        'delete_user': False,
    }

class Guest(AbstractUserRole):
    available_permissions = {
        'view_user': False,
        'edit_user': False,
        'delete_user': False,
    }

class SuperUser(AbstractUserRole):
    available_permissions = {
        'view_user': True,
        'edit_user': True,
        'delete_user': True,
        'manage_roles': True,
        'manage_permissions': True,
    }

class Moderator(AbstractUserRole):
    available_permissions = {
        'view_user': True,
        'edit_user': True,
        'delete_user': False,
        'manage_roles': False,
        'manage_permissions': False,
    }

class CustomRole(AbstractUserRole):
    available_permissions = {
        'view_user': True,
        'edit_user': True,
        'delete_user': False,
        'manage_roles': False,
        'manage_permissions': False,
    }