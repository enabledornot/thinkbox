import psycopg2.pool


class database:
    def __init__(self,cred_file):
        with open(cred_file,"r") as f:
            data = f.read().split("\n")
        cred = {}
        for line in data:
            split = line.split("=")
            cred[split[0]] = split[1]
        self.config = cred
        self.pool = psycopg2.pool.ThreadedConnectionPool(
            minconn=1,
            maxconn=5,
            host=cred["POSTGRES_HOST"],
            database=cred["POSTGRES_DB"],
            user=cred["POSTGRES_USER"],
            password=cred["POSTGRES_PASSWORD"],
            port=cred["PORT"]
        )
    def init_db(self):
        with open("init.sql","r") as f:
            init_command = f.read()
        conn = self.pool.getconn()
        with conn.cursor() as cursor:
            cursor.execute(init_command)
        conn.commit()
        self.pool.putconn(conn)
    def get_comments(self):
        conn = self.pool.getconn()
        with conn.cursor() as cursor:
            command_tz = "set timezone TO '{}'".format(self.config["TZ"])
            cursor.execute(command_tz)
            command = "SELECT author,time,text FROM comments ORDER BY time DESC"
            cursor.execute(command)
            rows = cursor.fetchall()
        self.pool.putconn(conn)
        comments = []
        for row in rows:
            comments.append({
                "author":row[0],
                "time":row[1].strftime('%B %d, %Y %I:%M %p'),
                "comment":row[2]
            })
        return comments
    def add_comment(self,author,body):
        conn = self.pool.getconn()
        with conn.cursor() as cursor:
            command_tz = "set timezone TO '{}'".format(self.config["TZ"])
            cursor.execute(command_tz)
            command = "INSERT INTO comments (author, time, text) VALUES (%s, CURRENT_TIMESTAMP, %s)"
            cursor.execute(command,(author,body))
        conn.commit()
        self.pool.putconn(conn)
db = database(".env")