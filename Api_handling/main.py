from fastapi import FastAPI, Query
import sqlite3
from Database_manager.create_database import create_table
from Ram_logger.memmory_logger import MemoryLogger
import time

app = FastAPI()  # create object from FastAPI
create_table()

class ApiHandling():
    def get_memory_data(self, n: int):
        conn = sqlite3.connect("memory_data.db")
        c = conn.cursor()
        try:
            c.execute(
                """
                SELECT timestamp, total, free, used FROM memory ORDER BY id DESC LIMIT ?
            """,
                (n,),
            )
            rows = c.fetchall()
            result = []
            for item in rows:
                data = {
                    "timestamp": item[0],
                    "total": item[1],
                    "free": item[2],
                    "used": item[3],
                }
                result.append(data)
            return result
        except Exception as e:
            print(f"Error fetching memory data: {e}")
            return []


# Create an instance of ApiHandling
api_handler = ApiHandling()


@app.get("/memory")
def read_memory_data(
    limit: int = Query(10, description="Number of recent records to retrieve")
):
    return api_handler.get_memory_data(limit)


@app.get("/get-log")
def read_memory_data():
    a = MemoryLogger()
    conn = sqlite3.connect("memory_data.db")
    c = conn.cursor()
    while True:
        a.log_memory_data(conn,c)
        time.sleep(30)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
