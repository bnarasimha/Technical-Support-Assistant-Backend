# PicChatter Backend

Welcome to the PicChatter Backend, a FastAPI application that provides image description services.

## Features

- **Image Description**: Retrieve detailed descriptions of images using a specified API.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Requests

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/pic-chatter-backend.git
   cd pic-chatter-backend
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:

   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:

   - **Root Endpoint**: `GET /` - Returns a welcome message.
   - **Image Description Endpoint**: `GET /get_image_description` - Returns a description of the specified image.

## Configuration

- **API Key**: Ensure you have a valid API key for the image description service. Replace the placeholder in `main.py` with your actual API key.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
