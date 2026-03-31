import psycopg2

DATABASE_URL = "postgresql://postgres:newpassword@localhost:5432/voters_db"

def init_database():
    connection = psycopg2.connect(DATABASE_URL)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS voters (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            age INTEGER NOT NULL,
            phone VARCHAR(20) NOT NULL,
            address TEXT NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()
    print("Database initialized!")

if __name__ == "__main__":
    init_database()
