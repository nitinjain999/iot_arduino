import base64
import sys
from temboo.Library.Dropbox.Files import Upload
from temboo.core.session import TembooSession

print str(sys.argv[1])

# Encode image
with open(str(sys.argv[1]), "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

# Create a session with your Temboo account details
session = TembooSession("Temboo Account", "Name of Temboo App", "Temboo Application Key")

# Instantiate the Choreo
uploadChoreo = Upload(session)

# Get an InputSet object for the Choreo
uploadInputs = uploadChoreo.new_input_set()

# Set the Choreo inputs
#uploadInputs.set_Path("/test3.txt")
#uploadInputs.set_FileContent("Hello World")
uploadInputs.set_FileName(str(sys.argv[1]))
uploadInputs.set_AccessToken("Access token create with OAuth")
uploadInputs.set_FileContents(encoded_string)
uploadInputs.set_Root("sandbox")

# Execute the Choreo
uploadResults = uploadChoreo.execute_with_results(uploadInputs)

# Print the Choreo outputs
print("Response: " + uploadResults.get_Response())
