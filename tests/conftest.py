"""
conftest.py
Allow test to be run in a certain order.

"""

def pytest_collection_modifyitems(items):
    """Modifies test items in place to ensure test modules run in a given order."""
    MODULE_ORDER = ["test_main.test_main_root"
                    ,"test_main.test_sub_root"
                    ]
    module_mapping = {item: item.module.__name__ for item in items}

    sorted_items = items[:]
    # Iteratively move tests of each module to the end of the test queue
    for module in MODULE_ORDER:
        sorted_items = [it for it in sorted_items if module_mapping[it] != module] + [
            it for it in sorted_items if module_mapping[it] == module
        ]
    items[:] = sorted_items
    pass
