Updating rows:


    UPDATE cities
    SET population = 39505000
    WHERE name = 'Tokyo';


Deleting rows:

    DELETE FROM cities
    WHERE name = 'Tokyo';


Plan Moving forward: working with tables

    database for a photo-sharing app, we will make other databases (users, photos, comments, likes)

    One to many AND many to one relationships
    -> if we see a one to many or a many to one relation ship, the opposite is true ( a photo has many comments OR a user has many pictures)

    many to many AND one to one relationship


Primary key AND Foreign key

    Primary key: Uniquely identifies this record in this table
    Foreign key: identifies a record (usually in another table) that this row is associated with.


We will build a database that contains two tables (photos AND users):

    We strat creating a users table with 'id' AND 'username' column:

    CREATE TABLE users(
        id SERIAL PRIMARY KEY,
                #serial tells pgs to generate a serial id, we put just a username and pgs generates an id
        username VARCHAR(50)
    );

    Now we will insert a  users to this table:

    INSERT INTO users (username)
    VALUES
        ('manahan93'),
        ('pferrer'),
        ('si93onis'),
        ('99stroman');

    Now we will create a photos table AND add a foreign key:

        CREATE TABLE photos(
        id SERIAL PRIMARY KEY,
                #serial tells pgs to generate a serial id, we put just a username and pgs generates an id
        url VARCHAR(200),
        user_id INTEGER REFERENCES users(id)
        );