from database.initialization import initialization


class testCase(initialization):
    def select_fun_case(self, case_name=None):
        if case_name is None:
            self.cursor.execute("select * from functional where status=0")
        else:
            self.cursor.execute(f"select * from functional where case_name={case_name} and status=0")
        response = self.cursor.fetchall()
        return response

    def delete_fun_case(self, case_name, status):
        try:
            self.cursor.execute(f"update functional set status={status} where case_name={case_name}")
            self.db.commit()
            return True
        except Exception as e:
            print(str(e))
            self.db.rollback()
            return False

    def insert_fun_case(self, case_name, case_step, case_expected):
        pass
