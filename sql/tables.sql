
CREATE TABLE person (
    username VARCHAR(64),
    pw CHAR(255) NOT NULL,
    account_type VARCHAR(16),
    national_id VARCHAR(16) UNIQUE,
    firstname VARCHAR(16),
    lastname VARCHAR(16),
    phone_number VARCHAR(16),
    address VARCHAR(64),
    balance NUMERIC(9 , 0 ) DEFAULT 0,
    account_created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (username),
    CHECK (account_type IN ('student' , 'professor', 'library_admin', 'librarian', 'other'))
);

CREATE TABLE login (
    username VARCHAR(64),
    token CHAR(255) UNIQUE NOT NULL,
    login_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (username),
	FOREIGN KEY (username)
        REFERENCES person (username) ON DELETE CASCADE
);

CREATE TABLE book (
    book_id VARCHAR(16),
    title VARCHAR(64),
    editation NUMERIC(2, 0 ),
    author_name VARCHAR(256),
    book_type VARCHAR(64),
    price NUMERIC(9 , 0 ) not null,
    published_date DATE,
    inventory NUMERIC(3, 0 ) default 0,
    PRIMARY KEY (book_id)
);

CREATE TABLE borrow (
    borrow_id INT AUTO_INCREMENT,
    username VARCHAR(64),
    book_id VARCHAR(16),
    state VARCHAR(16),
	price NUMERIC(9 , 0 ),
    borrowing_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    returned_date TIMESTAMP DEFAULT NULL,
    PRIMARY KEY (borrow_id),
    FOREIGN KEY (username)
        REFERENCES person (username) ON DELETE CASCADE,
    FOREIGN KEY (book_id)
        REFERENCES book (book_id ),
	CHECK (state IN ('borrowed' , 'returned', 'not_enough', 'already_have',
					'unavailable', 'access_denied', 'deprived'))
);

