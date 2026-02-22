# anki-multiplayer

## Plan: 
- Extract questions and answers: start with only MCQs
- Save correct answers and questions as a Mark Scheme with code abc
- Save each question and their set of potential answers as a Quiz with code abc
- Play the quiz in the console independently to confirm it goes through whole deck without repeating
- Add function to check if selected answers are correct (remove self marking unlike Anki)
- Track score and display at the end of the game
- Refactor to play game outside the console on HTML webpage
- Refactor to ask for input Anki text file (include error handling for incorrect files)
- Add local network multiplayer (practise this on phone and laptop)
- Display scores in a leaderboard among all players at the end of the deck
- Refactor until ideal (add more edge case tests, include nickname entry, game room codes)
- Dockerise for CI/CD?
- Host using Cloud which charges with usage, not with time 
