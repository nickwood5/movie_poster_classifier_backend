from ninja import NinjaAPI
from movie_poster_classifier.views.debug.router import debug_router
from movie_poster_classifier.views.router import movie_poster_classifier_router

api = NinjaAPI()

api.add_router("/debug", debug_router)
api.add_router("/", movie_poster_classifier_router)
