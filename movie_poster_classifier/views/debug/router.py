from ninja import Router
from movie_poster_classifier.views.debug.schema import PingResponse

debug_router = Router()


@debug_router.get("/ping")
def ping(
    request,
):
    return PingResponse(message="Hello World!")
