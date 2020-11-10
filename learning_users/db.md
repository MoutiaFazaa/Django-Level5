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

    Now we will insert values in photos table:

        INSERT INTO photos(url, user_id)
        VALUES
        (
            ('hhtp://one.jpeg', 4),
            ('hhtp://two.jpeg', 1),
            ('hhtp://25.jpeg', 1),
            ('hhtp://36.jpeg', 1),
            ('hhtp://754.jpeg', 2),
            ('hhtp://35.jpeg', 3),
            ('hhtp://256.jpeg', 4)
        );

    Running queries on associated data:

        SELECT * FROM photos WHERE user_id = 4;

        using JOIN:
        SELECT * FROM photos 
        JOIN users ON users.id = photos.user_id;

Constraints around deletion:

    ON Delete Option:
    1- ON DELETE RESTRICT = THROW AN ERROR
    2- ON DELETE NO ACTION = THROW AN ERROR
    3- ON DELETE CASCADE = DELETE THE PHOTO TOO!
    4- ON DELETE SET NULL = SET THE "user_id" OF THE PHOTO TO "NULL"
    5- ON DELETE SET DEFAULT = SET "user_id" OF THE PHOTO TO A DEFAULT VALUE, IF ONE IS PROVIDED


    to configure our delete parameter see exemple:
     **On delete cascade:
        CREATE TABLE photos(
        id SERIAL PRIMARY KEY,
                #serial tells pgs to generate a serial id, we put just a username and pgs generates an id
        url VARCHAR(200),
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
        );

     **on delete set null:

        CREATE TABLE photos(
        id SERIAL PRIMARY KEY,
                #serial tells pgs to generate a serial id, we put just a username and pgs generates an id
        url VARCHAR(200),
        user_id INTEGER REFERENCES users(id) ON DELETE SET NULL
        );


Now we will add a table called comments that will have a relationship with users and photos:

    JOINS: 1- produces values by mergin together rows from different related tables
           2- Use a join most times that you're asked to find data that involves multiple resources

    AGGREGATION: 1- Looks at many rows and calculates a single value
                 2- Words like 'most', 'average', 'least' are a sign that you need to use an aggregation