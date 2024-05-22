# Reflex Mypy Example
This is a minimal example to show how normal, by-the-docs Reflex code causes Mypy to fail.

## How to reproduce
1. Clone this repository 
`git clone 
2. Create & activate a virtual environment
`python3 -m venv venv; source ./venv/bin/activate`
3. Install the requirements
`pip install -r requirements.txt`
4. Init Reflex
`reflex init`
5. Confirm Reflex is running as intended
`reflex run`  (And load page at `http://localhost:3000` to see the Reflex app running)
6. Run Mypy
`mypy .`
7. Observe the error Mypy flags
```shell
(venv) [ reflex_mypy  $] mypy .
rxconfig.py:1: error: Skipping analyzing "reflex": module is installed, but missing library stubs or py.typed marker  [import-untyped]
reflex_mypy/reflex_mypy.py:1: error: Skipping analyzing "reflex": module is installed, but missing library stubs or py.typed marker  [import-untyped]
reflex_mypy/reflex_mypy.py:1: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
reflex_mypy/reflex_mypy.py:24: error: Missing positional argument "arg" in call to "increment_by" of "State"  [call-arg]
reflex_mypy/reflex_mypy.py:24: error: Argument 1 to "increment_by" of "State" has incompatible type "int"; expected "State"  [arg-type]
```


The usage on line 24 of `reflex_mypy.py` is as follows:
```python
            rx.button(State.counter_message, on_click=lambda: State.increment_by(1)),
```
This breaks normal Python expectations, where we would usually either expect the 
`State.increment_by()` to be noted as a `staticmethod` or `classmethod` or to 
be called on an *instance* of `State` rather than the class itself. 
Reflex doesn't do this, so Mypy flags it as an error.