from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = "secret_key"  # Required for flash messages

# Configure MongoDB URI (local MongoDB instance or Atlas)
app.config['MONGO_URI'] = "mongodb://localhost:27017/voting_system"  # Use your MongoDB URI
mongo = PyMongo(app)

# Predefined political parties
political_parties = ["Party A", "Party B", "Party C", "Party D"]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_candidate", methods=["GET", "POST"])
def add_candidate():
    if request.method == "POST":
        voter_id = request.form["voter_id"]
        candidate_name = request.form["candidate_name"]

        # Check if candidate already exists in MongoDB
        if mongo.db.candidates.find_one({"voter_id": voter_id}):
            flash(f"Voter ID '{voter_id}' already exists. Please enter a unique ID!")
        else:
            # Insert candidate into MongoDB
            mongo.db.candidates.insert_one({"voter_id": voter_id, "candidate_name": candidate_name})
            flash(f"Candidate '{candidate_name}' with Voter ID '{voter_id}' added successfully!")
        return redirect(url_for("index"))

    return render_template("add_candidate.html")


@app.route("/cast_vote", methods=["GET", "POST"])
def cast_vote():
    if request.method == "POST":
        voter_id = request.form["voter_id"]
        selected_party = request.form["selected_party"]

        # Check if the selected party is valid
        if selected_party in political_parties:
            # Update the vote count in MongoDB
            mongo.db.votes.update_one(
                {"party": selected_party},
                {"$inc": {"vote_count": 1}},
                upsert=True  # Create new if it doesn't exist
            )
            flash(f"Vote cast successfully for {selected_party}!")
        else:
            flash("Invalid party selection!")
        return redirect(url_for("index"))
    return render_template("cast_vote.html", political_parties=political_parties)


@app.route("/results")
def results():
    # Get the current votes from MongoDB
    candidates = {}
    for vote in mongo.db.votes.find():
        candidates[vote["party"]] = vote.get("vote_count", 0)
    return render_template("results.html", candidates=candidates)


if __name__ == "__main__":
    app.run(debug=True)
