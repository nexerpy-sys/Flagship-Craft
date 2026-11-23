# Task Mode Adapter (Backend Craft)

- Probe available runtimes (`python3`, `node`, `sqlite3`, etc.) in the offline sandbox first.
- Build the thinnest end-to-end slice and run a real test against it before adding breadth.
- Provoke at least one failure mode from the frame (bad input, duplicate request, missing record) and observe the real error response.
