# Term Ontologies Django Project

## Description
This is a Django web application designed to function as a bilingual dictionary, currently supporting English to German and German to English term lookups. It provides definitions, synonyms, and translations by reading data directly from CSV files.

## Features
-   **Bilingual Search**: Search for terms in English to German or German to English.
-   **Definition Lookup**: Retrieves the definition of a searched term.
-   **Synonym Listing**: Displays synonyms associated with the term.
-   **Translation Display**: Shows translations for the searched term.
-   **CSV Data Source**: Terms and their related information are loaded dynamically from specified CSV files.

## Getting Started

### Prerequisites
-   Python 3.x
-   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/term_ontologies.git
    cd term_ontologies
    ```
    *(Note: Replace `https://github.com/your-username/term_ontologies.git` with the actual repository URL)*

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Data Files
This project relies on two CSV files located in the root directory:
-   `terms_english_to_german.csv`
-   `terms_german_to_english.csv`

Each CSV file is expected to have terms, definitions, synonyms (separated by '__________'), and translations.
The `searchTerm` view expects the format: `Term,Definition,Synonym1,Synonym2,...,__________,Translation1,Translation2,...`

### Running the Project

1.  **Apply database migrations (for Django's built-in apps):**
    ```bash
    python manage.py migrate
    ```
    *(Note: The `dictionary` app currently uses models from a default Django tutorial (`Question`, `Choice`) which are not actively used by the search functionality. You might consider removing these if they are not intended for future use.)*

2.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

3.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Project Structure
-   `term_ontologies/`: Main Django project configuration.
-   `dictionary/`: Django app containing core logic for the dictionary functionality (views, templates).
-   `terms_english_to_german.csv`: CSV file for English to German terms.
-   `terms_german_to_english.csv`: CSV file for German to English terms.
-   `manage.py`: Django's command-line utility.
-   `requirements.txt`: Python dependencies.

## Technologies Used
-   Python 3
-   Django 4.2.26
