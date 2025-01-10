# Online Voting System

## ✨ Introduction
Welcome to the **Online Voting System** repository! This web application simulates a secure, automated voting process where users can register candidates, cast votes for political parties, and view live results. The system is built using **Flask** as the backend framework, **MongoDB** for data storage, and **HTML/CSS** for the front-end. 

It ensures smooth and accurate election management with unique voter IDs and real-time results.

## 🔍 Problem Domain
This project addresses the problem of managing an election process:
- Registering candidates with unique voter IDs.
- Casting votes for predefined political parties.
- Ensuring fair voting by using unique voter IDs.
- Displaying real-time election results based on the votes received.
The aim is to provide an efficient, digital solution to the traditional voting process.

## 💡 Solution Domain
The solution includes:
- **Candidate Registration**: Voters can register candidates with unique IDs.
- **Vote Casting**: Voters can cast their votes for predefined political parties.
- **Results Display**: View live vote counts for each party as votes are cast.
This system can be extended to accommodate additional features like real-time updates or more advanced election management.

## 🛠 Technology
- **Flask**: Web framework for building the backend of the application.
- **Flask-PyMongo**: A Flask extension to interact with MongoDB.
- **MongoDB**: NoSQL database for storing candidate and vote data.
- **HTML/CSS**: For building the web interface and styling the application.
- **Optional**: Bootstrap (can be added for responsive design).

## 🗂 Data Structure Used
- **MongoDB Collections**:
  - `candidates`: Stores candidate data, including `voter_id` and `candidate_name`.
  - `votes`: Tracks the number of votes for each political party (`party` and `vote_count`).

## 🧑‍💻 Methodology
### 1. **Candidate Registration**:
   - Users input a unique voter ID and candidate name.
   - The application ensures no duplicate voter IDs exist in the database.
   - Data is stored in the `candidates` collection.

### 2. **Vote Casting**:
   - Voters provide their voter ID and select a political party to vote for.
   - The app updates the `votes` collection, incrementing the vote count for the selected party.
   - Feedback is provided to the user through flash messages.

### 3. **Results Display**:
   - The results page fetches vote counts for each party from MongoDB and displays them in a structured format.

### 4. **User Interface**:
   - Simple, intuitive HTML forms for user interaction.
   - Styled using custom CSS to ensure a clean and responsive layout.

## 🏁 Conclusion
The **Online Voting System** simplifies election processes by automating candidate registration, vote casting, and result computation. It is built with scalable technologies (Flask and MongoDB) and provides a secure, user-friendly platform for elections.

Feel free to extend and adapt this system for your own use cases!
