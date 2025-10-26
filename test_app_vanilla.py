from app import api, ProductIn


def assertTrue(test_name, function_result, expected):
    result: bool = function_result == expected

    if result == True:
        print(f"{test_name}: ✅")
    else:
        print(f"{test_name}: 🛑", end="\n")
        print(f"function_result: {function_result}", end="\n")
        print(f"expected: {expected}", end="\n")


def test_get():
    print("GET ALL:")
    client = api()
    result = client["GET"]()

    assertTrue(
        test_name="GET ALL - Status code is 200",
        function_result=result["code"],
        expected=200,
    )
    assertTrue(
        test_name="GET ALL - Data has items",
        function_result=len(result["data"]),
        expected=1,
    )


test_get()


def test_post():
    print("POST:")
    client = api()
    product = ProductIn(
        name="Procut 2",
        price=100,
        category="Category 2",
    )
    result = client["POST"](product)

    assertTrue(
        test_name="POST - Status code is 201",
        function_result=result["code"],
        expected=201,
    )
    assertTrue(
        test_name="POST - product created",
        function_result=result["data"].id,
        expected=2,
    )


test_post()


def test_post_validation_error():
    print("POST VALIDATION ERROR:")
    client = api()
    product = ProductIn(
        name="Procut 2",
        price=-1,
        category="Category 2",
    )
    result = client["POST"](product)

    assertTrue(
        test_name="POST VALIDATION ERROR - Status code is 422",
        function_result=result["code"],
        expected=422,
    )


test_post_validation_error()
