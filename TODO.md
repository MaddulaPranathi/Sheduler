# TODO - Make Sheduler run in the browser

- [ ] Replace the terminal-only scheduler with a Flask backend that:
  - [ ] Serves `app.html` + static assets (`style.css`, `script.js`).
  - [ ] Provides an endpoint `/add_reminder` for the browser UI.
  - [ ] Saves reminders to `reminders.db`.
  - [ ] Schedules notifications.
- [ ] Add browser-visible confirmation messages (fix/complete `script.js`).
- [ ] Fix `script.js` bugs (wrong input property, missing bot message variables).
- [ ] Add a desktop/browser notification strategy:
  - [ ] Use system notifications via `plyer` (works on server machine).
  - [ ] (Optional) Use Web Notifications API for in-browser popups.
- [ ] Update README.md with run instructions.
- [ ] Test end-to-end:
  - [ ] Start server
  - [ ] Open browser
  - [ ] Add reminder
  - [ ] Verify reminder triggers.

