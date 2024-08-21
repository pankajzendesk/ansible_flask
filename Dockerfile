FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy current directory contents into the container at /app
COPY . /app

# Install SSH client and Ansible
RUN apt-get update && \
    apt-get install -y ansible ssh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Ensure permissions are set correctly for SSH key
RUN touch /root/.ssh/known_hosts

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
