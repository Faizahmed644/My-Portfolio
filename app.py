
from flask import Flask, render_template, request

app = Flask(__name__)

# Personal Profile
PROFILE = {
    "name": "Sahil ali",
    "role": "Python Developer in Training",
    "tagline": "I turn ideas into useful, creative digital experiences.",
    "about": (
        "I'm learning Python and building practical projects. "
        "I enjoy solving problems, exploring new technology, and turning "
        "what I learn into things people can use."
    ),
    "email": "faiz6023@gmail.com",
    "location": "Pakistan",
}

# Skills
SKILLS = [
    "Python",
    "Flask",
    "HTML",
    "CSS",
    "Problem Solving"
]

# Projects
PROJECTS = [
    {
        "number": "01",
        "title": "Billing System",
        "description": "A desktop billing application for entering products and calculating customer totals.",
        "tags": ["Python", "Tkinter"],
        "color": "peach",
    },
    {
        "number": "02",
        "title": "Portfolio Website",
        "description": "A responsive website that introduces me, highlights my skills, and showcases my work.",
        "tags": ["Flask", "HTML", "CSS"],
        "color": "lilac",
    },
    {
        "number": "03",
        "title": "Next Project",
        "description": "A space for the next idea I build and the lessons I learn along the way.",
        "tags": ["Learning", "Building"],
        "color": "mint",
    },
]


# Home Page
@app.route("/", methods=["GET", "POST"])
def home():

    message = ""

    if request.method == "POST":

        visitor_name = request.form.get("name", "").strip()
        visitor_email = request.form.get("email", "").strip()
        visitor_message = request.form.get("message", "").strip()

        if visitor_name and visitor_email and visitor_message:

            message = (
                "Thanks! The form works. "
                "Email sending has not been configured yet."
            )

        else:
            message = "Please fill in all three fields."

    return render_template(
        "index.html",
        profile=PROFILE,
        skills=SKILLS,
        projects=PROJECTS,
        message=message
    )


# Run Flask Application
if __name__ == "__main__":
    app.run(debug=True)
