# Advanced Backend Programming

- Localization and Internationalization Group 3

## Group Members

1. Nagasaro Ghislaine
2. Divine Nubuhoro
3. Shaday Sine
4. Patrick Mukunzi
5. Latjor Dak
6. Kosisochukwo Okeke

## How to run this project

1. Create a virtual environment

    ```python
    python3 -m venv venv
    ```

2. Install the requirements from the requirements.txt file

    ```bash
    pip install -r requirements.txt
    ```

3. Run the django app through your terminal

    ```bash
    python3 manage.py runserver
    ```

4. To see the different language selections, you need to change the language in the URL. For example:

    ```text
    http://localhost:8000/en/ #For English
    http://localhost:8000/fr/ #For French
    http://localhost:8000/es/ #For Spanish
    ```

5. To simulate a logged in user, you need to add the 'login_as' query parameter. For Example:

    ```text
    http://localhost:8000/en/?login_as=1
    http://localhost:8000/fr/?login_as=2
    ```

    **Note that there are only 4 possible users you can simulate**
