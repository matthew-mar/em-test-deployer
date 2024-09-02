from configparser import ConfigParser

SERVICE_NAMES = [
    "product_service",
    "history_service",
]

SCRIPTS_DIR = "db_init"
CONFIG_FILE_PATH = "db_init.ini"

parser = ConfigParser()
parser.read(CONFIG_FILE_PATH)


def create_service_sheme(service_name: str) -> None:
    query = """
    CREATE USER {username} WITH PASSWORD '{password}';
    CREATE SCHEMA IF NOT EXISTS {schema} AUTHORIZATION {username};
    """.format_map({
        "username": parser.get(service, "username"),
        "password": parser.get(service, "password"),
        "schema": parser.get(service, "schema"),
    })

    with open(f"{SCRIPTS_DIR}/{service_name}.sql", "w") as sql_file:
        sql_file.write(query)


if __name__ == "__main__":
    for service in SERVICE_NAMES:
        create_service_sheme(service)
