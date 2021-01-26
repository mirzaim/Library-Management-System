

DELIMITER $$
CREATE procedure register (
	username VARCHAR(64),
    pw VARCHAR(255),
    account_type VARCHAR(16),
    national_id VARCHAR(16),
    firstname VARCHAR(16),
    lastname VARCHAR(16),
    phone_number VARCHAR(16),
    address VARCHAR(64))
BEGIN
	INSERT INTO person(username, pw, account_type, national_id, firstname, lastname, phone_number, address) 
		VALUES (username, SHA2(pw, 256), account_type, national_id, firstname, lastname, phone_number, address);
	SELECT 'sucsess';
END; $$

DELIMITER $$
CREATE procedure login (
	uname VARCHAR(64),
    pword VARCHAR(255))
BEGIN
	IF exists(select pw from person where username = uname and pw = SHA2(pword, 256)) THEN 
		IF not exists(select uname from login where username = uname) THEN
			INSERT INTO login(username, token)
				values (uname, SHA2(concat(uname, SHA2(pword, 256), CURRENT_TIMESTAMP), 256));
        END IF;
		SELECT token from login where username = uname;
    ELSE
		SELECT 'failure';
	END IF;
END; $$

DELIMITER $$
CREATE procedure logout(tk CHAR(255))
BEGIN
	IF exists(select * from login where token = tk) THEN 
		DELETE from login where token = tk;
        SELECT 'loged out.';
	END IF;
END; $$

DELIMITER $$
CREATE procedure get_user_data(tk CHAR(255), username VARCHAR(64))
BEGIN
	if username is not null and exists(select * from person where person.username = auth(tk) and
									person.account_type in ('library_admin', 'librarian')) then
		select * from person where person.username = username;
	else
		select * from person where person.username = auth(tk);
    end if;
END; $$

DELIMITER $$
CREATE procedure add_book(
	tk CHAR(255),
    book_id VARCHAR(16),
    title VARCHAR(64),
    editation NUMERIC(2, 0 ),
    author_name VARCHAR(256),
    book_type VARCHAR(64),
    price NUMERIC(9 , 0 ),
    published_date DATE,
    inventory NUMERIC(3, 0 ))
BEGIN
	IF exists(select * from person where username = auth(tk) and
				(account_type in ('library_admin','librarian'))) THEN 
		IF exists(select * from book where book.book_id = book_id) THEN
			update book set book.inventory = book.inventory + inventory where book.book_id = book_id;
        ELSE
			INSERT INTO book values (book_id, title, editation,
						author_name, book_type, price, published_date, inventory);
        END IF;
		
        select 'success';
	END IF;
END; $$

DELIMITER $$
CREATE procedure search_book(
    tit VARCHAR(64),
    ed NUMERIC(2, 0 ),
    auth_n VARCHAR(256),
    pub_date DATE)
BEGIN
	select * from book where (tit is null or (title like concat('%', tit, '%'))) and
							 (ed is null or editation = ed) and
							 (auth_n is null or (author_name like concat('%', auth_n, '%'))) and
							 (pub_date is null or published_date = pub_date);
END; $$

DELIMITER $$
CREATE procedure charge_account(
	tk CHAR(255),
    bl NUMERIC(9 , 0 ))
BEGIN
	IF exists(select * from person where username = auth(tk)) and bl >= 0 THEN 
		update person set balance = balance + bl where username = auth(tk);
        select 'success';
	END IF;
END; $$

DELIMITER $$
CREATE procedure borrow_book(
	tk CHAR(255),
    book_id VARCHAR(16))
BEGIN
	 DECLARE account_type VARCHAR(16);
	 DECLARE book_type VARCHAR(64);
     DECLARE book_price NUMERIC(9 , 0 );
     DECLARE result VARCHAR(16);
     select person.account_type into account_type from person where username = auth(tk);
     select book.book_type, book.price into book_type, book_price from book where book.book_id = book_id;
	IF account_type is not null AND book_type is not null THEN 
		IF not (account_type = 'professor' or (account_type = 'student' and book_type != 'reference') or 
		       (book_type not in  ('reference', 'textbook'))) THEN
			set result = 'access_denied';
		elseif exists(select * from borrow where username = auth(tk) and
					borrow.book_id = book_id and borrow.state = 'borrowed') then
			set result = 'already_have';
		elseif not exists(select * from book where book.book_id = book_id and book.inventory > 0) then
			set result = 'unavailable';
		elseif not exists(select * from person where username = auth(tk) and 0.05 * book_price <= balance) then
			set result = 'not_enough';
-- 		elseif () then
-- 			et result = 'deprived';
		else
			set result = 'borrowed';
            update book set inventory = inventory - 1 where book.book_id = book_id;
            update person set balance = balance - 0.05 * book_price where person.username = auth(tk);
		END IF;
		INSERT INTO borrow(username, book_id, state, price) values
							(auth(tk), book_id, result, 0.05 * book_price);
        select result;
	ELSE
		select 'falure';
	END IF;
END; $$

DELIMITER $$
CREATE procedure return_book(
	tk CHAR(255),
    book_id VARCHAR(16))
BEGIN
	IF exists(select * from person where username = auth(tk)) and 
	   exists(select * from borrow where borrow.username = auth(tk) and
				borrow.book_id = book_id and state = 'borrowed') THEN 
		update borrow set state = 'returned', returned_date = now() where username = auth(tk) and
											  borrow.book_id = book_id and state = 'borrowed';
		update book set inventory = inventory + 1 where book.book_id = book_id;
        select 'book returned.';
	else
		select 'failure.';
	END IF;
END; $$

DELIMITER $$
CREATE procedure delete_user(
	tk CHAR(255),
    username VARCHAR(64))
BEGIN
	IF exists(select * from person where person.username = auth(tk) and account_type = 'library_admin') THEN
		IF not exists(select * from borrow where borrow.username = username and state = 'borrowed') THEN
			delete from person where person.username = username;
			select 'user deleted';
		else
			select 'user already borrowed book(s).';
        END IF;
	else
		select 'failure.';
	END IF;
END; $$

DELIMITER $$
CREATE procedure view_accepted_requests(
	tk CHAR(255),
    page_number INT)
BEGIN
	declare p INT;
    set p = 5*(page_number - 1);
	IF exists(select * from person where username = auth(tk) and
				account_type in ('library_admin', 'librarian')) THEN 
        select * from borrow where state = 'borrowed' order by borrowing_date desc limit p, 5;
	else
		select 'access denied';
	END IF;
END; $$

DELIMITER $$
CREATE procedure search_users(
	tk CHAR(255),
    username VARCHAR(64),
    lastname VARCHAR(16),
    page_number INT)
BEGIN
	declare p INT;
    set p = 5*(page_number - 1);
	IF exists(select * from person where person.username = auth(tk) and
				person.account_type in ('library_admin', 'librarian')) THEN 
        select * from person where (username is null or person.username = username) and
				(lastname is null or person.lastname like concat('%', lastname, '%'))
                order by person.lastname limit p, 5;
	else
		select 'access denied';
	END IF;
END; $$

DELIMITER $$
CREATE procedure view_user_requests(
	tk CHAR(255),
    username VARCHAR(64))
BEGIN
	IF exists(select * from person where person.username = auth(tk) and
				person.account_type in ('library_admin', 'librarian')) THEN 
        select * from borrow where borrow.username = username order by borrowing_date desc;
	else
		select 'access denied';
	END IF;
END; $$

DELIMITER $$
CREATE function auth(tk CHAR(255))
returns VARCHAR(64)
READS SQL DATA
BEGIN
	DECLARE uname VARCHAR(64);
    select username into uname from login where token = tk;
    return uname;
END; $$

