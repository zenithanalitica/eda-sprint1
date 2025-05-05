import credentials
from neo4j import GraphDatabase


def main():
    with GraphDatabase.driver(
        credentials.uri, auth=(credentials.user, credentials.password)
    ) as driver:
        driver.verify_connectivity()
        print(f"Auth: {driver.verify_authentication()}")


if __name__ == "__main__":
    main()
