from ninja import NinjaAPI
from movie_poster_classifier.views.debug.router import debug_router

api = NinjaAPI()

api.add_router("/debug", debug_router)
