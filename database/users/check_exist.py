from database import cursor

def check_exits(phone):
	query = "SELECT * FROM TABLE users"
	cursor.execute(f"SELECT * FROM users WHERE phone = {phone}")

	return (len(cursor.fetchall()) != [])