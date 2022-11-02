Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 16.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.3.7) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing
Your servers
Name	Username	IP	State	
8364-web-01	ubuntu	3.91.63.125	running	
8364-web-02	ubuntu	3.239.2.120	running	
8364-lb-01	ubuntu	3.231.220.245	running	
Tasks
0. Sign up for Datadog and install datadog-agent
mandatory
For this task head to https://www.datadoghq.com/ and sign up for a free Datadog account. When signing up, you’ll have the option of selecting statistics from your current stack that Datadog can monitor for you. Once you have an account set up, follow the instructions given on the website to install the Datadog agent.



Sign up for Datadog - Please make sure you are using the US website of Datagog (.com)
Install datadog-agent on web-01
Create an application key
Copy-paste in your Intranet user profile (here) your DataDog API key and your DataDog application key.
Your server web-01 should be visible in Datadog under the host name XX-web-01
You can validate it by using this API
If needed, you will need to update the hostname of your server
Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x18-webstack_monitoring
   
1. Monitor some metrics
mandatory
Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some monitors within the Datadog dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: System Check.



Set up a monitor that checks the number of read requests issued to the device per second.
Set up a monitor that checks the number of write requests issued to the device per second.
Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x18-webstack_monitoring
   
2. Create a dashboard
mandatory
Now create a dashboard with different metrics displayed in order to get a few different visualizations.

Create a new dashboard
Add at least 4 widgets to your dashboard. They can be of any type and monitor whatever you’d like
Create the answer file 2-setup_datadog which has the dashboard_id on the first line. Note: in order to get the id of your dashboard, you may need to use Datadog’s API
Repo:

GitHub repository: alx-system_engineering-devops
Directory: 0x18-webstack_monitoring
File: 2-setup_datadog
