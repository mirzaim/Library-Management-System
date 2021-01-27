from mysql.connector import MySQLConnection, Error
import mysql.connector
import datetime


def register_test():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="mor",
            password="abcd1234",
            database="library_system_v2"
        )
        cursor = conn.cursor()

        args = ('morteza120', 'abcd', 'student', '9731064', 'morteza', 'mirzai', '09123123123', 'there')
        result_args = cursor.callproc('register', args)
        conn.commit()

        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def login_test():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="mor",
            password="abcd1234",
            database="library_system_v2"
        )
        cursor = conn.cursor()

        args = ('librarian1', 'abcd')
        result_args = cursor.callproc('login', args)
        conn.commit()

        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def auth_test():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="mor",
            password="abcd1234",
            database="library_system_v2"
        )
        cursor = conn.cursor(buffered=True)
        token = '79e20708c3ce1a1a8395db967f897659ed0d5e0e32e83248283176fa19291c5a'
        result_args = cursor.execute(f"select auth('{token}');")
        conn.commit()

        for result in cursor.fetchall():
            print(result)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def logout_test():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="mor",
            password="abcd1234",
            database="library_system_v2"
        )
        cursor = conn.cursor(buffered=True)
        token = '79e20708c3ce1a1a8395db967f897659ed0d5e0e32e83248283176fa19291c5a'
        result_args = cursor.callproc('logout', (token,))
        conn.commit()

        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def get_acount_details_test():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="mor",
            password="abcd1234",
            database="library_system_v2"
        )
        cursor = conn.cursor()

        token = '9bf27fba934f8c56b26ff378da51679e3cd456bf45f423517dfc53ce0d09333f'
        result_args = cursor.callproc('get_user_data', (token, 'morteza120'))
        conn.commit()

        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def register_test2():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="mor",
            password="abcd1234",
            database="library_system_v2"
        )
        cursor = conn.cursor()

        args = ('moein', 'abcd', 'other', '250', 'moein', 'mirzai', '09XXXXXXXX', 'there')
        result_args = cursor.callproc('register', args)
        conn.commit()

        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def add_book_test():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="mor",
            password="abcd1234",
            database="library_system_v2"
        )
        cursor = conn.cursor()

        # args = ('a03415c992dee642404e6b4dab230a4f7aca9f6f1fc805f7a8f221c8914a96ec',
        #         'efg20', '1001 shab','1', 'X', 'children', '100000', None, '3')
        # args = ('a03415c992dee642404e6b4dab230a4f7aca9f6f1fc805f7a8f221c8914a96ec',
        #         'au320', 'Database System Concepts', '7', 'Avi Silberschatz', 'textbook',
        #         '80000', datetime.datetime.now(), '1')
        args = ('a03415c992dee642404e6b4dab230a4f7aca9f6f1fc805f7a8f221c8914a96ec',
                'uys98', 'Modern Plumbing', '8', 'E. Keith Blankenbaker', 'reference',
                '200000', datetime.datetime.now(), '2')
        result_args = cursor.callproc('add_book', args)
        conn.commit()

        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def charge_account_test():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="mor",
            password="abcd1234",
            database="library_system_v2"
        )
        cursor = conn.cursor()

        args = ('79e20708c3ce1a1a8395db967f897659ed0d5e0e32e83248283176fa19291c5a', '100000')
        result_args = cursor.callproc('charge_account', args)
        conn.commit()

        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def search_book_test():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="mor",
            password="abcd1234",
            database="library_system_v2"
        )
        cursor = conn.cursor()

        args = (None, None, 'Silberschatz', None)
        result_args = cursor.callproc('search_book', args)
        conn.commit()

        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def borrow_book_test():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="mor",
            password="abcd1234",
            database="library_system_v2"
        )
        cursor = conn.cursor()

        args = ('9c9d8ac62e89d598cfe25e5d3de5911a9bde3c8981f6e9ba3768e48cd975583e',
                'efg20')
        result_args = cursor.callproc('borrow_book', args)
        conn.commit()

        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def return_book_test():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="mor",
            password="abcd1234",
            database="library_system_v2"
        )
        cursor = conn.cursor()

        args = ('df382cee1b435dac949e96024a0e4a9c08407120ffda39905a4120a5a49a416c',
                'efg20')
        result_args = cursor.callproc('return_book', args)
        conn.commit()

        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def delete_user_test():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="mor",
            password="abcd1234",
            database="library_system_v2"
        )
        cursor = conn.cursor()

        args = ('9bf27fba934f8c56b26ff378da51679e3cd456bf45f423517dfc53ce0d09333f',
                'moein')
        result_args = cursor.callproc('delete_user', args)
        conn.commit()

        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def view_accepted_requests_test():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="mor",
            password="abcd1234",
            database="library_system_v2"
        )
        cursor = conn.cursor()

        args = ('9bf27fba934f8c56b26ff378da51679e3cd456bf45f423517dfc53ce0d09333f',
                1)
        result_args = cursor.callproc('view_accepted_requests', args)
        conn.commit()

        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def search_users_test():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="mor",
            password="abcd1234",
            database="library_system_v2"
        )
        cursor = conn.cursor()

        args = ('9bf27fba934f8c56b26ff378da51679e3cd456bf45f423517dfc53ce0d09333f',
                None, 'mirzai', 1)
        result_args = cursor.callproc('search_users', args)
        conn.commit()

        for result in cursor.stored_results():
            print(result.fetchall())

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def view_user_requests_test():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="mor",
            password="abcd1234",
            database="library_system_v2"
        )
        cursor = conn.cursor()

        args = ('9bf27fba934f8c56b26ff378da51679e3cd456bf45f423517dfc53ce0d09333f',
                'moein')
        result_args = cursor.callproc('view_user_requests', args)
        conn.commit()

        for result in cursor.stored_results():
            for x in result.fetchall():
                print(x)
            print('#' * 50)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def main():
    get_acount_details_test()


if __name__ == '__main__':
    main()
