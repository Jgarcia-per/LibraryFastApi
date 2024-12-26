
def override_get_current_user():
    return {
                'id': 1,
                'first_name': 'User',
                'role': 'ADMIN',
                'last_name': 'pytest',
                'email': 'user_pytest@gmail.com',
                'username': 'User Pytest',
                'password': 'AdminPassword',
                'is_active': True,
                'phone_number': '999 888 7766'
            }
