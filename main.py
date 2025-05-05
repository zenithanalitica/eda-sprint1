from typing import LiteralString
import neo4j
import credentials
from neo4j import GraphDatabase


def main():
    with GraphDatabase.driver(
        credentials.uri, auth=(credentials.user, credentials.password)
    ) as driver:
        driver.verify_connectivity()
        print(f"Auth: {driver.verify_authentication()}")
        run_query(driver, "MATCH (t:Tweet) RETURN t.id AS id LIMIT 10000")


def run_query(driver: neo4j.Driver, query: LiteralString):
    records, summary, _ = driver.execute_query(
        query,
        database_="neo4j",
    )

    # Loop through results and do something with them
    for tweet in records:
        print(tweet)

    # Summary information
    print(
        "The query `{query}` returned {records_count} records in {time} ms.".format(
            query=summary.query,
            records_count=len(records),
            time=summary.result_available_after,
        )
    )


if __name__ == "__main__":
    main()
