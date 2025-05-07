from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text

# Load environment variables from .env
load_dotenv()

pg_user = os.getenv('PG_USER')
pg_password = os.getenv('PG_PASSWORD')
pg_host = os.getenv('PG_HOST')
pg_db = os.getenv('PG_DB')

print("Connecting to database:", pg_db)

# Create the SQLAlchemy engine
engine = create_engine(
    f"postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:5432/{pg_db}"
)

with engine.connect() as conn:
    # Step 1: Create the schema if it doesn't exist
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS sql_project;"))
    print("Schema 'sql_project' created or already exists.")

    # Step 2: Verify the schema exists
    result = conn.execute(
        text("SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'sql_project';")
    )
    rows = result.fetchall()

    if rows:
        print("✅ sql_project schema DOES exist.")
    else:
        print("❌ sql_project schema does NOT exist.")

    # Step 3: List all schemas for visibility
    result = conn.execute(text("SELECT schema_name FROM information_schema.schemata;"))
    print("\nSchemas in the database:")
    for row in result:
        print(row[0])
