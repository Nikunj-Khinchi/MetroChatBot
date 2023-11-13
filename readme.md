## Ahmedabad Metro ChatBot

### Group 13

- Abhishek Bhagat S20210010005
- Nikunj Khinchi  S20210010159
- Swastik Mukati  S20210010221

### Overview
This project implements a chatbot for Ahmedabad Metro System using Natural Language Processing (NLP), The chatbot is designed to provide information and answer user queries related to the Ahmedabad Metro.

## Features

- **Data Preprocessing:**
  We performed data preprocessing on the input text to clean and standardize it for effective natural language understanding.

- **Data Creation:**
  The project involved the creation of a dataset tailored for the Ahmedabad Metro domain. This dataset is used for training the chatbot model.

- **Entity Recognition:**
  Entity recognition is a key component of the chatbot's understanding. It involves identifying and classifying entities such as names, locations, dates, etc., within the preprocessed text. This enhances the chatbot's ability to provide accurate and relevant information.

- **Similarity Coefficient:**
  The chatbot uses a similarity coefficient to measure the similarity between user input and predefined patterns. This helps in identifying the user's intent and retrieving appropriate responses.

- **Web Interface:**
  The chatbot is accessible through a web interface, allowing users to interact with it using a user-friendly form. Users can input queries related to the Ahmedabad Metro, and the chatbot will respond with relevant information.

## Technologies Used

- Python
- Django
- Natural Language Processing (NLP) techniques
- Web development technologies (for the web interface)

## How to Use

1. **Install Python**
    Make sure you have Python installed on your system. if not, you can download it from the offical Python Website

2. **Clone Repository**
    Clone this repository to your local machine using the following command:
    `git clone https://github.com/Nikunj-Khinchi/MetroChatBot.git`

3. **Install Dependencies:**
    Ensure you have the necessary dependencies installed. You can use the provided `requirements.txt` file. `pip install -r requirements.txt`

4. **Navigate**
    Navigate to the project directory
    `cd mysite`

5. **Start Application**
    Start the development server by running the following command:
    `python manage.py runserver`

Open your web browser and visit `http://localhost:8000` to access the application.