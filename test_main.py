import pytest

from cr2 import app

@pytest.fixture
def client():
    #app.testing = True
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

#@pytest.mark.parametrize("test_input", "expected", [
#    ({'a': 3, 'b': 4}, 
#])

@pytest.mark.parametrize("a", [x for x in range(5)])
@pytest.mark.parametrize("b", [x for x in range(5, 10)])
def test_add(client, a, b):
    rv = client.get(f'/add?a={a}&b={b}')
    rv = rv.data.decode()
    print(f"\n{a}+{b}: {rv}\n")
    assert rv==str(float(a+b))

@pytest.mark.parametrize("a", [x for x in range(5)])
@pytest.mark.parametrize("b", [x for x in range(5, 10)])
def test_sub(client, a, b):
    rv = client.get(f'/sub?a={a}&b={b}')
    rv = rv.data.decode()
    print(f"\n{a}-{b}: {rv}\n")
    assert rv==str(float(a-b))

@pytest.mark.parametrize("a", [x for x in range(5)])
@pytest.mark.parametrize("b", [x for x in range(5, 10)])
def test_mult(client, a, b):
    rv = client.get(f'/mult?a={a}&b={b}')
    rv = rv.data.decode()
    print(f"\n{a}*{b}: {rv}\n")
    assert rv==str(float(a*b))

@pytest.mark.parametrize("a", [x for x in range(5, 10)])
@pytest.mark.parametrize("b", [x for x in range(5)])
def test_div(client, a, b):
    rv = client.get(f'/div?a={a}&b={b}')
    rv = rv.data.decode()
    if b==0:
        assert rv=="Error: Cannot divide by zero"
    else:
        print(f"\n{a}/{b}: {rv}\n")
        assert rv==str(float(a/b))
