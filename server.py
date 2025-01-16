from app import create_app

app, limiter = create_app()

# Apply rate limit to specific routes
@limiter.limit("10 per minute")
def rate_limit_translate():
    pass

# Apply the rate limiter to the translate route
app.before_request(rate_limit_translate)

if __name__ == '__main__':
    app.run(debug=True) 