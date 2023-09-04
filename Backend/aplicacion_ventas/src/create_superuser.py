from general.ormbase import ORMManager
from users.models.users import User
from users.schemas.user_input import LoginInput


def create_user() -> None:
    try:
        with ORMManager.get_orm()._get_session() as sess:
            print("Esta por crear un usuario, use ctrl+c para cancelar en cualquier momento")  # noqa: T201
            while True:
                username = input("Ingrese el nombre de usuario: ")
                if len(username) < 3 or len(username) > 50:
                    print("Nombre de usuario inválido, debe tener entre 3 y 50 caracteres")  # noqa: T201
                    continue
                user = sess.query(User).filter(User.username == username).first()
                if user is not None:
                    print("Nombre de usuario ya existe")  # noqa: T201
                    continue
                break
            while True:
                password = input("Ingrese la contraseña: ")
                if len(password) < 8 or len(password) > 50:
                    print("Contraseña inválida, debe tener entre 8 y 50 caracteres")  # noqa: T201
                    continue
                break
            while True:
                superuser = input("¿Es superusuario? (y/n): ")
                if superuser == "y":
                    is_superuser = True
                    break
                elif superuser == "n":
                    is_superuser = False
                    break
                else:
                    print("Opción inválida, seleccione y o n")  # noqa: T201
            LoginInput(username=username, password=password)
            user = User(username=username, password=password, is_superuser=is_superuser)
            sess.add(user)
            sess.commit()
            print("Usuario creado con éxito")  # noqa: T201
    except KeyboardInterrupt:
        print("Creación de usuario cancelada")  # noqa: T201
        return


if __name__ == "__main__":
    create_user()
