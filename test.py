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
    tests = [test_basic, test_addition, test_string]
    failed = []
    
    for test in tests:
        try:
            test()
            print(f"✓ {test.__name__} passed")
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed.append(test.__name__)
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed.append(test.__name__)
    
    if failed:
        print(f"\n{len(failed)} test(s) failed: {', '.join(failed)}")
        exit(1)
    else:
        print("\nAll tests passed!")
