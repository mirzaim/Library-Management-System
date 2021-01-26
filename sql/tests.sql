
INSERT INTO person(username, pw, account_type, national_id) VALUES ('morteza120', 'abcd', 'student', '9731064');

SELECT 'sucsess';

call register('morteza120', 'abcd', 'student', '9731064', 'morteza', 'mirzai', '09123123123', 'there');

select auth('1eb9acbdce853751abca2c5763dda2c828b86bc3e3ca52b045d311f1c7ee9304');