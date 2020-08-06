def create_table(db):
    cur = db.cursor()
    cur.execute('create table if not exists'
                + ' Contacts(name text, number int)')
    pass


def add_user(db, name, number):
    cur = db.cursor()
    cur.execute('insert into Contacts values(?, ?)'
                , (name, number))
    db.commit()


def update_user_name(db, name, new_name):
    cur = db.cursor()
    cur.execute('update Contacts set name=? where name=?',
                (new_name, name))
    db.commit()


def update_user_number(db, name, new_number):
    cur = db.cursor()
    cur.execute('update Contacts set number=? where name=?',
                (new_number, name))
    db.commit()


def delete_user_by(db, name):
    cur = db.cursor()
    cur.execute('delete from Contacts where name=?',
                (name,))
    db.commit()


def current_db_info(db, flag=0):
    cur = db.cursor()
    if flag == 1:
        cur.execute('select name from Contacts')
        return [name[0] for name in cur.fetchall()]
    elif flag == 2:
        cur.execute('select number from Contacts')
        return [num[0] for num in cur.fetchall()]
    else:
        cur.execute('select * from Contacts')
        return cur.fetchall()

