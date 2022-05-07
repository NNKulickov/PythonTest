from module_print import print_hi

def test_print(capfd):
    print_hi("T")
    out, err = capfd.readouterr()
    assert out == "Hi, T\n"