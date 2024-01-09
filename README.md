# Python Hotkey Project

This project is a Python application that uses a hotkey to trigger an AI call to the OpenAI API. It also includes a settings GUI for managing API keys and other settings.

## Setup

1. Clone the repository to your local machine.

2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory of the project and add your OpenAI API endpoint, API key, and model ID:

    ```env
    API_END_POINT=<your-api-endpoint>
    API_KEY=<your-api-key>
    MODEL_ID=<your-model-id>
    ```

## Usage

1. Run the settings GUI:

    ```sh
    python settings_gui.py
    ```

2. In the settings GUI, you can start the application by clicking the 'Start APP' button. This will start the hotkey listener.

3. Copy any text to your clipboard and press `<ctrl>+0` to trigger the AI call. The AI will process the text and return the result.

4. You can stop the application by clicking the 'Stop APP' button in the settings GUI.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
