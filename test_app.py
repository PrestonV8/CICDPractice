# The runner file to run "app.py"
from app import add

def test_add():
    assert add(2, 3) == 6 # intentially supposed to fail to test CI/CD pipeline.
