# TimeTree Parser
A Tkinter program designed to take in a .json file of your calander and return 3 graphs showing what labels, months and users have the most evenets tied to them

# Setup
Do the following to make the .json file

- Go to https://timetreeapp.com/signin
- Right click and select "inspect element"
- Go to "Recorder" and start a new recording
- Go to "Network"
- Select "preserve log"
- In the search bar of the "network" tab, type "sync"
- Log in
- (If you have multiple calanders and the one you want isn't the first one that shows up when logging in, see special case 1)
- You should see a few things popup called "sync" or "sync?since=", right click on all of these and select "copy response"

![Screenshot 2024-06-19 215307](https://github.com/levi-ivel/TimeTreeParser/assets/142150222/98361c99-9a40-4c71-aee5-73384b9e1153)

- Go into your IDE
- Put all responses into https://jsonlint.com and click "validate", then copy the results
- Make a .json file and copy paste all of the respones in
- (If you have multiple responses, see special case 2)
- Save the file and start up "parser.py"
- Cick on the "load json" button and select your .json file
- You will now be prompted to enter label names, go to "event label management" in TimeTree and fill in the label names, top to bottom. Leave the text field empty if you don't have a name for that label
- You will now be prompted to enter aurthor names, either search in the JSON what aurthor ID's make what events to find out who it is or put something random into the text field. Don't leave it empty
- Done!

## Special case 1
If you want to do this with a calander that doesn't immediately get loaded on login, do the following:

- Login
- Select the calander you want
- Copy the link in the search bar
- Log out
- Paste the link into the search bar
- Do the rest of the steps as normal

## Special case 2
If you have multiple responses you must do the following for it to work as intended:

- Paste the first response
- Go the the end of the file and make a line below the last brace

![image](https://github.com/levi-ivel/TimeTreeParser/assets/142150222/c8fa06b6-a3c9-4110-aefe-5a789694cfd9)

- Paste the second response in this line
- Go to the beginning of the second response (you can jump to it by clicking on the error that has popped up)
- Add a comma to the last brace of the first response
- Remove the highlighted text:

![image](https://github.com/levi-ivel/TimeTreeParser/assets/142150222/22629f0f-b198-4ad0-b3c0-a270f8c172ac)

- If you get an "end of file" error, remove this highlighted text aswell:

![image](https://github.com/levi-ivel/TimeTreeParser/assets/142150222/fcf99c72-baf8-408e-9799-56c3d4cd4db2)

- Repeat for every response
- Do the rest of the steps as normal


