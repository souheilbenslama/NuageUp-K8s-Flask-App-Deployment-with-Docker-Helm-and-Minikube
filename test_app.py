from app import createhello


def test_createhello():
    assert createhello(None) == "Hello World !"
    assert createhello("Alice") == "Hello, Alice!"
    assert createhello("<script>alert('hello')</script>") == "Hello, &lt;script&gt;alert(&#39;hello&#39;)&lt;/script&gt;!"
