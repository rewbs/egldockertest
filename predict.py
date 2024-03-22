from cog import BasePredictor
import subprocess

class Predictor(BasePredictor):

    def setup(self):
        pass

    def predict(self) -> str:
        process = subprocess.run(["eglinfo"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("STDOUT:", process.stdout)
        print("STDERR:", process.stderr)
        return "completed"