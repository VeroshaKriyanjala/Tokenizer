
# Tokenizer for In-house LLM

This repository contains the code for creating and managing a tokenizer for our in-house Language Model (LLM) project. 

## Prerequisites

Before running the project, ensure you have the following installed:
- Python 3.6 or later

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine by running the following command:

```bash
git clone https://github.com/VeroshaKriyanjala/Tokenizer.git
```

### 2. Set Up a Virtual Environment

Create a virtual environment to manage the dependencies:

#### For macOS/Linux:
```bash
python3 -m venv venv
```

#### For Windows:
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Activate the virtual environment:

#### For macOS/Linux:
```bash
source venv/bin/activate
```

#### For Windows:
```bash
venv\Scripts\activate
```

### 4. Install the Required Dependencies

Once the virtual environment is activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 5. Running the Project

Before you run the project you need to change ```codebase_path = "/home/verosha/Music/csi-sentinel" ``` in ```main.py``` with existing codebase in your local machine

To run the tokenizer, execute the following command:

```bash
python main.py
```

This will initialize and run the tokenizer for the LLM.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
