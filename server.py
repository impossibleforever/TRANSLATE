from app import create_app

app, limiter = create_app()

# Apply rate limit to specific routes
@limiter.limit("10 per minute")
def rate_limit_translate():
    pass

# Apply the rate limiter to the translate route
app.before_request(rate_limit_translate)
print("Server is running on port 5000")
print("Rate limit is 10 requests per minute")
if __name__ == '__main__':
    app.run(debug=True) 