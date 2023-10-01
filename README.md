# README - FastAPI Redis Example

This repository contains an example of a FastAPI application that uses Redis for storing player data.

## Prerequisites

Before getting started, make sure you have Python 3.x installed on your system. You can download Python from the official website: https://www.python.org/downloads/

## Installation

1. Clone the repository to your computer:

```
git clone https://github.com/maurizio-cirilli/First_FastAPI_Project.git
```

2. Navigate to the project directory:


```bash
cd [project directory]
```

3. Create a Python virtual environment to isolate project dependencies:


```bash
python -m venv venv
```

4. Activate the virtual environment:

- On Windows:

  ```
  venv\Scripts\activate
  ```

- On macOS and Linux:

  ```
  source venv/bin/activate
  ```

5. Now that the virtual environment is active, install the required libraries using pip:

```bash
pip install fastapi
```

```bash
pip install "uvicorn[standard]"
```

```bash
pip install redis
```

## Configuration

Set in the config.py the variable HOST, PORT and PASSWORD with the DB connection parameters.

```python
HOST = ''
PORT = 17976
PASSWORD = ''
```

## Running the App

1. Make sure the virtual environment is activated.

2. Start the FastAPI app by running the following command:


```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The app will now be running at http://localhost:8000

## Usage

The application provides three main endpoints:

- `POST /player`: To save a new player.
- `GET /player/{id}`: To read data for a specific player.
- `DELETE /player/{id}`: To delete a specific player.

You can use an API client or tools like curl or Postman to interact with the application.

## References

- FastAPI Tutorial: https://fastapi.tiangolo.com/tutorial/
- Redis Documentation and Tutorials: https://redis.io/documentation

## License

This project is distributed under the GNU GENERAL PUBLIC LICENSE. See the [LICENSE](LICENSE) file for more details.







