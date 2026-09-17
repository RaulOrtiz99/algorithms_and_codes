from exercises.numeros_enteros import par, impar


def test_par():
    assert par(0) is True
    assert par(2) is True
    assert par(-4) is True
    assert par(100) is True
    assert par(1) is False
    assert par(-3) is False


def test_impar():
    assert impar(1) is True
    assert impar(-3) is True
    assert impar(99) is True
    assert impar(0) is False
    assert impar(2) is False
    assert impar(-4) is False
