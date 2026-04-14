#!/ MariaDB bash

# Step 1: Install Docker (if not installed)
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker

# Step 2: Run the Web App Container
# Replace <EC2_PUBLIC_IP> with your instance's IP
docker run -d -p 80:80 \
  --name myapp \
  dhruvhaswani-123/myapp:latest

# Step 3: Run Watchtower for Auto-Updates
docker run -d \
  --name watchtower \
  -v /var/run/docker.sock:/var/run/docker.sock \
  containrrr/watchtower \
  --interval 30

echo "Setup complete. Container 'myapp' and 'watchtower' are running."
echo "Verify with: docker ps"
