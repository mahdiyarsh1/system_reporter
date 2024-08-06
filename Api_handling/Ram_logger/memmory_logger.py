import time
import psutil
from datetime import datetime


class MemoryLogger():
    def log_memory_data(self,connection,cursur):
        try:
            memory_info = psutil.virtual_memory()
            timestamp = int(time.time())
            total = memory_info.total // 1024 // 1024  # byte to megabyte
            free = memory_info.available // 1024 // 1024
            used = total - free
            cursur.execute(
                """
                INSERT INTO memory (timestamp, total, free, used) VALUES (?, ?, ?, ?) 
            """,
                (timestamp, total, free, used),
            )
            connection.commit()
            print(f"Logged memory data at {datetime.fromtimestamp(timestamp)}")
        except Exception as e:
            print(f"Error logging memory data: {e}")


# Usage example
