
import streamlit as st
import sqlite3
from pathlib import Path

__DB_Path = str(Path(__file__).parent.parent.parent / "data.db")


@st.cache_resource
def _get_connection():
    conn = sqlite3.connect(
        __DB_Path,
        check_same_thread=False
    )
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _init_db():
    conn = _get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS exercise (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL REFERENCES user(id),
            exercise_name TEXT NOT NULL,
            reps INTEGER NOT NULL DEFAULT 0,
            sets INTEGER NOT NULL DEFAULT 0,
            time INTEGER NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()


def _get_user(name):
    conn = _get_connection()
    return conn.execute(
        "SELECT * FROM user WHERE name = ?",
        (name,)
    ).fetchone()


def create_user(name):
    conn = _get_connection()

    with conn:
        conn.execute(
            "INSERT INTO user (name) VALUES (?)",
            (name,)
        )

    return _get_user(name)


def get_or_create_user(name):
    user = _get_user(name)

    if user is None:
        user = create_user(name)

    return user


def add_exercise(user_id, exercise_name, reps, sets, time):
    conn = _get_connection()

    existing = conn.execute("""
        SELECT * FROM exercise
        WHERE user_id = ?
          AND exercise_name = ?
          AND DATE(created_at) = DATE('now')
    """, (user_id, exercise_name)).fetchone()

    with conn:
        if existing:
            conn.execute("""
                UPDATE exercise
                SET reps = reps + ?,
                    sets = sets + ?,
                    time = time + ?
                WHERE id = ?
            """, (reps, sets, time, existing["id"]))
        else:
            conn.execute("""
                INSERT INTO exercise
                (user_id, exercise_name, reps, sets, time)
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, exercise_name, reps, sets, time))


def get_users_exercises(user_id):
    conn = _get_connection()

    return conn.execute("""
        SELECT * FROM exercise
        WHERE user_id = ?
        ORDER BY created_at DESC
    """, (user_id,)).fetchall()


def user_get_exercise(user_id):
    return get_users_exercises(user_id)
_init_db()
