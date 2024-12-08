from users.schemas import CreateUser


def create_user(user: CreateUser) -> dict:
    user = user.model_dump()
    return {
        'status': 'success',
        'user': user
    }



