from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("sqlite+pysqlite:///:memory:", echo=False)

with engine.connect() as con:
    con.execute(text("create table questions(q varchar, option1 int, option2 int, option3 int)"))
    con.execute(text("insert into questions values(:x, :y, :z, :q)"), [{"x":"what is your name?", "y": "Name", "z":"aram", "q":"mandap"},])
    con.commit()
    res = con.execute(text("select * from questions"))
    print(res.all())