run:
\tpython main.py

api:
\tuvicorn api:app --reload

test:
\tpytest -q

fmt:
\tblack . && ruff check --fix .
