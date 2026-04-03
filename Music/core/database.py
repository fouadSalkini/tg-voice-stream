import datetime
import sys

import aiomysql

from config import Config

from .logger import LOGS


class Database(object):
    def __init__(self):
        self.pool = None

        self.active_vc = [{"chat_id": 0, "join_time": 0, "vc_type": "voice"}]
        self.inactive = {}
        self.loop = {}
        self.watcher = {}

    async def _get_conn(self):
        if self.pool is None:
            await self.connect()
        return await self.pool.acquire()

    def _release_conn(self, conn):
        self.pool.release(conn)

    async def connect(self):
        try:
            self.pool = await aiomysql.create_pool(
                host=Config.MYSQL_HOST,
                port=Config.MYSQL_PORT,
                user=Config.MYSQL_USER,
                password=Config.MYSQL_PASSWORD,
                db=Config.MYSQL_DB,
                charset="utf8mb4",
                autocommit=True,
                minsize=1,
                maxsize=10,
            )
            conn = await self._get_conn()
            await conn.ping()
            self._release_conn(conn)
            LOGS.info("\x3e\x3e\x20\x44\x61\x74\x61\x62\x61\x73\x65\x20\x63\x6f\x6e\x6e\x65\x63\x74\x69\x6f\x6e\x20\x73\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x21")
        except Exception as e:
            LOGS.error(f"\x44\x61\x74\x61\x62\x61\x73\x65\x20\x63\x6f\x6e\x6e\x65\x63\x74\x69\x6f\x6e\x20\x66\x61\x69\x6c\x65\x64\x3a\x20\x27{e}\x27")
            sys.exit()

    # users db #
    async def add_user(self, user_id: int, user_name: str):
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute(
                    "INSERT IGNORE INTO users (user_id, user_name, join_date, songs_played) VALUES (%s, %s, %s, %s)",
                    (user_id, user_name, datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), 0),
                )
        finally:
            self._release_conn(conn)

    async def delete_user(self, user_id: int):
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        finally:
            self._release_conn(conn)

    async def is_user_exist(self, user_id: int) -> bool:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("SELECT 1 FROM users WHERE user_id = %s", (user_id,))
                row = await cur.fetchone()
                return row is not None
        finally:
            self._release_conn(conn)

    async def get_user(self, user_id: int):
        conn = await self._get_conn()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
                return await cur.fetchone()
        finally:
            self._release_conn(conn)

    async def get_all_users(self):
        conn = await self._get_conn()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute("SELECT * FROM users")
                return await cur.fetchall()
        finally:
            self._release_conn(conn)

    async def total_users_count(self):
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("SELECT COUNT(*) FROM users")
                row = await cur.fetchone()
                return row[0]
        finally:
            self._release_conn(conn)

    async def update_user(self, user_id: int, key: str, value):
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                if key == "songs_played":
                    await cur.execute(
                        "UPDATE users SET songs_played = songs_played + %s WHERE user_id = %s",
                        (value, user_id),
                    )
                else:
                    await cur.execute(
                        f"UPDATE users SET {key} = %s WHERE user_id = %s",
                        (value, user_id),
                    )
        finally:
            self._release_conn(conn)

    # chat db #
    async def add_chat(self, chat_id: int):
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute(
                    "INSERT IGNORE INTO chats (chat_id, join_date) VALUES (%s, %s)",
                    (chat_id, datetime.datetime.now()),
                )
        finally:
            self._release_conn(conn)

    async def delete_chat(self, chat_id: int):
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("DELETE FROM chats WHERE chat_id = %s", (chat_id,))
        finally:
            self._release_conn(conn)

    async def is_chat_exist(self, chat_id: int) -> bool:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("SELECT 1 FROM chats WHERE chat_id = %s", (chat_id,))
                row = await cur.fetchone()
                return row is not None
        finally:
            self._release_conn(conn)

    async def get_chat(self, chat_id: int):
        conn = await self._get_conn()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute("SELECT * FROM chats WHERE chat_id = %s", (chat_id,))
                return await cur.fetchone()
        finally:
            self._release_conn(conn)

    async def get_all_chats(self):
        conn = await self._get_conn()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute("SELECT * FROM chats")
                return await cur.fetchall()
        finally:
            self._release_conn(conn)

    async def total_chats_count(self):
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("SELECT COUNT(*) FROM chats")
                row = await cur.fetchone()
                return row[0]
        finally:
            self._release_conn(conn)

    # active vc db #
    async def get_active_vc(self) -> list:
        return self.active_vc

    async def add_active_vc(self, chat_id: int, vc_type: str):
        cid = [x["chat_id"] for x in self.active_vc]
        if chat_id not in cid:
            self.active_vc.append(
                {
                    "chat_id": chat_id,
                    "join_time": datetime.datetime.now(),
                    "vc_type": vc_type,
                }
            )

    async def is_active_vc(self, chat_id: int) -> bool:
        cid = [x["chat_id"] for x in self.active_vc]
        return chat_id in cid

    async def remove_active_vc(self, chat_id: int):
        for x in self.active_vc:
            if x["chat_id"] == chat_id:
                self.active_vc.remove(x)

    async def total_actvc_count(self) -> int:
        return len(self.active_vc) - 1

    # autoend db #
    async def get_autoend(self) -> bool:
        try:
            conn = await self._get_conn()
            try:
                async with conn.cursor() as cur:
                    await cur.execute("SELECT enabled FROM autoend WHERE id = 1")
                    row = await cur.fetchone()
                    return bool(row and row[0])
            finally:
                self._release_conn(conn)
        except:
            return False

    async def set_autoend(self, autoend: bool):
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute(
                    "INSERT INTO autoend (id, enabled) VALUES (1, %s) ON DUPLICATE KEY UPDATE enabled = %s",
                    (autoend, autoend),
                )
        finally:
            self._release_conn(conn)

    # loop db #
    async def set_loop(self, chat_id: int, loop: int):
        self.loop[chat_id] = loop

    async def get_loop(self, chat_id: int) -> int:
        return self.loop.get(chat_id) or 0

    # watcher db #
    async def set_watcher(self, chat_id: int, key: str, watch: bool):
        self.watcher[chat_id] = {key: watch}

    async def get_watcher(self, chat_id: int, key: str) -> bool:
        try:
            return self.watcher[chat_id][key]
        except KeyError:
            return False

    # sudousers db #
    async def get_sudo_users(self) -> list:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("SELECT user_id FROM sudo_users")
                rows = await cur.fetchall()
                return [row[0] for row in rows]
        finally:
            self._release_conn(conn)

    async def add_sudo(self, user_id: int) -> bool:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute(
                    "INSERT IGNORE INTO sudo_users (user_id) VALUES (%s)", (user_id,)
                )
        finally:
            self._release_conn(conn)
        return True

    async def remove_sudo(self, user_id: int) -> bool:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("DELETE FROM sudo_users WHERE user_id = %s", (user_id,))
        finally:
            self._release_conn(conn)
        return True

    # blocked users db #
    async def get_blocked_users(self) -> list:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("SELECT user_id FROM blocked_users")
                rows = await cur.fetchall()
                return [row[0] for row in rows]
        finally:
            self._release_conn(conn)

    async def add_blocked_user(self, user_id: int) -> bool:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute(
                    "INSERT IGNORE INTO blocked_users (user_id) VALUES (%s)", (user_id,)
                )
        finally:
            self._release_conn(conn)
        return True

    async def remove_blocked_user(self, user_id: int) -> bool:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("DELETE FROM blocked_users WHERE user_id = %s", (user_id,))
        finally:
            self._release_conn(conn)
        return True

    async def total_block_count(self) -> int:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("SELECT COUNT(*) FROM blocked_users")
                row = await cur.fetchone()
                return row[0]
        finally:
            self._release_conn(conn)

    # gbanned users db #
    async def get_gbanned_users(self) -> list:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("SELECT user_id FROM gban_users")
                rows = await cur.fetchall()
                return [row[0] for row in rows]
        finally:
            self._release_conn(conn)

    async def add_gbanned_user(self, user_id: int) -> bool:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute(
                    "INSERT IGNORE INTO gban_users (user_id) VALUES (%s)", (user_id,)
                )
        finally:
            self._release_conn(conn)
        return True

    async def remove_gbanned_users(self, user_id: int) -> bool:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("DELETE FROM gban_users WHERE user_id = %s", (user_id,))
        finally:
            self._release_conn(conn)
        return True

    async def is_gbanned_user(self, user_id: int) -> bool:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("SELECT 1 FROM gban_users WHERE user_id = %s", (user_id,))
                row = await cur.fetchone()
                return row is not None
        finally:
            self._release_conn(conn)

    async def total_gbans_count(self) -> int:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("SELECT COUNT(*) FROM gban_users")
                row = await cur.fetchone()
                return row[0]
        finally:
            self._release_conn(conn)

    # authusers db #
    async def add_authusers(self, chat_id: int, user_id: int, details: dict):
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute(
                    "INSERT IGNORE INTO auth_users (chat_id, user_id, user_name, auth_by_id, auth_by_name, auth_date) VALUES (%s, %s, %s, %s, %s, %s)",
                    (
                        chat_id,
                        user_id,
                        details.get("user_name", ""),
                        details.get("auth_by_id", 0),
                        details.get("auth_by_name", ""),
                        details.get("auth_date", ""),
                    ),
                )
        finally:
            self._release_conn(conn)

    async def is_authuser(self, chat_id: int, user_id: int) -> bool:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute(
                    "SELECT 1 FROM auth_users WHERE chat_id = %s AND user_id = %s",
                    (chat_id, user_id),
                )
                row = await cur.fetchone()
                return row is not None
        finally:
            self._release_conn(conn)

    async def get_authuser(self, chat_id: int, user_id: int):
        conn = await self._get_conn()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(
                    "SELECT user_name, auth_by_id, auth_by_name, auth_date FROM auth_users WHERE chat_id = %s AND user_id = %s",
                    (chat_id, user_id),
                )
                row = await cur.fetchone()
                if row:
                    return {
                        "user_name": row["user_name"],
                        "auth_by_id": row["auth_by_id"],
                        "auth_by_name": row["auth_by_name"],
                        "auth_date": row["auth_date"],
                    }
                return {}
        finally:
            self._release_conn(conn)

    async def get_all_authusers(self, chat_id: int) -> list:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute(
                    "SELECT user_id FROM auth_users WHERE chat_id = %s", (chat_id,)
                )
                rows = await cur.fetchall()
                return [row[0] for row in rows]
        finally:
            self._release_conn(conn)

    async def remove_authuser(self, chat_id: int, user_id: int):
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute(
                    "DELETE FROM auth_users WHERE chat_id = %s AND user_id = %s",
                    (chat_id, user_id),
                )
        finally:
            self._release_conn(conn)

    # authchats db #
    async def get_authchats(self) -> list:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("SELECT chat_id FROM auth_chats")
                rows = await cur.fetchall()
                return [row[0] for row in rows]
        finally:
            self._release_conn(conn)

    async def add_authchat(self, chat_id: int) -> bool:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute(
                    "INSERT IGNORE INTO auth_chats (chat_id) VALUES (%s)", (chat_id,)
                )
        finally:
            self._release_conn(conn)
        return True

    async def remove_authchat(self, chat_id: int) -> bool:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("DELETE FROM auth_chats WHERE chat_id = %s", (chat_id,))
        finally:
            self._release_conn(conn)
        return True

    async def is_authchat(self, chat_id: int) -> bool:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("SELECT 1 FROM auth_chats WHERE chat_id = %s", (chat_id,))
                row = await cur.fetchone()
                return row is not None
        finally:
            self._release_conn(conn)

    # favorites db #
    async def get_favs(self, user_id: int) -> dict:
        conn = await self._get_conn()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(
                    "SELECT video_id, title, duration, add_date FROM favorites WHERE user_id = %s",
                    (user_id,),
                )
                rows = await cur.fetchall()
                result = {}
                for row in rows:
                    result[row["video_id"]] = {
                        "video_id": row["video_id"],
                        "title": row["title"],
                        "duration": row["duration"],
                        "add_date": row["add_date"],
                    }
                return result
        finally:
            self._release_conn(conn)

    async def add_favorites(self, user_id: int, video_id: str, context: dict):
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute(
                    "INSERT INTO favorites (user_id, video_id, title, duration, add_date) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE title = VALUES(title), duration = VALUES(duration), add_date = VALUES(add_date)",
                    (
                        user_id,
                        video_id,
                        context.get("title", ""),
                        context.get("duration", ""),
                        context.get("add_date", ""),
                    ),
                )
        finally:
            self._release_conn(conn)

    async def rem_favorites(self, user_id: int, video_id: str) -> bool:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute(
                    "DELETE FROM favorites WHERE user_id = %s AND video_id = %s",
                    (user_id, video_id),
                )
                return cur.rowcount > 0
        finally:
            self._release_conn(conn)

    async def get_all_favorites(self, user_id: int) -> list:
        favs = await self.get_favs(user_id)
        return list(favs.keys())

    async def get_favorite(self, user_id: int, video_id: str) -> dict:
        conn = await self._get_conn()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(
                    "SELECT video_id, title, duration, add_date FROM favorites WHERE user_id = %s AND video_id = %s",
                    (user_id, video_id),
                )
                row = await cur.fetchone()
                if row:
                    return dict(row)
                return {}
        finally:
            self._release_conn(conn)

    # songs db #
    async def total_songs_count(self) -> int:
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute("SELECT count FROM songs_counter WHERE id = 1")
                row = await cur.fetchone()
                return row[0] if row else 0
        finally:
            self._release_conn(conn)

    async def update_songs_count(self, count: int):
        conn = await self._get_conn()
        try:
            async with conn.cursor() as cur:
                await cur.execute(
                    "INSERT INTO songs_counter (id, count) VALUES (1, %s) ON DUPLICATE KEY UPDATE count = count + %s",
                    (count, count),
                )
        finally:
            self._release_conn(conn)


db = Database()
