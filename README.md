# READ ME

## This program has three parts: 
1. load a txt file of Marcus Aurelius's Meditations from Project Gutenberg
2. Parse the text to generate a randomly selected meditation from a randomly selected book in the Meditations 
3. A call to the Slack API for a given channel in a given Slack workspace. The message posts with the book number and meditation number. 

## Additional Notes (why?)
Additionally, I have set this program up to execute once daily using a Windows Task Scheduler such that it will generate a "daily meditation" and post it to a "meditations" slack channel in my workspace. The program posts, in Slack lingo, "an ephemeral message". This is appropriate because in the Words of Marcus Aurelius, "all is ephemeral". 

