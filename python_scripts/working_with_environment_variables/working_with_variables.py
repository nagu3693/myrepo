#!/usr/local/bin/python3.6
import os
#stage = os.environ["STAGE"].upper()
stage = os.getenv("STAGE",default="dev").upper()
output = f"We are runnin in {stage}"
if stage.startswith("PROD"):
    output = "DANGER !!!! -" + output

print(output)
