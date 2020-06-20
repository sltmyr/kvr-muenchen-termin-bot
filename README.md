# kvr-muenchen-termin-bot

Script that periodically checks if a new appointment (termin) is available at the KVR Munich. Code inspired by https://github.com/okainov/munich-scripts.

The script checks every minute if an appointment at the "Führescheinstelle" of the KVR Munich (https://www.muenchen.de/rathaus/terminvereinbarung_fs.html) is available for the purpose of converting your driver's license to a german one. It can be adapted to check for different types of appointments, see the aforementioned repo. If an appointment becomes available, it publishes a message to an AWS SNS topic (https://aws.amazon.com/sns) which will notify me via SMS.

At the time of writing this (June 2020) it seems that this is the only way to actually get an appointment. We checked the website every day for a week an never saw any open appointment.
