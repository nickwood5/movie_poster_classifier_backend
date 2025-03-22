from ninja import Router
from ninja import File
from PIL import Image
from movie_poster_classifier.views.utils import predict
from ninja.files import UploadedFile
from rest_framework import status

movie_poster_classifier_router = Router()


@movie_poster_classifier_router.post("/classify/")
def predict_movie_genre(request, image: UploadedFile = File(...)):
    # Open the uploaded file as a PIL image
    if image.file is None:
        return status.HTTP_422_UNPROCESSABLE_ENTITY, {"detail": "Image not found"}
    try:
        pil_image = Image.open(image.file).convert("RGB")
        pil_image = pil_image.resize((182, 268))
    except Exception as e:
        return {"error": f"Invalid image file: {str(e)}"}

    # Run prediction using the previously defined function
    predicted_genres = predict(pil_image)

    return {"predicted_genres": predicted_genres}
