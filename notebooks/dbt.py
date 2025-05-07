from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine, text

# Step 1: Load environment variables
load_dotenv()

pg_user = os.getenv('PG_USER')
pg_password = os.getenv('PG_PASSWORD')
pg_host = os.getenv('PG_HOST')
pg_db = os.getenv('PG_DB')

print("Connecting to database:", pg_db)

# Step 2: Create SQLAlchemy engine
engine = create_engine(
    f"postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:5432/{pg_db}"
)

# Step 3: Read CSV files
payrolls = pd.read_csv('/workspaces/moneyball/notebooks/data/mlb_payrolls.csv')
records = pd.read_csv('/workspaces/moneyball/notebooks/data/mlb_team_records_2011_2024.csv')

print("Payrolls shape:", payrolls.shape)
print("Records shape:", records.shape)

# Step 4: Clean up column names
payrolls.columns = payrolls.columns.str.strip()
records.columns = records.columns.str.strip()

# Step 5: Map abbreviations to full names
abbrev_to_full = {
    'NYY': 'New York Yankees', 'TB': 'Tampa Bay Rays', 'BOS': 'Boston Red Sox',
    'TOR': 'Toronto Blue Jays', 'BAL': 'Baltimore Orioles', 'DET': 'Detroit Tigers',
    'CLE': 'Cleveland Guardians', 'CHW': 'Chicago White Sox', 'KC': 'Kansas City Royals',
    'MIN': 'Minnesota Twins', 'TEX': 'Texas Rangers', 'LAA': 'Los Angeles Angels',
    'OAK': 'Oakland Athletics', 'SEA': 'Seattle Mariners', 'PHI': 'Philadelphia Phillies',
    'ATL': 'Atlanta Braves', 'WSH': 'Washington Nationals', 'NYM': 'New York Mets',
    'MIA': 'Miami Marlins', 'FLA': 'Florida Marlins', 'MIL': 'Milwaukee Brewers',
    'STL': 'St. Louis Cardinals', 'CIN': 'Cincinnati Reds', 'PIT': 'Pittsburgh Pirates',
    'CHC': 'Chicago Cubs', 'HOU': 'Houston Astros', 'ARI': 'Arizona Diamondbacks',
    'SF': 'San Francisco Giants', 'LAD': 'Los Angeles Dodgers', 'COL': 'Colorado Rockies',
    'SD': 'San Diego Padres'
}

# Fix team names in payrolls
payrolls['Team Full'] = payrolls['Team'].map(abbrev_to_full)

# Fix team names in records
records['Team'] = records['Team'].replace({
    'Florida Marlins': 'Miami Marlins',
    'Cleveland Indians': 'Cleveland Guardians',
    'Los Angeles Angels of Anaheim': 'Los Angeles Angels'
})

# Step 6: Merge dataframes on full team name and year
combined = pd.merge(
    payrolls,
    records,
    left_on=['Team Full', 'Year'],
    right_on=['Team', 'Year'],
    how='inner'
)

print("Combined shape:", combined.shape)
print(combined.head())

# Step 7: Ensure the schema exists (and confirm it's really there)
with engine.begin() as conn:
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS sql_project;"))
    result = conn.execute(text("""
        SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'sql_project';
    """))
    rows = result.fetchall()
    if rows:
        print("✅ sql_project schema confirmed before uploading.")
    else:
        print("❌ sql_project schema still missing!")

# Step 8: Upload to Postgres in 'sql_project' schema
if combined.shape[0] > 0:
    combined.to_sql(
        'team_payroll_records',
        engine,
        schema='sql_project',
        if_exists='replace',
        index=False
    )
    print("✅ Data uploaded to sql_project.team_payroll_records")
else:
    print("⚠ No data to upload — merged DataFrame is empty.")
