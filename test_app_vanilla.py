from app import api


def test(test_name, function_result, expected):
    result: bool = function_result == expected


    if result == True:
        print(f"{test_name}: ✅")
    else:
        print(f"{test_name}: 🛑", end="\n")
        print(f"function_result: {function_result}", end="\n")
        print(f"expected: {expected}", end="\n")


api = api()
api["POST"](1)

test(
    test_name="Should GET",
    function_result=api["GET"](),
    expected={
        "code": 200,
        "data": [1],
    },
)

test(
    test_name="Should POST",
    function_result=api["POST"](2),
    expected={
        "code": 201,
        "data": [1, 2],
    },
)

test(
    test_name="Should POST and get an error",
    function_result=api["POST"](2),
    expected={
        "code": 500,
        "error": "2 already exists",
    },
)
