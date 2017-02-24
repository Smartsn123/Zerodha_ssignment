# Introduction 
This app displays Nifty top 10 Gainers and Updates the Information every minute  .
This app is based on a cherry backend with redis as storage.
This app Uses CherryPy to Expose API to get Nifty top 10 and Uses Materialize HTML+CSS for frontend.
Javascript timed loop keeps updating the infromation by requesting to server after each timeout.
Python Thread Runs the two processes in different Thread and. Supervisor monior the running of the all over process.
This app has been deployed on http://13.54.210.62:8080/


#Running
To run do folllwing commands .
chmod +x requirements.sh
sudo ./requirements.sh


#Deployment and testing 
For local deployment:
$ supervisord -c supervisord.conf
$ supervisorctl update.

To stop supervisor, type:
$ supervisorctl shutdown

