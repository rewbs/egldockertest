import runpod
import subprocess

async def async_generator_handler(job):   
        process = subprocess.run(["eglinfo"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("STDOUT:", process.stdout)
        print("STDERR:", process.stderr)
        return "completed"

runpod.serverless.start({
  "handler": async_generator_handler, # Required
})
