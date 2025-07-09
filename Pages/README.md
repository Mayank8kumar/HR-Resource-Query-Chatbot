# HR Resource Query Chatbot

A Python-based chatbot designed to streamline and automate HR-related resource queries. This project aims to provide instant answers to frequently asked questions about HR policies, resources, and general employee support through a conversational interface.

## Features

- **Automated HR Query Resolution:** Quickly answers common HR questions for employees.
- **Extensible Knowledge Base:** Easily update or expand the chatbot's database of HR resources and FAQs.
- **Conversational Interface:** Seamless, interactive experience for end users.
- **Python Implementation:** Built entirely in Python for easy customization and integration.
- **Integration Ready:** Can be embedded into web apps, intranets, or messaging platforms.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Recommended: Virtual environment tool (`venv` or `virtualenv`)

### Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/Mayank8kumar/HR-Resource-Query-Chatbot.git
   cd HR-Resource-Query-Chatbot
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Start the FastAPI server:**
   ```bash
   python pages/Fast_api.py
   ```

2. **Interact with the chatbot via the provided API endpoints or using the web interface (if available).**

### API Documentation

- By default, FastAPI provides interactive docs at:
  - `http://127.0.0.1:8000/docs`
  - `http://127.0.0.1:8000/redoc`

## Project Structure

```
HR-Resource-Query-Chatbot/
├── pages/            # Contains Fast_api.py and other related modules
├── data/             # HR policy and FAQ data files
├── chatbot/          # Core chatbot logic and modules
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

For questions, feature requests, or support, please contact [Mayank8kumar](https://github.com/Mayank8kumar).
