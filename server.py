from __future__ import annotations

import threading
import time
from typing import Any

import schedule
from flask import Flask, jsonify, request, send_from_directory

from chatbot import parse_input
from db import init_db, add_reminder


def create_app() -> Flask:
    app = Flask(__name__, static_folder=".")

    init_db()

    # Store reminders in memory so frontend can fetch them
    reminders: list[str] = []

    def remind(task: str) -> None:
        print(f"⏰ Reminder triggered: {task}")
        reminders.append(task)

    def scheduler_loop() -> None:
        while True:
            try:
                schedule.run_pending()
            except Exception as e:
                print("Scheduler loop error:", e)
            time.sleep(1)

    # Start scheduler loop once
    t = threading.Thread(target=scheduler_loop, daemon=True)
    t.start()

    @app.get("/")
    def index():
        # Serve your index.html
        return send_from_directory(app.root_path, "index.html")

    @app.post("/add_reminder")
    def add_reminder_endpoint():
        data: dict[str, Any] = request.get_json(silent=True) or {}
        user_text = str(data.get("task", "")).strip()
        time_str = str(data.get("time", "")).strip()

        if not time_str:
            task, parsed_time = parse_input(user_text)
        else:
            task, parsed_time = user_text, time_str

        if not task or not parsed_time:
            return jsonify({"ok": False, "error": "Invalid format. Use: task and time=HH:MM"}), 400

        add_reminder(task, parsed_time)
        schedule.every().day.at(parsed_time).do(remind, task)
        print(f"BOT: Reminder saved for '{task} at {parsed_time}'")

        return jsonify({"ok": True, "task": task, "time": parsed_time})

    @app.get("/get_reminders")
    def get_reminders():
        # Frontend can poll this to show notifications
        return jsonify(reminders)

    @app.get("/style.css")
    def style_css():
        return send_from_directory(app.root_path, "style.css")

    @app.get("/script.js")
    def script_js():
        return send_from_directory(app.root_path, "script.js")

    return app


# Expose app for Gunicorn
app = create_app()

if __name__ == "__main__":
    # Local testing
    app.run(host="127.0.0.1", port=5000, debug=True)
