# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Use the official Python 3 image as the base image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the content of the application directory to the app directory in the container
COPY application .

# Install the required pip modules
RUN pip install --no-cache-dir -r requirements.txt


# Define environment variables
ENV APIKEY="ENTER PD API KEY"
ENV APIKEY_REGION="US/EU"

# Set the command to run when the container starts
#CMD ["bash", "-i"]
CMD ["python", "-u", "main.py", "$API_KEY", "$API_KEY_REGION"]
