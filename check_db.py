"""
Diagnostic script.
Run this from inside your project folder (where app/ lives) with:
    python check_db.py

It will:
1. Show which columns actually exist on the `users` table right now.
2. Try to create ONE test employee user directly (no FastAPI, no Swagger)
   and print the FULL error if something goes wrong.

Delete this file once the issue is fixed. It creates a throwaway user
with email 'diagnostic_test_user@example.com' - delete that row afterwards.
"""

from sqlalchemy import inspect
from app.database import engine, SessionLocal
from app.models.user import User
from app.auth import hash_password
import traceback
import datetime

print("=" * 60)
print("STEP 1: Checking actual columns on 'users' table in your DB")
print("=" * 60)

inspector = inspect(engine)
columns = inspector.get_columns("users")
for col in columns:
    print(f"  - {col['name']:20s} {col['type']}  nullable={col['nullable']}")

print()
print("=" * 60)
print("STEP 2: Trying to insert one test EMPLOYEE user directly")
print("=" * 60)

db = SessionLocal()

try:
    test_user = User(
        first_name="Diagnostic",
        last_name="Test",
        email="diagnostic_test_user@example.com",
        phone="9999999999",
        password=hash_password("Test@1234"),
        role_id=1,  # change this to a role_id that actually exists in your roles table
        user_type="employee",
        department_id=None,
        joining_date=datetime.date.today(),
        salary=10000,
        status=True,
    )

    db.add(test_user)
    db.commit()
    db.refresh(test_user)

    print("SUCCESS! User created with id:", test_user.id)
    print("Now go delete this row from your DB (email = diagnostic_test_user@example.com)")

except Exception:
    print("FAILED. Full error below:\n")
    traceback.print_exc()
    db.rollback()

finally:
    db.close()