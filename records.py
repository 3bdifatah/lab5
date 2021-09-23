import sqlite3
import ui

db='records.sqlite'


def create_table():
    """creats table called records
    with ID, name, country, and number of catches attributs 
    """
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS records (record_id INTEGER PRIMARY KEY, name TEXT UNIQUE, country TEXT, num_of_catches INT)')
    conn.close()


def main():
    create_table()
    menu_text = """
    1. Display all records
    2. Add new record
    3. Edit existing record
    4. Delete record 
    5. Search record holder
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            add_new_record()
        elif choice == '3':
            edit_existing_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            name =ui.get_name()
            name_found=search_record(name)
            if name_found:
                print(name_found)
            else:
                ui.error_message(name)
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    """displays all the records in the databse if there is any
    """
    conn = sqlite3.connect(db)
    all_records = conn.execute('SELECT * FROM records')
    for record in all_records:
        print(record)
    conn.close()


def add_new_record():
    """adds new records to the database
    asks name country and record and adds them to the database     
    """
    name=ui.get_name()
    country, record=ui.get_country_and_record()
    try:
        with sqlite3.connect(db) as conn:
            conn.execute('INSERT INTO records (name, country, num_of_catches) VALUES (?, ?, ?)', (name, country, record))
        conn.close()
    except sqlite3.IntegrityError:
        print('error! name already exists')


def edit_existing_record():
    """updates records
    checks if name exists in the database if name in the database it updates the record
    if not displays error message
    """
    name = ui.get_name()
    search_name = search_record(name)
    if search_name:
        new_record = ui.get_new_record()

        with sqlite3.connect(db) as conn:
            conn.execute('UPDATE records SET num_of_catches = ? WHERE name = ?', (new_record, name))
        conn.close()
    else:
        ui.error_message(name)


def delete_record():
    """delets records
    checks if name exists in the database if name in the database it removes
    if not displays error message
    """
    name=ui.get_name()
    name_found = search_record(name)
    if name_found:
        with sqlite3.connect(db) as conn:
            conn.execute('DELETE FROM records WHERE name= ?', (name, ))
        conn.close()
    else:
        ui.error_message(name)


def search_record(name):
    """searches name 
    parameters: name
    returns: none if not in the database or data
    """
    with sqlite3.connect(db) as conn:
        search_name = conn.execute('SELECT * FROM records WHERE name LIKE ?', (name, ))
        name_found=search_name.fetchone()
    conn.close()

    return name_found


if __name__ == '__main__':
    main()