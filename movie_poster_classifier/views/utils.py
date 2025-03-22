import torch
import torchvision.transforms as transforms
import os

# Load the pre-trained model and set it to evaluation mode
file_dir = os.path.dirname(os.path.abspath(__file__))
loaded_model = torch.load(f"{file_dir}/model.pt", weights_only=False)
loaded_model.eval()

# Define the class labels
classes = [
    "Action_Adventure",
    "Animation",
    "Comedy",
    "Documentary",
    "Drama",
    "Horror_Thriller",
    "Romance",
]

# Set transformation and data loader parameters
transform = transforms.Compose([transforms.ToTensor()])
batch_size = 1  # Assuming one image at a time
num_workers = 0  # No parallel workers needed for a single image


def create_dataloader(image):
    """
    Creates a DataLoader object for a given PIL Image.

    Args:
        image (PIL.Image.Image): The input image.

    Returns:
        DataLoader: A DataLoader for the image.
    """
    image_tensor = transform(image)
    poster_genres = ["none", "test"]
    dataset = [image_tensor, poster_genres]  # just a list of tensors

    dataloader = torch.utils.data.DataLoader(
        dataset, batch_size=batch_size, num_workers=num_workers, shuffle=False
    )

    return dataloader


def normalize_output(output):
    """
    Binarizes the output tensor.

    Args:
        output (torch.Tensor): The output predictions (logits or probabilities).

    Returns:
        torch.Tensor: A tensor of 0s and 1s based on a 0.5 threshold.
    """
    return (output >= 0.5).int()


def predict(image):
    """
    Predicts the genres of a movie poster.

    Args:
        image (PIL.Image.Image): The input image.

    Returns:
        list[str]: The list of predicted genre names.
    """
    image_tensor = transform(image).unsqueeze(0)  # Add batch dimension here
    outputs = loaded_model(image_tensor)
    outputs = torch.sigmoid(outputs).squeeze(0)
    outputs = normalize_output(outputs)

    predicted_genres = [classes[i] for i, val in enumerate(outputs) if val == 1]

    return predicted_genres
