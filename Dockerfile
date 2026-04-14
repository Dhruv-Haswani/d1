FROM nginx:alpine

# Copy the static files to the nginx public directory
COPY index.html /usr/share/nginx/html/index.html
COPY style.css /usr/share/nginx/html/style.css

# Expose port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
