from src import create_app
from dotenv import load_dotenv, find_dotenv
from src.solver.job_manager import process_jobs
import threading


load_dotenv(find_dotenv())
app = create_app()

if __name__ == '__main__':
    threading.Thread(target=process_jobs).start()
    app.run(debug=True)

