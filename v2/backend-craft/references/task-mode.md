# Task Mode Adapter (Backend Craft)

In **Gemini Task Mode**, you have an **offline Linux sandbox** (zero internet, zero `pip`/`npm`/`apt` installs) to build, test, and scan backend code deterministically.

## Execution Rules
1. **Probe Runtimes First**: Check pre-installed binaries (`python3 --version`, `node --version`, `sqlite3 --version`) before writing code.
2. **Thin-Slice + Failure Provocation**: Build one vertical slice and run real tests that provoke at least one failure mode (bad input, concurrent double-submit, missing record).
3. **Mandatory Security Scan**: Run `python3 scripts/security_scan.py <target_dir_or_file>` in the sandbox and resolve any `[HARDCODED_SECRET]`, `[UNSAFE_SHELL]`, `[SQL_INTERPOLATION]`, or `[EVAL_EXEC]` findings before reporting done.
