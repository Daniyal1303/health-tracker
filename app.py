from flask import Flask,render_template

app = Flask(__name__)

posts = {
    1: {"id": 1, "title": "First Post", "content": "This is the content of the first post."},
    2: {"id": 2, "title": "Second Post", "content": "This is the content of the second post."}
}

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    post = posts.get(post_id)
    if not post:
        return "Post not found", 404
    return f'<h1>{post["title"]}</h1> <p>{post["content"]}</p>'

if __name__ == '__main__':
    app.run(debug=True)