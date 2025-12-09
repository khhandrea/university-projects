from csv import writer
from sqlite3 import connect

if __name__ == '__main__':
    conn = connect('sakila.db')
    cursor = conn.cursor()

    query = "SELECT * FROM film WHERE rental_duration BETWEEN 3 AND 7"
    cursor.execute(query)

    with open('result.csv', 'w') as file:
        csv_writer = writer(file)
        csv_writer.writerow([i[0] for i in cursor.description])

        csv_writer.writerows(cursor.fetchall())
    
    conn.close()