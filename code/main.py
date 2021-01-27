import cmd
import mysql.connector


class CommandProcessor(cmd.Cmd):
    intro = 'Welcome to the library system. Type help or ? to list commands.\n'
    prompt = 'library_system > '

    @staticmethod
    def parse_args(args: str, n: int):
        return [x if x != '*' else None for x in args.split(maxsplit=n)] + \
               [None] * (n - len(args.split(maxsplit=n)))

    def preloop(self) -> None:
        self.connection = mysql.connector.connect(
            host="127.0.0.1",
            user="project_db",
            password="abcd+1234",
            database="library_system_v2"
        )
        self.cursor = self.connection.cursor()

    def postloop(self) -> None:
        self.cursor.close()
        self.connection.close()

    def print_results(self):
        for result in self.cursor.stored_results():
            for title in result.description:
                print(title[0], end=' ')
            print()
            for row in result.fetchall():
                print(*row)

    def postcmd(self, stop: bool, line: str) -> bool:
        self.connection.commit()
        self.print_results()
        return stop

    def do_register(self, args: str):
        """register username password account_type national_id firstname lastname phone_number address"""
        self.cursor.callproc('register', CommandProcessor.parse_args(args, 8))

    def do_login(self, args: str):
        """login username password"""
        self.cursor.callproc('login', CommandProcessor.parse_args(args, 2))

    def do_logout(self, args: str):
        """logout token"""
        self.cursor.callproc('logout', CommandProcessor.parse_args(args, 1))

    def do_get_user_data(self, args: str):
        """get_user_data token username"""
        self.cursor.callproc('get_user_data', CommandProcessor.parse_args(args, 2))

    def do_add_book(self, args: str):
        """add_book token book_id title ed author_name book_type price published_date inventory"""
        self.cursor.callproc('add_book', CommandProcessor.parse_args(args, 9))

    def do_charge_account(self, args: str):
        """charge_account token balance"""
        self.cursor.callproc('charge_account', CommandProcessor.parse_args(args, 2))

    def do_search_book(self, args: str):
        """search_book title ed author publish_date"""
        self.cursor.callproc('search_book', CommandProcessor.parse_args(args, 4))

    def do_borrow_book(self, args: str):
        """borrow_book token book_id"""
        self.cursor.callproc('borrow_book', CommandProcessor.parse_args(args, 2))

    def do_return_book(self, args: str):
        """return_book token book_id"""
        self.cursor.callproc('return_book', CommandProcessor.parse_args(args, 2))

    def do_delete_user(self, args: str):
        """delete_user token username"""
        self.cursor.callproc('delete_user', CommandProcessor.parse_args(args, 2))

    def do_view_accepted_requests(self, args: str):
        """view_accepted_requests token page_number"""
        self.cursor.callproc('view_accepted_requests', CommandProcessor.parse_args(args, 2))

    def do_search_users(self, args: str):
        """search_users token username lastname page_number"""
        self.cursor.callproc('search_users', CommandProcessor.parse_args(args, 4))

    def do_view_user_requests(self, args: str):
        """view_user_requests token username"""
        self.cursor.callproc('view_user_requests', CommandProcessor.parse_args(args, 2))

    def do_book_history(self, args: str):
        """view_user_requests token book_id"""
        self.cursor.callproc('book_history', CommandProcessor.parse_args(args, 2))

    def do_get_delayed_books(self, args: str):
        """get_delayed_books token"""
        self.cursor.callproc('get_delayed_books', CommandProcessor.parse_args(args, 1))

    def do_quit(self, arg):
        """quit from program"""
        print('Bye!')
        return True


def main():
    CommandProcessor().cmdloop()


if __name__ == '__main__':
    main()
