IARRC Repository
================

To set up your environment:

1. Run "cd [Project Directory]"
2. Set up a Python 2 virtualenv using `virtualenv venv`
3. Enter the virtualenv using `source venv/bin/activate`
4. Install the dependencies using `pip install -r requirements.txt`
2. Install OpenCV from http://opencv.org

To work on the code:

1. Cd to the project directory
2. Enter the virtualenv using `source venv/bin/activate`
3. Do whatever you need to do

To deploy/run on the Raspberry Pi (Follow this EXACT order):

1. Plug the USB hub into the Portable Battery, then into the Raspberry Pi
2. Plug the Raspberry Pi into the Portable Battery
3. Plug in the Traxxas Battery to the ECS
4. Plug in the Arduino USB Cable
5. Plug the 9V battery into the Arduino
6. Go to https://vpn.remarkr.io/admin/current_users
7. Email me at andyilyas@gmail.com with the subject VPN Password to get the password (security)
8. Find the Pi's IP address (it's the one with user AIlyas)
9. Go to terminal, and type "ssh pi@[IP Address from Step 8]"
10. Congratulations, you're in! Do whatever you need to do.

To shutdown the Raspberry Pi:

1. Run "sudo shutdown -h now" in the Pi's command line, then wait a couple seconds
2. Unplug the Raspberry Pi from the Portable Battery
3. Press the E-Stop
4. Unplug the Traxxas Battery; Charge if needed
5. Unplug the USB hub from the Pi

Happy coding!
