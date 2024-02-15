from src.rollasback.app import RollAsBack
from src.rollasback.redirect import Redirect, Blink
from src.rollasback.cookie import Cookie
from src.rollasback.http_response import HttpResponse

api = RollAsBack(name="Service1 API")
api.config["SECRET"] = "SECRET_KEY"


@api.endpoint("/user/{user_id}/{trialer_id}")
def user_endpoint(request):
    user_id = request.path_params
    query_params = request.query_params  # Get the query parameters
    api.print_log(f"User ID: {user_id}", level="INFO")
    return HttpResponse({"user_id": user_id, "query_params": query_params}, response_headers={}, status=200)


@api.endpoint("/asd")
def func(request):
    if request.method != "GET":
        response = HttpResponse("Method not allowed!", response_headers={}, status=405)
        response.set_cookie(cookie=Cookie(key="session_id", value="123456789", expires="2024-01-30", path="/app",
                                          domain="example.com", secure=True, httponly=True))
        return response
    return HttpResponse({"merhaba": "deneme"}, response_headers={}, status=200)


@api.endpoint("/redirect")
def redirect(request):
    api.print_log("Redirecting...", level="INFO")
    return Redirect("Redirect!", location="https://www.geeksforgeeks.org/redirecting-to-url-in-flask/", response_headers={}, status=302, blink_sec=5)

@api.endpoint("/blink")
def blink(request):
    api.print_log("Blinking...", level="INFO")
    return Blink("Blink!",location="https://www.geeksforgeeks.org/redirecting-to-url-in-flask/", response_headers={},blink_sec=5)


api.start_server(host="127.0.0.1", port=8888)
