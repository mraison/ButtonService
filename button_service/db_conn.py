from cassandra.cluster import Cluster


class SQLRequest:
    def __init__(self, sql: str, args):
        self.sql = sql
        self.args = args


class InsertIntoButtonStatusTbl(SQLRequest):
    def __init__(self, state, change_time):
        sql = """
            INSERT INTO panicbutton.statetbl (
                id,
                state,
                change_time
            ) VALUES (uuid(), %s, %s)
        """
        args = [state, change_time]
        super().__init__(sql, args)


class DBConnection:
    def execute(self, req: SQLRequest):
        pass


class CassandraConnection(DBConnection):
    def __init__(self, ip='localhost', port=9042):
        self.cluster = Cluster([ip], port=port)
        self.session = self.cluster.connect()

    def execute(self, req: SQLRequest):
        return self.session.execute(req.sql, req.args)
