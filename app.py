def api():
    db: dict = {
        "data": [],
        "next_id": 1,
    }

    def get():
        return {
            "code": 200,
            "data": db["data"],
        }

    def create(number: int):
        if number in db["data"]:
            return {"code": 500, "error": f"{number} already exists"}

        db["data"].append(number)

        return {"code": 201, "data": db["data"]}

    return {
        "GET": get,
        "POST": create,
    }
