"""
Simple test file for ReZlack repository
"""


def test_basic():
    """Basic test to verify testing infrastructure works"""
    assert True


def test_addition():
    """Test basic arithmetic"""
    assert 1 + 1 == 2


def test_string():
    """Test string operations"""
    assert "ReZlack".lower() == "rezlack"


if __name__ == "__main__":
    print("Running tests...")
    test_basic()
    print("✓ test_basic passed")
    test_addition()
    print("✓ test_addition passed")
    test_string()
    print("✓ test_string passed")
    print("\nAll tests passed!")
