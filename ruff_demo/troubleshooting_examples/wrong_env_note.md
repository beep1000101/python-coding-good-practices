# Wrong Python Environment

**Symptom:**  
VS Code shows no linting or formatting, no errors.

**Likely cause:**  
VS Code is using a different Python interpreter than the one where Ruff is installed.

Check your interpreter in the bottom-right of VS Code.

To see where Ruff is installed, run:

```bash
which python
python -m pip show ruff
```

Switch VS Code to the correct interpreter if needed.
